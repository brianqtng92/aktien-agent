#!/usr/bin/env python3
"""Generischer Trend-Linienchart (Full-Deep-Dive-Ergaenzung, 2026-09-10).

Fuer Kennzahlen-Zeitreihen mit wenigen Datenpunkten (Bruttomarge-Verlauf,
KGV-/Multiple-Historie), im selben Design wie render_chart.py. Ein Punkt pro
Periode (Jahr oder Quartal als Label), eine Linie, optionale horizontale
Referenzlinie (z.B. Branchen-/Peer-Durchschnitt).

Beispiel:
  python3 render_trend_line.py --point "2021:81.0" --point "2022:79.5" \
      --point "2023:78.9" --point "2024:80.1" --point "2025:81.0" \
      --point "TTM Q2'26:78.2" --title "RMBS -- Bruttomarge-Verlauf" \
      --ylabel "Bruttomarge %" --out RMBS-margin-trend-2026-09-10.png
"""
import argparse

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG = "#FFFFFF"
TEXT = "#262420"
TEXT_DIM = "#5C564A"
BORDER = "#D9D4C8"
GOLD = "#9C7A2E"
GOLD_BRIGHT = "#8A6A22"
RED = "#B03A2E"


def render(points, title, ylabel, out_path, ref_line=None, ref_label=""):
    labels = [p[0] for p in points]
    values = [p[1] for p in points]
    x = list(range(len(labels)))

    fig, ax = plt.subplots(figsize=(5.4, 4.2))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    ax.plot(x, values, color=GOLD_BRIGHT, linewidth=1.6, marker="o", markersize=5,
             markerfacecolor=GOLD_BRIGHT, markeredgecolor=BG, zorder=3)
    for xi, v in zip(x, values):
        ax.annotate(f"{v:g}", (xi, v), textcoords="offset points", xytext=(0, 8),
                    ha="center", fontsize=8.3, color=TEXT, fontweight="bold")

    if ref_line is not None:
        ax.axhline(ref_line, color=RED, linewidth=0.9, linestyle="--", alpha=0.75, zorder=2)
        ax.text(x[-1], ref_line, f" {ref_label}", color=RED, fontsize=7.6,
                 va="bottom", ha="right", clip_on=False)

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8.3)
    ax.set_title(title, color=TEXT, fontsize=11, loc="left", fontweight="bold", pad=8)
    ax.set_ylabel(ylabel, color=TEXT_DIM, fontsize=8.5)
    ax.tick_params(colors=TEXT_DIM, labelsize=8.5)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_color(BORDER)
    ax.grid(True, axis="y", color=BORDER, linewidth=0.4, alpha=0.5, zorder=1)
    vmin, vmax = min(values), max(values)
    pad = max((vmax - vmin) * 0.25, vmax * 0.05, 1)
    ax.set_ylim(vmin - pad, vmax + pad)

    fig.tight_layout()
    fig.savefig(out_path, dpi=160, facecolor=BG)
    plt.close(fig)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--point", action="append", default=[], required=True,
                    help="'Label:Wert', mehrfach verwendbar, chronologisch, z.B. --point '2025:81.0'")
    p.add_argument("--title", default="")
    p.add_argument("--ylabel", default="")
    p.add_argument("--ref-line", type=float, default=None, help="Optionale horizontale Referenzlinie")
    p.add_argument("--ref-label", default="")
    p.add_argument("--out", required=True)
    args = p.parse_args()

    points = []
    for pt in args.point:
        label, val = pt.split(":", 1)
        points.append((label, float(val)))

    render(points, args.title, args.ylabel, args.out, args.ref_line, args.ref_label)
    print(f"OK: {args.out}")
