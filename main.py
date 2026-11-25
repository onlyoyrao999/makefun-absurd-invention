#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — the Self-Blaming Toaster.

First draft pitched a crumb-eating couch robot, but the joke landed flat:
a robot that eats crumbs is just a Roomba with a grudge. The toaster is
funnier because the absurdity is the product itself — it burns your toast
on purpose, then makes the bread apologise, so breakfast takes the blame.
"""

import os
import sys

LINE = "The Self-Blaming Toaster burns your toast on purpose, then prints a tearful apology letter signed by the bread itself, so you can finally blame breakfast instead of admitting you forgot it again."
MAX_CHARS = 220


def validate(line):
    """The gate: one sentence, 1 to 220 characters, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    return line


def main() -> None:
    line = validate(LINE)
    print(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Read back and confirm what landed is exactly the pitch.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        if f.read().strip() != line:
            print("verification failed: entry.txt does not match the pitch",
                  file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
