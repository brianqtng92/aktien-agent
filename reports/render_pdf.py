#!/usr/bin/env python3
"""HTML -> PDF Renderer fuer den Aktien-Agent (lokal, Claude-Code-nativ).

Ersetzt den Cloud-Container-Playwright-Umweg aus HANDOVER.md Abschnitt 10.2:
laeuft direkt auf Brians Mac gegen das bereits installierte Google Chrome
(kein `playwright install chromium` noetig, kein extra Download).

Usage:
    python3 reports/render_pdf.py <input.html> <output.pdf>
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


def render(html_path: str, pdf_path: str) -> None:
    html_file = Path(html_path).resolve()
    if not html_file.exists():
        raise FileNotFoundError(html_file)

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        page = browser.new_page()
        page.goto(html_file.as_uri())
        page.pdf(path=pdf_path, format="A4", print_background=True, margin={
            "top": "0", "bottom": "0", "left": "0", "right": "0",
        })
        browser.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 render_pdf.py <input.html> <output.pdf>")
        sys.exit(1)
    render(sys.argv[1], sys.argv[2])
    print(f"OK: {sys.argv[2]}")
