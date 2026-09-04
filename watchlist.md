# Watchlist – Brians Aktien-Agent

**Angelegt:** 2026-08-28 · **Zweck (von Brian festgelegt):** Eigenständige Liste von
Aktien außerhalb des aktuellen Depots, die entweder als möglicher **Ersatz für
bestehende Depot-Positionen** dienen könnten oder als **interessante Ergänzung**
fürs Portfolio beobachtet werden. Läuft **jede Woche automatisiert im Hintergrund**
(siehe `architecture.md`, Abschnitt "Watchlist-System") mit fester Obergrenze
**max. 20-30 Werte**, damit Brian nicht den Überblick verliert. Erscheint ab sofort
als eigener Abschnitt im wöchentlichen Wochenfazit (neu rein / raus + 1-2 Sätze
Begründung).

**Struktur (2026-08-28, von Brian gefordert):** Die Watchlist folgt derselben
Kategorie-Logik wie das Depot selbst (siehe `architecture.md`, Abschnitt 3) –
**Champions / Profi / Talent** – damit ein Watchlist-Wert direkt erkennen lässt,
in welche Depot-Kategorie er bei einer Aufnahme fallen würde bzw. welche Art von
Depot-Position er ersetzen könnte. Alle drei Kategorien sind bewusst gefüllt.

**Aktueller Stand:** 30 Werte gesamt – **Champions: 16 · Profi: 10 · Talent: 4** (Stand 2026-09-04, nach Umkategorisierung Lasertec Talent→Champions, Asahi Intecc Talent→Profi, sowie Arista Networks Profi→Champions und USLM Talent→Champions im "geschärfter Blick"-Review – siehe jeweilige Zeilen)
(21 von Brian vorgegeben, 9 systematisch von Jarvis ergänzt, um die Liste
sektoral/geografisch breiter aufzustellen und alle drei Kategorien sauber zu
füllen; zuletzt Exponent (EXPO) am 2026-08-29 aus einer gezielten
Depot-Lücken-Suche ergänzt).

**Hinweis zur Kategorisierung:** Die Einordnung folgt derselben Logik wie im
Depot – Champions = etablierte Weltklasse-Compounder mit breitem, bewiesenem
Moat (TMR-Pfad); Profi = solide Qualitätsfirmen/Nischenführer, die ihre
Langfrist-Bewährung noch nicht vollständig abgeschlossen haben oder zyklischer/
konzentrierter sind (Scout-Pfad oder TMR Quick Filter); Talent = Werte mit
echtem spekulativem Risiko (Bewertung, Zyklik, Unternehmensgröße, Datenlage),
auch wenn die Marktkapitalisierung selbst schon groß ist (z.B. Palantir –
Größe schützt hier nicht vor Bewertungsrisiko). Das ist eine erste,
systematische Einordnung von Jarvis – Brian kann jederzeit einzelne Werte
manuell in eine andere Kategorie verschieben.

---

## Legende
- **Herkunft:** BRIAN = von Brian selbst vorgegeben (2026-08-28) · JARVIS = von Claude/Jarvis systematisch ergänzt (2026-08-28)
- **Status:** 🆕 NEU (diese Woche aufgenommen) · ✅ BEOBACHTUNG (unverändert) · ⚠️ RISIKO (Abstiegs-Kandidat, wird genauer beobachtet)
- **[EX-DEPOT]** = Position, die Brian im Zuge der Depot-Restrukturierung vom 27./28.08.2026 verkauft hat und jetzt zur möglichen Wiederaufnahme beobachtet.

---

## CRV-Ampel (neu, 2026-09-03, von Brian gefordert)

Zusätzlich zur Champions/Profi/Talent-Kategorie (Geschäftsqualität) zeigt die
**CRV-Ampel** (Chance-Risiko-Verhältnis) je Wert, ob JETZT ein guter
Einstiegszeitpunkt ist – Bewertung/Trend, nicht Qualität:
- 🟢 **KAUFEN** – klar unterbewertet gegenüber eigener Historie/Peers, These intakt.
- 🟡 **ABWARTEN/BEOBACHTEN** – fair bewertet, kein starkes Signal in beide Richtungen.
- 🟠 **VORSICHT/TEUER** (neu, 2026-09-03, von Brian für mehr Differenzierung ergänzt) – spürbar teuer ggü. Historie/Peers, aber kein hartes Warnsignal (spekulativ, nicht fundamental gebrochen).
- 🔴 **MEIDEN/ÜBERBEWERTET** – deutlich überbewertet und/oder mehrere gleichzeitige Warnsignale (z.B. Bewertung läuft der Ertragslage erkennbar davon).
- 🔘 **GRAU – KEINE BELASTBARE AUSSAGE** (neu, 2026-09-03, auf Conans Vorschlag ergänzt) – der primäre Bewertungsanker (siehe unten) liefert kein sinnvolles Ergebnis (z.B. Gewinn nahe null, extreme Sondereffekte, zu kurze Historie) und auch kein tragfähiger Ersatzmaßstab ist verfügbar. Methodisch sauberer, als eine nicht belastbare KGV-Zahl künstlich in eine der vier Farben zu pressen.

**Bewertungsanker je Geschäftsmodell (2026-09-03, auf Conans Vorschlag
ergänzt: "nicht jede Aktie über KGV bewerten").** KGV ist der Standard-
Anker, passt aber nicht für jedes Geschäftsmodell. Wo ein anderer Anker
sinnvoller ist, steht das explizit in der CRV-Begründung ("Anker: ..."):
Banken/Versicherer → KBV/ROE statt KGV; unprofitable Wachstumswerte →
Umsatzwachstum/Bruttomarge/Cash-Runway statt KGV; stark verzerrte Gewinne
(Sondereffekte, Patentstreit-Erträge, junge Notierung) → qualitative
Einordnung statt erzwungenem KGV-Vergleich. Kein Ankerhinweis in der
Zelle bedeutet: KGV ist hier der passende Standard-Anker.

**Gilt jetzt auch für Depot-Positionen, nicht nur Watchlist-Kandidaten**
(2026-09-03, von Brian gefordert) – siehe `depot/kategorisierung.md` für
die CRV-Ampel aller 18 aktuellen Depot-Werte. Bei einer bestehenden
Depot-Position ist die CRV-Ampel KEIN automatisches Verkaufssignal, nur
ein Nachkauf-Zeitpunkt-Signal – für Verkäufe gelten weiterhin
ausschließlich die dokumentierten Abstauber-/Stop-These-Trigger.

**Trend-Pfeile bei Auf-/Abstufung (2026-09-03, von Brian gefordert):**
Ändert sich die CRV-Farbe eines Werts gegenüber der letzten Prüfung
(vorherige wöchentliche Pflege), wird das zusätzlich zur neuen Farbe mit
einem Pfeil markiert:
- 🔺 **Aufstufung** – Ampel hat sich verbessert (z.B. 🟠→🟡 oder 🟡→🟢) – Aktie ist interessanter/günstiger geworden.
- 🔻 **Abstufung** – Ampel hat sich verschlechtert (z.B. 🟢→🟡 oder 🟡→🟠/🔴) – Aktie ist teurer/unattraktiver geworden.

Format: Farbe + Pfeil + Kurzgrund, z.B. "🟢🔺 KAUFEN (hochgestuft von 🟡) –
KGV nach Kursrücksetzer jetzt X% unter Historie". Bleibt die Ampel
unverändert, kein Pfeil (kein Rauschen bei stabilen Einstufungen). **Stand
2026-09-03 ist die Basislinie** – noch keine Vorwoche zum Vergleich, daher
aktuell überall ohne Pfeil. Erste mögliche Pfeile entstehen beim nächsten
wöchentlichen Watchlist-Check.

Basiert auf KGV vs. historischem Durchschnitt (10J-Median wo verfügbar) und
Peer-Vergleich, Stand 2026-09-03 (WebSearch-Snapshot). Wird ab jetzt beim
wöchentlichen Watchlist-Check (Wochenfazit) mitgepflegt – Kurse/Bewertungen
ändern sich, dieser Stand ist kein Dauerzustand.

**Wichtige Methodik-Klarstellung (2026-09-03, von Brian korrigiert: "du
sollst nach unserem System die Aktie bewerten... andere Webseiten kann man
dazu nehmen, aber nie als Benchmark").** Die Ampel-Farbe ist IMMER Jarvis'
(bzw. bei vollen Cross-Checks: das 3-KI-Team) eigenes Urteil, hergeleitet
aus unserer eigenen Logik (KGV im Kontext von Wachstumsrate/Marge/Moat-
Qualität, analog zur Multiples-Schnellcheck-Logik aus `jack-moat-reaper-
v11.7.md`). Externe Quellen (GuruFocus, stockanalysis.com, Yahoo Finance
u.ä.) liefern ausschließlich ROHDATEN (aktueller KGV, historischer KGV-
Verlauf, Branchen-Durchschnitt) – NIEMALS wird ein fertiges Drittanbieter-
Urteil ("Significantly Overvalued", "X% above/below Fair Value" o.ä.)
direkt als eigene Einschätzung übernommen oder zitiert. Grund: ein
proprietärer "Fair Value"-Algorithmus einer fremden Webseite ist keine
nachvollziehbare, in unserem eigenen Regelwerk verankerte Methodik – wir
prüfen die Rohzahlen und bilden uns daraus eine EIGENE Meinung. Bei der
Erstbefüllung am 2026-09-03 wurde das an mehreren Stellen nicht sauber
getrennt (GuruFocus-Label direkt übernommen statt nur als Datenpunkt
genutzt) – seither korrigiert, gilt ab jetzt als feste Regel für jede
künftige Pflege dieser Spalte.

**Margin of Safety / historisches Drawdown-Verhalten (2026-09-03, von Brian
ergänzt: "auch die Kurse aus der Vergangenheit mit einbeziehen, z.B. dass
Nvidia in der Vergangenheit auch mal 40-50% korrigieren kann").** "🟢
KAUFEN" heißt NICHT "sicher vor scharfen Korrekturen" – ein günstiges KGV
ggü. der eigenen Historie ist keine Garantie gegen einen erneuten
Rücksetzer, insbesondere bei AI-Trend-/Hype-getriebenen Werten, wo auch
bei intakter fundamentaler These historisch scharfe Korrekturen (30-50%+)
normal sind. Ab jetzt fließt bei AI-Trend-exponierten Werten zusätzlich
das historische Max-Drawdown-Muster in die CRV-Begründung ein (siehe
Tabellen unten), nicht nur der aktuelle KGV-Vergleich. Kein Ersatz für
eigene Positionsgrößen-Disziplin (siehe Sizing-Tiers/Positions-Cap,
Abschnitt 3 architecture.md) – ein 🟢-KAUFEN-Signal bedeutet "günstiger
Einstiegspunkt ggü. Historie", nicht "risikofrei" oder "Kursziel
garantiert".

## Matrix: Geschäftsqualität × CRV (2026-09-03, auf Jack/Conan-Feedback hin ergänzt)

Champions/Profi/Talent zeigt Geschäftsqualität, die CRV-Ampel zeigt den
aktuellen Einstiegszeitpunkt – beides zusammen ergibt die eigentliche
Priorisierung. Faustregel: **Champions+Grün** = höchste Kandidaten-
Priorität (Top-Qualität, günstig), **Talent+Rot** = schlechteste
Kombination (spekulativ UND teuer). Ein "Champions+Rot" ist kein
schlechtes Unternehmen, sondern ein gutes Unternehmen zum falschen Preis.

| Qualität \\ CRV | 🟢 Kaufen | 🟡 Beobachten | 🟠 Vorsicht/Teuer | 🔴 Meiden | 🔘 Grau |
|---|---|---|---|---|---|
| 🏆 Champions (16) | NVDA, V, MA, SPGI, TSM, FICO, CPRT, ROL, USLM (9) | SYK, Keyence, Brookfield, Lasertec (4) | ASML, Hoya, ANET (3) | – | – |
| ⚙️ Profi (10) | WSO (1) | VRT, FTNT, MPWR, AIT, Disco Corp, Asahi Intecc (6) | Exponent (1) | nVent Electric (1) | CrowdStrike (1) |
| 🚀 Talent (4) | – | Innodata, SKWD (2) | – | Palantir, Rorze (2) | – |

**Lesehilfe:** Die 8 Champions+Grün-Werte sind aktuell die "Goldenen
Kaufgelegenheiten" der Liste – hohe Qualität UND günstiger Einstiegspunkt.
nVent Electric ist die einzige Profi+Rot-Kombination (gutes Geschäft,
aktuell klar zu teuer). Bei Talent+Rot (Palantir, Rorze) kommen
spekulatives Risiko UND Überbewertung zusammen – hier ist auch bei
Interesse an der These aktuell kein guter Einstiegszeitpunkt.

## 🏆 Champions (16) – etablierte Weltklasse-Compounder

| Ticker/Börse | ISIN | Firma | Region | Sektor | Herkunft | Status | CRV | Kurzthese |
|---|---|---|---|---|---|---|---|---|
| NVDA (NASDAQ) | US67066G1040 | Nvidia Corp. | USA | Halbleiter (KI-Beschleuniger) | BRIAN | 🆕 | 🟢 KAUFEN – KGV 27,5x, unter eigenem Ø (31,6x). **MoS-Hinweis:** 3 Korrekturen >35% im letzten Jahrzehnt (-56% 2018, -66% 2021/22, -22-25% 2023/24) trotz seither jeweils intakter These – günstiges KGV ist keine Garantie gegen einen erneuten scharfen Rücksetzer, aktueller AI-Capex-Hype erhöht dieses Risiko eher als dass er es senkt. | Dominanter GPU-/KI-Infrastruktur-Anbieter, faktisches Ökosystem-Monopol (CUDA), zentrale Position im KI-Capex-Zyklus. |
| V (NYSE) | US92826C8394 | Visa Inc. | USA | Zahlungsverkehr | BRIAN | 🆕 **[EX-DEPOT]** | 🟢 KAUFEN – KGV 29,6x, unter 3J-Ø (32,4x). **MoS-Hinweis:** historischer Max-Drawdown -51,9% (2009) – auch Zahlungsnetzwerk-Duopole sind nicht immun gegen scharfe Korrekturen in echten Krisen. | Ehemalige Depot-Position (verkauft 27.08.2026 @ 326,40€). Zahlungsnetzwerk-Duopol mit Mastercard, extrem hohe Kapitalrendite. |
| MA (NYSE) | US57636Q1040 | Mastercard Inc. | USA | Zahlungsverkehr | JARVIS | 🆕 | 🟢 KAUFEN – KGV unter 3J/5J-Ø. **MoS-Hinweis:** historischer Max-Drawdown -62,7% (noch tiefer als Visa) – identisches Muster, keine Ausnahme vom Duopol-Bonus. | Direktes Duopol-Pendant zu Visa – falls Visa nicht zurückgekauft wird, naheliegende Alternative mit identischer Moat-Logik. |
| SPGI (NYSE) | US78409V1044 | S&P Global Inc. | USA | Finanzinfrastruktur (Ratings/Indizes/Daten) | BRIAN | 🆕 **[EX-DEPOT]** | 🟢 KAUFEN – KGV 24,9x, -20% ggü. 12M-Ø. **MoS-Hinweis:** 5J-Max-Drawdown -39,8% – auch defensiv wirkende Finanzinfrastruktur kann deutlich korrigieren. | Ehemalige Depot-Position (verkauft 27.08.2026 @ 378,15€). Duopol-Moat bei Ratings/Indizes. |
| SYK (NYSE) | US8636671013 | Stryker Corp. | USA | MedTech (Orthopädie/Chirurgierobotik) | BRIAN | ⚠️ RISIKO **[EX-DEPOT]** | 🟡 BEOBACHTEN – unter Eigenhistorie, aber 44% über Branchen-Ø. **MoS-Hinweis:** historischer Max-Drawdown -58,6% – MedTech mit Robotik-Wachstumsstory ist bei Sentiment-Wechsel überdurchschnittlich anfällig. | Ehemalige Depot-Position (verkauft 27.08.2026 @ 279,75€). Qualitäts-MedTech mit starkem Robotik-Wachstumstreiber (Mako-System). **News-Ampel 2026-09-03:** 🟡 Cybervorfall störte Fertigung (Lieferrückstände), zusätzlich Wolfe-Downgrade auf "Peer Perform" – operative Delle, kein Moat-Verlust. |
| ASML (Amsterdam) | NL0010273215 | ASML Holding N.V. | Europa (NL) | Halbleiterausrüstung (EUV-Lithografie) | JARVIS | 🆕 | 🟠 VORSICHT/TEUER – KGV 52,7x, 42% über 10J-Median – eigene Einordnung: deutlich teuer ggü. eigener Historie. **MoS-Hinweis:** historisch bis -90% Max-Drawdown seit Börsengang, zuletzt -45% seit Hoch Mitte 2024 – bei bereits hoher Bewertung aktuell wenig Sicherheitsmarge gegen eine erneute Korrektur. | EUV-Lithografie-Monopolist – ohne ASML keine Advanced-Chip-Fertigung möglich, der kritischste Baustein der gesamten Halbleiter-Lieferkette. |
| TSM (NYSE ADR) | US8740391003 | Taiwan Semiconductor Mfg. (TSMC) | Asien (Taiwan) | Halbleiter-Auftragsfertigung (Foundry) | JARVIS | 🆕 | 🟢 KAUFEN – KGV 30,2x, -10% ggü. 12M-Ø. **MoS-Hinweis:** historisch bis -89% Max-Drawdown möglich (zyklisches Foundry-Geschäft, geopolitisches Taiwan-Risiko zusätzlich) – auch bei günstigerem KGV bleibt das sektortypische Korrekturrisiko real. | Fertigt die KI-Chips von Nvidia & Co. tatsächlich – größter Foundry-Moat der Welt, strukturelles Kernstück der KI-Lieferkette. |
| FICO (NYSE) | US3032501047 | Fair Isaac Corp. | USA | Finanzdaten/Analytics (Kredit-Scoring) | JARVIS | 🆕 | 🟢 KAUFEN – KGV 30,2x, 39% unter 10J-Median – eigene Einordnung: deutlicher Abschlag zur eigenen Historie. **MoS-Hinweis:** historischer Max-Drawdown -79,3% (2009), aktuell bereits selbst -40,8% im laufenden Drawdown – der günstige KGV-Vergleich spiegelt teilweise genau diesen laufenden Rücksetzer, nicht garantiert reine Stabilität. | Faktisches Monopol beim US-Kredit-Scoring (FICO-Score als Industriestandard) – einer der stärksten Preissetzungsmacht-Moats überhaupt. |
| 6861 (Tokyo) | JP3236200006 | Keyence Corp. | Japan | Fabrikautomatisierung (Sensorik/Machine Vision) | BRIAN | 🆕 **[EX-DEPOT]** | 🟡 BEOBACHTEN – KGV 43,6x, leicht erhöht, unter historischem Hoch (65x). **MoS-Hinweis:** deutlicher Kursrückgang bereits während der Finanzkrise 2008 dokumentiert (genaue % nicht verlässlich recherchierbar) – auch fabless Qualitätskonzerne mit extremer Marge sind in Krisen nicht immun. | Ehemalige Depot-Position (verkauft 27.08.2026 @ 439,90€). Einer der profitabelsten Industriekonzerne der Welt (fabless, extrem hohe Marge). |
| 7741 (Tokyo) | JP3837800006 | Hoya Corp. | Japan | Optik/Halbleiter-Photomasken & MedTech | BRIAN | 🆕 | 🟠 VORSICHT/TEUER – KGV ~32-37x, deutlich über Branchen-Ø (16,6x). **MoS-Hinweis:** Allzeittief während der Finanzkrise 2008 dokumentiert (genaue % nicht verlässlich recherchierbar) – bei bereits hoher Bewertung zusätzlich wenig Sicherheitsmarge. | Diversifizierter Qualitätskonzern mit Weltmarktführerschaft bei Halbleiter-Photomasken-Rohlingen plus stabilem MedTech-Standbein. |
| BN (NYSE/TSX) | CA11271J1075 | Brookfield Corp. | Kanada | Alternative Asset Management/Holding | BRIAN | 🆕 | 🟡 BEOBACHTEN – KGV 78x absolut hoch, aber -28% ggü. 12M-Ø (Holding-Struktur, KGV schwer vergleichbar). **MoS-Hinweis:** historischer Max-Drawdown -63,6% (2009), 5J-Max-Drawdown -42,3% – Asset-Manager-Holdings sind bei Kreditmarkt-Stress überdurchschnittlich exponiert. | Diversifizierter Vermögensverwalter/Holding (Infrastruktur/Erneuerbare/Private Equity) – Compounder über Kapitalallokation statt Einzelprodukt-Moat. |
| CPRT (NASDAQ) | US2172041061 | Copart Inc. | USA | Fahrzeugauktionen/Salvage | JARVIS | ⚠️ RISIKO | 🟢 KAUFEN – KGV 17,4x, 46% unter 10J-Median – eigene Einordnung: deutlicher Abschlag zur eigenen Historie. **MoS-Hinweis:** historisch bis ~-60% Max-Drawdown möglich, aktuell bereits selbst -40,6% vom 52-Wochen-Hoch – der günstige KGV-Vergleich spiegelt zu einem Teil genau diesen laufenden Rücksetzer. | Marktführer bei Online-Fahrzeugauktionen mit Netzwerk-Moat (Flächen/Logistik) und sehr hoher Kapitalrendite. **News-Ampel 2026-09-03:** 🟡 Analysten kappen Kursziel unter aktuellen Kurs, Sorge um Marktanteile im Salvage-Geschäft – gegenläufig prüft Copart selbst eine Übernahme von CCC Intelligent Solutions (Expansion statt Rückzug). |
| ROL (NYSE) | US7757111049 | Rollins Inc. | USA | Schädlingsbekämpfung (Dienstleistung) | JARVIS | ⚠️ RISIKO | 🟢 KAUFEN – KGV 33,2x, 38% unter 10J-Median – eigene Einordnung: deutlicher Abschlag zur eigenen Historie. **MoS-Hinweis:** 5J-Max-Drawdown -30,3% – moderater als viele andere Werte der Liste, aber auch bei "langweiligen" Dienstleistungs-Compoundern nicht ausgeschlossen. | Extrem stabiler, wiederkehrender Cashflow (Abo-artiges Geschäftsmodell), einer der zuverlässigsten Compounder im S&P 500. **News-Ampel 2026-09-03:** 🟡 Schwache Residential-Nachfrage, Kursziel-Konsens von ~59$ auf ~46$ gekappt, Aktie -40% YTD – aber weiter &gt;6% organisches Wachstum &amp; Margenverbesserung für H2 erwartet, Abo-Cashflow-These intakt. |
| 6920 (Tokyo) | JP3979200007 | Lasertec Corp. | Japan | Halbleiterausrüstung (EUV-Masken-Inspektion) | BRIAN | ⚠️ RISIKO | 🟡 BEOBACHTEN – KGV 41,5x, nahe 10J-Median (44,3x), über JP-Sektor-Ø (25,5x). **MoS-Hinweis:** keine spezifische Drawdown-Quelle recherchiert, aber Sektor (Halbleiterausrüstung) strukturell stark zyklisch – analog ASML/TSM historisch 40-90%-Korrekturen möglich. **News-Ampel 2026-09-03:** 🟡 Quartalsumsatz -26% YoY, Marge -829 Bp, Aktie -14% nach Zahlen wegen Sorgen um Margen-Guidance FY2027 – realer Zyklus-Rücksetzer, kein Moat-Bruch. | **Umkategorisiert 2026-09-04 von Talent zu Champions** (Brian: "sind das keine Talente?" – gegenrechercht und bestätigt): de facto 100% Marktanteil bei actinic EUV-Masken-Inspektion (13,5nm) – MATRICS A150 ist das einzige kommerziell verfügbare Werkzeug dieser Art, selbst KLA (deutlich größerer US-Konkurrent) konnte bisher kein gleichwertiges System entwickeln. Proprietäre EUV-Lichtquelle + über 10 Jahre nationale Forschungsprojekte als Eintrittsbarriere. Ein ebenso konzentrierter, technologisch abgesicherter Monopol-Moat wie ASML (bereits Champions) – der aktuelle Umsatzrückgang ist ein realer Zyklus-Rücksetzer (Halbleiterausrüstung ist strukturell zyklisch, siehe ASML/TSM), kein struktureller Bruch der Marktstellung. |
| ANET (NYSE) | US0404132054 | Arista Networks | USA | Netzwerktechnik (Rechenzentren) | BRIAN | 🆕 | 🟠 VORSICHT/TEUER – KGV 63,4x, 54% über 10J-Median. **MoS-Hinweis:** -37% Drawdown allein im Inflations-Schock 2022 – bei aktuell hoher Bewertung kaum Sicherheitsmarge gegen einen ähnlichen Rücksetzer. | **Umkategorisiert 2026-09-04 von Profi zu Champions** ("geschärfter Blick"-Review – gegenrechercht und bestätigt): GAAP-Bruttomarge 64,1% (FY2025)/62,4% (Q1 2026), operative Marge ~43% seit 8 aufeinanderfolgenden Quartalen konstant gehalten – eine Konsistenz, die kein reiner Netzwerktechnik-Wettbewerber in vergleichbarer Wachstumsphase erreicht. Führende Position bei Hochleistungs-Switches für KI-/Cloud-Rechenzentren, Lieferkettenengpässe im Sektor wirken aktuell eher stabilisierend für Aristas Marktposition als schwächend. Die hohe Bewertung ist ein CRV-Timing-Thema (bleibt 🟠 VORSICHT/TEUER), kein Geschäftsqualitäts-Einwand – daher Champions statt Profi. |
| USLM (NASDAQ) | US9119221029 | United States Lime & Minerals | USA | Baustoffe/Industriemineralien | BRIAN | 🆕 | 🟢 KAUFEN – KGV 23,3x, moderat für Nischenmonopolisten. **MoS-Hinweis:** keine spezifische Drawdown-Quelle recherchiert – Handelsvolumen moderat, keine strukturelle Illiquidität, aber Nischenwert mit entsprechend höherer Volatilität möglich. | **Umkategorisiert 2026-09-04 von Talent zu Champions** ("geschärfter Blick"-Review – gegenrechercht und bestätigt): die bisherige "klein/illiquide"-Begründung für Talent war faktisch falsch – Marktkapitalisierung $3,44 Mrd. (Mid-Cap, nicht Small-Cap), tägliches Handelsvolumen ~81.000-217.000 Aktien, keine strukturelle Illiquidität. Operative Marge 42,35%, ROIC 41,90% – regionaler Nischenmonopolist mit sehr hoher, nachhaltiger Kapitalrendite. Derselbe unzulässige Proxy-Fehler (Positionsgröße/Liquidität statt Marge/Marktstellung/Wachstumsverlässlichkeit als Kategorisierungs-Kriterium) wie zuvor bei Allianz/Bank Central Asia im Depot – dort bereits korrigiert, hier nachgezogen. |

## ⚙️ Profi (10) – solide Qualitätsfirmen/Nischenführer, Bewährung läuft noch

| Ticker/Börse | ISIN | Firma | Region | Sektor | Herkunft | Status | CRV | Kurzthese |
|---|---|---|---|---|---|---|---|---|
| CRWD (NASDAQ) | US22788C1053 | CrowdStrike Holdings | USA | Cybersecurity (Endpoint/Cloud) | BRIAN | 🆕 | 🔘 GRAU – KEINE BELASTBARE AUSSAGE – **Anker: KGV ungeeignet** (TTM-EPS nahe Null, GAAP-Verlust durch hohe SBC/Investitionsphase verzerrt), kein tragfähiger Ersatzmaßstab aus dem Fact-Pack ableitbar – für eine echte Einordnung wäre EV/Sales oder Rule-of-40 (Wachstum + FCF-Marge) nötig, nicht im aktuellen Snapshot recherchiert. **MoS-Hinweis:** historischer Max-Drawdown -67,7% – trotz starker Kundenbindung eine der volatileren Cybersecurity-Aktien. | Cloud-native Cybersecurity-Plattform mit hoher Kundenbindung (Falcon), profitiert von wachsender Angriffsfläche – noch nicht so lange bewiesen wie ein Champions-Titel. |
| VRT (NYSE) | US92537N1081 | Vertiv Holdings | USA | Rechenzentrums-Infrastruktur (Kühlung/Stromversorgung) | BRIAN | 🆕 | 🟡 BEOBACHTEN – KGV 58,2x absolut hoch, 16% unter 10J-Median, aber kurze eigenständige Handelshistorie (erst seit 2020) macht die "10J-Median"-Basis selbst wenig belastbar. **MoS-Hinweis:** direktes AI-Rechenzentrums-Play, keine lange eigene Krisen-Historie – Vorsicht vor falscher Sicherheit durch die relative KGV-Zahl. | Zentraler Ausrüster für Rechenzentrums-Kühlung/-Stromversorgung, noch relativ junge Börsenhistorie als eigenständiger Titel. |
| FTNT (NASDAQ) | US34959E1091 | Fortinet Inc. | USA | Cybersecurity (Netzwerksicherheit/Firewalls) | JARVIS | 🆕 | 🟡 BEOBACHTEN – KGV ~54-62x, moderat teuer, aber profitabelster der Cybersecurity-Gruppe. **MoS-Hinweis:** historischer Max-Drawdown -51,2% – geringer als CrowdStrike, aber immer noch ein signifikanter Sektor-Rücksetzer möglich. | Ergänzt CrowdStrike um die Netzwerk-/Firewall-Seite der Cybersecurity-Landschaft – Diversifikation innerhalb des Sektors. |
| MPWR (NASDAQ) | US6098391054 | Monolithic Power Systems | USA | Halbleiter (Power Management) | BRIAN | ⚠️ RISIKO | 🟡 BEOBACHTEN – KGV 74,8x, im Rahmen der eigenen Bewertungsspanne für einen margenstarken Halbleiter-Nischenführer – eigene Einordnung: kein klares Signal, kein Schnäppchen. **MoS-Hinweis:** -46% Drawdown 2022, aktuell bereits wieder -27% vom letzten Hoch – deutliches historisches Korrekturmuster trotz starker Erholungsfähigkeit (+74% 2023). | Nischenführer bei Power-Management-Chips für Rechenzentren/KI-Server, hohe Margen, aber zyklischer als ein reiner Champions-Titel. **News-Ampel 2026-09-03:** 🟡 Weiterhin laufende Kanzlei-Untersuchungen zu Governance-/Fiduciary-Duty-Vorwürfen im Nachgang der Nvidia-Auftragsstornierung 2024; operatives Geschäft aktuell sehr stark (+48% Umsatz), Kundenkonzentrationsrisiko bleibt Beobachtungspunkt. |
| AIT (NYSE) | US03820C1053 | Applied Industrial Technologies | USA | Industrielle Distribution (Antriebstechnik/Automatisierung) | BRIAN | 🆕 | 🟡 BEOBACHTEN – KGV ~25-29x, keine klaren Extremsignale, moderat. **MoS-Hinweis:** keine spezifische Drawdown-Quelle recherchiert, aber als Industriedistributor konjunkturabhängig – bei einem Abschwung realistisch zweistellige Korrekturen möglich. | Qualitäts-Distributor mit stetigem Cross-Selling-Modell, profitiert von Reshoring/Automatisierung in der US-Industrie. |
| 6146 (Tokyo) | JP3548600000 | Disco Corp. | Japan | Halbleiterausrüstung (Wafer-Dicing/-Schleifen) | BRIAN | 🆕 | 🟡 ABWARTEN/BEOBACHTEN – KGV ~50x teuer, FCF-Marge (16,9%) unter 20%-Schwelle, volle Analyse 2026-09-03 (Jarvis ABBRUCH/Jack SCHROTT/Conan BEOBACHTEN 5,5). **MoS-Hinweis:** Halbleiterausrüster generell stark zyklusanfällig (vgl. ASML/TSM: 45-90% Max-Drawdowns historisch) – bei bereits hohem KGV kaum Sicherheitsmarge. | Führend bei Präzisions-Schneide-/Schleiftechnik für Halbleiter-Wafer, profitiert vom Advanced-Packaging-Trend – zyklisches Semicap-Geschäft. |
| WSO (NYSE) | US9426222009 | Watsco Inc. | USA | HVAC-Distribution (Klima-/Heiztechnik) | JARVIS | ⚠️ RISIKO | 🟢 KAUFEN – KGV 26,9x, 6% unter 10J-Ø. **MoS-Hinweis:** historischer Max-Drawdown -64,3% – trotz stabilem Distributionsgeschäft überraschend hohe historische Schwankungsbreite. | Familiengeführter Marktführer in der nordamerikanischen HVAC-Distribution – US-Pendant zur Beijer-Ref-Logik aus dem Nicht-Index-Screening. **ISIN am 2026-09-01 korrigiert** – die ursprünglich erfasste US9427491025 gehört tatsächlich zu Watts Water Technologies, einer anderen Firma; beim Scalable-Watchlist-Abgleich aufgefallen. **News-Ampel 2026-09-03:** 🟡 Q2-EPS klar unter Konsens (4,00$ vs. 4,41$ erwartet), Kurs -11% seit Zahlen, Morgan Stanley senkt Kursziel – erste spürbare Delle in der sonst sehr verlässlichen HVAC-Distributionsthese. |
| NVT (NYSE) | IE00BDVJJQ56 | nVent Electric plc | USA/Irland | Elektrotechnik (Verbindungs-/Schutztechnik) | BRIAN | 🆕 | 🔴 MEIDEN/ÜBERBEWERTET – KGV 55,1x, 171% über 10J-Median – eigene Einordnung: stärkstes Überbewertungssignal der Liste. **MoS-Hinweis:** historischer Max-Drawdown -56,2% – Überbewertung UND hohe Grundvolatilität gleichzeitig, doppelt ungünstige Kombination. | Profiteur von Elektrifizierung, Rechenzentrums-Ausbau und Reshoring; solide, aber weniger dominant als ein Champions-Titel. |
| EXPO (NASDAQ) | US30214U1025 | Exponent, Inc. | USA | Wissenschaftlich-technisches Consulting (Gerichtsgutachten/Produktsicherheit/Schadensanalyse) | JARVIS | 🆕 | 🟠 VORSICHT/TEUER – KGV ~27-35x, deutlich über Branchen-Ø (18x). **MoS-Hinweis:** historischer Max-Drawdown -86,4% – trotz kapitalleichtem, margenstarkem Geschäftsmodell die höchste recherchierte Drawdown-Zahl der ganzen Watchlist. | 2026-08-29 aus gezielter Depot-Lücken-Suche: kapitalleichtes Reputations-/Expertise-Moat-Geschäft (ROIC ~27%, Nettomarge ~20%), unkorreliert zu bestehenden Software-/Fintech-/Space-Positionen. Bewusster Gegenentwurf zur AIT-Analyse (margenschwacher Distributor) – hier margenstark und asset-light. Wachstum moderat (~9%), daher Profi statt Champions. |
| 7747 (Tokyo) | JP3110650003 | Asahi Intecc Co. | Japan | MedTech (Führungsdrähte für Katheter) | BRIAN | 🆕 | 🟡 ABWARTEN/BEOBACHTEN – KGV ~25x forward nicht günstig. **MoS-Hinweis:** keine spezifische Drawdown-Quelle recherchiert, aber konzentriertes Nischengeschäft (Guidewires) macht das Unternehmen anfällig für Einzelrisiken (z.B. Wettbewerb/Rückruf) – höhere Vorsicht als bei diversifizierteren Werten angebracht. | **Umkategorisiert 2026-09-04 von Talent zu Profi** (Brian: "sind das keine Talente?" – gegenrechercht und bestätigt): >50% globaler Marktanteil bei PCI-Guidewires (Top-5-Gesamtmarkt mit Boston Scientific/Terumo/Abbott/Medtronic, aber klare Führung speziell im PCI-Segment), operative Marge konstant 20-25% dank vertikal integrierter Fertigung. Das ursprüngliche "gemischte Rating" (Jarvis ABBRUCH/Jack SCHROTT/Conan BEOBACHTEN 6) war primär ein Datenlücken-Artefakt (fehlende FCF-/Bilanz-Primärquellen lösten Jacks bekannten Reflex-Abbruch-Bug aus, siehe HANDOVER.md 10.13), keine echte Geschäftsqualitäts-Schwäche – die verifizierten Kennzahlen (ROIC/ROCE 23,21%, operative Marge 29,71%, Umsatzwachstum +21,2% YoY) passen klar zu "gute bis hohe Margen und Wachstumsrate, kein Monopol" – der Profi-Definition, nicht Talents "eventuell noch unprofitabel". |

## 🚀 Talent (4) – spekulative Spitze, hohes Risiko/hohe Upside

| Ticker/Börse | ISIN | Firma | Region | Sektor | Herkunft | Status | CRV | Kurzthese |
|---|---|---|---|---|---|---|---|---|
| PLTR (NASDAQ) | US69608A1088 | Palantir Technologies | USA | Software (Daten-/KI-Plattform) | BRIAN | 🆕 | 🔴 MEIDEN/ÜBERBEWERTET – Forward-KGV ~98-176x, "much of future growth already reflected in price". **MoS-Hinweis:** -85% Max-Drawdown 2021-2022 trotz seither operativ deutlich verbesserter Story – bei aktuell erneut extremer Bewertung ist ein ähnlich scharfer Rücksetzer nicht auszuschließen. | Trotz riesiger Marktkap ein echter Talent-Fall: extreme Bewertung, These noch nicht über einen vollen Zyklus bewiesen – Größe schützt hier nicht vor Risiko. |
| INOD (NASDAQ) | US4576422053 | Innodata Inc. | USA | Daten-/KI-Trainingsdienstleistungen | BRIAN | 🆕 | 🟡 BEOBACHTEN – KGV 52,5x vs. Branchen-Ø 23,3x, aber starkes Momentum (+86% YTD). **MoS-Hinweis:** kleine, illiquide AI-Nebenwert-Aktie ohne belastbare eigene Drawdown-Historie – Vergleichsgruppe (kleine AI-Profiteure) historisch extrem volatil, Positionsgröße entsprechend vorsichtig wählen trotz Momentum. | Kleiner, spekulativer Profiteur des KI-Booms (Daten-Annotation für große KI-Modelle), Kundenkonzentrationsrisiko. |
| SKWD (NASDAQ) | US8309401029 | Skyward Specialty Insurance | USA | Spezialversicherung (Nischen-Underwriting) | BRIAN | 🆕 | 🟡 BEOBACHTEN – KGV 15x, nah am fairen Wert (14,7x), leicht über Branche (11,6x). **MoS-Hinweis:** 3J-Max-Drawdown -36,5% – noch kurze Börsenhistorie, daher wenig belastbare Langzeit-Datenbasis für die Krisenfestigkeit. | Kleinerer Spezialversicherer mit diszipliniertem Underwriting, noch kurze Börsenhistorie – bereits Gegenstand einer früheren TMR-Analyse (siehe `analysen/`). |
| 6323 (Tokyo) | JP3982200002 | Rorze Corp. | Japan | Halbleiterausrüstung (Wafer-Handling-Robotik) | BRIAN | ⚠️ RISIKO | 🔴 MEIDEN/ÜBERBEWERTET – Marktkap +137% bei Nettogewinn -19% – eigene Einordnung: Bewertung läuft der Ertragsentwicklung erkennbar davon. **MoS-Hinweis:** Kombination aus kleiner Marktkap, Zyklik und Bewertungs-Ertrags-Schere ist ein klassisches Setup für eine scharfe Korrektur – praktisch keine Sicherheitsmarge vorhanden. | Kleiner Nischenzulieferer für Wafer-Transport-Robotik – hohe Relevanz für den Fab-Ausbau, aber kleine, zyklische Firma. **News-Ampel 2026-09-03:** 🟡 Erdbeben (Kumamoto) legte Kyushu-Werk zeitweise lahm (Betrieb inzwischen wieder hochgefahren), Jahresgewinn -19% – temporärer externer Schock zusätzlich zur bereits bestehenden Bewertungs-Warnung. |

---

## Lateinamerika / sonstige Schwellenländer – noch offen

Aus dem Nicht-Index-Screening vom 2026-08-28 (siehe
`analysen/nicht-index-screening-konsolidiert-2026-08-28.md`) kam kein Name,
der gleichzeitig die Qualitäts-/Big-Player-Logik dieser Watchlist UND eine
echte Lateinamerika-Zuordnung erfüllt (Alicorp/Peru wäre der einzige echte
Kandidat, käme als Talent-Position infrage, aber noch nicht offiziell
aufgenommen – siehe Offene Punkte).

**Update 2026-08-31 (täglicher Kandidaten-Scan, voller 3-fach-Quick-Filter,
siehe `analysen/WEGE3-TMR-cross-check-fazit-2026-08-31.md`):** WEG S.A.
(WEGE3, ISIN BRWEGEACNOR0, B3 São Paulo, Brasilien, Elektrotechnik/
Industrieautomation) besteht Strategie-Fit-Gate, Duplikations-Check und
Identity-Gate klar, und alle drei KIs (Jarvis/Jack/Conan) stufen die
Unternehmensqualität einstimmig als Champion-Tier ein (ROIC 32-36%, Wide
Moat, Net Cash, globale Diversifikation) – aber ebenso einstimmig
**VERDICT: BEOBACHTEN/WATCH**, da die aktuelle Bewertung (~33-34x KGV) keine
Sicherheitsmarge lässt (kein Sofort-Kauf-Signal). **Noch NICHT formal in die
Champions-Tabelle aufgenommen**, da die Watchlist bei 30/30 (Obergrenze)
steht und ein Ersatz eines bestehenden Champions-Werts (mehrere davon von
Brian bewusst als Ex-Depot-Wiederaufnahme-Kandidaten markiert) eine
Entscheidung ist, die über die tägliche Scan-Routine hinausgeht – Brian
entscheidet, ob WEG einen Slot bekommt oder vorerst nur hier als
LatAm-Beobachtungsposten außerhalb der 30er-Kapazität geführt wird. Nächster
Prüfpunkt: Rücksetzer Richtung 23-25x KGV (Jack) würde die Einschätzung
deutlich verbessern.

---

## Aufnahme-Kriterien (für künftige automatisierte Ergänzungen)

Ein Kandidat wird nur bei freiem Slot (siehe Obergrenze 20-30, aktuell 29)
aufgenommen, wenn mindestens eines zutrifft:
1. **Qualitäts-Compounder mit klarem Moat**, der im TMR-Sinne (siehe `prompts/`)
   potenziell KAUFEN/BEOBACHTEN-Niveau erreichen könnte → Kategorie **Champions**.
2. **Solide Nischenfirma/Qualitätswert**, dessen Langfrist-Bewährung noch läuft
   oder die zyklischer/konzentrierter ist → Kategorie **Profi**.
3. **"Big Player"-Potenzial-Kandidat** (Scout-Pfad-Logik) mit plausibler These,
   künftig deutlich größer/relevanter zu werden, aber mit echtem spekulativem
   Risiko → Kategorie **Talent**.
4. **Möglicher Ersatzkandidat** für eine bestehende, schwächere Depot-Position.
5. **Ex-Depot-Position**, die Brian bewusst weiter im Blick behalten will.

## Ausschluss-/Abstiegs-Kriterien (täglich per Ampel + wöchentlich vertieft geprüft)

**Seit 2026-09-03:** Zusätzlich zur wöchentlichen Tiefenprüfung (Freitag,
Wochenfazit) läuft täglich (Teil des Täglichen Trigger-Checks) eine
schnelle 🔴/🟡/🟢-Ampel über alle Werte unten – siehe architecture.md,
"Watchlist-System", "Tägliche Watchlist-News-Ampel". Ein 🔴-Fund führt zur
sofortigen Entfernung noch am selben Tag, nicht erst freitags.

Ein Wert fliegt von der Watchlist, wenn mindestens eines zutrifft:
1. **Katastrophale Quartalszahlen** (Umsatz-/Gewinneinbruch, Guidance-Cut) ohne
   glaubwürdige Erholungsstory.
2. **Gerissene fundamentale These** – der ursprüngliche Moat-/Wachstumsgrund ist
   nicht mehr intakt (z.B. Verlust des Technologie-Vorsprungs, neuer
   disruptiver Wettbewerber).
3. **Fraud-/Bilanzskandal, Going-Concern-Warnung oder harter Regulatorik-
   Schlag** (Kartellstrafe, Produktverbot, Sanktion).
4. **Übernahme oder Delisting** – der Wert verschwindet schlicht vom Markt.
5. **Manuelle Entscheidung von Brian** – jederzeit möglich, unabhängig vom
   automatisierten Check.

Reine Kursrückgänge oder eine "nur" hohe Bewertung sind für sich genommen KEIN
Ausschlussgrund – die Watchlist bildet Unternehmensqualität ab, nicht Timing
(das übernimmt bei Bedarf der TA-Pfad). Ein Wert KANN aber zwischen Kategorien
wandern (z.B. Profi → Champions nach mehreren bewiesenen Quartalen, oder
Champions → Talent bei aufkommenden Zweifeln), ohne die Watchlist komplett zu
verlassen.

**Entfernung heißt Archivierung, nicht Löschen (2026-09-03, aus dem
3-KI-System-Audit, P2-Punkt Conans):** ein 🔴-Ausschluss wird NICHT
stillschweigend aus der Datei gelöscht, sondern in den Abschnitt
"Ausschluss-Archiv" unten verschoben (Ticker, Datum, Kategorie zum
Ausschlusszeitpunkt, Ausschlussgrund, letzter CRV-Stand) – so bleibt
nachvollziehbar, welche Werte wann aus welchem Grund geflogen sind, statt
dass die Historie mit jeder Watchlist-Bearbeitung verloren geht.

## Ausschluss-Archiv

_Noch keine archivierten Ausschlüsse._

<!-- Format je archiviertem Eintrag:

### TICKER - Firmenname (Ausschluss: YYYY-MM-DD)
- Kategorie zum Ausschlusszeitpunkt: Champions/Profi/Talent
- Ausschlussgrund: [1-5 aus der Liste oben, kurz begründet]
- Letzter CRV-Stand vor Ausschluss: [Farbe + Kurzbegründung]

-->

## Offene Punkte
- Lateinamerika-Slot bewusst leer gelassen (siehe oben) – Alicorp (Peru) als
  möglicher erster Talent-Kandidat steht zur Diskussion mit Brian an.
- Kategorisierung (Champions 13 / Profi 9 / Talent 7) ist eine erste,
  systematische Einordnung von Jarvis nach Marktkap/Reifegrad/Zyklik-Logik –
  Brian kann jederzeit einzelne Werte manuell verschieben, falls er einen
  Wert anders einschätzt (z.B. Palantir wurde bewusst als Talent statt
  Champions eingestuft, trotz großer Marktkapitalisierung, wegen des
  Bewertungsrisikos).
- ISINs wurden am 2026-08-28 per WebSearch verifiziert (Quellen: justetf.com,
  divvydiary.com, cbonds.com, MarketScreener u.a.) – bei einer echten Order
  sollte die ISIN nochmal beim jeweiligen Broker gegengecheckt werden.
