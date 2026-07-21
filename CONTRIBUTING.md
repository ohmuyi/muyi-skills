# 贡献指南

感谢你改进 `muyi-skills`。本仓库接受新 Skill、现有 Skill 修订、reference 修正和校验工具改进。

## 新增 Skill

1. 在 `skills/<skill-name>/` 中创建 Skill。
2. 将入口文件命名为 `SKILL.md`。
3. 保证目录名与 frontmatter 的 `name` 完全一致。
4. `name` 只使用小写字母、数字和连字符，长度不超过 64 个字符，不以连字符开头或结尾，也不包含连续连字符。
5. `description` 同时说明“做什么”和“何时使用”，长度不超过 1024 个字符。
6. 仅在确有需要时增加 `references/`、`scripts/` 或 `assets/`，不要创建空目录或在单个 Skill 内添加 README、CHANGELOG、安装指南。

## 内容约定

- 保持 `SKILL.md` 精简，把详细知识、变体和长示例放入一层深度的 reference。
- 从 `SKILL.md` 使用相对于 Skill 根目录的路径直接引用资源，不建立多级引用链。
- 不写入本机绝对路径、密钥、私人测试素材或特定 Agent 才能理解的必需配置。
- 新增脚本时说明依赖、处理错误，并在提交前实际执行代表性测试。
- 不提交生成输出、缓存、编辑器文件或 `.DS_Store`。

## 校验

在仓库根目录运行：

```bash
python3 scripts/validate_skills.py
```

如已安装官方 `skills-ref`，校验脚本会同时调用它。CI 会要求官方校验器存在并验证所有 Skill。

## Pull request

1. 从最新 `main` 创建独立分支。
2. 只提交与当前修改有关的文件。
3. 说明修改目的、行为影响和测试方式。
4. 等待 `validate-skills` 检查通过后再合并。
5. 使用 squash merge，并在合并后删除功能分支。
