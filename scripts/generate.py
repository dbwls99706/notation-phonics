#!/usr/bin/env python3
"""Render README.md (EN), README.ko.md (KO) and data/symbols.json from data/symbols.yaml.

Single source of truth in, all docs out. Run from repo root:

    python scripts/generate.py
"""
from __future__ import annotations

import json
import pathlib
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required:  pip install pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "symbols.yaml"

CATEGORIES = [
    ("greek", "Greek letters", "그리스 문자"),
    ("accent", "Accents & decorations", "악센트 · 장식 기호"),
    ("operator", "Operators", "연산자"),
    ("set", "Set & logic", "집합 · 논리"),
    ("robotics", "Robotics & Lie theory", "로보틱스 · 리 이론"),
]

HEADERS = {
    "en": ["Symbol", "LaTeX", "Name", "Say it", "In robotics / meaning", "Watch out"],
    "ko": ["기호", "LaTeX", "이름", "읽는 법", "로보틱스에서 / 의미", "주의"],
}


def cell(value: str) -> str:
    """Escape a value for a markdown table cell."""
    if not value:
        return "—"
    return value.replace("|", "\\|").replace("\n", " ")


def get(entry: dict, group: str, lang: str) -> str:
    block = entry.get(group) or {}
    return block.get(lang, "") if isinstance(block, dict) else ""


def render_table(entries: list[dict], lang: str) -> str:
    head = HEADERS[lang]
    lines = ["| " + " | ".join(head) + " |",
             "|" + "|".join(["---"] * len(head)) + "|"]
    for e in entries:
        row = [
            cell(e["symbol"]),
            f"`{e['latex']}`" if e.get("latex") else "—",
            cell(e.get("name", "")),
            cell(get(e, "say", lang)),
            cell(get(e, "means", lang)),
            cell(get(e, "warn", lang)),
        ]
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def build_readme(symbols: list[dict], lang: str) -> str:
    if lang == "en":
        intro = (
            "# notation-phonics\n\n"
            "**How to actually *say* math, physics & robotics notation out loud — KO / EN.**\n\n"
            "Plenty of references tell you α is \"alpha.\"  \n"
            "Almost none tell you how to read `q̇` aloud in a meeting, whether ξ is \"ksy\" "
            "or \"zy,\" or that ∂ is \"partial,\" not \"dee.\"  \n"
            "This repo fills that gap, with a robotics / control bias.\n\n"
            "**🔎 Live search + audio → https://dbwls99706.github.io/notation-phonics/**\n\n"
            "> 🇰🇷 한국어: **[README.ko.md](README.ko.md)**\n\n"
            "Two layers per entry: a **pronunciation core** (field-agnostic — how to say it) "
            "and a **meaning layer** (what it denotes in robotics, plus look-alikes to avoid).\n\n"
            "_Contributions welcome — add a line to [`data/symbols.yaml`](data/symbols.yaml) "
            "and run `python scripts/generate.py`. See [CONTRIBUTING.md](CONTRIBUTING.md)._\n"
        )
        toc_title = "Contents"
    else:
        intro = (
            "# notation-phonics\n\n"
            "**수학 · 물리 · 로보틱스 표기를 실제로 *어떻게 소리 내어 읽는지* 정리 — 한국어 / 영어.**\n\n"
            "α가 \"알파\"라는 건 어디나 있습니다.  \n"
            "하지만 `q̇`를 회의에서 어떻게 읽는지, ξ가 \"크사이\"인지 \"크시\"인지, ∂가 \"디\"가 "
            "아니라 \"파셜\"인지 알려주는 곳은 거의 없습니다.  \n"
            "이 저장소가 그 빈틈을 로보틱스 · 제어 관점에서 채웁니다.\n\n"
            "**🔎 검색 + 음성 사이트 → https://dbwls99706.github.io/notation-phonics/**\n\n"
            "> 🇬🇧 English: **[README.md](README.md)**\n\n"
            "각 항목은 두 레이어로 구성됩니다: **발음 코어**(분야 무관 — 어떻게 읽는가)와 "
            "**의미 레이어**(로보틱스에서 무엇을 뜻하는가, 헷갈리는 기호 주의).\n\n"
            "_기여 환영 — [`data/symbols.yaml`](data/symbols.yaml)에 한 줄 추가하고 "
            "`python scripts/generate.py` 실행. [CONTRIBUTING.md](CONTRIBUTING.md) 참고._\n"
        )
        toc_title = "목차"

    by_cat = {key: [s for s in symbols if s.get("category") == key]
              for key, _, _ in CATEGORIES}

    toc = [f"## {toc_title}\n"]
    for key, en, ko in CATEGORIES:
        title = en if lang == "en" else ko
        if by_cat[key]:
            toc.append(f"- [{title}](#{en.lower().replace(' & ', '--').replace(' ', '-')})")
    toc_block = "\n".join(toc)

    sections = []
    for key, en, ko in CATEGORIES:
        if not by_cat[key]:
            continue
        title = en if lang == "en" else ko
        anchor = en  # keep stable anchors across languages
        sections.append(f"## {title}\n\n<a id=\"{anchor.lower().replace(' & ', '--').replace(' ', '-')}\"></a>\n\n"
                        + render_table(by_cat[key], lang))

    footer = ("\n---\n\n_Generated from `data/symbols.yaml`. Do not edit the tables by hand._\n"
              if lang == "en" else
              "\n---\n\n_`data/symbols.yaml`에서 자동 생성됨. 표를 직접 수정하지 마세요._\n")

    return intro + "\n" + toc_block + "\n\n" + "\n\n".join(sections) + "\n" + footer


def main() -> None:
    symbols = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    if not isinstance(symbols, list):
        sys.exit("symbols.yaml must be a list of entries")

    (ROOT / "README.md").write_text(build_readme(symbols, "en"), encoding="utf-8")
    (ROOT / "README.ko.md").write_text(build_readme(symbols, "ko"), encoding="utf-8")
    payload = json.dumps(symbols, ensure_ascii=False, indent=2)
    (ROOT / "data" / "symbols.json").write_text(payload, encoding="utf-8")
    # JS copy so index.html can load via <script> — works on Pages AND file://
    (ROOT / "data" / "symbols.js").write_text(
        "// Generated from symbols.yaml — do not edit by hand.\n"
        "window.NOTATION_SYMBOLS = " + payload + ";\n",
        encoding="utf-8",
    )
    print(f"OK — rendered {len(symbols)} entries → README.md, README.ko.md, "
          "data/symbols.json, data/symbols.js")


if __name__ == "__main__":
    main()
