# TA-Testlauf (Investor-Entry-Modus): Mastercard (MA) — 2026-08-22 — zweite Stufe der Pipeline, TMR-Handoff aus MA-TMR-testlauf-2026-08-22.md, nur Claude-Durchlauf (ChatGPT/Gemini-Cross-Check noch nicht angebunden)

---

Okay Brian. TMR sagt "KAUFEN", 8/10, Fair Value bis $688. Schön für dich. Mich interessiert das nicht die Bohne — ich schau mir an, ob der Chart gerade sagt "rein" oder "warte". Reiner Chart-Job, keine Bilanzen, keine Story. Los geht's.

**MODUS-DETECTION: TMR Bear FV + Base FV im Input vorhanden → MODUS 2 (INVESTOR-ENTRY) automatisch aktiv, zusätzlich zu MODUS 1 (Standard-TA), der immer vollständig läuft.**

---

## ANALYSE-HEADER

Ticker: **MA** | Horizont: **INVESTOR (>6 Monate)** | Gewichts-Schema: **INVESTOR aktiv** (F1×1,50 / F2×1,50 / F3×1,25 / F4×0,75 / F5×1,00; W1-Doppelgewicht aktiv; RSI-VETO-Schwelle 85 statt 80)
Kurs-Quelle: **LIVE** (Web-Search, stockanalysis.com + barchart.com, gegenverifiziert) | TMR-Kurs-Abgleich: **OK** — kein Delta. TMR-Kurs $580,63 (21.08.2026) = identischer Schlusskurs wie TA-Kurs. Am 22.08.2026 (Analysetag) ist die Börse geschlossen (Samstag), letzter Handelstag bleibt 21.08.2026. **Kein ⚠️ KURS-DESYNC, kein ⚠️ KURS-DELTA-FLAG.**

---

## 1. TREND & SEKTOR

**MA-Stack (SMA20/50/200):** Kurs $580,63 > SMA20 $568,26 > SMA50 $537,68 > SMA200 $528,42 → **Bullish (+1,00)**
Quelle: [barchart.com](https://www.barchart.com/stocks/quotes/MA/technical-analysis), [stockanalysis.com](https://stockanalysis.com/stocks/ma/statistics/) — beide Quellen liefern konsistente SMA-Werte, kreuzvalidiert.

**EMA-Konfluenz:** [KEINE DATEN] — verfügbare Quellen lieferten widersprüchliche EMA20/50-Werte (unterschiedliche Snapshots derselben Quelle wichen stark voneinander ab, nicht belastbar). Check entfällt, **kein Konfidenz-Malus** (optionales Signal).

**W1-Konfluenz:** Kurs steht bei 96,5% des 52-Wochen-Hochs ($601,77) — klar bullisher Wochentrend, aber mit dem alten Hoch als unmittelbarem Deckel direkt über dem Kurs. → **Bullish nahe Widerstand**
INVESTOR-Doppelgewicht: **+0,10**

**Sektor:** Finanzsektor / Payment Networks. Aktuelle Lage: robuste operative Dynamik im Sektor (Cross-Border-Volumen und Value-Added-Services beschleunigen bei MA wie bei Visa), Aktien nahe 52-Wochen-Hochs nach kräftiger Erholung seit Frühjahrstief, XLF (Finanzsektor-ETF) zuletzt mit +6,15% im 1-Monats-Fenster. → **Stärke: Stark / Richtung: Verbessernd**
Matrix-Score: **+0,50**
Quelle: [The Motley Fool, 12.08.2026](https://www.fool.com/investing/2026/08/12/visa-mastercard-payments-giant-best-buy-now/), [SSGA XLF](https://www.ssga.com/us/en/intermediary/etfs/state-street-financial-select-sector-spdr-etf-xlf)

**Faktor-Rohscore:** 1,00 (MA-Stack) + 0 (EMA) + 0,10 (W1) + 0,50 (Sektor) = **1,60** (Cap: −2,15/+2,25, i.O.)
**Faktor-Score (gewichtet ×1,5 INVESTOR): +2,40**

---

## 2. MOMENTUM

**1M:** $531,98 (22.07.2026) → $580,63 = **+9,15%** [LIVE, stockanalysis.com Kurshistorie]
**3M:** ~$491 (Mitte Mai 2026) → $580,63 ≈ **+18,25%** [Datenpunkt genähert, Quelle: TIKR-Artikel vom 14.05.2026, nicht exakt auf den Tag genau — Abweichung von wenigen Tagen zum echten 3M-Stichtag]
**6M:** ~$518,22 (13.02.2026, dokumentiertes 42-Wochen-Tief) → $580,63 ≈ **+12,04%** [Datenpunkt genähert, ~8 Tage vor dem exakten 6M-Stichtag]
**Benchmark 6M% (S&P 500):** ≈ **+12,4%** grob geschätzt (7.641,16 aktuell vs. ~6.800 Mitte Februar 2026, aus Meilenstein-Berichterstattung abgeleitet, kein exakter Tages-Schlusskurs verifizierbar) — **Datenqualität schwach, aber Differenz zu MA so klein, dass es die Kategorisierung nicht kippt.**

**Rel. Stärke vs. Benchmark (6M):** +12,04% (MA) vs. ≈+12,4% (Benchmark) → Differenz ≈ −0,4 Prozentpunkte → liegt klar innerhalb der −5%/+5%-Neutralzone → **Neutral (0)**

**Momentum-Beschleunigung:** 1M (+9,15%) vs. 3M/3 (+18,25%/3 = +6,08%) → 1M > 3M/3 → **Beschleunigung (+0,50)**

**Faktor-Rohscore:** 0 + 0,50 = **+0,50** (Cap: −1,5/+1,5, i.O.)
**Faktor-Score (gewichtet ×1,5): +0,75**
Kontext: 1M +9,15% / 3M ≈+18,25% / 6M ≈+12,04%

---

## 3. VOLUMEN + INSTITUTIONAL FOOTPRINT

**Vol. vs. 20T-Ø:** Letzter Handelstag (21.08.): 2.200.629 Aktien vs. Ø 20T 2.981.696 = **73,8% des Ø** bei Kursanstieg (+1,18%) → **Warnsignal (0)**
**Volumen-Anomalie:** Kein Vol. >300% Ø ohne Preisbewegung → **0**
**Volumen-Trend:** Unterdurchschnittliches Volumen am Anstiegstag + externe Quelle (stockinvest.us) bestätigt explizit "Volumen fiel trotz steigendem Kurs" → **fallend (−0,50)**

Standard Volumen-Rohscore: 0 + 0 − 0,50 = **−0,50**

**── Institutional Footprint:**
**OBV-Trend:** **[KEINE DATEN]** — keine belastbare, aktuelle OBV-Zahlenreihe für MA über Web-Search auffindbar → **0 + Konfidenz-Malus −1**
**Akkumulations-Muster:**
Große Kerzen ohne News-Trigger (20T): [KEINE DATEN] → 0
Up-Volumen > Down-Volumen in Rücksetzern: [KEINE DATEN] → 0
→ **0/2 positiv, beide [KEINE DATEN]**
**Institutional Score: 0**

**Institutional Footprint Urteil:** 0/3 positiv → formal "Kein Akkumulations-Signal — oder aktive Distribution". **Ehrlicher Zusatz:** Das ist hier kein Beleg für aktive Distribution, sondern schlicht Datenmangel — OBV und Kerzen-/Rücksetzer-Muster waren über frei zugängliche Quellen nicht verifizierbar. Nicht verwechseln mit einem echten Negativ-Befund.

**DISTRIBUTION-VETO-Check:** OBV [KEINE DATEN] → Bedingung "OBV fallend" nicht erfüllbar → **kein Trigger.**

**FAKTOR 3 GESAMT-ROHSCORE:** −0,50 + 0 = **−0,50** (Cap: −1,25/+1,75, i.O.)
**Faktor-Score gesamt (gewichtet ×1,25): −0,625**

---

## 4. OSZILLATOREN

**RSI(14):** **65,78** → Kategorie 60–70 → **überkauft-Zone (−0,50)** [LIVE, barchart.com]
**MACD:** ⚠️ Uneinheitliche Quellenlage — eine Quelle (investing.com) zeigt MACD positiv/über Signallinie ("Buy"), eine andere (stockinvest.us) zeigt ein Sell-Signal auf 3-Monats-Basis. Zusammen mit dem starken ADX-Trend (ADX 33,46, +DI 30,42 klar über −DI 13,06 → etablierter Aufwärtstrend) werte ich das Tages-MACD vorsichtig als **Bullish (+1,00)**, aber mit explizitem Konflikt-Hinweis.
**Bei INVESTOR-Horizont: Tages-MACD ist ohnehin kurzfristiges Rauschen — die Quellen-Uneinigkeit bestätigt genau das: auf Tagesbasis kein sauberes Signal, für die >6-Monats-These irrelevant.**
**Divergenz:** Keine belastbare Bullische/Bärische RSI- oder MACD-Divergenz in den Quellen erkennbar → **Keine (0)**

**Faktor-Rohscore:** (−0,50 + 1,00)/2 + 0 = **+0,25** (Cap: −1,5/+1,5, i.O.)
**Faktor-Score (gewichtet ×0,75 INVESTOR): +0,1875**

---

## 5. STRUKTUR

**Bollinger:** **[KEINE DATEN]** — trotz mehrfacher Versuche über verschiedene Quellen keine belastbaren Bandwerte gefunden. Kurs liegt zwar 2,2% über dem SMA20 (Hinweis auf Nähe zum oberen Band), aber ohne echte Bandwerte will ich hier keine Zahl erfinden → **0**
**52W-Kontext:** Kurs $580,63 = 96,5% des 52W-Hochs ($601,77) → >90% → **Relative Stärke (+0,25)**
**Support/Widerstand R/R:** Nächster Support $575,02 (−0,97%) / nächster Widerstand $584,26 (+0,63%) [Pivot-Punkte, barchart.com] — Kurs liegt näher am Widerstand als am Support, beide <3% entfernt → **Schlechtes R/R (−0,50)**. Zusatzhinweis: übergeordneter Widerstand ist das 52W-Hoch bei $601,77.
**Trendkanal:** **[KEINE DATEN]** — kein User-Input geliefert (reiner User-Input-Baustein). Check entfällt, **kein Malus**.

**Faktor-Rohscore:** 0 + 0,25 − 0,50 + 0 = **−0,25** (Cap: −1,5/+1,5, i.O.)
**Faktor-Score (gewichtet ×1,0): −0,25**

---

## 6. FORMATION

Formations-Kandidat: **[KEINE DATEN]** (kein User-Input geliefert, reiner User-Input-Baustein) — **Status: Keine — VETO ausgelöst: Nein**

---

────────────────────────────────────────────
## 7. GESAMTSCORE

| Faktor | Rohscore | Gewicht (INVESTOR) | Gewichtet |
|---|---|---|---|
| 1 Trend & Sektor | +1,60 | ×1,50 | **+2,40** |
| 2 Momentum | +0,50 | ×1,50 | **+0,75** |
| 3 Volumen+Footprint | −0,50 | ×1,25 | **−0,625** |
| 4 Oszillatoren | +0,25 | ×0,75 | **+0,1875** |
| 5 Struktur | −0,25 | ×1,00 | **−0,25** |

**GESAMTSCORE: +2,4625 / max. INVESTOR +10,44 (fix)**
**Normierter Vergleichswert: 1,95 / 8,25**

## 8. RATING: **HOLD**

(+0,5 bis +2,9 Schwelle — Score +2,46 liegt sauber in dieser Bandbreite. Kein VETO-Aggregat-Deckel relevant, da Rating nicht STRONG BUY.)
────────────────────────────────────────────

---

## 9. ⚡ JACKS VETO

Alle Bullish-Warnungen (Überdehnung, Death Cross, Bärische Divergenz, Volumen-Climax, OBV-Divergenz, MA-Stack Bearish, Risk-Off, Sektor-Verfall, Kanal-Ausbruch, Formation) setzen als Vorbedingung ein Rating **BUY oder STRONG BUY** voraus. Rating hier ist **HOLD** → keiner dieser Trigger greift, unabhängig vom RSI-Stand.
Alle Bearish-Warnungen setzen Rating **AVOID oder WEAK** voraus — auch das trifft nicht zu.

**→ Kein VETO — Score konsistent.**
Anzahl aktiver Bullish-VETOs: 0 → Aggregat-Deckel: Nein (ohnehin nicht relevant bei HOLD)

---

## 10. RISIKO-MODUL

**ATR(14):** $10,85 → **ATR%: 1,87%** → **Mittel** (Standard-Stops)
**Stop-Loss (Standard):** Support $575,02 − 0,5×ATR ($5,43) = **≈$569,60**
**Stop-Loss (Konservativ):** Support $575,02 − 1,0×ATR ($10,85) = **≈$564,17**
**R/R-Ratio:** Abstand Kurs→Widerstand ($584,26 − $580,63 = $3,63) / Abstand Kurs→Stop ($580,63 − $569,60 = $11,03) = **0,33 → Schlecht** (Kurs klemmt direkt zwischen S1 und R1, extrem enges Fenster). Zusatzhinweis: gegen das übergeordnete 52W-Hoch ($601,77) als Ziel läge das R/R bei ≈1,92 (akzeptabel) — hängt stark davon ab, welchen Widerstand man als relevant ansieht.
**Vola-Alignment:** **[KEINE DATEN]** — ATR-Ø 20T nicht auffindbar → Check übersprungen, Konfidenz-Malus −1.
**Noise-Level:** ATR% 1,87% → weder <1% noch >4% → **Normal**
**Abstauber-Limit-Check:** Kurs $580,63 liegt **16,13% über** dem TMR-Abstauber-Limit ($500) → "Kurs liegt 16,1% über TMR-Abstauber-Limit. Limit-Order bei $500 platzieren."

---

## 11. JACKS FAZIT

Der Chart ist technisch sauber bullish aufgestellt — voller SMA-Stack, starker ADX-Trend, Sektor mit Rückenwind — aber genau deshalb klemmt der Kurs jetzt direkt unter seinem eigenen 52-Wochen-Hoch, und das ist bei INVESTOR-Horizont das entscheidende strukturelle Signal, nicht das Tages-RSI oder das widersprüchliche Tages-MACD (beides kurzfristiges Rauschen, siehe Faktor 4). Die Trend- und Sektor-Story trägt den Score fast alleine (+2,40 von +2,46 Gesamtscore) — Momentum bestätigt leicht, Volumen und Struktur ziehen dagegen, weil institutionelle Fußspuren schlicht nicht sichtbar sind und der Kurs zwischen Pivot-Support und -Widerstand eingeklemmt liegt. Für einen Investor-Einstieg heißt das: technisch kein Alarm, aber auch keine Einladung — du kaufst hier nicht in Stärke hinein, du kaufst in eine Verschnaufpause direkt unter dem alten Hoch.

---

## 12. DATENLAGE

**Fehlende Datenpunkte:** EMA20/50 (widersprüchlich, kein Malus), OBV-Trend (Malus), Akkumulations-Muster 2x (Malus), Bollinger Bands (Malus), ATR-Ø 20T (Malus), Trendkanal (kein Malus, User-Input), Formation (kein Malus, User-Input). Momentum 3M/6M und Benchmark 6M sind Näherungswerte (keine exakten Stichtags-Schlusskurse verfügbar), aber nicht "KEINE DATEN" im engeren Sinn.

**Analyse-Konfidenz: Niedrig (4 Felder unvollständig: OBV-Trend, ATR-Ø 20T, Bollinger Bands, Akkumulations-Muster)**

Ehrlicher Kommentar: Die Kern-Preisstruktur (SMA-Stack, RSI, ATR, Support/Widerstand, 52W-Range) ist solide über mehrere Quellen kreuzvalidiert. Was fehlt, ist die "unter der Motorhaube"-Ebene — Institutional Footprint (OBV, Akkumulationsmuster) und exakte Bollinger-Bandwerte. Frei zugängliche Finanzseiten liefern das für MA schlicht nicht zuverlässig. Konfidenz-Stufe entsprechend ehrlich auf Niedrig gesetzt statt geschönt.

---

## MODUS 2: ══ INVESTOR-ENTRY-MODUS ══════════════════════════

Horizont: **INVESTOR** | TMR-Konfidenz: **🟢 HOCH (89%)**
TMR-Rating: **KAUFEN** | Mapping: TA-Äquivalent laut Rating-Mapping-Tabelle wäre BUY/STRONG BUY-Zielbereich — **tatsächlich liefert die TA aktuell nur HOLD.** Kein hart definierter ⚔️-Konflikttrigger (der greift nur bei TA AVOID/WEAK), aber diese Lücke zwischen TMR-Erwartung und TA-Realität ist der zentrale Punkt dieser Analyse für Brian — siehe Block E.

### BLOCK A — PREISZONE
Kurs: $580,63 / Bear FV: $372 / Base FV: $634 / Bull FV: $688
- Zone 1 (Günstig, <$372): nein
- Zone 2 (Attraktiv, $372–$570,60): nein ($580,63 > $570,60)
- Zone 3 (Fair, $570,60–$697,40): **JA**

**PREISZONE: 3 – FAIR**

### BLOCK B — MARGIN OF SAFETY
MoS% = (Bear FV $372 − Kurs $580,63) / Bear FV $372 × 100 = **−56,08%**
**MoS: 🔴 KEINER** (negativ — Kurs liegt weit über dem Bear-Case-Szenario, keine Sicherheitsmarge gegen das Downside-Szenario vorhanden)

### BLOCK C — ENTRY-AMPEL
Zone 3 + TA HOLD (nicht BUY/STRONG BUY) → kein Abstauber-Override möglich, da Kurs ($580,63) über dem Abstauber-Limit ($500) liegt → greift "Zone 3 — unabhängig TA" (außer Abstauber-Override, der hier nicht zieht).

**ENTRY-AMPEL: 🟡 WARTEN**
Begründung: Fair bewertet laut TMR-Preiszonen, technisch nur HOLD, kein Abstauber-Trigger (Kurs 16,1% über dem Limit). Weder ein klarer Kaufgrund noch ein Alarmsignal — reine Geduldsposition.

### BLOCK D — KOMBINATIONS-SCORE

Schritt 1 — TA-Norm (INVESTOR-Konstanten MAX +10,44 / MIN −9,66):
TA-Norm = (2,4625 + 9,66) / (10,44 + 9,66) × 10 = 12,1225 / 20,10 × 10 = **6,03**

Schritt 2 — Bewertungs-Score: Zone 3 → 5,0 Basispunkte + MoS-Bonus 🔴 (−1,0) = **4,0**

Schritt 3 — K-Score = (TA-Norm 6,03 + Bewertungs-Score 4,0) / 2 = **5,02**

**Aktive Sizing-Caps geprüft:** TMR Konfidenz 🟢 (nicht 🔴, kein Cap) · TMR Aktive Flags: KEINE (kein SBC-Infection, kein Transformation-Flag, kein BIAS-Strike; Debt-Maturity ist 🟡 ERHÖHT, nicht 🔴 KRITISCH → kein Cap) → **Kein Cap aktiv.**

**KOMBINATIONS-SCORE: 5,0 / 10 → 🟡 MODERATER ENTRY**
TA-Norm: 6,03 / Bewertungs-Score: 4,0 (inkl. MoS-Bonus −1,0)
Aktive Caps: Kein Cap aktiv
Horizont-Modus: INVESTOR — Gewichts-Schema F1×1,5/F2×1,5/F3×1,25/F4×0,75/F5×1,0

### BLOCK E — KONFLIKTERKENNUNG

Geprüft gegen alle definierten ⚔️-Kategorien:
- Bewertungs-Konflikt (TA BUY/STRONG BUY + Zone 4/5): nein, TA=HOLD
- Timing-Konflikt (Zone 1/2 + TA WEAK/AVOID): nein, Zone 3
- Momentum-Konflikt (MoS 🟢 + TA AVOID): nein
- Abstauber-Konflikt (TMR BEOBACHTEN + ...): nein, TMR=KAUFEN
- Flag-Konflikt: nein, keine aktiven Flags
- Horizont-Konflikt (Score ausschließlich Faktor-4-getrieben): nein — Faktor 1 (+2,40) trägt den Score, nicht Faktor 4 (+0,1875)
- Formations-Konflikt: nein, keine Formation vorhanden

→ Formal: **"Bewertung und Technik zeigen in dieselbe Richtung"** (keiner der definierten Konflikt-Trigger greift).

**Zusätzlicher, nicht formal kategorisierter Hinweis (für Brian wichtig):** TMR sagt KAUFEN (Reaper Score 8/10), TA liefert nur HOLD statt des laut Mapping-Tabelle erwarteten BUY/STRONG-BUY-Bereichs. Das ist kein harter ⚔️-Konflikt nach Definition dieses Prompts (der triggert erst bei AVOID/WEAK), aber real ist die Lücke da: **Die fundamentale These ist bullish, das Timing-Fenster ist es (noch) nicht.** Kurs sitzt fair bewertet und technisch direkt unter dem 52W-Hoch — kein Rabatt, keine Schwäche zum Reinkaufen.

### BLOCK F — ZYKLUS-KONTEXT
TMR Zyklus-Status: **AUFSCHWUNG**
→ "✅ Bullishe TA-Signale durch Zyklusrückenwind unterstützt." — mit der Einschränkung, dass die TA-Signale hier selbst nur moderat bullish sind (HOLD, nicht BUY); der Zyklusrückenwind stützt die Story, ersetzt aber kein fehlendes Kauf-Timing-Signal.

════════════════════════════════════════════════════════════

---

*Ende der Analyse. Testlauf-Hinweis: Dies ist der erste vollständige Claude-Durchlauf durch den TA-v1.9-Prompt für MA im Investor-Entry-Modus, mit TMR-Handoff aus dem MA-TMR-Testlauf vom 22.08.2026. Kein Cross-Check gegen ChatGPT/Gemini erfolgt. Mehrere technische Datenpunkte (OBV, Akkumulationsmuster, Bollinger Bands, exakte 3M/6M-Stichtagskurse, exakter S&P500-Benchmarkwert vor 6 Monaten) waren über frei zugängliche Web-Quellen nicht oder nur näherungsweise verifizierbar — entsprechend ehrlich als [KEINE DATEN] bzw. als Näherungswert markiert, mit Konfidenz-Abschlag auf "Niedrig". Sollte vor produktivem Einsatz der Pipeline gegengeprüft werden, insbesondere die Institutional-Footprint-Lücke.*
