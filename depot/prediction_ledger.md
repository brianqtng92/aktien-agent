---
Datei: Prediction Ledger / Decision Journal
Angelegt: 2026-09-03 (Lücke geschlossen - Mechanismus war seit 2026-08-30 in
architecture.md als "aktiv" dokumentiert, aber die Datei existierte nicht und
kein einziger Eintrag wurde je angelegt; im 3-KI-System-Audit vom 2026-09-03
gefunden und rückwirkend geschlossen)
Zweck (siehe architecture.md, "Meta-Retrospektive", Phase 2): systematisches
Nachhalten der eigenen Prognosen, damit sich das System über die Zeit
kalibrieren kann - ohne das bleibt jede noch so saubere Kriterien-Logik
unüberprüft. Ausdrücklich KEIN Scoring zwischen Jack/Jarvis/Conan - dient dem
Lernen des Gesamtsystems, nicht einem Ranking der drei KIs.

Ein Eintrag pro NEUER Kauf-/Watchlist-Empfehlung (Pflichtfelder zum
Zeitpunkt der Empfehlung, nicht rückwirkend änderbar). Bestehende
Depot-Positionen von vor 2026-08-30 werden NICHT auf einmal rückwirkend
befüllt, sondern schrittweise beim jeweils nächsten regulären
[B] THESE-CHECK nachgetragen (siehe Täglicher Trigger-Check/Wochenfazit).

Post-Mortem-Kadenz: bei Fälligkeit des Prüf-Zeithorizonts (6/12/24 Monate)
vergleicht der Agent die tatsächliche Entwicklung gegen die damalige
Erwartung und trägt das Ergebnis nach - geprüft im jeweiligen Monatsrecap,
nicht als tägliche Meldung.
---

## Offene Einträge (Prüf-Zeithorizont noch nicht erreicht)

### 2026-08-31 — Disco Corp. (6146, Tokyo, JP3548600000)
- **Kategorie:** Profi (Bucket C, Mispricing/Re-Rating-Kandidat - nicht Bucket A, da Kapitalallokation/Beta-Unsicherheit gegen einen reinen Compounder-Fall sprechen) · TMR-Pfad
- **Empfehlungs-Typ:** Watchlist-Aufnahme (KEIN Kauf-Rating) - Rating bei Aufnahme: BEOBACHTEN, unverändert zwischen Quick Filter und Full Deep Dive
- **Zentrale These:** Weltmarktführer (60-70% Anteil) bei Präzisions-Wafer-Dicing/-Grinding mit außergewöhnlichem ROIC (~33%) und operativer Marge (42-44%), praktisch schuldenfrei - aber Bewertung (KGV ~50x TTM) lässt bei aktueller FCF-Marge (16,9%, unter der 20%-Schwelle) und aggressiver Kapazitätsausbauphase keine Sicherheitsmarge für einen Einstieg JETZT.
- **Konkrete Erwartung (Fair-Value-Bandbreite, Base-Case DCF):** je nach Beta-Annahme −31% bis −58% ggü. damaligem Kurs (¥62.260) - Spanne bewusst breit, weil die Beta-Frage (0,?? vs. 1,02 je Quelle) den Fair Value um ±30+ Prozentpunkte verschiebt. Reverse-DCF: Markt preist 17-27% langfristiges Wachstum ein, plausibel bis grenzwertig ambitioniert je nach Szenario.
- **These-Bruch-Kriterien:** (a) FCF-Marge erholt sich NICHT innerhalb 2-4 Quartalen deutlich Richtung 20%-Schwelle trotz auslaufender Kapex-Phase → strukturelles statt zyklisches Problem; (b) Marktanteilsverlust an GL Tech (China) wird dokumentiert bestätigt; (c) Management-Score (aktuell 1/3, keine Rückkäufe trotz Netto-Cash) verbessert sich nicht.
- **Beobachtungs-/Nachkauf-Trigger:** Kursrücksetzer Richtung ¥45.000 (ca. -28-32% vom damaligen Niveau) ODER deutliche FCF-Marge-Erholung.
- **Prüf-Zeithorizont:** 12 Monate (2027-08-31) - Halbleiterausrüstung ist zyklisch, ein 6-Monats-Fenster wäre zu kurz für eine faire Bewertung der These.
- **Status (2026-09-03, nachrichtlich, ändert den ursprünglichen Eintrag nicht):** Re-Check am 2026-09-03 bestätigte BEOBACHTEN unverändert, KI-Ratings liefen dabei allerdings methodisch auseinander (Jarvis ABBRUCH/Jack SCHROTT/Conan BEOBACHTEN 5,5) - Detail siehe `analysen/6146-cross-check-fazit-2026-09-03.md`, ändert nichts an diesem Ledger-Eintrag selbst.

### 2026-09-02 — Asahi Intecc Co. (7747, Tokyo, JP3110650003)
- **Kategorie:** Talent (Bucket B, Quality in Formation - noch nicht ausreichend primärquellen-verifiziert für Bucket A) · TMR Quick Filter
- **Empfehlungs-Typ:** Watchlist-Aufnahme (KEIN Kauf-Rating) - gemischtes Cross-Check-Ergebnis (Jarvis ABBRUCH-Datenlücke / Jack SCHROTT-1 / Conan BEOBACHTEN-6), einstimmig aber "watchlist-würdig aufgrund starker operativer Kennzahlen"
- **Zentrale These:** Weltmarktführer bei Katheter-Führungsdrähten (Guidewires), verifiziert starke operative Kennzahlen (ROIC/ROCE 23,21%, operative Marge 29,71%, Umsatzwachstum +21,2% YoY, Nettogewinn +151,8% YoY) - aber konzentriertes Nischengeschäft und mehrere K-Kriterien (FCF-Marge, Piotroski, Net Debt/EBITDA, 5J-EPS-CAGR) mangels Primärquelle nicht verifizierbar, daher kein vollwertiges Rating möglich.
- **Konkrete Erwartung:** Mehrjahres-Umsatz-CAGR ~18,78% (2022-2028E, teils Prognose); Analysten gespalten (Nomura Hold 3.500 JPY vs. Citi Buy 5.400 JPY bei damaligem Kurs 3.601 JPY) - keine belastbare eigene Fair-Value-Spanne möglich, solange FCF-/Bilanzdaten fehlen (explizit als Einschränkung dokumentiert, keine erfundene Zahl).
- **These-Bruch-Kriterien:** (a) Primärquellen-Recherche (SEC/IR) bestätigt FCF-Marge dauerhaft schwach; (b) Umsatzwachstum bricht spürbar unter die ~19%-CAGR-Erwartung ein; (c) Kundenkonzentrationsrisiko materialisiert sich (bisher nicht quantifiziert, nur als Risiko benannt).
- **Beobachtungs-/Nachkauf-Trigger:** Abstauber-Limit 3.150 JPY (Conans vorläufige Orientierung, NICHT als bestätigtes Urteil markiert) ODER vollständige K-Kriterien-Verifikation über echte Primärquellen ermöglicht ein belastbares volles Rating.
- **Prüf-Zeithorizont:** 6 Monate (2027-03-02) - kürzeres Fenster als Disco Corp, weil die offene Frage hier primär Datenverfügbarkeit ist (schneller klärbar), nicht ein mehrjähriger Zyklus.

## Erledigt (Post-Mortem abgeschlossen)

_Noch keine fälligen Einträge._

<!-- Format je Post-Mortem-Eintrag:

### [Ursprüngliches Datum] — Ticker (verschoben aus "Offene Einträge")
- Ergebnis nach Ablauf des Prüf-Zeithorizonts: Base-Case getroffen? Näher an Bear oder Bull? These-Bruch-Kriterium eingetreten, obwohl noch gehalten/beobachtet, oder umgekehrt?
- Tatsächliche Kursentwicklung seit Empfehlung.
- Kurzes, ehrliches Fazit - kein Schönreden.

-->
