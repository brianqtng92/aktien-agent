# Changelog — Aktien-Agent System

Chronologisches Änderungsprotokoll für Agent-Playbook.md, die Methodik-Dateien (Jack/Conan/TA), Report-Formate und die Automatisierungs-Infrastruktur. Ergänzt (ersetzt nicht) die ausführlichen Herkunfts-/Begründungs-Notizen direkt in Agent-Playbook.md und HANDOVER.md — hier geht es um schnelle Scanbarkeit "was änderte sich wann", ohne das ganze Regelwerk lesen zu müssen. Neueste Einträge oben.

**Pflege (neu, 2026-09-09, Priorität 4 aus dem Playbook-Meta-Review):** Jede
künftige substantielle Änderung an Agent-Playbook.md, den Methodik-Dateien
(`prompts/*.md`) oder den Hermes-`SKILL.md`-Dateien bekommt zusätzlich zur
bisherigen inline-Dokumentation (Herkunft/Begründung direkt im Regeltext)
einen Kurz-Eintrag hier — ein Satz, Datum, betroffene Datei(en). Ausgelöst
durch die Erkenntnis, dass Agent-Playbook.md (6.000+ Zeilen) allein durch
inline-Versionierungsnotizen kaum noch überblickbar ist. Zusätzlich: **beim
ersten Playbook-editierenden Chat jedes Kalendermonats** einmal kurz prüfen
(siehe Agent-Playbook.md "Wartung & Redundanz-Check"), ob sich in den
letzten Wochen echte Redundanz angesammelt hat (mehrfach fast wortgleiche
Regeln, wie beim Conan-Prompt-Fund vom 08.09.) — bei Fund: verschlanken wie
bereits einmal geschehen (siehe 2026-09-08 unten), nicht stillschweigend
weiter anwachsen lassen.

---

## 2026-09-09

- Playbook-Härtung Prio 1+2: feste Primärquellen + Bridge-Health-Check/Fallback
- Playbook-Härtung Prio 3: Selbstwiderspruch-Check als achter Standard-Klarstellungsblock (HANDOVER.md 10.13) — gilt jetzt für ALLE Kennzahlen bei jedem Bridge-Aufruf, nicht nur die 5 Kennzahlen aus dem Primärquellen-Standard
- Playbook-Härtung Prio 4: dieses CHANGELOG.md angelegt (aus git log rekonstruiert) + monatlicher Redundanz-Check-Prozess dokumentiert

## 2026-09-08

- A10 Networks (ATEN): zweiter Full Deep Dive mit 10-Seiten-Rigor-Standard
- Widerspruch bei A10-Schulden-Zahl behoben + neue Cross-Check-Pflicht
- Umsatz-/OCF-Grafiken + Dividendenrendite in beide Deep Dives eingebaut
- Peer-Tabellen um Operating-Margin/Median erweitert, DCF-Kernannahmen ergaenzt
- DNA-Check-Datentyp-Tags als Farb-Badges statt Klammer-Text
- Jack-Prompt v11.9 -> v11.10: Persona/Sarkasmus raus, Makro zentralisiert, JSON-Summary ergaenzt
- Conan-Prompt v1.12 -> v1.13: symmetrisches JSON-Summary; Hermes-Job statt neuem Job erweitert
- Master-Agent bekommt einen Namen: Aegis
- Hermes-Gedaechtnis-Synchronisations-Pflicht dokumentiert + SKILL.md-Dateien nachgezogen
- Conan-Prompt v1.14 -> v1.15: Regeln 19-42 auf Kurzverweise gekuerzt (Redundanz-Fund)
- Conan-Prompt v1.15 -> v1.16: gezielte N/V-Ausnahme gegen Datenverfuegbarkeits-Bias
- On-Demand-Analyse-Trigger dokumentiert (Watchlist-Zusatz + E-Mail)
- Agent Deep Dive Report: Scout-Pfad-Mapping dokumentiert
- Blitz-Scan 08.09.: On-Demand-Watchlist-Trigger VEIL dokumentiert (Methodik-Mismatch, Fonds statt Einzelwert)
- VEIL-Frage geklaert: unabhaengig vom Aktien-Agent-System, keine Analyse
- Agent-Playbook.md verschlankt: Abschnitte 9-13 in Archiv-Datei ausgelagert
- Watchlist: 4 neue Werte aufgenommen, Obergrenze auf 50 angehoben
- Watchlist-Scalable-Sync jetzt bidirektional (Weg C ergaenzt)
- Blitz-Scan 08.09.: Weg-C-Sync (UCB/LGND/Itochu/Qnity/BONESUPPORT -> Scalable) + LGND-ISIN-Fix (US53219L1076 hatte ungueltige Pruefziffer, korrekt US53220K5048)
- Ligand Pharmaceuticals (LGND): vollstaendiger 3-fach Full-Deep-Dive-Cross-Check
- Trigger-Check 08.09.: ruhiger Tag, Japan/Asien-Lücken-Kandidatensuche (10 Namen), Kuchendiagramm aktualisiert
- Rigor-Standard um 6 Punkte aus ChatGPT/Gemini-Cross-Review des CLBT-Reports erweitert
- Rigor-Standard: Geminis Nachfassrunde zu fehlenden Visualisierungen eingearbeitet
- Novo Nordisk (NVO): Full-Deep-Dive-Cross-Check mit erweitertem 28-Punkte-Rigor-Standard
- Cross-Check-Prozess: beide KIs bekommen ab sofort dieselbe Methodik-Datei
- NVO-Report: Kurs+KGV-Verlaufs-Chart ergaenzt statt Jahres-Tabelle (neue Seite 5/9)
- NVO-Report: Seite 5 (Bewertungs-Chart) und 7 (Kursverlauf) zusammengelegt
- NVO-Report: vollstaendige DNA-Check-Tabelle nachgeholt (K+E-Kriterien)
- NVO-Report: Tag- und Typ-Spalten aus DNA-Check-Tabelle entfernt
- Neues Report-Format: Schnellanalyse (2-3 Seiten) zwischen Kompakt und Deep Dive
- Rambus (RMBS): erste Agent-Schnellanalyse (neues 2-3-Seiten-Format)

## 2026-09-07

- Master-Status um Kategorisierungs-Kriterien + Watchlist-Kompaktübersicht erweitert (fuer Jack/Conan-Kontext ohne volle architecture.md/watchlist.md)
- architecture.md zu Agent-Playbook.md umbenannt, alle Referenzen aktualisiert
- Jack/Conan werden jetzt auch als eigenstaendige Suchquelle eingesetzt
- Portfolio-Lücken-Trigger (Talent-Slot + Europa/Gesundheitswesen): BONESUPPORT neu in Watchlist, ersetzt Rorze
- Alle 4 Scheduled Tasks + Hermes-Cron-Piloten komplett entfernt (Brians Wunsch)
- Taeglicher-Report-Pflichtstruktur ergaenzt (4-Punkte-Format)
- Trigger-Check 07.09. Folgelauf: Scalable wieder ok, Transaktion+Cash+Pie aktualisiert, Kraken/Rambus-Erinnerung + Tages-Mail verschickt
- Wochenfazit 07.09.2026: BEOBACHTEN - kein akuter Handlungsbedarf (verkuerztes 3-Tage-Fenster)
- Wochenfazit 07.09. Nachtrag: PDF-Base64-Anhang-Fix als strukturell nicht machbar verifiziert
- SKILL.md-Backups nach Hermes-Rebuild-Testlauf aktualisiert
- Trigger-Check 07.09. Folgelauf 2: ruhiger Tag, Watchlist-Ampel (30/30 gruen)
- Portfolio-Sensitivitaets-Analyse bei Material Shift eingefuehrt
- Drei neue Prinzipien nach Vergleich mit Raketentonis Agent-System
- Nordstern um drittes Grundziel ergaenzt: langfristig != fuer immer
- Drittes Grundziel praezisiert: nur mit nachvollziehbarem Grund verkaufen
- Full Deep Dive PDF-Format erweitert (Reaper Deep Dive Report)
- Chart-Workflow-Anleitung: --rsi --macd fuer Full Deep Dive verankern
- render_chart.py: FutureWarning bei RSI-Berechnung beseitigt
- ADR-Fallback-Regel fuer Twelve-Data-Plan-Sperren ins Playbook aufgenommen
- Cellebrite (CLBT): Full Deep Dive als Timing-Test, 3-fach Cross-Check
- Projektweites Rebranding: Reaper -> Agent (auf Brians Wunsch)
- Agent Deep Dive Report: auf 5+ Seiten erweitert (jetzt 7), CLBT als Beispiel
- Agent Deep Dive Report: heller/weisser Hintergrund statt dunklem Anthrazit
- CLBT Deep Dive: Schriftgroesse um 2pt erhoeht fuer bessere Lesbarkeit
- Alle Report-Formate auf hellen/weissen Hintergrund umgestellt
- Full-Deep-Dive-Rigor-Standard nach uncoveredjapan.com-Vorbild ergaenzt
- CLBT Deep Dive auf 10 Seiten erweitert: uncoveredjapan.com-Rigor-Standard

## 2026-09-06

- taeglicher-trigger-check 2026-09-05: ruhiger Tag, keine Trigger
- TMR: Regel-Widerspruch bei >20%-Quellenabweichung behoben
- Echte Ursache des Jack-Reflex-Abbruch-Bugs gefunden und behoben
- Hoya Corp (7741): vollstaendiger 3-fach TMR-Cross-Check + Fact-Pack-Tag-Fix-Test
- Hoya Corp (7741): Reaper-Kompakt-PDF nachgetragen
- Jack/Conan bekommen jetzt bei jedem Bridge-Aufruf den vollen Master-Status

## 2026-09-05

- Jack und Conan bekommen get_quote (Twelve Data) und read_master_status
- Lasertec Corp (6920): vollstaendiger 3-fach TMR-Cross-Check + wichtiger Kursfehler-Fund
- Alle drei KIs bekommen jetzt alle drei Methodik-Dateien (TMR+Scout+TA)

## 2026-09-04

- Prediction Ledger: Luecke geschlossen (2026-09-03 im 3-KI-Pulse-Check gefunden)
- architecture.md: Prediction-Ledger-Korrektur dokumentiert
- HANDOVER.md: RKLB-Meta-Retro-Fall als geloest markiert (war bereits am 01.09. erledigt)
- Bridge-Status-Log eingefuehrt (Conans Vorschlag aus dem 3-KI-Pulse-Check)
- macro_context.md: EZB- und BoJ-Sitzungstermine fuer Rest-2026 ergaenzt
- HANDOVER.md: drei weitere veraltete Offene-Punkte korrigiert (Gaps-Abarbeitung)
- architecture.md: 9-Positionen-Datenluecke als geloest markiert
- Täglicher Trigger-Check 2026-09-04: keine neuen Transaktionen, Watchlist-Ampel ruhig, Pie-Chart aktualisiert
- Frischer 3-fach-Scout-These-Check: Cellebrite (Exit) + Rocket Lab (Terminal-State bestaetigt)
- Neue Pflicht: Gruendliche These-Pruefung vor Verkaufsempfehlung (bestehende Positionen)
- Cellebrite-Korrektur umgesetzt: VERKAUFEN->HALTEN+Checkpoint, Talent->Profi
- Täglicher Trigger-Check 04.09. (2. Durchlauf): Makro-Kontext befüllt, E-Mail-Nachtrag für Cellebrite-VERKAUFEN
- Rocket Lab: konkrete, recherchierte Nachkauf-Aufstufungs-Trigger hinterlegt
- CBOE zu Champions, SoFi zu Profi - Talent-Rebalancierung exakt auf Ziel
- Lasertec zu Champions, Asahi Intecc zu Profi (Watchlist-Rekategorisierung)
- Watchlist "geschärfter Blick"-Review: ANET und USLM zu Champions hochgestuft
- Watchlist "geschärfter Blick": vollständiger Review aller 30 Werte abgeschlossen
- Depot "geschärfter Blick": Review der restlichen 14 Positionen abgeschlossen
- Rorze Corp (6323): vollstaendiger 3-fach Scout-Quick-Filter fuer freien Talent-Slot
- Neue Regel: Automatisierte Portfolio-Luecken-Kandidatensuche-Pflicht
- Praezisierung: Portfolio-Luecken-Kandidatensuche meint vollstaendige Index-Durchsuchung
- Neue Regel: tieferer Zweck der Kandidatensuche - Bereicherung, Unter-Radar-Funde, Qualitaets-Vergleich
- Blitz-Scan 16:15 UTC: Disco Corp (6146) -5,4% - Jarvis-Only (Bridges nicht verfügbar)
- Täglicher Trigger-Check 04.09. (3. Durchlauf): ruhiger Tag, Mehrfachlauf-Ursache geklärt
- Drei Meta-Regeln von Raketentonis System uebernommen: Vorrang-Hierarchie, Regel-Disziplin, Master-Status
- Neue Datei: depot/master_status.md - konsolidiertes Status-Dashboard
- Portfolio-Regel-Check: echte Berechnung statt Schaetzung
- Wochenfazit 2026-09-04: BEOBACHTEN - ETF-Anteil kritisch niedrig (21,7%), SoFi ueber 10%-Cap
- Cellebrite/Israel-Region-Luecke geschlossen
- Regelwerk gilt fuer alle drei KIs - Bridge-Bloecke 5+6 fuer Jack/Conan ergaenzt
- Jack und Conan bekommen eigene Live-Web-Recherche

## 2026-09-03

- Kategorisierungs-Fix (feste 10-6-4-Struktur), Disco-Corp-Analyse, taegliche Watchlist-Ampel
- Erinnerungs-Mechanismus fuer offene Kauf-/Verkauf-Empfehlungen (5-Werktage-Rhythmus, Chat+Mail)
- CRV-Ampel je Watchlist-Wert (Bewertungssignal, getrennt von Champions/Profi/Talent-Qualitaet)
- Margin-of-Safety/Drawdown-Historie in CRV-Ampel eingebaut (AI-Trend-Werte)
- CRV-Ampel auf 4 Stufen erweitert (+ORANGE) und auf alle 18 Depot-Positionen ausgeweitet
- Methodik-Fix: CRV-Ampel-Urteil ist eigene Einordnung, externe Quellen nur Rohdaten
- Trend-Pfeile (🔺/🔻) fuer CRV-Ampel-Auf-/Abstufungen eingefuehrt
- Watchlist-Uebersicht-PDF (lesbare Ansicht aller 30 Werte mit CRV-Ampel)
- 3 Ergaenzungen aus Jack/Conan-Produkt-Feedback zur CRV-Ampel umgesetzt
- CRV-Ampel: Bewertungsanker je Geschaeftsmodell + 5. Farbe GRAU ergaenzt
- 10-7-3-Korrektur + Terminal-State-Pflicht in Bridge-Meta-Instruktion (3-KI-System-Audit)
- Taeglicher Trigger-Check 2026-09-03: CLBT-Jarvis-Only-Reassessment nach CEO-Wechsel/Guidance-News
- CLBT-Jarvis-Only-Reassessment vom 2026-09-03 entfernt (nicht mehr benötigt)
- Restliches 3-KI-Audit-Backlog umgesetzt (alle 8 offenen Punkte)
- Fix: Prompt-Änderungsrechte-Klarstellung an Abschnitt 2 angeglichen
- TMR-Prompt v11.7 -> v11.8: Korrelierte-Mali-Regel gegen Reaper-Score-Double-Counting
- HANDOVER.md: E-Mail-Bug-Diagnose + Fix dokumentiert (Abschnitt 11, Punkt 14)
- Taeglicher Markt-/Makro-Kontext-Check (Fear&Greed, VIX, Zinsen, Geopolitik)
- Markt-/Makro-Kontext erweitert: S&P-Level, Wahl-/Fed-Kalender, weitere Dimensionen

## 2026-09-02

- Jack/Conan von Browser-Automation auf direkte API-Bridges umgestellt (openai-bridge/gemini-bridge) + Depot-Transaktions-Erkennung
- Orion Oyj + Asahi Intecc Testlaeufe, ISIN-Gegenprobe-Regel, Jack-Abbruch-Bug gefixt, Depot-Kuchendiagramm aktualisiert

## 2026-09-01

- HANDOVER.md: Migrations-Update Cowork -> Claude Code (Repo-Pfad, Scheduling, PDF-Pipeline)
- reports/render_pdf.py: lokaler HTML->PDF-Renderer (Playwright + Google Chrome)
- Kraken Robotics & Rocket Lab: Nachhol-Analyse abgeschlossen, Meta-Retro-Fall RKLB aufgelöst
- HANDOVER.md: Eskalations-Kanal dokumentiert (Push funktioniert, E-Mail nicht verdrahtet)
- HAWK: Chart- und Einstiegslage-Sektion nachgetragen (Seite 2 PDF + Markdown)
- watchlist.md: Watsco-ISIN korrigiert (falsch identifizierte Firma)
- HANDOVER.md: Scalable-Watchlist-Spiegel + Watsco-ISIN-Bug dokumentiert
- Core-vs-Advisory-Rules-Trennung + Terminal-State-Mechanismus (Abschnitt 14)
- Earnings-Season-Automatisierung: Phase-4-Earnings-Kalender umgesetzt
- depot/earnings_calendar.md angelegt + beide Scheduled Tasks erweitert
- E-Mail-Kanal (Gmail) verdrahtet - alle 4 Scheduled Tasks erweitert
- Antizyklisches Grundprinzip explizit verankert (Verkaufsdisziplin-Sektion)
- Antizyklisches Grundprinzip auf TA-Modul (Charttechnik) ausgeweitet
- Systematische Herleitung Talent-langfristig-vs-Zock-Trade-Tag
- benchmark_chart.py: alten Cowork-Pfad (/root/aktien-agent) auf relative Pfade umgestellt
- Charttechnik-Ergaenzung: echte Candlestick-Charts + Bodenbildung-Proxy
- Charttechnik-Skripte im Regelwerk verankert
- Tranchen-Entscheidungslogik + Zonen-Benachrichtigung per E-Mail/Preisalarm
- Portfolio-Kontext-Pflichtprüfung vor Zonen-/Tranchen-Empfehlungen
- Kostenstruktur Scalable + Trade Republic ergaenzt (finanzen.net zero war schon da)
- Klarstellung: Scalable dient nur dem ETF-Sparplan, BBCA ist Ausnahme
- Konkrete-Eurosumme-Pflicht + Klarstellung: Preisalarm ist kein Kaufsignal
- Explizite Limit-Order-vs-Beobachtung-Kennzeichnung in Zonen-E-Mails
- RMBS: Kompaktes Update 2026-09-01 (Nachkauf-Nachfrage) + Preisalarm 65€ gesetzt
- Neue Umschichtungs-Logik: Kapitalrotation zwischen Positionen (Gewinnmitnahme/Verlust -> aktive Wiederanlage-Prüfung)
- Add .gitignore (schuetzt lokale .mcp.json vor versehentlichem Commit)

## 2026-08-31

- Initial commit
- Disco Corp (6146.T): 3-KI-Quick-Filter-Cross-Check + Reaper-Kompakt-PDF (2026-08-31)
- Regelwerk: TA-Pflicht (Twelve Data) + Chart-und-Einstiegslage-Sektion + EUR-Durchgaengigkeit fuer JEDE Einzelanalyse (Brian-Feedback nach Disco-Analyse)
- Klarstellung: Couche-Tard-PDF ist nur lose Inspiration fuer Chart-und-Einstiegslage-Sektion, kein 1:1-Klon (Brian-Praezisierung)
- Disco Corp: Chart-und-Einstiegslage-Sektion nachgetragen (Twelve-Data-Fallback, Zonen+EUR, Brian-Feedback umgesetzt)
- Disco 6146: Full Deep Dive (DCF/Reverse-DCF dual-beta, Management-Score, Debt-Maturity, verifizierte DNA-Korrekturen, Chartmuster)
- Vincorion (V1NC): 3-KI-Cross-Check + PDF-Methodikvergleich + Regelwerk-Erweiterung (IPO-Overhang-Modul, Post-IPO-Datenluecken-Konfidenz, No-False-Precision-Regel)
- HawkEye 360 (HAWK): Nachtrag zu Lock-up-Vorziehung (02.09.) + Russell-2000-Aufnahme (21.09.), Positions-Sizing-Check gegen Trace-Deckel
- Formulierungsstil der Kurz-Fazits/PDF-Fazits an Raketentonis Erzählstil angelehnt (No-False-Precision-Regel unangetastet)
- Klarstellung: Formulierungsregel dient Verstaendlichkeit der Analyse, nicht nur dem Erzaehlstil (Item 7 ergaenzt)
- Täglicher Trigger-Check 2026-08-31: WEG S.A. (WEGE3) als LatAm-Watchlist-Kandidat, 3-fach-Quick-Filter (BEOBACHTEN, einstimmig)
- HawkEye 360 (HAWK): Full Scout 3-fach-Cross-Check (Jarvis/Jack/Conan) - erster Live-Test der Verstaendlichkeits-Formulierungsregel
- Vollständige technische Übergabe (HANDOVER.md) für einen neuen Claude-Code-Agenten
