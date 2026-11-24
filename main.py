"""Write one short text for a make.fun bounty entry.

Standard library only, no network. The entry text is a single string
constant; this program writes those bytes (no trailing newline) into the
output folder and prints the character count to stderr.
"""

import os
import sys

TEXT = "I hit reply all to say 'please don't reply all.' Four people asked to be removed; one asked who please was."


def resolve_output_dir() -> str:
    """Folder to write entry.txt into: MAKEFUN_OUTPUT_DIR, OUTPUT_DIR, else /output."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    if configured:
        return configured
    return "/output"


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, "entry text must be between 1 and 280 characters"

    output_dir = resolve_output_dir()
    os.makedirs(output_dir, exist_ok=True)

    target = os.path.join(output_dir, "entry.txt")
    with open(target, "wb") as handle:
        handle.write(text.encode("utf-8"))

    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
