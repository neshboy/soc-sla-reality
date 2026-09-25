"""
Assemble ordered manuscript fragments (manuscript/content/*.html) into one
printable HTML file, then render it to PDF via headless Edge.

Fragment authoring convention:
  - Each fragment lives in manuscript/content/NN-slug.html
  - Each fragment is a full <html> doc for easy standalone preview, referencing
    assets as "../../assets/..." (two levels up from manuscript/content/)
  - The assembler extracts the <body> inner content and rewrites
    "../../assets/" -> "../assets/" so it resolves correctly from build/manuscript.html
  - Order is controlled by the MANIFEST list below (not just filename sort),
    so sections can be added out of numeric order if needed.
"""
import re
import sys
import time
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "manuscript" / "content"
BUILD_DIR = ROOT / "build"
OUT_HTML = BUILD_DIR / "manuscript.html"
OUT_PDF = BUILD_DIR / "SOC_SLA_Reality_neshboy.pdf"

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

BODY_RE = re.compile(r"<body[^>]*>(.*)</body>", re.DOTALL | re.IGNORECASE)


def load_manifest():
    manifest_file = CONTENT_DIR / "MANIFEST.txt"
    if manifest_file.exists():
        lines = [l.strip() for l in manifest_file.read_text(encoding="utf-8").splitlines()]
        return [l for l in lines if l and not l.startswith("#")]
    return sorted(p.name for p in CONTENT_DIR.glob("*.html"))


def extract_body(html_text: str) -> str:
    m = BODY_RE.search(html_text)
    content = m.group(1) if m else html_text
    return content.replace("../../assets/", "../assets/")


def assemble():
    manifest = load_manifest()
    if not manifest:
        print("No fragments found in manuscript/content/. Nothing to assemble.")
        sys.exit(1)

    parts = []
    missing = []
    for name in manifest:
        fpath = CONTENT_DIR / name
        if not fpath.exists():
            missing.append(name)
            continue
        parts.append(f"<!-- ==== {name} ==== -->\n" + extract_body(fpath.read_text(encoding="utf-8")))

    if missing:
        print("WARNING: missing fragments (skipped):", missing)

    cache_bust = str(int(time.time()))
    doc = f"""<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<title>THE SOC SLA REALITY</title>
<link rel="stylesheet" href="../assets/theme.css?v={cache_bust}">
</head>
<body>
{chr(10).join(parts)}
</body></html>
"""
    BUILD_DIR.mkdir(exist_ok=True)
    OUT_HTML.write_text(doc, encoding="utf-8")
    print(f"Wrote {OUT_HTML} ({len(parts)} sections, {len(missing)} missing)")


def render_pdf():
    url = "file:///" + str(OUT_HTML).replace("\\", "/")
    cmd = [
        EDGE, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
        "--disk-cache-dir=" + str(BUILD_DIR / "_edge_cache"), "--disk-cache-size=1",
        f"--user-data-dir={BUILD_DIR / '_edge_profile'}",
        f"--print-to-pdf={OUT_PDF}", "--no-pdf-header-footer",
        "--virtual-time-budget=30000",
        url,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Edge exited", result.returncode, result.stdout, result.stderr)
        sys.exit(1)
    print(f"Wrote {OUT_PDF}")


if __name__ == "__main__":
    assemble()
    if "--pdf" in sys.argv:
        render_pdf()
