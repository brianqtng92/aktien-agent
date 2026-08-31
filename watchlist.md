# Watchlist – Brians Aktien-Agent

**Angelegt:** 2026-08-28 · **Zweck (von Brian festgelegt):** Eigenständige Liste von
Aktien außerhalb des aktuellen Depots, die entweder als möglicher **Ersatz für
bestehende Depot-Positionen** dienen könnten oder als **interessante Ergänzung**
fürs Portfolio beobachtet werden. Läuft **jede Woche automatisiert im Hintergrund**
(siehe `architecture.md`, Abschnitt "Watchlist-System") mit fester Obergrenze
**max. 20-30 Werte**, damit Brian nicht den Überblick verliert. Erscheint ab sofort
als eigener Abschnitt im wöchentlichen Wochenfazit (neu rein / raus + 1-2 Sätze
Begründung).

**Struktur (2026-08-28, von Brian gefordert):** Die Watchlist folgt derselben
Kategorie-Logik wie das Depot selbst (siehe `architecture.md`, Abschnitt 3) –
**Champions / Profi / Talent** – damit ein Watchlist-Wert direkt erkennen lässt,
in welche Depot-Kategorie er bei einer Aufnahme fallen würde bzw. welche Art von
Depot-Position er ersetzen könnte. Alle drei Kategorien sind bewusst gefüllt.

**Aktueller Stand:** 30 Werte gesamt – **Champions: 13 · Profi: 10 · Talent: 7**
(21 von Brian vorgegeben, 9 systematisch von Jarvis ergänzt, um die Liste
sektoral/geografisch breiter aufzustellen und alle drei Kategorien sauber zu
füllen; zuletzt Exponent (EXPO) am 2026-08-29 aus einer gezielten
Depot-Lücken-Suche ergänzt).

**Hinweis zur Kategorisierung:** Die Einordnung folgt derselben Logik wie im
Depot – Champions = etablierte Weltklasse-Compounder mit breitem, bewiesenem
Moat (TMR-Pfad); Profi = solide Qualitätsfirmen/Nischenführer, die ihre
Langfrist-Bewährung noch nicht vollständig abgeschlossen haben oder zyklischer/
konzentrierter sind (Scout-Pfad oder TMR Quick Filter); Talent = Werte mit
echtem spekulativem Risiko (Bewertung, Zyklik, Unternehmensgröße, Datenlage),
auch wenn die Marktkapitalisierung selbst schon groß ist (z.B. Palantir –
Größe schützt hier nicht vor Bewertungsrisiko). Das ist eine erste,
systematische Einordnung von Jarvis – Brian kann jederzeit einzelne Werte
manuell in eine andere Kategorie verschieben.

---

## Legende
- **Herkunft:** BRIAN = von Brian selbst vorgegeben (2026-08-28) · JARVIS = von Claude/Jarvis systematisch ergänzt (2026-08-28)
- **Status:** 🆕 NEU (diese Woche aufgenommen) · ✅ BEOBACHTUNG (unverändert) · ⚠️ RISIKO (Abstiegs-Kandidat, wird genauer beobachtet)
- **[EX-DEPOT]** = Position, die Brian im Zuge der Depot-Restrukturierung vom 27./28.08.2026 verkauft hat und jetzt zur möglichen Wiederaufnahme beobachtet.

---

## 🏆 Champions (13) – etablierte Weltklasse-Compounder

| Ticker/Börse | ISIN | Firma | Region | Sektor | Herkunft | Status | Kurzthese |
|---|---|---|---|---|---|---|---|
| NVDA (NASDAQ) | US67066G1040 | Nvidia Corp. | USA | Halbleiter (KI-Beschleuniger) | BRIAN | 🆕 | Dominanter GPU-/KI-Infrastruktur-Anbieter, faktisches Ökosystem-Monopol (CUDA), zentrale Position im KI-Capex-Zyklus. |
| V (NYSE) | US92826C8394 | Visa Inc. | USA | Zahlungsverkehr | BRIAN | 🆕 **[EX-DEPOT]** | Ehemalige Depot-Position (verkauft 27.08.2026 @ 326,40€). Zahlungsnetzwerk-Duopol mit Mastercard, extrem hohe Kapitalrendite. |
| MA (NYSE) | US57636Q1040 | Mastercard Inc. | USA | Zahlungsverkehr | JARVIS | 🆕 | Direktes Duopol-Pendant zu Visa – falls Visa nicht zurückgekauft wird, naheliegende Alternative mit identischer Moat-Logik. |
| SPGI (NYSE) | US78409V1044 | S&P Global Inc. | USA | Finanzinfrastruktur (Ratings/Indizes/Daten) | BRIAN | 🆕 **[EX-DEPOT]** | Ehemalige Depot-Position (verkauft 27.08.2026 @ 378,15€). Duopol-Moat bei Ratings/Indizes. |
| SYK (NYSE) | US8636671013 | Stryker Corp. | USA | MedTech (Orthopädie/Chirurgierobotik) | BRIAN | 🆕 **[EX-DEPOT]** | Ehemalige Depot-Position (verkauft 27.08.2026 @ 279,75€). Qualitäts-MedTech mit starkem Robotik-Wachstumstreiber (Mako-System). |
| ASML (Amsterdam) | NL0010273215 | ASML Holding N.V. | Europa (NL) | Halbleiterausrüstung (EUV-Lithografie) | JARVIS | 🆕 | EUV-Lithografie-Monopolist – ohne ASML keine Advanced-Chip-Fertigung möglich, der kritischste Baustein der gesamten Halbleiter-Lieferkette. |
| TSM (NYSE ADR) | US8740391003 | Taiwan Semiconductor Mfg. (TSMC) | Asien (Taiwan) | Halbleiter-Auftragsfertigung (Foundry) | JARVIS | 🆕 | Fertigt die KI-Chips von Nvidia & Co. tatsächlich – größter Foundry-Moat der Welt, strukturelles Kernstück der KI-Lieferkette. |
| FICO (NYSE) | US3032501047 | Fair Isaac Corp. | USA | Finanzdaten/Analytics (Kredit-Scoring) | JARVIS | 🆕 | Faktisches Monopol beim US-Kredit-Scoring (FICO-Score als Industriestandard) – einer der stärksten Preissetzungsmacht-Moats überhaupt. |
| 6861 (Tokyo) | JP3236200006 | Keyence Corp. | Japan | Fabrikautomatisierung (Sensorik/Machine Vision) | BRIAN | 🆕 **[EX-DEPOT]** | Ehemalige Depot-Position (verkauft 27.08.2026 @ 439,90€). Einer der profitabelsten Industriekonzerne der Welt (fabless, extrem hohe Marge). |
| 7741 (Tokyo) | JP3837800006 | Hoya Corp. | Japan | Optik/Halbleiter-Photomasken & MedTech | BRIAN | 🆕 | Diversifizierter Qualitätskonzern mit Weltmarktführerschaft bei Halbleiter-Photomasken-Rohlingen plus stabilem MedTech-Standbein. |
| BN (NYSE/TSX) | CA11271J1075 | Brookfield Corp. | Kanada | Alternative Asset Management/Holding | BRIAN | 🆕 | Diversifizierter Vermögensverwalter/Holding (Infrastruktur/Erneuerbare/Private Equity) – Compounder über Kapitalallokation statt Einzelprodukt-Moat. |
| CPRT (NASDAQ) | US2172041061 | Copart Inc. | USA | Fahrzeugauktionen/Salvage | JARVIS | 🆕 | Marktführer bei Online-Fahrzeugauktionen mit Netzwerk-Moat (Flächen/Logistik) und sehr hoher Kapitalrendite. |
| ROL (NYSE) | US7757111049 | Rollins Inc. | USA | Schädlingsbekämpfung (Dienstleistung) | JARVIS | 🆕 | Extrem stabiler, wiederkehrender Cashflow (Abo-artiges Geschäftsmodell), einer der zuverlässigsten Compounder im S&P 500. |

## ⚙️ Profi (10) – solide Qualitätsfirmen/Nischenführer, Bewährung läuft noch

| Ticker/Börse | ISIN | Firma | Region | Sektor | Herkunft | Status | Kurzthese |
|---|---|---|---|---|---|---|---|
| CRWD (NASDAQ) | US22788C1053 | CrowdStrike Holdings | USA | Cybersecurity (Endpoint/Cloud) | BRIAN | 🆕 | Cloud-native Cybersecurity-Plattform mit hoher Kundenbindung (Falcon), profitiert von wachsender Angriffsfläche – noch nicht so lange bewiesen wie ein Champions-Titel. |
| ANET (NYSE) | US0404132054 | Arista Networks | USA | Netzwerktechnik (Rechenzentren) | BRIAN | 🆕 | Führender Anbieter von Hochleistungs-Switches für Cloud-/KI-Rechenzentren, direkter Profiteur des KI-Infrastruktur-Ausbaus. |
| VRT (NYSE) | US92537N1081 | Vertiv Holdings | USA | Rechenzentrums-Infrastruktur (Kühlung/Stromversorgung) | BRIAN | 🆕 | Zentraler Ausrüster für Rechenzentrums-Kühlung/-Stromversorgung, noch relativ junge Börsenhistorie als eigenständiger Titel. |
| FTNT (NASDAQ) | US34959E1091 | Fortinet Inc. | USA | Cybersecurity (Netzwerksicherheit/Firewalls) | JARVIS | 🆕 | Ergänzt CrowdStrike um die Netzwerk-/Firewall-Seite der Cybersecurity-Landschaft – Diversifikation innerhalb des Sektors. |
| MPWR (NASDAQ) | US6098391054 | Monolithic Power Systems | USA | Halbleiter (Power Management) | BRIAN | 🆕 | Nischenführer bei Power-Management-Chips für Rechenzentren/KI-Server, hohe Margen, aber zyklischer als ein reiner Champions-Titel. |
| AIT (NYSE) | US03820C1053 | Applied Industrial Technologies | USA | Industrielle Distribution (Antriebstechnik/Automatisierung) | BRIAN | 🆕 | Qualitäts-Distributor mit stetigem Cross-Selling-Modell, profitiert von Reshoring/Automatisierung in der US-Industrie. |
| 6146 (Tokyo) | JP3548600000 | Disco Corp. | Japan | Halbleiterausrüstung (Wafer-Dicing/-Schleifen) | BRIAN | 🆕 | Führend bei Präzisions-Schneide-/Schleiftechnik für Halbleiter-Wafer, profitiert vom Advanced-Packaging-Trend – zyklisches Semicap-Geschäft. |
| WSO (NYSE) | US9427491025 | Watsco Inc. | USA | HVAC-Distribution (Klima-/Heiztechnik) | JARVIS | 🆕 | Familiengeführter Marktführer in der nordamerikanischen HVAC-Distribution – US-Pendant zur Beijer-Ref-Logik aus dem Nicht-Index-Screening. |
| NVT (NYSE) | IE00BDVJJQ56 | nVent Electric plc | USA/Irland | Elektrotechnik (Verbindungs-/Schutztechnik) | BRIAN | 🆕 | Profiteur von Elektrifizierung, Rechenzentrums-Ausbau und Reshoring; solide, aber weniger dominant als ein Champions-Titel. |
| EXPO (NASDAQ) | US30214U1025 | Exponent, Inc. | USA | Wissenschaftlich-technisches Consulting (Gerichtsgutachten/Produktsicherheit/Schadensanalyse) | JARVIS | 🆕 | 2026-08-29 aus gezielter Depot-Lücken-Suche: kapitalleichtes Reputations-/Expertise-Moat-Geschäft (ROIC ~27%, Nettomarge ~20%), unkorreliert zu bestehenden Software-/Fintech-/Space-Positionen. Bewusster Gegenentwurf zur AIT-Analyse (margenschwacher Distributor) – hier margenstark und asset-light. Wachstum moderat (~9%), daher Profi statt Champions. |

## 🚀 Talent (7) – spekulative Spitze, hohes Risiko/hohe Upside

| Ticker/Börse | ISIN | Firma | Region | Sektor | Herkunft | Status | Kurzthese |
|---|---|---|---|---|---|---|---|
| PLTR (NASDAQ) | US69608A1088 | Palantir Technologies | USA | Software (Daten-/KI-Plattform) | BRIAN | 🆕 | Trotz riesiger Marktkap ein echter Talent-Fall: extreme Bewertung, These noch nicht über einen vollen Zyklus bewiesen – Größe schützt hier nicht vor Risiko. |
| INOD (NASDAQ) | US4576422053 | Innodata Inc. | USA | Daten-/KI-Trainingsdienstleistungen | BRIAN | 🆕 | Kleiner, spekulativer Profiteur des KI-Booms (Daten-Annotation für große KI-Modelle), Kundenkonzentrationsrisiko. |
| USLM (NASDAQ) | US9119221029 | United States Lime & Minerals | USA | Baustoffe/Industriemineralien | BRIAN | 🆕 | Regionaler Nischenmonopolist mit sehr hoher Kapitalrendite, aber klein/illiquide genug, um als Talent statt Champions zu gelten. |
| SKWD (NASDAQ) | US8309401029 | Skyward Specialty Insurance | USA | Spezialversicherung (Nischen-Underwriting) | BRIAN | 🆕 | Kleinerer Spezialversicherer mit diszipliniertem Underwriting, noch kurze Börsenhistorie – bereits Gegenstand einer früheren TMR-Analyse (siehe `analysen/`). |
| 6920 (Tokyo) | JP3979200007 | Lasertec Corp. | Japan | Halbleiterausrüstung (EUV-Masken-Inspektion) | BRIAN | 🆕 | Faktisches Weltmonopol bei EUV-Masken-Inspektion, aber klassisch zyklisches Semicap-Geschäft mit hoher Kursvolatilität. |
| 6323 (Tokyo) | JP3982200002 | Rorze Corp. | Japan | Halbleiterausrüstung (Wafer-Handling-Robotik) | BRIAN | 🆕 | Kleiner Nischenzulieferer für Wafer-Transport-Robotik – hohe Relevanz für den Fab-Ausbau, aber kleine, zyklische Firma. |
| 7747 (Tokyo) | JP3110650003 | Asahi Intecc Co. | Japan | MedTech (Führungsdrähte für Katheter) | BRIAN | 🆕 | Weltmarktführer bei Katheter-Führungsdrähten, enger technischer Moat, aber konzentriertes Nischengeschäft mit begrenzter Diversifikation. |

---

## Lateinamerika / sonstige Schwellenländer – noch offen

Aus dem Nicht-Index-Screening vom 2026-08-28 (siehe
`analysen/nicht-index-screening-konsolidiert-2026-08-28.md`) kam kein Name,
der gleichzeitig die Qualitäts-/Big-Player-Logik dieser Watchlist UND eine
echte Lateinamerika-Zuordnung erfüllt (Alicorp/Peru wäre der einzige echte
Kandidat, käme als Talent-Position infrage, aber noch nicht offiziell
aufgenommen – siehe Offene Punkte).

**Update 2026-08-31 (täglicher Kandidaten-Scan, voller 3-fach-Quick-Filter,
siehe `analysen/WEGE3-TMR-cross-check-fazit-2026-08-31.md`):** WEG S.A.
(WEGE3, ISIN BRWEGEACNOR0, B3 São Paulo, Brasilien, Elektrotechnik/
Industrieautomation) besteht Strategie-Fit-Gate, Duplikations-Check und
Identity-Gate klar, und alle drei KIs (Jarvis/Jack/Conan) stufen die
Unternehmensqualität einstimmig als Champion-Tier ein (ROIC 32-36%, Wide
Moat, Net Cash, globale Diversifikation) – aber ebenso einstimmig
**VERDICT: BEOBACHTEN/WATCH**, da die aktuelle Bewertung (~33-34x KGV) keine
Sicherheitsmarge lässt (kein Sofort-Kauf-Signal). **Noch NICHT formal in die
Champions-Tabelle aufgenommen**, da die Watchlist bei 30/30 (Obergrenze)
steht und ein Ersatz eines bestehenden Champions-Werts (mehrere davon von
Brian bewusst als Ex-Depot-Wiederaufnahme-Kandidaten markiert) eine
Entscheidung ist, die über die tägliche Scan-Routine hinausgeht – Brian
entscheidet, ob WEG einen Slot bekommt oder vorerst nur hier als
LatAm-Beobachtungsposten außerhalb der 30er-Kapazität geführt wird. Nächster
Prüfpunkt: Rücksetzer Richtung 23-25x KGV (Jack) würde die Einschätzung
deutlich verbessern.

---

## Aufnahme-Kriterien (für künftige automatisierte Ergänzungen)

Ein Kandidat wird nur bei freiem Slot (siehe Obergrenze 20-30, aktuell 29)
aufgenommen, wenn mindestens eines zutrifft:
1. **Qualitäts-Compounder mit klarem Moat**, der im TMR-Sinne (siehe `prompts/`)
   potenziell KAUFEN/BEOBACHTEN-Niveau erreichen könnte → Kategorie **Champions**.
2. **Solide Nischenfirma/Qualitätswert**, dessen Langfrist-Bewährung noch läuft
   oder die zyklischer/konzentrierter ist → Kategorie **Profi**.
3. **"Big Player"-Potenzial-Kandidat** (Scout-Pfad-Logik) mit plausibler These,
   künftig deutlich größer/relevanter zu werden, aber mit echtem spekulativem
   Risiko → Kategorie **Talent**.
4. **Möglicher Ersatzkandidat** für eine bestehende, schwächere Depot-Position.
5. **Ex-Depot-Position**, die Brian bewusst weiter im Blick behalten will.

## Ausschluss-/Abstiegs-Kriterien (wöchentlich geprüft)

Ein Wert fliegt von der Watchlist, wenn mindestens eines zutrifft:
1. **Katastrophale Quartalszahlen** (Umsatz-/Gewinneinbruch, Guidance-Cut) ohne
   glaubwürdige Erholungsstory.
2. **Gerissene fundamentale These** – der ursprüngliche Moat-/Wachstumsgrund ist
   nicht mehr intakt (z.B. Verlust des Technologie-Vorsprungs, neuer
   disruptiver Wettbewerber).
3. **Fraud-/Bilanzskandal, Going-Concern-Warnung oder harter Regulatorik-
   Schlag** (Kartellstrafe, Produktverbot, Sanktion).
4. **Übernahme oder Delisting** – der Wert verschwindet schlicht vom Markt.
5. **Manuelle Entscheidung von Brian** – jederzeit möglich, unabhängig vom
   automatisierten Check.

Reine Kursrückgänge oder eine "nur" hohe Bewertung sind für sich genommen KEIN
Ausschlussgrund – die Watchlist bildet Unternehmensqualität ab, nicht Timing
(das übernimmt bei Bedarf der TA-Pfad). Ein Wert KANN aber zwischen Kategorien
wandern (z.B. Profi → Champions nach mehreren bewiesenen Quartalen, oder
Champions → Talent bei aufkommenden Zweifeln), ohne die Watchlist komplett zu
verlassen.

## Offene Punkte
- Lateinamerika-Slot bewusst leer gelassen (siehe oben) – Alicorp (Peru) als
  möglicher erster Talent-Kandidat steht zur Diskussion mit Brian an.
- Kategorisierung (Champions 13 / Profi 9 / Talent 7) ist eine erste,
  systematische Einordnung von Jarvis nach Marktkap/Reifegrad/Zyklik-Logik –
  Brian kann jederzeit einzelne Werte manuell verschieben, falls er einen
  Wert anders einschätzt (z.B. Palantir wurde bewusst als Talent statt
  Champions eingestuft, trotz großer Marktkapitalisierung, wegen des
  Bewertungsrisikos).
- ISINs wurden am 2026-08-28 per WebSearch verifiziert (Quellen: justetf.com,
  divvydiary.com, cbonds.com, MarketScreener u.a.) – bei einer echten Order
  sollte die ISIN nochmal beim jeweiligen Broker gegengecheckt werden.
