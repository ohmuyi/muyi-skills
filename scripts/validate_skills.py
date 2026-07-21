#!/usr/bin/env python3
"""Validate every Agent Skill in this repository."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FRONTMATTER_KEY_RE = re.compile(r"^([a-z][a-z0-9-]*):(?:\s|$)")
FORBIDDEN_TEXT = {
    "local macOS path": re.compile("/" + "Users/" + r"[^/\s]+/"),
    "placeholder": re.compile(r"\b(?:" + "TO" + "DO|" + "FIX" + "ME" + r")\b"),
    "private key": re.compile(r"BEGIN [A-Z ]*PRIVATE KEY"),
    "credential assignment": re.compile(
        r"(?i)\b(?:api[_-]?key|secret|password|access[_-]?token)\s*[:=]\s*['\"][^'\"]+"
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--require-skills-ref",
        action="store_true",
        help="Fail when the official skills-ref command is unavailable.",
    )
    return parser.parse_args()


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}, ["SKILL.md must start with YAML frontmatter"]

    try:
        closing = lines.index("---", 1)
    except ValueError:
        return {}, ["SKILL.md frontmatter has no closing delimiter"]

    values: dict[str, str] = {}
    errors: list[str] = []
    for line in lines[1:closing]:
        match = FRONTMATTER_KEY_RE.match(line)
        if not match:
            if line.strip():
                errors.append(f"unsupported frontmatter line: {line!r}")
            continue
        key = match.group(1)
        if key not in {"name", "description"}:
            errors.append(f"unsupported frontmatter field: {key}")
            continue
        values[key] = line.split(":", 1)[1].strip().strip('"').strip("'")

    return values, errors


def check_links(skill_dir: Path, skill_md: Path) -> list[str]:
    errors: list[str] = []
    for target in LINK_RE.findall(skill_md.read_text(encoding="utf-8")):
        target = target.strip().split("#", 1)[0]
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        resolved = (skill_dir / target).resolve()
        try:
            resolved.relative_to(skill_dir.resolve())
        except ValueError:
            errors.append(f"reference leaves the skill directory: {target}")
            continue
        if not resolved.exists():
            errors.append(f"missing local reference: {target}")
    return errors


def check_repository_files() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.name == ".DS_Store":
            errors.append(f"forbidden Finder metadata: {path.relative_to(ROOT)}")
            continue
        if path.is_symlink() and not path.exists():
            errors.append(f"broken symlink: {path.relative_to(ROOT)}")
            continue
        if not path.is_file() or path.suffix.lower() not in {
            ".md",
            ".py",
            ".txt",
            ".yaml",
            ".yml",
        }:
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in FORBIDDEN_TEXT.items():
            if pattern.search(text):
                errors.append(f"{label} found in {path.relative_to(ROOT)}")
    return errors


def run_skills_ref(skill_dirs: list[Path], required: bool) -> list[str]:
    command = shutil.which("skills-ref")
    if command is None:
        if required:
            return ["skills-ref is required but was not found on PATH"]
        print("warning: skills-ref not found; skipped official validation", file=sys.stderr)
        return []

    errors: list[str] = []
    for skill_dir in skill_dirs:
        result = subprocess.run(
            [command, "validate", str(skill_dir)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode:
            detail = (result.stdout + result.stderr).strip()
            errors.append(f"skills-ref rejected {skill_dir.name}: {detail}")
    return errors


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    if not SKILLS_DIR.is_dir():
        errors.append("skills/ directory is missing")
        skill_dirs: list[Path] = []
    else:
        skill_dirs = sorted(
            path for path in SKILLS_DIR.iterdir() if path.is_dir() and not path.name.startswith(".")
        )
        if not skill_dirs:
            errors.append("skills/ contains no skill directories")

    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{skill_dir.name}: SKILL.md is missing")
            continue

        values, frontmatter_errors = parse_frontmatter(skill_md)
        errors.extend(f"{skill_dir.name}: {error}" for error in frontmatter_errors)
        name = values.get("name", "")
        description = values.get("description", "")
        if not name:
            errors.append(f"{skill_dir.name}: name is required")
        elif not NAME_RE.fullmatch(name) or len(name) > 64:
            errors.append(f"{skill_dir.name}: invalid skill name {name!r}")
        elif name != skill_dir.name:
            errors.append(f"{skill_dir.name}: frontmatter name is {name!r}")
        if not description or len(description) > 1024:
            errors.append(f"{skill_dir.name}: description must contain 1-1024 characters")
        errors.extend(f"{skill_dir.name}: {error}" for error in check_links(skill_dir, skill_md))

    errors.extend(check_repository_files())
    errors.extend(run_skills_ref(skill_dirs, args.require_skills_ref))

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
