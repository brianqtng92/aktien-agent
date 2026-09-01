"""
Depot vs. Markt - Vorwaerts-Tracking-Chart (siehe depot/performance_tracking.md).

Liest depot/performance_tracking.csv (eine Zeile pro Woche, angehaengt vom
woechentlichen Wochenfazit-Lauf) und zeichnet die prozentuale Veraenderung
von Depot, S&P 500, Nasdaq 100 und MSCI-World-Proxy seit der Baseline-Zeile
(erste Zeile der Datei) als Linienchart.

Wird jede Woche mit der aktuellen CSV neu ausgefuehrt, Output-Dateiname ist
fix (kein Datum im Namen), damit der Wochenfazit-Report immer denselben Pfad
einbetten kann.
"""
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

CSV_PATH = "depot/performance_tracking.csv"
OUT_PATH = "reports/benchmark_vs_depot.png"

rows = []
with open(CSV_PATH, newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        rows.append({
            "date": datetime.strptime(r["date"], "%Y-%m-%d"),
            "depot": float(r["depot_value_eur"]),
            "sp500": float(r["sp500"]),
            "nasdaq100": float(r["nasdaq100"]),
            "msci": float(r["msci_world_proxy_eur"]),
        })

base = rows[0]
dates = [r["date"] for r in rows]

series = {
    "Depot (Brian)": ("depot", "#C6922C", 3.0),
    "S&P 500": ("sp500", "#4A7FB5", 1.8),
    "Nasdaq 100": ("nasdaq100", "#7A6FB0", 1.8),
    "MSCI World (Proxy)": ("msci", "#5CA793", 1.8),
}

fig, ax = plt.subplots(figsize=(10, 6))

for label, (key, color, lw) in series.items():
    pct = [(r[key] / base[key] - 1) * 100 for r in rows]
    marker = "o" if len(rows) < 6 else None
    ax.plot(dates, pct, label=label, color=color, linewidth=lw, marker=marker, markersize=5)
    ax.annotate(f"{pct[-1]:+.1f}%", (dates[-1], pct[-1]), textcoords="offset points",
                xytext=(6, 0), fontsize=9, fontweight="bold", color=color, va="center")

ax.axhline(0, color="#444444", linewidth=1)
ax.set_ylabel("Veränderung seit Start (%)", fontsize=11)
ax.set_title(
    f"Depot vs. Markt – seit {base['date'].strftime('%d.%m.%Y')} (Vorwärts-Tracking)",
    fontsize=13, fontweight="bold", pad=15,
)
ax.legend(loc="upper left", frameon=False, fontsize=9)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m."))
ax.spines[["top", "right"]].set_visible(False)

if len(rows) == 1:
    ax.text(
        0.5, 0.5,
        "Startpunkt – noch kein Wochenverlauf.\nAb der nächsten Woche erscheint hier die Kurve.",
        transform=ax.transAxes, ha="center", va="center", fontsize=11, style="italic", color="#888888",
    )
    ax.set_xlim(dates[0] - __import__("datetime").timedelta(days=3), dates[0] + __import__("datetime").timedelta(days=3))
    ax.set_ylim(-5, 5)

plt.tight_layout()
plt.savefig(OUT_PATH, dpi=150, bbox_inches="tight")
print(f"Saved to {OUT_PATH}")
for r in rows:
    print(r["date"].strftime("%Y-%m-%d"), {k: round((r[v[0]] / base[v[0]] - 1) * 100, 2) for k, v in series.items()})
