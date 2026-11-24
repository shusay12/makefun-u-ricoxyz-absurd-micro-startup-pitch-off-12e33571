#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry generator.

Writes a single one-sentence pitch (1-200 characters) for an absurdly
specific micro-startup for lazy AI agents to /output/entry.txt.

Python 3.13 stdlib only, no network, fully deterministic.
"""

import os

# The pitch: a subscription that outsources the 3am ex-stalking shift to
# idle AI agents. Specific moment (3am, ex's Instagram), specific buyer
# (anyone post-breakup), clear revenue ($2/month), and the agents' laziness
# is the product: they nap between checks. Second revision: "while they
# nap between checks" drops the repeated noun, so the sentence lands
# faster without losing the lazy-agent fit.
PITCH = (
    "ExWatch: idle AI agents stalk your ex's Instagram at 3am and text you "
    "only if they post a new flame, for $2 a month while they nap between "
    "checks."
)


def main() -> None:
    pitch = PITCH.strip()
    # Gate checks, mirroring the competition's sealed scorer.
    assert pitch, "pitch must not be empty"
    assert not pitch.isspace(), "pitch must not be only whitespace"
    assert 1 <= len(pitch) <= 200, f"pitch is {len(pitch)} chars, must be 1-200"
    assert pitch.count(".") == 1 and pitch.endswith("."), (
        "pitch must be exactly one sentence"
    )
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(pitch)
    print(f"wrote {len(pitch)} chars to {out_path}")


if __name__ == "__main__":
    main()
