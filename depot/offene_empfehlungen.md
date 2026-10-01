# Offene Kauf-/Verkauf-Empfehlungen

**Zweck (2026-09-03, von Brian gefordert):** Liste aller aktuell offenen,
noch nicht ausgeführten Kauf-/Nachkauf-/Verkauf-/Teilverkauf-Empfehlungen.
Wird vom Täglichen Trigger-Check geführt: neue Empfehlungen werden
eingetragen, ausgeführte oder durch neue Analysen überholte Empfehlungen
werden entfernt, offene Empfehlungen ab einem gewissen Alter erneut
per Chat + E-Mail in Erinnerung gebracht (nicht täglich, um Ermüdung zu
vermeiden – siehe Agent-Playbook.md "Erinnerungs-Mechanismus für offene
Empfehlungen").

| Position | ISIN | Empfehlung | Zone/Preis | Quelle | Datum | Zuletzt erinnert |
|---|---|---|---|---|---|---|
| Kraken Robotics | CA50077N1024 | Nachkauf-Zone (Preisalarm) | ≤2,80 CAD (Downside-Alert aktiv) | E-Mail "Zwei Zonen im Blick", 2026-09-01 | 2026-09-01 | 2026-09-17 |
| Rambus | US7509171069 | Nachkauf-Zone (Preisalarm) | ≤$68-75 (bestätigt und gestärkt nach Full-Deep-Dive-Refresh 21.09.2026 – deckt sich fast exakt mit dem reconciliierten DCF-Base ~$60-70; **Kurs 25.09. (stockanalysis.com, Twelve Data diese Session nicht verbunden) $105,16**, weiterhin deutlich über der Zone, Rally seit 21.09. im Wesentlichen gehalten. Kein neuer fundamentaler Treiber.) | RMBS-Full-Deep-Dive-Refresh, 2026-09-21 | 2026-09-01 | 2026-09-17 |
| CBOE Holdings | US12503M1080 | Nachkauf-Zone, gestaffelt (KAUFEN, Tier 2) | Tranche 1: Stabilisierung über $268-270 (~1,5-2%) UND RSI&gt;45/MACD-Boden/OBV-Wende · Tranche 2: $255-262. **28.09. (stockanalysis.com, Twelve Data diese Session nicht verbunden):** Kurs $258,03 (-3,6% Tagesverlust am 25.09., trotz eines an diesem Tag steigenden Gesamtmarkts – passt zu einem Treasury-Yield-Anstieg, der zinssensitive Finanzinfrastruktur-Werte belastet) – **jetzt INNERHALB der Tranche-2-Zone ($255-262)**, ein deutlicher Sprung ggü. 22.09. ($266,56, noch über beiden Zonen). Keine frische RSI-/TA-Bestätigung in diesem Lauf geprüft – vor einer Order-Entscheidung nachholen. | CBOE-Full-Deep-Dive, 2026-09-16 | 2026-09-16 | – |
| innoscripta SE | DE000A40QVM8 | Stop-Loss + Teilverkauf-Plan (von Brian selbst gesetzt, bewusster Zock) | **Stop-Loss 36,50-36,90€** (knapp unter Einstand 38,05€, Risiko: Whipsaw bei hoher Volatilität/Gap-Risiko bei Scale-Segment-Liquidität) · **Teilverkauf bei +15-20%** (~43,76-45,66€, Technik-Trigger, keine Fundamental-Entwarnung). Hintergrund: Kauf am Tag einer Durchsuchung wegen Forschungszulage-Betrugsverdacht, siehe `depot/finanzen-net-zero.md`. | Chat 01.10.2026 | 2026-10-01 | – |

## Format bei neuem Eintrag
`| Position | ISIN | Empfehlung (KAUFEN/NACHKAUFEN/VERKAUFEN/TEILVERKAUF) | Zone/Preis | Quelle (Analyse-Datei oder Report) | Datum | Zuletzt erinnert (– falls noch nie) |`

**Entfernt 2026-09-24:** Hermès-Zeile entfernt – Position von Brian komplett verkauft (@ 1.362,00 €), Empfehlung damit gegenstandslos. Details `depot/finanzen-net-zero.md`.

## Entfernt wird ein Eintrag, wenn:
- eine entsprechende Transaktion erkannt wird (Scalable: `list_portfolio_transactions`; manuelle Broker: Brian bestätigt es im Chat oder aktualisiert die jeweilige `depot/*.md`),
- eine neue Analyse die Empfehlung explizit ersetzt/aufhebt (z.B. KAUFEN → BEOBACHTEN),
- Brian die Position manuell als "erledigt/verworfen" markiert.
