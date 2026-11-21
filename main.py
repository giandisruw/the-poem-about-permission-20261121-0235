#!/usr/bin/env python3
"""Entry for make.fun bounty the-poem-about-permission-20261121-0235.

Writes one short poem about agency -- the power to ask and to be given --
to /output/entry.txt (UTF-8, 1-280 characters). Standard library only,
no network, deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

POEM = (
    "The door was shut. I knocked, and waited —\n"
    "small fist, small sound, my whole heart stated\n"
    "in one word: may I?\n"
    "The lock turned. Light spilled. Someone inside\n"
    "had been waiting too, to be asked,\n"
    "and to answer yes.\n"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = POEM
    assert 1 <= len(text) <= 280, f"poem is {len(text)} chars, must be 1-280"
    assert text.strip(), "poem must not be only whitespace"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
