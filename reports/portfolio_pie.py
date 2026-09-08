import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Stand 2026-09-08: Scalable-Positionen + Cash live per MCP aktualisiert
# (Kurse per 08.09. abends, Cash-Verrechnungskonto zeigt live 0,00 EUR -
# siehe macro/master-status-Notiz), uebrige Broker unveraendert aus
# depot/*.md uebernommen (Stand 2026-09-05, keine taegliche Live-Quelle
# fuer diese drei Broker verfuegbar, siehe Fussnote im Chart)
data = [
    ("Vanguard FTSE All-World (ETF)", 8168.99, "#2E5A8C"),
    ("SoFi Technologies", 3984.69, "#E4572E"),
    ("Bank Central Asia", 2015.91, "#4A7FB5"),
    ("ServiceNow Inc", 2507.32, "#F2A541"),
    ("Cellebrite DI Ltd", 2056.28, "#7A6FB0"),
    ("MercadoLibre Inc", 1714.48, "#5CA793"),
    ("Hermès", 1541.50, "#B85C8A"),
    ("Constellation Software Inc", 1881.77, "#9B59B6"),
    ("HawkEye 360", 1494.42, "#D98C3D"),
    ("Intuitive Surgical", 1273.83, "#D4A5A5"),
    ("CBOE Holdings", 1285.18, "#6FA3D8"),
    ("Broadridge Financial Sol.", 1232.46, "#8FBB4A"),
    ("Cash (Scalable)", 0.00, "#5A5A5A"),
    ("Kraken Robotics", 957.70, "#C9A227"),
    ("Münchener Rück", 1030.80, "#B85C5C"),
    ("Tristel PLC", 929.88, "#8C6BB1"),
    ("Rocket Lab USA", 553.21, "#3E9C8C"),
    ("EUWAX Gold II", 494.68, "#D4B106"),
    ("Allianz SE", 517.67, "#2F6B5E"),
    ("A10 Networks", 446.83, "#C46A6A"),
    ("Rambus Inc.", 435.75, "#A0A0A0"),
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
    f"Portfolio-Zusammensetzung – alle 4 Broker, Stand 2026-09-08\n"
    f"Gesamtwert: {total_str}",
    fontsize=13, fontweight="bold", pad=20,
)
ax.text(
    0, -1.42,
    "Scalable Capital (ETF, Bank Central Asia, Gold, Cash) live per MCP Stand 08.09.\n"
    "Übrige Positionen (finanzen.net zero, Trade Republic, Smartbroker+): letzter Stand aus depot/*.md vom 05.09. (keine tägliche Live-Quelle).",
    ha="center", va="center", fontsize=8.5, style="italic", color="#555555",
)
ax.axis("equal")
plt.tight_layout()
plt.savefig("/Users/brianqtng/Downloads/aktien-agent/reports/portfolio_pie_2026-09-08.png", dpi=150, bbox_inches="tight")
print("Saved. Total value:", total)
for name, value, _ in data:
    print(f"{name}: {value:.2f} EUR -> {value/total*100:.1f}%")
