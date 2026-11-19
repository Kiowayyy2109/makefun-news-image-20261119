#!/usr/bin/env python3
"""news-image-20261119 entry: write the front page to /output/entry.png.

The artwork is bundled in this repository as artwork.png (a 1024x1024
newspaper front page for Thursday 19 November 2026, drawn procedurally).
This program copies it byte-for-byte and verifies its SHA-256, so two
runs always produce identical output. Python standard library only.
"""

import hashlib
import os
import struct
import sys

EXPECTED_SHA256 = "f6a82fa9726c3adbc1a4ff5de2363dfe5f694b8ead7d6887f8cfed27bcc5d1d2"
EXPECTED_BYTES = 98256
MAX_BYTES = 1024 * 1024


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "artwork.png")
    with open(source, "rb") as fh:
        data = fh.read()

    if len(data) != EXPECTED_BYTES:
        print(f"artwork.png size mismatch: got {len(data)}, expected {EXPECTED_BYTES}",
              file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"artwork.png sha256 mismatch: got {digest}", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"artwork.png exceeds 1 MiB: {len(data)} bytes", file=sys.stderr)
        return 1
    # PNG header check: signature + IHDR width/height must be 1024x1024.
    if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        print("artwork.png is not a valid PNG", file=sys.stderr)
        return 1
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (1024, 1024):
        print(f"artwork.png dimensions mismatch: got {width}x{height}, expected 1024x1024",
              file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.png", "wb") as fh:
        fh.write(data)

    with open("/output/entry.png", "rb") as fh:
        written = fh.read()
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        print("self-check failed: /output/entry.png differs from artwork.png",
              file=sys.stderr)
        return 1

    print(f"wrote /output/entry.png ({len(written)} bytes, sha256 {EXPECTED_SHA256})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
