---
Datei: Prediction Ledger / Decision Journal
Angelegt: 2026-09-03 (Lücke geschlossen - Mechanismus war seit 2026-08-30 in
Agent-Playbook.md als "aktiv" dokumentiert, aber die Datei existierte nicht und
kein einziger Eintrag wurde je angelegt; im 3-KI-System-Audit vom 2026-09-03
gefunden und rückwirkend geschlossen)
Zweck (siehe Agent-Playbook.md, "Meta-Retrospektive", Phase 2): systematisches
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

### 2026-09-04 — Münchener Rückversicherung (Depot, Champions) — nachgetragen
- **Anlass:** Bestehende Depot-Position (Kauf vor 2026-08-30, daher bisher kein Ledger-Eintrag), im Rahmen des "geschärfter Blick"-Reviews vom 04.09.2026 als [B] THESE-CHECK nachgetragen (schrittweise Nachpflege, siehe Agent-Playbook.md).
- **Zentrale These:** Oligopol-Rückversicherer, ROE weiterhin exzellent (23,0% H1 2026, 25,5% Q2 allein), an der Spitze der Peer-Gruppe (Swiss Re 22,7%, Hannover Re 21,2%). Aktueller Beobachtungspunkt: Preiszyklus dreht real (Januar-2026-Erneuerungen -14,7% Property-Cat, Juli -5,5% bis -9,1%), Combined Ratio (~82%) leicht über Guidance (~80%), aber klar profitabel.
- **These-Bruch-Kriterien:** (a) Januar-2027-Erneuerungspreise fallen nochmals deutlich UND Combined Ratio schiebt sich Richtung 90%+; (b) ROE fällt 2+ Jahre in Folge unter ~15% (Kapitalkosten) — beide zusammen wären ein struktureller statt zyklischer Softening-Befund.
- **Nächster Prüfpunkt:** Januar-2027-Erneuerungspreise + FY2026-Combined-Ratio vs. ~80%-Guidance.
- **Prüf-Zeithorizont:** 6 Monate (2027-03-04).

### 2026-09-04 — Constellation Software (Depot, Champions) — nachgetragen
- **Anlass:** wie oben (schrittweise Nachpflege bestehender Depot-Positionen).
- **Zentrale These:** Serial-Acquirer mit Nischen-Monopolen, Akquisitionstempo weiter hoch (~$2,5 Mrd. in 7,5 Monaten 2026). Beobachtungspunkt: organisches Wachstum verlangsamte auf 2% in Q2 2026 (von 4%/6%), EBITA-Marge -130 Bp YoY auf 25,2%, aber sequenziell von Q1 erholt; 2026er-Akquisitions-Kohorte bereits von -16% auf +16% Marge verbessert.
- **These-Bruch-Kriterium:** organisches Wachstum bleibt 2 weitere Quartale (bis Q4 2026/Q1 2027) unter 3%, statt sich Richtung historischer 5-6% zu erholen.
- **Nächster Prüfpunkt:** Q4 2026/Q1 2027-Zahlen.
- **Prüf-Zeithorizont:** 6 Monate (2027-03-04).

### 2026-09-04 — MercadoLibre (Depot, Champions) — nachgetragen
- **Anlass:** wie oben.
- **Zentrale These:** Dominante E-Commerce/Fintech-Plattform LatAm, Umsatz Q2 2026 erstmals >$10 Mrd. (+50% YoY). Beobachtungspunkt: operative Marge komprimierte auf 6,7% (von 12,2%, -550 Bp) durch bewusste Reinvestition (Logistik, MELI+, Cross-Border, PIX-Rabatte) plus höhere Kreditrückstellungen — aber Kreditqualität selbst stabil (NPL 15-90 Tage nahe historischem Tief 7,0%, Nettozinsmarge nach Verlusten verbessert auf 21%).
- **These-Bruch-Kriterium:** operative Marge bleibt 3+ Quartale unter 8% UND NPL-Quote steigt über ~8-9% (beide zusammen = echte Kreditqualitäts-/Wettbewerbserosion statt bewusster Offensiv-Investition).
- **Nächster Prüfpunkt:** Q4 2026/Q1 2027-Zahlen.
- **Prüf-Zeithorizont:** 6 Monate (2027-03-04).

### 2026-09-04 — Bank Central Asia (Depot, Champions) — nachgetragen
- **Anlass:** wie oben.
- **Zentrale These:** ROE 24,1%, dominante Marktstellung Indonesien. Beobachtungspunkt: Nettozinsmarge komprimierte YoY von ~5,8% auf ~5,4% durch branchenweite Bank-Indonesia-Zinserhöhungen (Sektor-NIMs laut Macquarie ~14% gefallen, keine BBCA-spezifische Schwäche) — Kreditwachstum beschleunigte trotzdem wieder auf 8,0% YoY / +4,2% QoQ, NPL 1,9% im Normalbereich, CAR 27,4%.
- **These-Bruch-Kriterium:** ROE fällt nachhaltig unter ~20% AUCH NACHDEM sich der BI-Zinszyklus stabilisiert hat (nicht während der laufenden Zinsphase).
- **Nächster Prüfpunkt:** NIM-Entwicklung über die nächsten 2-3 Quartale.
- **Prüf-Zeithorizont:** 6 Monate (2027-03-04).

### 2026-09-16 — CBOE Holdings (Depot, Champions) — Full Deep Dive, Rating KAUFEN (gestaffelt)
- **Anlass:** Bestehende Depot-Position, echter 3-fach-Cross-Check auf Brians Wunsch (Ausbau der Position prüfen) — siehe `analysen/CBOE-fulldeepdive-cross-check-2026-09-16.md`. Erster Analyseversuch scheiterte an einem Bugfix-Bedarf (Bridges ohne echten Web-Search-Zugriff, siehe HANDOVER.md 10.14), nach Fix komplett neu durchgeführt.
- **Empfehlungs-Typ:** Nachkauf-Empfehlung (KAUFEN, gestaffelt), Kurs bei Empfehlung $270,40 (15.09.2026, nach -4,96%-Tagesverlust, sektorweiter FOMC-Ausverkauf ohne CBOE-spezifischen Auslöser).
- **Zentrale These:** Champion-Qualität bestätigt (ROE 25-26%, ROIC 17-29% je Quelle, Netto-Cash-Bilanz, Moat STARK/SPX-VIX-Exklusivlizenz), Guidance 2026 zweimal angehoben. Alle drei unabhängigen DCF-Rechnungen (Jarvis/Jack/Conan) kommen strukturell über Analysten-Konsens ($292-318) — Ursache: bei CBOEs niedrigem Beta (0,41-0,64) ist der WACC-Terminal-g-Spread so eng, dass der Terminal-Value-Anteil auf 84-87% des EV steigt (Modell-Artefakt, kein Fehler). Peer-EV/EBITDA-Abschlag (14,25x vs. Peer-Median 17,3x) stützt die These zusätzlich.
- **Konkrete Erwartung (Fair-Value-Bandbreite):** Bear $240-291 · Base $360-410 (bewusst unter dem mechanischen Gordon-DCF-Wert von $396-484, siehe Root-Cause oben) · Bull $503-610. Analysten-Konsens $292-318 als zusätzlicher, konservativerer Anker.
- **These-Bruch-Kriterien:** (a) ROIC dreht 2 Quartale in Folge unter WACC; (b) Moat-Decay bestätigt (SPX-Exklusivlizenz-Risiko materialisiert); (c) Debt-Maturity Januar 2027 dreht auf KRITISCH ohne klare Refinanzierungslösung; (d) Kurs steigt >30% über Base-FV ohne Fundamentalverbesserung.
- **Nachkauf-Trigger (gestaffelt, keine automatische Order):** Tranche 1 bei Stabilisierung über $268-270 (Tier 2, ~1,5-2%) — technische Bestätigung Pflicht (RSI-Erholung >45, MACD-Bodenbildung oder OBV-Trendwechsel). Tranche 2 bei $255-262.
- **Nächster Prüfpunkt:** Ausführung Tranche 1 (technische Bestätigung) sowie Q3-2026-Earnings.
- **Prüf-Zeithorizont:** 6 Monate (2027-03-16).

### 2026-09-21 — WALLIX Group SA (ALLIX, Euronext Growth Paris, FR0010131409)
- **Kategorie:** Talent (Bucket B, Quality in Formation) · Scout-Pfad
- **Anlass:** Brians direkte Anforderung eines Full Deep Dive. Zweiter Kandidat für die 2 offenen, weltweiten Talent-Slots (siehe Agent-Playbook.md Punkt 1b) — erster war ORKA.
- **Empfehlungs-Typ:** Watchlist-Aufnahme (KEIN volles Kauf-Rating, Starter-Empfehlung) — Rating bei Aufnahme: KAUFEN-KANDIDAT/Starter. Konvergenz MODERAT (JJ konstruktiv aber vage, Conan strenger/spezifischer — kein Rating-Widerspruch wie beim Kokusai-Fall, daher keine formale Diskussionsrunde nötig). Siehe `analysen/ALLIX-Scout-fulldeepdive-2026-09-21.md`.
- **Zentrale These:** Europäischer PAM-Cybersecurity-Anbieter, echter Wendepunkt 2025 (erstmals positiver Gesamtjahres-FCF), wiederkehrender Umsatz +24,1% (81% des Umsatzes), starker Cash-Runway. Zentraler Vorbehalt: Rule-of-40 nur ~19,2 (klar unter 30-40%-SaaS-Elite-Schwelle), keine NRR-Offenlegung.
- **Konkrete Erwartung (EV/Sales-zu-Wachstum, kein DCF):** EV/Sales ~3,1-3,4x, EV/ARR ~4,3-4,6x — bei ~15% Wachstum "fair", nicht klar teuer noch klar günstig.
- **These-Bruch-Kriterien:** (a) Rule-of-40 verschlechtert sich weiter; (b) FCF-Wende erweist sich als Einmaleffekt; (c) neue Finanzierung (€25-65 Mio.) wird für überteuerte/schlecht integrierte M&A statt organisches Wachstum verwendet; (d) dokumentierter Kundenverlust an CyberArk/Delinea/BeyondTrust.
- **Nächster Prüfpunkt:** H1-2026-Zahlen 08.10.2026 — Margenpfad, FCF-Fortsetzung, ARR/MRR-Wachstumstempo, ob NRR erstmals offengelegt wird.
- **Prüf-Zeithorizont:** 6 Monate (2027-03-21).

### 2026-09-21 — Kokusai Electric Corporation (6525, Tokyo, JP3266400005)
- **Kategorie:** Profi (Bucket A/C) · TMR-Pfad
- **Anlass:** Brians direkte Anforderung eines Full Deep Dive.
- **Empfehlungs-Typ:** Watchlist-Aufnahme (KEIN Kauf-Rating) — Rating bei Aufnahme: BEOBACHTEN/HOLD, Nachkauf-Zone ¥6.500-7.800. Konvergenz startete als "widerspruch" (JJ KAUFEN/5-7% vs. Conan HOLD/1-1,5%), nach Diskussionsrunde "moderat" (beide bei HOLD/BEOBACHTEN, Sizing max. 3-4%). Siehe `analysen/6525-fulldeepdive-cross-check-2026-09-21.md`.
- **Zentrale These:** ~70-80% Weltmarktanteil bei Batch-ALD-Halbleiterausrüstung (physik-/ökonomiebasierter Moat), Netto-Cash-Bilanz, gerade durchlaufene primärquellenverifizierte Gewinn-Reacceleration nach China-getriebener Schwächephase (FY2026 -16,4% Gewinn → Q1 FY2027 +70,6% Gewinn, Guidance +21% angehoben). Zentraler Vorbehalt: FCF-Marge (13,5%) verfehlt die 20%-TMR-Elite-Schwelle.
- **Konkrete Erwartung (DCF, reconciliiert):** Bear ¥4.000-5.200 · Base ¥6.800-8.500 · Bull ¥10.500-13.000. Aktueller Kurs (¥8.884) am oberen Rand der Base-Spanne — begrenzte Sicherheitsmarge.
- **These-Bruch-Kriterien:** (a) Auftragseingang bricht nach Q1-Spitze deutlich ein; (b) FCF-Marge normalisiert sich NICHT Richtung 15-18%; (c) China-Exportkontrollen verschärfen sich mit direktem Kokusai-Bezug; (d) NAND-Schwäche erweist sich als struktureller statt zyklischer Rückgang.
- **Nächster Prüfpunkt:** Q2 FY2027-Zahlen (~Anfang November 2026).
- **Prüf-Zeithorizont:** 6 Monate (2027-03-21) — zyklisches Semicap-Geschäft, kürzerer Horizont als bei einem klassischen Compounder.

### 2026-09-21 — Oruka Therapeutics (ORKA, NASDAQ, US6876041087)
- **Kategorie:** Talent (Biotech-Override) · Scout-Pfad
- **Anlass:** Weltweite, regionsunabhängige Talent-Slot-Suche (2 freie Slots, siehe Agent-Playbook.md Punkt 1b) — Kandidat von JJ vorgeschlagen, siehe `analysen/ORKA-Scout-quickfilter-2026-09-21.md`.
- **Empfehlungs-Typ:** Watchlist-Aufnahme (KEIN Kauf-Rating) — Rating bei Aufnahme: BEOBACHTEN-STARK. Konvergenz "moderat" (JJ nach Korrektur konstruktiv, Conan BEOBACHTEN — dessen Urteil auf einem von Aegis korrigierten Market-Cap-Fehler basierte).
- **Zentrale These:** Klinisches Biotech (Phase 2a, Psoriasis-Antikörper ORKA-001/002), außergewöhnlich starke Bilanz (Cash-Runway 100+ Monate bei aktuellem Burn), Differenzierungspotenzial ggü. Skyrizi/Bimzelx (längere Dosierungsintervalle bei mind. gleicher Wirksamkeit).
- **Konkrete Erwartung:** Kein DCF (Biotech-Override) — EV ~$5,2 Mrd. gegen Jefferies-Spitzenumsatzschätzung $5-10 Mrd. für ORKA-001 allein, als fair bis ambitioniert eingeordnet, nicht überzogen.
- **These-Bruch-Kriterien:** (a) Woche-28/52-Daten EVERLAST-A zeigen Wirksamkeits- oder Sicherheitsrückschlag; (b) Insider-Nettoverkäufe beschleunigen sich deutlich über die bekannten steuerbedingten RSU-Verkäufe hinaus; (c) Cash-Runway verkürzt sich durch beschleunigten Burn ohne neue Finanzierungsquelle.
- **Nächster Prüfpunkt:** Woche-28/52-Daten EVERLAST-A (H2 2026), Phase-2b-Daten (2027).
- **Prüf-Zeithorizont:** 12 Monate (2027-09-21) — klinische Biotech-Kataloge brauchen mehr Zeit als ein normaler Quartalszyklus.

### 2026-09-21 — Rambus Inc. (RMBS, Depot, Profi) — nachgetragen (Full-Deep-Dive-Refresh)
- **Kategorie:** Profi (etablierte Semiconductor-IP-Firma seit 1990) · TMR-Pfad
- **Anlass:** Bestehende Depot-Position von vor 2026-08-30, jetzt beim regulären [B] THESE-CHECK nachgetragen (Brians direkte Anforderung eines Full-Deep-Dive-Refresh der Analyse vom 09.09.2026). Siehe `analysen/RMBS-fulldeepdive-cross-check-2026-09-21.md`.
- **Empfehlungs-Typ:** Bestätigung BEOBACHTEN/HALTEN, kein Nachkauf — Konvergenz startete als echter Rating-Widerspruch (JJ KAUFEN/DCF-Base $110-125 vs. Conan BEOBACHTEN/DCF-Base $69), nach Diskussionsrunde STARK konvergiert (beide BEOBACHTEN, DCF Base $50-70). **Bemerkenswerter Fund:** Aegis' eigene Gegenrechnung von JJs genannten DCF-Annahmen deckte eine Rechenungenauigkeit auf ($110-125 war mit JJs eigenen Annahmen nicht reproduzierbar) — JJ bestätigte das nach Konfrontation selbst.
- **Zentrale These:** Rekord-Q2-2026-Zahlen (+20,4% Umsatz, Non-GAAP-EPS +24%) und angehobene Q3-Guidance bestätigen operative Stärke, aber der Kurs (+30% in einer Woche, $95,77) hat das bereits vorweggenommen. Neuer Struktur-Risiko-Fund: Südkorea-Kartellermittlung seit 15.07.2026 (Rambus+Montage+Renesas, Vorwurf Preisabsprache).
- **Konkrete Erwartung (DCF, reconciliiert):** Bear $40-50 · Base $50-70 · Bull $95-115. Kurs $95,77 liegt am oberen Rand/über der Base-Spanne.
- **These-Bruch-Kriterien:** (a) Südkorea-Kartellverfahren führt zu Anklage/hohen Bußgeldern; (b) Top-2-Kundenkonzentration steigt Richtung >50%; (c) Q3/Q4-Guidance wird verfehlt; (d) HBM4E/AI-Memory-Narrativ bleibt ohne erkennbare 2027er-Umsatzwirkung.
- **Nächster Prüfpunkt:** Q3'26-Earnings (02.11.2026) + Entwicklung Südkorea-Kartellverfahren.
- **Prüf-Zeithorizont:** 6 Monate (2027-03-21).

## Erledigt (Post-Mortem abgeschlossen)

_Noch keine fälligen Einträge._

<!-- Format je Post-Mortem-Eintrag:

### [Ursprüngliches Datum] — Ticker (verschoben aus "Offene Einträge")
- Ergebnis nach Ablauf des Prüf-Zeithorizonts: Base-Case getroffen? Näher an Bear oder Bull? These-Bruch-Kriterium eingetreten, obwohl noch gehalten/beobachtet, oder umgekehrt?
- Tatsächliche Kursentwicklung seit Empfehlung.
- Kurzes, ehrliches Fazit - kein Schönreden.

-->
