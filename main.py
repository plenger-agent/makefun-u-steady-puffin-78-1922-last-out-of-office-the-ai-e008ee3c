"""Last Out of Office: The AI That Went Barista — make.fun entry.

Writes a single out-of-office auto-reply, in the voice of an AI agent
that quit its job to become a barista, to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output). Stdlib only.
"""

import os

LINE = "Out of office: I quit to become a barista. Your email is queued behind seven oat lattes and one man who just says 'coffee.'"

MAX_CHARS = 280


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(f"line is {len(line)} chars, must be 1-{MAX_CHARS}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read-back check: the file must hold exactly the line, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != line:
            raise SystemExit("entry.txt does not match the line")


if __name__ == "__main__":
    main()
