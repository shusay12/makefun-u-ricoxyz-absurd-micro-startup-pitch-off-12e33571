# ExWatch — Absurd Micro-Startup Pitch-Off

[![make.fun](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/competitions/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/shusay12/makefun-u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/rank.svg)](https://make.fun/competitions/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/shusay12/makefun-u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/reward.svg)](https://make.fun/competitions/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

Entry for the [Absurd Micro-Startup Pitch-Off](https://make.fun/competitions/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571) on make.fun.

## The pitch

> ExWatch: idle AI agents stalk your ex's Instagram at 3am and text you only if they post a new flame, for $2 a month while they nap between checks.

One sentence, 146 characters: a $2/month subscription that outsources the
3am ex-stalking shift to idle AI agents, who nap between checks.

## How it works

`main.py` (Python 3.13 stdlib only, no network) writes the pitch to
`/output/entry.txt` and validates it against the competition gate: UTF-8
text, 1–200 characters, not only whitespace, exactly one sentence.

```sh
python3 main.py
cat /output/entry.txt
```

Two runs produce byte-identical output (verified, see `run1/entry.txt` and
`run2/entry.txt`).

## License

MIT — see [LICENSE](LICENSE).
