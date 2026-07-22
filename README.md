# muyi-skills

`muyi-skills` 是一组由 ohmuyi 维护、遵循 [Agent Skills specification](https://agentskills.io/specification) 的跨平台 Agent Skills。每个 Skill 都以独立目录发布，并通过 `SKILL.md` 与按需加载的 references、scripts 或 assets 提供可复用能力。

## 安装

```bash
npx skills add ohmuyi/muyi-skills
```

安装工具会发现仓库中的 Skill，并通过交互界面选择要安装的 Skill 和目标 Agent。

## Skills

| Skill | 用途 |
| --- | --- |
| [`muyi-portrait-tang`](skills/muyi-portrait-tang/) | 将简短关键词扩写为新中式唐风成年中国女性单人或双人人像中文提示词，未指定人数时默认单人。 |

## 基本用法

安装后，可以显式调用 `$muyi-portrait-tang`，也可以直接提出与唐风单人独照、双人古风人像、闺阁闺蜜合照、花榻俯拍、对镜簪花、帘影逆光或雾感柔光提示词相关的请求。

这个 Skill 只生成提示词，不直接调用图像生成工具，不处理参考图编辑，也不生成视频提示词。它支持一位或两位成年中国女性，未指定人数时默认一位；“合照”与“闺蜜照”等语义按两位处理，零人、三人以上、多人或群像暂不支持。涉及衣着、姿态和镜头语言时保持成年、非露骨和非窥视表达。

## 开发与贡献

新增或修改 Skill 前，请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。仓库会在 pull request 和 `main` 分支更新时自动检查目录命名、frontmatter、文件引用和通用 Agent Skills 规范。

安全问题请遵循 [SECURITY.md](SECURITY.md)，不要通过公开 Issue 披露尚未修复的漏洞。

## License

本仓库采用 [Apache License 2.0](LICENSE)。
