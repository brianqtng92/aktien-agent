import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Vollstaendige, aktuell bewertbare Positionen (Stand 2026-09-02, Kurse per Twelve-Data-Live-Abruf
# bzw. Investsumme als Platzhalter fuer Positionen ohne Live-Quelle - siehe depot/*.md fuer Details/Quellen)
data = [
    ("Vanguard FTSE All-World (ETF)", 7541.94, "#2E5A8C"),
    ("SoFi Technologies", 4120.00, "#E4572E"),
    ("Bank Central Asia", 2009.72, "#4A7FB5"),
    ("ServiceNow Inc", 2487.20, "#F2A541"),
    ("Cellebrite DI Ltd", 2082.00, "#7A6FB0"),
    ("MercadoLibre Inc", 1671.20, "#5CA793"),
    ("Hermès", 1541.50, "#B85C8A"),
    ("Constellation Software Inc", 1972.00, "#9B59B6"),
    ("HawkEye 360", 1681.70, "#D98C3D"),
    ("Intuitive Surgical", 1286.20, "#D4A5A5"),
    ("CBOE Holdings", 1268.13, "#6FA3D8"),
    ("Broadridge Financial Sol.", 1229.24, "#8FBB4A"),
    ("Cash (Scalable)", 1060.33, "#5A5A5A"),
    ("Kraken Robotics", 1050.00, "#C9A227"),
    ("Münchener Rück", 1030.80, "#B85C5C"),
    ("Tristel PLC", 945.00, "#8C6BB1"),
    ("Rocket Lab USA", 554.00, "#3E9C8C"),
    ("EUWAX Gold II", 496.60, "#D4B106"),
    ("Allianz SE", 504.31, "#2F6B5E"),
    ("A10 Networks", 448.27, "#C46A6A"),
    ("Rambus Inc.", 438.69, "#A0A0A0"),
]

labels = [f"{name}\n{value:,.0f} €".replace(",", ".") for name, value, _ in data]
values = [v for _, v, _ in data]
colors = [c for _, _, c in data]
total = sum(values)

fig, ax = plt.subplots(figsize=(13, 11))
wedges, texts, autotexts = ax.pie(
    values,
    labels=labels,
    colors=colors,
    autopct=lambda pct: f"{pct:.1f}%" if pct >= 1.5 else "",
    pctdistance=0.78,
    labeldistance=1.08,
    startangle=90,
    wedgeprops=dict(width=0.55, edgecolor="white", linewidth=1.5),
    textprops=dict(fontsize=8.2),
)
for at in autotexts:
    at.set_fontsize(7.8)
    at.set_color("white")
    at.set_fontweight("bold")

total_str = f"{total:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")
ax.set_title(
    f"Portfolio-Zusammensetzung – alle 4 Broker, Stand 2026-09-02\n"
    f"Gesamtwert: {total_str}",
    fontsize=13, fontweight="bold", pad=20,
)
ax.text(
    0, -1.42,
    "Kraken Robotics, Rocket Lab USA, HawkEye 360: Investsumme statt Live-Kurs (keine Live-Quelle).\n"
    "Allianz SE: Schaetzung aus Einstandskurs+Performance (Stand 22.08.), keine API bei Trade Republic.",
    ha="center", va="center", fontsize=8.5, style="italic", color="#555555",
)
ax.axis("equal")
plt.tight_layout()
plt.savefig("/Users/brianqtng/Downloads/aktien-agent/reports/portfolio_pie_2026-09-02.png", dpi=150, bbox_inches="tight")
print("Saved. Total value:", total)
for name, value, _ in data:
    print(f"{name}: {value:.2f} EUR -> {value/total*100:.1f}%")
