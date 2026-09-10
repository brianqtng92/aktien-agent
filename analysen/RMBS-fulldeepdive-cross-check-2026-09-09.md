# Rambus Inc. (RMBS) — Full Deep Dive Cross-Check, 2026-09-09

**Auslöser:** Brian bat um einen vollständigen Full Deep Dive einer bestehenden Depot-Position (finanzen.net zero, 6 Aktien, Ø-Einstand $88,94), als Nachschlag zur Schnellanalyse vom 08.09.2026 (nur Jack+Aegis, Conan-Bridge war da ausgefallen). Bucket A/C (etabliertes, profitables Halbleiter-IP-Lizenzunternehmen seit 1990) → TMR-Pfad. Zweiter echter, nicht-degradierter 3-fach-Cross-Check seit dem OpenAI-Credits-Fix (nach HawkEye 360).

**Ergebnis vorweg:** **BEOBACHTEN/HALTEN**, kein Nachkauf bei aktuellem Kurs (~$87). Beide KIs konvergieren auf dieselbe Kernaussage: operativ ein sehr starkes Unternehmen (hohe Margen, Netto-Cash, Rekordumsatz), aber die Bewertung ist trotz ~50%-Kursrückgangs vom Juni-Hoch nicht günstig genug — ein per DCF hergeleiteter Fair Value liegt bei beiden deutlich unter dem aktuellen Kurs. **Eine echte, unaufgelöste Divergenz beim Piotroski F-Score (Jack: 4/9 Fail, Conan: eigene Berechnung 7/9 Pass)** ist der bemerkenswerteste Einzelfund.

---

## Kurs-Datenintegrität (wichtiger Vorab-Befund)

Eine WebSearch-Anfrage lieferte erneut den bereits einmal falsch identifizierten Wert **$104,69** (siehe Depot-Update-Korrektur vom selben Tag). Beide KIs verifizierten den Kurs unabhängig gegen und kamen auf **$86,89 (Jack, Google Finance)** bzw. **$87,65 (Conan, dediziertes Finance-Tool)** — beide klar im $87-Bereich, nicht bei $104,69. **Conan fand die wahrscheinliche Fehlerursache:** Yahoo Finance zeigt für RMBS einen **Ask-Preis von $104,00** — WebSearch-Zusammenfassungen verwechseln offenbar den Ask-Preis mit dem tatsächlichen letzten Handelskurs. Damit ist der wiederkehrende Fehler erstmals erklärt, nicht nur erneut festgestellt.

---

## Fact-Pack (Jarvis, 09.09.2026)

RMBS (NASDAQ), Rambus Inc. — Halbleiter-IP-Lizenzgeber + Memory-Interconnect-Chips (DDR/HBM), seit 1990. Q2 2026: Umsatz $207,4 Mio. (Rekord, +20% YoY, +15% QoQ, über eigener Guidance), Produktumsatz Rekord $99,2 Mio. (+22% YoY). Non-GAAP-Nettogewinn $84,4 Mio. ($0,77 EPS), GAAP $67,6 Mio. ($0,61 EPS). Q3-Guidance $210-216 Mio. HBM4E-Controller-IP (März 2026), 100+ HBM-Design-Wins, neuer Hyperscaler-Design-Win (Kunde nicht genannt). PHY-IP-Sparte an Cadence verkauft (2023, $110 Mio.), digitale Controller-IP behalten. $100-Mio.-Accelerated-Share-Repurchase seit 05.08.2026. Fortgesetzte Insider-Verkäufe (u.a. Director Kissner, 5.000 Aktien @ $100,92, 10b5-1-Plan), keine Käufe. Frühere Schnellanalyse (08.09.) fand Piotroski 5, Capex/Umsatz 5,88%, widersprüchliche FCF-Marge je Periode.

---

## Jack (Gemini 2.5 Flash) — Kernaussagen

**Kurs:** $86,89 (Google Finance, Kurs-Diskrepanz-Warnung korrekt beachtet).

**DNA-Check:** ROIC 36,35% ✅, FCF-Marge 39,6% TTM ✅ (Q2 nur 23,63%, als Diskrepanz vermerkt), Op.Leverage kein klarer Beleg ❌ [TRAINING], **Piotroski 4,00 (GuruFocus) ❌ klar verfehlt** (schlechter als die 5 aus der Schnellanalyse), EPS-CAGR 44,5% ✅ (methodisch unsauber). E-Kriterien: Bruttomarge 79,7-80% ✅, Op.Margin 35,94% ✅, Revenue-CAGR 22,51% ✅, Net Debt/EBITDA negativ (Netto-Cash) ✅, **Capex/Umsatz 5,88% ❌ verfehlt**, CCC nicht ermittelbar [TRAINING].

**Kein Python-DCF durchgeführt** — explizit begründet: Datengrundlage (EPS-CAGR-Unsauberkeit, FCF-Marge-Diskrepanz je Periode) nicht stabil genug für eine zuverlässige Modellierung ohne tiefere manuelle Bereinigung. Zitiert GuruFocus-DCF als Referenz: **$39,97**.

**Moat:** stark (2.010 Patente, 476 anhängige Anmeldungen, hohe Switching Costs). PHY-IP-Verkauf als ambivalent eingeordnet (Fokussierung vs. TAM-Verengung).

**MEIN VERDICT:** Rating "Neutral bis Leicht Bullisch", Sizing "Klein", Konfidenz "Mittel", Abstauber-Limit $70-75.

---

## Conan (ChatGPT/gpt-5.5) — Kernaussagen

**Kurs:** $87,65 (dediziertes Finance-Tool), inkl. Root-Cause-Fund für den WebSearch-Fehler (Ask-Preis-Verwechslung, siehe oben).

**DNA-Check:** ROIC 30-36% ✅, FCF-Marge H1 31,9%/TTM 39,6% ✅ (aber H1-OCF YoY rückläufig, $144,5 Mio. vs. $171,8 Mio. Vorjahr — explizit quantifiziert). Op.Leverage "Ja auf Mehrjahresbasis, aber nicht sauber in H1 2026" (weicher Pass). **Piotroski: eigene Berechnung ~7/9 ✅ Pass** (GuruFocus lieferte keinen exakten Score laut Conan) — **direkter Widerspruch zu Jacks 4/9 Fail**. EPS-CAGR ✅ (gleiche Qualitätswarnung wie Jack). E-Kriterien: Bruttomarge/Op.Margin/Revenue-CAGR/Net-Debt-EBITDA alle ✅. Capex/Umsatz: H1 5,34% ❌, TTM ~4,4% ✅ (grenzwertig, konsistent mit Jacks Fund). **CCC ❌, Inventory-Aufbau quantifiziert: $44,1 Mio. → $74,8 Mio. seit Jahresende 2025 (+70%).**

**Python-DCF durchgeführt** (FCF-to-Equity, TTM-FCF $299,5 Mio., Beta ~1,87): **Bear $31 / Base $43-44 / Bull $68-69** — bemerkenswert konsistent mit Jacks zitiertem GuruFocus-Wert ($39,97, liegt zwischen Bear und Base).

**Struktur-Risiko (Punkt 35) — konkreter als Jack:** Kundenkonzentration mit harten Zahlen aus dem 10-Q belegt: **Customer A 22-25% des Umsatzes, Customer B 15-16%**, bei Accounts Receivable sogar **Top-2-Kunden 65%** der Forderungen. Südkorea-Umsatz $93,7 Mio. von $207,4 Mio. (45%) — geografische Konzentration. Das ist ein echtes Kernrisiko, nicht nur ein theoretisches.

**Moat-Score 7,5/10, Management-Score 7,0/10, Insider-Score 4,0/10** (10b5-1-Verkäufe nicht automatisch bearish, aber keine Gegenkäufe nach 50%-Kursrückgang ist kein Vertrauenssignal).

**MEIN VERDICT:** Rating "HOLD/WATCH, kein Nachkauf bei $87-88". Sizing 0,5-1,5% Zielgewicht, max. 2%. Nachkauf-Tranchen $68/$62/$55. Exit-Trigger klar benannt (Q3-Umsatz <$210 Mio., Inventory wächst weiter schneller als Produktumsatz, OCF/FCF-Schwäche 2 Quartale). Konfidenz 0,70.

---

## Aegis-Synthese (Jarvis, finales Fazit)

**Konvergenz:** beide KIs kommen unabhängig auf BEOBACHTEN/HALTEN mit identischer Kernlogik — starkes operatives Geschäft, aber Bewertung trotz Kursrückgangs nicht günstig genug. Beide DCF-/Referenzwerte (Jacks GuruFocus-Zitat $39,97, Conans eigenes Bear/Base $31-44) liegen in einer ähnlichen Größenordnung, deutlich unter dem aktuellen Kurs $87 — eine echte methodische Konvergenz, nicht nur eine zufällige Übereinstimmung der Endkategorie.

**Die zentrale Divergenz: Piotroski F-Score 4 (Jack) vs. 7 (Conan).** Das ist kein Rundungsfehler, sondern ein K-Kriterium, das je nach KI zwischen "klar verfehlt" und "erfüllt" kippt. Jack stützte sich auf einen zitierten GuruFocus-Wert, Conan auf eine eigene Berechnung, da GuruFocus laut Conan keinen exakten Score lieferte. **Eigene Einordnung:** da der Piotroski-Score aus 9 binären Einzeltests besteht und beide Werte plausibel aus leicht unterschiedlichen Bilanzstichtagen/Berechnungsmethoden stammen können, ist dies nicht sauber auflösbar ohne eine echte Zeile-für-Zeile-Nachrechnung aus dem 10-Q — für den heutigen Report wird der Widerspruch transparent stehen gelassen (Selbstwiderspruch-Check: dokumentiert, nicht stillschweigend übernommen), mit Tendenz zur vorsichtigeren Jack-Einschätzung (4/9), da Conans Verfahren selbst als "eigene Berechnung ohne exakte GuruFocus-Bestätigung" gekennzeichnet war.

**Eigener Mehrwert (Aegis):** Conans quantifizierte Kundenkonzentration (Customer A 22-25%, Top-2-AR-Konzentration 65%, Südkorea 45% des Umsatzes) ist der wichtigste neue Fund dieser Analyse — deutlich konkreter als die bisherige qualitative "abhängig von wenigen Speicherherstellern"-Einschätzung. Das gehört als Kernrisiko in den Report, nicht als Randnotiz.

**Finales Rating: BEOBACHTEN/HALTEN.** Sizing-Deckel Tier 3 (0,5-2% Zielgewicht bei einem Nachkauf, aktuelle 6-Aktien-Position bleibt unverändert). Abstauber-Zone $68-75 (Überschneidung beider KI-Einschätzungen), gestaffelter Nachkauf nur bei echtem Rückgang in diese Zone, nicht beim aktuellen Kurs. Nächster Prüfpunkt: Q3-2026-Zahlen (02.11.2026) — insbesondere Inventory-Normalisierung und OCF-Trend.

---

## Nachtrag 10.09.2026: SBC-Infection-Check + CFO-Wechsel (nach externem Gemini-Review)

Ein externer Gemini-Review des Reports schlug einen SBC-Infection-Check vor (der bereits als Pflichtcheck in `jack-moat-reaper-v11.7.md` existiert, aber im ursprünglichen Report nicht mit echten Zahlen belegt war) und wies auf einen bisher nicht erfassten CFO-Wechsel hin. Gemini's eigene erste Rechnung war fehlerhaft (falsche TTM-Umsatzbasis, unbelegter SBC-Schätzwert) — Jack und Conan wurden daher unabhängig zur Nachrecherche gebeten.

**Ergebnis, per WebFetch-Gegenprobe an der SEC-Primärquelle verifiziert (Conans Zahlen bestätigt, Jacks Zahlen falsifiziert):**
- SBC-Quote FY2025: 7,67% (SBC $54,3 Mio. / Umsatz $707,6 Mio.), TTM Q2'26: 7,40% (SBC $56,0 Mio. / Umsatz $756,3 Mio.) — beide klar unter der 15%-Schwelle.
- Verwässerung (Diluted Shares Q2'26 vs. Q2'25 YoY): +1,34% — unter der 2%-Schwelle.
- **☢ SBC-INFECTION-Flag: nicht aktiv.**
- CFO-Wechsel: Sumeet Gagneja (SVP & CFO) seit 29.04.2026, Nachfolger von Interim-CFO John Allen (zuvor permanenter CFO Desmond Lynch, Rücktritt 04.02.2026/wirksam 27.02.2026).

**Datenintegritäts-Fund:** Jack (Gemini, mit aktivierter Suche) lieferte bei beiden Punkten falsche, unbelegte Werte — CFO-Wechseldatum "1.4.2026" mit Vorgänger "Rohit Kumar" (frei erfunden, existiert im echten 8-K nicht) sowie FY2025-SBC $76,2 Mio. statt real $54,3 Mio. Conans Zahlen stimmten exakt mit der per WebFetch direkt geprüften SEC-Quelle überein (10-Q/8-K). Kein Grund, Jack künftig grundsätzlich zu misstrauen, aber ein konkreter Beleg dafür, dass Live-Suche alleine keine Primärquellen-Verifikation ersetzt — besonders bei spezifischen Namen/Daten. In `reports/RMBS-agent-deepdive-2026-09-09.html` Seite 8 als Datenintegritäts-Warnstrip dokumentiert.

---

## PDF

`reports/RMBS-agent-deepdive-2026-09-09.pdf` — vollständiger Full Deep Dive nach kanonischem Seitengerüst (10 Seiten), inkl. Kundenkonzentrations-Vertiefung, Piotroski-Divergenz-Box. Am 10.09.2026 vollständig auf NVO-Referenzniveau nachgezogen: DCF-Bear/Base/Bull jetzt auch als Balkenchart (Seite 5), Bruttomargen-Verlauf 2021-TTM als neue Chart (Seite 5, Jack+Conan-recherchiert, Kernbefund: keine Erosion, Stabilisierung ~80% seit 2024), WACC-Sensitivitätsmatrix (Seite 5), Kursverlauf mit DCF-Fair-Value-Zonen + KGV-Verlauf-Chart (Seite 6), Kapitalrückführung nach Seite 8 verschoben. Zusätzlich am 10.09.2026 (nach externem Gemini-Review, siehe Nachtrag unten): SBC-Infection-Check mit echten Zahlen (Flag nicht aktiv) und CFO-Wechsel/M&A-Risiko-Box auf Seite 8 ergänzt.
