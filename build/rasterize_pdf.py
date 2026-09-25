"""Rasterize each page of the final PDF to PNG for visual QA review."""
import sys
from pathlib import Path
import pymupdf  # pip package: pymupdf

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "build" / "SOC_SLA_Reality_neshboy.pdf"
OUT_DIR = ROOT / "assets" / "screenshots"


def main():
    pdf_path = Path(sys.argv[1]) if len(sys.argv) > 1 else PDF
    doc = pymupdf.open(pdf_path)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for old in OUT_DIR.glob("page-*.png"):
        old.unlink()
    for i, page in enumerate(doc, start=1):
        pix = page.get_pixmap(matrix=pymupdf.Matrix(2, 2))
        out = OUT_DIR / f"page-{i:02d}.png"
        pix.save(out)
    print(f"Rasterized {len(doc)} pages to {OUT_DIR}")


if __name__ == "__main__":
    main()
