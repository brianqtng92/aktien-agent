# Synopsys Inc. (SNPS) — Full Deep Dive, 3-fach TMR-Cross-Check — 2026-09-16

**Auslöser:** Brians Bitte "Jetzt möchte ich eine SYNOPSYS Full Deep dive Analyse". SNPS ist ein komplett neuer Kandidat, weder in watchlist.md noch im Depot. Erster Full Deep Dive nach dem Jarvis→Aegis-Rebranding und den vier neuen Rigor-Punkten 43-46 (Verwässerungs-Wasserfall, Meilenstein-Timeline, Risiko-Quadrant, Agent-Score-Herleitung).

**Ergebnis vorweg:** Alle drei KIs konvergieren unabhängig auf **BEOBACHTEN**, Agent Score 6-7/10, Konfidenz 🟡 MITTEL — trotz eines komplexen Sondersituation-Setups (Mega-Merger-Integration, aktivistischer Investor, Investor Day in 2 Wochen). Wichtiger methodischer Fund dieser Runde: **JJ (Gemini) hat trotz aktivierter Web-Search den aktuellen Kurs um +54% zu hoch angegeben** ($577,92 statt real $375,73) — ein eigenständiger, dokumentierter Beleg für [[feedback_ki_suche_kann_trotzdem_halluzinieren]], dieses Mal auf der Kern-Kennzahl selbst statt auf einem Nebenfakt.

---

## Aegis Live-Check (Twelve Data, autoritative Quelle für Kurse)

Kurs **$375,725** [LIVE] (16.09.2026, +2,18% intraday), 52W-Range **$362,55-$539,48** [LIVE] (-30,4% vom Hoch). RSI14 38,71→34,56 (fallend, noch nicht extrem überverkauft), MACD deutlich negativ (-8,47, Signal -3,76, Hist -4,71, aber leicht sich verbessernd ggü. Vortagen), Kurs unter SMA200 ($446,9) und unter dem mittleren Bollinger-Band ($405,15), nahe dem unteren Band ($360,07). ATR14 $15,25 (≈4,1% des Kurses). OBV-Trend der letzten Tage klar negativ (Verkaufsdruck). **Technisches Gesamtbild: bearish**, Kurs nahe 52W-Tief, aber (noch) kein klassisches Extrem-Oversold-Signal.

**Twelve-Data-Limitierung dieser Runde:** `/statistics`, `/income_statement`, `/balance_sheet`, `/cash_flow`, `/analyst_ratings`, `/price_target`, `/earnings`, `/insider_transactions` sind mit dem aktuellen API-Key gesperrt ("pro/ultra/venture/enterprise"-Plan nötig). Alle Fundamentaldaten dieser Analyse stammen daher aus WebSearch/SEC-EDGAR-Primärquellen (v.a. via Conans Recherche, siehe unten) statt aus Twelve Data — entsprechend als [VERIFIED]/[N/V] getaggt, nie als [LIVE].

**Eigene WebSearch-Recherche (vor KI-Dispatch):** Ansys-Closing 17.07.2025 ($35 Mrd., größte EDA/CAE-Fusion überhaupt), China-SAMR-Freigabe 14.07.2025 mit Auflagen (Bestandsverträge chinesischer Kunden müssen honoriert werden). Elliott Investment Management seit März 2026 Multi-Milliarden-Beteiligung, Cooperation Agreement Mai 2026, Board-Sitz Jesse Cohn seit 01.06.2026. Verkauf Processor-IP-Sparte (ARC-V/ARC CPU/DSP/NPU-IP) an GlobalFoundries, angekündigt 14.01.2026, Closing erwartet 2. Halbjahr 2026. Cadence kontert mit eigenem $3,16-Mrd.-Zukauf von Hexagons Design/Engineering-Geschäft (Closing 23.02.2026) — direkte strukturelle Antwort auf die Ansys-Fusion. FY26-Guidance (nach Q3-Bericht Ende August): Umsatz $9,69-9,74 Mrd. inkl. ca. $2,98 Mrd. Ansys-Beitrag, Non-GAAP-Op-Margin ~41,5%, Non-GAAP-EPS $15,04-15,10. Investor Day 30.09.2026 als von BofA benannter "key catalyst".

## Aegis eigene DCF-Schätzung (Python, Rule 20)

Basis: Kurs $375,725 [LIVE], ~192 Mio. verwässerte Aktien (FY26-Guidance-Mitte, [VERIFIED] via Conan/SEC), Net Debt ~$6,5 Mrd. [VERIFIED via Conan/SEC], FCF-Guidance FY26 $2,6 Mrd. [VERIFIED]. Beta 1,15 (Mittelwert aus JJs 1,11 und Conans 1,23 — Twelve-Data-Statistics gesperrt, kein eigener Live-Wert verfügbar, daher [N/V]-Ersatzannahme). Rf 4,9% (10J-UST, WebSearch/AP News Mitte September 2026), ERP 5,0%. WACC-Berechnung: Cost of Equity 10,65%, After-Tax Cost of Debt 4,02%, Gewichtung 91,7%/8,3% → **WACC 10,10%**.

| Szenario | 5J-FCF-Wachstumspfad | Terminal-g | Fair Value | Δ vs. Kurs $375,73 | TV-Anteil EV |
|---|---|---|---|---|---|
| Bear (Integration stockt, Cadence gewinnt Anteile) | 3%→2%→2%→2%→2% | 2,0% | $138,30 | -63,2% | 68,2% |
| Base (Integration gelingt, organisch 8-10%) | 10%→9%→8%→7%→6% | 3,0% | $209,55 | -44,2% | 73,2% |
| Bull (Silicon-to-Systems wird Standard) | 16%→15%→13%→11%→9% | 3,5% | $280,60 | -25,3% | 76,1% |

**Reverse-DCF:** implizites konstantes 5J-FCF-Wachstum bei Terminal-g 3,0% und WACC 10,10%, das den aktuellen Kurs rechtfertigt: **21,3% p.a.** — das liegt spürbar ÜBER dem Wachstumspfad meines eigenen Bull-Szenarios (Ø ~12,8%). Der Markt preist damit eine Silicon-to-Systems-Erfolgsgeschichte ein, die aggressiver ist als selbst mein optimistisches Szenario.

**Wichtiger methodischer Hinweis (Sanity-Check-Pflicht):** Alle drei DCF-Ansätze (Aegis reiner Gordon-Growth, Conans Gordon-Growth $260, Conans Exit-Multiple $390-410) zeigen dasselbe Muster: **TV-Anteil am Enterprise Value liegt durchgängig über der 70%-Warnschwelle** (68-76% bei Aegis, ~54%/>75% bei Conan je Methode). Das ist kein Rechenfehler, sondern eine ehrliche Eigenschaft der Bewertungssituation: bei einer FCF-Basis von nur $2,6 Mrd. gegen eine EV von ~$78,6 Mrd. muss fast der gesamte Wert aus weit in der Zukunft liegendem Wachstum kommen. Reiner Gordon-Growth-DCF unterschätzt SNPS daher tendenziell strukturell (bestätigt durch die Konvergenz aller drei unabhängigen Gordon-Rechnungen weit unter dem aktuellen Kurs), während die Exit-Multiple-Methode empfindlich auf das gewählte Peer-Multiple reagiert — beide Methoden sind hier nur mit Vorsicht als Fair-Value-Anker zu nutzen, eher als Bandbreiten-Orientierung.

**Analysten-Konsens-Sanity-Check:** Laut Conans Recherche liegt der Analysten-Konsens bei ca. $544,97 Kursziel (Range $414,77-$633), was +48% Upside implizieren würde. Das weicht von Aegis' eigenem DCF-Base-Case ($209,55) um weit mehr als die 25-30%-Warnschwelle ab. **Aegis-Einordnung:** DCF-Modelle mit reinem Fokus auf den Cashflow der Kernsparten (EDA+IP, ohne vollen Ansys-Synergie-Case) sind für ein frisch fusioniertes, noch nicht bewiesenes Bundle-Geschäft systematisch zu konservativ — der Analysten-Konsens preist wahrscheinlich einen erfolgreichen Ansys-Cross-Sell UND eine Multiple-Erholung nach dem Investor Day ein, die noch nicht bewiesen ist. Beide Extreme (reiner DCF vs. Analysten-Konsens) sind daher als Leitplanken zu verstehen, nicht als Punktschätzung.

---

## JJ (Gemini) — Runde 1

**⚠ Kritischer Datenqualitäts-Fund:** JJ nannte trotz `enable_search=true` einen aktuellen Kurs von **$577,92** und eine 52W-Range von **$405-$830** — beide Werte sind eindeutig falsch (Twelve Data LIVE: $375,73 / $362,55-$539,48; von Conan unabhängig fast exakt bestätigt). Auch Marktkapitalisierung ($90,15 Mrd. statt korrekt ~$72 Mrd.) und der abgeleitete Share-Count (165 Mio. statt Conans SEC-verifizierte 191,6 Mio.) sind Folgefehler aus derselben falschen Kursbasis. **Alle quantitativen JJ-Outputs, die auf dieser Kursbasis aufbauen (WACC-Berechnung, DCF-Sanity-Check-Bereich $757-867), werden für die Synthese verworfen.** Dies ist eine eigenständige Bestätigung von [[feedback_ki_suche_kann_trotzdem_halluzinieren]] — dort ging es um einen CFO-Namen und einen SBC-Betrag bei RMBS, hier um die grundlegendste aller Kennzahlen trotz aktivem Search-Grounding.

**Qualitative Einschätzungen (unabhängig von der Kursbasis, daher weiter verwertbar):**
- DNA-Check: K-Basis 1/4, E-Basis 3/4 — Operativer Leverage ✅, ROIC/EPS-CAGR/ROE ❌ (N/V wegen Fusions-Verzerrung, explizit nicht als "schlecht" gewertet, sondern als Datenlücke).
- Moat-Score **4/4 STARK**, Trend **STÄRKER** — EDA+CAE-Kombination erhöht Switching-Costs, Ansys-Fusion stärkt den Moat strukturell trotz kurzfristigem Integrationsrisiko.
- KSF-Scorecard (6 Faktoren): KI-native Design-Flows ✅, Foundry-Zertifizierungen ✅, Cross-Sell-Integration 🟡, Reaktion auf Cadence-Hexagon 🟡, Backlog-Qualität 🟡, Bilanzdisziplin/Deleveraging ✅.
- Management-Score **1,5/7 RISIKO** — Guidance-Hit-Rate als einziger klarer Pluspunkt, Rest N/V oder durch Fusion verzerrt (v.a. Share-Count-Verwässerung durch Aktien-Emission für den Ansys-Deal).
- Elliott-Faktor: eingeordnet als **Qualitäts-Signal** (kompetenter Aktivist sieht Unterbewertung, kooperative statt konfrontative Vereinbarung).
- Verwässerungs-Wasserfall: als anwendbar markiert (wegen der Aktien-Emission für den Ansys-Deal) — methodisch nicht ganz korrekt, da die Regel auf Wandelanleihen/Preferred/Warrants/große unvestete Optionsprogramme zielt, nicht auf eine bereits abgeschlossene, einmalige M&A-Aktienausgabe. Conan bewertet dies korrekt als "entfällt ersatzlos" (siehe unten).
- Kill-Sheet: Stop-These-Trigger (Backlog schrumpft weiter, Cadence gewinnt nachweislich Marktanteil, Elliott verkauft/eskaliert, Integrationskosten übertreffen Erwartungen) und Bull-Trigger (positiver Investor Day, beschleunigtes organisches Wachstum, schnelleres Deleveraging, neue KI-Produkte) decken sich inhaltlich stark mit Conans Kill-Sheet.
- **Verdict: BEOBACHTEN, Agent Score 6/10, Konfidenz 🟡 MITTEL, Tier 3.**

---

## Conan (ChatGPT) — Runde 1

Deutlich granularere, SEC-EDGAR-primärquellen-gestützte Recherche (10-Q vom 31.07.2026 direkt zitiert), Kursbasis ($372,35, Intraday-Range $367,40-$373,95, 52W-Range $362,55-$539,48) **deckungsgleich mit Twelve Data** — reines Live-Feed-Grounding hat hier funktioniert, im Gegensatz zu JJ.

- Going-Concern-Precheck: kein Treffer für "going concern"/"substantial doubt" im 10-Q — **going_concern_flag: false** [VERIFIED].
- DNA-Check: K-Basis **1/4** (ROIC unbereinigt nur ~1,7-2,0% wegen $26,8 Mrd. Goodwill + Amortisation, bereinigt ~8-10% — beide unter 20%; ROE unbereinigt ~3-4%, bereinigt ~9-10% — beide unter 15%; EPS-CAGR N/V wegen GAAP-Verzerrung; Operativer Leverage als einziges Pass). E-Basis **3/4** (GAAP-Op-Margin nur ~10,4% FY26-Guidance ❌; Revenue-CAGR organisch ex-Ansys ~9,9% ✅; Net-Debt/EBITDA ~1,5-1,6x ✅; Capex/Umsatz ~2,3% ✅). SBC/Umsatz 9M ~10,0% (unter 15%-Schwelle).
- **Verwässerungs-Wasserfall: korrekt als "entfällt ersatzlos" markiert** (keine Wandelanleihen/Preferred/signifikante Warrants gefunden — die Aktien-Verwässerung durch den Ansys-Deal ist bereits vollständig im aktuellen Share-Count enthalten, kein zukünftiger Wasserfall-Trigger).
- Share-Count-Trend: 154,1 Mio. (Okt. 2024) → 191,6 Mio. (Jul. 2026), **+24% Verwässerung**, getrieben durch ~30 Mio. neue Aktien für den Ansys-Deal plus $2,0 Mrd. NVIDIA-Private-Placement.
- Moat-Score **4/4 STARK**, Trend **STABIL bis STÄRKER** — mit einer wichtigen Nuance, die JJ nicht fand: laut EU-Kommissions-Fusionsentscheidung hat Synopsys in einzelnen Subsegmenten (Place & Route) tatsächlich Marktanteile an Cadence verloren (Rückgang von ~60-70% auf ~40-50% zwischen 2018 und 2024, während Cadence von ~30-40% auf ~40-50% stieg) — ein echter, primärquellenbelegter Moat-Decay-Hinweis in einem Teilsegment, auch wenn der Gesamt-Moat stark bleibt.
- Debt-Maturity: konkrete Fälligkeitstabelle mit Kupons (2027 $1,0 Mrd. @4,55%, 2028 $1,0 Mrd. @4,65%, 2030 $2,0 Mrd. @4,85%, 2032 $1,5 Mrd. @5,00%, 2035 $2,4 Mrd. @5,15%, 2055 $2,1 Mrd. @5,70%) — Refinanzierungsrisiko 🟡 MITTEL (solide Coverage auf Non-GAAP-Basis, aber GAAP-EBIT/Interest nur ~1,6x).
- Divestiture-Check: Processor-IP-Verkauf brachte $440 Mio. Netto-Erlös in 9M FY26, FY26-Guidance reflektiert ca. $40 Mio. Umsatzeffekt — strategisch positiv (Fokussierung), Backlog-Rückgang ($11,4 Mrd. FY25-Ende → $10,9 Mrd.) teilweise dadurch erklärt.
- KSF-Scorecard: 4× ✅ (KI-native Flows, Foundry/Sign-off-Vertrauen, Backlog-Qualität, Bilanzdisziplin), 2× 🟡 (Cross-Sell-Integration, Cadence-Antwort).
- Management-Score **1/7 RISIKO** — fast identisch mit JJs 1,5/7, unabhängig konvergiert.
- Elliott-Faktor: nuancierter als JJ — "leicht positiv als Margen-/Disziplin-Katalysator, aber auch Warnsignal, dass externe Governance-Unterstützung nötig wurde" (nicht rein positiv wie bei JJ).
- Insider: Executive Chair Aart de Geus verkaufte Ende Aug./Anfang Sept. 2026 Aktien (u.a. 49.641 Stück, ca. $21,38 Mio., 01.09.2026) — als "kein Kaufsignal, aber nicht these-killend (10b5-1-Kontext)" eingeordnet.
- Eigene DCF: Gordon-Growth $260 (TV-Anteil ~54%), Exit-Multiple $390-410 (TV-Anteil >75%), gewichteter eigener Fair Value $375-400 — **auffällig nah am aktuellen Kurs**, während Aegis' eigener reiner Gordon-Growth-Ansatz mit $209,55 deutlich konservativer liegt (siehe Diskussion oben zur strukturellen Gordon-Growth-Unterschätzung).
- **Verdict: BEOBACHTEN, Agent Score 7,0/10, Konfidenz 🟡 MITTEL, Sizing: Tier 2/kleine Testposition erst nach Investor Day, kein Tier 1 vor Integrationstransparenz.**

---

## Cross-Check-Synthese (Aegis)

**Konvergenz trotz methodisch unterschiedlicher Rechenwege:** Alle drei unabhängigen Perspektiven (Aegis, JJ, Conan) kommen auf **BEOBACHTEN** mit Agent Score im Band 6-7/10 und Konfidenz 🟡 MITTEL. Das ist bei einem derart komplexen Sondersituation-Kandidaten (Mega-Merger + Aktivist + Investor Day in 2 Wochen) selbst ein positives Signal für die Robustheit des Urteils — keine der drei KIs sieht trotz unterschiedlicher Datenbasis einen klaren Kauf- oder Verkaufsfall.

**Der eigentliche Fund dieser Runde ist kein Rating-Dissens, sondern ein Daten-Integritäts-Fund:** JJs Kursangabe war um +54% zu hoch, trotz aktivem Search-Grounding. Das bestätigt erneut (nach dem RMBS-CFO-Namen-Fall vom 10.09.) [[feedback_ki_suche_kann_trotzdem_halluzinieren]] — diesmal auf der Kennzahl, die am einfachsten zu verifizieren wäre. **Konsequenz für die Methodik:** Twelve Data bleibt für Kurs-/TA-Daten ausnahmslos die Referenz (bereits bestehende Regel, [[feedback_websearch_kurse_unzuverlaessig]]), auch wenn JJ/Conan eigene Recherche betreiben dürfen — jede von einer KI genannte Kurs- oder Marktkapitalisierungs-Zahl wird vor Report-Übernahme gegen Twelve Data geprüft, nicht ungeprüft übernommen. In diesem Fall wäre eine blinde Übernahme von JJs Zahlen zu einer um mehr als die Hälfte überhöhten Bewertungsbasis geführt.

**Bewertungslage:** Die DCF-Spannbreite ist ungewöhnlich weit (Aegis Bear $138/Base $210/Bull $281 via reinem Gordon-Growth; Conan Bear $200-230/Base $375-400/Bull $500-540 via gemischtem Gordon+Exit-Multiple-Ansatz) — nicht wegen schlechter Arbeit, sondern weil TV-Anteil am EV in JEDER Variante über der 70%-Warnschwelle liegt. Das ist eine ehrliche Eigenschaft der aktuellen Situation: SNPS ist heute fundamental kaum von der reinen Cashflow-Basis zu bewerten, sondern fast ausschließlich von der Frage, ob die Ansys-Integration und das "Silicon-to-Systems"-Bundle in 5-10 Jahren echte, verteidigbare Zusatzerlöse bringen. Der Analysten-Konsens (~$545, +48% Upside) unterstellt bereits einen erfolgreichen Case; Aegis' eigener konservativer DCF liegt weit darunter. **Die Wahrheit liegt vermutlich zwischen beiden Anker-Punkten, näher an Conans gemischtem Ansatz** — reine Gordon-Growth-DCFs sind für ein Unternehmen mit derart niedriger aktueller FCF-Basis relativ zur EV strukturell zu konservativ.

**Was für Kaufen spricht:** 4/4-Moat in allen drei Analysen unabhängig bestätigt, EDA+CAE-Kombination mission-critical mit enormen Switching-Costs, Deleveraging läuft schneller als ursprünglich kommuniziert (Term Loans bereits vollständig getilgt), Going-Concern unauffällig, kein Verwässerungs-Wasserfall-Risiko mehr offen (Ansys-Verwässerung ist bereits vollständig eingepreist/abgeschlossen), Backlog trotz leichtem Rückgang mit $10,9 Mrd. weiterhin sehr hoch, Investor Day als konkreter, datierter Katalysator in 2 Wochen.

**Was gegen einen Kauf JETZT spricht:** K-Basis nur 1/4 (ROIC/ROE/EPS-CAGR aktuell klar unter Schwelle, nicht nur Datenlücke sondern reale Verzerrung durch $26,8 Mrd. Goodwill), GAAP-Op-Margin nur ~10,4% (riesige GAAP/Non-GAAP-Lücke, die erst über mehrere Jahre abgebaut werden muss), Management-Score nur 1-1,5/7 (Kapitalallokations-Qualität nach dem Mega-Deal noch nicht bewiesen), TA klar bearish (unter SMA200, negativer MACD, negativer OBV-Trend), Cadence kontert strukturell mit eigenem Multiphysics-Zukauf statt sich geschlagen zu geben, ein primärquellenbelegter Moat-Decay-Hinweis in Place&Route, Insider (Gründer/Executive Chair) verkauft statt zu kaufen, und die DCF-Bewertung hängt fast vollständig an einem noch unbewiesenen Terminal-Value-Case.

**Finales Rating:** **BEOBACHTEN** (Aegis-Synthese). Kein Kauf vor dem Investor Day am 30.09.2026 — dieser muss laut allen drei Analysen konkrete, belastbare Antworten liefern: organisches EDA-Wachstum jenseits der Ansys-Konsolidierung, echte Cross-Sell-/Retention-Kennzahlen statt reiner Umsatzaddition, und einen glaubwürdigen mehrjährigen Margen-/Deleveraging-Pfad. **Agent Score 6-7/10 (Aegis-Mittelwert: 6,5/10), Anker-Bereich 6-8 Qualitäts-Kern** — mit aktivem Mali für die noch unbewiesene Integration und dem primärquellenbelegten Place&Route-Marktanteilsverlust, aktivem Deckel für die GAAP/Non-GAAP-Verzerrung. Konfidenz 🟡 MITTEL, explizit weil die Situation ehrlich in Übergang ist, nicht weil die Recherche unvollständig wäre. Sizing bei Neuaufnahme: Tier 2/3, keine Tier-1-Position vor dem Investor Day.

**Nächster verbindlicher Prüfpunkt:** Investor Day 30.09.2026 (neues Long-Term-Modell erwartet), danach Q4-FY26-Zahlen (geschätzt Anfang Dezember 2026, offizielles Datum noch nicht bestätigt).

---

## PDF

Vollformat-Report: `reports/SNPS-agent-deepdive-2026-09-16.html` / `.pdf` ("J.A.C.K Deep Dive"-Format, Aegis/JJ/Conan/KI-Branding nach dem 16.09.-Rebranding).
