# TMR QUICK FILTER · MODUS A – Jarvis (Claude)
## Hoya Corporation · 7741 Tokyo (ADR: HOCPY) · Stand: 2026-09-06

**Kontext:** Hoya ist bereits Watchlist-Eintrag (Champions, CRV bisher
🟠 VORSICHT/TEUER, siehe `watchlist.md` Zeile 160). Dieser Lauf ist eine
vollständige Neubewertung/Auffrischung dieses bestehenden Eintrags – KEIN
Erstscreening eines brandneuen Kandidaten, aber auch keine bereits
gehaltene Depot-Position (nicht in `depot/trade-republic.md`,
`depot/scalable-capital.md` oder `depot/smartbroker-plus.md` gefunden) –
Block 5 (Gründliche-These-Prüfung-vor-Verkauf) daher nicht einschlägig.

**Zweiter Zweck dieses Laufs:** bewusster Test des heute (2026-09-06)
implementierten Fact-Pack-Tag-Fixes (siehe HANDOVER.md 10.13 "Block 7
ergänzt" und Agent-Playbook.md "Fact-Pack-Tag-Disziplin") – frühere
Läufe (Disco Corp, Lasertec) hatten Piotroski F-Score/FCF-Marge in Jarvis'
eigenem Fact-Pack fälschlich als [N/V] statt [TRAINING] getaggt, was Jacks
(Gemini) SCHROTT/Terminal-State-Abbruch auslöste. Ich wende hier bewusst
die korrekte TRAINING-vs-N/V-Schwelle an.

## SCHRITT 0 – LIVE-CHECK (eigene Web-Recherche, 2026-09-06)

- **Kurs (TSE):** ¥24.140 – Schlusskurs 04.09.2026, 15:30 JST.
  [LIVE] – gegengecheckt über zwei unabhängige Kanäle: (a) WebSearch-
  Aggregation (mehrere Finanzportale konsistent), (b) Twelve-Data-Live-Quote
  für die ADR HOCPY: $156,10 Schlusskurs 04.09.2026, Vortagesschluss
  $157,31, 52-Wochen-Range $130,05–$190,18. Impliziter FX ¥24.140/$156,10 ≈
  ¥154,6/$ – plausibel für 2026, bestätigt Konsistenz zwischen beiden
  Quellen (kein Lasertec-artiger Fehlkurs).
- **Abweichender älterer Wert verworfen:** eine Quelle nannte einen
  Referenzkurs ¥27.245 im Kontext eines Analysten-Kursziels – das ist
  inkonsistent mit dem zweifach bestätigten Live-Kurs ¥24.140 und wird
  nicht übernommen (aktuellere/mehrfach bestätigte Zahl vor älterer/
  singulärer Zahl, siehe Regelwerk).
- **Marktkapitalisierung:** ~¥8,08 Bio. / ~$52,3-52,4 Mrd. (Aktien
  ausstehend ~334,5 Mio., konsistent mit ¥24.140 × 334,5 Mio. ≈ ¥8,08 Bio.).
  [TRAINING] (Einzelangabe vom 21.08.2026, ~2 Wochen alt, aber intern
  konsistent nachgerechnet – ein zweiter, abweichender Aktienzahl-Wert
  (379,7 Mio.) wurde verworfen, da er nicht zur Marktkap-Angabe passt).
- **Going-Concern-Precheck (SCHRITT 0C):** ✅ Unauffällig. Netto-Cash-nahe
  Bilanz (Eigenkapital ¥1.002,9 Mrd. vs. Gesamtschulden nur ¥41,5 Mrd.,
  D/E ~4,1%), durchgehend positive und wachsende operative Erträge über
  mehrere Jahre – ein Going-Concern-Risiko ist evident unplausibel.

## SCHRITT 2 – DNA-CHECK

**AKTIVE K-BASIS:** Standard 5S (Hoya ist Industrie/Tech/Healthcare-
Mischkonzern, kein Finanz-/SaaS-/Infrastruktur-Override einschlägig).

| Kennzahl | Typ | Schwelle | Ist-Wert | Quelle | Tag | Status |
|---|---|---|---|---|---|---|
| ROIC | K | >20% | Quellen streuen breit (16,4% / 20-25% / 48-60% je nach Methodik). Die Mehrzahl der Schätzungen liegt klar über 20%; selbst die konservativste Lesart liegt nahe der Schwelle. Plausible Größenordnung: ~20-30%. | WebSearch (GuruFocus/stockanalysis/roic.ai, divergent) | [TRAINING] | ✅ (Grenzfall bei der konservativsten Einzelquelle, aber Median klar >20%) |
| FCF-Marge (real) | K | ≥20% | Operativer CF ¥278,45 Mrd. − Capex ¥56,58 Mrd. = FCF ¥221,87 Mrd. auf Umsatz ¥947,75 Mrd. → **≈23,4%**. Keine einzelne zitierte "FCF-Margin"-Kennzahl gefunden, aber aus soliden Linienpositionen selbst berechnet – klare Größenordnung ableitbar. | Eigene Berechnung aus CFO/Capex/Umsatz (WebSearch-Rohdaten) | [TRAINING] | ✅ |
| Op. Leverage | K | Ja | Q1 FY2027: Umsatz +16,0% YoY, Gewinn +28,1% YoY – Gewinn wächst deutlich schneller als Umsatz, klassisches Signal für positive operative Hebelwirkung bei hohem Fixkostenanteil (F&E/Spezialfertigung). | WebSearch (Q1-FY2027-Zahlen) | [TRAINING] | ✅ |
| Piotroski F-Score | K | ≥7 | **Keine einzelne zitierbare Piotroski-Zahl gefunden** (auch bei gezielter Suche nach GuruFocus-Wert nicht). ABER: GuruFocus "GF Score" (Qualitäts-Composite) 98/100 gefunden, plus mehrere qualitative Einzelindikatoren, die direkt in Piotroskis 9 Kriterien einzahlen: durchgehend positive UND wachsende Profitabilität (ROA/Nettomarge steigend), operativer Cashflow (¥278,45 Mrd.) deutlich positiv und über净income-Niveau (Qualität der Erträge erfüllt), sinkende/sehr niedrige Verschuldung (D/E nur 4,1%, keine Anzeichen für Nettoverschuldungsanstieg), keine Hinweise auf Aktienverwässerung, Margen stabil/steigend (operative Marge 29,9%). Aus dieser Kombination ist eine plausible GRÖSSENORDNUNG ableitbar: **7-8 von 9**. **Explizite Anwendung des heutigen Fixes:** dies ist exakt der Kennzahlentyp, der bei Disco Corp/Lasertec fälschlich [N/V] getaggt wurde, obwohl daneben plausible qualitative Indikatoren standen – hier bewusst korrekt [TRAINING], NICHT [N/V]. | GuruFocus (GF Score) + eigene Herleitung aus Profitabilität/Bilanzqualität | [TRAINING] | ✅ |
| EPS-CAGR (5J) | K | ≥12%, Ziel 15-25% | Keine sauber vergleichbare 5J-EPS-Zeitreihe gefunden (verfügbare Quartalsdaten sind einheitenmäßig uneinheitlich/teils ADR-USD, teils JPY). Aus Umsatzwachstum (FY2026 +9,4%, Q1 FY2027 +16,0%), Gewinnwachstum (Q1 FY2027 +28,1%) und dem langjährig bekannten Track Record als stabiler Compounder ist eine plausible Größenordnung **~12-18%** ableitbar – räumt die Schwelle, aber ohne großen Puffer. | WebSearch (Wachstumsraten, keine direkte 5J-EPS-Reihe) | [TRAINING] | ✅ (Grenzfall, geringerer Puffer als andere K) |

**DNA-URTEIL: K: 5/5 (Standard-K-BASIS)** – alle fünf K-Kriterien erfüllt,
aber **alle fünf als [TRAINING] statt [VERIFIED] getaggt** → automatischer
Konfidenz-Deckel greift (≥2 K-Kriterien [TRAINING] → Konfidenz max. 🟡
MITTEL, hier de facto sogar niedriger, da ausnahmslos alle K betroffen
sind). **Kein Abbruch** – kein K-Kriterium ist [N/V], die Abbruch-Schwelle
(K ≤ K-BASIS−3 bzw. jedes einzelne [N/V]) wird an keiner Stelle erreicht.

## Moat / Wettbewerbsposition

Hoya + AGC (Asahi Glass) bilden ein **Duopol bei EUV-Mask-Blanks** mit
kombiniert ~90-93% Weltmarktanteil; Hoya allein >60% bei konventionellen
Mask-Blanks, >75% spezifisch bei EUV – strukturell abgesichert durch
extreme technische Eintrittsbarrieren (defektfreie Mo/Si-Multilayer-
Beschichtung). Das IT-Segment (inkl. Halbleiter-Substrate) macht <30% des
Umsatzes, aber >50% des Gewinns aus (Margen-Hebel). Das Life-Care-Segment
(Brillengläser, Kontaktlinsen, Medizintechnik) liefert >60% Umsatz und
zeigt aktuell zweistelliges Wachstum (Brillengläser +11% YoY zuletzt). Der
Moat ist damit **doppelt abgesichert**: ein enges, hochprofitables
Halbleiter-Nischenmonopol PLUS ein breiteres, stabileres Konsumgüter-
Standbein – seltene Kombination, ähnlich wie bei Lasertec (Halbleiter-
Nische) aber mit zusätzlicher Diversifikation.

## Bewertung

- KGV trailing: ~36,9x / KGV forward: ~34,9x (Konsens ~32-37x je nach
  Quelle – konsistent).
- PBR: 8,71x – hoch, aber typisch für einen margen-starken
  Nischenmonopolisten mit wenig Sachanlagevermögen.
- Dividendenrendite: ~1,07% (kein Ertrags-Treiber, Compounder-Story
  primär über Kursgewinn).
- Analysten-Kursziel-Median: ¥29.594 (Quelle nennt +8,6% Upside – dieser
  Prozentwert bezieht sich vermutlich auf den verworfenen Referenzkurs
  ¥27.245, nicht auf den bestätigten Live-Kurs ¥24.140; gegen den
  bestätigten Kurs gerechnet ergäbe sich sogar ~+22,6% Upside – ich
  behandle das mit Vorsicht, da die Zielkurs-Methodik der Quelle nicht
  transparent ist).

## Champions oder Profi? Eigene Einordnung

Bleibt **Champions**: strukturell abgesicherter Duopol-Moat in einem
wachsenden Halbleiter-Nischenmarkt, Elite-Margen (Brutto/operativ), sehr
konservative Bilanz (D/E 4,1%), plus ein zweites, unkorreliertes
Ertragsstandbein (Medizintechnik/Optik). Bestätigt die bisherige
Watchlist-Einordnung.

**CRV bleibt 🟠 VORSICHT/TEUER** – KGV ~35x liegt deutlich über dem
Branchendurchschnitt (~16,6x lt. bisherigem Watchlist-Eintrag) und bietet
aktuell wenig Sicherheitsmarge, trotz solider fundamentaler Entwicklung
(Q1 FY2027 Reakzeleration). Kein Grund für eine Rückstufung der
Geschäftsqualität, aber auch kein aktuell günstiger Einstiegszeitpunkt.

**Nächster Prüfpunkt:** nächste Quartalszahlen (Q2 FY2027, ~Ende Oktober/
Anfang November 2026) – Bestätigung der Q1-Reakzeleration, insbesondere ob
das IT-/Halbleiter-Segment vom KI-/Advanced-Node-Capex-Zyklus profitiert.

**Sizing-Empfehlung:** kein neuer Kauf bei aktueller Bewertung – Watchlist-
Status (Champions/🟠) bestätigt, kein Kategorie-Wechsel.

## TA-Quickcheck (Jarvis, MODUS 1 Standard-TA, ohne eigenen Chart-Tool-Zugriff
in dieser Session – nutze Conans per Live-Websuche gefundene, primärquellen-
nahe Chart-Daten als Cross-Check-Basis statt eigener Schätzung)

- Kurs 24.140 JPY liegt UNTER SMA50 (~25.222,60) und UNTER SMA200 (~26.102,63)
  [LIVE, von Conan per Websuche bestätigt] – kurzfristige MA-Stack-Bearish-Lage
  trotz solider Fundamentaldaten, klassisches "gutes Unternehmen, Kurs
  konsolidiert" statt Trendbruch-Signal (52-Wochen-Performance weiterhin
  +23,64%, also Konsolidierung innerhalb eines längeren Aufwärtstrends).
- RSI(14) 37,83 – schwach, aber nicht klassisch überverkauft (<30) [LIVE].
- Volumen 04.09.: ~985.000 vs. 20T-Ø ~941.675 – kein Panik-/Distributionsvolumen
  erkennbar.
- **TA-Rating: HOLD/NEUTRAL-WEAK.** Kein technischer Kaufzwang, aber auch kein
  Abverkaufssignal – deckt sich mit dem TMR-Bild (Qualität intakt, Bewertung/
  Timing noch nicht attraktiv).
- Ohne TMR-Bear/Base/Bull-FV aus einem vollen DCF (Quick Filter liefert das
  nicht) ist MODUS 2 (Investor-Entry-Preiszonen) hier nicht anwendbar – bleibt
  MODUS 1.
