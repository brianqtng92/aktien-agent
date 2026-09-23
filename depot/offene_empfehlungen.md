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
| Rambus | US7509171069 | Nachkauf-Zone (Preisalarm) | ≤$68-75 (bestätigt und gestärkt nach Full-Deep-Dive-Refresh 21.09.2026 – deckt sich fast exakt mit dem reconciliierten DCF-Base ~$60-70; Kurs 22.09. (Twelve Data, live) $104,99, Rally setzt sich fort (+8,3% intraday), weiter deutlich über der Zone. Kein neuer fundamentaler Treiber – Form-3-Insider-Meldung/neuer CAO ohne Kursrelevanz.) | RMBS-Full-Deep-Dive-Refresh, 2026-09-21 | 2026-09-01 | 2026-09-17 |
| CBOE Holdings | US12503M1080 | Nachkauf-Zone, gestaffelt (KAUFEN, Tier 2) | Tranche 1: Stabilisierung über $268-270 (~1,5-2%) UND RSI&gt;45/MACD-Boden/OBV-Wende · Tranche 2: $255-262. **22.09. (Twelve Data, live):** Kurs $266,56 (52W-Range $227,15-$371,18) – knapp unter der Zone, kein neuer RSI-Wert in diesem Lauf recherchiert. Hinweis: eine WebSearch-Quelle nannte fälschlich $226,40 (mit Twelve Data widerlegt, siehe websearch_kurse_unzuverlaessig-Regel) – Twelve-Data-Live-Kurs ist hier maßgeblich. Positive Fundamentalnews (19%-Dividendenerhöhung, Q2-EBITDA-Marge ~72%, Barclays Buy/PT $354) unverändert ggü. Full-Deep-Dive. TA-Bestätigung weiterhin nicht erneut geprüft in diesem Lauf, kein Order-Signal. | CBOE-Full-Deep-Dive, 2026-09-16 | 2026-09-16 | – |
| Hermès | FR0000052292 | Nachkauf-Zone quasi wieder erreicht, TA-Bestätigung nicht geprüft (Preisalarm bleibt dokumentiert) | ≤1.350€ (Abstauber-Limit aus RMS-Quick-Filter, 23.08.2026) – **Kurs 23.09. (Scalable Capital, live) 1.350,75€** – **Korrektur eines Fehlfunds:** die am 21.09. per WebSearch (ad-hoc-news.de) gemeldete "Erholung auf 1.597€" war falsch (erneuter Beleg der websearch_kurse_unzuverlaessig-Regel) – per Scalable-Live-Quote UND einer frischen WebSearch-Gegenprobe (die einen Schlusskurs von 1.344€ am 21.09. nennt) widerlegt. Der Kurs hat die Erholung real NIE in diesem Ausmaß vollzogen und notiert jetzt praktisch exakt auf dem Abstauber-Limit. Kein neuer fundamentaler Negativ-Treiber gefunden (RBC-PT-Kürzung auf 1.600€, Bernstein auf 1.750€ + Q3-Wachstumsschätzung von 6,4% auf 4,7% gesenkt – beides bereits vor diesem Lauf bekannte Analysten-Reaktionen, kein frischer Schock). Keine RSI-/TA-Bestätigung in diesem Lauf geprüft – daher kein Order-Signal, aber Zone-Status jetzt korrekt als "erreicht" statt "verlassen" dokumentiert. | RMS-TMR-Quick-Filter (23.08.2026) + Blitz-Scan-Preiskorrektur (2026-09-23) | 2026-09-18 | – |

## Format bei neuem Eintrag
`| Position | ISIN | Empfehlung (KAUFEN/NACHKAUFEN/VERKAUFEN/TEILVERKAUF) | Zone/Preis | Quelle (Analyse-Datei oder Report) | Datum | Zuletzt erinnert (– falls noch nie) |`

## Entfernt wird ein Eintrag, wenn:
- eine entsprechende Transaktion erkannt wird (Scalable: `list_portfolio_transactions`; manuelle Broker: Brian bestätigt es im Chat oder aktualisiert die jeweilige `depot/*.md`),
- eine neue Analyse die Empfehlung explizit ersetzt/aufhebt (z.B. KAUFEN → BEOBACHTEN),
- Brian die Position manuell als "erledigt/verworfen" markiert.
