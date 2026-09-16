# Cboe Global Markets Inc. (CBOE) — Full Deep Dive, 3-fach-Cross-Check

**Ticker:** CBOE (BATS/NASDAQ) · **ISIN:** US12503M1080 · **Datum:** 16.09.2026
**Depot-Status:** Bestehende Position, Kategorie Champions (siehe `depot/kategorisierung.md`) — Anlass war Brians Wunsch, den Ausbau der Position zu prüfen.
**Modus:** A – Einzelanalyse, Tiefe FULL DEEP DIVE, TMR-Pfad (Bucket A/C, Finanzsektor-Override/Asset-Manager-Börsenbetreiber).

---

## 0. Vorgeschichte: der Bugfix, der diese Analyse erst möglich gemacht hat

Der erste Versuch (16.09., vormittags) über `ask_gemini_agentic`/`ask_chatgpt_agentic` scheiterte: beide Funktionen hatten **keinen echten Web-Search-Zugriff** (reiner Code-Bug in den lokalen Bridge-Servern, siehe HANDOVER.md Abschnitt 10.14) — Jack (Gemini) erfand daraufhin Fundamentaldaten (selbst als "Simulierte..." gekennzeichnet, aber trotzdem mit `[VERIFIED]`/`[LIVE]` getaggt, ein echter Regelverstoß), Conan (ChatGPT) erkannte den fehlenden Zugriff dagegen korrekt und meldete ihn ehrlich statt zu raten.

Nach dem Bugfix (beide Bridge-Server neu gestartet, `ask_gemini`/`ask_chatgpt` jetzt mit echtem Such-Zugriff verifiziert) wurde dieser Full Deep Dive komplett neu durchgeführt — diesmal mit echter, unabhängiger Web-Recherche bei allen drei Beinen (Jarvis/Jack/Conan). Jack brach einmal mitten in der Analyse ab (bekanntes Gemini-Verhalten: Suche wird fälschlich als abgeschlossene Antwort interpretiert) und wurde mit einem gezielten Fortsetzungs-Prompt komplettiert.

---

## 1. SCHRITT 0/0C — Live-Check

**Kurs:** $270,40 (15.09.2026 Schlusskurs, Twelve Data [LIVE]) · -4,96% Tagesbewegung · 52W-Range $227,15-$371,18.
Jacks eigene Suche fand $277,77 (TradingView) — Diskrepanz zur Twelve-Data-Primärquelle nicht abschließend geklärt, aber unter der 10%-Schwelle für eine Erklärungspflicht.

**Kein CBOE-spezifischer Negativ-Auslöser gefunden** (trotz gezielter Recherche aller drei Beine) — der Tagesverlust ist Teil einer sektorweiten Bewegung am FOMC-Vortag: ICE -0,54%, CME -1,91%, NDAQ -2,56%, SPY nur -0,46% [LIVE, Twelve Data]. Getrieben von US-10J-Rendite auf 5,041% (höchster Stand seit Juli 2007) und Öl-Preis-Schock (Straße von Hormuz).

**Going-Concern:** ✅ Unauffällig (alle drei Beine unabhängig bestätigt — Conan verifizierte direkt gegen das SEC-10-K: KPMG-Testat uneingeschränkt, kein "going concern"/"substantial doubt"-Treffer im Volltext).

---

## 2. Leitindikator-Pflicht (Regel 39) — erster produktiver Einsatz

CBOE = Hybrid/Finanzdienstleister-Börsenbetreiber, VIX/Optionsvolumen als dominanter externer Nachfrage-Treiber. Von Aegis geliefert und von allen drei Beinen referenziert:
- VIX ~15,8-17,1 (moderat) — ABER: Cboes eigener "Week of 9-14-2026"-Marktbericht zeigt OVX (Öl-Vola) +14 Pkt auf 59% WoW, drei der vier größten VIX-Call-Trades des Jahres in den letzten 2 Wochen (>120.000 Kontrakte je Trade, ~$12 Mio. Prämie), SPX-1-Monats-Put-Skew im 73. Perzentil.
- **Einordnung (Konvergenz aller drei Beine):** operativ POSITIV fürs gebührenbasierte Handelsvolumen-Geschäft — Jack und Conan stuften die Zyklusphase übereinstimmend als ÜBERHITZUNG ein (moderater VIX-Level, aber stark erhöhte Absicherungsnachfrage als Frühindikator).

---

## 3. DNA-Check — Finanzsektor-Override (K-BASIS 4 nach Piotroski-Override)

| Kriterium | Jarvis | Jack | Conan |
|---|---|---|---|
| ROIC >20% | 26,9% ✅ (stockanalysis) | 16,9% ❌ (GuruFocus, konservativ gewählt) | 23-29% ✅ |
| Op. Leverage | Ja ✅ | Ja ✅ | Ja ✅ (H1 Op.Income +41,6% bei Net-Revenue +26,7%) |
| EPS-CAGR(5J) ≥12% | ~20% ✅ (ex 2022-Impairment-Anomalie) | 19,6% ✅ | ~21% ✅ |
| ROE >15% | 26,3% ✅ | 26,3% ✅ | 25-26% ✅ |

Trotz der ROIC-Divergenz (Datenquellen-Streuung 16,9-29%, siehe bekanntes Muster "unterschiedliche Definition/Zeitraum") bestehen alle drei Beine das K-Gate klar bis grenzwertig — kein Abbruch. Piotroski-Override-Ersatzkriterien (ROE-Trend, Fee-Marge-Trend) von allen dreien bestätigt.

**Real recherchierte Primärzahlen (Conan, direkt aus SEC 10-K/10-Q):**
- FY2025 Total Revenue $4.714 Mio., Net Revenue $2.429 Mio. (+17% YoY)
- Q2 2026 Net Revenue $731,6 Mio. (+25% YoY), Diluted EPS $3,35 (+50%), Adj. EPS $3,56 (+45%)
- H1 2026 Net Revenue $1.460,5 Mio. (+26,7% YoY)
- Adjusted Operating Margin FY2025: 65,6% (auf Net-Revenue-Basis) — H1 2026 sogar 67,2%
- Capex/Net-Revenue: 2,9% (FY2025) bzw. 3,6% (H1 2026) — klar unter 5%
- SBC FY2025: $50,4 Mio. (1,1% Total Revenue / 2,1% Net Revenue) — keine SBC-Infection
- Net Debt: negativ (Netto-Cash $0,77-0,83 Mrd.) — Net Debt/EBITDA klar erfüllt
- Debt-Fälligkeiten: $650 Mio. Notes fällig Januar 2027 (3,65%), $500 Mio. 2030 (1,625%), $300 Mio. 2032 (3,0%) — Refinanzierungsrisiko NIEDRIG bis ERHÖHT (Januar-2027-Fälligkeit in höherem Zinsumfeld)

---

## 4. Moat & Management

**Moat:** STARK bei allen drei Beinen (4/4 bzw. 3,5/4 Kriterien) — SPX-/VIX-Exklusivlizenz mit S&P Global (>98% des US-Index-Optionsvolumens), Netzwerkeffekte, hohe Switching-Costs für institutionelle Marktteilnehmer. Trend: STABIL bis STÄRKER (Randgeschäfte wie Cboe Japan/Digital eingestellt bzw. Australien/Kanada an TMX verkauft — Portfoliofokussierung, kein Moat-Verfall im Kern).

**Management-Score:** Jack 4/7, Conan 5,0/7 — Guidance zweimal 2026 angehoben (zuletzt auf "mid to high teens" organisches Net-Revenue-Wachstum), Dividende +19% erhöht (16. Jahr in Folge), Buyback-Programm mit $536,8 Mio. verbleibender Ermächtigung. Tonalität in Earnings Calls durchweg positiv, kein erkennbarer Dodge-Factor.

---

## 5. Valuation — der zentrale, konvergente Befund

**Alle drei unabhängigen DCF-Rechnungen kommen auf einen Fair Value deutlich über dem Analysten-Konsens (~$315) und über dem aktuellen Kurs:**

| | Jarvis | Jack | Conan |
|---|---|---|---|
| Beta | 0,44 | 0,64 | 0,41 |
| WACC | 6,89% | 7,73% | 6,74% |
| g (Basis) | 6,2% (Revenue-CAGR-Fallback) | 5,6% | 9,5% |
| Gordon-TV FV | $484 | $410 | $447 |
| Exit-Multiple FV | $393 | $382 | $435 |
| **TV-Anteil EV** | 84% ⚠ | n/a | 85% ⚠ |
| **Base FV (final)** | $484 (bewusst nicht weiter gedämpft, stattdessen auf Konsens/Peers verwiesen) | $396,16 (ungedämpft übernommen) | **$360-400 (bewusst risikoadjustiert nach unten korrigiert)** |

**Root Cause (von allen dreien unabhängig identifiziert):** CBOEs sehr niedriges Beta (0,41-0,64 je Quelle) drückt den WACC so nah an die 3%-Gordon-Terminalwachstumsrate, dass der Terminal-Value-Anteil auf 84-87% des Enterprise Value explodiert — ein Struktur-Artefakt des Modells bei diesem Beta-/Margen-Profil, kein Rechenfehler. **Konsequenz für die Methodik:** bei sehr niedrig-Beta-Titeln mit hoher Marge ist der reinen Gordon-Growth-DCF-Zahl grundsätzlich zu misstrauen — Peer-Multiples und Analysten-Konsens sind hier die verlässlicheren Anker (siehe SCHRITT 5B, korrekt von allen drei Beinen ausgelöst: Abweichung DCF vs. Konsens >25-30%).

**Peer-Vergleich (real recherchiert):** CBOE EV/EBITDA 14,25x vs. Peer-Median 17,3x (ICE 16,0x, CME 17-25x je Quelle, NDAQ 17,3x) — **CBOE handelt mit einem Abschlag zu den direkten Peers**, trotz vergleichbarer oder besserer operativer Kennzahlen.

**Analysten-Konsens:** $292-318 (Ø $291,98-318,17), Spanne $248-380 (Barclays $354 Overweight, Deutsche Bank $380 Buy, Morgan Stanley/UBS eher Hold-Bereich).

---

## 5b. Nachtrag (16.09., nach Brians Vollständigkeits-Einwand): Bruttomarge-Trend, TA, Pipeline/Struktur-Risiko/Insider

Der erste Report-Entwurf hatte die Pflicht-Elemente Rigor-Punkte 34-36 (Pipeline-Ausblick/Struktur-Risiko-Check/Insider-Transaktionen) sowie die Kursverlauf-/TA-Seite und den Bruttomarge-Trend beim Komprimieren unterschlagen, statt sie nach dem Kürzen wieder zu ergänzen — genau das kanonische NVO/HawkEye-Seitengerüst hätte das verhindert. Nachträglich real recherchiert/berechnet:

**Bruttomarge-Trend (real, SEC ARS-Filings, Total-Revenue-Basis):** 39,3% (2023) → 40,9% (2024) → 43,4% (2025) — **klare Expansion, keine Erosion.** Getrieben durch Umsatzwachstum, das schneller steigt als Cost-of-Revenue (Section-31-Gebühren, Liquiditätszahlungen). Korrigiert Brians ursprüngliche "Bruttomargen-Erosion"-Vermutung explizit.

**Technische Analyse (Jack-TA v1.9, Investor-Modus, echte Indikatoren via Twelve Data — RSI 35,78, MACD -2,69/1,08/-3,77, Bollinger 319,44/296,38/273,31, SMA20/50/200 296,38/289,25/286,16, EMA20/50 291,83/291,33, OBV fallend, ATR14 10,64):**
- Faktor 1 (Trend&Sektor) -1,275 · Faktor 2 (Momentum) -2,25 (Floor) · Faktor 3 (Volumen/Institutional) 0 · Faktor 4 (Oszillatoren) -0,1875 · Faktor 5 (Preisstruktur) +1,0
- **Gesamtscore -2,7125 → Rating WEAK.** Kein VETO ausgelöst.
- Risiko-Modul: ATR% 3,94% (Hoch) → Stop-Loss ≈$252,68, R/R≈1,44 (schlecht/grenzwertig)
- Investor-Entry-Modus (mit Conans TMR-Werten Bear $242/Base $380/Bull $575): Block A Preiszone 2 ATTRAKTIV · Block B MoS 🔴 KEINER · Block C Entry-Ampel 🟡 WARTEN · Block D Kombinations-Score ≈5,23 → 🟡 MODERATER ENTRY · Block E ⚔ Timing-Konflikt ("Bewertung attraktiv — Technik bärisch") · Block F Zyklus ÜBERHITZUNG
- **Einordnung:** Die TA bestätigt quantitativ das, was die Aegis-Synthese qualitativ schon sagte — fundamental attraktive Zone, technisch noch keine Bestätigung. Begründet den gestaffelten statt sofortigen Nachkauf.

**Pipeline-Ausblick (Rigor-Punkt 34):** Q3-2026-Earnings 30.10.2026 (Analysten-Konsens EPS $3,43, dritte Guidance-Bestätigung/-Anhebung nach zwei Anhebungen in Folge — hoher Erwartungsdruck). SPX-Weeklys-Erweiterung (Dienstag/Donnerstag-Expiries) ab 19./28.09.2026, marginal umsatzpositiv. Cboe/Charles-Schwab-Partnerschaft für S&P-500-Binary-Options in regulierten Prediction-Markets — neue, proprietäre Produktkategorie plus Schwab-Distribution.

**Struktur-Risiko-Check (Rigor-Punkt 35) — neuer Fund:** Prediction-Market-Plattformen (Polymarket, mit angestrebter CFTC-Zulassung) stellen 2026 eine neue, strukturell potenziell disruptive Wettbewerbsform gegenüber klassischen Optionsbörsen dar (einfachere Ja/Nein-Kontrakte statt komplexer Optionsstrukturen). CBOEs Antwort ist proaktiv (Schwab-Partnerschaft bringt eigene S&P-500-Produkte direkt ins Prediction-Market-Terrain) statt defensiv. Keine akute Bedrohung, aber ein neues Beobachtungsthema — ab jetzt Bestandteil der These-Bruch-Kriterien (siehe unten). Regulatorik SPX-Exklusivlizenz weiterhin unkritisch: keine neue Litigation gefunden, 2026er SEC-Filings zeigen ausschließlich proaktive Produkterweiterungen.

**Insider-Transaktionen (Rigor-Punkt 36):** Janet P. Froetscher (Director), Verkauf 937 Aktien @ $278,95 am 12.08.2026 unter 10b5-1-Plan — routinemäßig, geplant. Fredric J. Tomczyk (Director), 337 Aktien einbehalten für Steuern (RSU-Vesting) am 01.07.2026 — kein Verkauf am Markt. **Kein klares Signal in beide Richtungen** — ausschließlich geplante 10b5-1-Verkäufe und steuerbedingte Einbehalte, keine ungeplanten Netto-Käufe/-Verkäufe.

**KGV-Verlauf (trailing GAAP, Jahresschlusskurs ÷ EPS, Twelve-Data-Kurse + Company-Releases):** 2021 26,5x → 2023 25,1x → 2024 27,1x → 2025 23,8x → aktuell ~25,9x (auf FY2025-EPS-Basis, TTM-Näherung). 2022 wegen der Goodwill-Impairment-Anomalie ausgelassen (KGV nicht aussagekräftig). **Einordnung:** das aktuelle KGV liegt nahe am historischen 4-Jahres-Durchschnitt (Ø 25,6x) — keine erkennbare Multiple-Expansion oder -Kontraktion. Der Kursrücksetzer vom 15.09. ist damit kein Bewertungs-Reset (die Aktie war weder "billig geworden" noch "teurer geworden" relativ zu ihrer eigenen Historie), sondern reine Kursbewegung innerhalb der etablierten Bewertungsbandbreite.

**DCF-Szenarien im Chart-Kontext:** Der aktuelle Kurs $270,40 liegt knapp über Conans risikoadjustierter Bear-Zone ($240-245) und deutlich unter der Base-Zone ($360-400) — visualisiert auf der neuen Report-Seite 7 zusammen mit dem KGV-Verlauf. Die Bear-Zone fungiert damit als grober struktureller Boden (nicht als hartes Stop-Signal).

---

## 6. Datenintegritäts-Fund

Jacks abschließender JSON-Block enthielt `"going_concern_flag": true` — dies widerspricht seiner eigenen Prosa (kein Going-Concern-Vermerk gefunden) und seinem eigenen Rating KAUFEN (unter einem echten Going-Concern-Flag zwingend SCHROTT). Als Tipp-/Generierungsfehler eingeordnet und in der Synthese auf `false` korrigiert — Beispiel dafür, warum der JSON-Block die Prosa nie ungeprüft ersetzen darf (siehe Methodik, "JSON ersetzt nicht die Begründungspflicht").

---

## 7. Rating-Divergenz und Aegis-Synthese

| | Rating | Sizing |
|---|---|---|
| Jarvis (Jarvis-eigene Analyse, vor Bugfix) | BEOBACHTEN (Technik: unter 200D-SMA, RSI 35,8, MACD bearish, OBV fallend) | Watchlist/Tier 3 |
| Jack | KAUFEN (mechanisch, folgt DCF direkt) | Tier 2 |
| Conan | KAUFEN, gestaffelt (DCF bewusst gedämpft) | Tier 2 (3-5%) |

**Finales Aegis-Verdict: KAUFEN, Ausführung gestaffelt.** Zwei von drei unabhängigen Beinen kommen trotz methodisch vorsichtiger DCF-Behandlung auf KAUFEN, gestützt zusätzlich durch den Peer-EV/EBITDA-Abschlag und den moderat über dem Kurs liegenden Analysten-Konsens. Die kurzfristig schwache Technik (Jarvis' ursprünglicher Vorbehalt) bestimmt bei einer bestehenden Champions-Position nur die Tranchierung des Nachkaufs, nicht die fundamentale KAUFEN/BEOBACHTEN-Grundentscheidung.

**AGENT SCORE: 8/10 · Konfidenz: 🟡 MITTEL** (Beta-/ROIC-Streuung zwischen Quellen, DCF-Modell-Sensitivität bei diesem Beta-Profil).

### Kaufplan (gestaffelt, keine automatische Order)
- **Tranche 1:** bei Stabilisierung über $268-270, Tier 2, ca. 1,5-2% Zielgewicht
- **Tranche 2:** bei $255-262 (technische Zone + zusätzliche Sicherheitsmarge)
- **Technische Bestätigung vor Tranche 1:** RSI-Erholung über 45, MACD-Bodenbildung oder OBV-Trendwechsel (siehe TA-Modul)

### Exit-/Stop-These-Trigger
ROIC <WACC (2Q in Folge) · Moat-Decay bestätigt (inkl. Prediction-Market-Wettbewerb materialisiert sich als echte Volumen-Abwanderung) · Debt-Maturity dreht auf KRITISCH (Januar-2027-Refinanzierung) · Kurs >30% über Base-FV ohne Fundamentalverbesserung · Going-Concern-Flag erscheint neu.

---

## 8. Quellen (Auswahl, real recherchiert von Jack/Conan)

- Cboe Q2 2026 Earnings Release, ir.cboe.com
- Cboe 10-K FY2025 (SEC EDGAR, cboe-20251231.htm), 10-Q Q2 2026 (cboe-20260630.htm)
- Cboe Insights: "Week of 9-14-2026: Macro Uncertainty Fuels Hedging Demand Ahead of FOMC"
- Damodaran ERP (pages.stern.nyu.edu), Stand 01.09.2026: 4,14%
- Yahoo Finance / StockAnalysis.com: Peer-Multiples ICE/CME/NDAQ, Analystenkonsens
- AP News: "US stocks slip after oil prices and the bond market crank up the pressure", 15.09.2026

---

**Nächster Prüfpunkt:** Bei Tranche-1-Ausführung Eintrag in `depot/prediction_ledger.md`. Nächster regulärer [B] These-Check über den täglichen Trigger-Check.
