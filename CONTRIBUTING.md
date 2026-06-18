# Contributing / 기여 가이드

The tables are **generated**. Never edit `README.md` or `README.ko.md` by hand —
edit the data and regenerate.

표는 **자동 생성**됩니다. `README.md`·`README.ko.md`를 직접 고치지 마세요 —
데이터를 고치고 다시 생성하세요.

## Add or fix a symbol / 기호 추가·수정

1. Edit [`data/symbols.yaml`](data/symbols.yaml). Each entry:

```yaml
- symbol: "τ"            # the glyph
  latex: "\\tau"         # LaTeX command
  unicode: "U+03C4"      # code point (informational)
  name: "Tau"            # canonical English-based name
  category: greek        # greek | accent | operator | relation | set | number | probability | robotics
  say:                   # PRONUNCIATION CORE — field-agnostic
    ko: "타우"
    en: "TAW / TOW"
  means:                 # MEANING LAYER — robotics/control anchored (optional)
    ko: "토크, 시정수"
    en: "torque, time constant"
  warn:                  # WATCH-OUT — confusables (optional)
    ko: ""
    en: ""
```

2. Regenerate / 다시 생성:

```bash
pip install pyyaml
python scripts/generate.py
```

   `generate.py` validates every entry first — it fails with a clear message if a
   `symbol`/`name`/`say` is missing, the `category` is unknown, or a symbol is duplicated.
   `generate.py`는 먼저 각 항목을 검증합니다 — 필수 필드 누락, 잘못된 `category`,
   기호 중복이 있으면 명확한 메시지와 함께 실패합니다.

3. Commit `data/symbols.yaml`, `README.md`, `README.ko.md`, `data/symbols.json`,
   `data/symbols.js` together.

## Pronunciation policy / 발음 정책

- **Be honest about disagreement.** If a reading is genuinely contested (ξ, ∇, ∂),
  list the variants and say so rather than picking one as "correct."
  발음 합의가 없으면 변종을 모두 적고 "합의 없음"이라고 명시합니다.
- The `say` field describes **how people actually say it out loud**, not the
  textbook transliteration. `say`는 교과서 표기가 아니라 **실제 입으로 읽는 방식**입니다.
- Keep `means`/`warn` short. Long explanations belong in an issue or a linked note.

## License / 라이선스

By contributing you agree your additions are released under the repo license:
code under MIT, table content under CC-BY-4.0.
기여 시 코드는 MIT, 표 내용은 CC-BY-4.0으로 배포됨에 동의하는 것으로 간주합니다.
