# Master-Status – Aktien-Agent (Brian)

**Zweck (2026-09-04, von Raketentonis "Master-Status"-Konzept übernommen,
siehe architecture.md "Informations-Vorrang-Hierarchie" für die
vollständige Einordnung):** EIN konsolidiertes Status-Dashboard für den
schnellen Überblick – v.a. beim Einstieg in einen neuen Chat oder
Scheduled-Task-Lauf ohne Erinnerung an vorherige Sessions, damit nicht
6+ Einzeldateien gelesen werden müssen, um den aktuellen Stand zu
verstehen. **Ersetzt NICHT die Detail-Dateien** – für die vollständige
Begründung/Historie einer einzelnen Position bleiben
`depot/kategorisierung.md`, `watchlist.md` etc. maßgeblich. Wird am Ende
jedes `taeglicher-trigger-check`- und `wochenfazit`-Laufs aktualisiert.

**Zuletzt aktualisiert:** 2026-09-04, ~22:35 (ad-hoc, nach Anlage dieser
Datei) – nächste reguläre Aktualisierung beim nächsten
`taeglicher-trigger-check`-Lauf.

---

## 1. Kategorie-Struktur Depot ("10-7-3"-Ziel)

| Kategorie | Ziel | Ist | Freie Slots |
|---|---|---|---|
| Champions | 10 | 10 | exakt auf Ziel |
| Profi | 7 | 7 | exakt auf Ziel |
| Talent | 3 | 1 | **2 frei** |

Quelle: `depot/kategorisierung.md`, Abschnitt "Ziel-Positionsanzahl".
Talent liegt seit heute unter statt auf Ziel (Kraken Robotics + HawkEye 360
wurden zu Profi hochgestuft) – kein Verkaufssignal, reine Folge korrigierter
Fehlzuordnungen.

## 2. Kategorie-Struktur Watchlist (30 Werte gesamt)

| Kategorie | Anzahl |
|---|---|
| Champions | 17 |
| Profi | 10 |
| Talent | 3 |

Quelle: `watchlist.md`, "Aktueller Stand".

## 3. Offene Prüfpunkte / Checkpoints (chronologisch, wo bekannt)

| Position | Kontext | Kategorie | Prüfpunkt-Termin/Auslöser |
|---|---|---|---|
| Cellebrite DI Ltd | Depot, Profi | Guidance-Cut-Nachprüfung | Q3-Earnings (~Nov 2026), Guidance $145-148 Mio – dann 3 Re-Rating-Trigger neu prüfen |
| Rocket Lab USA | Depot, Talent | Nachkauf-Aufstufungs-Trigger | Q3-Zahlen (Guidance: Umsatz $250-265 Mio, Adj.-EBITDA-Verlust $17-23 Mio) – Neutron-Erstflug/Verwässerungstempo/Burn-Multiple prüfen |
| Rollins (ROL) | Watchlist, Profi (abgestuft 04.09.) | mögliche Rückstufung zu Champions | H2-2026-Verbesserung laut Management-Guidance – noch unbestätigt |
| Fair Isaac (FICO) | Watchlist, Champions (Beobachtungspunkt) | mögliche Abstufung zu Profi | belastbare Daten zur VantageScore-Adoptionsrate bei GSE-Hypotheken |
| Constellation Software | Depot, Champions (Beobachtungspunkt) | organisches Wachstum | Q4 2026/Q1 2027 – sollte Richtung 5-6% zurückkehren |
| MercadoLibre | Depot, Champions (Beobachtungspunkt) | operative Marge | Q4 2026/Q1 2027 – sollte sich Richtung zweistellig erholen |
| Münchener Rück | Depot, Champions (Beobachtungspunkt) | Rückversicherungs-Preiszyklus | Januar-2027-Erneuerungen + FY2026-Combined-Ratio vs. ~80%-Guidance |
| Bank Central Asia | Depot, Champions (Beobachtungspunkt) | NIM-Erholung | nächste 2-3 Quartale, sollte sich mit BI-Zinsstabilisierung erholen |
| Rorze (6323) | Watchlist, Talent (durchgefallen 04.09.) | Neubewertung möglich | Quartalszahlen 08.10.2026 – bei zweistelligem Wachstum + gehaltener Marge |
| Watsco (WSO) | Depot, Profi (Beobachtungspunkt) | Margen-Normalisierung | nächste 1-2 Quartale beobachten |

## 4. Offene Kauf-/Verkauf-Empfehlungen

Quelle: `depot/offene_empfehlungen.md` (dort maßgeblich, hier nur Kurzstand).

| Position | Empfehlung | Zone/Preis |
|---|---|---|
| Kraken Robotics | Nachkauf-Zone (Preisalarm) | ≤2,80 |
| Rambus | Nachkauf-Zone (Preisalarm) | ≤65 |

## 5. Offene Portfolio-Regel-Fragen (noch nicht live verifiziert)

**Wichtig:** die folgenden Zahlen sind grobe Schätzungen aus einer
manuellen Überschlagsrechnung (04.09.2026, Ad-hoc-Diskussion), NICHT aus
einer echten Live-Berechnung mit exakten ETF-Binnengewichten – siehe
Regionen-Frage unten. Nächster `wochenfazit`-Lauf sollte den echten
Portfolio-Regel-Check (Region/Sektor-Bänder) mit sauberen Daten
durchführen und diese Zeile ersetzen.

| Topf | Geschätzt | Ziel-Band | Status |
|---|---|---|---|
| USA/Nordamerika (inkl. Kanada) | ~64% | ≤55-60% | möglicherweise über Cap – zu verifizieren |
| Japan/Asien | ~9% | 10-15% | unterbesetzt |

## 6. Offene gezielte Kandidatensuchen (Portfolio-Lücken-Regel)

| Lücke | Zuletzt geprüfter Kandidat | Ergebnis | Nächster Schritt |
|---|---|---|---|
| Talent-Slot + Japan/Asien-Region | Rorze (6323) | Durchgefallen (3-fach Scout-Check, 04.09.2026) – Moat 2/4, Wachstum eingebrochen | Vollständige Nikkei225/TOPIX-Durchsuchung noch ausstehend (siehe architecture.md "Automatisierte Portfolio-Lücken-Kandidatensuche-Pflicht") – nächster `taeglicher-trigger-check`-Lauf sollte damit beginnen |

## 7. Letzte Scheduled-Task-Läufe

Quelle: `depot/bridge_status.md` (Log) + `list_scheduled_tasks` (Live-Stand).

| Task | Letzter Lauf | Nächster Lauf |
|---|---|---|
| taeglicher-trigger-check | 2026-09-04 ~20:35 UTC (3. Durchlauf, siehe Auffälligkeiten in bridge_status.md) | täglich ~21:03 lokale Zeit |
| blitz-scan | 2026-09-04 ~16:15 UTC (Bridges FAIL, Jarvis-Only) | stündlich |
| wochenfazit | noch nicht gelaufen | Freitag, ~22:03 lokale Zeit |
| monatsrecap | noch nicht gelaufen | 28.-31. des Monats |

## 8. Cash-Stand (nur Scalable Capital, live abrufbar)

Verfügbare Kaufkraft: 460,33 € (Stand 2026-09-04, Cash-Bestand 1.060,33 €,
teilweise durch ETF-Sparplan gebunden). Für die drei manuellen Broker
(finanzen.net zero, Trade Republic, Smartbroker+) kein Live-Zugriff –
siehe jeweilige `depot/*.md`-Datei für den zuletzt gemeldeten Stand.
