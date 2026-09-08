# Ligand Pharmaceuticals (LGND) — Full Deep Dive, 3-fach TMR-Cross-Check — 2026-09-08

**Auslöser:** Brians Bitte "führe einen full deep dive zu Ligand Pharma für mich". LGND war zuvor am 2026-09-08 als "Profi"-Watchlist-Eintrag ohne vollen 3-fach-Cross-Check aufgenommen worden (nur Jarvis-Solo-Recherche, siehe watchlist.md). Dieser Deep Dive holt den vollen Cross-Check nach.

**Ergebnis vorweg:** Alle drei unabhängigen Analysen (Jack/TMR, Conan/Scout, Aegis/DCF) kommen einstimmig zu einem ablehnenden Urteil (SCHROTT/DURCHGEFALLEN/NICHT KAUFEN) — der Kurs von $281,25 preist mehr Wachstum ein, als selbst der methodisch zulässige Bull Case hergibt.

---

## Jarvis Fact-Pack (Ausgangsbasis für Jack/Conan)

**Live-Kurs:** $281,245 (08.09.2026, -1,52%), 52W-Range $161,82–$326,63 [Twelve Data]

**Geschäftsmodell:** Biopharma-Royalty-Aggregator (analog Royalty Pharma/RPRX, kleiner) — erwirbt/finanziert Lizenz-, Meilenstein- und Royalty-Ansprüche an Medikamenten Dritter, kein eigener F&E-/Vertriebsapparat, strukturell sehr hohe Marge.

**XOMA-Royalty-Akquisition (2026):** Verdoppelt Royalty-Portfolio auf 200+ Assets, Closing 25.06.2026. Finanziert über Convertible Senior Notes, finaler Stand: $700 Mio. (Basis $625 Mio. + voll ausgeübte Über-Zuteilungsoption $75 Mio., Netto-Erlös ca. $678,2 Mio.) — frühere Presseberichte mit $550 Mio./$82,5 Mio. waren Zwischenstände desselben, sich entwickelnden Deals, kein Widerspruch.

**Bilanz-Snapshot-Mismatch (Datenintegritäts-Kernpunkt):** Cash $733,5 Mio. ist PRE-XOMA (31.12.2025 10-K), Total Debt ~$1.160 Mio. ist POST-XOMA (nach Notes-Closing Juni 2026) — vollständige Post-Merger-Quartalszahlen (Q3 2026) erst November 2026 erwartet. Real FCF ($142,1 Mio.) ebenfalls PRE-XOMA. Netto-Effekt: kombiniert alten (niedrigeren) Cashflow mit neuer (höherer) Schuldenlast → tendenziell konservativer, nicht optimistischer Bias in der DCF.

**Weitere Punkte:** CEO Todd Davis (Transformation zum Royalty-Aggregator). Q1-2026-Earnings-Miss mit Kursdruck. Short Interest ~14,72% des Free Float (ungewöhnlich hoch). Beta-Diskrepanz zwischen Quellen (Motley Fool 1,06 / TradingView 0,83 / Jacks Live-Abfrage 0,94) — Aegis nutzte 0,95 als Mittel.

Quellen: Twelve Data (Kurs/Zeitreihe), SEC 10-K FY2025, Unternehmens-IR/Pressemeldungen zur XOMA-Akquisition/Notes-Finanzierung, mehrere Finanzmedien (Q1-Earnings-Coverage, Short-Interest-Daten), Yahoo Finance/Motley Fool/TradingView (Beta).

---

## Jarvis eigene DCF-Berechnung (Python, Rule 20)

WACC 9,15% (Rf US10Y + Beta 0,95 × ERP + Damodaran-CRP).

| Szenario | Fair Value | Δ vs. Kurs $281,245 |
|---|---|---|
| Bear | $92,29 | -67,2% |
| Base | $222,24 | -21,0% |
| Bull | $266,96 | -5,1% (selbst Bull unter Kurs) |

g gecappt bei 20% (Deckel erreicht). **Reverse-DCF impliziertes Wachstum: 25,7% p.a.** — liegt über dem eigenen Bull-Case-Deckel von 20%. Downside-Boden (begrenzt belastbar): $57,54.

⚠ Diese DCF trägt den oben beschriebenen Snapshot-Mismatch-Bias (PRE-XOMA-Cashflow-Basis + POST-XOMA-Schuldenlast) — tendenziell konservativ, nicht großzügig. Selbst mit diesem konservativen Bias liegt der Kurs oberhalb aller drei Szenarien.

---

## Jack (Gemini) — vollständige Antwort (Kernpunkte)

Rating **SCHROTT**, Agent Score 2/10 (Anker 1-2), Konfidenz 🟢 HOCH (90%).

DNA-Check (K-BASIS 5, Royalty-Aggregator-angepasst — Jack erhöhte Net Debt/EBITDA und Bruttomarge eigenständig von E zu K, da für dieses Geschäftsmodell zentraler): ROIC ~10,5% (Fail, Schwelle >20%), FCF-Marge ~98,3% (Pass), EPS-CAGR(5J) -15,2% (Fail), Net Debt/EBITDA ~2,59x (Fail, Schwelle <2,0x), Bruttomarge ~98,7% (Pass). **2/5 K-Kriterien erfüllt → Abbruch-Logik ausgelöst** (K ≤ K-BASIS-2).

Moat trotz Abbruch bewertet: SOLIDE, Trend STRENGTHENING (XOMA-Verdopplung verbessert Diversifikation). Going-Concern-Precheck: unauffällig (PwC-Prüfbericht, kein Vermerk). SBC-Intensity ~19,7% des Umsatzes (über 15%-Infection-Schwelle) → Verwässerungs-Warnung. Beta-Live-Abruf: ~0,94 (Yahoo Finance), nahe an Aegis' Referenzwert.

(Vollständige Rohantwort im Session-Log — Kernaussagen oben und in der PDF-Cross-Check-Tabelle vollständig erfasst.)

---

## Conan (ChatGPT) — vollständige Antwort (Kernpunkte)

Rating **DURCHGEFALLEN** (explizit als Mandatsurteil markiert, kein Qualitätsurteil über das Geschäftsmodell), Scout Score 4,0/10 (Anker 3-5), Konfidenz MEDIUM.

Methodik-Passung: Conan stellte selbst fest, dass LGND in keinen der vier Sektor-Overrides sauber passt (kein SaaS/Pre-Revenue/Deep-Tech/Biotech im Scout-Sinn) — wählte "NONE_APPLICABLE" statt sich eine Kategorie zu erzwingen. Trichter-Stufe: bereits 2 (etablierter Profi), nicht Stufe 1.

Moat-in-Formation 2/4 (🟠 SCHWACH) — Skalierungslogik stark (1/1), aber Wettbewerbsfenster schwach (0/1, Royalty-Deals sind kompetitiv auktioniert). Führungs-Score 3/5. Outcome-Wahrscheinlichkeiten: Totalverlust 2% / Enttäuschung 63% / Marktrendite 32% / Multibagger 3% / Tenbagger+ 0% → **EV-Multiple 1,07x → 🔴 RED**. Downside-Summe 65% (über Base-Rate-Floor 40-50%). Fraud-Check CLEAN, aber Supply-Overhang-Flag (Convertible Notes) und Klumpenrisiko-Flag (Produktkonzentration) aktiv.

(Vollständige Rohantwort mit allen Berechnungen im Session-Log — Kernaussagen oben und in der PDF-Cross-Check-Tabelle vollständig erfasst.)

---

## Cross-Check-Synthese (Jarvis)

**Konvergenz:** Alle 3 unabhängigen Analysen landen bei einer Ablehnung des aktuellen Kurses, obwohl keine der drei Methoden auf die anderen beiden Bezug nahm (Jack: harte K-Kriterien-Gatekeeper. Conan: Asymmetrie-/Outcome-Wahrscheinlichkeits-Modell. Aegis: eigenständige Python-DCF + Reverse-DCF). Das ist ein deutlich robusteres Signal als eine Einzelanalyse mit gleichem Ergebnis. Zentraler roter Faden: der Markt preist mehr Wachstum ein, als die Methodik für plausibel hält (Reverse-DCF-g 25,7% > Bull-Case-Deckel 20%; EV-Multiple 1,07x knapp über 1x aber RED wegen Downside-Mehrheit).

**Wichtige Einschränkung:** Jacks ROIC-/EPS-CAGR-Werte sind eigene [TRAINING]-Herleitungen der Bridge-Analyse, nicht von Aegis unabhängig primärquellen-verifiziert. Das schwächt die DNA-Check-Abbruchbegründung punktuell, ändert aber das Gesamtbild nicht, da Conan und Aegis über völlig andere Rechenwege zum selben "nicht attraktiv"-Ergebnis kommen.

**Datenintegritäts-Kernpunkt:** Die zentrale Limitierung dieser gesamten Analyse ist der PRE-XOMA/POST-XOMA-Snapshot-Mismatch in der Bilanzdatenbasis (siehe Fact-Pack). Dieser Bias wirkt tendenziell konservativ (drückt Fair Value eher nach unten) — das Ablehnungsurteil ist also eher robust als fragil gegenüber dieser Datenlücke. Eine sauberere Neubewertung sollte nach den ersten vollständigen Post-XOMA-Quartalszahlen (Q3 2026, erwartet November 2026) erfolgen.

**Finales Rating:** SCHROTT/DURCHGEFALLEN/NICHT KAUFEN (einstimmig). Keine Kauf- oder Sparplan-Empfehlung. Watchlist-Status bleibt "Profi" (Geschäftsmodell ordentlich), CRV-Ampel wird von der vorläufigen Einschätzung auf 🟠 Vorsicht/Teuer aktualisiert. Nächster Prüfpunkt: Q3-2026-Zahlen (erwartet November 2026) — dann DNA-Check und DCF mit sauberer, nicht-gemischter Datenbasis wiederholen.

---

## PDF

Vollformat-Report: `reports/LGND-agent-deepdive-2026-09-08.pdf` (6 Seiten, "Agent Deep Dive Report"-Format, gleiches Design-System wie CLBT/ATEN). Bewusst kürzer als die CLBT/ATEN-Reports (11 Seiten) — dort ging es um Depot-Positionen mit KAUFEN/BEOBACHTEN-Ausgang und entsprechend viel positivem Erzählstoff (Management-Historie, Burggraben-Origin-Story, Kapitalrückführung). Bei einem einstimmigen Ablehnungsurteil wie hier wäre eine künstliche Streckung auf 11 Seiten reine Füllung ohne Erkenntnisgewinn — der Report fokussiert stattdessen auf die drei konvergenten Analyse-Ergebnisse, den DCF-Rechenweg und den Datenintegritäts-Kernpunkt.
