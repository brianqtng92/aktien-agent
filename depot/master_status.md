# Master-Status – Aktien-Agent (Brian)

**Zweck (2026-09-04, von Raketentonis "Master-Status"-Konzept übernommen,
siehe Agent-Playbook.md "Informations-Vorrang-Hierarchie" für die
vollständige Einordnung):** EIN konsolidiertes Status-Dashboard für den
schnellen Überblick – v.a. beim Einstieg in einen neuen Chat oder
Scheduled-Task-Lauf ohne Erinnerung an vorherige Sessions, damit nicht
6+ Einzeldateien gelesen werden müssen, um den aktuellen Stand zu
verstehen. **Ersetzt NICHT die Detail-Dateien** – für die vollständige
Begründung/Historie einer einzelnen Position bleiben
`depot/kategorisierung.md`, `watchlist.md` etc. maßgeblich. Wird am Ende
jedes `taeglicher-trigger-check`- und `wochenfazit`-Laufs aktualisiert.

**Zuletzt aktualisiert:** 2026-09-07 ~15:00 UTC (regulärer
`taeglicher-trigger-check`-Folgelauf, ersetzt einen abgebrochenen Versuch
desselben Tages ~22:55 UTC, der ohne Commit/E-Mail endete, siehe
`depot/bridge_status.md`). Frühere 2026-09-07-Aktivität desselben Tages
bereits committet (Commit e603bbd): automatisierte Portfolio-Lücken-
Kandidatensuche, Talent-Slot-Trigger ausgelöst, Jack+Conan gezielt befragt,
BONESUPPORT Holding AB nach vollem 3-fach-Quick-Filter in die Watchlist
aufgenommen, ersetzt Rorze (siehe Abschnitt 4 + 8). **In diesem Folgelauf:**
Scalable-Capital-MCP-Verbindung war wieder funktionsfähig (`ping` → pong,
der zuvor gemeldete "needs to reconnect"-Zustand war offenbar transient/
zwischenzeitlich vom Nutzer behoben) – Depot-Live-Scan, Cash-Stand
(460,33 € Kaufkraft/Cash, nach Ausführung der monatlichen ETF-Sparplanrate),
Kuchendiagramm (Stand 07.09., Gesamtwert ~34.992,90 €) und
Transaktions-Erkennung nachgeholt: 1 neue Transaktion seit Checkpoint
(Vanguard-FTSE-All-World-Sparplanausführung, 599,9999 €, 07.09.), als
routinemäßig gewertet, kein 3-fach-Cross-Check-Anlass. Jack/Conan-Bridges
heute grundsätzlich erreichbar (ToolSearch erfolgreich), aber nicht
eingesetzt, da kein Trigger vorlag. Watchlist-Tages-Ampel/Markt-Makro-
Kontext/Kandidaten-Scan für 2026-09-07 bereits durch den früheren Lauf
desselben Tages abgedeckt, nicht erneut dupliziert. Offene-Empfehlungen-
Erinnerung (Kraken Robotics, Rambus, seit 2026-09-01 unverändert, 5+
Werktage) heute per E-Mail ausgelöst (siehe Abschnitt 4). Earnings-Kalender
geprüft: kein Termin für heute fällig. Pending-3fach-Queue: leer. – nächste
reguläre Aktualisierung beim nächsten `taeglicher-trigger-check`-Lauf.

---

## 1. Kategorie-Struktur Depot ("10-7-3"-Ziel)

| Kategorie | Ziel | Ist | Freie Slots |
|---|---|---|---|
| Champions | 10 | 10 | exakt auf Ziel |
| Profi | 7 | 7 | exakt auf Ziel |
| Talent | 3 | 1 | **2 frei** |

Quelle: `depot/kategorisierung.md`, Abschnitt "Ziel-Positionsanzahl".
Talent liegt seit heute unter statt auf Ziel (Kraken Robotics + HawkEye 360
wurden zu Profi hochgestuft) – kein Verkaufssignal, reine Folge korrigierter
Fehlzuordnungen.

## 2. Kategorisierungs-Kriterien (Champions/Profi/Talent)

Quelle: `Agent-Playbook.md` Abschnitt 3 (qualitative Kriterien) +
"[1.5]/[2] KATEGORISIERUNG" (Bucket-Modell). Die feste Ist-Zuordnung steht
in `depot/kategorisierung.md`/`watchlist.md` – hier nur die Kriterien,
NICHT pro Analyse neu erraten (siehe Abschnitt 1).

**Die drei gültigen Kriterien – NIEMALS Positionsgröße/Alter/Land/Marktkap
als Proxy:** Marge (Höhe+Nachhaltigkeit) · Marktstellung/Moat (Monopol/
Quasi-Monopol vs. Nischenführer vs. unbewiesen) · Wachstumsverlässlichkeit
(verlässlich hoch vs. solide vs. spekulativ).

| Kategorie | Kern-Definition |
|---|---|
| Champions | Weltklasse: hohe/sehr hohe Marge, Monopol-/Quasi-Monopolstellung, verlässlich hohes Wachstum |
| Profi | "Zweite Reihe": gute bis hohe Marge/Wachstum, Moat/Wachstumsverlässlichkeit noch nicht voll bewiesen |
| Talent/Zock | Ggf. noch unprofitabel, spekulatives Risiko (Bewertung/Zyklik/Datenlage), Nische mit Potenzial oder Momentum |

**Bucket A-D → TMR- vs. Scout-Pfad (ersetzt alte Größen-/Alters-Heuristik):**
- **A** Compounder Candidate (bereits bewiesene Qualität) / **C**
  Mispricing-Re-Rating (gefallene Bewertung, stabile Fundamentaldaten) →
  **TMR-Pfad**, volle harte Kriterien (mehrjährig FCF-positiv,
  ROIC-Schwelle, Pricing Power).
- **B** Quality in Formation (Wachstum/Marge verbessert sich, Moat noch
  nicht bewiesen) / **D** Speculative Optionality (jung/klein,
  Marktpotenzial) → **Scout-Pfad**, weichere Ersatzkriterien
  (Rule-of-40/Sales-Efficiency bzw. ersatzweise Umsatzwachstum >25% UND
  Bruttomarge >65%).

**Fallback bei widersprüchlichen/fehlenden Reifemetriken:** TMR nur, wenn
Historie/Datenqualität ausreicht UND Rule-of-40/Sales-Efficiency erfüllt
ist. Nur Wachstum+Bruttomarge erfüllt, Effizienz nicht prüfbar → Scout (im
Zweifel Scout, nicht TMR). Ist Umsatzbasis/Wachstum/Bruttomarge selbst
nicht sinnvoll messbar (Pre-Revenue, Biotech ohne Umsatz, Banken/
Rohstofffirmen) → weder automatisch TMR noch Scout, manuelle Klärung durch
Jarvis vor dem Deep-Dive.

## 3. Kategorie-Struktur Watchlist (30 Werte gesamt)

| Kategorie | Anzahl |
|---|---|
| Champions | 17 |
| Profi | 10 |
| Talent | 3 |

Quelle: `watchlist.md`, "Aktueller Stand".

## 4. Watchlist-Kompaktübersicht (30 Werte, Detail/volle These: `watchlist.md`)

Zweck: schneller Abgleich – "gibt es schon einen ähnlichen/besseren
Kandidaten in dieser Kategorie/Region?" – bei neuen Kauf-Kandidaten. CRV-
Ampel = Chance-Risiko-Verhältnis/Einstiegszeitpunkt, NICHT Geschäftsqualität
(🟢 Kaufen · 🟡 Beobachten · 🟠 Vorsicht/Teuer · 🔴 Meiden · 🔘 keine
belastbare Aussage). Volle Thesen/Begründungen bleiben in `watchlist.md`.

| Ticker | Kategorie | CRV | Kurzthese |
|---|---|---|---|
| NVDA | Champions | 🟢 | GPU-/KI-Infra-Monopol (CUDA), Inferenz-Marktanteilsrisiko im Blick |
| V | Champions | 🟢 | Zahlungs-Duopol mit Mastercard, extrem hohe Kapitalrendite |
| MA | Champions | 🟢 | Duopol-Pendant zu Visa, identische Moat-Logik |
| SPGI | Champions | 🟢 | Ratings-/Indizes-Duopol, defensive Finanzinfrastruktur |
| SYK | Champions | 🟡 | MedTech, starker Robotik-Wachstumstreiber (Mako), kurzer Cyber-Vorfall |
| ASML | Champions | 🟠 | EUV-Lithografie-Monopolist, kritischster Halbleiter-Lieferkettenbaustein |
| TSM | Champions | 🟢 | Größter Foundry-Moat, fertigt praktisch alle KI-Chips |
| FICO | Champions | 🟢 | Kredit-Scoring-Monopol, bröckelt bei Hypotheken (VantageScore-Zulassung) |
| Keyence (6861) | Champions | 🟡 | Fabless-Sensorik, extrem hohe Marge, profitabelster Industriekonzern |
| Hoya (7741) | Champions | 🟠 | EUV-Photomasken-Duopol plus MedTech-Standbein, teuer |
| Brookfield (BN) | Champions | 🟡 | Diversifizierter Vermögensverwalter, Compounder über Kapitalallokation |
| Lasertec (6920) | Champions | 🟡 | De-facto-Monopol EUV-Masken-Inspektion, Zyklus-Erholung läuft |
| Arista (ANET) | Champions | 🟠 | Führend bei KI-Rechenzentrums-Switches, konstante Marge, teuer |
| USLM | Champions | 🟢 | Regionaler Kalk-/Baustoff-Monopolist, sehr hohe Kapitalrendite |
| Vertiv (VRT) | Champions | 🟡 | Marktführer KI-Kühlung/-Stromversorgung, expandierende Marge |
| Fortinet (FTNT) | Champions | 🟡 | Profitabelster Cybersecurity-Anbieter, klarer Marktanteilsgewinn |
| Exponent (EXPO) | Champions | 🟠 | Gerichtsgutachten-Consulting, elite Kapitalrendite, teuer |
| CrowdStrike (CRWD) | Profi | 🔘 | Cloud-Cybersecurity, hohe Kundenbindung, Bewährung läuft noch |
| Monolithic Power (MPWR) | Profi | 🟡 | Power-Management-Nischenführer, zyklischer, Governance-Untersuchung läuft |
| Applied Industrial (AIT) | Profi | 🟡 | Industrie-Distributor, Cross-Selling, Reshoring-Profiteur |
| Disco Corp (6146) | Profi | 🟡 | Dominant bei Wafer-Dicing, aber zyklisches Semicap-Geschäft |
| Watsco (WSO) | Profi | 🟢 | HVAC-Distributionsführer, temporäre Margen-Normalisierung |
| nVent Electric (NVT) | Profi | 🔴 | Elektrifizierungs-Profiteur, weniger dominant, deutlich überbewertet |
| Asahi Intecc (7747) | Profi | 🟡 | Marktführer PCI-Guidewires, konstant gute Marge |
| Copart (CPRT) | Profi | 🟢 | Salvage-Auktions-Duopol, aber realer Kundenverlust an IAA |
| Rollins (ROL) | Profi | 🟢 | Schädlingsbekämpfung, Wachstums-/Margendelle bei Residential-Segment |
| Skyward Specialty (SKWD) | Profi | 🟡 | Diszipliniertes Spezialversicherungs-Underwriting, kurze Börsenhistorie |
| Palantir (PLTR) | Talent | 🔴 | KI-Datenplattform, extreme Bewertung, These noch unbewiesen |
| Innodata (INOD) | Talent | 🟡 | Kleiner KI-Daten-Annotationsdienstleister, Kundenkonzentrationsrisiko |
| BONESUPPORT (BONEX) | Talent | 🟡 | Schwedischer MedTech, CERAMENT-Plattform mit FDA-De-Novo-Moat, Bewertung nicht günstig |

## 5. Offene Prüfpunkte / Checkpoints (chronologisch, wo bekannt)

| Position | Kontext | Kategorie | Prüfpunkt-Termin/Auslöser |
|---|---|---|---|
| Cellebrite DI Ltd | Depot, Profi | Guidance-Cut-Nachprüfung | Q3-Earnings (~Nov 2026), Guidance $145-148 Mio – dann 3 Re-Rating-Trigger neu prüfen |
| Rocket Lab USA | Depot, Talent | Nachkauf-Aufstufungs-Trigger | Q3-Zahlen (Guidance: Umsatz $250-265 Mio, Adj.-EBITDA-Verlust $17-23 Mio) – Neutron-Erstflug/Verwässerungstempo/Burn-Multiple prüfen |
| Rollins (ROL) | Watchlist, Profi (abgestuft 04.09.) | mögliche Rückstufung zu Champions | H2-2026-Verbesserung laut Management-Guidance – noch unbestätigt |
| Fair Isaac (FICO) | Watchlist, Champions (Beobachtungspunkt) | mögliche Abstufung zu Profi | belastbare Daten zur VantageScore-Adoptionsrate bei GSE-Hypotheken |
| Constellation Software | Depot, Champions (Beobachtungspunkt) | organisches Wachstum | Q4 2026/Q1 2027 – sollte Richtung 5-6% zurückkehren |
| MercadoLibre | Depot, Champions (Beobachtungspunkt) | operative Marge | Q4 2026/Q1 2027 – sollte sich Richtung zweistellig erholen |
| Münchener Rück | Depot, Champions (Beobachtungspunkt) | Rückversicherungs-Preiszyklus | Januar-2027-Erneuerungen + FY2026-Combined-Ratio vs. ~80%-Guidance |
| Bank Central Asia | Depot, Champions (Beobachtungspunkt) | NIM-Erholung | nächste 2-3 Quartale, sollte sich mit BI-Zinsstabilisierung erholen |
| Watsco (WSO) | Depot, Profi (Beobachtungspunkt) | Margen-Normalisierung | nächste 1-2 Quartale beobachten |
| BONESUPPORT (BONEX) | Watchlist, Talent (neu 07.09., ersetzt Rorze) | CERAMENT-V-FDA-Entscheidung | Datenpaket fällig spätestens 31.10.2026, danach FDA-Antwort – De-Risking-Trigger für mögliche Aufstufung |

## 6. Offene Kauf-/Verkauf-Empfehlungen

Quelle: `depot/offene_empfehlungen.md` (dort maßgeblich, hier nur Kurzstand).

| Position | Empfehlung | Zone/Preis |
|---|---|---|
| Kraken Robotics | Nachkauf-Zone (Preisalarm) | ≤2,80 |
| Rambus | Nachkauf-Zone (Preisalarm) | ≤65 |

## 7. Portfolio-Regel-Check (echt berechnet, 2026-09-04)

**Methodik:** Live-Positionswerte aller 18 Depot-Einzelwerte (4 Broker,
Kraken/RKLB/HawkEye mit frischen Twelve-Data-Kursen aktualisiert) + echte
Vanguard-FTSE-All-World-Regions-/Sektor-Gewichte (offizielles Factsheet,
Stand 31.07.2026, justETF/vanguard.co.uk) – NICHT mehr aus dem Gedächtnis
geschätzt. Gold-ETC und Cash bewusst ausgeschlossen (siehe
`scalable-capital.md`). Portfolio-Gesamtwert (Aktien+ETF): ~33.576 €.

### Region

**Update 2026-09-04 (Methodik-Lücke geschlossen):** Agent-Playbook.md wurde
präzisiert – der vierte Topf heißt jetzt explizit "Rest (Lateinamerika,
Naher Osten/Israel, sonstige)" statt nur "Lateinamerika/sonstige Länder".
Cellebrite (Israel) zählt damit offiziell in diesen Topf.

| Topf | Real | Ziel-Band | Status |
|---|---|---|---|
| USA/Nordamerika (inkl. Kanada) | **63,03%** | ≤55-60% | **bestätigt über der harten Grenze** |
| Europa/UK | 14,72% | 15-20% | knapp unterbesetzt |
| Japan/Asien | 9,79% | 10-15% | unterbesetzt |
| Rest (MercadoLibre/LatAm 4,98% + Cellebrite/Israel 6,20% + ETF-Rest 1,29%) | **12,47%** | *kein festes Band, "nur bei echten Kandidaten"* | faktisch bereits ausgelastet durch Cellebrite allein – neue Nicht-LatAm/Europa/Asien-Kandidaten zurückhaltender priorisieren |

### Sektor

| Topf | Real | Ziel-Band | Status |
|---|---|---|---|
| Technologie/Halbleiter | 29,05% | 30-38% | knapp unterbesetzt |
| **Finanzwesen** | **36,17%** | **20-25%** | **massiv über dem Zielband** (neu entdeckt, vorher unbekannt) |
| Gesundheitswesen | 8,51% | 10-15% | unterbesetzt |
| Industriewerte | 11,37% | 10-15% | im Zielband |
| Rest | 14,90% | 5-10% | über dem Zielband |

**Eine verbleibende Näherung, transparent:** MercadoLibre wurde
näherungsweise 45%/55% auf Finanzwesen (Mercado Pago)/Rest (E-Commerce)
gesplittet, keine exakte Segment-Umsatzzahl verwendet. ETF-"Rest"-Anteil
bei Region (~5,7%) nicht weiter aufgeschlüsselt (Vanguard-Factsheet deckt
nur Top-15-Länder ab, 94,3% der ETF-Ländergewichtung).

**Konsequenz:** kein automatisches Verkaufssignal (siehe Agent-Playbook.md),
aber die neue Portfolio-Lücken-Kandidatensuche-Pflicht sollte Kandidaten
aus Finanzwesen/USA jetzt konsequent niedriger priorisieren, Kandidaten aus
Japan/Asien, Gesundheitswesen oder Europa/UK bevorzugen.

## 8. Offene gezielte Kandidatensuchen (Portfolio-Lücken-Regel)

| Lücke | Zuletzt geprüfter Kandidat | Ergebnis | Nächster Schritt |
|---|---|---|---|
| Talent-Slot (Watchlist) + Europa/UK + Gesundheitswesen | BONESUPPORT Holding AB (BONEX) | **Aufgenommen 07.09.2026** (3-fach-Quick-Filter einstimmig BEOBACHTEN-STARK, ersetzt Rorze) | Erledigt für diesen Slot – Beobachtungspunkt: CERAMENT-V-FDA-Entscheidung (Datenpaket fällig 31.10.2026) |
| Japan/Asien-Region (weiterhin unterbesetzt, 9,79% vs. 10-15%) | Rorze (6323) | Durchgefallen (3-fach Scout-Check, 04.09.2026) – Moat 2/4, Wachstum eingebrochen | Vollständige Nikkei225/TOPIX-Durchsuchung weiterhin ausstehend – bisherige Läufe (05.09., 07.09.) fanden über Jack/Conan primär Europa/Gesundheitswesen-Kandidaten (BONESUPPORT, PeptiDream als Rückstellung), noch kein systematischer Nikkei225/TOPIX-Indexdurchlauf – nächster Lauf sollte gezielt einen echten Japan/Asien-Abschnitt (z.B. Nikkei225 Top 50 nach Marktkap) vollständig durchgehen, da BONESUPPORT die Region-Lücke nicht schließt (Schweden = Europa) |

## 9. Letzte Scheduled-Task-Läufe

Quelle: `depot/bridge_status.md` (Log) + `list_scheduled_tasks` (Live-Stand).

| Task | Letzter Lauf | Nächster Lauf |
|---|---|---|
| taeglicher-trigger-check | 2026-09-07 ~15:00 UTC (regulärer Folgelauf, Scalable-Capital wieder erreichbar, Bridges erreichbar aber nicht benötigt, keine inhaltlichen Trigger ausgelöst) | täglich ~21:03 lokale Zeit |
| blitz-scan | 2026-09-04 ~16:15 UTC (Bridges FAIL, Jarvis-Only) | stündlich |
| wochenfazit | noch nicht gelaufen | Freitag, ~22:03 lokale Zeit |
| monatsrecap | noch nicht gelaufen | 28.-31. des Monats |

## 10. Cash-Stand (nur Scalable Capital, live abrufbar)

Stand 2026-09-07 ~15:00 UTC (live verifiziert): verfügbare Kaufkraft/
Cash-Bestand 460,33 € (Rückgang ggü. 05.09. durch Ausführung der
monatlichen 600-€-ETF-Sparplanrate am 07.09.). Für die drei manuellen
Broker (finanzen.net zero, Trade Republic, Smartbroker+) kein Live-Zugriff
– siehe jeweilige `depot/*.md`-Datei für den zuletzt gemeldeten Stand.
Gesamtportfoliowert (alle 4 Broker inkl. Cash+Gold, Scalable-Anteil live,
übrige Broker Stand 05.09., siehe `reports/portfolio_pie_2026-09-07.png`):
~34.993 €.
