import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Stand 2026-09-17: Depot-Komplettupdate, alle 4 Broker live/frisch geprueft
# (Scalable per MCP, finanzen.net zero + Smartbroker+ per Twelve Data,
# Trade Republic Xetra weiterhin nicht live abrufbar - Stand 09.09.
# uebernommen, siehe depot/trade-republic.md)
data = [
    ("Vanguard FTSE All-World (ETF)", 8149.30, "#2E5A8C"),
    ("SoFi Technologies", 3663.60, "#E4572E"),
    ("Bank Central Asia", 1952.96, "#4A7FB5"),
    ("ServiceNow Inc", 2433.99, "#F2A541"),
    ("Cellebrite DI Ltd", 1989.99, "#7A6FB0"),
    ("MercadoLibre Inc", 1600.66, "#5CA793"),
    ("Hermès", 1573.00, "#B85C8A"),
    ("Constellation Software Inc", 1791.29, "#9B59B6"),
    ("HawkEye 360", 1407.62, "#D98C3D"),
    ("Intuitive Surgical", 1330.35, "#D4A5A5"),
    ("CBOE Holdings", 1176.51, "#6FA3D8"),
    ("Broadridge Financial Sol.", 1163.30, "#8FBB4A"),
    ("Cash (Scalable)", 0.00, "#5A5A5A"),
    ("Kraken Robotics", 856.86, "#C9A227"),
    ("Münchener Rück", 1052.20, "#B85C5C"),
    ("Tristel PLC", 1027.37, "#8C6BB1"),
    ("Rocket Lab USA", 554.35, "#3E9C8C"),
    ("EUWAX Gold II", 494.05, "#D4B106"),
    ("Allianz SE", 512.09, "#2F6B5E"),
    ("A10 Networks", 484.98, "#C46A6A"),
    ("Rambus Inc.", 424.94, "#A0A0A0"),
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
    f"Portfolio-Zusammensetzung – alle 4 Broker, Stand 2026-09-17\n"
    f"Gesamtwert: {total_str}",
    fontsize=13, fontweight="bold", pad=20,
)
ax.text(
    0, -1.42,
    "Depot-Komplettupdate 17.09.: Scalable Capital live per MCP, finanzen.net zero + Smartbroker+ per Twelve Data.\n"
    "Trade Republic (Allianz, Xetra): letzter Stand vom 09.09. (keine Live-Quelle, Tarif-Sperre).",
    ha="center", va="center", fontsize=8.5, style="italic", color="#555555",
)
ax.axis("equal")
plt.tight_layout()
plt.savefig("/Users/brianqtng/Downloads/aktien-agent/reports/portfolio_pie_2026-09-17.png", dpi=150, bbox_inches="tight")
print("Saved. Total value:", total)
for name, value, _ in data:
    print(f"{name}: {value:.2f} EUR -> {value/total*100:.1f}%")
