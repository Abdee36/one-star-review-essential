#!/usr/bin/env python3
"""One-star review of something essential.

Writes a single deadpan one-star review (one line, <=160 chars) to
/output/entry.txt for make.fun's "One-Star Review of Something Essential"
bounty. Stdlib only, no network.
"""

import os

REVIEW = "One star. My pillow is cool for four minutes, then warm for the rest of the night, whichever side I turn it to."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
