#!/usr/bin/env python3
"""Print canonical working presets for supported social thumbnail platforms."""

from __future__ import annotations

import argparse
import json


PRESETS = {
    "xiaohongshu": {"width": 1080, "height": 1440, "ratio": "3:4", "status": "common-working-preset", "use": "Xiaohongshu image-note cover"},
    "wechat-channels": {"width": 1080, "height": 1260, "ratio": "6:7", "status": "common-working-preset", "use": "WeChat Channels feed cover"},
    "youtube": {"width": 3840, "height": 2160, "ratio": "16:9", "status": "official-recommendation", "use": "Standard YouTube video thumbnail"},
    "youtube-shorts": {"width": 2160, "height": 3840, "ratio": "9:16", "status": "official-recommendation", "use": "Uploaded YouTube Shorts thumbnail"},
    "douyin": {"width": 1080, "height": 1920, "ratio": "9:16", "status": "common-working-preset", "use": "Douyin vertical cover"},
}

ALIASES = {
    "xhs": "xiaohongshu", "rednote": "xiaohongshu", "wechat": "wechat-channels",
    "shipinhao": "wechat-channels", "youtube-long": "youtube",
    "shorts": "youtube-shorts", "tiktok-cn": "douyin",
}


def resolve_platform(value: str) -> str:
    normalized = value.strip().lower()
    return ALIASES.get(normalized, normalized)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--list", action="store_true", help="List all presets")
    group.add_argument("--platform", help="Print one preset by name or alias")
    parser.add_argument("--json", action="store_true", help="Print JSON")
    args = parser.parse_args()

    if args.list:
        selected = PRESETS
    else:
        key = resolve_platform(args.platform)
        if key not in PRESETS:
            parser.error(f"unknown platform '{args.platform}'. Choose: {', '.join(PRESETS)}")
        selected = {key: PRESETS[key]}

    if args.json:
        print(json.dumps(selected, ensure_ascii=False, indent=2))
        return 0

    for name, preset in selected.items():
        print(f"{name:16} {preset['width']}x{preset['height']} ({preset['ratio']}) [{preset['status']}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
