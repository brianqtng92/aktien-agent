# CROSS-CHECK-FAZIT: ORION OYJ B (ORNBV)
**Datum:** 2026-09-02 · **Kandidat:** Orion Oyj B, Nasdaq Helsinki, ISIN FI0009014377 · **Status:** Neuer Kandidat (nicht in Watchlist/Depot) · **Tiefe:** TMR Quick Filter

## Ergebnis: ⚠ WIDERSPRUCH — nicht durch Diskussionsrunde aufgelöst (Stand dieser Runde 1)

| | Jarvis (Claude) | Jack (Gemini) | Conan (ChatGPT) |
|---|---|---|---|
| Rating | ABBRUCH – Datenlücke | **SCHROTT** | **BEOBACHTEN** |
| Reaper Score | — (formal kein Score bei Abbruch) | 1/10 | 6/10 |
| Konfidenz | 🔴 unzureichend | 🔴 0% | 🔴 45% |
| Sizing | Tier 4 (0%) | Tier 4 (0%) | Tier 4 aktuell, max. Tier 3 bei Upgrade |
| Abstauber-Limit | — | — | 70,00 € |

**Kernursache des Widerspruchs:** Alle drei KIs bekamen identisches Fact-Pack mit denselben 3 offenen K-Kriterien (FCF-Marge, Piotroski F-Score, historischer 5J-EPS-CAGR). Sie unterscheiden sich NICHT in den Fakten, sondern in der **Interpretation der Tagging-Regeln**:

- **Jack** taggt fehlende Werte konsequent als `[N/V]` → löst die harte ABBRUCH-LOGIK aus ("K-Kriterium [N/V] → Sofort-Abbruch") → SCHROTT.
- **Conan** taggt dieselben fehlenden Werte als `[TRAINING]` (plausible Schätzung aus Trainingswissen) → technisch regelkonform (TRAINING ist für K-Kriterien erlaubt, nur ESTIMATE ist verboten) → kein Abbruch, kommt bis BEOBACHTEN.
- **Jarvis** recherchierte aktiv nach, konnte die EPS-CAGR-Lücke mit echten Daten (2023–2025er EPS-Historie) schließen, fand aber bei einer Suche zu Cashflow/Verschuldung Daten zu einer **namensähnlichen, aber anderen Firma** ("Orion S.A."/"Orion Group Holdings") — verwarf diese bewusst statt sie fälschlich zu übernehmen. Bleibt bei 2 echten Datenlücken (FCF-Marge, Piotroski) und damit formal beim Abbruch, tendenziell näher an Jacks Position als an Conans.

**Das ist kein Zahlenkonflikt (Datenkonflikt-Notbremse trifft nicht zu) — beide KIs hatten dieselben Zahlen.** Es ist ein methodischer Dissens darüber, wie viel Vertrauen in unverifizierte Trainingswissen-Schätzungen für harte K-Kriterien angemessen ist. Das ist grundsätzlicher Natur und könnte auch bei künftigen Analysen mit Datenlücken wieder auftreten — ein Kandidat für eine spätere Meta-Retrospektive, ähnlich dem RKLB-Fall.

## Was verifiziert vorliegt (Konsens, unstrittig)

- ROIC/ROCE 52,18% [VERIFIED]
- Operative Marge 35,99% [VERIFIED]
- Umsatz-CAGR 3J 11,88% [VERIFIED]
- KGV 18,1x / PEG 1,32x [VERIFIED]
- Kurs nahe 52-Wochen-Hoch (80,45€ von 82,80€) [VERIFIED]
- Zwei negative Lizenzpartner-Studien-Fehlschläge (10.08.2026) [VERIFIED]
- **EPS-Historie (von Jarvis nachgetragen):** 1,54€ (2023) → 2,35€ (2024) → 3,56€ (2025), 2J-CAGR ≈52% [TRAINING, 2 unabhängige Quellen]

## Was offen bleibt

FCF-Marge, Piotroski F-Score, Net Debt/EBITDA, Debt-Maturity — keine belastbare, eindeutig Orion-Oyj-zuordenbare Quelle gefunden. **Wichtiger Nebenbefund:** Bei der Suche danach wurde eine Namensverwechslung mit "Orion S.A."/"Orion Group Holdings" entdeckt und verworfen — Anlass für die neue, projektweite ISIN-Gegenprobe-Regel bei jeder Fundamentalrecherche (siehe architecture.md, HANDOVER.md 10.12).

## Offen für Brian

1. TA-Modul (Pure Technical Analyst) steht noch aus — bislang nicht durchgeführt, obwohl laut Regelwerk Pflicht bei jeder Einzelanalyse. Twelve Data liefert für ORNBV keine Kursdaten (Plan-/Abdeckungs-Limitierung), müsste über WebSearch/Chart-Quelle nachgezogen werden.
2. Gezielte IR-Recherche (orionpharma.com Jahresbericht) für die drei offenen K-Kriterien, danach echte Neubewertung mit vollständigerem Fact-Pack.
3. Optional: Diskussionsrunde [3b] mit dem erweiterten Fact-Pack (inkl. EPS-Historie) — könnte Jack vom automatischen Abbruch wegbewegen, da die EPS-Lücke jetzt echt geschlossen ist.

**Vorläufige Gesamteinordnung:** Watchlist-würdig aufgrund der außergewöhnlichen Profitabilität, aber **kein Kauf-Rating vergebbar**, bis die Bilanz-/Cashflow-Lücke mit echten Primärquellen geschlossen ist. Kurs nahe 52-Wochen-Hoch spricht ohnehin gegen einen eiligen Einstieg.
