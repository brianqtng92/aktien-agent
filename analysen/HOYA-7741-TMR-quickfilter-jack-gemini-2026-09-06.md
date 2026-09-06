# TMR QUICK FILTER · MODUS A – Jack (Gemini, via gemini-bridge, enable_search=False)
## Hoya Corporation · 7741 Tokyo (ADR: HOCPY) · Stand: 2026-09-06

**Dispatch-Kontext:** Vollstaendiger Mega-Prompt (7 Klarstellungsbloecke + alle 3
Methodik-Dateien TMR/Scout/TA + Jarvis' Fact-Pack), `enable_search=False`
(siehe HANDOVER.md 10.10 - bei Gemini+3-Datei-Mega-Prompt bekanntes Abbruch-
Risiko mit aktiver Suche). Dies ist zugleich der Test-Lauf fuer den heute
(2026-09-06) implementierten Fact-Pack-Tag-Fix (siehe HANDOVER.md 10.13 Block 7
und Agent-Playbook.md "Fact-Pack-Tag-Disziplin").

**ERGEBNIS DES TESTS: KEIN ABBRUCH.** Jack lief die komplette Analyse bis zum
Ende durch, kein SCHROTT/Terminal-State. Piotroski F-Score (7-8/9) und
FCF-Marge (~23,4%) wurden korrekt als [TRAINING] uebernommen statt als [N/V]
behandelt zu werden - identisch zu den fruehen Faellen (Disco Corp, Lasertec),
bei denen genau diese beiden Kennzahlen im Fact-Pack faelschlich [N/V] getaggt
waren und den Abbruch ausloesten.

---

## SCHRITT 0 / 0C

Kurs 24.140 JPY / 156,10 USD (04.09.2026), Marktkap. ~8,08 Bio. JPY [LIVE/TRAINING
aus Fact-Pack uebernommen]. Going-Concern-Precheck: Bilanzqualitaet mit D/E ~4,1%
[VERIFIED], Going-Concern-Risiko "evident unplausibel" - kein Abbruch.

## DNA-CHECK (K-BASIS 5S)

| K-Kriterium | Wert | Tag | Status |
|---|---|---|---|
| ROIC >20% | ~20-30% | [TRAINING] | Ja |
| FCF-Marge >=20% | ~23,4% | [TRAINING] | Ja |
| Op. Leverage | Ja (Q1 FY27: Umsatz +16%, Gewinn +28,1%) | [VERIFIED] | Ja |
| Piotroski F-Score >=7 | 7-8/9 (aus GF Score 98/100 + qualitativen Indikatoren) | [TRAINING] | Ja |
| EPS-CAGR 5J >=12% | ~12-18% | [TRAINING] | Ja |

**K: 5/5** - kein K-Kriterium [N/V], kein Abbruch. Alle fuenf K-Kriterien
[TRAINING] statt [VERIFIED] -> Konfidenz-Deckel automatisch NIEDRIG (>=2 K
TRAINING-Regel).

## Reaper-Reality-Check (Stichpunkte)

Moat-Verifikation: Preissetzungsmacht indirekt Ja (Duopol + hohe Margen)
[TRAINING]. Switching-Cost-Beweis belegt (extreme technische Eintrittsbarrieren
bei EUV-Mask-Blanks) [VERIFIED]. Marktanteil-Trend stabil/steigend [VERIFIED].
**Moat-Score: 3-4/4 STARK.** Moat-Trend STABIL, kein Decay-Flag.

## Valuation (Quick Filter Schnellcheck)

KGV trailing ~36,9x, KGV forward ~34,9x [VERIFIED] - deutlich ueber
Branchendurchschnitt (~16,6x, +110% Premium). PEG ~2,33x [TRAINING] -
"ambitioniert" (1,5-2,5-Band). EV/FCF ~36,6x [TRAINING] - hoch.

## Devil's Advocate

1. Warum liege ich komplett falsch? Die hohe Bewertung koennte durch
   langfristige EUV-Wachstumsaussichten und Life-Care-Stabilitaet
   gerechtfertigt sein, staerker als die niedrige Konfidenz suggeriert.
2. Welche Kennzahl widerspricht am staerksten? Das KGV (~35x, mehr als
   doppelt so hoch wie Branchendurchschnitt) und der ambitionierte PEG (~2,33x).
3. Was sieht der Markt, was ich ignoriere? Die herausragende Wettbewerbsposition
   (Duopol >75% MA bei EUV-Mask-Blanks), Elite-Margen und solide Bilanz
   rechtfertigen ein Qualitaets-Premium.

## MEIN VERDICT

**RATING: BEOBACHTEN**
**REAPER SCORE: 6/10** - Anker waere bei sauberem 5/5-VERIFIED-Durchmarsch
7-8/10, aber Konfidenz-Deckel (NIEDRIG wegen 4 TRAINING-K-Kriterien) begrenzt
auf max. 6/10.
**KONFIDENZ: NIEDRIG** (1 K VERIFIED, 4 K TRAINING)
**SIZING: 0%** (Rating BEOBACHTEN). Theoretisch bei Kauf: nur Tier 3 (max. 2%)
wegen NIEDRIGER Konfidenz.

**Beobachten-Protokoll:**
- Abstauber-Limit: ~KGV <30x, entspricht grob ¥20.000 (bzw. ~130-140 USD ADR,
  nahe 52-Wochen-Tief)
- Upgrade-Trigger (mind. 2/3): Kurs erreicht Abstauber-Limit / Q2-FY2027-Zahlen
  bestaetigen Wachstum+Margen / Makro-Sentiment dreht positiv
- Downgrade-Trigger: K-Kriterium bricht dauerhaft (2Q) / Bewertung >20% ohne
  Fundamental-Verbesserung / Moat-Erosion sichtbar
- Beobachtungs-Horizont: 12-24 Monate

**Terminal-State-Selbstpruefung (explizit von Jack durchgefuehrt):** Kein
Abbruch-Zustand erreicht, kein K-Kriterium [N/V], kein Going-Concern-Zweifel.
