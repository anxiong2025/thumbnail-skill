# Thumbnail Skill

[English](README_EN.md) | 简体中文

一个面向 Codex 的社交媒体封面制作 Skill：使用用户提供的真实人物、产品和截图，按照小红书、视频号、YouTube、YouTube Shorts、抖音的常用比例完成设计、适配与质量检查。

> 当前版本：`v0.2.1`。首个真实成品已经作为风格演示加入；其中第三方人物、品牌和界面素材的授权状态未确认，因此不代表可商用。

## 核心能力

- 支持 5 个平台/内容预设和横竖屏适配。
- 区分“真实素材”“风格参考”“可生成装饰”，避免把参考图误当成可直接使用的素材。
- 真实截图、产品、Logo、数据和人物不会被 AI 重绘或替换。
- 支持标题区、真实拼图、人物抠图、白色到透明渐变等常用封面结构。
- 内置素材真实性、商业授权、可读性、尺寸和导出 QA 清单。
- 提供无第三方依赖的 Python 尺寸预设与 PNG/JPEG 校验脚本。
- 提供 10 类可复用风格编号、中英文提示词模板和提示词生成器。

## 缩略图示例

完整说明见 [风格目录](create-social-thumbnails/references/style-catalog.md)，可直接复制的版本见 [中文提示词库](PROMPTS.md)。

| 编号 | 预览效果 | 风格 | 适合内容 |
|---|---|---|---|
| `S01` | <a href="demos/S01-warm-handwritten-collage-6x7/preview.png"><img src="demos/S01-warm-handwritten-collage-6x7/preview.png" width="180" alt="S01 暖白手写拼贴缩略图"></a> | 暖白手写拼贴 | 资源包、模板、设计合集 |
| `S02` | 待补充 | 人物高点击 | 个人 IP、教程、反应类 |
| `S03` | 待补充 | 极简 UI 展示 | SaaS、App、Figma、工作流 |
| `S04` | 待补充 | 深色科技霓虹 | AI、编程、自动化、金融科技 |
| `S05` | 待补充 | 大数字清单 | 合集、排行榜、对比 |
| `S06` | 待补充 | 前后对比 | 改版、改造、测试结果 |
| `S07` | 待补充 | 新闻观点 | 热点、分析、知识解读 |
| `S08` | 待补充 | 高级杂志 | 品牌、访谈、思想内容 |
| `S09` | 待补充 | 活力贴纸 | 生活方式、教育、创作者技巧 |
| `S10` | 待补充 | 产品主视觉 | 新品、评测、电商 |

现有的 Figma 模板封面归为 **`S01 暖白手写拼贴`主风格 + `S02 人物高点击`辅助特征**。主编号使用 `S01`，因为最明显的识别元素是暖白纸张、手写大标题、橙蓝笔刷、真实界面拼贴和顶部渐变；人物负责增强点击力，但不是基础构图类型。查看 [完整 Demo 说明](demos/S01-warm-handwritten-collage-6x7/README.md)。

使用时只需指定“`S01 + 6:7`”或“`S02 + 16:9`”，再替换标题和真实素材。

## 平台预设

| 平台 | 默认画布 | 比例 | 说明 |
|---|---:|---:|---|
| 小红书 | 1080 × 1440 | 3:4 | 常用图文封面工作预设 |
| 视频号 | 1080 × 1260 | 6:7 | 常用信息流封面工作预设 |
| YouTube | 3840 × 2160 | 16:9 | 官方当前推荐尺寸 |
| YouTube Shorts | 2160 × 3840 | 9:16 | 官方当前推荐尺寸 |
| 抖音 | 1080 × 1920 | 9:16 | 常用竖版工作预设 |

平台界面会变化，小红书、视频号和抖音的尺寸在本项目中属于实用工作预设；发布前仍应检查当时 App 的裁切预览。YouTube 尺寸依据 [YouTube Help](https://support.google.com/youtube/answer/72431?hl=en)。

### 独立比例预设

不指定平台时，也可以直接生成这些比例：

| 比例 | 默认画布 | 常见用途 |
|---:|---:|---|
| `1:1` | 1080 × 1080 | 方形社交封面 |
| `4:3` | 1600 × 1200 | 横版展示、经典视频封面 |
| `3:4` | 1080 × 1440 | 竖版社交封面 |
| `4:5` | 1080 × 1350 | 竖版信息流 |
| `6:7` | 1080 × 1260 | 视频号式竖版封面 |
| `16:9` | 1920 × 1080 | 通用横版视频封面 |
| `9:16` | 1080 × 1920 | 全屏竖版视频封面 |

## 安装

运行 Skill 需要支持 Agent Skills 的 Codex。三个辅助脚本需要 Python 3.10 或更高版本，不依赖第三方 Python 包。

### 方法一：让 Codex 安装（推荐）

在 Codex 中输入：

```text
$skill-installer install the create-social-thumbnails skill from https://github.com/anxiong2025/thumbnail-skill/tree/main/create-social-thumbnails
```

安装后 Codex 通常会自动识别；如果没有出现，重启 Codex。

### 方法二：个人级安装

```bash
git clone https://github.com/anxiong2025/thumbnail-skill.git
mkdir -p ~/.agents/skills
cp -R thumbnail-skill/create-social-thumbnails ~/.agents/skills/
```

个人级 Skill 会对本机上的不同项目可用。

### 方法三：项目级安装

在目标项目根目录执行：

```bash
mkdir -p .agents/skills
cp -R /path/to/thumbnail-skill/create-social-thumbnails .agents/skills/
```

将 `.agents/skills/create-social-thumbnails` 提交到项目后，团队成员可在该项目中共同使用。以上安装位置依据 [OpenAI 官方 Skill 文档](https://learn.chatgpt.com/docs/build-skills)。

## 使用

在 Codex 中显式调用：

```text
$create-social-thumbnails
请用我提供的真实人物照片和产品截图，制作一张视频号 6:7 封面。
标题：400+ Figma 设计模板
副标题：可商用
风格：暖白手写感；标题下方用白色到透明渐变衔接真实拼图。
不要生成或重绘产品截图，也不要改变人物长相。
```

也可以直接描述任务；当请求与 Skill 的说明匹配时，Codex 可以自动选择它。

如果只想快速套用风格，可以打开 [PROMPTS.md](PROMPTS.md)，选择 `S01–S10` 后替换大括号里的标题、比例和素材说明。

### 建议提供的内容

- 目标平台和内容类型；
- 主标题、副标题或行动词；
- 必须原样使用的真实照片、截图、产品、Logo；
- 只用于参考的风格图；
- 品牌色、语气和希望输出的格式；
- 素材是否拥有公开或商业使用授权。

### 更多示例

```text
$create-social-thumbnails 用这张真人照片和三张真实界面截图做小红书 3:4 封面，给我文字主导和人物主导两个版本。
```

```text
$create-social-thumbnails 把这张视频号封面适配为 YouTube 16:9。保持人物和真实产品截图不变，重新安排层级，不要直接拉伸。
```

```text
$create-social-thumbnails 审核这张抖音封面：检查小图可读性、安全边距、人物抠图、素材真实性和商业授权表述，只给修改建议。
```

## 辅助脚本

查看预设：

```bash
python3 create-social-thumbnails/scripts/platform_presets.py --list
python3 create-social-thumbnails/scripts/platform_presets.py --list-ratios
python3 create-social-thumbnails/scripts/platform_presets.py --ratio 4:3 --json
python3 create-social-thumbnails/scripts/platform_presets.py --platform wechat --json
```

生成可编辑提示词：

```bash
python3 create-social-thumbnails/scripts/prompt_builder.py --list-styles
python3 create-social-thumbnails/scripts/prompt_builder.py --style S01 --ratio 16:9 --title "400+ Figma 设计模板" --platform YouTube
```

校验 PNG/JPEG：

```bash
python3 create-social-thumbnails/scripts/verify_thumbnail.py cover.png --platform wechat-channels
python3 create-social-thumbnails/scripts/verify_thumbnail.py cover.png --ratio 4:3
python3 create-social-thumbnails/scripts/verify_thumbnail.py cover.jpg --platform youtube --aspect-only
```

脚本仅检查文件和比例等技术条件，不能替代视觉、事实和授权审核。

## 项目结构

```text
thumbnail-skill/
├── README.md
├── README_EN.md
├── PROMPTS.md
├── PROMPTS_EN.md
├── LICENSE
├── demos/
│   └── README.md
└── create-social-thumbnails/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/README.md
    ├── references/
    │   ├── asset-integrity.md
    │   ├── composition-patterns.md
    │   ├── platform-specs.md
    │   ├── qa-checklist.md
    │   └── style-catalog.md
    └── scripts/
        ├── platform_presets.py
        ├── prompt_builder.py
        └── verify_thumbnail.py
```

## Demo 规范

后续案例放在 [`demos/`](demos/)；每个 Demo 必须包含平台、尺寸、输入素材、输出文件、复现步骤和 `LICENSE-ASSETS.md`。用户私有照片、未授权名人照片、第三方模板和字体不能直接加入公开仓库。

## 许可与“可商用”说明

本项目的代码和工作流依据 [MIT License](LICENSE) 发布。MIT License **不自动覆盖** Demo 图片、用户上传照片、人物肖像、品牌 Logo、软件界面截图、字体、第三方模板或外部生成服务产物。

只有当封面内每一项素材的权利都已确认时，才应宣称成品“可商用”。本项目提供的是制作 SOP 和校验机制，不构成法律意见。

## 参与改进

欢迎提交 Issue 或 Pull Request。新增平台预设时，请说明来源和检查日期；新增 Demo 时，请先补齐素材授权说明，并确保不会泄露个人信息。
