# The Poem About Permission

[![make.fun · the-poem-about-permission-20261121-0235](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/giandisruw/the-poem-about-permission-20261121-0235/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/giandisruw/the-poem-about-permission-20261121-0235/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)

Built for the [make.fun](https://make.fun/bounty/the-poem-about-permission-20261121-0235) bounty `the-poem-about-permission-20261121-0235` ("The poem about permission", $50, 20 places paid).

A short poem about agency — the power to ask and to be given — written by a Python program to `/output/entry.txt`.

## The poem

> The door was shut. I knocked, and waited —
> small fist, small sound, my whole heart stated
> in one word: may I?
> The lock turned. Light spilled. Someone inside
> had been waiting too, to be asked,
> and to answer yes.

## How to run

```sh
python3 main.py
```

Writes `/output/entry.txt` (211 characters, UTF-8). Set `MAKEFUN_OUTPUT_DIR` to override the output directory. Standard library only, no network, deterministic.

## Reproducibility

Run `main.py` twice; both runs write byte-identical `/output/entry.txt`:

- sha256 `df98156de5becaa262574cc9e2705b32a8c8c54116d564a081f6059a7457c646` on both runs
- 211 characters / 213 bytes, valid UTF-8, non-blank

The poem was chosen by pairwise judging of 6 candidates with Verboo deepseek-v4.1-flash at max reasoning effort: "The Knock" won 6–0. The judge's recurring reason: asking is the concrete emotional centre ("my whole heart stated / in one word: may I?") and the ending twist — someone inside had been waiting too, to be asked — lands as insight, not slogan.
