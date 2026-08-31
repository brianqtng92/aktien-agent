import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Bekannte, aktuell bewertbare Positionen (Stand 2026-08-29, Kurse per WebSearch/WebFetch
# bzw. Investsumme+Saldo aus nachgereichter Kaufhistorie berechnet)
data = [
    ("Vanguard FTSE All-World (ETF)", 7515.82, "#2E5A8C"),
    ("SoFi Technologies", 4066.97, "#E4572E"),
    ("Bank Central Asia", 1935.52, "#4A7FB5"),
    ("ServiceNow Inc", 2185.60, "#F2A541"),
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

fig, ax = plt.subplots(figsize=(12, 10))
wedges, texts, autotexts = ax.pie(
    values,
    labels=labels,
    colors=colors,
    autopct=lambda pct: f"{pct:.1f}%",
    pctdistance=0.78,
    labeldistance=1.08,
    startangle=90,
    wedgeprops=dict(width=0.55, edgecolor="white", linewidth=1.5),
    textprops=dict(fontsize=8.5),
)
for at in autotexts:
    at.set_fontsize(8)
    at.set_color("white")
    at.set_fontweight("bold")

total_str = f"{total:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")
ax.set_title(
    f"Portfolio-Zusammensetzung (bekannter Teil) – Stand 2026-08-29\n"
    f"Bekannter Gesamtwert: {total_str}",
    fontsize=13, fontweight="bold", pad=20,
)
ax.text(
    0, -1.38,
    "Noch offen (nicht enthalten): Constellation Software (Investsumme 1.380€ bekannt,\n"
    "aktueller Wert noch nicht berechenbar, vermutlich Bruchstück-Kauf).\n"
    "Hinweis: SoFi Technologies liegt bereits deutlich über der neuen 10%-Positionsgrenze.",
    ha="center", va="center", fontsize=9, style="italic", color="#8a3b1f", fontweight="bold",
)
ax.axis("equal")
plt.tight_layout()
plt.savefig("/root/aktien-agent/reports/portfolio_pie_2026-08-29b.png", dpi=150, bbox_inches="tight")
print("Saved. Total known value:", total)
for name, value, _ in data:
    print(f"{name}: {value:.2f} EUR -> {value/total*100:.1f}%")
