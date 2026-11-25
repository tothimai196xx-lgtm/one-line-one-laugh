#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single self-contained funny line (93 characters, well under the
140-character gate) to /output/entry.txt.

The joke: a two-beat escalation. The setup is a relatable failure
(houseplants died), the fix is a plastic replacement, and the punchline is
that the guilt survives the fix — the narrator now feels guilty for not
watering plants that cannot be watered. Concrete image, real turn, no
explanation needed.
"""

import os

LINE = "My houseplants died, so I bought plastic ones \u2014 now I feel guilty for not watering those too."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
