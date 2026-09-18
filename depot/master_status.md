**Nachtrag 2026-09-09 ~Nachmittag (ad-hoc-chat, Depot-Update, KORRIGIERTE
FASSUNG – Brian wies die erste Fassung zurecht als falsch zurück):** Erste
Fassung dieses Depot-Updates enthielt zwei echte Fehler aus WebSearch-
Kursabfragen: **A10 Networks wurde fälschlich mit ~38$ statt real 24,94$
angegeben (behaupteter +54%-Anstieg existierte nicht)**, zusätzlich war
auch Rambus falsch (104,69$ statt real 87,20$). Beide per Twelve Data
(zuverlässige Primärquelle) korrigiert – Twelve Data wird ab jetzt für
jeden Basic-Plan-fähigen Ticker VOR WebSearch verwendet, WebSearch nur noch
als Fallback für Ticker ohne Twelve-Data-Abdeckung (Kanada/TSX/TSXV,
London, Paris, teils Xetra). **Korrigiertes Gesamtdepot: 33.602,29 €**
(-3,98% ggü. Wochenfazit-Baseline 07.09. [34.992,90 €], -2,63% ggü. 08.09.
[34.523,35 €]) – etwas schwächer als in der fehlerhaften Erstfassung
berichtet, aber weiterhin kein Material-Shift. Größte reale Bewegungen:
SoFi weiterhin stärkste Position (+43,5% ggü. Investsumme, Twelve-Data-
bestätigt), Constellation Software +29,8% (nur WebSearch-basiert, TSX
nicht über Twelve Data Basic abrufbar, daher geringere Konfidenz als die
Twelve-Data-Werte), Rambus jetzt schwächste Einzelposition (-15,7%, nicht
wie ursprünglich berichtet leicht positiv). Cash-Position weiterhin
praktisch bei Null (Scalable 0€) – kein aktiver Cash-vs-Invest-
Entscheidungsbedarf. Beide offenen Empfehlungen (Kraken Robotics ≤2,80 CAD,
Rambus ≤65€/$75) bleiben von ihrer Nachkauf-Zone entfernt, auch nach
Korrektur (Rambus jetzt $87,20 statt fälschlich $104,69 – aber immer noch
deutlich über der $75-Marke). EZB-Ratssitzung 09./10.09.2026 nächster
relevanter Katalysator (Allianz/Münchener Rück/Hermès-Exposure). Details
siehe `depot/finanzen-net-zero.md`, `depot/trade-republic.md`,
`depot/smartbroker-plus.md`, `depot/scalable-capital.md` (je Update
2026-09-09, finanzen-net-zero.md mit vollständiger Fehler-Dokumentation).

**Nachtrag 2026-09-08 ~19:15 UTC (taeglicher-trigger-check):** ruhiger Tag,
kein Anlass. Scalable live abgefragt (`ping` OK), Holdings/Cash/Transaktionen
geprüft - **Cash-Verrechnungskonto zeigt live 0,00 € statt der zuletzt
gemeldeten 460,33 € (07.09.)**, keine erklärende Transaktion in
`list_portfolio_transactions` gefunden (einziger Treffer seit Checkpoint ist
weiterhin die bereits verarbeitete Sparplanrate) - transparent als
unerklärte Abweichung vermerkt statt stillschweigend übernommen, kein
Anlass für eine Eskalation (keine Order-relevante Handlung möglich/nötig,
reines Beobachtungsfeld für den nächsten Lauf). Depot-/Watchlist-News-Scan
(alle 18 Depot- + 30 Watchlist-Werte, gebündelte WebSearches) ohne neue
🔴/🟡-Funde - bestehende Flags (MPWR/WSO/SYK) unverändert. Markt-/Makro-
Kontext: kein Material Shift (VIX 15,64 (+2,23%), F&G weiter Fear-Zone ~42,
S&P -0,15%/NQ100 -0,48%, SPY weiter klar über 50D/200D-SMA, 200D-SMA
weiter steigend). **Kalender-Hinweis:** EZB-Ratssitzung bereits morgen/
übermorgen (09./10.09.2026) - Erinnerung in die Tages-Mail aufgenommen.
Kuchendiagramm aktualisiert (`reports/portfolio_pie_2026-09-08.png`,
Gesamtwert 34.523,35 € statt 34.992,90 € am 07.09. - Rückgang primär durch
den o.g. Cash-Rückgang auf 0€, keine Kategorie-/Regel-Schwelle verletzt).
Gezielter Japan/Asien-Lücken-Rechercheauftrag an Jack+Conan (siehe
`depot/bridge_status.md`) lieferte 10 neue Kandidatennamen (Sansan,
Smaregi, VRAIN Solution, Shin-Etsu Chemical, Park Systems, OBIC, GMO
Payment Gateway, eGuarantee, SMC Corp, AirTAC International) - als Backlog
vermerkt (Abschnitt 8), noch KEIN Strategie-Fit-/Duplikations-/Identity-
Gate oder 3-fach-Quick-Filter in diesem Lauf durchlaufen (Zeitpriorität).
Keine offene Empfehlung fällig zur Erinnerung (Kraken/Rambus zuletzt erst
07.09. erinnert). Bestätigungsmail verschickt (siehe Verifikation unten).

**Nachtrag 2026-09-17 (Depot- und Watchlist-Komplettupdate, live, Scalable-Capital-Reconnect erfolgreich):** Scalable-Capital-Verbindung war seit dem 17.09. kurzzeitig unauthentifiziert, von Brian re-authentifiziert (siehe `project_scalable_capital_mcp_auth_fehlt.md`, GELÖST). Alle 4 Broker frisch geprüft, soweit live erreichbar:

| Broker | Wert (17.09.) | Vorheriger Stand |
|---|---|---|
| Scalable Capital (Gold+BCA+Vanguard-ETF, Cash 0€) | 10.596,26 € | 10.585,46 € (09.09.) |
| finanzen.net zero (11 von 15 Positionen live aktualisiert) | 21.123,39 € | 21.084,86 € (09.09.) |
| Trade Republic (Allianz, Xetra nicht live abrufbar) | 512,09 € | unverändert (09.09.) |
| Smartbroker+ (HawkEye 360) | 1.407,62 € | 1.419,89 € (09.09.) |
| **Gesamt (4 Broker)** | **33.639,36 €** | ~34.523 € (08.09.) — **-2,56%** |

**Wichtigste Einzelfunde:** (1) CBOE ist von +4,0% auf **-4,0%** gedreht (Full-Deep-Dive-Tag 16.09., -4,96%-Tagesverlust) — Kurs $270,43 sitzt praktisch genau an der Tranche-1-Nachkaufzone ($268-270), noch keine bestätigte Stabilisierung. (2) Rambus weiter geschwächt (-20,4% ggü. Einstand, war -15,7%), nähert sich der $68-75-Abstauberzone weiter an. (3) A10 Networks/Intuitive Surgical/ServiceNow deutlich erholt. (4) Die am 08.09. "unerklärte" Scalable-Cash-Abweichung (460,33€→0€) ist geklärt: eine reguläre interne Überweisung vom 07.09., keine Dateninkonsistenz. (5) **Neuer bestätigter Twelve-Data-Fund:** Xetra/Frankfurt jetzt zusätzlich zu TSX/TSXV/LSE/Paris auf dem aktuellen Tarif gesperrt — betrifft Münchener Rück und Allianz, die deshalb weiterhin nicht live aktualisiert werden können. (6) Scalable-Watchlist aufgeräumt: 9 verworfene/kaputte Einträge entfernt (Rorze, Novo Nordisk, UCB, Aurinia, Ligand, ITOCHU, Vietnam Enterprise, Qnity Electronics, ein unauflösbarer ISIN-Eintrag), 48 statt 57 Einträge übrig.

**Nicht in diesem Lauf gemacht (Transparenz):** keine vollständige Neubewertung der CRV-Ampeln/Kategorie-Zuordnung (das wäre ein Wochenfazit-artiger Rechercheaufwand) — nur Kursaktualisierung + Auffälligkeiten-Check. Watchlist-CRV-Ampeln bleiben auf dem Stand vom 03./04.09. (bis auf die bereits dokumentierten Einzel-Updates).

**Nachtrag 2026-09-17 ~13:15 UTC (taeglicher-trigger-check, Folgelauf nach
dem Depot-Komplettupdate desselben Tages):** Pending-Queue leer. 2 neue
Scalable-Transaktionen seit Checkpoint (BCA-Dividende + automatisches
Reinvestment, 15./16.09.) als routinemäßig gewertet, kein Cross-Check nötig
- Checkpoint auf 2026-09-16T14:18:59.156Z vorgezogen. Watchlist-News-Ampel
(gebündelt) ohne neue 🔴/🟡-Funde - bestehende Flags MPWR/WSO/SYK/FICO
unverändert; die gefundene Rambus-DOJ-Subpoena-Meldung datiert auf Juni
2026 (bereits bekannt/eingepreist, kein neuer Fund). Fed hat am 16.09. wie
zu ~90-92% erwartet um 25 Bp auf 3,75-4,00% angehoben (erste Anhebung seit
2023) - keine Überraschung, daher kein Material Shift trotz der
grundsätzlichen Tragweite; BoJ-Entscheid (17./18.09.) zum Zeitpunkt dieses
Laufs noch offen. Kraken Robotics (zuletzt erinnert 07.09., 8 Werktage) und
Rambus (zuletzt erinnert 09.09., 6 Werktage) waren fällig zur Erinnerung -
beide weiterhin weit von ihrer Nachkaufzone entfernt (Kraken 4,69 CAD vs.
Zone ≤2,80 CAD; Rambus $85,28 vs. Zone $68-75) - Erinnerung per E-Mail +
PushNotification verschickt, `depot/offene_empfehlungen.md` aktualisiert.
Kuchendiagramm neu erzeugt (`reports/portfolio_pie_2026-09-17.png`,
Gesamtwert 33.639,41 € auf Basis des heutigen Komplettupdates). Japan/
Asien-Kandidaten-Backlog (10 Namen, siehe Abschnitt 8) bewusst nicht
weiterbearbeitet (Zeitpriorität, Komplettupdate lief bereits heute).

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

**Nachtrag 2026-09-07 ~19:15 UTC (taeglicher-trigger-check, Folgelauf 2):**
zweiter Trigger-Check-Lauf desselben Tages (nach abab2f3, ~17:00 UTC) -
neue Hermes-Cron-Automatisierung feuert den Task offenbar mehrfach am
selben Tag, wie am 2026-09-04 bereits einmal beobachtet, Ursache weiterhin
ungeklärt. Inhaltlich nichts Neues: `list_portfolio_transactions` seit dem
Checkpoint (07.09. 10:55 UTC) liefert nur die bereits verarbeitete
Sparplanrate, Checkpoint unverändert. Zusätzlich zum vorherigen Lauf: alle
30 Watchlist-Werte per gebündelter Websuche auf News-Ampel geprüft (Punkt
3B) - keine neuen 🔴/🟡-Funde, bestehende Flags (MPWR/WSO/SYK) unverändert.
Kraken/Rambus-Erinnerung nicht erneut nötig (bereits heute im Vorlauf
erinnert). Bestätigungsmail verschickt (Message-ID 1a07d4722696b7ea).

**Zuletzt aktualisiert:** 2026-09-07 ~17:15 lokale Zeit (`wochenfazit`-Lauf,
ersetzt den entfernten nativen Scheduled-Task-Eintrag 1:1 – Automatisierung
läuft seither über Hermes-Cron). Deckt bewusst nur ein **verkürztes
3-Tage-Fenster** seit dem letzten Wochenfazit (04.09.2026) ab. Frühere
2026-09-07-Aktivität bereits committet (e603bbd: BONESUPPORT-Aufnahme;
abab2f3: Scalable-Reconnect, Cash/Pie-Update, Offene-Empfehlungen-
Erinnerung). **Dieser Wochenfazit-Lauf:** Depotwert 34.992,90 € (-0,12%
ggü. Baseline 30.08.), Portfolio-Regel-Check mit frischen Zahlen neu
gerechnet (Abschnitt 7 unten aktualisiert), performance_tracking.csv/md
neue Zeile (07.09.), alle 5 Charts + Benchmark-Chart neu erzeugt,
earnings_calendar.md Rorze→BONESUPPORT nachgezogen, 8-seitiges
Wochenfazit-PDF gebaut (`reports/Wochenfazit-2026-09-07.pdf`, 1,1 MB,
Erfolgs-Verifikation bestanden: Datei existiert, plausible Größe). Keine
Kategorie-/CRV-Änderungen ggü. 04.09. (kein neuer Trigger, US-Feiertag
Labor Day am 07.09. ohne neue US-Handelssession). **Bekannte Abweichung
von der Skill-Vorgabe, transparent benannt:** SendUserFile war in dieser
Session nicht als Tool verfügbar; der E-Mail-Versand mit PDF-Anhang wurde
versucht, aber aus Vorsicht vor Anhang-Korruption (die Base64-Kodierung des
~640 KB-PDFs hätte in dieser Session nur über ~70 einzelne, manuell
zusammenzusetzende Chunk-Reads reproduziert werden können – hohes Risiko
eines stillen Übertragungsfehlers) bewusst NICHT angehängt – stattdessen
Text-Zusammenfassung per E-Mail verschickt, PDF liegt vollständig im Repo
(committet+gepusht). Push-Notification versucht, aber nicht zugestellt
(Remote Control in dieser Session inaktiv). Beides im Chat gegenüber Brian
explizit benannt, nicht stillschweigend übergangen. – nächste reguläre
Aktualisierung beim nächsten `taeglicher-trigger-check`- bzw.
`wochenfazit`-Lauf.

**Nachtrag 2026-09-07 ~17:35 (Folge-Trigger, PDF-Anhang-Fix versucht):**
in einer Folge-Session gezielt geprüft, ob der Base64-über-Bash-Workaround
(PDF → `base64 -i` → Textdatei → als `content` ins `attachments`-Array)
funktioniert. **Ergebnis: strukturell nicht machbar, kein session-
spezifisches Vorsichts-Problem.** Das 1,1-MB-PDF ergibt als Base64 ~1,4 MB
Text; schon der Lese-Versuch dieser Zwischen-Textdatei per Read-Tool schlägt
mit derselben harten 256-KB-Grenze fehl, die auch fürs direkte PDF-Lesen
gilt. Diese Grenze ist nicht auf Read beschränkt – sie spiegelt die
praktische Obergrenze für Inhalte, die als einzelnes Tool-Call-Argument
generiert werden können; ein `send_message`-Aufruf mit ~1,4 MB Base64 im
`content`-Feld müsste ich als Modell in EINEM Antwort-Turn ausgeben, was
weit über jedes realistische Output-Token-Budget pro Turn hinausgeht.
Chunk-weises Lesen der Base64-Datei löst das nicht, weil am Ende trotzdem
alles in einem einzigen Tool-Aufruf zusammengeführt werden müsste. **Fazit:
PDF-Anhang per Inline-Base64 ist mit den aktuell verfügbaren Tools
(kein `SendUserFile`, keine Datei-Referenz-Option im `send_message`-Schema)
für Dateien dieser Größenordnung nicht zuverlässig möglich, unabhängig von
Read- vs. Bash-Kodierweg.** Keine erneute (doppelte) E-Mail verschickt, da
die inhaltsgleiche Text-Zusammenfassung bereits um 17:17 zugestellt wurde
– ein zweiter, fast identischer Mail-Versand wäre nur Spam ohne Mehrwert.
`reports/wochenfazit/SKILL.md` entsprechend korrigiert (siehe dortiger
Versionsvermerk), damit künftige Läufe diesen Workaround nicht wiederholt
ergebnislos versuchen. Echter Fix bräuchte entweder ein Tool mit
Datei-Referenz statt Inline-Content (z.B. `SendUserFile`, falls in einer
Session verfügbar) oder einen Cloud-Link (z.B. Drive) statt Anhang.

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
| CBOE Holdings | Nachkauf-Zone, gestaffelt (KAUFEN, Tier 2) | Tranche 1: $268-270 · Tranche 2: $255-262 |
| Hermès | Nachkauf-Zone (Preisalarm) | ≤1.350€ (Kurs 18.09. bereits nahe/an der Zone, 1.353-1.387€) |

## 7a. Portfolio-Regel-Check — AKTUALISIERT 2026-09-17 (Region-/Sektor-Diskrepanz geklärt)

**Fund beim Nachrechnen (Brian: "kläre das jetzt"):** eine erste Schnellrechnung kam auf USA≈38% statt der dokumentierten 53,65% — Ursache war ein reiner Rechenfehler (ETF-Wert nur im Nenner mitgezählt, aber nicht per `ETF_REGION_SPLIT`/`ETF_SECTOR_SPLIT` (siehe `reports/weekly_charts.py`) auf die Regionen/Sektoren verteilt). Mit korrigierter Methodik und heutigen Live-Zahlen (Depot-Komplettupdate vom 17.09., Gesamtwert 33.639,41 €, Stocks+ETF-Basis 33.145,36 €):

| Region | Real (17.09.) | Ziel-Band | Status | Vorher (07.09.) |
|---|---|---|---|---|
| USA/Nordamerika | 53,28% | ≤55-60% | erfüllt | 53,65% (nahezu unverändert) |
| Europa/UK | 15,54% | 15-20% | **jetzt im Zielband** | 14,73% (knapp unterbesetzt) |
| Japan/Asien | 9,57% | 10-15% | unterbesetzt | 9,49% (nahezu unverändert) |
| Sonstige (CA/IL) | 16,77% | kein festes Band | unverändert ausgelastet | 17,10% |
| Lateinamerika | 4,83% | kein festes Band | unverändert | 5,04% |

| Sektor | Real (17.09.) | Ziel-Band | Status | Vorher (07.09.) |
|---|---|---|---|---|
| Finanzwesen | 32,58% | 20-25% | **weiterhin klar über Zielband** | 33,32% |
| Technologie/Halbleiter | 29,71% | 30-35% | knapp unterbesetzt | 29,57% |
| Rest | 17,05% | 5-10% | über Zielband | 16,88% |
| Industriewerte | 11,60% | 10-15% | im Zielband | 11,86% |
| Gesundheitswesen | 9,06% | 10-15% | unterbesetzt | 8,38% |

**ETF-Anteil:** 24,23% des Gesamtportfolios (Ziel ≥50%, weiterhin VERSTOSS, aber im gewohnten langsamen Aufbau via 600€/Monat-Sparplan — war 23,40% am 07.09.). **Positionsgrößen:** größte Position SoFi 10,89% (innerhalb der dokumentierten 12%-Ausnahme, kein Verstoß), keine Position unter der 1%-Mindestgrenze.

**Konsequenz unverändert:** kein automatisches Verkaufssignal. Finanzwesen bleibt der einzige echte Struktur-Überhang, Japan/Asien und Gesundheitswesen bleiben die priorisierten Lücken für neues Kapital — deckt sich mit der bereits laufenden Priorisierung (Hoya/Disco/Asahi-Intecc-Zielzonen).

## 7. Portfolio-Regel-Check (echt berechnet, 2026-09-07, historisch — siehe 7a oben für den aktuellen Stand)

**Methodik:** Live-Positionswerte Scalable Capital (ETF, Bank Central Asia,
Gold, Cash) zum 07.09., übrige 3 Broker unverändert aus `depot/*.md` vom
04./05.09. übernommen (keine neue US-Handelssession seit 04.09., US-
Feiertag Labor Day am 07.09.) + echte Vanguard-FTSE-All-World-Regions-/
Sektor-Gewichte (offizielles Factsheet, Stand 31.07.2026,
justETF/vanguard.co.uk). Gold-ETC und Cash bewusst aus Region/Sektor
ausgeschlossen (siehe `scalable-capital.md`). Portfolio-Gesamtwert
(Aktien+ETF): 34.034,17 €. Gesamtportfolio inkl. Gold+Cash: 34.992,90 €.

### Region

| Topf | Real | Ziel-Band | Status |
|---|---|---|---|
| USA/Nordamerika (inkl. Kanada) | **53,65%** | ≤55-60% | erfüllt (unter der weichen 55%-Grenze) |
| Europa/UK | 14,73% | 15-20% | knapp unterbesetzt |
| Japan/Asien | 9,49% | 10-15% | unterbesetzt |
| Rest (MercadoLibre/LatAm 5,04% + Kraken/Constellation/Cellebrite 17,10% zusammen als "Sonstige") | **17,10%** (Sonstige) + **5,04%** (LatAm) | *kein festes Band, "nur bei echten Kandidaten"* | Sonstige-Topf weiterhin ausgelastet – neue Nicht-LatAm/Europa/Asien-Kandidaten zurückhaltend priorisieren |

### Sektor

| Topf | Real | Ziel-Band | Status |
|---|---|---|---|
| Technologie/Halbleiter | 29,57% | 30-35% | knapp unterbesetzt |
| **Finanzwesen** | **33,32%** | **20-25%** | **weiterhin über dem Zielband** |
| Gesundheitswesen | 8,38% | 10-15% | unterbesetzt |
| Industriewerte | 11,86% | 10-15% | im Zielband |
| Rest | 16,88% | 5-10% | über dem Zielband |

**Faktor-/Korrelations-Cluster (NEU, 2026-09-09, ergänzt die obige
GICS-artige Sektor-Sicht um quer laufende Faktoren – siehe
`depot/faktor_korrelations_analyse.md` für die volle Analyse):**
Regierungs-/Verteidigungsbudget-Abhängigkeit 14,7% (Cellebrite, HawkEye
360, Kraken Robotics, Rocket Lab – über 3 verschiedene Sektor-Etiketten
verteilt, daher oben unsichtbar), Hochbeta-Kleinkapitalisierer 11,3%
(22,8% inkl. SoFi), zinssensitive Finanzwerte 10,3%. Kein Handlungszwang,
monatlich im Monatsrecap aktualisiert.

**Eine verbleibende Näherung, transparent:** MercadoLibre wird
näherungsweise 45%/55% auf Finanzwesen (Mercado Pago)/Rest (E-Commerce)
gesplittet, keine exakte Segment-Umsatzzahl verwendet.

**Konsequenz:** kein automatisches Verkaufssignal (siehe Agent-Playbook.md),
Struktur ggü. 04.09. praktisch unverändert (einzige Bewegung: ETF-Anteil
21,7%→23,40% durch die 07.09.-Sparplanrate) – Kandidaten aus Finanzwesen/
USA weiter niedriger priorisieren, Japan/Asien/Gesundheitswesen/Europa-UK
bevorzugen.

### Positionsgrößen (% von Gesamtportfolio 34.992,90 €, Stand 07.09.)

Größte Position: SoFi Technologies 11,39% (innerhalb der 12%-Ausnahme).
Kleinste: Rambus 1,25% (über der 1%-Mindestgrenze, keine Grenzfall-Markierung
nötig). ETF-Anteil 23,40% (Ziel ≥50%, VERSTOSS, aber verbessert ggü. 21,7%
am 04.09.).

## 8. Offene gezielte Kandidatensuchen (Portfolio-Lücken-Regel)

| Lücke | Zuletzt geprüfter Kandidat | Ergebnis | Nächster Schritt |
|---|---|---|---|
| Talent-Slot (Watchlist) + Europa/UK + Gesundheitswesen | BONESUPPORT Holding AB (BONEX) | **Aufgenommen 07.09.2026** (3-fach-Quick-Filter einstimmig BEOBACHTEN-STARK, ersetzt Rorze) | Erledigt für diesen Slot – Beobachtungspunkt: CERAMENT-V-FDA-Entscheidung (Datenpaket fällig 31.10.2026) |
| Japan/Asien-Region (weiterhin unterbesetzt, 9,49% vs. 10-15%) | Rorze (6323) | Durchgefallen (3-fach Scout-Check, 04.09.2026) – Moat 2/4, Wachstum eingebrochen | **17.09.2026 (Brian): Kandidaten-Pipeline vorerst abgeblasen.** Die 10 am 08.09. gefundenen Namen (Sansan, Smaregi, VRAIN Solution, Shin-Etsu Chemical, Park Systems, OBIC, GMO Payment Gateway, eGuarantee, SMC Corp, AirTAC International) bleiben unverarbeitet als Backlog dokumentiert (kein Gate-Check/Quick-Filter durchlaufen), werden aber NICHT weiter aktiv verfolgt, bis Brian das reaktiviert. Stattdessen aktueller Fokus: Zielzonen für bereits bekannte Japan-Watchlist-Werte (Asahi Intecc/Hoya/Disco) herleiten, siehe watchlist.md. Kein Datenverlust – die 10 Namen bleiben hier als Wiedereinstiegspunkt notiert. |

## 9. Letzte Scheduled-Task-Läufe

Quelle: `depot/bridge_status.md` (Log) + `list_scheduled_tasks` (Live-Stand).

| Task | Letzter Lauf | Nächster Lauf |
|---|---|---|
| taeglicher-trigger-check | 2026-09-17 ~13:15 UTC (regulärer Lauf, ruhiger Tag, kein Trigger, Kraken/Rambus-Erinnerung verschickt, Kuchendiagramm auf Basis des heutigen Depot-Komplettupdates neu erzeugt) | täglich ~21:03 lokale Zeit |
| blitz-scan | 2026-09-04 ~16:15 UTC (Bridges FAIL, Jarvis-Only) | stündlich |
| wochenfazit | 2026-09-07 ~17:15 lokale Zeit (ersetzt den entfernten nativen Scheduled-Task-Eintrag, läuft ab jetzt über Hermes-Cron; verkürztes 3-Tage-Fenster seit 04.09., PDF gebaut+committet, E-Mail als Text-Zusammenfassung ohne Anhang verschickt – siehe Kopfnotiz oben) | Freitag, nächster reg. Lauf voraussichtlich 11.09.2026 |
| monatsrecap | noch nicht gelaufen | 28.-31. des Monats |

## 10. Cash-Stand (nur Scalable Capital, live abrufbar)

Stand 2026-09-17 ~13:15 UTC (live verifiziert): verfügbare Kaufkraft/
Cash-Bestand weiterhin **0,00 €** (die frühere 08.09.-Abweichung ist geklärt
- reguläre interne Überweisung vom 07.09., siehe Nachtrag 17.09. oben). Für
die drei manuellen Broker (finanzen.net zero, Trade Republic, Smartbroker+)
kein Live-Zugriff für Trade Republic (Xetra gesperrt), die anderen beiden
per Twelve Data frisch – siehe jeweilige `depot/*.md`-Datei. Gesamt-
portfoliowert (alle 4 Broker inkl. Cash+Gold, Stand 17.09.-
Komplettupdate, siehe `reports/portfolio_pie_2026-09-17.png`): 33.639,41 €.
