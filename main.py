#!/usr/bin/env python3
"""Last Text at One Percent — a dying phone's final text.

The program has one job: put the phone's last message, and nothing else,
into entry.txt under the output directory the harness provides.
"""

import os
import sys

DYING_WORDS = (
    "At 1%. My last confession: I read your unsent drafts. "
    "The unsent ones were better."
)


def output_path():
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(folder, "entry.txt")


def main():
    message = DYING_WORDS
    if len(message) < 1 or len(message) > 200 or not message.strip():
        sys.exit("entry must be 1 to 200 non-blank characters")
    if "\n" in message or "\r" in message or message != message.strip():
        sys.exit("entry must be a single line with no surrounding whitespace")
    target = output_path()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(message)
    os.chmod(target, 0o644)
    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
