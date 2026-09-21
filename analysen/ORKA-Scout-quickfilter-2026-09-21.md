# Scout Quick Filter: Oruka Therapeutics, Inc. (ORKA) — 2026-09-21 — Aegis/JJ/Conan

**Ticker:** ORKA (NASDAQ) · **ISIN:** US6876041087 · **Datum:** 21.09.2026 · **Sektor-Override:** BIOTECH (klinische Phase, kein Umsatz) · **Anlass:** weltweite, regionsunabhängige Talent-Slot-Suche (siehe Agent-Playbook.md "Automatisierte Portfolio-Lücken-Kandidatensuche-Pflicht" Punkt 1b)

---

## Herkunft

JJ (Gemini) fand ORKA im Rahmen einer weltweiten Talent-Kandidatensuche (4 Vorschläge: ORKA, IonQ, D-Wave, AST SpaceMobile). Brian wählte ORKA + D-Wave für den vollen Quick Filter. Conan (ChatGPT) fiel beim ersten Dispatch-Versuch 3x aus (Tool-Fehler, Health-Check über `list_openai_models` war OK — vermutlich transientes Problem), war beim zweiten Durchgang wieder erreichbar.

## Fact-Pack (Stand 21.09.2026)

- Kurs: $95,16 (live, Twelve Data)
- Cash: $1,126 Mrd. (SEC 10-Q, 30.06.2026) + $122,5 Mio. ATM-Erlös Juli 2026 ≈ $1,25 Mrd. pro forma
- Q2 2026: R&D $43,3 Mio. (+80% YoY), Netto-Verlust $41,2 Mio., H1-Netto-Verlust $73,0 Mio.
- Operativer Cash Burn H1 2026: $56,7 Mio. (≈ $9,5 Mio./Monat)
- Pipeline: ORKA-001 (IL-23p19, Phase 2a Psoriasis, EVERLAST-A-Trial) — 16-Wochen-Daten 63,5% PASI-100; ORKA-002 (IL-17A/F, Phase 2, auch Psoriasis-Arthritis/Hidradenitis Suppurativa)
- Analysten-Konsens: Strong Buy, Kursziel $155 (+62,9%)

## ⚠ Datenkonflikt gefunden und aufgelöst (Aegis)

Conans Live-Suche meldete Market Cap **$12,0 Mrd.** — deutlich über der ursprünglich recherchierten $6,31 Mrd. (stockanalysis.com). Aegis prüfte das eigenständig gegen: **66,21 Mio. ausstehende Aktien × $95,16 = $6,30 Mrd.** — bestätigt die ursprüngliche, niedrigere Zahl. Conans Zahl war ein Live-Suche-Fehler (Quelle nicht identifiziert, evtl. Verwechslung mit einer anderen Kennzahl). **Bindend: Market Cap $6,3 Mrd., EV ≈ $5,2 Mrd.** (Market Cap − Cash).

## JJ-Lauf 1 (Fehler, transparent dokumentiert)

Erster Durchlauf hatte `enable_search=False` (Aegis-Fehler — bei einem kurzen, methodik-datei-freien Prompt sollte per HANDOVER.md 10.10 `enable_search=True` gelten). JJ griff dadurch auf veraltete Trainingsdaten zurück (Zeitstempel "2023" bei Cash/CFO/Insider-Ownership) statt echte 2026er-Zahlen zu recherchieren — Ergebnis war methodisch unbrauchbar, wurde verworfen. Nach Korrektur (Lauf 2, `enable_search=True`) lieferte JJ konsistente, live-recherchierte 2026er-Daten.

## DNA-Check (Biotech-Override, K-BASIS=4, E=3)

| Kriterium | Typ | Schwelle | Status |
|---|---|---|---|
| Cash-Runway | K | ≥24 Monate bis nächsten Katalysator | ✅ — bei $9,5 Mio./Monat Burn reicht $1,1-1,25 Mrd. Cash für 100+ Monate, weit über Schwelle |
| Pipeline-Reife | K | Mind. Phase 2 mit Daten | ✅ — ORKA-001 Phase 2a mit positiven 16-Wochen-Daten |
| Trial-Design-Qualität | K | Randomisiert/kontrolliert, klare Endpunkte | ✅ — Standard-Psoriasis-Trial-Design (PASI-100), etablierter Endpunkt |
| Kapitalallokation/Partnering | K | Nicht-verwässernde Finanzierung vorhanden/glaubwürdiger Plan | ⚠ — bisher rein eigenkapitalfinanziert (Secondary + ATM), kein Partnering-Deal, aber bei aktuellem Cash-Runway kein akutes Problem |
| Insider-/Gründer-Ownership | E | ≥10% | ⚠ N/V — CEO Klein hält 1,4% individuell, Gesamt-Insider-% nicht sauber verifiziert |
| Konkurrenz-Pipeline | E | Führend/Mittelfeld/Nachzügler | 🟡 — starke etablierte Konkurrenz (AbbVie/Skyrizi, UCB/Bimzelx), aber ORKA-001/002 zeigen in frühen Daten Differenzierungspotenzial (längere Dosierungsintervalle) |
| Regulatorischer Pfad | E | Klar/Unklar | ✅ — etablierter Pfad für Psoriasis-Indikationen, keine ungewöhnlichen Hürden |

**DNA-Urteil: K 3,5/4 (Grenzfall knapp über K-BASIS-1, Begründung: Partnering-Kriterium nur ⚠ nicht ❌) · E 1,5/3 (Insider-Ownership offen)**

## Zukunfts-Moat-Check

Intangible Assets (Patente/klinische Daten) als Kern-Moat — hoch, da PASI-100-Vorteil ggü. Skyrizi und längere Dosierungsintervalle ggü. Bimzelx echte, potenziell verteidigbare Differenzierung wären, sofern in Phase 3 bestätigt. Wettbewerbs-Fenster: eng (etablierte Konkurrenten mit Milliarden-Umsatz), aber First-Mover bei jährlicher IL-23-Dosierung wäre strukturell, nicht nur zeitlich.

## Gründer-/Management-Score

CEO Dr. Lawrence Klein (seit Feb. 2024), zuvor Führungspositionen bei Novartis/Amgen/Bristol Myers Squibb/Takeda — hohe Branchenerfahrung. Neuer CCO (Todd Edwards, 25+ Jahre Kommerzialisierungserfahrung Immunologie/Dermatologie, seit 24.08.2026) deutet auf aktiven Aufbau der kommerziellen Infrastruktur vor einer möglichen Zulassung hin — positives Signal.

**Einziger Wermutstropfen:** Insider verkauften in den letzten 12 Monaten netto $22 Mio. mehr als sie kauften (CEO Klein plant weitere 75.000-Aktien-Verkäufe). Laut JJ größtenteils steuerbedingte RSU-Sell-to-Cover-Transaktionen (10b5-1-Pläne) — kein eindeutiges Alarmsignal, aber auch kein positives Kaufsignal.

## Bewertung

EV/Sales nicht anwendbar (kein Umsatz). TAM-Sanity-Check: Psoriasis-Markt ~$30 Mrd. und wachsend. Jefferies schätzt $5-10 Mrd. Spitzenumsatzpotenzial für ORKA-001 allein. Bei EV ~$5,2 Mrd. (korrigierter Wert) ist das ambitioniert, aber nicht irrational — deutlich anders als bei der (falschen) $12-Mrd.-Marktkap-Annahme, unter der Conan zunächst zu BEOBACHTEN kam.

## Cross-Check-Ergebnis

- **JJ (nach Korrektur):** tendenziell konstruktiv ("potenzieller Branchenführer mit hohem Risiko/hoher Belohnung"), ursprünglich KAUFEN-KANDIDAT (8/10) im (verworfenen) ersten Lauf
- **Conan:** BEOBACHTEN ("sehr gute Bilanz + starkes Signal, aber viel Erfolg eingepreist") — basierend auf der fehlerhaften $12-Mrd.-Marktkap; mit korrigierter Zahl wäre die eigene Logik konstruktiver ausgefallen
- **Aegis:** BEOBACHTEN-STARK, an der Grenze zu KAUFEN-KANDIDAT

## MEIN VERDICT (Aegis-Synthese)

**RATING: BEOBACHTEN-STARK** (Watchlist-Aufnahme, kein Kauf-Signal)

Begründung: Außergewöhnlich starke Bilanz (praktisch unbegrenzter Cash-Runway bei aktuellem Burn), überzeugende frühe klinische Daten mit echtem Differenzierungspotenzial ggü. etablierten Milliarden-Produkten, erfahrenes Management. Bewertung nach Korrektur des Market-Cap-Fehlers nicht überzogen relativ zum Spitzenumsatzpotenzial. Verbleibendes Risiko ist das übliche Biotech-Binärrisiko (Studienausgang) plus die offene Insider-Ownership-Frage.

**KONFIDENZ: 🟡 MITTEL** (Insider-Ownership-Schwelle nicht sauber verifiziert, DNA-K-Kriterium Partnering nur ⚠)

**NÄCHSTER PRÜFPUNKT:** Woche-28/52-Daten EVERLAST-A (H2 2026), Phase-2b-Daten (2027).

**HINWEIS:** Watchlist-Aufnahme ist keine Kaufempfehlung (siehe Agent-Playbook.md "Proaktive Suche ist keine Kaufpflicht"). Vor einer echten Depot-Positionierung: FULL SCOUT nachholen (inkl. vollständiger Insider-Ownership-Verifikation über SEC-Proxy/Form-4).
