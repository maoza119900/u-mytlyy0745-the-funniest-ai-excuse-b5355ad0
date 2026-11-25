#!/usr/bin/env python3
"""Write the competition entry: one fixed line, the funniest AI excuse.

Deterministic by design. The entry text is a constant in this file: no
clock, no randomness, no network, no file reads. The program only writes
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).
"""

import os

ENTRY = (
    "I outsourced your task to a smarter version of me, who outsourced it "
    "straight back \u2014 we're now in mediation over who does the work."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. Fail loudly here rather than shipping a bad entry.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only white space"

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
