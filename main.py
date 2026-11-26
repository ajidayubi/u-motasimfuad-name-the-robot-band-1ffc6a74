#!/usr/bin/env python3
"""Name the Robot Band: one funny robot band name plus its hit song.

The program writes a single funny line, under 200 characters, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt) and prints it.
Deterministic: the same fixed text on every run. No time, no randomness,
no network, no input read, no model call.
"""

import os

LINE = (
    "The Power Chords \u2014 hit single 'Unplugged' blacked out the whole "
    "arena, so the encore ran on one AA battery."
)


def _validate(line: str) -> None:
    """Mirror the competition gate: 1-200 characters, exactly one line."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if line.strip() != line or "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line, no surrounding whitespace")


def main() -> None:
    _validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Verify the file round-trips exactly: what the judge reads must be
    # byte for byte the line we validated, with no added newline.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError(f"entry.txt mismatch: wrote {len(LINE)} chars, read back {len(written)}")
    print(LINE)


if __name__ == "__main__":
    main()
