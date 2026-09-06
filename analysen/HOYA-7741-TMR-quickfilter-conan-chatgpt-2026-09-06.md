# TMR QUICK FILTER · MODUS A – Conan (ChatGPT, via openai-bridge, enable_search=True)
## Hoya Corporation · 7741 Tokyo (ADR: HOCPY) · Stand: 2026-09-06

**Dispatch-Kontext:** Identischer Mega-Prompt wie an Jack (7 Klarstellungsbloecke
+ alle 3 Methodik-Dateien + Jarvis' Fact-Pack), `enable_search=True`. Conan nutzte
seine eigene Live-Websuche aktiv und fand mehrere Primaerquellen (Hoya
Geschaeftsbericht, Quartalsbericht, TDnet-Meldungen), die teils vom Fact-Pack
abweichen - explizit benannt statt stillschweigend uebernommen, wie gefordert.

**ERGEBNIS: KEIN ABBRUCH.** Conan lief die komplette Analyse durch, kein
SCHROTT/Terminal-State - bestaetigt explizit am Ende: "Kein K-Kriterium ist
[N/V], kein bestaetigter Going-Concern-Zweifel. Kein Abbruch-Zustand erreicht."

---

## Wichtige eigene Recherche-Funde (Divergenzen zum Fact-Pack)

- **Piotroski F-Score:** Conan fand per Live-Suche selbst WIDERSPRUECHLICHE
  externe Quellen (StockAnalysis: 3, Validea: 4, ValueMarkers: 7) und
  rekonstruierte selbst einen Wert von **~6/9** [TRAINING] aus den
  Einzelkriterien - niedriger als Jarvis' Fact-Pack-Schaetzung (7-8/9), aber
  ausdruecklich NICHT [N/V]. Das ist der interessanteste Cross-Check-Fund:
  drei verschiedene Datenanbieter UND Conans eigene Rekonstruktion UND Jarvis'
  Schaetzung landen bei vier unterschiedlichen Werten (3, 4, 6, 7-8) - ein
  Lehrbeispiel dafuer, wie unscharf dieser Kennzahl bei japanischen Emittenten
  ist, aber Conan behandelt es trotzdem korrekt als TRAINING-Bandbreite statt
  als Abbruchgrund.
- **Bewertung niedriger als im Fact-Pack:** Conans Live-Daten (Stand 06.09.)
  zeigen KGV trailing 30,57x / forward 28,18x - niedriger als Jarvis'
  36,9x/34,9x (vermutlich aktuellere TTM-Basis). PEG 3,08, EV/FCF 32,0x.
- **Neue Corporate-News seit Fact-Pack-Stichtag:** (1) Aktienrueckkaufprogramm
  aktiv (bis zu 10 Mio. Aktien/200 Mrd. JPY bis 24.03.2027, bereits 973.500
  Aktien fuer ~25 Mrd. JPY im August zurueckgekauft). (2) Strategische Pruefung
  des PENTAX-Medical-Endoskopiegeschaefts (moeglicher Verkauf), angekuendigt
  31.07.2026 - finanzielle Auswirkung noch offen.
- **Moat-Praezisierung:** manche Quellen sehen AGC (nicht Hoya) als fuehrend
  bei EUV-Mask-Blanks - kein reines "Hoya besitzt EUV", sondern echtes Duopol
  mit Wettbewerbsspannung.
- **Eigene TA-Daten gefunden:** Kurs unter 50-Tage-SMA (25.222,60) und
  200-Tage-SMA (26.102,63), RSI 37,83 (schwach, nicht ueberverkauft).

## DNA-CHECK (K-BASIS 5S, Conans eigene Bewertung)

| Kriterium | Wert | Tag | Erfuellt? |
|---|---|---|---|
| ROIC >20% | ~21,1% (konservativ, Hoya-eigene Angabe) | [VERIFIED+DISCREPANCY] | Ja |
| FCF-Marge >=20% | ~23,4% (FY26), ~24,1% TTM | [VERIFIED] | Ja |
| Op. Leverage | Ja (Q1 FY27: Umsatz +16%, Gewinn +28,1%, Op.Profit +30%) | [VERIFIED] | Ja |
| Piotroski >=7 | ~6/9 (eigene Rekonstruktion) | [TRAINING+HIGH DISCREPANCY] | **Nein/Grenzfall** |
| EPS-CAGR 5J >=12% | ~13,7% p.a. | [VERIFIED] | Ja |

**K: 4/5** - Piotroski nicht als erfuellt gewertet (Conans strengere eigene
Rekonstruktion), aber **kein N/V**, also **kein Abbruch**. K = K-BASIS-1 =
Grenzfall mit Begruendungspflicht, Analyse laeuft normal weiter.

## Moat-Verifikation

Moat-Score **3,5/4 STARK**: EUV-Mask-Blank-Duopol mit AGC (kombiniert ~90-93%),
strukturell kritischer Zulieferer, aber kein reines Monopol (manche Quellen
sehen AGC als fuehrend). Kein akuter Moat-Decay, aber Multi-Sourcing-Risiko als
Beobachtungspunkt benannt.

## Valuation

Trailing P/E 30,57x, Forward P/E 28,18x, P/S 8,21x, P/B 7,84x, P/FCF 34,09x,
EV/FCF 32,0x, PEG 3,08 (TMR-Warnzone >2,5), FCF-Yield 2,93% (mager gegen
~2,9-3,0% JGB-Rendite). **Valuation-Urteil: VORSICHT/TEUER, keine
Sicherheitsmarge.**

## MEIN VERDICT

**RATING: BEOBACHTEN**
**REAPER SCORE: 6,5/10** - Elite-Margen + Net Cash + EUV-Moat stuetzen die
Qualitaet, Piotroski-Divergenz und EV/FCF 32x verhindern ein Kauf-Rating.
**KONFIDENZ: GELB (62%)** - viele Primaerquellen-Daten gut, aber Piotroski- und
Marktanteils-Quellen widersprechen sich stark.
**SIZING: 0% aktuell** (Tier 4). Bei Trigger spaeter max. Tier 3 (1-2%).

**Beobachten-Protokoll:**
- Abstauber-Limit: ~20.500 JPY (~133 USD ADR) - entspricht grob Forward-KGV
  ~24x
- Upgrade-Trigger (mind. 2/3): Kurs erreicht Limit / Q2-FY2027 (~30.10.2026)
  bestaetigt Wachstum+Marge / Piotroski-Bild klaert sich Richtung >=7
- Downgrade-Trigger: FCF-Marge 2Q <20% / Marktanteilsverlust bei EUV-Mask-
  Blanks / Bewertung >20% ohne Fundamentalverbesserung / PENTAX-Review
  belastet Kapitalallokation / Operating Margin dauerhaft <28%
- Naechster Pflichtpruefpunkt: Q2-FY2027-Zahlen, ~30.10.2026

**Scout-Perspektive (Zusatz):** WATCHLIST-ELITE-Qualitaet, aber kein
Scout-Kaufsetup - reifer Quality-Compounder, kein Fruehphasen-Fall fuer Conan.

**TA-Perspektive (Zusatz, mit selbst gefundenen Live-Chartdaten):** Kurs unter
50-/200-Tage-SMA, RSI 37,83 (schwach). TA-Rating HOLD/NEUTRAL-WEAK - kein
technischer Kaufzwang, aber auch keine Panik.
