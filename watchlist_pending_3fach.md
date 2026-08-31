---
Datei: Warteschlange für offene 3-fach-Bestätigungen (täglicher Kandidaten-Scan)
Angelegt: 2026-08-29
Zweck: Kandidaten aus dem täglichen automatisierten Kandidaten-Scan (siehe
architecture.md, "Watchlist-System" → "Täglicher automatisierter
Kandidaten-Scan"), die das Strategie-Fit-Gate, den Duplikations-Check und
das Identity-Gate bereits bestanden haben, deren 3-fach-Quick-Filter
(Jarvis/Jack/Conan) aber mangels verbundenem Chrome-Browser nur als
Jarvis-Only-Vorabbefund vorliegt. Diese Datei wird vom täglichen Trigger-
Check automatisch gepflegt (Schritt 3b): bei jedem Lauf zuerst prüfen, ob
hier offene Einträge stehen und Chrome JETZT verbunden ist - falls ja, die
fehlende Jack/Conan-Bestätigung nachholen und den Eintrag danach nach
"Erledigt" verschieben (aufgenommen in watchlist.md ODER verworfen).
NIEMALS wird ein Eintrag hier allein auf Jarvis-Basis in watchlist.md
übernommen - das widerspräche der von Brian am 2026-08-29 festgelegten
Regel "immer alle drei KIs, auch im Quick-Filter".
Zuletzt aktualisiert: 2026-08-29 (Datei angelegt, noch keine echten Einträge)
---

## Offene Kandidaten (warten auf Jack+Conan-Bestätigung)

_Aktuell leer - wird vom täglichen Trigger automatisch befüllt, sobald ein
Kandidat mangels Browser-Zugriff zurückgestellt werden muss._

<!-- Format je Eintrag, vom täglichen Trigger beim Zurückstellen so anzulegen:

### TICKER - Firmenname
- Gefunden am: YYYY-MM-DD (Quelle: welcher Index/Sektor-Ausschnitt, z.B. "Russell 2000, Sektor Industrials")
- Jarvis-Vorabbefund: KAUFEN / BEOBACHTEN / SCHROTT (Reaper-Score, grobe Ampel), kurze 1-2-Satz-Begründung
- Strategie-Fit-Gate: bestanden (Kategorie-Kandidat: Champions/Profi/Talent, ggf. Zeithorizont-Tag)
- Duplikations-Check ggü. FTSE-All-World-ETF: bestanden
- Identity-Gate: bestanden (Ticker/ISIN/Börsenplatz/Land/Sektor)
- Zurückgestellt seit: YYYY-MM-DD
- Status: wartet auf Jack+Conan-Bestätigung

-->

## Erledigt (Historie, jeweils letzte 15 Einträge behalten, ältere löschen)

_Noch keine erledigten Einträge._

<!-- Format je erledigtem Eintrag:

### TICKER - Firmenname
- Zurückgestellt: YYYY-MM-DD → Nachgeholt: YYYY-MM-DD
- Ergebnis: AUFGENOMMEN in watchlist.md (Kategorie: ...) / VERWORFEN (Grund: ...)

-->
