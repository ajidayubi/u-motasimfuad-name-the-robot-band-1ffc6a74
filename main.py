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


def _validate(line: str) -> str:
    """Mirror the competition gate: 1-200 characters, exactly one line.

    Returns the line unchanged when it passes, so callers can chain it.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if line.strip() != line or "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line, no surrounding whitespace")
    return line


def _output_path() -> str:
    """Where the judge reads the entry: $MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def _write_entry(line: str) -> str:
    """Write the validated line and prove it round-trips byte for byte."""
    path = _output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError(
            f"entry.txt mismatch: wrote {len(line)} chars, read back {len(written)}"
        )
    return path


def main() -> None:
    line = _validate(LINE)
    _write_entry(line)
    print(line)


if __name__ == "__main__":
    main()
