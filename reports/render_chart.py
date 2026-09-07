#!/usr/bin/env python3
"""Reaper Candlestick-Chart-Renderer (Charttechnik-Ergaenzung, 2026-09-01).

Rendert einen echten Candlestick-Chart (+ Volumen, optional EMA-Overlays und
Zonen-Linien) aus Twelve-Data-Zeitreihen-JSON, im Reaper-Dunkel/Gold-Design.
Ersetzt die bisherigen reinen Tabellen-Sektionen in "Chart- und Einstiegslage"
durch ein echtes Chart-Bild, analog zu Raketentonis Referenz-PDFs, aber im
eigenen Design statt 1:1-Screenshot-Uebernahme.

Seit 2026-09-08 (Full-Deep-Dive-Erweiterung, "Reaper Deep Dive Report"):
optionale RSI(14)- und MACD(12,26,9)-Subplots unter dem Hauptchart (--rsi /
--macd), fuer Full Deep Dive gedacht -- Quick Filter nutzt weiterhin nur den
einfachen Haupt-Chart ohne Indikator-Subplots, um Renderzeit klein zu halten.

Workflow (vom Agenten pro Analyse ausgefuehrt):
  1. get_time_series (Twelve Data MCP) fuer den Ticker abrufen (z.B. 120-180
     Tage, interval=1day), Ergebnis-JSON in eine Datei schreiben
     (z.B. /tmp/<TICKER>_series.json).
  2. python3 reports/render_chart.py --json /tmp/<TICKER>_series.json
     --out reports/<TICKER>_chart.png --ema 20,50 --title "HAWK -- NYSE"
     [--zone "21.43:EMA20 Widerstand" --zone "17.00:52W-Tief"]
     [--rsi --macd]   (nur bei Full Deep Dive)
  3. Erzeugtes PNG in die PDF-Sektion "Chart- und Einstiegslage" einbetten
     (<img src="...">).

Erwartetes Eingabeformat: der ROHE "result"-String von get_time_series
(Twelve Data MCP), 1:1 in eine Datei geschrieben -- semikolon-getrennt mit
Kopfzeile, z.B.:
  datetime;open;high;low;close;volume
  2026-08-31;218.862;221.3;216.21;220.78;124033835
  ...
Zeilen duerfen in beliebiger Reihenfolge vorliegen (wird intern chronologisch
sortiert). Fehlt "volume" (z.B. bei manchen Indizes/FX), wird das
Volumen-Subplot automatisch weggelassen. Reines JSON ({"values": [...]})
wird als Fallback ebenfalls akzeptiert.
"""
import argparse
import json
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

BG = "#1A1C1F"
PANEL = "#232629"
BORDER = "#3A3E43"
TEXT = "#EDE8DF"
TEXT_DIM = "#A39B8E"
GOLD = "#C6922C"
GOLD_BRIGHT = "#E0B24E"
GREEN = "#5C9A5F"
RED = "#BC4F41"
EMA_COLORS = ["#5B8FC7", "#C97BC9", "#D9A441"]
RSI_LINE = "#D9A441"
RSI_OVERBOUGHT = "#BC4F41"
RSI_OVERSOLD = "#5C9A5F"
MACD_LINE = "#5B8FC7"
MACD_SIGNAL = "#C97BC9"


def load_series(path: str) -> pd.DataFrame:
    with open(path, encoding="utf-8") as f:
        raw = f.read().strip()
    if raw.startswith("{") or raw.startswith("["):
        data = json.loads(raw)
        values = data.get("values", data) if isinstance(data, dict) else data
        df = pd.DataFrame(values)
    else:
        from io import StringIO
        df = pd.read_csv(StringIO(raw), sep=";")
    for col in ("open", "high", "low", "close", "volume"):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.sort_values("datetime").reset_index(drop=True)
    return df


def compute_rsi(close: pd.Series, period: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, float("nan"))
    rsi = 100 - (100 / (1 + rs))
    return rsi.fillna(50)


def compute_macd(close: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9):
    ema_fast = close.ewm(span=fast, adjust=False).mean()
    ema_slow = close.ewm(span=slow, adjust=False).mean()
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    hist = macd_line - signal_line
    return macd_line, signal_line, hist


def render(df: pd.DataFrame, out_path: str, ema_periods, zones, title: str, currency: str,
           show_rsi: bool = False, show_macd: bool = False):
    has_volume = "volume" in df.columns and df["volume"].notna().any()

    rows = [("main", 3)]
    if has_volume:
        rows.append(("volume", 1))
    if show_macd and len(df) >= 26:
        rows.append(("macd", 1))
    if show_rsi and len(df) >= 14:
        rows.append(("rsi", 1))

    fig_h = 3.2 + 1.35 * (len(rows) - 1)
    fig, axes_raw = plt.subplots(
        len(rows), 1, figsize=(9.6, fig_h),
        gridspec_kw={"height_ratios": [r[1] for r in rows]},
        sharex=True,
    )
    axes_raw = [axes_raw] if len(rows) == 1 else list(axes_raw)
    axes = dict(zip((r[0] for r in rows), axes_raw))

    ax = axes["main"]
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    dates = mdates.date2num(df["datetime"])
    width = (dates[-1] - dates[0]) / max(len(dates), 1) * 0.6 if len(dates) > 1 else 0.6

    for x, o, h, l, c in zip(dates, df["open"], df["high"], df["low"], df["close"]):
        color = GREEN if c >= o else RED
        ax.plot([x, x], [l, h], color=color, linewidth=0.8, zorder=2)
        ax.add_patch(plt.Rectangle(
            (x - width / 2, min(o, c)), width, max(abs(c - o), 0.0001),
            facecolor=color, edgecolor=color, linewidth=0.4, zorder=3,
        ))

    for i, period in enumerate(ema_periods):
        if len(df) >= period:
            ema = df["close"].ewm(span=period, adjust=False).mean()
            ax.plot(dates, ema, color=EMA_COLORS[i % len(EMA_COLORS)], linewidth=1.1,
                     label=f"EMA{period}", zorder=4)

    for level, label in zones:
        ax.axhline(level, color=GOLD, linewidth=0.7, linestyle="--", alpha=0.7, zorder=1)
        ax.text(dates[-1], level, f" {label}", color=GOLD_BRIGHT, fontsize=7,
                 va="center", ha="left", clip_on=False)

    ax.set_title(title, color=TEXT, fontsize=11, loc="left", fontweight="bold", pad=8)
    ax.tick_params(colors=TEXT_DIM, labelsize=7.5)
    ax.set_ylabel(currency, color=TEXT_DIM, fontsize=8)
    for spine in ax.spines.values():
        spine.set_color(BORDER)
    ax.grid(True, color=BORDER, linewidth=0.4, alpha=0.5)
    if ema_periods:
        leg = ax.legend(loc="upper left", fontsize=7, facecolor=PANEL, edgecolor=BORDER, labelcolor=TEXT)

    if has_volume:
        axv = axes["volume"]
        axv.set_facecolor(BG)
        vol_colors = [GREEN if c >= o else RED for o, c in zip(df["open"], df["close"])]
        axv.bar(dates, df["volume"], width=width, color=vol_colors, alpha=0.6)
        axv.tick_params(colors=TEXT_DIM, labelsize=7)
        axv.set_ylabel("Volumen", color=TEXT_DIM, fontsize=7.5)
        for spine in axv.spines.values():
            spine.set_color(BORDER)
        axv.grid(True, color=BORDER, linewidth=0.3, alpha=0.4)

    if "macd" in axes:
        axm = axes["macd"]
        axm.set_facecolor(BG)
        macd_line, signal_line, hist = compute_macd(df["close"])
        hist_colors = [GREEN if v >= 0 else RED for v in hist]
        axm.bar(dates, hist, width=width, color=hist_colors, alpha=0.5, zorder=1)
        axm.plot(dates, macd_line, color=MACD_LINE, linewidth=1.0, label="MACD", zorder=2)
        axm.plot(dates, signal_line, color=MACD_SIGNAL, linewidth=1.0, label="Signal", zorder=2)
        axm.axhline(0, color=BORDER, linewidth=0.6)
        axm.tick_params(colors=TEXT_DIM, labelsize=7)
        axm.set_ylabel("MACD", color=TEXT_DIM, fontsize=7.5)
        for spine in axm.spines.values():
            spine.set_color(BORDER)
        axm.grid(True, color=BORDER, linewidth=0.3, alpha=0.4)
        axm.legend(loc="upper left", fontsize=6.5, facecolor=PANEL, edgecolor=BORDER, labelcolor=TEXT)

    if "rsi" in axes:
        axr = axes["rsi"]
        axr.set_facecolor(BG)
        rsi = compute_rsi(df["close"])
        axr.plot(dates, rsi, color=RSI_LINE, linewidth=1.1, zorder=2)
        axr.axhline(70, color=RSI_OVERBOUGHT, linewidth=0.6, linestyle="--", alpha=0.7)
        axr.axhline(30, color=RSI_OVERSOLD, linewidth=0.6, linestyle="--", alpha=0.7)
        axr.fill_between(dates, 70, 100, color=RSI_OVERBOUGHT, alpha=0.08, zorder=1)
        axr.fill_between(dates, 0, 30, color=RSI_OVERSOLD, alpha=0.08, zorder=1)
        axr.set_ylim(0, 100)
        axr.set_yticks([30, 50, 70])
        axr.tick_params(colors=TEXT_DIM, labelsize=7)
        axr.set_ylabel("RSI(14)", color=TEXT_DIM, fontsize=7.5)
        for spine in axr.spines.values():
            spine.set_color(BORDER)
        axr.grid(True, color=BORDER, linewidth=0.3, alpha=0.4)

    axes_raw[-1].xaxis.set_major_formatter(mdates.DateFormatter("%d.%m."))
    fig.autofmt_xdate(rotation=0, ha="center")

    fig.tight_layout()
    fig.savefig(out_path, dpi=160, facecolor=BG)
    plt.close(fig)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--json", required=True, help="Pfad zur gespeicherten get_time_series-Ausgabe (Semikolon-CSV oder JSON)")
    p.add_argument("--out", required=True, help="Ziel-PNG-Pfad")
    p.add_argument("--ema", default="20,50", help="Kommagetrennte EMA-Perioden, z.B. 20,50")
    p.add_argument("--zone", action="append", default=[], help="Zonen-Linie als 'Kurs:Label', mehrfach verwendbar")
    p.add_argument("--title", default="", help="Chart-Titel (z.B. 'HAWK -- NYSE')")
    p.add_argument("--currency", default="", help="Waehrungslabel fuer Y-Achse, z.B. 'USD'")
    p.add_argument("--rsi", action="store_true", help="RSI(14)-Subplot rendern (Full Deep Dive)")
    p.add_argument("--macd", action="store_true", help="MACD(12,26,9)-Subplot rendern (Full Deep Dive)")
    args = p.parse_args()

    df = load_series(args.json)
    if df.empty:
        print("Fehler: keine Kursdaten in der JSON-Datei gefunden.", file=sys.stderr)
        sys.exit(1)

    ema_periods = [int(x) for x in args.ema.split(",") if x.strip()]
    zones = []
    for z in args.zone:
        try:
            level_str, label = z.split(":", 1)
            zones.append((float(level_str), label))
        except ValueError:
            print(f"Warnung: Zone '{z}' ignoriert (Format 'Kurs:Label' erwartet).", file=sys.stderr)

    render(df, args.out, ema_periods, zones, args.title, args.currency,
           show_rsi=args.rsi, show_macd=args.macd)
    print(f"OK: {args.out} ({len(df)} Kerzen)")
