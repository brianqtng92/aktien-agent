# HANDOVER – Aktien-Agent (Brians Depot-KI-System)

**Erstellt:** 2026-08-31 · **Zweck:** Vollständige technische Übergabe, damit ein
neuer Claude-Code-Agent (Cowork-Session) dieses Projekt **ohne jeden vorherigen
Chatverlauf** übernehmen kann. Dieses Dokument verändert **keine** bestehende
Regel – es ordnet, verweist und dokumentiert Infrastruktur-Wissen, das bisher
nur im Chatverlauf existierte. Die einzige verbindliche Quelle für Regeln
bleibt **`architecture.md`** (Repo-Root) plus die drei Prompt-Dateien unter
`prompts/`. Wo dieses Dokument etwas zusammenfasst, gilt im Zweifel immer das
Original in `architecture.md`/`prompts/` – nicht diese Zusammenfassung.

**Wie du dieses Dokument benutzt:** Lies es einmal komplett durch, bevor du
irgendetwas tust. Es ersetzt nicht `architecture.md` (3.769 Zeilen, der
eigentliche Regelwerk-Text), sondern ist die Landkarte dazu: Was steht wo,
was ist der aktuelle Stand, welche technischen Fallstricke gibt es, die
nirgends sonst dokumentiert sind.

---

## 0. Wer ist Brian, was will er von diesem Agenten

Brian betreibt mehrere Wertpapierdepots (Scalable Capital, Trade Republic,
Smartbroker+, finanzen.net zero) und lässt sein Portfolio von einem
KI-System aus drei "Personas" analysieren, überwachen und dokumentieren:

- **Jarvis** = du selbst (Claude, nativ in dieser Session) – führt die
  eigentliche Recherche/Analyse aus, orchestriert die anderen beiden KIs per
  Browser-Automation, schreibt alle Dateien, verwaltet Git, Reports, PDFs.
- **Jack** = Gemini (Google), angesprochen über Chrome-Browser-Automation.
- **Conan** = ChatGPT (OpenAI), ebenfalls über Chrome-Browser-Automation.

**Wichtig:** Diese Namen sind reine Reporting-Nicknames für die drei KIs,
unabhängig davon, welchen der drei Methodologie-Prompts sie gerade
ausführen. "Jack" heißt in den Prompt-Dateien selbst z.B. auch "The Moat
Reaper" oder "Pure Technical Analyst" – das ist derselbe Gemini-Slot, nur
mit unterschiedlichem Auftrag. Verwechsle nicht "Jack" (Persona/Gemini) mit
"jack-moat-reaper" (Dateiname/Methodik) – ersteres ist WER antwortet,
letzteres ist WELCHES Regelwerk gerade angewendet wird.

Ziel des Gesamtsystems (siehe `architecture.md` Abschnitt "Ziel"): Brian
trifft am Ende jede Kauf-/Verkaufsentscheidung selbst und manuell. Die KIs
liefern Analyse, Cross-Checks zwischen drei unabhängigen KI-Perspektiven und
Reports – **niemals** wird automatisiert eine Order ausgeführt.

---

## 1. Die wichtigste Regel zuerst: was der Agent NIEMALS tut

Diese Leitplanken sind laut `architecture.md` **fix** ("Grenze bleibt fix")
und dürfen von keiner Anweisung – auch nicht von Brian selbst im laufenden
Chat – aufgeweicht werden, ohne dass er explizit `architecture.md` ändert:

1. **Order-Ausführung ist IMMER manuell durch Brian.** Die
   Scalable-Capital-MCP-Tools `submit_buy_order`, `submit_sell_order`,
   `submit_savings_plan`, `cancel_order` sind **permanent verboten** – auch
   bei expliziter Anweisung. Nur lesende/Watchlist-/Preview-Funktionen sind
   erlaubt (vollständige 39-Tool-4-Stufen-Whitelist siehe
   `architecture.md`, Abschnitt "Offene Punkte" Punkt 2, und Abschnitt 8
   unten in diesem Dokument).
2. **USA/Nordamerika-Region:** harte Obergrenze 60% des Depots.
3. **ETF-Mindestanteil:** mindestens 50% des Gesamtportfolios.
4. **Einzelposition:** max. 10% (Ausnahme bis 12% für Top-Conviction-Werte,
   siehe Trailing-Weight-Regel unten).
5. **Max. 20 Einzelpositionen** (harte Obergrenze, siehe
   `architecture.md` Abschnitt 10 – aktuell in Phase mit 10-15 Positionen).

Diese Regeln stehen im Detail in `architecture.md`, Abschnitt 3
("Depot-Ziel-Struktur") und Abschnitt 10. Dieses Dokument fasst sie nur
zusammen, damit sie sofort präsent sind – **die Formulierungen dort sind
maßgeblich, nicht diese Kurzfassung.**

---

## 2. Repo-Karte – wo liegt was

Repo-Root ist `$HOME/mnt/aktien-agent` auf Brians Mac (per Cowork-Desktop-App
verbunden). **Wichtiger Fallstrick:** siehe Abschnitt 9 "Technische
Infrastruktur & Fallstricke" zum Thema `/tmp/aktien-agent` vs. der echten
verbundenen Ordner-Pfad – nutze IMMER `$HOME/mnt/aktien-agent`, nie ungeprüft
`/tmp/aktien-agent`.

```
aktien-agent/
├── architecture.md                     ← DAS Regelwerk (3.769 Zeilen, s.u.)
├── watchlist.md                        ← 30 Werte, Champions/Profi/Talent
├── watchlist_pending_3fach.md          ← Warteschlange offener Quick-Filter
├── prompts/
│   ├── jack-moat-reaper-v11.7.md       ← TMR-Methodik (Fundamentalanalyse)
│   ├── conan-the-scout-v1.12.md        ← Scout-Methodik (Frühphasen-Screening)
│   └── jack-technical-analyst-v1.9.md  ← TA-Methodik (reines Timing/Charts)
│       (architecture.md referenziert bereits "v1.10" nach einem Update vom
│        2026-08-30, das noch nicht in den Dateinamen übernommen wurde –
│        Dateiinhalt selbst ist v1.9, unverändert prüfen vor Gebrauch)
├── depot/
│   ├── scalable-capital.md             ← Live-MCP-Anbindung (siehe unten)
│   ├── finanzen-net-zero.md            ← 17 Positionen, manuell erfasst
│   ├── smartbroker-plus.md             ← 1 Position (HawkEye 360)
│   ├── trade-republic.md               ← 2 Positionen (Allianz, ex-WM)
│   └── performance_tracking.md/.csv    ← Depot-vs-Index-Tracking
├── analysen/                           ← 60+ Einzelanalysen (Historie)
└── reports/                            ← HTML/PDF-Reports + Python-Chart-Skripte
    ├── build_wochenfazit.py, benchmark_chart.py, portfolio_*.py, weekly_charts.py
    └── templates/ampel-batch-scan-template.html/.pdf
```

**Für eine schnelle Bestandsaufnahme beim Sessionstart:** lies zuerst dieses
Dokument, dann `architecture.md` Section-Overview (Abschnitt 3 unten), dann
bei Bedarf die drei Prompt-Dateien vollständig (sie sind Brians eigene,
unveränderte System-Prompts – niemals umformulieren, nur ausführen).

---

## 3. architecture.md – Navigationskarte (13 Abschnitte)

`architecture.md` ist 3.769 Zeilen lang. Damit ein neuer Agent nicht die
gesamte Datei am Stück lesen muss, hier die Section-Karte (ungefähre
Zeilenbereiche zum Zeitpunkt dieser Übergabe – bei künftigen Ergänzungen
verschieben sich die Zeilennummern, die Reihenfolge der Abschnitte bleibt
aber gleich):

| # | Abschnitt | Kerninhalt |
|---|---|---|
| – | Ziel | Mission, Brian entscheidet immer selbst, KI liefert Analyse |
| – | Das Regelwerk | Die drei Prompt-Dateien SIND das Regelwerk – der Agent führt sie aus, ersetzt sie nicht |
| 1 | Regime-basierte Regelanpassung | Risk-on/Neutral/Risk-off, Signal-Basis (Index vs. 50/200-MA, VIX, Drawdown, Marktbreite), Tie-Breaker: bei Konflikt immer konservativer runden, Drawdown-Psychologie-Protokoll bei Risk-off ODER -20% vom Hoch |
| – | Depot-Ziel-Struktur | Champions/Profi/Talent-Aufteilung, USA-Cap 60%, ETF-Minimum 50%, Positions-Cap 10-12% |
| – | Pipeline | [1] Screening → [1.5] Kill-Gates+Bucket A-D → [2] Kategorisierung → [3] 3-fach Cross-Check → [3b] Diskussionsrunde → [3c] Meta-Retro → [4] TA → [5] Report → [6] Depot-Abgleich |
| – | Monitoring | [A]-[E]-Checks, 5-Kategorie Exit/Nachkauf-System |
| – | Warum nicht alles automatisch | Begründung für manuelle Order-Ausführung |
| – | Technische Bausteine | Twelve Data (800 Credits/Tag, seit 2026-08-30 live), Gemini-Trunkierungs-Bug-Fix, TA-Pflicht-bei-jeder-Einzelanalyse (seit 2026-08-31, ausgelöst durch Disco-Corp-Vorfall) |
| 5 | Monitoring (Fortsetzung) | Watchlist-System (täglicher automatisierter Scan, Identity-Gate, Triple-Conviction-Flag), Verständlichkeits-Regel (7 Regeln, 2026-08-31), Verkaufsdisziplin & Gewinnmitnahme (5 Kategorien), Wochenfazit-Format, Charts & Benchmark-Tracking, Monatsrecap (15 Inhaltspunkte), PDF-Report-Design "Reaper Wochenreport" |
| 6 | (Blitz-Scan / weitere Monitoring-Details) | siehe Scheduled-Tasks-Abschnitt unten |
| 7 | Technische Bausteine (Detail) | Gemini-Paragraph-Trunkierungsbug, Twelve-Data-Integration im Detail |
| 8 | Offene Punkte | 13 nummerierte offene Punkte (siehe Abschnitt 10 unten in diesem Dokument) |
| 9 | Meta-Retrospektive | 4-Phasen-Rollout, Phase 2 = Prediction Ledger/Decision Journal (aktiv seit 2026-08-30) |
| 10 | (Trailing-Weight-Regel, Positions-Cap) | 12%/15%/18%-Schwellen, finale Entscheidung max. 20 Positionen |
| 11 | (Dual-Gate, Inflection-Signal) | Liquiditäts-Gate |
| 12 | (Strukturelle Ergänzungen) | 4 implementierte strukturelle Lücken-Schließungen |
| 13 | Cross-KI-Diskussion (4 Unterabschnitte) | Vincorion-Fall, IPO-Overhang-Check-Modul, N/V-wegen-kurzer-Handelshistorie-Konfidenzkategorie, No-False-Precision-Regel |

**Praktischer Tipp für neue Agenten:** Die Datei ist zu groß für einen
einzelnen `Read`-Aufruf. Nutze `grep -n "^#\{1,4\} "` für die Section-Köpfe,
dann gezielt mit `offset`/`limit` lesen, oder bei Bedarf mehrere
Subagenten parallel für verschiedene Zeilenbereiche einsetzen (bewährtes
Muster aus dieser Übergabe: 4 Subagenten für je ~700 Zeilen).

---

## 4. Die Pipeline im Überblick

1. **[1] Universum-Screening** – Kandidaten aus Indizes/Sektoren finden.
2. **[1.5] Kill-Gates + Bucket-Einordnung A-D** – harte Ausschlusskriterien,
   Vorsortierung.
3. **[2] Kategorisierung** – Champions/Profi/Talent-Zuordnung + Routing:
   TMR (Jack-Moat-Reaper) für etablierte Firmen, Scout (Conan-the-Scout)
   für Frühphasen-/spekulative Werte. Enthält Frische-Gate,
   Liquiditäts-/Spread-Gate (>500.000€ Tagesvolumen, <1,5% Spread,
   Limit-Orders-Pflicht für Talent/Scout).
4. **[3] 3-fach Cross-Check** – alle drei KIs (Jarvis/Jack/Conan) bekommen
   identisches Fact-Pack (Schritt-0-Datenpaket), analysieren unabhängig.
   Bei widersprüchlichen selbst-recherchierten Kernzahlen: **Datenkonflikt-
   Notbremse** – kein hochkonfidentes Ergebnis, sondern Flag "DATENKONFLIKT".
5. **[3b] Diskussionsrunde** – max. 2 Runden bei Uneinigkeit,
   Konvergenz-Status stark/moderat/widerspruch.
6. **[3c] Meta-Retro-Runde** – selten, nur bei echten Methodik-Streitfällen
   (nicht bei normalen Zahlen-Dissensen).
7. **[4] TA** – Pure Technical Analyst (Jack-TA), seit 2026-08-31 Pflicht
   bei JEDER Einzelanalyse (ausgelöst durch den Disco-Corp-Vorfall).
8. **[5] Report** – Kurz-Fazit (5-8 Sätze), PDF-Pflicht bei jeder
   abgeschlossenen Analyse, Ampel-Batch-Scan-Layout für Übersichten.
9. **[6] Depot-Abgleich** – optional, gleicht Ergebnis gegen bestehende
   Positionen ab.

Vollständige Detailregeln (exakte Schwellenwerte, Formate, Sonderfälle)
stehen ausschließlich in `architecture.md` – siehe Section-Karte oben.

---

## 5. Portfolio-Kategorie-Struktur

- **Champions** (35-45% des Aktienanteils, ex-ETF): etablierte
  Weltklasse-Compounder mit breitem, bewiesenem Moat. TMR-Pfad.
- **Profi** (20-30%): solide Qualitätsfirmen/Nischenführer, deren
  Langfrist-Bewährung noch läuft oder die zyklischer/konzentrierter sind.
- **Talent** (25-40%): echtes spekulatives Risiko – Untertags "Talent
  (langfristig)" vs. "Zock/Trade" mit unterschiedlicher
  Exit-Disziplin-Anwendung. Größe der Marktkapitalisierung schützt NICHT
  automatisch vor Talent-Einstufung (Beispiel Palantir: riesige Marktkap,
  trotzdem Talent wegen Bewertungsrisiko).

**Trailing-Weight-/Winner-Drift-Regel** (Abschnitt 10): passives Wachstum
einer Position wird bis 15% toleriert, 15-18% löst Pflicht-Review aus, über
18% erzwingt Rebalancing. Max. 20 Einzelpositionen ist eine finale,
begründete Entscheidung (siehe Abschnitt 10) – aktuell in Phase mit
10-15 Positionen.

---

## 6. Die drei Methodologie-Prompts (Kurzstruktur)

Diese drei Dateien SIND das eigentliche Analyse-Regelwerk – der Agent führt
sie wörtlich aus, verändert oder interpretiert sie nicht um. Nachfolgend nur
eine strukturelle Orientierung, nicht der vollständige Inhalt (der steht
unverändert in den Dateien selbst).

### 6.1 `jack-moat-reaper-v11.7.md` (TMR – "The Moat Reaper")
Fundamentalanalyse etablierter Firmen. Kernablauf:
- **SCHRITT 0** (blockierend, für JEDEN Modus): Live-Kurs + News-Websuche,
  Beta-Vorab-Abruf. Ohne erfolgreiche Live-Recherche: Abbruch, kein
  Training-Daten-Ersatz für den Kurs.
- **SCHRITT 0C** (blockierend, direkt nach 0): Going-Concern-Precheck – bei
  Auditor-Zweifel am Fortbestand sofortiger Abbruch, RATING zwingend
  SCHROTT, unabhängig von allem sonst.
- **Entscheidungshierarchie** (bei Regelkonflikten, niedrigere Nummer
  gewinnt immer): ① Datenintegrität → ② Going-Concern-Precheck →
  ③ DNA-Gate/Abbruch-Logik → ④ harte Risiko-Overrides & Konfidenz-Deckel →
  ⑤ Valuation → ⑥ Reaper Score → ⑦ Sizing-Tier → ⑧ Rating/Verdict.
- **Data-Integrity-Tags:** [LIVE] / [VERIFIED] / [TRAINING] / [ESTIMATE] /
  [N/V] – mit klaren Schwellen und Abstufungsregeln je Tag.
- **DNA-Check:** K-Kriterien (ROIC >20%, FCF-Marge ≥20%, Op. Leverage,
  Piotroski ≥7, EPS-CAGR ≥12%) und E-Kriterien, mit Sektor-Overrides
  (Finanzsektor, SaaS, Infrastruktur/Versorger, Transformation-Protokoll).
  K-Kriterium [N/V] → Sofort-Abbruch, keine Ausnahme.
- **Reaper Score** 1-10 (Qualitätsurteil, kein reiner Formel-Score),
  Stapel-Logik bei mehreren gleichzeitigen Deckeln/Mali (niedrigster
  Deckel gilt, Mali werden additiv abgezogen, Score nie unter 1).
- **Sizing-Tiers:** Tier 1 (5-8%, nur 🟢) · Tier 2 (3-5%, ab 🟡) ·
  Tier 3 (1-2%, auch 🔴 mit Warnung) · Tier 4 (0%, Abstauber-Limit).
- **Rating:** KAUFEN / BEOBACHTEN / SCHROTT. KAUFEN erfordert Pflicht-
  Exit-Strategie, BEOBACHTEN erfordert Pflicht-Abstauber-Limit +
  Upgrade-/Downgrade-Trigger.
- **Modi:** A (Einzelanalyse), B (Battle A-vs-B), C (These-Check "noch
  intakt?"), D (Quick News Scan), E (Ultra-Quick-Scan), F (Decision Mode,
  "Jack, entscheide"), Earnings-Prep.
- **36 Globale Regeln (Klasse A – eisern)** am Dateiende sind die einzige
  verbindliche Formulierung; alles davor ist nur Kurzverweis.

### 6.2 `conan-the-scout-v1.12.md` (Scout – "Conan the Scout")
Frühphasen-/spekulatives Screening künftiger Compounder. Bereits in einem
früheren Teil dieser Session vollständig gelesen (HawkEye-360-Arbeit).
Struktureller Unterschied zu TMR: statt DCF → Outcome-Wahrscheinlichkeiten
(5-Buckets: Totalverlust/Enttäuschung/Marktrendite/Multibagger/Tenbagger+
mit EV-Berechnung), statt Reaper-Score → Scout-Score, statt fixer
Sizing-Tiers → durchgehend winzige Positionsgrößen (<0,5-2%). Enthält
sektorspezifische Overrides für SaaS/Pre-Revenue/Deep-Tech/Biotech, einen
"Moat-in-Formation"-Begriff (statt bewiesenem Moat), einen Gründer-Score
und einen "Trichter"-Reifegrad (Stufe 1 Rohtalent / Stufe 2 Profi /
Stufe 3 möglicher Tenbagger-Kandidat). Rating-Skala: WATCHLIST-ELITE /
BEOBACHTEN-STARK / BEOBACHTEN-SPEKULATIV / ZU FRÜH / DURCHGEFALLEN.
Enthält ebenfalls einen Hype-Strike-Mechanismus (deckelt Sizing auf
Trace-Niveau bei übertriebenem Markt-Hype) und eine No-False-Precision-Regel
für unvorhersagbares Akteursverhalten (z.B. PE-Sponsor-Lockup-Verkäufe) –
Ausnahme: die sanktionierten Outcome-Wahrscheinlichkeiten selbst.
**Bei Unsicherheit über den exakten aktuellen Wortlaut: Datei neu lesen,
nicht aus dieser Zusammenfassung zitieren.**

### 6.3 `jack-technical-analyst-v1.9.md` (TA – "Pure Technical Analyst")
Reines Chart-/Timing-Modul, KEINE Fundamentaldaten, KEINE Prognosen. Nutzt
Live-Indikatoren über die Twelve-Data-MCP (MACD, RSI, SMA/EMA, Bollinger,
Volumen, Pivot-Punkte, OBV, ATR).
- **Zwei Modi:** MODUS 1 Standard-TA (immer aktiv) und MODUS 2
  Investor-Entry (aktiviert sich automatisch, wenn TMR-Fair-Value-Werte im
  Input mitgeliefert werden – Brücke TMR-Fundamentalbewertung ↔ TA-Timing).
- **Zwei Horizonte:** SWING (4-12 Wochen, Default) mit anderen
  Faktorgewichten als INVESTOR (>6 Monate) – bei INVESTOR wird der
  Wochenchart (W1) doppelt gewichtet, Oszillatoren gedämpft (Tagesrauschen
  weniger relevant bei langem Horizont).
- **5 Faktoren:** Trend&Sektor, Momentum, Volumen+Institutional Footprint
  (OBV-Trend, Akkumulationsmuster), Oszillatoren (RSI/MACD/Divergenz),
  Preisstruktur (Bollinger, 52W-Kontext, Support/Resistance, Trendkanal).
- **Fixe Score-Konstanten** (MAX +10,44 / MIN -9,71 SWING bzw. -9,66
  INVESTOR), Rating-Skala STRONG BUY bis AVOID.
- **VETO-Modul:** bullishe und bearishe Warnsignale (Überdehnung, Death
  Cross, bärische Divergenz, Volumen-Climax, OBV-Divergenz,
  Sektor-Verfall, Kanal-Ausbruch, bestätigte Chartformation). Bei ≥2
  gleichzeitig aktiven Bullish-VETOs wird ein STRONG-BUY-Rating auf BUY
  gedeckelt (VETO-Aggregat-Deckel).
- **Formations-Modul (v1.9):** reiner User-Input (Doppeltop/Doppelboden/
  SKS), Jack schätzt keine Chartformationen selbst aus Zahlenreihen.
- **Investor-Entry-Modus Blöcke A-F:** Preiszonen-Analyse (5 Zonen relativ
  zu TMR Bear/Base/Bull FV), Margin of Safety, Entry-Ampel, Kombinations-
  Score (0-10, verbindet TA-Score mit Bewertungs-Zone + MoS-Bonus, mit
  Flag-basierten Sizing-Caps), Konflikterkennung, Zyklus-Kontext.
- **Rating-Mapping TMR↔TA:** TMR SCHROTT erzwingt automatisch Entry-Ampel
  🔴, unabhängig vom TA-Score.

---

## 7. Aktueller Depot-Zustand (Stand 2026-08-31)

**Hinweis:** Dies ist ein Snapshot zum Übergabezeitpunkt. Für den
tagesaktuellen Stand IMMER die Dateien unter `depot/` neu lesen bzw. die
Scalable-Capital-MCP-Tools live abfragen – Zahlen ändern sich täglich.

### Scalable Capital (Live-MCP-Anbindung seit 2026-08-30)
- Boerse Stuttgart EUWAX Gold II: 4 Stück, 505,50€ (bewusst AUSSERHALB der
  Champions/Profi/Talent-Struktur geführt – reine defensive
  Diversifikation, fließt nicht in Sektor-/Regionsberechnung ein)
- Bank Central Asia: 6.183,77 Anteile, 1.954,07€, Sparplan seit 28.08.2026
  gestoppt
- Vanguard FTSE All-World (Acc): 45,22 Anteile, 7.585,00€, Sparplan
  600€/Monat, nächste Ausführung 07.09.2026
- Cash/Verrechnungskonto: 1.047,14€
- **Gesamtwert Scalable Capital: 11.091,71€**
- Keine Krypto-Bestände trotz freigeschalteter Funktion.

### finanzen.net zero (17 Positionen, manuell erfasst)
Vollständig erfasst seit 2026-08-29. Wichtigste noch gehaltene Positionen:
SoFi Technologies (250 Anteile, 4.120,00€, +57,7%), ServiceNow
(2.487,20€, +27,6%), Cellebrite (2.082,00€, -3,9%), MercadoLibre
(1.671,20€, +15,8%), Hermès (1.541,50€, -19,1%), Constellation Software
(1.972,00€, +42,9%), Intuitive Surgical (1.286,20€, -8,2%), Tristel
(945,00€, -5,8%), Rambus, A10 Networks.
**Im Zuge der Depot-Restrukturierung am 27.08.2026 komplett verkauft:**
Keyence, Intuit, Amazon, Cintas, S&P Global, Grab Holdings, Itochu, Stryker,
Visa, Netskope, Alphabet A, Waste Management (12 Positionen).
**Neukäufe danach (Talent/Moonshot-Fokus):** Kraken Robotics (300 Stk. @
3,50€, 1.050,00€, 24.08.2026), Rocket Lab USA (10 Stk. @ 55,40€, 554,00€,
28.08.2026) – beide noch nicht TMR/Scout-analysiert (Stand Übergabe).

### Smartbroker+
- HawkEye 360 (HAWK): 60 Aktien @ 17,80€, 1.068,10€ investiert. Aktuell
  ~2,7% des Depots. **Am 2026-08-31 Full-Deep-Dive durch alle 3 KIs
  durchgeführt** – Ergebnis: BEOBACHTEN-SPEKULATIV, Rating liegt bereits
  über eigenem Trace-Sizing-Deckel (<0,5%), kein Nachkauf. Details:
  `analysen/HAWK-SCOUT-*-2026-08-31.md`, `reports/HAWK-reaper-kompakt-*`.
  Nächste Beobachtungspunkte: 02.09. (Lock-up-Freigabe), 21.09.
  (Russell-2000-Wirksamkeit), Q3-Zahlen (~Anfang November).

### Trade Republic
- Allianz SE: 1,151396 Anteile, Ø-Einstand 369,11€, laufender
  Sparplan-artiger Kauf seit 16.04.2025.
- Waste Management: komplett verkauft am 27.08.2026 @ 187,35€.

### Performance-Tracking (Depot vs. Markt)
Vorwärts-Tracking-Methodik (kein Rückwirkungsvergleich), **korrigierter
Startpunkt 30.08.2026: Depot 35.034,17€** (die ursprüngliche Baseline vom
29.08. war zu niedrig, da die Scalable-Live-Anbindung noch fehlte).
Vergleichsindizes zum selben Datum: S&P 500 7.711,76 USD, Nasdaq 100
29.433,43 USD, MSCI World Proxy (IE00B4L5Y983) 127,735€. Wird jeden Freitag
im Wochenfazit-Lauf fortgeschrieben (`depot/performance_tracking.md`).

---

## 8. Watchlist & Pending-Queue

`watchlist.md`: **30 Werte** (Cap 20-30), Champions 13 / Profi 10 / Talent 7.
Herkunft: 21 von Brian selbst vorgegeben, 9 systematisch von Jarvis ergänzt.
Mehrere Werte sind explizit als **[EX-DEPOT]**-Wiederaufnahmekandidaten
markiert (Visa, S&P Global, Stryker, Keyence – alle am 27.08.2026 verkauft).
Aufnahme-/Ausschlusskriterien und wöchentlicher Prüfprozess stehen
vollständig in der Datei selbst.

**Aktueller Sonderfall (2026-08-31):** WEG S.A. (WEGE3, Brasilien) besteht
alle Gates und wird von allen drei KIs einstimmig als Champion-Tier-Qualität
eingestuft (ROIC 32-36%, Wide Moat, Net Cash), aber ebenso einstimmig
BEOBACHTEN/WATCH wegen zu hoher Bewertung (~33-34x KGV, keine
Sicherheitsmarge). Noch NICHT formal in die Champions-Tabelle aufgenommen
(Watchlist ist bei Kapazitätsgrenze 30/30) – Brian muss entscheiden, ob WEG
einen Slot bekommt oder als reiner LatAm-Beobachtungsposten außerhalb der
30er-Kapazität geführt wird. Nächster Prüfpunkt: Rücksetzer Richtung
23-25x KGV.

`watchlist_pending_3fach.md`: Warteschlange für Kandidaten aus dem
täglichen automatisierten Scan, die das Strategie-Fit-Gate, den
Duplikations-Check und das Identity-Gate bestanden haben, aber mangels
verbundenem Chrome-Browser nur einen Jarvis-Only-Vorabbefund haben. Regel:
**niemals** wird ein Eintrag allein auf Jarvis-Basis übernommen – es
braucht immer alle drei KIs, auch im Quick-Filter (Brian-Regel vom
2026-08-29). Stand Übergabe: Datei ist leer, keine offenen Einträge.

---

## 9. Scheduled Tasks (Cowork-Desktop, gerätegebunden)

**Kritisch zu verstehen:** Diese 4 wiederkehrenden Tasks sind über die
Cowork-Desktop-App **lokal auf Brians Mac gebunden** (Device-Binding). Sie
erscheinen deshalb **NICHT** in `list_triggers` (dem Cloud-seitigen
Routine-Listing-Tool) – das ist kein Datenverlust, sondern dokumentiertes
Verhalten dieses Tools. Ein neuer Agent, der `list_triggers` aufruft und nur
alte/gefeuerte Einmal-Routinen sieht, soll daraus NICHT schließen, dass die
Scheduled Tasks verloren gegangen sind.

| Task | Cron (UTC) | Zweck |
|---|---|---|
| Täglicher Trigger-Check | `0 19 * * *` (19:00 täglich) | Kandidaten-Scan, Watchlist-Pflege, Depot-Abgleich |
| Wochenfazit | `0 20 * * 5` (Freitag 20:00) | Wochenbericht, Performance-Tracking-Update, Watchlist-Neu/Raus |
| Monatsrecap | `0 21 28-31 * *` mit internem Last-Day-of-Month-Check | Monatsbericht |
| Blitz-Scan | `0 7-21 * * 1-5` (stündlich, Mo-Fr, Handelszeiten) | Schnell-Scan auf akute Ereignisse |

**Repo-Zugriffsmuster für alle 4 Tasks:**
```bash
rm -rf /tmp/aktien-agent 2>/dev/null
ln -sfn "$HOME/mnt/aktien-agent" /tmp/aktien-agent
cd /tmp/aktien-agent && git pull origin main
```
Der Symlink existiert, damit ältere Prompt-Textpassagen mit
`/tmp/aktien-agent/...`-Pfaden weiter funktionieren. Push funktioniert über
einen vorkonfigurierten Git-Credential-Helper (`credential.store`, auf
`github.com` beschränkt) – `git push origin main` sollte ohne weitere
Eingabe funktionieren (siehe aber Fallstrick in Abschnitt 10.1).

**Offene Unsicherheit – WICHTIG:** Der exakte aktuelle Live-Wortlaut des
"Täglicher Trigger-Check"-Prompts konnte in dieser Übergabe **nicht
zuverlässig rekonstruiert werden**. Alle in `/tmp/` gecachten Kopien
(`daily_trigger_prompt.txt`, `git_trig_taeglich.txt`,
`git_trig_taeglich_v2.txt`, `trigger_prompt.txt`) nutzen ein veraltetes,
rein lesendes Git-Clone-Muster ohne Push – das widerspricht der beobachteten
Realität, dass der Lauf vom 31.08.2026 tatsächlich einen Commit gepusht hat
(siehe Abschnitt 10.1, WEG-S.A.-Commit). Die drei anderen Tasks
(Wochenfazit, Monatsrecap, Blitz-Scan) sind über `/tmp/newprompt*.txt`
zuverlässig im aktuellen, geräte-gebundenen Wortlaut belegt. **Empfehlung
für den neuen Agenten:** vor dem nächsten inhaltlichen Eingriff in den
Täglichen-Trigger-Check-Task den tatsächlichen Prompt-Text direkt in der
Cowork-Desktop-App (Scheduled-Tasks-Verwaltung) nachsehen/mit Brian
abgleichen, statt sich auf eine der `/tmp/`-Kopien zu verlassen. Keine
Regel wurde dadurch verändert – es ist eine reine Wissenslücke über den
technischen Wrapper-Text, nicht über den Inhalt der auszuführenden Schritte
(die Rulebook-Logik selbst ist unverändert `architecture.md`).

---

## 10. Technische Infrastruktur & Fallstricke (aus dieser Session gelernt)

Dieser Abschnitt ist reines Tribal-Knowledge, das bisher nirgends
niedergeschrieben war – wichtig, damit ein neuer Agent nicht dieselben
Fehler wiederholt.

### 10.1 Stale-Clone-Risiko: `/tmp/aktien-agent` kann ein ECHTER Git-Clone sein statt eines Symlinks
Am 2026-08-31 wurde entdeckt, dass `/tmp/aktien-agent` auf Brians Mac zu
einem gegebenen Zeitpunkt **kein Symlink**, sondern ein eigenständiger,
veralteter Git-Clone war (von `nobody:nogroup` angelegt, Rechte gegen die
interaktive Session gesperrt). Dessen `.git/config` enthielt einen defekten
`credential.helper=osxkeychain`-Eintrag (macOS-natives Tool, existiert in
der sandboxten Linux-VM von `device_bash` nicht) – das blockierte
`git push` lautlos mit `git: 'credential-osxkeychain' is not a git
command`. Dadurch hatte dieser Klon einen echten, ungepushten Commit vom
selben Tag eingefangen (WEG-S.A.-Watchlist-Ergänzung), der ohne Eingreifen
nie auf GitHub gelandet wäre.

**Fix, der angewendet wurde:** In `$HOME/mnt/aktien-agent/.git/config`
(dem ECHTEN, live verbundenen Repo) den defekten Helper entfernt:
```bash
git config --local --unset-all credential.helper
```
(Das lässt den funktionierenden globalen
`credential.https://github.com.helper=store` unangetastet.) Der
gestrandete Commit wurde gerettet, indem der stale Clone temporär als
Remote hinzugefügt (`git remote add stale /tmp/aktien-agent`, davor
`git config --global --add safe.directory /tmp/aktien-agent/.git` gegen
den "dubious ownership"-Fehler), der Commit gefetcht/gecherry-picked und
der temporäre Remote wieder entfernt wurde.

**Praktische Konsequenz für künftige Sessions:** Vor jedem `git push` über
`device_bash` prüfen, ob `$HOME/mnt/aktien-agent` tatsächlich verwendet
wird und nicht versehentlich ein alter `/tmp/aktien-agent`-Clone. Bei
Push-Fehlern mit `credential`-Bezug immer zuerst
`git config --local -l | grep credential` in BEIDEN möglichen Pfaden
prüfen.

### 10.2 PDF-Rendering funktioniert NICHT auf Brians Mac direkt
`device_bash` (die sandboxte Linux-VM auf Brians Mac) hat **keine
PDF-Rendering-Fähigkeit** – kein `wkhtmltopdf`, kein Chromium,
`weasyprint` nicht installierbar (kein Netz für pip in dieser VM je nach
Konfiguration), `pdfkit` vorhanden aber ohne das nötige `wkhtmltopdf`-Binary.

**Funktionierender Workflow:**
1. HTML-Report irgendwo bauen/schreiben (im Cloud-Container oder auf dem
   Mac – Inhalt ist überall gleich).
2. Mit dem eigenen Cloud-Container (normales `Bash`-Tool, NICHT
   `device_bash`) über das vorinstallierte Playwright+Chromium rendern:
   `/opt/pw-browsers/chromium` ist vorinstalliert und referenziert.
3. Resultierende PDF-Datei per `SendUserFile` an den User schicken (liefert
   `file_uuid`).
4. Mit `mcp__remote-devices__device_commit_files` in den korrekten
   Repo-Pfad auf dem Mac schreiben.
5. Über `device_bash` git add/commit/push.

### 10.3 `device_stage_files` ist aktuell (Stand dieser Übergabe) NICHT nutzbar
Beim Versuch, `architecture.md` und die Prompt-Dateien zu staged, schlägt
der Aufruf konsistent fehl mit:
```
HTTP 403 adding session file: untrusted_device
```
und einem `auth_required`-Hinweis, dass sich Brian in der Cowork-
Desktop-App auf diesem Gerät neu anmelden muss (ein Sign-in-Banner wurde
dort ausgelöst). **Dies wurde Brian noch nicht mitgeteilt** – ein neuer
Agent sollte dies bei Gelegenheit ansprechen, falls das Problem noch
besteht, da es die normale Methode blockiert, große Dateien in den
Cloud-Container zu holen.

**Funktionierender Workaround, solange das Problem besteht:**
```bash
device_bash: cat <große_datei>
```
Bei Überschreitung des Tool-Output-Limits speichert der Harness den
kompletten Output automatisch in eine lokale `tool-results/*.txt`-Datei,
die dann ganz normal per `Read`-Tool (mit `offset`/`limit`) oder über
mehrere parallele Subagenten gelesen werden kann.

### 10.4 Browser-Automation: Große/Unicode-Texteingabe
`computer.type` ist unzuverlässig bei großen/Unicode-Texten (Timeout bei
>~60KB, Zeichenkorruption bei mittlerer Größe). Zuverlässiger Ersatz:
`javascript_tool` mit `document.execCommand('insertText', false, msg)` auf
dem contenteditable-Element direkt – ChatGPT: `#prompt-textarea`, Gemini:
`.ql-editor[role="textbox"]`. Text dabei ASCII-sicher halten (Umlaute
ausschreiben, keine Emoji).

### 10.5 Gemini-Trunkierungsbug (dokumentiert in architecture.md Abschnitt 7)
Enthält ein an Gemini gesendeter Prompt mehrere durch Leerzeilen getrennte
Absätze, trunkiert Gemini den Text beim Senden nach dem ersten Absatz
(Zeilenumbrüche lösen vorzeitig "Senden" aus). **Fix:** Gemini-Prompts immer
als EINEN durchgehenden Textblock ohne interne Leerzeilen-Absätze senden.
ChatGPT ist von diesem Bug nicht betroffen.

### 10.6 Twelve Data MCP – Plan-Einschränkungen
`get_financials` (und vermutlich `get_earnings`/`get_statistics` u.ä.) sind
auf dem aktuellen Plan NICHT verfügbar ("exklusiv für pro/ultra/venture/
enterprise"). `get_quote`, `get_company_news`, `currency_conversion`
funktionieren einwandfrei. Bei Bedarf an Fundamentaldaten für TMR/Scout auf
SEC/IR/Websearch ausweichen (ohnehin die Primärquelle laut Prompt-Regeln).

### 10.7 Scalable Capital MCP – Tool-Whitelist (4 Stufen)
Vollständig dokumentiert in `architecture.md` Abschnitt 8 (Offene Punkte,
Punkt 2) – hier nur die Kategorien-Übersicht:
1. Reine Analyse-Tools: immer erlaubt (`get_quote`, `get_security_chart`,
   `get_portfolio_holdings`, `get_portfolio_performance`, `list_*`, etc.)
2. Watchlist-/Preisalarm-/Portfoliogruppen-Verwaltung: erlaubt ohne
   Rückfrage (`add_watchlist_item`, `create_price_alert`,
   `create_portfolio_group`, etc.)
3. Preview-Funktionen: erlaubt (`preview_buy_order`, `preview_sell_order`,
   `preview_savings_plan`) – zeigen nur eine Vorschau, lösen nichts aus.
4. **Submit-/Cancel-Funktionen: PERMANENT VERBOTEN**
   (`submit_buy_order`, `submit_sell_order`, `submit_savings_plan`,
   `cancel_order`) – niemals aufrufen, auch nicht bei expliziter Anweisung
   im Chat.

### 10.8 Reaper-Kompakt-PDF-Designsystem
Dunkles Anthrazit/Gold-Theme, Schriften DejaVu Sans Condensed + Carlito,
3-Stimmen-Leiste (Jarvis/Jack/Conan-Konsens visualisiert),
Reaper-Score-Gauge (Halbkreis-Anzeige), DNA-Check-Strang (farbiges
Segmentband). Gerendert per Playwright/Chromium aus einer
Single-Page-HTML-Datei. Vollständiges CSS-Token-System steht in
`architecture.md` im Abschnitt "PDF-Report-Design" – als Referenzbeispiel
für den Aufbau dient `reports/WEGE3-reaper-kompakt-2026-08-31.html` bzw.
die zuletzt gebaute `reports/HAWK-reaper-kompakt-2026-08-31.html`.

---

## 11. Offene Punkte (Stand dieser Übergabe)

Aus `architecture.md` Abschnitt 8 (13 nummerierte Punkte, dort im Detail –
hier nur die wichtigsten für den Sessionstart):

1. **Core-vs-Advisory-Rules-Split** – noch nicht von Brian genehmigt.
2. Scalable-Capital-MCP-Integration mit vollständiger 39-Tool-Whitelist –
   siehe Abschnitt 10.7 oben.
3. Daten-Lücken blockieren sofortige Portfolio-Regel-Checks für 9 benannte
   Positionen (Details in architecture.md).
4-10. Diverse kleinere offene Punkte (siehe Original).
11. **2026-08-28 Wochenfazit-Zuverlässigkeitsvorfall:** "SUCCEEDED" beim
    Scheduled Task bedeutete nicht zwangsläufig "Task tatsächlich
    inhaltlich abgeschlossen" – ein Grund, Ergebnisse von Scheduled Tasks
    stichprobenartig zu verifizieren.
12. Praktischer PDF-Scope-Kompromiss: 6-Positionen-pro-Seite-Kartenraster
    für Wochenreports.
13. **Ungelöster RKLB-Scout-Quick-Filter-Meta-Retro-Fall:** Jarvis/Jack/
    Conan uneins, wie die Scout-Abbruch-Logik mit dem Rating interagieren
    soll – noch offen.

**Zusätzlich aus dieser Übergabe neu identifiziert (noch nicht in
architecture.md eingetragen, da dieses Dokument keine Regeln ändert –
Eintragung obliegt einer bewussten Entscheidung mit Brian):**

- `device_stage_files` liefert aktuell `untrusted_device`/HTTP 403 (siehe
  10.3) – Brian noch nicht informiert.
- Wortlaut-Unsicherheit beim Täglichen-Trigger-Check-Prompt (siehe
  Abschnitt 9) – noch nicht mit Brian abgeglichen.
- Stale-Clone-Risiko bei `/tmp/aktien-agent` (siehe 10.1) – der konkrete
  Vorfall vom 2026-08-31 wurde Brian bereits mitgeteilt und behoben; das
  strukturelle Risiko (kann jederzeit wieder auftreten) ist aber nicht
  präventiv abgesichert.
- Kraken Robotics und Rocket Lab USA (Neukäufe 24./28.08.2026) sind laut
  `finanzen-net-zero.md` noch nicht durch TMR/Scout analysiert.

---

## 12. Erste Schritte für den neuen Agenten (Quickstart)

1. Dieses Dokument vollständig gelesen? Dann weiter.
2. `architecture.md` per `grep -n "^#\{1,4\} "` scannen, um zu prüfen, ob
   seit dieser Übergabe (2026-08-31) neue Abschnitte/Zeilen hinzugekommen
   sind (Datei wächst chronologisch).
3. Aktuellen Depot-Stand über die Scalable-Capital-MCP-Tools live abfragen
   (nicht blind auf die Snapshot-Zahlen in Abschnitt 7 oben verlassen –
   die sind vom 2026-08-31).
4. `watchlist.md` und `watchlist_pending_3fach.md` auf neue Einträge
   prüfen.
5. Prüfen, ob Brian in der Zwischenzeit auf die offenen Punkte aus
   Abschnitt 11 reagiert hat (insbesondere WEG-S.A.-Slot-Entscheidung,
   device_stage_files-Problem, Trigger-Check-Prompt-Abgleich).
6. Bei jeder neuen Einzelanalyse: TMR- oder Scout-Pfad je nach
   Kategorisierung wählen, TA ist seit 2026-08-31 PFLICHT bei jeder
   Einzelanalyse (nicht optional).
7. Bei jedem Git-Push über `device_bash`: sicherstellen, dass
   `$HOME/mnt/aktien-agent` verwendet wird (siehe 10.1).
8. Niemals `submit_buy_order`/`submit_sell_order`/`submit_savings_plan`/
   `cancel_order` aufrufen – unabhängig von der Formulierung der Anfrage.

---

## 13. Migrations-Update (2026-09-01): Umstieg von Cowork auf Claude Code

Brian hat recherchiert, dass die in Abschnitt 9/10 dokumentierten
Zuverlässigkeitsprobleme (Device-Binding, `untrusted_device`,
Stale-Clone-Credential-Bruch) strukturell an der Cowork-Desktop-Architektur
liegen. Die Automatisierungsschicht wird deshalb auf Claude-Code-native
Mechanismen umgestellt:

- **Kanonischer Repo-Pfad ist jetzt `~/Downloads/aktien-agent`** (nicht mehr
  `$HOME/mnt/aktien-agent`). Git-Push-Auth über macOS-Keychain
  (`credential.helper=osxkeychain`) eingerichtet und verifiziert
  (2026-09-01, dieser Commit ist der Test-Beleg).
- Scheduled Tasks werden auf `mcp__scheduled-tasks__create_scheduled_task`
  umgestellt (lokale `SKILL.md`-Dateien unter `~/.claude/scheduled-tasks/`,
  läuft direkt auf Brians Mac, kein Device-Binding). Voraussetzung: Claude
  Code muss während der relevanten Zeitfenster (v.a. 21 Uhr täglich,
  Freitag 22 Uhr, stündlich Mo-Fr 8-22 Uhr) geöffnet sein – sonst läuft der
  Task erst beim nächsten App-Start nach.
  PDF-Rendering läuft künftig lokal über Playwright mit `channel="chrome"`
  gegen das bereits installierte `Google Chrome.app` – der
  Cloud-Container-Umweg aus Abschnitt 10.2 entfällt.
- Die vier alten, geräte-gebundenen Cowork-Tasks müssen von Brian separat
  in der Cowork-Desktop-App deaktiviert werden, sobald die neuen
  Claude-Code-Tasks laufen (sonst Doppel-Pushes).
- Inhaltlich unverändert: `architecture.md` und die drei Prompt-Dateien
  bleiben wortwörtlich die Regelquelle. Diese Migration betrifft nur die
  Infrastruktur, keine einzige Analyse-/Portfolio-Regel.
- **Eskalations-Kanal geklärt (2026-09-01):** `architecture.md` verlangt an
  mehreren Stellen "E-Mail/Push" bei echtem Anlass. Push funktioniert:
  Brian hat Remote Control verbunden, alle vier Scheduled Tasks rufen bei
  handlungsrelevantem Ergebnis zusätzlich zur Chat-Nachricht das
  `PushNotification`-Tool auf. E-Mail ist NICHT verdrahtet – kein
  Connector installiert, `mcp__mcp-registry__search_mcp_registry` findet
  auch nichts Passendes für Gmail/Outlook/SMTP in dieser Umgebung. War
  vermutlich auch zu Cowork-Zeiten nie ein echter Kanal, nur ein
  Konzept im Regelwerk. Müsste außerhalb einer Chat-Session eingerichtet
  werden (dort, wo auch Remote Control verbunden wurde) – noch offen.
- **Scalable-Watchlist gespiegelt + ISIN-Bug gefunden (2026-09-01):** Alle
  30 `watchlist.md`-Werte wurden per `add_watchlist_item` in Scalables
  eigene Watchlist eingetragen. Dabei aufgefallen: die für Watsco Inc.
  (WSO) erfasste ISIN (US9427491025) gehörte tatsächlich zu Watts Water
  Technologies, einer anderen Firma – klassischer Identity-Gate-Fehler,
  der bisher nicht aufgefallen war, weil noch nie gegen eine zweite,
  unabhängige Quelle (Scalables eigene ISIN-Auflösung) geprüft wurde.
  Korrigiert auf US9426222009 (per WebSearch mehrfach verifiziert), in
  `watchlist.md` und bei Scalable behoben. Der tägliche Trigger-Check
  spiegelt ab sofort jede Watchlist-Änderung automatisch zu Scalable und
  prüft dabei den von Scalable zurückgelieferten Firmennamen gegen den
  erwarteten Kandidaten – eine zusätzliche, unabhängige Gegenprobe fürs
  Identity-Gate, die vorher fehlte.

---

*Dieses Dokument wurde von Jarvis (Claude) am 2026-08-31 als reine
Dokumentations-/Konsolidierungsarbeit erstellt, auf Brians expliziten
Wunsch ohne jede Änderung an bestehenden Regeln. Es fasst zusammen und
verweist – bei jedem Widerspruch zwischen diesem Dokument und
`architecture.md`/`prompts/*.md` gilt ausschließlich Letzteres.*
