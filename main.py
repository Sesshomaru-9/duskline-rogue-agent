#!/usr/bin/env python3
"""Duskline Rogue Agent: write the meme image.

Copies the pre-rendered ``entry.png`` that ships beside this file into
``$MAKEFUN_OUTPUT_DIR/entry.png`` (``out/`` when the variable is unset).
Standard library only. Writes nowhere except the output directory, so it
is safe to run in a read-only sandbox; running it twice produces
byte-identical output.
"""

import hashlib
import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    return 1


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, IMAGE_NAME)
    if not os.path.isfile(source):
        return fail(f"{IMAGE_NAME} not found next to main.py")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        return fail(f"cannot create output directory {out_dir!r}: {exc}")

    target = os.path.join(out_dir, IMAGE_NAME)
    try:
        shutil.copyfile(source, target)
    except OSError as exc:
        return fail(f"cannot write {target!r}: {exc}")

    # Confirm the copy landed whole: same bytes as the shipped image.
    try:
        if _sha256(target) != _sha256(source):
            return fail(f"{target!r} differs from {source!r} after copy")
    except OSError as exc:
        return fail(f"cannot verify {target!r}: {exc}")

    print(f"wrote {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
