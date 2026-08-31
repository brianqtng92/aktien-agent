import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# VOLLSTÄNDIGES Portfolio (Stand 2026-08-29) - alle 18 Einzelwerte + ETF bekannt
data = [
    ("Vanguard FTSE All-World (ETF)", 7515.82, "#2E5A8C"),
    ("SoFi Technologies", 4066.97, "#E4572E"),
    ("ServiceNow Inc", 2185.60, "#F2A541"),
    ("Constellation Software", 1972.00, "#4A9E8F"),
    ("Bank Central Asia", 1935.52, "#4A7FB5"),
    ("Cellebrite DI Ltd", 1869.20, "#7A6FB0"),
    ("MercadoLibre Inc", 1642.60, "#5CA793"),
    ("Hermès", 1581.27, "#B85C8A"),
    ("Intuitive Surgical", 1286.20, "#D4A5A5"),
    ("CBOE Holdings", 1343.00, "#6FA3D8"),
    ("Broadridge Financial Sol.", 1262.40, "#8FBB4A"),
    ("Kraken Robotics", 1068.00, "#C9A227"),
    ("HawkEye 360", 1057.80, "#D98C3D"),
    ("Münchener Rück", 1030.80, "#B85C5C"),
    ("Tristel PLC", 945.00, "#8C6BB1"),
    ("Rocket Lab USA", 558.00, "#3E9C8C"),
    ("Rambus Inc.", 528.00, "#A0A0A0"),
    ("Allianz SE", 511.66, "#2F6B5E"),
    ("A10 Networks", 487.20, "#C46A6A"),
]

labels = [f"{name}\n{value:,.0f} €".replace(",", ".") for name, value, _ in data]
values = [v for _, v, _ in data]
colors = [c for _, _, c in data]
total = sum(values)

fig, ax = plt.subplots(figsize=(12.5, 10.5))
wedges, texts, autotexts = ax.pie(
    values, labels=labels, colors=colors,
    autopct=lambda pct: f"{pct:.1f}%",
    pctdistance=0.78, labeldistance=1.08, startangle=90,
    wedgeprops=dict(width=0.55, edgecolor="white", linewidth=1.5),
    textprops=dict(fontsize=8.5),
)
for at in autotexts:
    at.set_fontsize(8)
    at.set_color("white")
    at.set_fontweight("bold")

total_str = f"{total:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")
ax.set_title(
    f"Vollständige Portfolio-Zusammensetzung – Stand 2026-08-29\n"
    f"Gesamtwert: {total_str} (alle 18 Einzelwerte + ETF, keine Datenlücken mehr)",
    fontsize=13, fontweight="bold", pad=20,
)
ax.text(
    0, -1.42,
    "Regelverstöße: SoFi Technologies bei 12,4% (Grenze: max. 10%) · ETF-Anteil nur 22,9% (Ziel: min. 50%, langfristig 60%)",
    ha="center", va="center", fontsize=10, style="italic", color="#8a3b1f", fontweight="bold",
)
ax.axis("equal")
plt.tight_layout()
plt.savefig("/root/aktien-agent/reports/portfolio_full_2026-08-29.png", dpi=150, bbox_inches="tight")
print("Total:", total)

# --- Regionen-Chart (Näherung, ETF nach FTSE-All-World-Länder-Gewichten aufgeteilt) ---
region_data = [
    ("USA", 17407.67, "#2E5A8C"),
    ("Sonstige (Kanada/Israel/ETF-Reststreuung)", 5561.57, "#A0A0A0"),
    ("Europa/UK", 4979.85, "#8FBB4A"),
    ("Japan/Asien", 3256.80, "#D98C3D"),
    ("Lateinamerika", 1642.60, "#E4572E"),
]
r_labels = [f"{name}\n{value:,.0f} € ({value/total*100:.1f}%)".replace(",", ".") for name, value, _ in region_data]
r_values = [v for _, v, _ in region_data]
r_colors = [c for _, _, c in region_data]

fig2, ax2 = plt.subplots(figsize=(10, 8.5))
wedges2, texts2, autotexts2 = ax2.pie(
    r_values, labels=r_labels, colors=r_colors,
    autopct=lambda pct: f"{pct:.1f}%",
    pctdistance=0.75, labeldistance=1.1, startangle=90,
    wedgeprops=dict(width=0.55, edgecolor="white", linewidth=1.5),
    textprops=dict(fontsize=10),
)
for at in autotexts2:
    at.set_fontsize(9)
    at.set_color("white")
    at.set_fontweight("bold")
ax2.set_title(
    "Regionen-Verteilung (Näherung) – ETF+Aktien zusammen – Stand 2026-08-29",
    fontsize=13, fontweight="bold", pad=20,
)
ax2.text(
    0, -1.35,
    "Regeln: USA ≤55% (hart ≤60%) · Europa/UK 15-20% · Japan/Asien 10-15% · Rest LatAm/sonstige\n"
    "Näherung: ETF-Länderaufteilung geschätzt aus FTSE-All-World-Indexgewichten (justetf/Vanguard, Stand 31.07.2026).\n"
    "Kanada (Constellation Software, Kraken Robotics) und Israel (Cellebrite) passen in keinen der 4 Buckets sauber.",
    ha="center", va="center", fontsize=8.5, style="italic", color="#555555",
)
ax2.axis("equal")
plt.tight_layout()
plt.savefig("/root/aktien-agent/reports/portfolio_regionen_2026-08-29.png", dpi=150, bbox_inches="tight")
print("Region total check:", sum(r_values))
