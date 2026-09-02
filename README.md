# Thumbnail Skill

[English](README_EN.md) | 简体中文

一个面向 Codex 的社交媒体封面制作 Skill：使用用户提供的真实人物、产品和截图，按照小红书、视频号、YouTube、YouTube Shorts、抖音的常用比例完成设计、适配与质量检查。

> 当前版本：`v0.1.0`。Demo 将在素材授权信息完整后加入；初始版本不使用假界面或 AI 替代人物充数。

## 核心能力

- 支持 5 个平台/内容预设和横竖屏适配。
- 区分“真实素材”“风格参考”“可生成装饰”，避免把参考图误当成可直接使用的素材。
- 真实截图、产品、Logo、数据和人物不会被 AI 重绘或替换。
- 支持标题区、真实拼图、人物抠图、白色到透明渐变等常用封面结构。
- 内置素材真实性、商业授权、可读性、尺寸和导出 QA 清单。
- 提供无第三方依赖的 Python 尺寸预设与 PNG/JPEG 校验脚本。

## 平台预设

| 平台 | 默认画布 | 比例 | 说明 |
|---|---:|---:|---|
| 小红书 | 1080 × 1440 | 3:4 | 常用图文封面工作预设 |
| 视频号 | 1080 × 1260 | 6:7 | 常用信息流封面工作预设 |
| YouTube | 3840 × 2160 | 16:9 | 官方当前推荐尺寸 |
| YouTube Shorts | 2160 × 3840 | 9:16 | 官方当前推荐尺寸 |
| 抖音 | 1080 × 1920 | 9:16 | 常用竖版工作预设 |

平台界面会变化，小红书、视频号和抖音的尺寸在本项目中属于实用工作预设；发布前仍应检查当时 App 的裁切预览。YouTube 尺寸依据 [YouTube Help](https://support.google.com/youtube/answer/72431?hl=en)。

## 安装

运行 Skill 需要支持 Agent Skills 的 Codex。两个辅助脚本需要 Python 3.10 或更高版本，不依赖第三方 Python 包。

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
    │   └── qa-checklist.md
    └── scripts/
        ├── platform_presets.py
        └── verify_thumbnail.py
```

## Demo 规范

后续案例放在 [`demos/`](demos/)；每个 Demo 必须包含平台、尺寸、输入素材、输出文件、复现步骤和 `LICENSE-ASSETS.md`。用户私有照片、未授权名人照片、第三方模板和字体不能直接加入公开仓库。

## 许可与“可商用”说明

本项目的代码和工作流依据 [MIT License](LICENSE) 发布。MIT License **不自动覆盖** Demo 图片、用户上传照片、人物肖像、品牌 Logo、软件界面截图、字体、第三方模板或外部生成服务产物。

只有当封面内每一项素材的权利都已确认时，才应宣称成品“可商用”。本项目提供的是制作 SOP 和校验机制，不构成法律意见。

## 参与改进

欢迎提交 Issue 或 Pull Request。新增平台预设时，请说明来源和检查日期；新增 Demo 时，请先补齐素材授权说明，并确保不会泄露个人信息。
