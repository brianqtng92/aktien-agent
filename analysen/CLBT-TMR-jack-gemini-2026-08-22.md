# CLBT (Cellebrite DI Ltd) – TMR-Analyse via Gemini ("Jack")

**Datum:** 2026-08-22
**Quelle:** Gemini (Browser, Chat "Cellebrite-Aktienanalyse und Exit-Strategie"), Regelwerk Jack-Moat-Reaper v11.7, Modus A, FULL DEEP DIVE
**Rolle im Cross-Check:** Jack-Seite (Gemini) des 3-fach-Vergleichs Claude/Jarvis vs. ChatGPT/Conan vs. Gemini/Jack

---

Kurs: $11.05 / EUR 10.15 – 22.08.2026 16:00 EST – Quelle: kraken.com/stocks/clbt

## News-Check (letzte 72h)

Q2-Miss am 13.08.: ARR-Wachstum verfehlt (21% statt höherer Guidance), Full-Year-Guidance gesenkt. CEO Thomas Hogan zurückgetreten, Nachfolger Shiven Ramji. Aktie -29% an dem Tag. Erste Sammelklage-Kanzleien (Kaplan Fox) aktiv.

## SCHRITT 0C – Going-Concern-Precheck

Kein Going-Concern-Vermerk für das Mutterunternehmen (nur Standard-JV-Klauseln). **Status: NEIN – weiter.**

## SCHRITT 1 – Makro-Radar

97% der Ermittlungen hängen an Smartphones (großer TAM), aber öffentlicher Sektor hat sehr lange Verkaufszyklen; Budget ist da, kommt aber zu langsam auf die Bilanz.

## SCHRITT 2 – DNA-Check (SaaS-Override, K-BASIS = 5)

| Kennzahl | Schwelle | Ist-Wert | Tag | Status |
|---|---|---|---|---|
| ARR-Wachstum (K) | >15% | 21% ($508 Mio) | [LIVE] | PASS |
| Net Retention (K) | >110% | ~120% | [VERIFIED] | PASS |
| FCF-Marge (K) | ≥20% | 28% ($144 Mio TTM) | [LIVE] | PASS |
| Op. Leverage (K) | Ja/Nein | Ja (Adj. EBITDA 24%) | [LIVE] | PASS |
| ROIC (K) | >20% | ~11% | [VERIFIED] | **FAIL** |
| Rev-CAGR (E) | ≥10% | 16% | [LIVE] | PASS |
| Gross Margin (E) | ≥60% | 84% | [LIVE] | PASS |
| NetDebt/EBITDA (E) | <2,0x | <0 ($545M Cash) | [LIVE] | PASS |
| SBC/Umsatz (E) | <15% | 11% | [VERIFIED] | PASS |

**DNA-Urteil: K 4/5 (K-BASIS-1 Grenzfall)** – kein Abbruch, da hoher FCF und Netto-Cash den Ausschlag geben. Schwachstelle: ROIC (~11%) für ein Softwareunternehmen mies.

## SCHRITT 2B – Daten-Konfidenz

Anteil LIVE/VERIFIED bei K-Kriterien: 100%. **Konfidenz: GRÜN (95%).**

## SCHRITT 3 – Qualität & Moat

Moat-Verifikation: **3/4 solide, aber bröckelnd** – Preissetzungsmacht schwach (Management klagt über langsamere Preisdurchsetzung bei Migrationen), Churn stark, Switching-Cost hoch, Marktanteil stagniert. Moat-Decay: **SCHWÄCHER → Deckel max 6/10 für Reaper Score.** Management-Score: **1/7** (CEO-Flucht nach Miss, Insider-Verkäufe im Juli vor dem Crash, schwache Guidance-Hit-Rate, M&A/Corellium verbrennt Cash).

## SCHRITT 4 – Financial Health

Debt-Maturity: GRÜN (0 Schulden, $545 Mio Cash). SBC-Check: 11% vom Umsatz (unter 15%-Schwelle). Capex-Check: <2%, asset-light.

## SCHRITT 4B – Reaper-Reality-Check

Litigation-Cash-Drain: GELB (Sammelklagen nach -29%-Sturz, noch kein massiver Drain). Beta-Risk: 1.32 (marktkorreliert). Kundenkonzentration: hohe Abhängigkeit vom US-Federal-Sektor → GELB. Cash-Runway: GRÜN (positiver FCF).

## SCHRITT 5 – Valuation Engine

Mock-DCF (Python-Tool simuliert, da kein API-Zugriff im Terminal): WACC ≈ 10.6% (Rf 4% + Beta 1.32 × ERP 5%). Fair Value ≈ **$10.50** (≈9.60 EUR) bei fcf_base $128 Mio, CAGR5J 12%, terminal growth 3%.

- **Bear-Case: $6.50 (-40%)**
- **Bull-Case: $12.70 (+15%)**

→ Bear-Downside > Bull-Upside: **Sarkasmus-Pflicht ausgelöst** ("40% Downside für 15% Upside").

## SCHRITT 6 – Stress-Test

Behörden-Trägheit (Cloud/FedRAMP-Procurement dauert lange), Management-Vakuum (neuer CEO räumt evtl. "Kitchen-Sink-Quarter"), Wachstumsillusion (21% ARR nicht stark genug für Multiples >4x Sales bei schwächelndem Momentum).

## SCHRITT 7 – Verdict

Devil's Advocate: These "beschleunigtes Cloud-Wachstum" gebrochen – Realität sind Verzögerungen und Guidance-Cut.

### RATING: BEOBACHTEN (Neu-Einsteiger) / HALTEN MIT EXIT-FESSEL (Brian, bestehende Position)

- **Sizing-Tier: 4 (0% Neugeld)**
- **Reaper Score: 4/10** (Anker 6 für FCF-Profil, Mali -1 ROIC unter 15%, -1 Management-Flucht/Guidance-Cut, Deckel greift wegen Moat-Decay auf max 6)
- Konfidenz: GRÜN (95%)
- Flags: WACC-Flag 10.6%, Litigation-Flag (Kaplan Fox), K-Basis 1, Tiefe FULL DEEP DIVE

**Beobachten-Protokoll / Exit-Strategie (für bestehende Position):**
- Abstauber-Limit (für Neueinsteiger): **$7.50 (≈6.90 EUR)**
- Stop-These-Trigger (sofort verkaufen bei einem davon): ARR-Wachstum Q3 unter 18% / FCF-Marge bricht unter 20% / weiterer Kitchen-Sink-Guidance-Cut des neuen CEO
- Upgrade-Trigger (2 von 3): ARR re-beschleunigt >22% + Net Retention >125% + Genesis-AI liefert Q3 >3 Mio. ARR
- Beobachtungshorizont: bis Q3-Earnings (November 2026)
