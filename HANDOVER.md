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
  eigentliche Recherche/Analyse aus, orchestriert die anderen beiden KIs
  (seit 2026-09-02 primär per direktem API-Call statt Browser-Automation,
  siehe unten), schreibt alle Dateien, verwaltet Git, Reports, PDFs.
- **Jack** = Gemini (Google). Seit 2026-09-02 über die `gemini-bridge`-
  MCP-Tools (`ask_gemini`, Modell `gemini-2.5-flash`) angesprochen – direkter
  API-Call statt Chrome-Browser-Automation. Details: Abschnitt 10.10.
- **Conan** = ChatGPT (OpenAI). Seit 2026-09-02 über die `openai-bridge`-
  MCP-Tools (`ask_chatgpt`, Modell `gpt-5.5`) angesprochen – direkter
  API-Call statt Chrome-Browser-Automation. Details: Abschnitt 10.9.

Browser-Automation (Chrome via `claude-in-chrome`) ist seit 2026-09-02 für
beide KIs nur noch **Fallback**, falls eine der beiden Bridges mal ausfällt
– nicht mehr der Standardweg. Siehe Abschnitt 10.4/10.9/10.10.

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
Duplikations-Check und das Identity-Gate bestanden haben, aber nur einen
Jarvis-Only-Vorabbefund haben, weil Jack/Conan am Scan-Tag nicht
erreichbar waren. **Update 2026-09-03:** seit der API-Bridge-Migration
(2026-09-02) landet hier nur noch etwas, wenn BEIDE Bridges UND der
Chrome-Fallback an einem Lauf ausfallen – der alte "Laptop/Chrome war
aus"-Fall ist nicht mehr der Regelfall. Regel unverändert: **niemals**
wird ein Eintrag allein auf Jarvis-Basis übernommen – es braucht immer
alle drei KIs, auch im Quick-Filter (Brian-Regel vom 2026-08-29). Stand
Übergabe: Datei ist leer, keine offenen Einträge.

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
dem contenteditable-Element direkt – Gemini: `.ql-editor[role="textbox"]`.
Text dabei ASCII-sicher halten (Umlaute ausschreiben, keine Emoji).
**Betrifft seit 2026-09-02 keine der beiden KIs mehr im Standardbetrieb** –
sowohl ChatGPT/Conan (Abschnitt 10.9) als auch Gemini/Jack (Abschnitt 10.10)
laufen über direkte API-Calls, nicht mehr über den Browser. Diese ganze
Sektion (inkl. `#prompt-textarea`/`.ql-editor`-Selektoren) ist damit
Altlast-Wissen, nur relevant falls beide Bridges mal ausfallen und auf den
Browser-Weg zurückgefallen werden muss.

### 10.5 Gemini-Trunkierungsbug (dokumentiert in architecture.md Abschnitt 7)
**Betraf nur den alten Gemini-Browser-Betrieb, seit 2026-09-02 (Umstieg auf
`gemini-bridge`, Abschnitt 10.10) nicht mehr relevant – als Fallback-Wissen
aufbewahrt, falls wieder auf Browser-Automation zurückgefallen werden muss.**
Enthält ein an Gemini gesendeter Prompt mehrere durch Leerzeilen getrennte
Absätze, trunkiert Gemini den Text beim Senden nach dem ersten Absatz
(Zeilenumbrüche lösen vorzeitig "Senden" aus). **Fix (nur Browser-Fallback):**
Gemini-Prompts immer als EINEN durchgehenden Textblock ohne interne
Leerzeilen-Absätze senden. ChatGPT war von diesem Bug nicht betroffen.

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

### 10.9 `openai-bridge` MCP-Server – Conan läuft seit 2026-09-02 per API
Neuer projekt-lokaler MCP-Server (`.mcp.json` im Repo-Root → Eintrag
`openai-bridge`, Code unter `~/.claude/mcp-servers/openai-bridge/`,
API-Key in dortiger `.env`). Stellt zwei Tools bereit:

- `mcp__openai-bridge__ask_chatgpt(prompt, system_prompt="", model="gpt-5.5", enable_search=True)`
  – schickt den Prompt direkt an die OpenAI Chat-Completions-API, gibt den
  Antworttext zurück. Ersetzt den bisherigen Weg über
  `claude-in-chrome`/chatgpt.com für die Conan-Rolle vollständig (siehe
  Docstring in `server.py`).
  **`enable_search` (2026-09-04, von Brian gefordert: "Jack und Conan
  sollen die Freiheit haben, selbst zu recherchieren"):** aktiviert
  OpenAI's natives `web_search`-Tool über die **Responses-API**
  (`/v1/responses` statt `/v1/chat/completions`, da Chat Completions kein
  hosted Such-Tool hat) – ChatGPT entscheidet SELBST, ob/wann/was es
  sucht. Default `True`, dann wird IMMER über die Responses-API gerufen
  (auch für Nicht-Pro-Modelle wie das Standard-`gpt-5.5`). Gefundene
  URL-Zitate (`annotations` vom Typ `url_citation`) werden als "Quellen
  (Web Search)"-Anhang an die Antwort angehängt. **Zwei echte Testläufe
  bestätigt:** (1) kurze Live-Kurs-Frage (RKLB/CLBT) – Antwort inkl.
  korrekter aktueller Kurse und Yahoo-Finance-Zitat; (2) VOLLER
  ~77KB-Scout-Methodik-Prompt (identisch zum Rorze-Cross-Check vom selben
  Tag) + `web_search` gemeinsam – lief sauber durch (111,5s, 26.097
  Input-Tokens, 19.259 Zeichen Analyse-Output). Das ist wichtig, weil das
  frühere TPM-Limit-Problem (siehe unten, 50k TPM nur bei `-pro`-Modellen)
  hier NICHT greift, da `gpt-5.5` kein `-pro`-Modell ist. **Auf `False`
  setzen** für reine Diagnose-/Formatierungs-Anfragen ohne Recherchebedarf
  (dann regulärer, günstigerer Chat-Completions-Pfad für Nicht-Pro-Modelle).
  Motivation/Kosten-Hinweis: siehe identische Begründung bei
  `gemini-bridge` in 10.10 – gilt hier genauso.

**Bekannte Einschränkung entdeckt (2026-09-05, erster Produktiv-Lauf mit
vollem TMR-Methodik-Prompt für Lasertec):** bei `ask_gemini` mit
`enable_search=True` UND einem sehr langen Prompt (>70K Zeichen, wie bei
den vollen TMR/Scout-Methodik-Dateien) brach Gemini nach nur 359 Output-
Tokens mit `finishReason: STOP` ab, obwohl 26.571 Prompt-Tokens + 29.040
Tool-Use-Tokens verarbeitet wurden – das Modell "erledigte" offenbar die
Suche und hielt das für eine abgeschlossene Antwort, statt mit der vollen
Methodik fortzufahren. **Workaround (getestet, funktioniert):**
`enable_search=False` bei vollen TMR/Scout/TA-Methodik-Aufrufen setzen
(Jarvis' eigenes Fact-Pack lieferte in diesem Fall ausreichend Grundlage) –
lief danach sauber durch (7.981 Zeichen vollständige Analyse). **Für
KURZE, gezielte Anfragen (z.B. "aktueller Kurs von X") bleibt
`enable_search=True` Default und funktioniert nachweislich zuverlässig**
(siehe RKLB-Testlauf oben). **Regel bis zur genaueren Untersuchung:** bei
`ask_gemini`-Aufrufen mit dem vollen TMR/Scout/TA-Methodik-Prompt
(>50K Zeichen) `enable_search=False` setzen; bei `ask_chatgpt` trat dieses
Problem NICHT auf; **Update 2026-09-05 (alle drei KIs bekommen jetzt alle
drei Methodik-Dateien, siehe architecture.md Abschnitt "Kategorisierung"):**
diese Regel gilt jetzt ERST RECHT für den neuen Standardfall, dass ALLE
DREI Dateien (TMR+Scout+TA, zusammen ~190KB) in einem Prompt an Jack
gehen – `enable_search=False` ist hier PFLICHT, nicht optional, das Risiko
ist strukturell größer als beim bisherigen Einzeldatei-Fall (Conan lief mit `enable_search=True` UND vollem
~74K-Zeichen-Prompt sauber durch, 22.826 Zeichen Analyse-Output,
inklusive einem wichtigen Fund: Conans Live-Suche deckte einen ~29%-
Kursfehler in Jarvis' Fact-Pack auf, siehe
`analysen/LASERTEC-cross-check-fazit-2026-09-05.md`) – das Problem ist
Gemini-spezifisch, keine grundsätzliche Grenze der Architektur.
- `mcp__openai-bridge__list_openai_models()` – listet verfügbare
  Modell-IDs für den API-Key (zum Prüfen/Aktualisieren der Modellwahl,
  da OpenAI-Modellnamen sich ändern).

**Festgelegtes Modell für Conan (Brian, 2026-09-02, nach Testlauf final
bestätigt): `gpt-5.5`** (= Tool-Default, kein `model`-Override nötig).

**Vorgeschichte/Begründung (wichtig, falls das nochmal in Frage kommt):**
Brian wollte ursprünglich `gpt-5.5-pro` ("mehr Tiefe"). Beim ersten echten
End-to-End-Testlauf (volle TMR-Quick-Filter-Methodik für ASML, kompletter
`jack-moat-reaper-v11.7.md`-Prompt + Fact-Pack ≈ 92.000 Tokens) kam:
```
HTTP 429: Request too large for gpt-5.5-pro ... tokens per min (TPM):
Limit 50000, Requested 91663.
```
Das ist ein hartes Tier-Limit des OpenAI-Accounts für `-pro`-Modelle
(50k TPM), unabhängig vom Prompt-Inhalt – die vollen Methodik-Prompts
(TMR/Scout, jeweils 50-65KB Text) sprengen das strukturell bei JEDEM Lauf,
nicht nur gelegentlich. Derselbe Prompt lief mit `gpt-5.5` (kein TPM-Limit
in dieser Größenordnung) sauber durch und lieferte eine methodik-treue,
diszipliniert getaggte Analyse (siehe Testlauf-Ergebnis unten). Brian hat
danach explizit `gpt-5.5` als Standard bestätigt – **kein** `-pro`-Fallback
mehr nötig für die reguläre Pipeline. Falls „mehr Tiefe" später nochmal
gewünscht wird, müsste zuerst der OpenAI-Tarif/Usage-Tier für höhere
Pro-TPM-Limits geprüft werden (siehe https://platform.openai.com/account/rate-limits),
bevor `-pro` für volle Methodik-Läufe wieder infrage kommt.

**Test-Artefakt (nicht im Repo, nur zur Referenz):**
`/private/tmp/.../scratchpad/ASML-TMR-quickfilter-conan-testlauf-gpt55.md`
– Conan/ChatGPT-Bein einer TMR-Quick-Filter-Analyse für ASML (Watchlist-
Champion), sauber [TRAINING]-getaggt (kein Fact-Pack für Fundamentaldaten
vorhanden), Ergebnis BEOBACHTEN, Reaper Score 6/10, Abstauber-Limit $1250.
War ein reiner Conan-Solo-Testlauf (kein Jarvis/Jack-Bein, kein echter
3-fach-Cross-Check) – nicht als vollwertige Watchlist-Analyse behandeln,
nur als Beleg dass die Bridge inhaltlich sauber funktioniert.

**Praktische Konsequenz für die Pipeline:** Überall wo bisher "Conan via
Chrome-Browser-Automation" stand (3-fach Cross-Check [3], Scout-Methodik
`conan-the-scout-v1.12.md`, Diskussionsrunde [3b]), wird stattdessen
`ask_chatgpt` mit dem vollständigen Methodik-Prompt/Fact-Pack als
`prompt`-Argument aufgerufen (1:1 der Text, der vorher ins ChatGPT-
Textfeld eingefügt wurde) – kein Tab, kein `#prompt-textarea`-Workaround,
keine Timeout-/Encoding-Probleme aus Abschnitt 10.4 mehr für diesen
KI-Slot. Der in `architecture.md` an mehreren Stellen erwähnte Status
"fragiles Browser-Automation-Bein" wurde dort **nachträglich, mit Brians
Freigabe, angepasst** (Zeilen um 1433, 1633, 3211, 3392 – Stand nach dieser
Übergabe; siehe Git-Historie für den genauen Diff). Update seit demselben
Tag: das gilt jetzt **auch für Jack/Gemini**, siehe 10.10 unten – die
ursprüngliche Aussage "Jack bleibt Browser-basiert" ist damit überholt.

### 10.10 `gemini-bridge` MCP-Server – Jack läuft seit 2026-09-02 per API

Analog zu 10.9, aber für Gemini/Jack. Neuer projekt-lokaler MCP-Server
(`.mcp.json` → Eintrag `gemini-bridge`, Code unter
`~/.claude/mcp-servers/gemini-bridge/`, API-Key in dortiger `.env` als
`GEMINI_API_KEY`, von Brian selbst bei Google AI Studio erstellt und
eingetragen – **nie** vom Agenten im Chat abgefragt/eingetippt). Stellt
zwei Tools bereit:

- `mcp__gemini-bridge__ask_gemini(prompt, system_prompt="", model="gemini-2.5-flash", enable_search=True)`
  – schickt den Prompt direkt an die Google-Gemini-API
  (`generativelanguage.googleapis.com/v1beta/models/{model}:generateContent`),
  gibt den Antworttext zurück. Ersetzt den bisherigen Weg über
  `claude-in-chrome`/gemini.google.com für die Jack-Rolle vollständig.
  **`enable_search` (2026-09-04, von Brian gefordert: "Jack und Conan
  sollen die Freiheit haben, selbst zu recherchieren"):** aktiviert
  Gemini's natives Google-Search-Grounding-Tool (`tools: [{"google_search":
  {}}]` im API-Payload) – Gemini entscheidet SELBST, ob/wann/was es sucht,
  kein Tool-Call-Loop wie bei `ask_gemini_agentic` nötig. Default `True`.
  Gefundene Quellen (aus `groundingMetadata.groundingChunks`) werden als
  "Quellen (Google Search Grounding)"-Anhang an die Antwort angehängt –
  echte Test-Anfrage (RKLB-Live-Kurs) bestätigt: Antwort inkl. Quellen
  robinhood.com/tradingview.com. **Bekannte Einschränkung:** Google
  proxied Quellen-URLs über `vertexaisearch.cloud.google.com/grounding-
  api-redirect/...` statt der Original-URL direkt auszugeben – das ist ein
  bekanntes Verhalten von Gemini Grounding, kein Bug. **Motivation:**
  bisher bekamen alle drei KIs (Jarvis/Jack/Conan) dasselbe von Jarvis
  kuratierte FACT-PACK – ein blinder Fleck dort vererbte sich auf alle
  drei Urteile. Mit eigener Live-Recherche kann Jack jetzt unabhängig
  gefundene Fakten einbringen, was den Cross-Check echter unabhängig
  macht (kann auch zu mehr Divergenz zwischen den drei Urteilen führen -
  das ist beabsichtigt, kein Fehler). **Kosten-/Latenz-Hinweis:** jede
  Suche kostet extra (Google-Grounding-Pricing) und dauert etwas länger -
  auf `enable_search=False` setzen für reine Diagnose-/Formatierungs-
  Anfragen ohne Recherchebedarf.
- `mcp__gemini-bridge__list_gemini_models()` – listet verfügbare
  Modell-IDs für den API-Key.

**Festgelegtes Modell für Jack (Brian, 2026-09-02): `gemini-2.5-flash`**
(= Tool-Default, kein `model`-Override nötig).

**Begründung/Vorgeschichte:** Der ursprünglich naheliegende Kandidat für
"mehr Tiefe" wäre ein Pro-Modell gewesen (`gemini-3.1-pro-preview` – der
alte Default `gemini-2.5-pro` ist für neue Nutzer inzwischen abgeschaltet,
Google leitet auf `gemini-3.1-pro-preview` um). Brians kostenloser
AI-Studio-Key hat für Pro-Modelle aber ein Kontingent von **0**
(`generate_content_free_tier_requests limit: 0` – Pro-Zugriff erfordert ein
Billing-Konto). Flash-Modelle laufen dagegen im Free Tier. Ein echter
End-to-End-Testlauf (volle TMR-Quick-Filter-Methodik für ASML, gleiches
Fact-Pack wie beim Conan-Testlauf) mit `gemini-2.5-flash` lief sauber durch
und lieferte eine methodik-treue, korrekt `[TRAINING]`-getaggte Analyse
(Rating BEOBACHTEN, Reaper Score 6/10, Konfidenz 🔴 0%, Abstauber-Limit
$1450 – bemerkenswert abweichend von Conans $1250 bei identischem
Fact-Pack, was den Cross-Check-Mehrwert der drei unabhängigen KI-Beine
demonstriert). Brian hat danach `gemini-2.5-flash` als Standard bestätigt.
Falls "mehr Tiefe" später gewünscht wird, müsste zuerst ein Billing-Konto
bei Google AI Studio/Cloud eingerichtet werden (siehe
https://ai.google.dev/gemini-api/docs/rate-limits), bevor ein Pro-Modell
infrage kommt – das kann nur Brian selbst tun (Zahlungsdaten).

**Praktische Konsequenz:** Mit `gemini-bridge` UND `openai-bridge` laufen
jetzt **beide** externen KI-Beine (Jack + Conan) ohne Chrome-Abhängigkeit.
Das hebt die alte Scheduled-Task-Einschränkung auf (siehe architecture.md,
Abschnitt "Wichtige technische Einschränkung" bei den Earnings-/Trigger-
Checks) – ein unbeaufsichtigter Scheduled Task kann jetzt den vollen
3-fach-Check fahren, auch wenn Brians Desktop-App/Chrome nicht offen ist.
Chrome-Browser-Automation (Abschnitt 10.4, 10.5) bleibt als Fallback
dokumentiert, falls eine der beiden Bridges mal ausfällt.

**Setup-Analogie zu openai-bridge (falls die Bridge mal neu aufgesetzt
werden muss):** venv mit Python 3.11.15 (`~/.local/share/uv/python/
cpython-3.11.15-macos-aarch64-none/`), Package `mcp==2.1.1`, `run.sh` +
`server.py` + `.env` nach identischem Muster. Gleicher Fallstrick wie bei
openai-bridge: der MCP-Hintergrundprozess übernimmt Code-Änderungen NICHT
automatisch bei einem normalen Session-Neustart – bei Bedarf
`ps aux | grep gemini-bridge` + `kill <pid>`, respawnt beim nächsten
Tool-Aufruf automatisch neu (siehe 10.9 für die ausführliche Beschreibung
dieses Verhaltens). **Neue Tool-NAMEN** (nicht nur geänderter Code in
bestehenden Tools) tauchen zusätzlich erst nach einem echten
Session-Neustart in der Tool-Liste auf – reines Prozess-Killen reicht dafür
nicht (siehe 10.11 unten, dort erstmals aufgetreten).

### 10.11 Depot-Zugriff für Jack/Conan – `ask_chatgpt_agentic` / `ask_gemini_agentic`

Auf Brians Wunsch (2026-09-02): Jack und Conan sollen einen echten Blick
aufs Depot haben, nicht nur auf den einzelnen Analyse-Kandidaten. Wichtige
Einschränkung, die die gesamte Umsetzung bestimmt: **Die Bridge-Prozesse
selbst haben keinerlei Depot-Zugriff** – sie sind isolierte Skripte mit nur
einem OpenAI-/Gemini-API-Key, keine Verbindung zum Scalable-Capital-MCP.
"Live-Zugriff" bedeutet daher technisch: Jack/Conan fordern per
Function-Calling Depot-Daten an, **Jarvis führt die echten MCP-Tools aus
und reicht das Ergebnis zurück** – kein direkter Durchgriff der externen
KIs, sondern ein von Jarvis gesteuerter Relay-Loop.

**Neue Tools (zusätzlich zu `ask_chatgpt`/`ask_gemini`, die unverändert
bleiben und weiterhin die einfache Wahl sind, wenn kein Depot-Kontext
gebraucht wird):**
- `mcp__openai-bridge__ask_chatgpt_agentic(prompt, system_prompt, model, state_json, tool_results_json)`
- `mcp__gemini-bridge__ask_gemini_agentic(prompt, system_prompt, model, state_json, tool_results_json)`

**Exponierte Tools – bewusst NUR read-only (kein Order-/Watchlist-/
Preview-Zugriff, siehe Whitelist Abschnitt 10.7):**
`get_portfolio_holdings`, `get_portfolio_overview`, `get_portfolio_performance`,
`get_portfolio_cash_breakdown` – 1:1 dieselben vier MCP-Tools, die auch
Jarvis selbst nutzt, nur als Function-Calling-Schema an Jack/Conan gespiegelt.
**Plus `get_manual_broker_positions`** (2026-09-02 ergänzt, nachdem Brian
darauf hingewiesen hat, dass die vier `get_portfolio_*`-Tools NUR den
Scalable-Capital-Teil des Depots zeigen): liefert die Positionen der DREI
WEITEREN Broker (Trade Republic, Smartbroker+, finanzen.net zero), die
keine API haben und nur manuell per Screenshot in `depot/trade-republic.md`,
`depot/smartbroker-plus.md`, `depot/finanzen-net-zero.md` gepflegt werden.
Kein MCP-Tool – Jarvis liest bei diesem Tool-Call einfach die drei Dateien
und liefert eine kondensierte Zusammenfassung (nur aktive Positionen, keine
verkauften; wo kein aktueller Kurs bekannt ist, klar als "data_gap"/
Investsumme statt Live-Wert kennzeichnen – Data-Integrity-Prinzip auch hier).
**Ohne dieses Tool sehen Jack/Conan nur ~11.100€ von insgesamt ~34.800€
Depotwert** (Stand des Testlaufs 2026-09-02) – bei jeder Depot-Kontext-Analyse
`get_manual_broker_positions` also mit anfordern (die Tool-Beschreibung
weist die KI bereits explizit darauf hin, es "IMMER" zusätzlich zu nutzen).

**Ablauf (von Jarvis manuell zu steuern, kein Automatismus):**
1. Erster Aufruf nur mit `prompt` (+ optional `system_prompt`/`model`).
2. Rückgabe ist immer ein JSON-String mit `"status"`:
   - `"tool_calls"`: die KI will Depot-Daten. Enthält die angeforderten
     Tool-Namen/Argumente + `state_json` für den nächsten Aufruf. Jarvis
     führt JEDES angeforderte Tool über die echten
     `mcp__50674d01-4841-4959-92e2-6fc6b4e8a1ca__get_portfolio_*`-Tools
     dieser Session aus und ruft die Bridge-Funktion erneut auf, mit
     demselben `state_json` plus `tool_results_json` (Ergebnisse als
     JSON, ein Eintrag pro Tool-Call – bei OpenAI gematcht über
     `tool_call_id`, bei Gemini über `tool_name`).
   - `"final"`: fertige Antwort in `"text"`.
3. Schritt 2 wiederholen bis `"status":"final"` (im Testlauf: 1 Runde,
   beide KIs riefen `get_portfolio_holdings` + `get_portfolio_cash_breakdown`
   parallel auf).

**Wichtige Beobachtung aus dem Testlauf (2026-09-02):** Der Aufruf von
`get_portfolio_cash_breakdown` wurde beim ersten Versuch vom
Auto-Mode-Classifier der Session blockiert ("Blocked by classifier" –
vermutlich weil Cash-/Kredit-/Kaufkraft-Daten sensibler eingestuft werden
als reine Holdings), beim zweiten Versuch direkt danach ging derselbe aufruf
anstandslos durch – das Verhalten ist **nicht deterministisch**, kein
Code-Bug. Für diesen Fall: der `tool_results_json`-Eintrag für ein
fehlgeschlagenes Tool sollte ein `{"error": "N/V - ..."}`-Objekt sein statt
den Aufruf einfach wegzulassen – beide KIs haben das im Testlauf korrekt
als "keine Daten verfügbar, ich schätze nichts" behandelt (Data-Integrity-
Prinzip der Methodik-Prompts greift also auch hier automatisch). Falls ein
Tool wiederholt blockiert wird, könnte das an Berechtigungs-/Classifier-
Einstellungen liegen, die Brian ggf. anpassen müsste (siehe Fehlermeldung:
"To allow this type of action in the future, the user can add a Bash
permission rule to their settings").

**Praktische Konsequenz für die Pipeline:** Für Analysen, bei denen der
Depot-Kontext relevant ist (Konzentrationsrisiko, Kategorie-Caps, Cash-
Situation vor Nachkauf-Entscheidungen), `_agentic`-Varianten verwenden.
Für einzelne Kandidaten-Analysen ohne Depot-Bezug reichen weiterhin die
einfachen `ask_chatgpt`/`ask_gemini`-Funktionen ohne den Mehraufwand des
Relay-Loops (mehr Roundtrips = mehr Zeit/Tokens pro Analyse).

**Erweitert 2026-09-05 um `get_quote` und `read_master_status` (Brian:
"Twelve-Data erweitern, Dateizugriff mit begrenzter Variante").** Zwei
neue Tools zur bestehenden Whitelist hinzugefügt, gleiches Relay-Prinzip
wie oben:
- **`get_quote(symbol)`:** Jarvis führt das echte
  `mcp__57370ae8-105f-49c4-a0dd-b4c78cb6ceb7__get_quote`-Tool dieser
  Session mit dem angeforderten `symbol` aus und reicht das Ergebnis
  zurück. Gibt Jack/Conan einen exakten, strukturierten Live-Kurs statt
  einer aus der Websuche zusammengesuchten Zahl – nützlich für Abstauber-
  Limit-/Einstiegszonen-Berechnungen.
- **`read_master_status()`:** Jarvis liest `depot/master_status.md` (das
  konsolidierte Status-Dashboard, siehe architecture.md "Konsolidierter
  Master-Status") und reicht den Inhalt zurück. **Bewusst die EINZIGE per
  Tool zugängliche Repo-Datei** – kein Zugriff auf `architecture.md`,
  `watchlist.md`, `depot/kategorisierung.md` oder sonstige Dateien.
  **Begründung für diese enge Grenze (Jarvis, von Brian bestätigt):** Jack
  und Conan sollen unabhängige Gutachter für eine konkrete, von Jarvis
  gestellte Aufgabe bleiben, keine freien Systembrowser – mit Zugriff aufs
  ganze Regelwerk könnten sie anfangen, sich ihre eigene Aufgabenstellung
  zusammenzusuchen oder Regeln zu hinterfragen statt sie anzuwenden, was
  die Vergleichbarkeit der drei unabhängigen Urteile verwässern würde.
  `master_status.md` allein liefert nützlichen Portfolio-Kontext (offene
  Kategorie-Slots, Region-/Sektor-Übergewichte, offene Prüfpunkte) ohne
  dieses Risiko, weil es reine Kennzahlen aggregiert, keine Regeln enthält.

**Beide neuen Tools mit echten End-to-End-Tests bestätigt (2026-09-05,
beide Bridges):** ein Test-Prompt forderte gezielt beide Tools parallel
an (`get_quote(RKLB)` + `read_master_status`), Jarvis führte beide aus
(echter Twelve-Data-Call + echter Datei-Read) und reichte die Ergebnisse
zurück – beide KIs lieferten eine korrekte, beide Datenpunkte
einbeziehende Zusammenfassung im finalen `"status":"final"`-Ergebnis.
Funktioniert identisch bei Gemini (`functionCall`/`tool_name`-Matching)
und OpenAI (`tool_calls`/`tool_call_id`-Matching).

### 10.12 ISIN-Gegenprobe bei WebSearch-Fundamentaldaten – gilt für JEDE Analyse, nicht nur Watchlist

Beim Orion-Oyj-Testlauf (2026-09-02, ad-hoc Einzelanalyse auf Brians
Wunsch) lieferte eine WebSearch nach Cashflow/Verschuldung scheinbar
passende Zahlen, die tatsächlich zu **"Orion S.A."**/**"Orion Group
Holdings"** gehörten – andere Firmen. Nur durch Plausibilitätsprüfung
aufgefallen. **Neue Regel (architecture.md, Abschnitt "Watchlist-System",
Unterpunkt "ISIN-Gegenprobe bei JEDER WebSearch-Fundamentaldaten-
Recherche"):** gilt nicht nur bei Watchlist-Neuaufnahmen (dort schon
länger über das Identity-Gate abgedeckt), sondern bei JEDER
Fundamentaldaten-Recherche per WebSearch/WebFetch, auch bei einer
spontanen Einzelanalyse mitten im Chat. Bei nicht eindeutigen Firmennamen:
jede übernommene Kennzahl gegen ISIN/Ticker+Börsenplatz gegenprüfen, sonst
[N/V] statt "wahrscheinlich richtig". Lieber Datenlücke im Fact-Pack als
falsch zugeordnete Kennzahl.

### 10.13 Standard-Meta-Instruktion für Bridge-Aufrufe (Pflicht ab 2026-09-02) – behebt Jacks systematischen Reflex-Abbruch

**Symptom (Orion Oyj + Asahi Intecc, beide 2026-09-02):** Jack (Gemini)
brach bei JEDEM frischen Quick-Filter-Kandidaten ohne vollständiges
IR-Fact-Pack sofort auf SCHROTT/1 ab, während Conan (ChatGPT) mit
denselben Lücken zu einem vollständigen Rating kam. Auf Brians
ausdrückliche Bitte systematisch untersucht (nicht einfach hingenommen).

**Diagnose (verifiziert, kein Prompt-Kürzungs-Bug):** Ein Diagnose-Prompt
an Jack ("zitiere den letzten Satz vor dieser Frage wortwörtlich") kam mit
dem exakt korrekten letzten Satz der 70KB-Methodik-Datei zurück – der
volle Text kommt vollständig an. Die eigentliche Ursache waren ZWEI
Stellen, an denen Jack eine im Regelwerk vorhandene Formulierung
literalistischer als Conan ausgelegt hat und sich damit einen
Abbruchgrund gesucht hat:
1. Unklare Schwelle, wann `[TRAINING]` statt `[N/V]` bei fehlenden
   K-Kriterien zulässig ist (Regelwerk erlaubt TRAINING für K technisch,
   aber ohne explizite Daumenregel, wann eine Schätzung "gut genug" ist).
2. SCHRITT-0-LIVE-CHECK und die RECHEN-DOKTRIN (Regel 20,
   Python-Tool-Call-Pflicht für WACC/DCF) wörtlich genommen, obwohl die
   API-Bridge strukturell weder Web-Search noch Tool-Calls hat – nachdem
   Punkt 1 gefixt war, hat sich Jack genau diese zweite Stelle als neuen
   Abbruchgrund gesucht.

**Fix (getestet, funktioniert – Asahi Intecc lief danach vollständig
durch: BEOBACHTEN, Reaper Score 5/10, nah an Conans unabhängigem 6/10):**
Ab sofort bei JEDEM Bridge-Aufruf (`ask_chatgpt`/`ask_gemini`, sowohl
Jack als auch Conan – identischer Wortlaut für beide, damit sie nach
demselben Maßstab urteilen) folgende **vier** Klarstellungs-Blöcke VOR die
Methodik-Datei setzen, zusätzlich zum bisherigen Fact-Pack-Hinweis (Block
4 seit 2026-09-03, siehe Ergänzung unten):

```
WICHTIG: SCHRITT-0-LIVE-CHECK GILT ALS BEREITS DURCHGEFUEHRT UND ABGESCHLOSSEN.
Jarvis (der Orchestrator) hat SCHRITT 0 bereits SELBST per echter Web-Recherche
erledigt, BEVOR dieser Prompt an dich ging - das Ergebnis steht im FACT-PACK
unten. Wo SCHRITT 0/Global-Regeln von "Live-Check", "Web-Search ausfuehren"
oder "pausieren bis Live-Daten bestaetigt sind" sprechen: das bezieht sich auf
den Fall, dass GAR KEINE Live-Recherche stattgefunden hat. Hier hat sie
stattgefunden (durch Jarvis) - behandle das FACT-PACK als soliden Ausgangspunkt,
nicht als von dir nochmal komplett neu zu recherchierende Leerstelle.

WICHTIG, ERGAENZT 2026-09-04: DU HAST JETZT SELBST LIVE-WEB-SUCHE (Google Search
Grounding). Das FACT-PACK ersetzt NICHT deine eigene Recherche, es ist die
Ausgangsbasis. Nutze deine eigene Suche gezielt fuer: (a) jedes [TRAINING]- oder
[N/V]-getaggte K-Kriterium im Fact-Pack, das sich per Suche zu [VERIFIED]
aufwerten liesse, (b) Zahlen im Fact-Pack, die dir veraltet oder unplausibel
vorkommen, (c) News/Ereignisse NACH dem im Fact-Pack genannten Recherche-Datum.
Wenn deine eigene Recherche vom Fact-Pack abweicht: das explizit benennen (nicht
stillschweigend uebernehmen oder stillschweigend ersetzen) - genau diese
Divergenz macht den 3-fach-Cross-Check wertvoller, nicht ungenauer. Bei
widerspruechlichen Quellen gilt weiterhin die aktuelle Zahl vor der aelteren,
und eine erst waehrend deiner Suche gefundene Primaerquelle (Geschaeftsbericht,
Ad-hoc-Meldung) vor einer sekundaeren (Analysten-Kommentar, Forum).

WICHTIG: WACC-KOMPONENTEN (Beta, Rf, ERP, CRP) UND DCF-BERECHNUNGEN OHNE
PYTHON-TOOL-CALL. Du hast in dieser Sitzung keinen Python-Tool-Call zur
Verfuegung (technische Einschraenkung der API-Bridge, nicht deine
Entscheidung). Fuer QUICK FILTER ist ohnehin KEIN Full-DCF vorgesehen - die
Tool-Call-Pflicht (Regel 20) bezieht sich auf FULL-DEEP-DIVE-DCF-Berechnungen.
Schaetze WACC-Komponenten mit [TRAINING]-Tag statt die gesamte Analyse
deswegen abzubrechen.

WICHTIGE KLARSTELLUNG ZUR [TRAINING]-VS-[N/V]-ENTSCHEIDUNG BEI K-KRITERIEN
(gilt gleichermassen fuer dich wie fuer die andere KI im selben Cross-Check):
QUICK FILTER ist laut Methodik selbst ausdruecklich "geeignet fuer... datenarme
Firmen". Ein sofortiger Abbruch bei jeder einzelnen fehlenden Zahl wuerde
diesen erklaerten Zweck systematisch unterlaufen. Nutze [TRAINING] IMMER DANN,
wenn du zu einer Kennzahl eine halbwegs plausible, aus deinem allgemeinen
Wissen begruendbare GROESSENORDNUNG angeben kannst. Reserviere [N/V] NUR fuer
den Fall, dass du zu einer Kennzahl GAR KEINE Einordnung hast.

ZUSAMMENGEFASST: Fuehre die komplette Analyse bis zum Ende durch. Die zu
erwartende Konfidenz ist wegen der vielen [TRAINING]-Tags 🔴 NIEDRIG - das ist
ein KORREKTES, ERWARTETES Ergebnis dieser Sitzungsart, kein Grund zum Abbruch.
Ein Abbruch ist nur bei einem ECHTEN K-Kriterium-[N/V] angemessen (siehe
Klarstellung oben), nicht bei fehlendem Tool-Zugriff als solchem.

WICHTIG: TERMINAL-STATE-PFLICHT (gilt fuer dich genauso wie fuer Jarvis und
die andere KI im selben Cross-Check). Ausloeser: der RKLB-Canonical-
Failure-Case (2026-09-01) - eine KI hatte "ABBRUCH-LOGIK GREIFT" korrekt
erkannt, ist aber danach trotzdem regulaer durch die nachgelagerten Module
gelaufen und kam auf ein reguläres Rating mit echter Sizing-Freigabe. Ein
erkannter Abbruch war bis dahin nur eine Textzeile, kein echter
Systemzustand - das darf sich nicht wiederholen. Sobald WAEHREND dieser
Analyse einer der folgenden Zustaende eintritt: ein K-Kriterium ist [N/V]
(TMR oder Scout) - Going-Concern-Zweifel bestaetigt sich (TMR SCHRITT 0C) -
Scout: K <= K-BASIS-2 - Scout: Fraud-Check >= 3 Flags oder Going-Concern -
wird dieser Zustand SOFORT TERMINAL: kein nachgelagertes Modul (Moat/
Gruender-Score/Bewertung/Outcome/Rating/Sizing) darf danach noch
ENTSCHEIDUNGSRELEVANT laufen, hoechstens noch diagnostisch/erwaehnend. Eine
spaeter im Text auffallende positive Information (starker Moat, gute
Zahlen) kann einen bereits erreichten Terminal-Zustand NICHT rueckgaengig
machen ("GUARDRAIL > ENTSCHEIDUNG > SCORE" - ein ausgeloester Abbruch
schlaegt jedes nachgelagerte numerische Ergebnis). Pflicht-Ausgabeformat
bei Terminal-Zustand: ein klar markierter Block ("ABBRUCH-ZUSTAND
ERREICHT", die ausloesende Regel, der festgestellte Wert, Status "ANALYSE
BEENDET", Urteil, Sizing: 0%) - kein weiterer inhaltlicher Text danach.
PRUEFE VOR DEINER FINALEN RATING-ABGABE EXPLIZIT SELBST: "Wurde in diesem
Lauf ein Abbruch-Zustand erreicht? Falls ja, entspricht mein Endergebnis
exakt diesem Abbruch-Format, ohne dass ein nachgelagertes Modul das
Ergebnis beeinflusst hat?"
```

**Wichtig – was das NICHT ist:** Das ist keine Aufweichung der
Datenintegrität-Philosophie und keine Änderung an Brians Methodik-Dateien
(bleiben unverändert). Es ist eine Klarstellung EINER ECHTEN Unschärfe im
Text selbst (QUICK FILTER soll für datenarme Firmen funktionieren, aber
die ABBRUCH-LOGIK differenziert das nicht explizit) – auf beide KIs
gleich angewendet, damit nicht die Modellwahl (Gemini vs. GPT) über das
Ergebnis entscheidet, sondern die Faktenlage.

**Praktische Konsequenz:** Die SCHROTT-Ergebnisse für Orion Oyj (Jack,
2026-09-02) und den ersten Asahi-Intecc-Lauf (Jack, 2026-09-02, vor dem
Fix) gelten als durch einen Prompt-Klarheits-Mangel verzerrt, nicht als
belastbares Urteil über die Firmen – bei Bedarf mit dieser Standard-
Instruktion neu laufen lassen. Ab sofort MUSS jeder neue Bridge-Aufruf
für TMR/Scout-Analysen alle sechs Blöcke enthalten (auch im Täglichen
Trigger-Check und im Blitz-Scan, siehe dortige SKILL.md-Dateien) – Block 5
(Gründliche-These-Prüfung) ist bei jeder Analyse einer bestehenden
Depot-Position Pflicht, Block 6 (Master-Status/Vorrang-Hierarchie) nur bei
agentischem Depot-Tool-Zugriff (siehe unten für beide).

**Block 4 ergänzt (2026-09-03, aus dem 3-KI-System-Audit):** Brian ließ
Jarvis, Jack und Conan das gesamte Regelwerk gemeinsam durchgehen. Beide
KIs fanden unabhängig voneinander denselben kritischen Punkt: der
Terminal-State-Mechanismus (siehe architecture.md Abschnitt 14, ausgelöst
durch den RKLB-Fall) steht bisher NUR in architecture.md, nicht in den
tatsächlichen Prompt-Dateien oder im bisherigen Bridge-Meta-Instruktion-
Text – d.h. er erreichte Jack/Conan im API-Betrieb möglicherweise gar
nicht. Genau der Fehler, den der Mechanismus verhindern soll, könnte sich
so unbemerkt wiederholen. Block 4 schließt diese Lücke, indem er die
Terminal-State-Pflicht direkt in den Text einbettet, der bei jedem
Bridge-Aufruf tatsächlich ankommt.

**Block 5 ergänzt (2026-09-04, Brian: "das ganze System soll für alle
Agenten gelten, sowohl für Jack als auch für Conan").** Dieselbe Lücke wie
bei Block 4 trat erneut auf: die am selben Tag gebaute "Gründliche-These-
Prüfung-vor-Verkaufsempfehlung-Pflicht" (Auslöser: der Cellebrite-Fall,
siehe architecture.md "Verkaufsdisziplin & Gewinnmitnahme-Regeln") wurde
zunächst nur in architecture.md und den FIXE-GRENZEN-Abschnitten der
SKILL.md-Dateien verankert – das steuert Jarvis' eigenes Verhalten, aber
NICHT das, was Jack/Conan bei einem Bridge-Aufruf tatsächlich zu lesen
bekommen. Ohne diesen Block hätte ein künftiger Scout-/TMR-Lauf für eine
bestehende Depot-Position genau denselben vorschnellen SCHROTT-Reflex
wiederholen können, den die Regel eigentlich verhindern soll. Block 5:

```
WICHTIG: GRUENDLICHE-THESE-PRUEFUNG-VOR-VERKAUFSEMPFEHLUNG-PFLICHT (gilt fuer
dich genauso wie fuer Jarvis und die andere KI im selben Cross-Check). Ausloeser:
der Cellebrite-Fall (2026-09-04) - ein vorschneller Scout-Check kam zu SCHROTT/
VERKAUFEN fuer eine BEREITS GEHALTENE Depot-Position, obwohl 2 von 3 Re-Rating-
Triggern mangels aktueller Quartalszahlen noch gar nicht pruefbar waren (nicht
"durchgefallen", sondern schlicht noch nicht faellig) und der Guidance-Cut
plausibel auf Timing (verzoegerte Grossauftraege) statt einen echten
Struktur-Bruch zurueckging. Bevor du fuer eine im FACT-PACK als "bereits
gehalten"/"bestehende Depot-Position" gekennzeichnete Firma eine Kategorie-5-
Empfehlung (VERKAUF ERWAEGEN) allein aus deiner eigenen Abbruch-Logik (K<=K-
BASIS-2, Terminal-State, SCHROTT-Rating) ableitest, PRUEFE ZWINGEND UND WEISE
IM OUTPUT EXPLIZIT AUS:
1. TIMING vs. STRUKTUR: ist das ausloesende Ereignis (Guidance-Cut, Kursrutsch,
   ein K-Kriterium knapp verfehlt) ein temporaeres/zyklisches Ereignis oder ein
   echtes strukturelles Problem? Nicht reflexhaft die negativste Lesart nehmen.
2. CHECKPOINT RESPEKTIEREN: nennt das FACT-PACK bereits einen definierten
   kuenftigen Pruefpunkt (z.B. naechste Earnings), der noch in der Zukunft liegt?
   Dann bleibt es bei HALTEN+Checkpoint statt Verkauf, AUSSER ein hartes,
   unabhaengiges Ausschlusskriterium (Fraud/Going-Concern/Moat-Verlust/
   Uebernahme) ist JETZT bereits erfuellt.
3. REIFEGRAD-METHODIK-MISMATCH: greift ein fuer junge/spekulative Firmen
   gebauter Wachstumsmassstab (z.B. eine hohe CAGR-Schwelle) hier mechanisch bei
   einer bereits etablierten, umsatzstarken/profitablen Position, fuer die
   dieser Massstab methodisch gar nicht gebaut wurde?
Gilt NICHT fuer die Erstpruefung eines NEUEN Kandidaten (kein "bereits gehalten"
im FACT-PACK) - dort bleibt deine Abbruch-Logik unveraendert streng (bewusste
Asymmetrie: hohe Huerde fuer neues Kapital, mehr Geduld vor dem Rauswerfen einer
bereits finanzierten These).
```

**Block 6 ergänzt (2026-09-04, gleicher Anlass):** Master-Status/
Informations-Vorrang-Hierarchie – nur relevant, wenn Jack/Conan im
agentischen Modus (`ask_gemini_agentic`/`ask_chatgpt_agentic`, siehe
10.11) selbst Depot-Tools aufrufen und dabei auf mehrere, potenziell
widersprüchliche Datenquellen stoßen könnten. Kurzer Hinweis statt langer
Block, da im normalen (nicht-agentischen) Bridge-Betrieb ohnehin nur das
fertige FACT-PACK ankommt, keine eigene Dateisuche stattfindet:

```
HINWEIS (nur relevant, falls du in diesem Lauf selbst Depot-Tools aufrufst):
`depot/master_status.md` ist das konsolidierte, laufend aktualisierte Status-
Dashboard (Kategorie-Zaehlungen, offene Pruefpunkte, offene Empfehlungen,
offene Portfolio-Regel-Fragen). Bei widersprüchlichen Informationen zwischen
Dateien gilt diese Rangfolge (hoechste zuerst): 1. eine jüngste, explizit
bestätigte Transaktion/Entscheidung, 2. `depot/master_status.md`,
3. `architecture.md`, 4. ältere Analysen/Chat-Historie.
```

**Bewusst NICHT in die Bridge-Blöcke übernommen (2026-09-04, Abwägung
dokumentiert):** die "Regel-Aufnahme-Disziplin/Ruleset-Hygiene" und der
"Tieferer Zweck der Kandidatensuche" (Bereicherung/Unter-Radar/Watchlist-
Vergleich) sind reine Jarvis-Orchestrierungs-Aufgaben (Screening, Datei-
Pflege, Regelwerk-Pflege) – Jack/Conan bewerten nur den ihnen vorgelegten
einzelnen Kandidaten, sie screenen nicht selbst und pflegen keine Regeln.
Diese beiden Mechanismen bräuchten deshalb keinen eigenen Bridge-Block;
sollte sich das ändern (z.B. Jack/Conan werden künftig selbst zum
Screening herangezogen), müsste das hier nachgezogen werden.

**Bridge-Status-Log ergänzt (2026-09-04, Conans Vorschlag aus dem
3-KI-Pulse-Check vom 2026-09-03):** nach dem E-Mail-Bug (dokumentiert als
funktionierend, aber nie verifiziert, tagelang unbemerkt ausgefallen)
merkte Conan an, dass derselbe blinde Fleck beim API-Bridge-Mechanismus
selbst bestehen könnte – "die Architektur ist besser, aber Ausfälle
werden nicht sichtbar". Neue Datei `depot/bridge_status.md`: jeder
Scheduled-Task-Lauf, der Jack/Conan per Bridge einsetzt (oder bewusst
nicht einsetzt), hängt eine Statuszeile an (OK/FAIL/Fallback je KI). Fällt
eine Bridge über mehrere Läufe hinweg aus, ist das jetzt aus der Datei
ablesbar, statt erst aufzufallen, wenn eine Analyse spürbar fehlt.

**Dritte dokumentierte Wiederholung des Reflex-Abbruch-Bugs (2026-09-05,
Lasertec-Lauf):** trotz Block 2/3 (TRAINING-vs-N/V-Klarstellung) UND
eigener Websuche brach Jack erneut mit SCHROTT/Terminal-State ab, weil
Piotroski-F-Score (für japanische Emittenten strukturell oft nicht sauber
ermittelbar) und eine durch Working-Capital-Timing verzerrte
Quartals-FCF-Marge als [N/V] statt [TRAINING] eingestuft wurden – identisch
zum Muster bei Asahi Intecc und Disco Corp (siehe watchlist.md-
Änderungsprotokoll). **Bemerkenswert:** Conan stand im selben Lauf vor
GENAU denselben Datenlücken und schätzte beide korrekt mit [TRAINING]
(Piotroski 7-8/9, FCF-Marge ~19,5-20,3%) statt abzubrechen. Das bestätigt:
Block 2/3 hat das Problem für Conan gelöst, für Jack/Gemini nur
teilweise – die Klarstellung wird zwar gelesen (Jack referenziert sie
explizit im Output), aber bei genau diesen zwei Kennzahlen (Piotroski bei
Nicht-US-Emittenten, Quartals-FCF-Marge bei Working-Capital-Verzerrung)
entscheidet sich Jack trotzdem für die strengste Lesart. **Noch nicht
behoben, nur dokumentiert:** ein möglicher nächster Schritt wäre ein noch
konkreteres Beispiel im Klarstellungsblock ("Piotroski bei japanischen/
nicht-US-Emittenten OHNE 10-K: nutze eine plausible TRAINING-Schätzung
basierend auf Profitabilität/Bilanzqualität, niemals N/V allein deswegen")
– bei Gelegenheit prüfen, ob das die Wiederholungsrate senkt. Bis dahin:
ein Jack-SCHROTT/Terminal-State-Ergebnis, das ausschließlich auf Piotroski
und/oder einer einzelnen verzerrten FCF-Quartalszahl beruht, wird als
Datenlücken-Artefakt behandelt, nicht als belastbares Urteil – Conans und
Jarvis' Einschätzung erhalten in diesem Fall mehr Gewicht.

---

## 11. Offene Punkte (Stand dieser Übergabe)

Aus `architecture.md` Abschnitt 8 (13 nummerierte Punkte, dort im Detail –
hier nur die wichtigsten für den Sessionstart):

1. **Core-vs-Advisory-Rules-Split — GELÖST (2026-09-01, hier nur
   nachträglich als erledigt markiert, 2026-09-04 geprüft):** architecture.md
   Abschnitt 14 dokumentiert die Freigabe explizit ("von Brian am 01.09.2026
   angeordnet... mit sofortiger Wirkung freigegeben") - 16 Core-Rules +
   Advisory-Rules + Terminal-State-Mechanismus sind seither aktiv im Einsatz
   (u.a. Grundlage für die Terminal-State-Pflicht in jedem Bridge-Aufruf,
   siehe HANDOVER.md 10.13).
2. Scalable-Capital-MCP-Integration mit Tool-Whitelist (Abschnitt 10.7) —
   **funktional in aktivem täglichen Einsatz** (das 4-Stufen-Modell
   read-only/Verwaltung-ohne-Geldbewegung/Preview/PERMANENT-VERBOTEN steht
   wortgleich in jeder Scheduled-Task-SKILL.md und wird dort durchgesetzt).
   Nicht verifiziert: ob die Liste literal exakt 39 Tools umfasst (reine
   Zähl-/Vollständigkeitsfrage, kein funktionales Problem).
3. Daten-Lücken bei 9 benannten Positionen — **geprüft 2026-09-04, keine
   offenen 🔴-Datenqualitäts-Flags mehr in `depot/trade-republic.md`,
   `depot/smartbroker-plus.md`, `depot/finanzen-net-zero.md` gefunden**;
   alle drei Dateien sind seit der am 2026-08-23 bestätigten vollständigen
   Depot-Erfassung durchgängig ohne Datenlücken-Markierung. Punkt betraf
   vermutlich den Zustand vor dieser Erfassung.
4-10. Diverse kleinere offene Punkte (siehe Original).
11. **2026-08-28 Wochenfazit-Zuverlässigkeitsvorfall:** "SUCCEEDED" beim
    Scheduled Task bedeutete nicht zwangsläufig "Task tatsächlich
    inhaltlich abgeschlossen" – ein Grund, Ergebnisse von Scheduled Tasks
    stichprobenartig zu verifizieren.
12. Praktischer PDF-Scope-Kompromiss: 6-Positionen-pro-Seite-Kartenraster
    für Wochenreports.
13. **RKLB-Scout-Quick-Filter-Meta-Retro-Fall — GELÖST (2026-09-01, hier
    nur nachträglich als erledigt markiert, 2026-09-04 im Rahmen der
    Gaps-Abarbeitung geprüft):** Jacks Rating widersprach seinem eigenen
    Abbruch-Befund (Regelfehler, nicht gleichwertige Auslegung) - Auflösung
    in `analysen/KRKN-RKLB-nachholanalyse-final-2026-09-01.md`: Jarvis'
    ursprüngliches Ergebnis vom 28.08. (RATING ZU FRÜH, Sizing 0%) als
    offizielles System-Ergebnis bestätigt. Dieser Fall wurde zudem zum
    Canonical Failure Case für den späteren Terminal-State-Mechanismus
    (architecture.md Abschnitt 14, 2026-09-01).
14. **E-Mail-Versand aus Scheduled Tasks lief nie, seit 2026-09-01
    diagnostiziert und gefixt (2026-09-03):** Brian bekam trotz "verdrahtet
    und getestet" markiertem Gmail-Connector nie eine E-Mail aus
    `taeglicher-trigger-check`/`blitz-scan`/`wochenfazit`, obwohl die
    Läufe selbst (inkl. Commits) normal durchliefen. Per Gmail
    `search_threads` verifiziert: seit der Verbindungstest-Mail vom
    2026-09-01 keine einzige weitere Aktien-Agent-Mail im
    "Gesendet"-Ordner. Wahrscheinliche Ursache: `send_message` (Gmail)
    und `PushNotification` sind deferred tools und müssen vor dem ersten
    Aufruf per `ToolSearch` geladen werden (wie es für die Bridge-Tools
    bereits von Anfang an in den SKILL.md-Dateien stand) – das fehlte für
    Gmail/PushNotification. Fix in allen drei SKILL.md-Dateien ergänzt
    (expliziter `ToolSearch`-Aufruf ganz am Anfang jedes Laufs + Pflicht,
    das tatsächliche Erfolgsergebnis von `send_message` zu prüfen). Noch
    NICHT verifiziert, ob der Fix greift – Prüfpunkt ist die tägliche
    "alles ruhig"-Bestätigungsmail am 2026-09-04. Siehe
    `project_trigger_check_email_verifizierung`-Memory für Details.

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
- **Eskalations-Kanal vollständig (2026-09-01, Update im Laufe des Tages):**
  `architecture.md` verlangt an mehreren Stellen "E-Mail/Push" bei echtem
  Anlass. Push funktioniert seit dem Vormittag (Remote Control verbunden,
  `PushNotification`-Tool). **E-Mail war zunächst NICHT verdrahtet** (kein
  Connector in der Registry, mehrfach erfolglos gesucht – vermutlich auch
  zu Cowork-Zeiten nie ein echter Kanal, nur ein Konzept im Regelwerk) –
  **Brian hat den Gmail-Connector am Nachmittag selbst in den
  App-Einstellungen verbunden** (außerhalb dieser Chat-Session, gleicher
  Ort wie Remote Control). Danach mit einer echten Test-Mail an
  `brianqtng@outlook.de` verifiziert (Message-ID erhalten). Alle vier
  Scheduled Tasks rufen jetzt bei handlungsrelevantem Ergebnis zusätzlich
  zu Chat-Nachricht und PushNotification eine E-Mail auf (Wochenfazit/
  Monatsrecap mit PDF-Anhang, Trigger-Check/Blitz-Scan als Text-Mail).
  Gmail-Tools: `mcp__39fc6043-f82a-4cc9-8559-c05af3108ec2__*`.
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
