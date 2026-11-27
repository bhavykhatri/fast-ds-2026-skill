#!/usr/bin/env python3
"""Merge, decrypt and compress PDFs for the e-Filing portal (5 MB per file).

Requires: pip install pymupdf

Usage
  python compress_pdf.py out.pdf in1.pdf in2.pdf ... [--password PAN]
  python compress_pdf.py out.pdf scanned.pdf --dpi 96 --quality 60

Never commit or share the password; pass it on the command line or via the
PDF_PASSWORD environment variable.
"""
import argparse
import os
import sys

try:
    import fitz  # pymupdf
except ImportError:
    sys.exit("pip install pymupdf")

LIMIT = 5 * 1024 * 1024


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("out")
    p.add_argument("inputs", nargs="+")
    p.add_argument("--password", default=os.environ.get("PDF_PASSWORD"))
    p.add_argument("--dpi", type=int, default=96)
    p.add_argument("--quality", type=int, default=60)
    a = p.parse_args()

    out = fitz.open()
    for path in a.inputs:
        doc = fitz.open(path)
        if doc.needs_pass:
            if not a.password or not doc.authenticate(a.password):
                sys.exit(f"{path}: password required or wrong")
        out.insert_pdf(doc)
    try:
        out.rewrite_images(dpi_threshold=a.dpi + 4, dpi_target=a.dpi, quality=a.quality)
    except AttributeError:
        print("pymupdf too old for rewrite_images; saving without image compression")
    out.save(a.out, garbage=4, deflate=True)
    size = os.path.getsize(a.out)
    flag = "OK" if size <= LIMIT else "TOO LARGE - lower --dpi/--quality or split"
    print(f"{a.out}: {out.page_count} pages, {size / 1048576:.2f} MB ({flag})")


if __name__ == "__main__":
    main()
