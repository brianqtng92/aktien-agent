import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# (Name, Investsumme, Wert aktuell)
data = [
    ("SoFi Technologies", 2612.93, 4120.00),
    ("Constellation Software", 1380.00, 1972.00),
    ("Allianz SE", 425.00, 511.68),
    ("ServiceNow Inc", 1948.96, 2487.20),
    ("Vanguard FTSE All-World (ETF)", 6153.40, 7515.82),
    ("MercadoLibre Inc", 1442.80, 1671.20),
    ("Broadridge Financial Sol.", 1119.68, 1262.40),
    ("CBOE Holdings", 1226.15, 1343.00),
    ("Kraken Robotics", 1050.00, 1068.00),
    ("Rocket Lab USA", 554.00, 558.00),
    ("Rambus Inc.", 533.64, 528.00),
    ("HawkEye 360", 1068.10, 1057.80),
    ("Bank Central Asia", 1999.94, 1935.52),
    ("Münchener Rück", 1051.00, 1030.80),
    ("A10 Networks", 506.52, 487.20),
    ("Intuitive Surgical", 1400.50, 1286.20),
    ("Tristel PLC", 1002.67, 945.00),
    ("Cellebrite DI Ltd", 2166.15, 2082.00),
    ("Hermès", 1905.09, 1541.50),
]

rows = [(name, inv, cur, (cur - inv) / inv * 100) for name, inv, cur in data]
rows.sort(key=lambda r: r[3], reverse=True)

names = [r[0] for r in rows]
pcts = [r[3] for r in rows]
colors = ["#3E8C6A" if p >= 0 else "#C0453A" for p in pcts]

fig, ax = plt.subplots(figsize=(10, 9))
bars = ax.barh(names, pcts, color=colors, edgecolor="white", height=0.7)
ax.axvline(0, color="#444444", linewidth=1)
ax.invert_yaxis()
ax.set_xlabel("Rendite seit Kauf (%)", fontsize=11)
ax.set_title("Rendite je Position (Investsumme → aktueller Wert) – Stand 2026-08-29",
             fontsize=13, fontweight="bold", pad=15)

for bar, p in zip(bars, pcts):
    x = bar.get_width()
    ax.text(x + (1.2 if x >= 0 else -1.2), bar.get_y() + bar.get_height() / 2,
            f"{p:+.1f}%", va="center", ha="left" if x >= 0 else "right",
            fontsize=9, fontweight="bold", color="#222222")

ax.set_xlim(min(pcts) - 8, max(pcts) + 10)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("/root/aktien-agent/reports/portfolio_rendite_2026-08-29.png", dpi=150, bbox_inches="tight")

for name, inv, cur, pct in rows:
    print(f"{name}: invest={inv:.2f} cur={cur:.2f} gain={cur-inv:+.2f} pct={pct:+.2f}%")
