#!/usr/bin/env python3
"""DCF-Bear/Base/Bull-Balkenchart (Full-Deep-Dive-Ergaenzung, 2026-09-10).

Rendert einen einfachen Balkenchart fuer DCF-Szenarien (Bear/Base/Bull Fair
Value) mit einer horizontalen Linie fuer den aktuellen Kurs, im selben
Design (Farben/Typografie) wie render_chart.py.

Beispiel:
  python3 render_scenario_bar.py --scenario "Bear:31" --scenario "Base:43.5" \
      --scenario "Bull:68.5" --current 87.65 --title "RMBS -- DCF-Szenarien" \
      --currency USD --out RMBS-bearbasebull-2026-09-10.png
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
GREEN = "#3F7D44"
RED = "#B03A2E"

SCENARIO_COLORS = {"bear": RED, "base": GOLD, "bull": GREEN}


def render(scenarios, current, title, currency, out_path):
    labels = [s[0] for s in scenarios]
    values = [s[1] for s in scenarios]
    colors = [SCENARIO_COLORS.get(l.lower(), GOLD) for l in labels]

    fig, ax = plt.subplots(figsize=(5.4, 4.2))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    bars = ax.bar(labels, values, color=colors, width=0.55, zorder=3)
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, v + max(values) * 0.02,
                 f"{currency} {v:,.2f}".replace(",", "."), ha="center", va="bottom",
                 color=TEXT, fontsize=9.5, fontweight="bold")

    if current is not None:
        ax.axhline(current, color=TEXT, linewidth=1.1, linestyle="--", zorder=2)
        ax.text(len(labels) - 0.42, current, f" Kurs {currency} {current:,.2f}".replace(",", "."),
                color=TEXT, fontsize=8.2, va="bottom", ha="left", clip_on=False)

    top = max(values + ([current] if current else [])) * 1.18
    ax.set_ylim(0, top)
    ax.set_title(title, color=TEXT, fontsize=11, loc="left", fontweight="bold", pad=8)
    ax.set_ylabel(currency, color=TEXT_DIM, fontsize=8.5)
    ax.tick_params(colors=TEXT_DIM, labelsize=9)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_color(BORDER)
    ax.grid(True, axis="y", color=BORDER, linewidth=0.4, alpha=0.5, zorder=1)

    fig.tight_layout()
    fig.savefig(out_path, dpi=160, facecolor=BG)
    plt.close(fig)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--scenario", action="append", default=[], required=True,
                    help="'Label:Wert', mehrfach verwendbar, z.B. --scenario 'Bear:31'")
    p.add_argument("--current", type=float, default=None, help="Aktueller Kurs (horizontale Linie)")
    p.add_argument("--title", default="")
    p.add_argument("--currency", default="USD")
    p.add_argument("--out", required=True)
    args = p.parse_args()

    scenarios = []
    for s in args.scenario:
        label, val = s.split(":", 1)
        scenarios.append((label, float(val)))

    render(scenarios, args.current, args.title, args.currency, args.out)
    print(f"OK: {args.out}")
