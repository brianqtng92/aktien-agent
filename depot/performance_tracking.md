# Portfolio-Performance-Tracking vs. Markt (ab 2026-08-30, korrigiert)

**Methodik (von Brian gewählt, 2026-08-29):** Vorwärts-Tracking ab heute, kein
rückwirkender Vergleich. Heutiger Gesamt-Depotwert = Startpunkt (Index 100),
ebenso die Stände von S&P 500, Nasdaq 100 und MSCI World (Proxy) am selben Tag.
Jede Woche (im Rahmen des Wochenfazit-Laufs, freitags) wird der aktuelle
Depotwert sowie die aktuellen Indexstände erfasst und die prozentuale
Veränderung seit dem Startdatum verglichen — Depot vs. jeder der drei Indizes.

**Korrektur der Baseline (2026-08-30, von Brian entschieden):** Die
ursprüngliche Baseline vom 29.08.2026 (33.403,32 €) kannte die Scalable-
Capital-Live-Anbindung noch nicht und war dadurch zu niedrig – ihr fehlten die
neu entdeckte Gold-Position, +600 € Cash sowie ein paar frisch abgerufene
Live-Kurse (siehe `architecture.md`, "Broker-Anbindung Scalable Capital").
Startpunkt wurde deshalb auf **30.08.2026, 35.034,17 €** korrigiert – die
einzige Anpassung dieser Art, ab jetzt gilt der neue Startpunkt fest.

**Wichtige Einschränkung:** Reines Vorwärts-Tracking ab dem Start der
Beobachtung, keine Aussage über die Performance seit den tatsächlichen
Kaufdaten der einzelnen Positionen (die liegen teils deutlich vor dem
30.08.2026 und haben teils schon Gewinne/Verluste, siehe
`finanzen-net-zero.md`). Außerdem wird die Fremdwährungs-Bewegung (USD/EUR)
bei S&P 500 und Nasdaq 100 NICHT herausgerechnet — verglichen wird die
Index-Eigenperformance in der jeweiligen Notierungswährung, nicht
währungsbereinigt gegen den Euro-Depotwert. Das ist eine bewusste
Vereinfachung (Brian ist in der Aufbauphase, es geht primär um die
Wachstumsrate, nicht um eine exakte währungsbereinigte Renditevergleichsgröße).

## Baseline (Startpunkt 30.08.2026, korrigiert)

| Kennzahl | Wert | Datum/Quelle |
|---|---|---|
| Gesamt-Depotwert (Portfolio, alle Positionen inkl. ETF, exkl. Gold-ETC-Sonderstellung s.o.) | 35.034,17 € | Stand 30.08.2026, nach Scalable-Live-Abgleich korrigiert |
| S&P 500 (^GSPC) | 7.711,76 USD | Schlusskurs 28.08.2026 (letzter Handelstag vor dem Wochenende), Yahoo Finance |
| Nasdaq 100 (^NDX) | 29.433,43 USD | Schlusskurs 28.08.2026, Yahoo Finance |
| MSCI World (Proxy: iShares Core MSCI World UCITS ETF, IE00B4L5Y983) | 127,735 EUR | 28.08.2026, 20:55 Uhr, onvista.de |

## Verlaufs-Tabelle (wird jede Woche im Wochenfazit-Lauf ergänzt)

| Datum | Depotwert | Depot % seit Start | S&P 500 | S&P % seit Start | Nasdaq 100 | Nasdaq % seit Start | MSCI World (Proxy) | MSCI % seit Start | Schlägt Brian den Markt? |
|---|---|---|---|---|---|---|---|---|---|
| ~~29.08.2026~~ | ~~33.403,32 €~~ | ~~0,0%~~ | ~~7.711,76~~ | ~~0,0%~~ | ~~29.433,43~~ | ~~0,0%~~ | ~~127,735 €~~ | ~~0,0%~~ | verworfen, siehe Korrektur oben |
| 30.08.2026 | 35.034,17 € | 0,0% | 7.711,76 | 0,0% | 29.433,43 | 0,0% | 127,735 € | 0,0% | Neuer Startpunkt, noch kein Vergleich möglich |

## Prozess für den wöchentlichen Wochenfazit-Lauf (freitags)

1. Aktuellen Gesamt-Depotwert neu berechnen (wie beim Rendite-Chart:
   Investsumme+Saldo bzw. frisch abgerufene Live-Kurse je Position, siehe
   `finanzen-net-zero.md`).
2. Aktuelle Stände von S&P 500, Nasdaq 100 und dem MSCI-World-Proxy per
   WebSearch/WebFetch abrufen (gleiche Quellen wie Baseline, damit die Reihe
   konsistent bleibt).
3. Prozentuale Veränderung seit 30.08.2026 für Depot und alle drei Indizes
   berechnen, neue Zeile an die Verlaufs-Tabelle oben anhängen.
4. Kurzer Kommentar in der neuen Zeile bzw. im Wochenfazit-Text: schlägt das
   Depot aktuell den Markt (welchen Index konkret) oder liegt es zurück?
5. Ergebnis fließt ins Wochenfazit-PDF (eigene Kennzahlen-Zeile/Chart, siehe
   architecture.md Abschnitt 5) UND in den Chat-Kurztext.
