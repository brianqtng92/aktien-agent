"""
Kanonisches Chart-Set fuer den woechentlichen Wochenfazit-Report.

WIRD JEDE WOCHE VOM WOCHENFAZIT-LAUF NEU AUSGEFUEHRT:
  1. Die DATA-Liste unten mit den aktuellen Investsumme/Wert-Zahlen pro
     Position aktualisieren (Quelle: depot/finanzen-net-zero.md, jeweils
     frisch nachgezogene Kurse -- siehe dortige "Update"-Historie).
  2. Region und Sektor je Position pflegen (Klassifizierung wie in den
     bisherigen Wochenfazits/architecture.md Abschnitt 3 hergeleitet).
  3. `python3 reports/weekly_charts.py` ausfuehren.
  4. Vier PNGs mit FESTEN Dateinamen (kein Datum im Namen) werden neu
     geschrieben und koennen so unveraendert vom PDF-Report
     (reports/build_wochenfazit.py) eingebettet werden:
       - reports/chart_zusammensetzung.png  (Donut: alle Positionen)
       - reports/chart_regionen.png         (Donut: 4-Regionen-Split)
       - reports/chart_sektoren.png         (Donut: 5-Sektoren-Split)
       - reports/chart_rendite.png          (Balken: Rendite % je Position)
  5. reports/benchmark_chart.py separat ausfuehren, NACHDEM die neue Zeile
     in depot/performance_tracking.csv ergaenzt wurde.

ETF-Naeherung: der Vanguard-FTSE-All-World-Anteil wird sowohl fuer Region
als auch Sektor ueber die zuletzt abgerufenen Index-Gewichte aufgeteilt
(siehe architecture.md, "Geografische Streuung" / "Sektor-Streuung").
Diese ETF_REGION_SPLIT / ETF_SECTOR_SPLIT unten bei Bedarf aktualisieren,
wenn ein neuer justetf/Vanguard-Factsheet-Abruf andere Gewichte liefert.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

STAND = "2026-08-29"

# (Name, Investsumme, Wert aktuell, Region, Sektor)
# Region-Buckets: USA | Europa/UK | Japan/Asien | Lateinamerika | Sonstige (CA/IL/etc.)
# Sektor-Buckets: Technologie | Finanzwesen | Gesundheitswesen | Industriewerte | Rest
DATA = [
    ("SoFi Technologies",              2612.93, 4120.00, "USA",          "Finanzwesen"),
    ("Constellation Software",         1380.00, 1972.00, "Sonstige",     "Technologie"),  # Kanada
    ("Allianz SE",                      425.00,  511.68, "Europa/UK",    "Finanzwesen"),
    ("ServiceNow Inc",                 1948.96, 2487.20, "USA",          "Technologie"),
    ("MercadoLibre Inc",               1442.80, 1671.20, "Lateinamerika","Rest"),
    ("Broadridge Financial Sol.",      1119.68, 1262.40, "USA",          "Finanzwesen"),
    ("CBOE Holdings",                  1226.15, 1343.00, "USA",          "Finanzwesen"),
    ("Kraken Robotics",                1050.00, 1068.00, "Sonstige",     "Industriewerte"),  # Kanada
    ("Rocket Lab USA",                  554.00,  558.00, "USA",          "Industriewerte"),
    ("Rambus Inc.",                     533.64,  528.00, "USA",          "Technologie"),
    ("HawkEye 360",                    1068.10, 1057.80, "USA",          "Industriewerte"),
    ("Bank Central Asia",              1999.94, 1935.52, "Japan/Asien",  "Finanzwesen"),
    ("Münchener Rück",                 1051.00, 1030.80, "Europa/UK",    "Finanzwesen"),
    ("A10 Networks",                    506.52,  487.20, "USA",          "Technologie"),
    ("Intuitive Surgical",             1400.50, 1286.20, "USA",          "Gesundheitswesen"),
    ("Tristel PLC",                    1002.67,  945.00, "Europa/UK",    "Gesundheitswesen"),
    ("Cellebrite DI Ltd",              2166.15, 2082.00, "Sonstige",     "Technologie"),  # Israel
    ("Hermès",                         1905.09, 1541.50, "Europa/UK",    "Rest"),
]
ETF_NAME = "Vanguard FTSE All-World (ETF)"
ETF_INVEST = 6153.40
ETF_WERT = 7515.82

# Naeherung, Stand 31.07.2026 (justetf/Vanguard-Factsheet, siehe architecture.md)
ETF_REGION_SPLIT = {
    "USA": 0.6162, "Europa/UK": 0.1212, "Japan/Asien": 0.1497,
    "Lateinamerika": 0.0, "Sonstige": 0.1129,
}
ETF_SECTOR_SPLIT = {
    "Technologie": 0.334, "Finanzwesen": 0.157, "Industriewerte": 0.126,
    "Gesundheitswesen": 0.079, "Rest": 0.304,  # Rest = Cons.Disc+Staples+Telecom+Materials+Utilities+RealEstate+Energy
}

COLORS = {
    "USA": "#2E5A8C", "Europa/UK": "#8FBB4A", "Japan/Asien": "#D98C3D",
    "Lateinamerika": "#E4572E", "Sonstige": "#A0A0A0",
    "Technologie": "#2E5A8C", "Finanzwesen": "#B85C8A", "Gesundheitswesen": "#5CA793",
    "Industriewerte": "#D98C3D", "Rest": "#A0A0A0",
}

total = sum(w for _, _, w, _, _ in DATA) + ETF_WERT


def donut(slices, title, subtitle, out_path):
    labels = [f"{name}\n{val:,.0f} € ({val/total*100:.1f}%)".replace(",", ".") for name, val in slices]
    values = [v for _, v in slices]
    colors = [COLORS.get(name, "#999999") for name, _ in slices]
    fig, ax = plt.subplots(figsize=(9, 8))
    wedges, texts, autotexts = ax.pie(
        values, labels=labels, colors=colors,
        autopct=lambda p: f"{p:.1f}%", pctdistance=0.76, labeldistance=1.1,
        startangle=90, wedgeprops=dict(width=0.5, edgecolor="white", linewidth=1.5),
        textprops=dict(fontsize=9.5),
    )
    for at in autotexts:
        at.set_fontsize(8.5); at.set_color("white"); at.set_fontweight("bold")
    ax.set_title(title, fontsize=13, fontweight="bold", pad=18)
    if subtitle:
        ax.text(0, -1.32, subtitle, ha="center", va="center", fontsize=8.5, style="italic", color="#555555")
    ax.axis("equal")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


# --- 1) Gesamt-Zusammensetzung ---
comp_slices = [(ETF_NAME, ETF_WERT)] + [(n, w) for n, _, w, _, _ in DATA]
donut(comp_slices,
      f"Portfolio-Zusammensetzung – Stand {STAND}\nGesamtwert: {total:,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."),
      None, "reports/chart_zusammensetzung.png")

# --- 2) Regionen ---
region_totals = {}
for _, _, w, region, _ in DATA:
    region_totals[region] = region_totals.get(region, 0) + w
for region, share in ETF_REGION_SPLIT.items():
    region_totals[region] = region_totals.get(region, 0) + ETF_WERT * share
donut(sorted(region_totals.items(), key=lambda x: -x[1]),
      f"Regionen-Verteilung (ETF+Aktien) – Stand {STAND}",
      "Regeln: USA ≤55% (hart ≤60%) · Europa/UK 15-20% · Japan/Asien 10-15% · Rest LatAm/Sonstige\n"
      "ETF-Länderaufteilung genähert über FTSE-All-World-Indexgewichte.",
      "reports/chart_regionen.png")

# --- 3) Sektoren ---
sector_totals = {}
for _, _, w, _, sektor in DATA:
    sector_totals[sektor] = sector_totals.get(sektor, 0) + w
for sektor, share in ETF_SECTOR_SPLIT.items():
    sector_totals[sektor] = sector_totals.get(sektor, 0) + ETF_WERT * share
donut(sorted(sector_totals.items(), key=lambda x: -x[1]),
      f"Sektor-Verteilung (ETF+Aktien) – Stand {STAND}",
      "Ziel: Technologie 30-35% · Finanzwesen 20-25% · Gesundheitswesen 10-15% · Industrie 10-15% · Rest 5-10%\n"
      "ETF-Sektoraufteilung genähert über Vanguard-Factsheet-Gewichte.",
      "reports/chart_sektoren.png")

# --- 4) Rendite je Position ---
rendite_rows = [(ETF_NAME, ETF_INVEST, ETF_WERT)] + [(n, inv, w) for n, inv, w, _, _ in DATA]
rendite_rows = [(n, inv, w, (w - inv) / inv * 100) for n, inv, w in rendite_rows]
rendite_rows.sort(key=lambda r: r[3], reverse=True)
names = [r[0] for r in rendite_rows]
pcts = [r[3] for r in rendite_rows]
bar_colors = ["#3E8C6A" if p >= 0 else "#C0453A" for p in pcts]

fig, ax = plt.subplots(figsize=(10, 9))
bars = ax.barh(names, pcts, color=bar_colors, edgecolor="white", height=0.7)
ax.axvline(0, color="#444444", linewidth=1)
ax.invert_yaxis()
ax.set_xlabel("Rendite seit Kauf (%)", fontsize=11)
ax.set_title(f"Rendite je Position – Stand {STAND}", fontsize=13, fontweight="bold", pad=15)
for bar, p in zip(bars, pcts):
    x = bar.get_width()
    ax.text(x + (1.2 if x >= 0 else -1.2), bar.get_y() + bar.get_height() / 2,
            f"{p:+.1f}%", va="center", ha="left" if x >= 0 else "right",
            fontsize=9, fontweight="bold", color="#222222")
ax.set_xlim(min(pcts) - 8, max(pcts) + 10)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("reports/chart_rendite.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print(f"Gesamtwert: {total:.2f} EUR")
print("4 Charts geschrieben: chart_zusammensetzung.png, chart_regionen.png, chart_sektoren.png, chart_rendite.png")
