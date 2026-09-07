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

Vollformat-Report: `reports/CLBT-reaper-deepdive-2026-09-07.pdf` (7 Seiten,
"Agent Deep Dive Report"-Format, zuletzt am 2026-09-07 auf Brians Wunsch
erweitert: narrative Burggraben-Einführungsseite [Unternehmensgeschichte
seit 1999, Sun-Corporation-Übernahme 2007, warum der Burggraben aus
Gerichtsverwertbarkeit statt Patenten besteht], eigene Management-Sektion
[CEO Ramji/CFO Barter/CTO Wade, Großaktionärsstruktur, Kapitalallokation],
"Katalysator-Ausblick" mit datierten Terminen, RSI/MACD-Chart-Subplots,
Bear/Base/Bull-Balkendiagramm, ausformulierte Fließtext-Boxen bei Moat/
Going-Concern/SBC-Check/Reality-Check, "Der unterschätzte Punkt"-Box,
Aufstufungs-/Abstauber-Trigger-Kästen, Score-Aufschlüsselungstabelle,
formale Quellen-/Annahmen-Seite). Rebrand von "Reaper" zu "Agent"
zeitgleich umgesetzt, siehe Agent-Playbook.md.
