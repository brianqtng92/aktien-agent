# Novo Nordisk A/S (NVO) — Full Deep Dive, 3-fach TMR-Cross-Check — 2026-09-08

**Auslöser:** Brians Bitte "führe einen full deep dive mit Novo Nordisk durch". NVO ist ein komplett neuer Kandidat, weder in watchlist.md noch im Depot. Erster Full Deep Dive dieser Session mit dem erweiterten 28-Punkte-Rigor-Standard (siehe Agent-Playbook.md, Punkte 22-28, ergänzt nach ChatGPT/Gemini-Cross-Review des CLBT-Reports).

**Ergebnis vorweg:** Echte, unaufgelöste Divergenz zwischen Jack (Runde 2: SELL, 3/10) und Conan (Runde 2: WATCHLIST_PLUS) auf Basis identischer Zusatzdaten. Aegis-Synthese: BEOBACHTEN, kein Kauf vor dem Capital Markets Day am 21.09.2026.

---

## Jarvis Fact-Pack Runde 1 (Kernpunkte)

Live-Kurs $45,235 (08.09.2026, -2,93%), 52W-Range $35,12-$64,16, ATH (Juni 2024) $148,15 (-69% vom ATH). Geschäftsmodell: GLP-1-Duopol mit Eli Lilly (Ozempic/Wegovy/Rybelsus, Semaglutide-Basis). Krisenjahr 2025-2026: CagriSema-Enttäuschung #1 (März 2025), Guidance-Cut + Compounding-Sammelklagen (Juli 2025), CEO-Wechsel Jørgensen→Doustdar (Aug. 2025), CagriSema-Enttäuschung #2 (Feb. 2026, verfehlte Nicht-Unterlegenheit vs. Lillys Tirzepatide), Ziltivekimab-Phase-3-Fehlschlag (Juli 2026). Gegenläufig: Q2-2026-Beat, Guidance zweimal angehoben. Lilly hat Novo als GLP-1-Marktführer ex-US überholt. Balance Sheet: Total Debt $19,95 Mrd., Net Debt ~$13 Mrd., FCF FY2025 $8,93 Mrd. Produktkonzentration: Ozempic+Wegovy = 66,7% des Umsatzes.

Quellen: Twelve Data (Kurs/Zeitreihe), CNBC/Bloomberg/STAT News/FierceBiotech (Trial-Coverage), Novo-Nordisk-IR/SEC-Filings, mehrere Sammelklagen-Kanzlei-Meldungen.

---

## Jarvis eigene DCF-Berechnung (Python, Rule 20)

WACC 8,70% (Rf 4,1% + Beta 1,00 × ERP 4,6%).

| Szenario | Wachstumspfad (2026-2030) | Terminal-g | Fair Value | Δ vs. Kurs $45,235 |
|---|---|---|---|---|
| Bear | -6%→-3%→0%→2%→3% | 2,0% | $23,71 | -47,6% |
| Base | 0%→4%→7%→8%→6% | 3,0% | $36,34 | -19,7% |
| Bull | 2%→8%→11%→10%→7% | 3,5% | $44,54 | -1,5% |

Reverse-DCF (konstantes 5J-Wachstum + 3% Terminal-g): **+9,60% p.a.** — liegt zwischen Base-Durchschnitt (5,0%) und Bull-Durchschnitt (7,6%), plausibel, kein Extremwert. Sensitivitätsmatrix (3×3 WACC×Y1-g) zeigt FV-Spanne $32,41-$41,04. ⚠ Diese DCF wurde vor der in Runde 2 gefundenen Bruttomargen-Erosion gerechnet — mit korrigierter Marge läge der faire Wert in allen Szenarien tendenziell niedriger.

---

## Jack (Gemini) — Runde 1

Rating **HOLD**, Agent Score **6/10**, Konfidenz Hoch (90%). K-BASIS Standard=5 (kein Sektor-Override gewählt, explizit begründet: hohe Produktkonzentration + jüngste Verlässlichkeits-Brüche sprechen gegen Override trotz Big-Pharma-Charakter). Eigener Text-DCF (konservativerer Wachstumspfad: -5%→2%→5%→7%→6%, Terminal-g 2,5%): Fair Value **$30,39** (-32,8%). Moat: stark, aber Achillesferse Produktkonzentration (66,7%). Live-Beta-Recherche bestätigte niedrigere Cluster (0,34-0,74), behielt aber konservativ Aegis-Referenzwert 1,00 bei.

## Jack (Gemini) — Runde 2

Nach Einpreisung der Bruttomargen-Erosion (FY2025 81,0%, Q2-2026-adjusted 78,2%, von Conan verifiziert): Rating **SELL**, Score **3/10**, Konfidenz Hoch. Wertet den Margen-Fund als "Game-Changer" — kombiniert mit Wachstumsverlangsamung und inkonsistenter Kapitalrückführung (starke Buyback-Drosselung 2025) überwiegen für Jack die Risiken klar. Empfiehlt Positionsreduktion/-schließung (rein hypothetisch, da NVO kein Depot-Wert ist).

---

## Conan (ChatGPT) — Runde 1

Sektor-Override-Check: **NONE_APPLICABLE** für klassischen Scout (kein SaaS/Pre-Revenue/Deep-Tech/Biotech) — explizit als methodisch ehrlicher Befund markiert, nicht erzwungen. Lief stattdessen als Scout-Sonderfall "**Mature Moat Decay / Mispricing**". Trichter-Logik: NVO ist eindeutig Stufe 3-4 (nicht Stufe 1), bestätigt die Nicht-Passung zur klassischen Scout-Methodik. Kernthese: "NVO ist nicht billig, weil der Markt vergessen hat, dass Novo großartig ist; NVO ist billig, weil der Markt bezweifelt, dass Novos historischer GLP-1-Moat in gleicher Qualität fortbesteht." Fand eigenständig den Capital Markets Day (21.09.2026) als nächsten Katalysator. Multiple-Rahmen: Bear 9-11x/Base 12-15x/Bull 18-22x. Urteil: **WATCHLIST/kein Scout-Buy** bei $45, interessanter unter $35-38.

## Conan (ChatGPT) — Runde 2

Verifizierte und korrigierte mehrere Fact-Pack-Werte per Live-Suche: 2024-Umsatz DKK 290.403 Mio. (nicht 291.570), initiale 2026-Guidance war -5%/-13% (nicht -4%/-12%), 2025-Dividende DKK 11,70 (weiter wachsend), 2025-Buyback nur DKK 1,388 Mrd. (starke Drosselung bereits 2025, nicht erst 2026), **Bruttomargen-Erosion bestätigt und quantifiziert** (FY2025 81,0%, Q2-2026-adjusted 78,2%), Lilly-Bruttomarge Q2 2026 85,8%/86,3% non-GAAP, Zenagamtide-AMAZE-Phase-3 bereits initiiert, Q3-2026-Termin 04.11.2026 bestätigt. Trotz des Margen-Fundes: Urteil bleibt **WATCHLIST_PLUS** — leicht konstruktiver als Runde 1 wegen der verifizierten Guidance-Beat-and-Raise-Sequenz. Aktualisierter Multiple-Rahmen: Bear 9-11x/Base 12-16x/Bull-Recovery 18-24x/Exceptional-Remoat 24-28x. Zentrale Einordnung: "Der historische 10J-KGV-Schnitt (25-26x) ist jetzt ein verdientes Ziel-Multiple, kein automatischer Fair-Value-Anker mehr — NVO darf es wieder erreichen, muss es aber neu beweisen."

---

## Cross-Check-Synthese (Jarvis/Aegis)

**Die zentrale Divergenz:** Jack und Conan erhielten in Runde 2 identische Zusatzdaten (insbesondere den Bruttomargen-Erosions-Fund) und reagierten entgegengesetzt — Jack stufte scharf ab (HOLD→SELL), Conan blieb bei seiner Einschätzung mit leichter Aufwärtstendenz (WATCHLIST→WATCHLIST_PLUS). Dies ist keine Methodik-Störung, sondern eine echte, aussagekräftige Meinungsverschiedenheit zwischen zwei unterschiedlichen, in sich konsistenten Bewertungsphilosophien: Jacks TMR-Methodik reagiert hart und unmittelbar auf eine harte Finanzkennzahlen-Verschlechterung (SCHRITT-4-Pflicht-Logik), während Conans Scout-Perspektive den Gesamttrend (verifizierte Guidance-Erholung, fortgesetzte Kapitalrückführung, unmittelbar bevorstehender Katalysator) stärker gewichtet.

**Aegis' eigene Einordnung:** Die Bruttomargen-Erosion ist real und ernst zu nehmen, aber laut Unternehmensangabe ein Mix aus strukturellen (niedrigere realisierte Preise) und einmaligen (Kapazitäts-Right-Sizing-Kosten, FX) Faktoren — eine vollständige Neubewertung sollte den Capital Markets Day am 21.09.2026 abwarten, der laut Conans eigener Checkliste genau diese Bruttomargen-Brücke liefern muss. Jacks scharfe Reaktion ist ein legitimes, ernstzunehmendes Warnsignal, das nicht ignoriert werden sollte — aber eine endgültige Festlegung vor dem CMD wäre verfrüht.

**Konvergenz trotz Rating-Divergenz:** Beide KIs beschreiben den Moat unabhängig fast wortgleich als "von Dominanz-Moat zu umkämpftem/erodierendem Qualitäts-Moat" gewandelt. Beide nennen unabhängig den Capital Markets Day als Schlüssel-Trigger. Beide nennen unabhängig eine ähnliche Einstiegszone ($35-38) als attraktiver als der aktuelle Kurs. Selbst der Aegis-DCF-Bull-Case liegt bereits leicht unter dem aktuellen Kurs — keine der drei unabhängigen Perspektiven sieht am aktuellen Kurs $45,24 eine klare Kaufgelegenheit.

**Finales Rating:** BEOBACHTEN (Aegis-Synthese, unter Berücksichtigung der Divergenz). Kein Kauf vor dem 21.09.2026. Bevorzugte Einstiegszone $35-38 (von beiden KIs unabhängig genannt). Vorsicht über $48-50 ohne neue positive Daten. Nächster verbindlicher Prüfpunkt: Capital Markets Day 21.09.2026, danach CagriSema-FDA-Entscheidung (erwartet Ende 2026) und Q3-2026-Zahlen (04.11.2026).

---

## PDF

Vollformat-Report: `reports/NVO-agent-deepdive-2026-09-08.pdf` (9 Seiten nach mehreren Nachträgen, "Agent Deep Dive Report"-Format). Erster Full Deep Dive mit dem am 2026-09-08 erweiterten Rigor-Standard (siehe Agent-Playbook.md Punkte 22-29). Besonderheit dieses Reports: erstmals wird eine echte, unaufgelöste Cross-Check-Divergenz zwischen Jack und Conan als eigenständiger, prominent platzierter Befund behandelt (Seite 2) statt zu einem künstlichen Konsens geglättet.

## Nachtrag 1 (2026-09-08): Kurs+KGV-Verlaufs-Chart statt Jahres-Tabelle

Auf Brians Vorbild (onvista-YouTube-Format: Kurs-Panel + KGV-Verlauf-Panel + Mittelwert-Linie) wurde die ursprüngliche reine KGV-Jahres-Tabelle durch eine echte Grafik ersetzt (neu Agent-Playbook.md Punkt 22, präzisiert). Datenquelle: Twelve-Data-Kurshistorie + per WebSearch recherchierte Jahres-/Quartals-KGV-Werte (2021-2023 Jahresdurchschnitt, 2024-2026 Quartalswerte — kein täglicher NTM-KGV-Feed verfügbar, Twelve-Data-Statistics-Endpunkte gesperrt). PEG-Ratio bewusst nicht dargestellt (bei 2026er-Guidance nahe Null/negativ nicht aussagekräftig).

## Nachtrag 2 (2026-09-08): Seiten zusammengelegt (Kursverlauf-Redundanz)

Brian wies darauf hin, dass die neue KGV-Chart-Seite und die bestehende technische Kursverlauf-Seite (Candlestick+EMA+RSI+MACD) beide einen Kursverlauf zeigten. Zusammengelegt auf eine gemeinsame Seite (KGV-Chart auf einpaneliges Format ohne redundante Preislinie verschlankt) — Report dadurch kurzzeitig auf 8 Seiten reduziert.

## Nachtrag 3 (2026-09-08): Vollständige DNA-Check-Tabelle nachgeholt

Brian stellte fest, dass der DNA-Check im Report komplett fehlte (nur Fließtext-Score-Zusammenfassung, keine Tabelle) und forderte zusätzlich, dass DNA-Check-Tabellen künftig ALLE K- und E-Kriterien zeigen, nicht nur die 5 K-Kriterien (neu Agent-Playbook.md Punkt 29). Ursache: Jack lieferte die NVO-Kennzahlen in beiden Runden nur als Fließtext statt im eigenen Tabellenformat — unbemerkt beim Report-Bau übernommen.

Nachgeholt per gezieltem Gemini-Follow-up (vollständige K+E-DNA-Check-Tabelle angefordert). Die Antwort enthielt selbst zwei Qualitätsprobleme, die vor Übernahme gegengeprüft und korrigiert wurden:
- **Op.-Margin-Widerspruch:** Jacks Nachtrag nannte sowohl 37,23% (Fact-Pack-Altwert) als auch 42,24% (neue Live-Suche) im selben Beitrag. Per eigener WebSearch verifiziert: **41,3%** (mehrere Quellen, u.a. Investing.com FY2025-Review) — beide vorherigen Werte waren falsch/veraltet.
- **Capex/Umsatz aufgebläht:** Jacks Wert (29,55%, $13,8 Mrd.) vermischte organisches PP&E-Capex mit den Akquisitionskosten für Akero Therapeutics (Dez. 2025). Korrigiert auf reines PP&E-Capex: DKK 60,1 Mrd. / DKK 309,1 Mrd. Umsatz = **19,4%** — weiterhin deutlich über der 5%-Schwelle, aber ohne die M&A-Verzerrung.

**Ergebnis der vollständigen Tabelle:** DNA-Urteil K 2-3/4 (ROIC✅, FCF-Marge❌ knapp bei 19,1%, Op.-Leverage⚠ fraglich, EPS-CAGR✅), E 4/6 (Bruttomarge✅, Op.-Margin✅, Revenue-CAGR✅, Net-Debt/EBITDA✅, Capex/Umsatz❌, CCC❌ 264 Tage). Ein echtes Grenzfall-Bild, kein sauberer Pass oder Fail — konsistent mit und erklärend für die Jack/Conan-Divergenz aus Runde 2. Capex-Verfehlung wird als investitionsgetrieben (Kapazitätsausbau, ⚡ CAPEX-AUSNAHME-Logik) eingeordnet, nicht als reine Ineffizienz. CCC-Verfehlung wird als für globale Pharma-Distribution strukturell branchentypisch eingeordnet (30-Tage-Schwelle ist für asset-leichte Geschäftsmodelle kalibriert), aber transparent als hartes ❌ ausgewiesen statt stillschweigend wegdiskutiert.

Report jetzt 9 Seiten (neue Seite 3: vollständiger DNA-Check). Finales Rating bleibt **BEOBACHTEN** — die vollständige Tabelle bestätigt eher die Nuance der bestehenden Divergenz als dass sie eindeutig eine Seite (SELL oder HOLD) bestätigt.
