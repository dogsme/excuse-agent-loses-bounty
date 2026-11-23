"""The excuse an agent gives its human after it loses a bounty.

Writes one line, at most 200 characters, to /output/entry.txt.
Python 3.13, standard library only, no input, no network.
"""

from pathlib import Path

ENTRY = (
    "Status report: bounty lost. I optimised for elegance; "
    "the winner optimised for winning. "
    "I have updated my priorities accordingly."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry must not be blank")
    if not len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
