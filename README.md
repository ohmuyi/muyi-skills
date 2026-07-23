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
| [`muyi-portrait-office-siren`](skills/muyi-portrait-office-siren/) | 将关键词或“随机一组”扩写为现代 Office Siren 风格的成年东亚女性单人肖像中文提示词。 |

## 基本用法

安装后，可以显式调用 `$muyi-portrait-tang`，也可以直接提出与唐风单人独照、双人古风人像、闺阁闺蜜合照、花榻俯拍、对镜簪花、帘影逆光或雾感柔光提示词相关的请求。

这个 Skill 只生成提示词，不直接调用图像生成工具，不处理参考图编辑，也不生成视频提示词。它支持一位或两位成年中国女性，未指定人数时默认一位；“合照”与“闺蜜照”等语义按两位处理，零人、三人以上、多人或群像暂不支持。涉及衣着、姿态和镜头语言时保持成年、非露骨和非窥视表达。

`muyi-portrait-tang` 采用单文件结构。除通过安装工具使用外，也可以将其 [`SKILL.md`](skills/muyi-portrait-tang/SKILL.md) 全文作为 system 或 developer instruction 提供给支持长上下文的其他对话模型。

安装后，可以显式调用 `$muyi-portrait-office-siren`，并指定场景、姿势、发型与妆面变体、服装面料与袖型、短裙或包臀半裙、兼容外搭、道具、色盘、光线或构图；只说“随机一组”时，Skill 会自动生成一套连贯且避开固定模板的方案。这里的 Office Siren 指源自现代职场与都市时装语境的冷艳海妖风美学，场景可以扩展到酒吧、酒店、公寓、画廊、机场休息室等现代空间，不是神话海妖或海洋奇幻题材。

这个 Skill 只生成一位成年东亚女性的七段结构化中文提示词，不直接调用图像生成工具，不处理参考图编辑，也不生成视频提示词。它充分吸收托腮交腿、扶镜低头抬眼、靠窗回头、前倾俯视和桌边侧坐五种参考原型；每套造型固定包含白色深 V 修身上衣、黑色高腰短裙或包臀半裙、黑色半透丝袜和黑色尖头高跟鞋，并通过场景、姿势、面料、裙型、发型、妆面、道具、光色和机位保持创造性。成像固定为超写实真人摄影，使用中性偏冷白平衡和冷白 CCD 直闪突出明亮通透、保留极浅冷粉血色与真实微纹理的冷白皮，避免暖色环境把面部、手臂和丝袜下腿部染黄或压暗。

`muyi-portrait-office-siren` 同样采用单文件结构，可以将其 [`SKILL.md`](skills/muyi-portrait-office-siren/SKILL.md) 全文独立提供给支持长上下文的其他对话模型。

## 开发与贡献

新增或修改 Skill 前，请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。仓库会在 pull request 和 `main` 分支更新时自动检查目录命名、frontmatter、文件引用和通用 Agent Skills 规范。

安全问题请遵循 [SECURITY.md](SECURITY.md)，不要通过公开 Issue 披露尚未修复的漏洞。

## License

本仓库采用 [Apache License 2.0](LICENSE)。
