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

## 7. Portfolio-Regel-Check (echt berechnet, 2026-09-07)

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
| Japan/Asien-Region (weiterhin unterbesetzt, 9,79% vs. 10-15%) | Rorze (6323) | Durchgefallen (3-fach Scout-Check, 04.09.2026) – Moat 2/4, Wachstum eingebrochen | Vollständige Nikkei225/TOPIX-Durchsuchung weiterhin ausstehend – bisherige Läufe (05.09., 07.09.) fanden über Jack/Conan primär Europa/Gesundheitswesen-Kandidaten (BONESUPPORT, PeptiDream als Rückstellung), noch kein systematischer Nikkei225/TOPIX-Indexdurchlauf – nächster Lauf sollte gezielt einen echten Japan/Asien-Abschnitt (z.B. Nikkei225 Top 50 nach Marktkap) vollständig durchgehen, da BONESUPPORT die Region-Lücke nicht schließt (Schweden = Europa) |

## 9. Letzte Scheduled-Task-Läufe

Quelle: `depot/bridge_status.md` (Log) + `list_scheduled_tasks` (Live-Stand).

| Task | Letzter Lauf | Nächster Lauf |
|---|---|---|
| taeglicher-trigger-check | 2026-09-07 ~15:00 UTC (regulärer Folgelauf, Scalable-Capital wieder erreichbar, Bridges erreichbar aber nicht benötigt, keine inhaltlichen Trigger ausgelöst) | täglich ~21:03 lokale Zeit |
| blitz-scan | 2026-09-04 ~16:15 UTC (Bridges FAIL, Jarvis-Only) | stündlich |
| wochenfazit | 2026-09-07 ~17:15 lokale Zeit (ersetzt den entfernten nativen Scheduled-Task-Eintrag, läuft ab jetzt über Hermes-Cron; verkürztes 3-Tage-Fenster seit 04.09., PDF gebaut+committet, E-Mail als Text-Zusammenfassung ohne Anhang verschickt – siehe Kopfnotiz oben) | Freitag, nächster reg. Lauf voraussichtlich 11.09.2026 |
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
