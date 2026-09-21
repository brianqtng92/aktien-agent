# Scout Full Deep Dive: WALLIX Group SA (ALLIX) — 2026-09-21 — Aegis/JJ/Conan

**Ticker:** ALLIX (Euronext Growth Paris) · **ISIN:** FR0010131409 · **Sektor:** Cybersecurity — Privileged Access Management (PAM), Bastion-Suite · **Sektor-Override:** SAAS-DEFAULT · **Anlass:** Brians direkte Anforderung eines Full Deep Dive · **Pfad:** Scout (Bucket B, Quality in Formation)

---

## SCHRITT 0 — Live-Check

**Kurs:** €22,25-22,40 (21.09.2026, verschiedene Quellen, +1,8-2,5% am Tag) · **52W-Range:** €20,55-30,20 (aktuell nahe unterem Rand)

**⚠ Datenkonflikt gefunden und aufgelöst (Conan, transparent benannt):**
1. **Umsatz-Divergenz:** StockAnalysis/Aggregator zeigen FY2025-Umsatz €45,84 Mio., WALLIX' eigene IR-Veröffentlichung nennt €40,62 Mio. "chiffre d'affaires". Für Bewertung wurde die Marktdaten-Zahl (€45,84 Mio.) verwendet, für operative KPIs (Wachstumsraten, Margen) die Unternehmenszahlen — transparent gekennzeichnet statt einen Wert stillschweigend zu bevorzugen.
2. **Aktienzahl/Market-Cap-Korrektur (Aegis, gegengeprüft):** NextStage AM wandelte im August 2026 Anleihen in 312.499 neue Aktien — Aktienzahl stieg von 6.787.070 auf **7.099.569**. Aggregatoren (z.B. €146,36 Mio. Market Cap) reflektieren teilweise noch die alte, niedrigere Aktienzahl. **Korrigierte Market Cap: 7.099.569 × €22,40 ≈ €159,0 Mio.**

## Geschäftsverlauf

- **FY2025:** Umsatz €45,84 Mio. (Marktdaten-Basis, +16,9% ggü. €39,20 Mio. FY2024), Nettoverlust €875.000, H2-2025-Op.-Marge nahe 10%, **erstmals positiver Gesamtjahres-FCF (€1,04 Mio., ggü. -€4,88 Mio. FY2024)** — echter Wendepunkt.
- **H1 2026:** Umsatz €20,6 Mio. (+14,2%), wiederkehrender Umsatz €16,6 Mio. (**+24,1%, jetzt 81% des Gesamtumsatzes, +7pp YoY**), ARR €33,1 Mio. (Ende Juni 2026), MRR €2,76 Mio. (+19,4% YoY), 183 neue Verträge, Portfolio 4.090 aktive Verträge, Gross-Retention >95%.
- **Kapitalstruktur (Juli/August 2026):** €25 Mio. nicht-verwässernde Finanzierung gesichert (potenziell bis €65 Mio.: €15 Mio. Bankdarlehen + €10 Mio. Anleihe), zur Beschleunigung einer "souveränen europäischen Cybersecurity-Plattform". NextStage-Anleihewandlung reduzierte zusätzlich Finanzschulden um €5 Mio.
- **FY2026-Guidance (bestätigt):** Hypergrowth im wiederkehrenden Geschäft + positives operatives Ergebnis + positiver FCF.
- **Nächster Termin:** 08.10.2026 (H1-2026-Zahlen/weitere Details).

## Compounder-DNA-Check (SaaS-Default)

| Kriterium | Typ | Schwelle | Ist-Wert | Status |
|---|---|---|---|---|
| Umsatz-CAGR (3J) | K | ≥30% | ~13,6% (2021-2025), 14,2-16,9% aktuell | ❌ Verfehlt deutlich |
| Bruttomarge-Trend | K | steigend | ~98,6-99,2% (stockanalysis) bzw. ~62% (JJ, andere Definition) — Divergenz nicht restlos aufgelöst, aber strukturell hoch (Software) | ✅ Erfüllt (Niveau), Trend nicht sauber belegt |
| Rule of 40 | K | ≥30% oder klar verbessernd | **~19,2** (Conan: Wachstum 16,94% + FCF-Marge 2,27%) — **zentraler K-Kritikpunkt** | ❌ Verfehlt deutlich |
| Burn-Multiple | K | <2,0x | Nicht anwendbar — FY2025 FCF-positiv (€1,04 Mio.) | ✅ Erfüllt (bestmöglich: kein Burn) |
| Cash-Runway | K | ≥18 Monate | Cash €12,1 Mio. + €25-65 Mio. neue nicht-verwässernde Finanzierung — sehr stark | ✅ Erfüllt, deutlich |
| Insider-/Gründer-Ownership | E | ≥10% | CEO de Galzain ~9,4%, TDH ~6,4%, Mitgründer Rosset ~3,8% (MarketScreener) — zusammen >19%, einzeln unter 10% | ⚠ Grenzfall je nach Zählweise |
| TAM-Expansionsnachweis | E | Belegt | PAM-Markt CAGR 21-29% je Quelle, Wallix <1% Marktanteil global — Markt ist nicht das Problem | ✅ Erfüllt |
| Net Revenue Retention | E | ≥110% | **Nicht offengelegt** — nur Gross-Retention >95% bekannt, keine echte NRR/Expansion-Kennzahl | ❌ N/V, echte Datenlücke |
| Verwässerung (3J) | E | Beobachten | +4,6% durch NextStage-Wandlung (Aug. 2026), dafür €5 Mio. Schuldenabbau — moderat, mit Gegenwert | ⚠ Beobachten |

**DNA-Urteil: K 3/5 (Rule-of-40 UND Umsatz-CAGR beide verfehlt — echte Wachstumsqualitäts-Lücke, kein reines Datenproblem) · E 2/4 belegt, 1 Grenzfall, 1 echte Lücke (NRR).** Kein "Elite-SaaS"-Profil, aber der FCF-Wendepunkt 2025 ist ein echter, verifizierter Fortschritt.

## Zukunfts-Moat-Check (Conan, 4 Dimensionen)

- **Produkt-/Tech-Moat: 3,5/5** — KuppingerCole "Overall Leader" (5. Jahr in Folge), aber CyberArk/BeyondTrust/Delinea bleiben mächtiger (Gartner-MQ-Leader).
- **Switching Costs: 4/5** — PAM sitzt tief in Admin-Zugängen/Audit/Compliance-Prozessen, Retention >95% bestätigt echte Trägheit.
- **Distribution/Ecosystem: 3/5** — 4.000+ Kunden, 100+ Länder, Partnernetz, aber Vertriebskraft/GSI-Tiefe begrenzt ggü. US-Marktführern.
- **Regulatory/Sovereignty-Moat: 4/5** — NIS2/DORA/CRA-Regulierung und europäische Souveränitäts-Agenda spielen Wallix im französisch-europäischen Public-/Industrial-Kontext real in die Karten.

**Moat-Gesamt: 14,5/20 — solider Nischenmoat, kein dominanter Plattform-Moat.**

## Gründer-/Führungs-Score: 4/5 (beide KIs konvergent)

Jean-Noël de Galzain, Gründer seit 2003, CEO/Chairman seit 2022, führte Wallix 2015 als erste französische Cybersecurity-Firma an die Pariser Börse. Positiv: aktiver Gründer, relevanter Eigenanteil, lange Branchenexpertise, strategisch passende Positionierung (EU-Souveränität/OT/PAM/AI via Malizen-Akquisition + Inria-Partnerschaft). Negativ: seit IPO 2015 lange Phase ohne klare Profitabilität, internationale Skalierung noch nicht bewiesen, Euronext-Growth-typische Liquiditäts-/Governance-Risiken.

## Bewertung (EV/Sales-zu-Wachstum + TAM-Sanity-Check, kein DCF)

Mit korrigierter Market Cap (~€159 Mio.) und EV grob €142-160 Mio. (Kapitalstruktur durch neue Finanzierung im Fluss, keine falsche Präzision vorgetäuscht): **EV/Sales ≈ 3,1-3,4x** auf FY2025-Umsatz, **EV/ARR ≈ 4,3-4,6x**. Bei Gesamtwachstum von nur 14-17% ist das nicht spottbillig, aber für einen europäischen Cybersecurity-SaaS mit 81% wiederkehrendem Umsatz, FCF-Wende und Souveränitäts-Narrativ vertretbar (EV/Sales-zu-Wachstum-Schwelle 1,0-2,0 = fair; hier ~3x bei ~15% Wachstum liegt am oberen Rand von "fair", nicht klar "teuer"). Teuer würde es erst bei >5x Sales ohne begleitendes ARR-Wachstum >25%/FCF-Marge >10%.

**TAM-Sanity-Check:** PAM-Markt wächst mit 21-29% CAGR je Quelle (Marktgröße-Schätzungen streuen stark, Richtung ist aber robust bullish). Wallix hält <1% globalen Marktanteil — der Markt selbst ist kein limitierender Faktor, Execution/Differenzierung ggü. den drei US-Marktführern schon.

**Analysten-Konsens:** Strong Buy, Kursziel €31,50 (+41-42% Upside) — Hinweis: nur 2 Analysten, dünne Coverage, entsprechend wenig belastbar.

## Cross-Check-Ergebnis

- **JJ:** konstruktiv, "überzeugendes Quality-in-Formation-Unternehmen", Sizing-Vorschlag vage ("mittelgroße Position")
- **Conan:** deutlich strenger bei Rule-of-40 (~19,2, klar verfehlt), Rating "B/73", explizit "Starter-Buy/Watchlist-Buy, KEIN Core-Compounder", präzise gestaffeltes Sizing
- **Konvergenz: MODERAT** — beide landen auf einem vorsichtig-konstruktiven Scout-Buy, keine echte Rating-Kollision wie beim Kokusai-Fall (keine formale Diskussionsrunde nötig, da kein Widerspruch auf Rating-Ebene, nur unterschiedliche Präzision/Strenge bei der Begründung). Conans Befund wird als maßgeblicher übernommen (spezifischer, mit mehr Primärquellen-Verifikation).

## MEIN VERDICT (Aegis-Synthese)

**RATING: KAUFEN-KANDIDAT / Watchlist-Aufnahme als Talent (Scout-Pfad), Starter-Position — kein Core-Compounder**

Wallix zeigt einen echten, verifizierten Wendepunkt (erstmals FCF-positiv 2025, 81% wiederkehrender Umsatz mit +24% Wachstum, starke Cash-Position + zusätzliche nicht-verwässernde Finanzierung) und einen soliden, wenn auch nicht dominanten Moat (Switching Costs + EU-Souveränitäts-Rückenwind). Der zentrale Vorbehalt: Gesamtwachstum und Rule-of-40 (~19,2) verfehlen die SaaS-Elite-Schwelle klar, und fehlende NRR-Offenlegung ist eine echte Datenlücke, nicht nur Konservatismus.

**KONFIDENZ: 🟡 MITTEL** (Umsatz-/Aktienzahl-Divergenzen zwischen Quellen selbst gegengeprüft und korrigiert, aber NRR fehlt strukturell, nur 2 Analysten Coverage).

**SIZING-VORSCHLAG (Conans gestaffeltes Framework übernommen):** Starter 0,5-1,0%. Aufstockung auf 1,5-2,0% nach Bestätigung am 08.10.2026 (Margenpfad intakt, FCF positiv/auf positivem Pfad, ARR/MRR-Wachstum weiter ~20%+). Maximum 2,5%, solange Wallix unter €100 Mio. Umsatz, ohne NRR-Disclosure und ohne Rule-of-40-Profil bleibt. Kein Core-Sizing (>3%) vor mind. 2 Jahren positivem FCF + >20% ARR-Wachstum durchgehend.

**Kauf-Zonen:** €20-22 attraktiv für Starter · €22-26 neutral/klein akkumulieren · >€31 nur bei sichtbar beschleunigtem Wachstum/Margen gerechtfertigt.

**NÄCHSTER PRÜFPUNKT:** H1-2026-Zahlen 08.10.2026 — insbesondere Margenpfad, FCF-Fortsetzung, ARR/MRR-Wachstumstempo, ob NRR erstmals offengelegt wird.

**KILL-KRITERIEN:** (a) Rule-of-40 verschlechtert sich weiter statt sich zu verbessern; (b) FCF-Wende erweist sich als Einmaleffekt (Rückfall in negativen FCF); (c) neue Finanzierung wird für überteuerte/schlecht integrierte M&A verwendet statt organisches Wachstum zu stützen; (d) Kundenverlust an CyberArk/Delinea/BeyondtTrust wird dokumentiert.

**Hinweis:** Dies wäre ein plausibler Kandidat für den 2. der noch offenen, weltweiten/regionsunabhängigen Talent-Slots (siehe `depot/master_status.md` Abschnitt 8) — der erste wurde bereits mit Oruka Therapeutics (ORKA) besetzt.

---

## 📊 TA-Nachtrag 2026-09-21 (Brian: "wo bleiben die technische Analyse")

**Quelle:** investing.com (Twelve Data deckt Euronext Growth Paris nicht ab, siehe bekannte Tarif-Limitierung).

| Indikator | Wert | Signal |
|---|---|---|
| RSI(14) | 52,4 | Neutral (weder überkauft noch überverkauft) |
| MACD | 0,050 | Buy |
| MA5 | €22,20 | Buy |
| MA20 | €22,23 | Buy |
| MA50 | €22,05 | Buy |
| MA200 | €22,25 | **Sell** (Kurs praktisch exakt am langfristigen Durchschnitt — echter Wendepunkt, kein klares Signal) |

**Gesamtbild: gemischt.** Kurz-/mittelfristig 12 Buy-/0 Sell-Signale (gleitende Durchschnitte) bzw. 8 Buy-/1 Sell (Gesamtindikatoren) — überwiegend bullisch, aber der 200-Tage-Durchschnitt mahnt beim längerfristigen Bild zur Vorsicht (Kurs liegt praktisch genau auf diesem Niveau, kein klarer Trend in beide Richtungen).

**Einordnung:** Passt gut zur fundamentalen "Starter, keine große Position"-Empfehlung — die Technik bestätigt weder eindeutig einen Einstieg noch eine Warnung. Die Kauf-Zone €20-22 liegt praktisch am aktuellen Kurs (€22,25-22,40) und am 200-Tage-Durchschnitt (€22,25) gleichzeitig — ein echter charttechnischer Entscheidungspunkt, den das anstehende Zahlen-Update am 08.10.2026 wahrscheinlich auflösen wird (in die eine oder andere Richtung).
