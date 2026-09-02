# JARVIS – TMR QUICK FILTER: ASAHI INTECC CO., LTD. (7747)
**Datum:** 2026-09-02 · **Analyst:** Jarvis (Claude) · **Modus:** MODUS A EINZELANALYSE, QUICK FILTER · **Regelwerk:** jack-moat-reaper-v11.7.md
**Anlass:** Brian bat um eine Analyse von Asahi Intecc, neuer Kandidat, noch nicht in Watchlist/Depot.
**Identity-Gate (neu seit 2026-09-02, siehe architecture.md):** Ticker 7747, ISIN JP3110650003, Tokyo Stock Exchange — gegengeprüft gegen zwei unabhängige Quellen (stockanalysis.com, stockopedia.com), beide bestätigen dieselbe Firma. KEINE Verwechslung mit Asahi Group Holdings (Bier), Asahi Kasei (Chemie) oder AGC/Asahi Glass — alles andere Ticker/ISINs.

---

### SCHRITT 0 — LIVE-CHECK
📍 Kurs: 3.601 JPY · 02.09.2026, 15:30 JST · Quelle: stockanalysis.com [LIVE]
Tagesveränderung: −5,16% — trotz durchweg positiver Nachrichtenlage (siehe unten). Grund nicht eindeutig identifizierbar (Gewinnmitnahme nach +37–48% 1J-Lauf? Reaktion auf Nomura-Hold-Einstufung? Sektorbewegung?) — als offene Frage behandelt, nicht spekulativ erklärt.
52-Wochen-Range: 2.272,50–4.282,00 JPY [LIVE]
News (letzte Wochen): Umsatz +18% (globale Nachfrage + schwacher Yen), Gewinnsprung + Dividendenerhöhung, exklusive Japan-Rechte für Nexsphere-F-Embolisationsmittel gesichert [LIVE, mehrere Quellen]
Beta: N/V direkt — [TRAINING]-Schätzung ~0,8-1,0.

### SCHRITT 0C — GOING-CONCERN-PRECHECK
Kein 10-K (japanischer Emittent). N/V – nicht geprüft, kein Abbruch. Bei ROCE 23,21% und durchweg profitablem Geschäft unplausibel, aber formal ungeprüft.

---

## SCHRITT 2 — 🧬 DNA-CHECK: 7747
Aktive K-BASIS: Standard 5S

| Kennzahl | Typ | Schwelle | Ist-Wert | Quelle | Tag | Status |
|---|---|---|---|---|---|---|
| ROIC (Proxy ROCE) | K | >20% | 23,21% | stockopedia.com | [VERIFIED] | ✅ |
| FCF-Marge (real) | K | ≥20% | N/V — "Free cash flow metrics are listed but not populated" (stockopedia) | — | [N/V] | ❌ |
| Op. Leverage | K | Ja | Ja — Umsatz +21,2% vs. Nettogewinn +151,8% YoY, direkt aus verifizierten Zahlen ableitbar (kein Trainingswissen nötig) | Ableitung aus zwei VERIFIED-Werten | [VERIFIED] | ✅ |
| Piotroski F-Score | K | ≥7 | N/V — keine verlässliche Quelle gefunden | — | [N/V] | ❌ |
| EPS-CAGR (5J) | K | ≥12% | N/V historisch — nur aktuelles Jahr (+157%) und Multi-Jahres-Umsatz-CAGR (18,78%, 2022-2028E, teilweise Prognose) bekannt, kein sauberer historischer 5J-EPS-Wert | — | [N/V] | ❌ |
| Bruttomarge | E | ≥60% | N/V | — | [N/V] | ❌ |
| Op. Margin | E | ≥20% | 29,71% | stockopedia.com | [VERIFIED] | ✅ |
| Revenue-CAGR | E | ≥8–10% | 18,78% (2022–2028E, teils Prognose) | stockopedia.com | [VERIFIED, mit Hinweis: teils Forward] | ✅ |
| Net Debt/EBITDA | E | <2,0x | N/V | — | [N/V] | ❌ |
| Capex/Umsatz | E | ≤5% | N/V | — | [N/V] | ❌ |
| CCC | E | <30T | N/V | — | [N/V] | ❌ |
| Beneish M-Score | OPT | <−1.78 | SKIP | keine 8 Live-Komponenten | [SKIP] | SKIP |

**DNA-URTEIL:** K: 3/5 verifiziert (ROIC, Op.Leverage aus echten Zahlen abgeleitet), **3 K-Kriterien [N/V]** (FCF-Marge, Piotroski, EPS-CAGR 5J historisch).

**⚠ ABBRUCH-LOGIK:** K-Kriterium [N/V] → SOFORT-ABBRUCH (ausnahmslos). Drei echte Lücken hier — anders als bei Orion Oyj konnte ich diesmal keine der drei mit einer eigenen Zusatzrecherche schließen (die Multi-Jahres-Umsatz-CAGR ist kein Ersatz für historische EPS-CAGR, da teilweise Analystenprognose statt reiner Ist-Historie).

---

## Einordnung zum jetzt bestätigten Jack/Conan-Muster

Das ist der **zweite Fall in Folge** (nach Orion Oyj), bei dem Jack sofort auf SCHROTT/1 abbricht, während Conan mit [TRAINING]-Schätzungen bis zu einem vollständigen Rating (hier: BEOBACHTEN/6) durchläuft. Beide folgen dem Regelwerk korrekt — der Unterschied liegt in der Risikotoleranz gegenüber Trainingswissen-Schätzungen für harte K-Kriterien. Das ist kein Zufallsfund mehr, sondern reproduzierbares Verhalten bei jedem Quick Filter ohne vollständige IR-Daten. **Empfehlung an Brian:** entweder akzeptieren, dass Jacks SCHROTT bei Quick-Filter-Kandidaten primär "Datenlücke", nicht "schlechtes Geschäft" bedeutet — oder das als Thema für eine Meta-Retrospektive aufgreifen (analog RKLB-Fall), ob die ABBRUCH-LOGIK für QUICK FILTER etwas Kulanz bei fehlenden, aber plausibel schätzbaren K-Kriterien vertragen könnte.

## MEIN VERDICT

**Formal-regelkonform: ABBRUCH** (3 K-Kriterien [N/V]) → kein vollwertiges Rating.

**Qualitative Einordnung:** Was verifiziert vorliegt, ist stark — ROCE 23%, operative Marge 30%, Umsatz +21%, ein massiver (wahrscheinlich teils FX-getriebener) Gewinnsprung. Nischenführer bei minimalinvasiven Guidewires/Kathetern mit strukturellem Rückenwind. Aber: Bewertung bei KGV 24,9x forward ist nicht günstig, der heutige −5,16%-Tagesverlust trotz guter News ist unerklärt, und die Analysten sind sich uneinig (Nomura Hold 3.500 vs. Citi Buy 5.400 JPY). Kein Grund zur Eile.

RATING: **ABBRUCH – DATENLÜCKE** (kein Werturteil über das Geschäft)
SIZING: Tier 4 (0%)
KONFIDENZ: 🔴 – unzureichend für belastbares Rating
TIEFE: QUICK FILTER · K-BASIS: 5S

**Nächster Schritt:** Annual Report/IR-Daten (asahi-intecc.co.jp) für FCF-Marge, Piotroski-relevante Kennzahlen und historische EPS-Reihe — dann echte Neubewertung.
