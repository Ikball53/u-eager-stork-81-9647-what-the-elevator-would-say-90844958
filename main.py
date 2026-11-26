#!/usr/bin/env python3
"""What the Elevator Would Say — one-liner entry.

The elevator answers the passenger who mashes the call button twice.
Composed from named parts so the line is built, not pasted.
Standard library only, deterministic, no network access.
"""

import hashlib
import os
import sys

# The passenger's habit: pressing twice, as if repetition adds speed.
SETUP = "You press the button twice like the second press makes me faster."

# The elevator's deadpan reply: it heard the passenger just fine.
RETORT = "I heard you."

# The twist: the delay is not deafness, it is policy.
TWIST = "I just don't hurry for anyone."

MAX_CHARS = 119  # line itself; entry.txt adds one trailing newline (120 total)


def build_line() -> str:
    """Assemble the elevator's line from its three beats."""
    parts = [SETUP, RETORT, TWIST]
    return " ".join(parts)


def main() -> int:
    line = build_line()
    if len(line) > MAX_CHARS:
        print(f"line too long: {len(line)} chars (max {MAX_CHARS})", file=sys.stderr)
        return 1

    target = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    out_path = target if target.endswith(".txt") else os.path.join(target, "entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")

    digest = hashlib.sha256((line + "\n").encode("utf-8")).hexdigest()
    print(f"chars: {len(line)}")
    print(f"sha256: {digest}")
    print(f"wrote: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
