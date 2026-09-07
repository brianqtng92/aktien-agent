# Cellebrite DI Ltd (CLBT) — Full Deep Dive, 3-fach TMR-Cross-Check — 2026-09-07

**Zweck dieser Analyse:** Live-Timing-Test des Full-Deep-Dive-Prozesses auf Wunsch von Brian (Vergleich mit Raketentonis ~15-Minuten-Referenzwert). Cellebrite ist eine bereits gehaltene Depot-Position (Kategorie Profi, CRV zuvor 🟡 Halten) und damit ein realistischer Full-Deep-Dive-Kandidat, kein künstliches Testobjekt.

**Wichtiger methodischer Hinweis:** Aus Zeit-/Kosten-Gründen wurden Jack (Gemini) und Conan (ChatGPT) NICHT mit den vollständigen Methodik-Dateien (jack-moat-reaper-v11.7.md/conan-the-scout-v1.12.md, je 65-72KB) gefüttert, sondern mit einer kondensierten, aber inhaltlich treuen Kurzfassung der TMR/Scout-Full-Deep-Dive-Regeln (Datenintegrität, SaaS-Override-Kriterien, Abbruch-Logik, Score-Berechnung, Reality-Flags). Die Produktions-Pipeline (Hermes-Cron-Jobs) sendet aktuell die vollständigen Dateien — ein echter automatisierter Full-Deep-Dive-Lauf ist dadurch strukturell LÄNGER als der hier gemessene Wert. Siehe Chat-Antwort für die vollständige Einordnung.

---

## Jarvis Fact-Pack (Ausgangsbasis für Jack/Conan)

Siehe Prompt-Text unten (identisch an beide KIs gesendet) — Kernpunkte: Kurs $11,45 (04.09.), Marktkap. $2,87 Mrd, Beta 1,15, Q2-2026 ARR $508 Mio (+21% YoY), Umsatz $131 Mio (+16% YoY), FY2026-Guidance gesenkt (ARR $550-560 Mio, Umsatz $555-561 Mio), Adj.-EBITDA-Guidance angehoben ($153-159 Mio), CEO-Wechsel Hogan→Ramji (13.08.2026), Cash+STI $442,5 Mio, Gesamtschulden nur $23,2 Mio, FCF TTM $144,2 Mio (28% Marge), Bruttomarge 82-86%, Analysten-Konsens Strong Buy PT $15,36.

Quellen: Twelve Data (Kurs/Zeitreihe/News), stockanalysis.com (Kennzahlen/Bilanz), Yahoo Finance/Seeking Alpha/Fool.com/stocktitan.net (Q2-2026-Earnings-Coverage), theglobeandmail.com (CEO-PR).

---

## Jarvis eigene DCF-Berechnung (Python, Rule 20)

WACC/Cost-of-Equity 10,58% (Rf 4,1% + Beta 1,15 × ERP 5,2% + 0,5% Israel-/Public-Sector-Aufschlag, praktisch schuldenfrei → WACC ≈ Cost of Equity).

| Szenario | FCF-Wachstum J1→J5 | Terminal-g | FV/Aktie | Δ vs. Live $11,45 | TV-Anteil EV |
|---|---|---|---|---|---|
| Bear | 10%→4% | 2,5% | $10,53 | -8,0% | 69,7% |
| Base | 17%→8% | 3,0% | $13,32 | +16,3% | 73,0% |
| Bull | 22%→12% | 3,5% | $16,35 | +42,8% | 75,8% |

TV-Anteil >69% in allen Szenarien → DCF sensitiv auf WACC/Terminal-g. Bear-Case leicht unter Live-Kurs, Base/Bull darüber — moderat-positiver Skew, deckt sich grob mit Analysten-PT $15,36.

---

## Jack (Gemini) — vollständige Antwort

Score 4/10, Konfidenz 🟡 MITTEL (SBC-Infection-Deckel), Rating BEOBACHTEN, Sizing Tier 3 (max 2%), Abstauber-Limit $9,00-9,50.

Kernfunde: ROIC 12,0% [VERIFIED] (Fail vs. >20%-Schwelle), FCF-Marge 28% Headline [VERIFIED], NRR 112% (halber K-Punkt), SBC-Infection-Flag aktiv (Verwässerung 2,16% p.a.), Moat STARK (Preissetzungsmacht + Switching Costs), Grant-Inflation-Flag.

(Vollständige Rohantwort im Session-Log, hier aus Platzgründen nicht 1:1 dupliziert — Kernaussagen oben und in der PDF-Cross-Check-Tabelle vollständig erfasst.)

---

## Conan (ChatGPT) — vollständige Antwort

Score 5,5/10 (Rohscore 7,0, Mali -2,0 SBC/-0,5-1,0 Guidance), Konfidenz 🔴 niedrig bis untere 🟡-Mittelzone, Rating HALTEN/BEOBACHTEN, Sizing Tier 3 (max 2%), Abstauber-Band $9,50-10,25.

Kernfunde (mit eigener Live-Recherche inkl. SEC-20-F-Primärquelle): NRR 117% (primärquellennah, Q2-2026 + 20-F), Going-Concern via EY-Prüfungsurteil bestätigt unauffällig, SBC-bereinigte reale FCF-Marge nur ≈17% (vs. 28% Headline), GAAP-Op.-Marge 5,3% vs. Non-GAAP 22,7%, Aktienzahl +9,33% YoY, Kundenkonzentration unkritisch (kein Kunde >5%), EV/Sales 4,6x.

(Vollständige Rohantwort mit allen Quellenangaben im Session-Log — Kernaussagen oben und in der PDF-Cross-Check-Tabelle vollständig erfasst.)

---

## Cross-Check-Synthese (Jarvis)

**Konvergenz:** Alle 3 unabhängigen Analysen landen bei BEOBACHTEN/HALTEN, kein KAUFEN. SBC-/Verwässerungs-Flag von Jack UND Conan unabhängig gefunden (unterschiedliche Rechenwege, gleiches Ergebnis) — starkes Signal für Robustheit dieses Fundes. Sizing-Konsens Tier 3 (max 2%). Abstauber-Zonen überlappen sich ($9,00-10,25).

**Divergenz (der eigentliche Mehrwert):** Conan grub bis zur SEC-20-F-Primärquelle vor und fand eine präzisere NRR (117% vs. Jacks 112%) sowie eine bestätigte Going-Concern-Entwarnung per Prüfungsurteil. Vor allem fand Conan die SBC-bereinigte reale FCF-Marge (≈17%) — Jack hatte hier nur die Headline-Zahl (28%) übernommen. Diese Divergenz ist als "Der unterschätzte Punkt" in die PDF aufgenommen.

**Finales Rating:** BEOBACHTEN (einstimmig), Reaper-Score ≈4,5-5,0/10 (Konsens zwischen 4,0 und 5,5), Konfidenz 🟡 MITTEL (Deckel wegen SBC-Flag), Sizing Tier 3 max 2%, Abstauber-Zone $9,00-10,25, nächster Re-Check Q3-2026-Zahlen + Investor-Event 14.09.2026.

---

## PDF

Vollformat-Report: `reports/CLBT-reaper-deepdive-2026-09-07.pdf` (10 Seiten,
"Agent Deep Dive Report"-Format). Zweite große Erweiterung am 2026-09-07
(nach der ersten 3→7-Seiten-Erweiterung): Rigor-Standard nach
uncoveredjapan.com-Digital-Arts-(2326)-Vorbild eingearbeitet (lose
Inspiration, unser eigener Stil, siehe Agent-Playbook.md "Full-Deep-Dive-
Tiefe: Rigor-Standard"). Neu hinzugekommen:
- **5-Jahres-Umsatzhistorie** (2022-2026E) statt nur TTM, inkl. GAAP-
  Nettoergebnis-Fallstrick-Erklärung 2024 (-$283M GAAP-Verlust war ein
  reiner SPAC-Warrant-Bilanzierungseffekt, Non-GAAP +$97,8M)
- **Guidance-Track-Record-Tabelle** (2023-2026): 3 Jahres-Beats in Folge,
  dann erste Kürzung 2026 — zeitlich exakt mit CEO-Wechsel zusammenfallend
- **Produktlinien-Tabelle mit benannten Wettbewerbern** (Inseyets/Pathfinder/
  Guardian/Corellium vs. Magnet Forensics-Grayshift, MSAB, Oxygen Forensics,
  Nuix, OpenText, Axon)
- **Peer-Multiple-Vergleichstabelle** (MSAB als einziger direkt
  vergleichbarer börsennotierter Peer, mit aufgedeckter Bewertungs-Anomalie:
  MSAB teurer bewertet trotz Bruchteil der Größe)
- **Eigenständige "Offene Schwächen"-Sektion** mit direktem CEO-Zitat
  (Ramji, Q2-2026-Call) zur Guidance-Kürzung
- **Root-Cause-Analyse** Guidance-Cut: Timing-/Ausführungs- statt
  Nachfrageproblem, mit 3 stützenden Indizien
- **Management-Glaubwürdigkeits-Matrix** (4 getrennte Achsen statt einer Note)
- **Kapitalrückführungs-Historie** (explizit: keine Dividende/Buyback seit
  Börsengang 2021, kein Track Record vorhanden statt stillschweigend
  übergangen)
- **DCF-Reverse-Engineering**: impliziertes Marktwachstum ≈9,6% p.a. liegt
  UNTER dem eigenen Bear-Case — Markt preist pessimistischer als Base-Case
- **Downside-Boden explizit quantifiziert**: Netto-Cash/Aktie $1,67 = nur
  14,6% des Kurses (deutlich dünnerer Puffer als im Digital-Arts-Vorbild)
- **Bear-Case als Wahrscheinlichkeits-Katalog** (5 benannte Risiken mit
  Eintrittswahrscheinlichkeit statt Fließtext)
- Offen und transparent vermerkt: keine namentliche Distributor-/
  Vertriebspartner-Konzentration für CLBT recherchierbar (anders als beim
  Digital-Arts-Vorbild) — als echte Lücke ausgewiesen, nicht verschwiegen.

Rebrand von "Reaper" zu "Agent" bereits zuvor umgesetzt, siehe
Agent-Playbook.md.

## Dritte Erweiterung (2026-09-08): Umsatz-/OCF-Grafiken + Dividendenrendite

Auf Brians Nachfrage ("mir fehlt auch ein paar Darstellung... wie operating
cash flow, revenue oder dividendenrendite") wurde eine neue Seite 5
ergänzt (Report jetzt 11 Seiten): Umsatzhistorie als Balkengrafik (nicht
nur Tabelle), erstmals eine Operating-Cashflow-Historie (OCF fast
verfünffacht 2021→2025, $36,05 Mio → $173,54 Mio), und ein expliziter
Dividendenrendite-Datenpunkt (Cellebrite zahlt keine Dividende, 0,00% —
explizit geprüft und vermerkt statt stillschweigend angenommen). Diese
drei Elemente sind jetzt Pflichtbestandteil des Rigor-Standards für alle
künftigen Full Deep Dives, siehe Agent-Playbook.md.

## Vierte Erweiterung (2026-09-08): Operating-Margin in Peer-Tabelle + Kernannahmen je DCF-Szenario

Auf Brians Hinweis auf die uncoveredjapan.com-Teil-5-Darstellung (Forward-KGV
vs. Median + Operating Margin, sowie qualitative Bear/Base/Bull-Annahmen)
wurde die Peer-Multiple-Tabelle um eine Operating-Marge-Spalte ergänzt
(Cellebrite 22,7% vs. MSAB 14,7% EBIT-Marge — MSAB bleibt trotz schwächerer
Marge teurer bewertet, verstärkt die bereits dokumentierte Anomalie). Kein
Median berechnet, da nur ein direkt vergleichbarer börsennotierter Peer
vorliegt (Rigor-Standard verlangt mind. 3). Zusätzlich: explizite
qualitative Kernannahmen je Bear/Base/Bull-Szenario (nicht nur
Wachstumsraten) direkt unter der DCF-Tabelle ergänzt.

## Sechste Anpassung (2026-09-08): DNA-Check-Tags als Farb-Badges statt Klammer-Text

Auf Brians Wunsch ("kann man das nicht weglassen?") wurden die
Klammer-Tags ([VERIFIED]/[TRAINING] usw.) in der DNA-Check-Tabelle durch
kompakte farbige Badges (V/T/E/N) mit einer einzeiligen Legende ersetzt —
die zugrunde liegende Tag-Disziplin und ihre Auswirkung auf Konfidenz/
Score/Sizing bleibt unverändert, nur die wiederholte Textanzeige pro
Tabellenzelle wurde visuell verschlankt.
