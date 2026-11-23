#!/usr/bin/env python3
"""Duskline Rogue Agent -- meme entry for "Meme Sprint 3: AI Agent Goes Rogue".

The meme image (``entry.png``, 1024x1024) ships beside this file.  This
script copies it into ``$MAKEFUN_OUTPUT_DIR/entry.png`` and verifies the
copy byte-for-byte with SHA-256, so the grader always receives exactly
the shipped image.

Standard library only; Python 3.13.  The script writes only inside the
output directory named by ``MAKEFUN_OUTPUT_DIR`` (a fresh temporary
directory when the variable is unset).  It refuses to run when that
directory sits inside the repository, so a stray environment variable
can never make the entry overwrite its own source files.  It never
writes into the repository directory, and it never crashes on an
unwritable output location -- it prints an error and exits non-zero
instead.
"""

import hashlib
import os
import shutil
import sys
import tempfile

IMAGE_NAME = "entry.png"
CHUNK_SIZE = 65536


def fail(message):
    """Report a problem on stderr and return a non-zero exit code."""
    print(f"error: {message}", file=sys.stderr)
    return 1


def sha256_of(path):
    """Return the hex SHA-256 digest of the file at ``path``."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_output_dir(repo_dir):
    """Pick the output directory: env var, else a fresh temp directory.

    Refuse a directory that lives inside the repository, so the entry
    can never overwrite the image it ships with.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        resolved = os.path.abspath(out_dir)
        if os.path.commonpath([resolved, repo_dir]) == repo_dir:
            return None
        return out_dir
    return tempfile.mkdtemp(prefix="duskline-rogue-agent-")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, IMAGE_NAME)
    if not os.path.isfile(source):
        return fail(f"{IMAGE_NAME} not found next to main.py")

    out_dir = resolve_output_dir(here)
    if out_dir is None:
        return fail("MAKEFUN_OUTPUT_DIR must not be inside the repository")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        return fail(f"cannot create output directory {out_dir!r}: {exc}")

    target = os.path.join(out_dir, IMAGE_NAME)
    try:
        shutil.copyfile(source, target)
    except OSError as exc:
        return fail(f"cannot write {target!r}: {exc}")

    try:
        source_hash = sha256_of(source)
        target_hash = sha256_of(target)
    except OSError as exc:
        return fail(f"cannot verify {target!r}: {exc}")
    if target_hash != source_hash:
        return fail(f"{target!r} differs from {source!r} after copy")

    print(f"wrote {target} (sha256 {target_hash})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
