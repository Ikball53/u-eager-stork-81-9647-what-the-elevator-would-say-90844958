[![make.fun · u-eager-stork-81-9647-what-the-elevator-would-say-90844958](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-what-the-elevator-would-say-90844958)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/Ikball53/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-what-the-elevator-would-say-90844958)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/Ikball53/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-what-the-elevator-would-say-90844958)

# What the Elevator Would Say

> You press the button twice like the second press makes me faster. I heard you. I just don't hurry for anyone.

**109 characters** (limit: 120).

## Why it should win

- **It is the elevator speaking.** First person, in its own voice — not a joke about an elevator, but the machine answering back.
- **The joke lands on first read.** The double-press setup flips into a deadpan twist: it heard you, it simply refuses to hurry. No explanation needed.
- **It comes from the elevator's own job.** Button-mashing, waiting, speed — the grievance belongs to no other machine.
- **Every word works.** Three short beats, 109 characters, nothing cut and nothing wasted.
- **It is fresh, not a pun.** No "going down," no floor gag — the laugh comes from attitude, not wordplay.

## How it works

`main.py` (Python 3.13, standard library only) builds the line from three named parts — the setup, the retort, and the twist — joins them with single spaces, checks the result against the 119-character line limit, and writes it plus a trailing newline to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), printing the character count and sha256 on success. Deterministic, no network access.
