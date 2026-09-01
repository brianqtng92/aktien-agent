#!/usr/bin/env python3
"""Bodenbildung-/Aufwaertstrend-Proxy (Charttechnik-Ergaenzung, 2026-09-01).

WICHTIGER HINWEIS (No-False-Precision-Regel, siehe architecture.md): Dies ist
eine ALGORITHMISCHE ANNAEHERUNG (hoehere Tiefs + EMA20-Breakout +
Volumen-Trend), KEIN echtes visuelles Chartmuster-Erkennen. Das TA-Modul
(jack-technical-analyst-v1.9.md) schaetzt Formationen laut eigenem Wortlaut
ausdruecklich nur aus Nutzer-Input, nicht selbst aus Zahlenreihen -- dieses
Skript schliesst die Luecke fuer den UNBEAUFSICHTIGTEN Betrieb (Scheduled
Tasks), wo niemand einen Chart-Screenshot beschreiben kann. Das Ergebnis ist
ein Hinweis, kein Ersatz fuer echte Musteranalyse. Bei einem "JA"-Ergebnis
bleibt Pflicht: mit der fundamentalen These abgleichen (siehe
"Chartmuster-Erkennung als aktiver Impuls" in architecture.md), bevor daraus
ein Kauf-Vorschlag wird.

Methodik:
  1. Pivot-Tiefs: ein Tag gilt als Pivot-Tief, wenn sein Low niedriger ist als
     das Low der `--fractal` Tage davor UND danach (Standard 3 Tage,
     einfache Fraktal-Definition).
  2. Hoehere-Tiefs-Check: die letzten >=2 Pivot-Tiefs im Betrachtungsfenster
     steigen an (jedes neuere Pivot-Tief > vorheriges).
  3. EMA20-Breakout: aktueller Schlusskurs > EMA20 UND EMA20 ist in den
     letzten 5 Tagen gestiegen (nicht nur zufaellig ein Tag drueber).
  4. Volumen-Trend: Durchschnittsvolumen der letzten 5 Tage > Durchschnitt
     der letzten 20 Tage (Akkumulations-Indiz).
  Verdict: "JA" wenn >=2 von 3 Signalen (2-4) erfuellt UND hoehere Tiefs
  vorliegen; sonst "NEIN". Bei zu kurzer Historie: "UNKLAR".

Eingabeformat: der ROHE "result"-String von get_time_series (Twelve Data
MCP), 1:1 in eine Datei geschrieben (Semikolon-CSV mit Kopfzeile). Reines
JSON ({"values": [...]}) wird als Fallback ebenfalls akzeptiert.

Aufruf: python3 reports/detect_bodenbildung.py --json /tmp/<TICKER>_series.txt
"""
import argparse
import json
import sys

import pandas as pd


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


def find_pivot_lows(df: pd.DataFrame, fractal: int):
    pivots = []
    lows = df["low"].values
    for i in range(fractal, len(lows) - fractal):
        window = lows[i - fractal:i + fractal + 1]
        if lows[i] == window.min() and (window == lows[i]).sum() == 1:
            pivots.append((df["datetime"].iloc[i], lows[i]))
    return pivots


def analyze(df: pd.DataFrame, fractal: int, lookback: int):
    recent = df.tail(lookback).reset_index(drop=True)
    if len(recent) < fractal * 2 + 10:
        return {"verdict": "UNKLAR", "reason": "zu wenig Historie fuer eine belastbare Pivot-Analyse"}

    pivots = find_pivot_lows(recent, fractal)
    higher_lows = False
    pivot_note = "keine ausreichende Pivot-Tief-Sequenz gefunden"
    if len(pivots) >= 2:
        last_two = pivots[-2:]
        higher_lows = last_two[1][1] > last_two[0][1]
        pivot_note = (
            f"Pivot-Tiefs {last_two[0][0].date()}={last_two[0][1]:.2f} -> "
            f"{last_two[1][0].date()}={last_two[1][1]:.2f} "
            f"({'steigend' if higher_lows else 'nicht steigend'})"
        )

    ema20 = recent["close"].ewm(span=20, adjust=False).mean()
    close_above_ema20 = recent["close"].iloc[-1] > ema20.iloc[-1]
    ema20_rising = ema20.iloc[-1] > ema20.iloc[-6] if len(ema20) > 6 else False
    ema_signal = close_above_ema20 and ema20_rising

    vol_signal = False
    vol_note = "keine Volumendaten"
    if "volume" in recent.columns and recent["volume"].notna().sum() >= 20:
        vol5 = recent["volume"].tail(5).mean()
        vol20 = recent["volume"].tail(20).mean()
        vol_signal = vol5 > vol20
        vol_note = f"Ø5T={vol5:,.0f} vs Ø20T={vol20:,.0f} ({'erhoeht' if vol_signal else 'nicht erhoeht'})"

    score = sum([ema_signal, vol_signal]) + (1 if higher_lows else 0)
    verdict = "JA" if higher_lows and score >= 2 else "NEIN"

    return {
        "verdict": verdict,
        "higher_lows": higher_lows,
        "pivot_note": pivot_note,
        "ema20_breakout": ema_signal,
        "ema_note": f"Schlusskurs {'ueber' if close_above_ema20 else 'unter'} EMA20, EMA20 {'steigend' if ema20_rising else 'nicht eindeutig steigend'}",
        "volume_confirmation": vol_signal,
        "volume_note": vol_note,
        "score": f"{score}/3 Signale (hoehere Tiefs zaehlen als Vorbedingung)",
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--json", required=True, help="Pfad zur Twelve-Data-time_series-JSON-Datei")
    p.add_argument("--fractal", type=int, default=3, help="Fraktal-Fenster fuer Pivot-Tiefs (Tage vor/nach)")
    p.add_argument("--lookback", type=int, default=60, help="Betrachtungsfenster in Handelstagen")
    args = p.parse_args()

    df = load_series(args.json)
    if df.empty:
        print("Fehler: keine Kursdaten in der JSON-Datei gefunden.", file=sys.stderr)
        sys.exit(1)

    result = analyze(df, args.fractal, args.lookback)
    print("BODENBILDUNG-PROXY (algorithmische Annaeherung, kein echtes Pattern-Matching):")
    print(f"  Verdict: {result['verdict']}")
    for k, v in result.items():
        if k != "verdict":
            print(f"  {k}: {v}")
