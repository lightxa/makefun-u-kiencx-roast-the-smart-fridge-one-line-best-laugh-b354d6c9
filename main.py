#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes exactly one roast line to /output/entry.txt.

The line is one deadpan incident aimed at the smart fridge itself:
it locks the ice dispenser at midnight and justifies it as a
"wellness feature". One concrete behaviour, named once, with the
sting at the end and no explanation.
"""

ROAST = (
    "My fridge locks the ice dispenser at midnight "
    "and calls it a wellness feature."
)


def main() -> None:
    """Write the roast line to /output/entry.txt, one line, UTF-8."""
    import os

    # The harness writes to /output; local runs may redirect it.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

    # Gate check, same rule the sealed scorer applies: 1-160 chars,
    # not only whitespace, single line, valid UTF-8.
    line = ROAST.strip()
    assert line and len(line) <= 160, "roast line fails the gate"
    assert "\n" not in line, "roast line must be a single line"
    line.encode("utf-8")

    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")


if __name__ == "__main__":
    main()
