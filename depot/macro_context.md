---
Datei: Tägliche Markt-/Makro-Kontext-Momentaufnahme + langfristiger politischer/Notenbank-Kalender
Angelegt: 2026-09-03, erweitert 2026-09-03 (S&P-Level, Wahlkalender, Fed-Pfad, weitere Dimensionen)
Zweck: Tag-über-Tag-Vergleichsbasis für den täglichen Markt-/Makro-Check
(siehe architecture.md, Abschnitt 5, "[D] CASH-ALLOKATIONS-CHECK / TÄGLICHER
MARKT-/MAKRO-KONTEXT" inkl. Erweiterung). Wird vom Täglichen Trigger-Check
gepflegt: pro Tag eine neue Zeile anhängen, Material-Shift-Kriterien gegen
die VORHERIGE Zeile prüfen. Der Kalender-Teil unten wird primär im
Wochenfazit gepflegt (langsamer bewegliche Termine), der Trigger-Check
erinnert nur ab ca. 14 Tage vor einem eingetragenen Termin. Kein Ersatz für
den tieferen monatlichen Makro-Rückblick im Monatsrecap - reine tägliche/
wöchentliche Momentaufnahme, bewusst kompakt. Keine erfundenen exakten
Wahrscheinlichkeiten (No-False-Precision-Regel) - Einordnungen immer
qualitativ + quellenbasiert.
---

## Tagesprotokoll

| Datum | Fear&Greed (Zone) | VIX | S&P 500 (Stand, Tagesänd.) | S&P vs. 50D/200D-SMA | Nasdaq 100 Tagesänd. | US-10J-Rendite | Kurve | EUR/USD | Gold | Investitionsklima | Auffälligkeit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-01 (Referenz, nachträglich recherchiert) | n/v (nicht Teil dieser Ad-hoc-Recherche) | n/v | 7.631,47 (Schlusskurs) | über 50D-SMA (7.567,50) UND über 200D-SMA (7.124,79), 200D-SMA-Richtung: steigend | n/v | n/v | n/v | n/v | n/v | tendenziell konstruktiv (Kurs über beiden SMAs, steigende 200D-Linie) | Erster Eintrag, per Ad-hoc-Recherche am 2026-09-03 nachträglich befüllt, kein vollständiger Tagesscan - ab dem nächsten regul. Trigger-Check-Lauf vollständige Zeilen |

<!-- Format je Zeile: Datum YYYY-MM-DD | Fear&Greed-Wert + Zone | VIX-Stand | S&P-Stand + Tagesänderung in % | Kurs relativ zu 50D/200D-SMA + Richtung der 200D-SMA (steigend/flach/fallend - wichtig für die Korrektur-Risiko-Einordnung, siehe architecture.md) | NQ100-Tagesänderung in % | US-10J-Rendite in % | normal/invers/flach | EUR/USD-Kurs | Gold-Preis (USD/oz) | eher günstig für Zukäufe / neutral / eher Vorsicht-Cash-halten, mit 1-Satz-Begründung | kurzer Hinweis bei Material-Shift, sonst "-" -->

## Politischer/Wahl- & Notenbank-Kalender (langfristiger Horizont, primär im Wochenfazit gepflegt)

| Datum | Ereignis | Relevanz | Status |
|---|---|---|---|
| 2026-09-09/10 | EZB-Ratssitzung (Zinsentscheid) | Europa-Exposure via Allianz, Münchener Rück, ASML, Hermès - Sondertermin diesmal in Berlin (Bundesbank), sonst kein Unterschied. | anstehend |
| 2026-09-15/16 | FOMC-Sitzung (inkl. Dot Plot/SEP) | Fed-Funds-Zielkorridor aktuell 3,50-3,75% (Stand 2026-09-01) | anstehend |
| 2026-09-16/17 | BoJ-Sitzung (Zinsentscheid) | Japan-Exposure zahlreicher Depot-/Watchlist-Werte (Hoya, Disco, Lasertec, Rorze, Asahi Intecc, Keyence u.a.) - Yen-Zinspfad wirkt sowohl auf Kurse als auch EUR/JPY-Umrechnung. | anstehend |
| 2026-10-27/28 | FOMC-Sitzung | - | anstehend |
| 2026-10-28/29 | EZB-Ratssitzung (Zinsentscheid) | siehe oben | anstehend |
| 2026-10-29/30 | BoJ-Sitzung (Zinsentscheid, inkl. Outlook Report) | siehe oben | anstehend |
| 2026-11-03 | US-Midterms | historisch oft erhöhte Vorfeld-Volatilität, kein verlässliches Muster pro Zyklus | anstehend, ab ca. 2026-10-20 im Trigger-Check als "bald"-Hinweis |
| 2026-12-08/09 | FOMC-Sitzung (inkl. Dot Plot/SEP) | - | anstehend |
| 2026-12-16/17 | EZB-Ratssitzung (Zinsentscheid) | siehe oben | anstehend |
| 2026-12-17/18 | BoJ-Sitzung (Zinsentscheid) | siehe oben | anstehend |

<!-- Format je Zeile: Datum | Ereignis (FOMC-Sitzung/EZB-Sitzung/BoJ-Sitzung/Wahl/Debt-Ceiling-Frist/sonstiges) | Relevanz-Kurzsatz | Status (anstehend/erledigt+Ergebnis). Vollständigen 2026er-FOMC-Kalender siehe architecture.md Abschnitt 5. EZB-/BoJ-Termine hier per WebSearch (ecb.europa.eu, boj.or.jp) recherchiert am 2026-09-04, Rest-2026-Jahr - Debt-Ceiling-Fristen bei Bekanntwerden ergänzen. -->

## Weitere Dimensionen (wöchentlich im Wochenfazit gepflegt, nicht täglich)

_Noch kein Eintrag - DXY, High-Yield-Credit-Spreads, Öl/Energie, China-Regulatorik/Konjunktur ab dem nächsten Wochenfazit._
