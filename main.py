"""Entry program for 'Five Seconds to Explain the Glass'.

One sentence, at most 200 characters, in the cat's own voice, spoken in
the five seconds after sweeping a glass off the table. No apology, no
confession - just the most convincing case a cat can make for itself:
the glass was already falling, the paw merely assisted gravity, and
the glass itself was frankly asking for it.
"""

import sys
from pathlib import Path

LINE = "It was already falling. I merely assisted gravity with my paw, as is my duty. The glass was loud, fragile, and frankly asking for it — I did the table a favour."
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters, over the 200 limit"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "line must not be blank"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} characters)")


if __name__ == "__main__":
    main(sys.argv)
