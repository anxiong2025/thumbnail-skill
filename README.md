# 自媒体爆款封面 Skill

[English](README_EN.md) | 简体中文

用真实人物、真实产品和真实截图，快速制作适合小红书、视频号、抖音、YouTube 和 YouTube Shorts 的高点击缩略图与自媒体封面。

> **真实素材 × 爆款结构 × 多平台比例 × 可复制提示词**

无需从空白画布开始：说出你想要的风格（例如“暖白手写拼贴”）、指定比例、上传素材并替换标题，即可让 Codex 按完整 SOP 制作和检查封面。`S01–S10` 只是目录索引，可省略。

> 当前版本：`v0.3.4`。“爆款”表示以提高信息流点击吸引力为目标的设计方法，不代表或保证播放量、点击率与商业结果。首个真实成品已经作为风格演示加入；其中第三方人物、品牌和界面素材的授权状态未确认，因此不代表可商用。

## 核心能力

- 内置 10 类自媒体爆款封面结构，覆盖人物、产品、知识、资源、热点和 UI 展示。
- 围绕“一秒看懂主题、小图仍可读、真实证据突出”建立点击导向的视觉层级。
- 支持 5 个平台/内容预设和横竖屏适配。
- 区分“真实素材”“风格参考”“可生成装饰”，避免把参考图误当成可直接使用的素材。
- 真实截图、产品、Logo、数据和人物不会被 AI 重绘或替换。
- 支持标题区、真实拼图、人物抠图、白色到透明渐变等常用封面结构。
- 内置素材真实性、商业授权、可读性、尺寸和导出 QA 清单。
- 提供无第三方依赖的 Python 尺寸预设与 PNG/JPEG 校验脚本。
- 提供中英文可复制提示词模板和提示词生成器。

## 缩略图示例

完整说明见 [风格目录](create-social-thumbnails/references/style-catalog.md)。表格中的 Prompt 是可直接复制修改的大概示例；上传真实素材后，把标题、比例和内容换成自己的即可。

| 编号 | 预览效果 | 风格 | 适合内容 | Prompt 示例 |
|---|---|---|---|---|
| `S01` | <a href="demos/S01-warm-handwritten-collage-6x7/preview.png"><img src="demos/S01-warm-handwritten-collage-6x7/preview.png" width="180" alt="S01 暖白手写拼贴缩略图"></a> | 暖白手写拼贴 | 资源包、模板、设计合集 | `$create-social-thumbnails 暖白手写拼贴，6:7；暖白手写标题，下方使用真实截图拼图和真人抠图，标题下加白色渐变，不生成假素材。` |
| `S02` | 待补充 | 人物高点击 | 个人 IP、教程、反应类 | `$create-social-thumbnails 人物高点击，16:9；真人占画面约 40%，使用强对比短标题，背景只保留一张真实结果图。` |
| `S03` | 待补充 | 极简 UI 展示 | SaaS、App、Figma、工作流 | `$create-social-thumbnails 极简 UI 展示，4:3；浅色留白背景，以一张真实产品界面为主，最多加入两张辅助卡片。` |
| `S04` | 待补充 | 深色科技霓虹 | AI、编程、自动化、金融科技 | `$create-social-thumbnails 深色科技霓虹，16:9；近黑背景搭配一种霓虹色，突出真实仪表盘或代码界面，不虚构数据。` |
| `S05` | 待补充 | 大数字清单 | 合集、排行榜、对比 | `$create-social-thumbnails 大数字清单，3:4；把数量做成最大元素，下方排列 3–6 个真实案例，只保留一处强调标记。` |
| `S06` | 待补充 | 前后对比 | 改版、改造、测试结果 | `$create-social-thumbnails 前后对比，16:9；用真实前后图做左右对比，保持对应裁切，清楚标记改造前后。` |
| `S07` | 待补充 | 新闻观点 | 热点、分析、知识解读 | `$create-social-thumbnails 新闻观点，16:9；采用真实事件图片和简短事实角度，不虚构引用或未经证实的结论。` |
| `S08` | 待补充 | 高级杂志 | 品牌、访谈、思想内容 | `$create-social-thumbnails 高级杂志，4:5；中性低饱和背景，高清人物或产品搭配衬线标题和大面积留白。` |
| `S09` | 待补充 | 活力贴纸 | 生活方式、教育、创作者技巧 | `$create-social-thumbnails 活力贴纸，3:4；使用真实人物或产品，搭配原创涂鸦、胶带和两到三种强调色。` |
| `S10` | 待补充 | 产品主视觉 | 新品、评测、电商 | `$create-social-thumbnails 产品主视觉，1:1；放大真实产品，以核心收益作主标题，使用干净品牌背景和自然光影。` |

现有的 Figma 模板封面归为 **`S01 暖白手写拼贴`主风格 + `S02 人物高点击`辅助特征**。主编号使用 `S01`，因为最明显的识别元素是暖白纸张、手写大标题、橙蓝笔刷、真实界面拼贴和顶部渐变；人物负责增强点击力，但不是基础构图类型。查看 [完整 Demo 说明](demos/S01-warm-handwritten-collage-6x7/README.md)。

使用时直接写“暖白手写拼贴 + 6:7”或“人物高点击 + 16:9”，再替换标题和真实素材；也可以自由组合描述，编号可省略。

## 热门平台推荐比例

| 平台 | 推荐画布 | 比例 | 适用内容 |
|---|---:|---:|---|
| 小红书 | 1080 × 1440 | 3:4 | 图文笔记、知识分享、产品种草 |
| 视频号 | 1080 × 1260 | 6:7 | 视频号信息流封面 |
| YouTube | 3840 × 2160 | 16:9 | 常规横版视频缩略图 |
| YouTube Shorts | 2160 × 3840 | 9:16 | Shorts 竖版缩略图 |
| 抖音 | 1080 × 1920 | 9:16 | 全屏竖版短视频封面 |

平台界面会变化，小红书、视频号和抖音的尺寸在本项目中属于实用工作预设；发布前仍应检查当时 App 的裁切预览。YouTube 尺寸依据 [YouTube Help](https://support.google.com/youtube/answer/72431?hl=en)。

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

如果只想快速套用风格，直接复制“缩略图示例”表格中的 Prompt，再补充标题和上传素材即可。

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
python3 create-social-thumbnails/scripts/verify_thumbnail.py cover.jpg --platform youtube --aspect-only
```

脚本仅检查文件和比例等技术条件，不能替代视觉、事实和授权审核。

## 项目结构

```text
thumbnail-skill/
├── README.md
├── README_EN.md
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

后续案例放在 [`demos/`](demos/)；每个 Demo 必须包含平台、尺寸、输入素材、输出文件、复现步骤和 `LICENSE-ASSETS.md`。公开 Demo 应优先使用自有或已授权素材；若仓库所有者明确加入授权未确认的风格示例，必须单独标注、排除在 MIT License 之外，并且不得宣称可商用。

## 许可与“可商用”说明

本项目的代码和工作流依据 [MIT License](LICENSE) 发布。MIT License **不自动覆盖** Demo 图片、用户上传照片、人物肖像、品牌 Logo、软件界面截图、字体、第三方模板或外部生成服务产物。

只有当封面内每一项素材的权利都已确认时，才应宣称成品“可商用”。本项目提供的是制作 SOP 和校验机制，不构成法律意见。

## 参与改进

欢迎提交 Issue 或 Pull Request。新增平台预设时，请说明来源和检查日期；新增 Demo 时，请先补齐素材授权说明，并确保不会泄露个人信息。
