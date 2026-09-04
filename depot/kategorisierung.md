# Champions/Profi/Talent – feste Zuordnungstabelle

**Zweck (2026-09-03, nach Brians Kritik "bei der Zuordnung müsst ihr schon
einer Meinung sein"):** Diese Datei ist die EINZIGE Quelle für die Frage
"welcher Kategorie gehört Position X an". Kein Report, keine PDF, kein
Scheduled Task und keine Analyse (egal ob Jarvis, Jack oder Conan) darf die
Kategorie-Zuordnung neu erraten oder aus Proxies (Positionsgröße, Land/
Emerging-Markets-Status, Datenlücken in der Kaufhistorie) ableiten. Eine
Zuordnung wird nur bei Neuaufnahme (Watchlist→Depot) oder bewusster
Neubewertung im Wochenfazit geändert – dann hier aktualisiert, mit
Begründung und Datum.

## Kriterien (Quelle: architecture.md, Brians Formulierung 2026-08-29)

- **Champions** – absolute Weltklasse-Unternehmen: hohe/sehr hohe Margen,
  Monopol- oder Quasi-Monopolstellung, hohe und verlässliche
  Wachstumsraten.
- **Profi** – die "zweite Reihe": gute bis hohe Margen und Wachstumsrate,
  aber (noch) nicht Monopol-/Quasi-Monopolstellung wie Champions.
- **Talent/Zock** – eventuell noch unprofitabel, nischiges/interessantes
  Geschäftsmodell mit Wachstumsfaktor, der schnell in Richtung
  Profitabilität führen kann, oder Momentum-/Hype-getrieben.

**Wichtig, explizit NICHT als Kriterium zulässig:** Positionsgröße
(kleine Position ≠ automatisch Talent), Land/Emerging-Markets-Status
(EM ≠ automatisch spekulativ) und Lücken in der internen
Kaufhistorien-Dokumentation (ein Dokumentationsproblem ist kein
Geschäftsqualitäts-Urteil). Nur die drei oben genannten Kriterien
(Marge, Marktstellung, Wachstumsverlässlichkeit) entscheiden.

## Ziel-Positionsanzahl: "10-7-3" (festgesetzt 2026-09-03, korrigiert 2026-09-03)

**10 Champions / 7 Profi / 3 Talent = 20 Einzelwerte gesamt** (siehe
architecture.md, Abschnitt 3, für die vollständige Begründung). Ursprünglich
als "10-6-4" festgelegt – noch am selben Tag im 3-KI-System-Audit als
rechnerisch fehlerhaft erkannt (der 10%-Positionsdeckel gilt fürs
Gesamtportfolio, die 40%-Talent-Grenze fürs Aktienanteil – beides zu
vermischen ergab die falsche Zahl 4 statt korrekt 3) und auf "10-7-3"
korrigiert. **Vorbehalt:** die "3" hängt am aktuellen Aktienanteil-Anteil
(~74% des Gesamtportfolios) – wächst der ETF-Anteil wie geplant, sinkt
diese Zahl rechnerisch weiter (siehe architecture.md für Details), daher
kein für immer fixer Wert.

| Kategorie | Ziel | Ist (04.09.2026) | Freie Slots |
|---|---|---|---|
| Champions | 10 | 9 | 1 frei |
| Profi | 7 | 6 | 1 frei |
| Talent | 3 | 3 | **exakt auf Ziel** |

**Update 2026-09-04 (im Tagesverlauf, zwei Korrekturrunden):** Zuerst
Cellebrite von Talent zu Profi umkategorisiert (Profi 5→6, Talent 5→4).
Dann, nach Brians Einwand zu CBOE ("extrem einmaliges Geschäftsmodell")
und SoFi: CBOE von Profi zu Champions (echtes SPX-/VIX-Exklusivmonopol,
gegenrecherchiert und bestätigt), SoFi von Talent zu Profi (9 Quartale
GAAP-profitabel, gegenrecherchiert und bestätigt, mit einem transparent
benannten Vorbehalt – laufender Muddy-Waters-Short-Report, siehe
Profi-Tabelle). Talent-Rebalancierung damit **exakt auf Ziel** erreicht,
ohne dass eine einzige Position tatsächlich verkauft wurde – die
ursprünglichen Talent-Zuordnungen von Cellebrite/SoFi und die
Profi-Zuordnung von CBOE waren schlicht zu konservativ/falsch (derselbe
Proxy-Fehlertyp wie bei Allianz/Bank Central Asia am 03.09.).

## CRV-Ampel (2026-09-03, von Brian gefordert: "das soll auch für Depot-Werte gelten")

Dieselbe CRV-Ampel wie in `watchlist.md` (Definition dort vollständig,
siehe "CRV-Ampel" + "Margin of Safety / historisches Drawdown-Verhalten"),
jetzt auch für alle 18 Depot-Positionen. **Vier Stufen, eigene Depot-
Formulierung (2026-09-03, auf Jack/Conan-Feedback hin präzisiert – "MEIDEN"
klingt bei einer bestehenden Position wie ein Verkaufssignal, ist aber
keins):**
- 🟢 **NACHKAUF ATTRAKTIV** – klar unterbewertet ggü. eigener Historie/Peers, These intakt.
- 🟡 **HALTEN/BEOBACHTEN** – fair bewertet, kein starkes Signal in beide Richtungen.
- 🟠 **KEIN NACHKAUF (TEUER)** – spürbar teuer ggü. Historie/Peers, aber kein hartes Warnsignal (spekulativ, nicht fundamental gebrochen).
- 🔴 **KEIN NACHKAUF – ÜBERBEWERTET (Review empfohlen)** – deutlich überbewertet und/oder mehrere gleichzeitige Warnsignale; löst KEINEN automatischen Verkauf aus, aber eine bewusste Prüfung, ob die These die Überbewertung rechtfertigt.
- 🔘 **GRAU – KEINE BELASTBARE AUSSAGE** (siehe `watchlist.md`, identisches Prinzip) – KGV liefert kein sinnvolles Ergebnis und kein tragfähiger Ersatzmaßstab ist verfügbar.

**Bewertungsanker je Geschäftsmodell** (siehe `watchlist.md`, identisches
Prinzip): bei den drei Versicherern/der Bank im Depot (Münchener Rück,
Allianz, Bank Central Asia) ist **KBV/ROE** der sachlich passendere Anker
als KGV – Versicherer/Banken werden am Markt strukturell über
Buchwert-Multiples bewertet, nicht über Gewinn-Multiples wie
Industrie-/Tech-Werte. Bei Kraken Robotics und HawkEye 360 ist KGV wegen
fehlender/verzerrter Gewinnhistorie nicht sinnvoll anwendbar.

**Wichtig:** Die CRV-Ampel bei einer bestehenden Depot-Position ist KEIN
automatisches Verkaufssignal – dafür gelten weiterhin ausschließlich die
in `analysen/*.md` dokumentierten Abstauber-/Stop-These-Trigger (siehe
"Verkaufsdisziplin & Gewinnmitnahme-Regeln", architecture.md). Die Ampel
zeigt nur, ob ein NACHKAUF zum aktuellen Preis eine gute Idee wäre. Stand
2026-09-03 (WebSearch-Snapshot), Pflege ab jetzt wöchentlich über den
Wochenfazit-Lauf
(analog Watchlist).

**Trend-Pfeile bei Auf-/Abstufung** (siehe `watchlist.md`, "CRV-Ampel",
identisches Prinzip): 🔺 bei Verbesserung ggü. letzter Prüfung, 🔻 bei
Verschlechterung, kein Pfeil bei unveränderter Einstufung. Stand
2026-09-03 ist die Basislinie, noch ohne Pfeile.

## Matrix: Geschäftsqualität × CRV (2026-09-03, auf Jack/Conan-Feedback hin ergänzt)

Analog zur Watchlist-Matrix (siehe `watchlist.md`) – zeigt auf einen
Blick, welche Depot-Positionen aktuell nachkaufwürdig sind (nach
Qualitätsstufe geordnet) und wo Vorsicht angebracht ist.

| Qualität \\ CRV | 🟢 Nachkauf attraktiv | 🟡 Halten/Beobachten | 🟠 Kein Nachkauf (teuer) | 🔴 Kein Nachkauf – überbewertet | 🔘 Grau |
|---|---|---|---|---|---|
| 🏆 Champions (9) | Intuitive Surgical, Münchener Rück, ServiceNow, Hermès, MercadoLibre, Bank Central Asia (6) | Constellation Software, Allianz (2) | CBOE (1) | – | – |
| ⚙️ Profi (6) | Broadridge, Tristel (2) | Rambus, Cellebrite, SoFi (3) | A10 Networks (1) | – | – |
| 🚀 Talent (3) | – | – | – | Rocket Lab (1) | Kraken Robotics, HawkEye 360 (2) |

**Lesehilfe:** 6 der 9 Champions sind aktuell nachkaufattraktiv – passt zum
Befund aus dem letzten Ist-Abgleich, dass Champions beim Gewicht bereits
über Ziel liegt, aber preislich trotzdem günstig ist (kein Widerspruch:
Gewichtsdisziplin und Einzelpreis-Attraktivität sind unabhängige Fragen).
Bei Talent liegt nur noch 1 von 3 Positionen (Rocket Lab) in der
ungünstigsten Kombination (spekulativ + überbewertet) – das ist der
Bereich, wo eine bewusste Prüfung der These am ehesten angebracht ist,
auch wenn kein automatisches Verkaufssignal vorliegt (Update 2026-09-04:
Cellebrite und SoFi nach Neukategorisierung zu Profi, CBOE zu Champions,
nicht mehr Teil dieser Zählung).

## Aktuelle Zuordnung (Stand 2026-09-04)

### Champions
| Position | CRV | Begründung Kategorie |
|---|---|---|
| Intuitive Surgical | 🟢 KAUFEN/NACHKAUFEN – KGV 40,1x, 42% unter 10J-Median (68,8x). **MoS-Hinweis:** historischer Max-Drawdown -82,3% (2001), -75,9% (2009), -49,9% (2022), aktuell bereits selbst -44,2% im laufenden Drawdown – der günstige KGV-Vergleich spiegelt genau diesen laufenden Rücksetzer. | Named-Beispiel Brian (Quasi-Monopol Roboterchirurgie) |
| Münchener Rückversicherung | 🟢 KAUFEN/NACHKAUFEN – **Anker: KBV/ROE statt KGV** (Rückversicherer). KGV ~10-11x zur Einordnung ergänzend absolut günstig für Qualitäts-Rückversicherer. **MoS-Hinweis:** dokumentierter schwerer Kursrückgang während der Finanzkrise 2008 (genaue % nicht verlässlich recherchierbar) – auch Rückversicherer sind bei Systemkrisen nicht immun. | Named-Beispiel Brian (Oligopol Rückversicherung) |
| ServiceNow | 🟢 KAUFEN/NACHKAUFEN – KGV 80,3x, 45% unter 10J-Median (146,8x). **MoS-Hinweis:** absolute Bewertung bleibt hoch, "günstig" ist relativ zur eigenen Historie, nicht zu Sicherheitsmarge im klassischen Sinn. | Named-Beispiel Brian (Enterprise-Software-Standard) |
| Constellation Software | 🟡 HALTEN/BEOBACHTEN – KGV 55,6x, nur 17% unter 10J-Median (66,9x), moderater Abschlag. **MoS-Hinweis:** bemerkenswert flache Drawdown-Historie für einen Software-Compounder (-23,7% 2008, -24,8% 2015/16, -24,2% 2020) – deutlich stabiler als die meisten Tech-Werte dieser Liste. | Serial-Acquirer, Nischen-Monopole, sehr hohe Marge |
| Hermès | 🟢 KAUFEN/NACHKAUFEN – KGV ~36-38x, 25-28% unter 10J-Median (49,2x). **MoS-Hinweis:** keine spezifische Drawdown-Quelle recherchiert, aber Luxusgüter historisch bei Konsumeinbrüchen (2008, 2020) mit deutlichen zweistelligen bis niedrigen dreistelligen Korrekturen. | Luxusmonopol, extreme Pricing Power |
| MercadoLibre | 🟢 KAUFEN/NACHKAUFEN – KGV 46,7x, 40% unter 10J-Median (77,4x). **MoS-Hinweis:** LatAm-Fintech/E-Commerce, historisch volatil bei Makro-/Währungsschocks. | Dominante E-Commerce/Fintech-Plattform LatAm |
| Allianz SE | 🟡 HALTEN/BEOBACHTEN – **Anker: KBV/ROE statt KGV** (Versicherer/Vermögensverwalter). KGV ~14-15x, leicht über eigenem 3J/5J-Ø (~10-11x) und 10% über Branchen-Ø. **MoS-Hinweis:** historischer Max-Drawdown -72,7% (2008), -48,7% (2020) – auch globale Top-Versicherer sind in Systemkrisen extrem exponiert. | Quasi-Monopol-Skala wie Münchener Rück, AA-Bonität, globaler Top-3-Versicherer/Vermögensverwalter (korrigiert 2026-09-03, vorher fälschlich Talent – Grund war Positionsgröße, kein zulässiges Kriterium) |
| Bank Central Asia | 🟢 KAUFEN/NACHKAUFEN – **Anker: KBV/ROE statt KGV** (Bank). ROE >20% ist der eigentlich tragende Beleg, KGV ~12-14x, 52% unter 10J-Median (24,4x). **MoS-Hinweis:** Max-Drawdown -42,8% (COVID-Crash März 2020) – EM-Bank trotz Qualität nicht immun gegen globale Schocks. | ROE >20%, dominante Marktstellung Indonesien, verlässliches Wachstum (korrigiert 2026-09-03, vorher fälschlich Talent – Grund war EM-Status, kein zulässiges Kriterium) |
| CBOE Holdings | 🟠 KEIN NACHKAUF (TEUER) – KGV ~22-24x, Forward-KGV 31% über Branchen-Ø – eigene Einordnung: spürbar teuer ggü. Sektor, kein Schnäppchen. **MoS-Hinweis:** 5J-Max-Drawdown -24,4% – moderat im Vergleich zur restlichen Liste, aber bei bereits hoher Bewertung zusätzlich wenig Puffer. | Named-Beispiel Brian – **umkategorisiert 2026-09-04 von Profi zu Champions** (Brian: "extrem einmaliges Geschäftsmodell" – bestätigt: Operating-Marge ~35-53% je Periode, UND ein echtes, vertraglich/regulatorisch abgesichertes Monopol bei SPX-/VIX-Optionen – VIX ist ein CBOE-Markenzeichen, laut CBOE >98% des gesamten US-Index-Optionsvolumens läuft über CBOE-Venues. Stärkerer, konzentrierterer Moat als mehrere bestehende Champions. **Einziges Risiko, transparent benannt:** die SPX-Exklusivlizenz mit S&P Global ist vertraglich, nicht ewig – ein Lizenzverlust wäre ein echtes, wenn auch aktuell nicht akutes These-Bruch-Kriterium für die Zukunft.) |

### Profi
| Position | CRV | Begründung Kategorie |
|---|---|---|
| Broadridge Financial Solutions | 🟢 KAUFEN/NACHKAUFEN – Forward-KGV 17,0x, deutlich unter 12M-Ø (31,7x). **MoS-Hinweis:** aktuell bereits selbst -34,4% vom 52-Wochen-Hoch – der günstige KGV-Vergleich spiegelt zu einem Teil genau diesen laufenden Rücksetzer, nicht nur strukturelle Unterbewertung. | Named-Beispiel Brian |
| A10 Networks | 🟠 KEIN NACHKAUF (TEUER) – TTM-KGV 59,8x deutlich über 5J-Ø (23,2x)/7J-Ø (29,9x); Forward-KGV moderater (26,5x) – Diskrepanz beobachten, evtl. temporärer Gewinneinbruch. **MoS-Hinweis:** keine spezifische Drawdown-Quelle recherchiert – als kleinerer Netzwerktechnik-Titel mit volatiler Ertragslage realistisch überdurchschnittlich schwankungsanfällig. | Named-Beispiel Brian |
| Rambus | 🟡 HALTEN/BEOBACHTEN – KGV nahe eigenem 10J-Median (leicht darüber je nach Quelle). **MoS-Hinweis:** 5J-Max-Drawdown -48,8% (u.a. -30% allein 2022, -45% 2024) – Halbleiter-IP-Lizenzgeschäft mit Patentstreit-getriebenem, unregelmäßigem Ertragsmuster bleibt volatil. | Named-Beispiel Brian (22.08.), etablierte Semiconductor-IP-Firma seit 1990 (korrigiert 2026-09-03, vorher fälschlich Talent) |
| Tristel PLC | 🟢 KAUFEN/NACHKAUFEN – KGV 23,3x, 41% unter 10J-Median (39,8x). **MoS-Hinweis:** keine spezifische Drawdown-Quelle recherchiert – als kleiner UK-AIM-Nebenwert mit dünnem Handelsvolumen realistisch überdurchschnittlich volatil, unabhängig vom günstigen KGV. | Named-Beispiel Brian (22.08.) (korrigiert 2026-09-03, vorher fälschlich Talent) |
| Cellebrite DI Ltd | 🟡 HALTEN – Checkpoint Q3-Earnings. KGV 52,7x, 25% über 10J-Median – **eigene Einordnung optisch teuer, aber CRV allein ist hier nicht aussagekräftig genug**, siehe Begründung. **MoS-Hinweis:** -33% Kursrückgang 2026 nach Guidance-Cut/CEO-Wechsel. **Korrigiert 2026-09-04** (vorher fälschlich SCHROTT/VERKAUFEN nach einem vorschnellen 3-fach-Scout-Check): gründliche These-Prüfung (siehe architecture.md, "Gründliche-These-Prüfung-vor-Verkaufsempfehlung-Pflicht") ergab, dass 2 von 3 Re-Rating-Triggern mangels Q3-Zahlen noch gar nicht prüfbar waren (nicht "durchgefallen"), und der Guidance-Cut plausibel auf verzögerte statt verlorene Großaufträge zurückgeht (Timing-, kein Struktur-Problem). **Nächster Prüfpunkt: Q3-Earnings** (Guidance: Umsatz $145-148 Mio) – dann die drei Re-Rating-Trigger mit echten Daten neu prüfen. | Named-Beispiel Brian – **umkategorisiert 2026-09-04 von Talent zu Profi** (Brian: profitabel, $500M+ wiederkehrender ARR-Umsatz, echter regulatorischer Moat bei lizenziertem forensischem Gerätezugriff für Strafverfolgung – passt nicht zur Talent-Definition "eventuell noch unprofitabel/Hype-getrieben") |
| SoFi Technologies | 🟡 HALTEN/BEOBACHTEN – KGV ~35-38x. **MoS-Hinweis:** bereits -53% Drawdown 2026 (Short-Seller-Attacke, Peak Ende 2025 → Tief 30.03.), aktuelle Bewertung nach der Korrektur moderater; Brian hat Position ohnehin als "erstmal voll" markiert, kein Nachkauf geplant. | **Umkategorisiert 2026-09-04 von Talent zu Profi** (Brian-Vorschlag, gegenrecherchiert und bestätigt): 9 aufeinanderfolgende Quartale GAAP-profitabel (Stand Q4 2025), Nettomarge TTM 10,1%, Q2 2026 Adj.-Nettomarge 13%, FY2026-Guidance ~18% – "eventuell noch unprofitabel" (Talent-Definition) trifft nicht mehr zu. **Wichtiger, transparent zu benennender Vorbehalt:** Muddy-Waters-Short-Report (März 2026) wirft SoFi vor, Risiko aus verkauften Krediten zurückzubehalten und die tatsächliche Ausfallrate zu niedrig auszuweisen (behauptet 6,1% vs. berichtete 2,89%), mit dem Vorwurf zirkulärer Finanzierungspraktiken und möglichem Restatement-/SEC-Risiko – bisher unbewiesen, SoFi weist es zurück, CEO kaufte danach eigene Aktien nach. Genau die Zahlen, auf denen diese Hochstufung beruht, stehen damit unter einem laufenden, ungeklärten Vorbehalt – bei Bestätigung der Vorwürfe wäre das ein echtes Rückstufungs-/Ausschluss-Kriterium (Bilanzintegrität), kein reines Bewertungsthema. |

### Talent/Zock
| Position | CRV | Begründung Kategorie |
|---|---|---|
| Kraken Robotics | 🔘 GRAU – KEINE BELASTBARE AUSSAGE – **Anker: KGV ungeeignet** (nahe Gewinnschwelle, 100x+ teils berichtet, extrem verzerrt), kein tragfähiger Ersatzmaßstab aus dem Fact-Pack ableitbar. **MoS-Hinweis:** bereits -41% vom 52-Wochen-Hoch – Vorsicht in beide Richtungen, Bewertung schwer greifbar. | Früher Umsatzaufbau, kein Live-Kurs, hohe Volatilität |
| Rocket Lab USA | 🔴 KEIN NACHKAUF – ÜBERBEWERTET – unprofitabel (kein KGV berechenbar), Marktkap preist bereits deutliches künftiges Wachstum ein, ohne dass die Ertragslage das aktuell stützt – eigene Einordnung: Bewertung sportlich. **MoS-Hinweis:** bereits -61% vom Jahreshoch, historisch bis zu -70% Drawdown (2022) und im Schnitt -37% je Schock über 5 Marktphasen – auch nach Korrektur bleibt die Bewertung angespannt. **Nachkauf-Aufstufungs-Trigger (2026-09-04, auf Brians Bitte hinterlegt – mind. 2 von 3 fundamental für ein Aufstufungssignal, Technik nur als Bestätigung, nie als eigenständiger Auslöser):** (1) **Neutron erfolgreicher Erstflug** (Pad-Delivery weiter Q4 2026 geplant, Zeitfenster für Start noch 2026 laut Unternehmen selbst "eng" – das ist der von Rocket Lab selbst genannte Auslöser für die EBITDA-Wende); (2) **Verwässerungstempo verlangsamt sich** – aktuell real und beschleunigend (Aktien im Umlauf 2023 ~482 Mio → Mitte 2026 ~598 Mio, davon 1,53 Mrd. USD allein aus ATM-Emissionen in H1/2026) – Trigger erfüllt, wenn 2 aufeinanderfolgende Quartale ohne neues großvolumiges ATM-Programm vergehen ODER Management explizit Selbstfinanzierung ohne weitere Aktienausgabe in Aussicht stellt; (3) **Burn-Multiple <2,5x UND Cash-Runway ≥18 Monate** wieder erfüllt (beide waren im frischen Scout-Check vom 04.09. die ausschlaggebenden K-Kriterien für den Terminal-State) – nächster Prüfpunkt Q3-Zahlen (Guidance: Umsatz $250-265 Mio, Adj.-EBITDA-Verlust $17-23 Mio, damit erstmals grob quantifiziert prüfbar). **Technischer Kontext (Stand 03.09., NUR Bestätigung, kein eigenständiger Trigger):** Kurs $63,81 bereits unter 50D-SMA ($75,24) UND 200D-SMA ($79,37), RSI(14) 36,1 (Richtung überverkauft, noch nicht dort) – "günstig" laut Chart, aber ohne erfüllte fundamentale Trigger laut eigenem Antizyklik-Grundprinzip explizit KEIN Kaufgrund ("falling knife"-Risiko). Analysten-Konsens-Kursziele (GuruFocus/Zacks-artige Quellen, $80-116) nur als Rohdaten-Kontext, nicht als eigene Bewertung übernommen. | Wachstumsphase, historisch unprofitabel, kein Monopol – **aber #2 aktivster Launch-Anbieter der westlichen Welt nach SpaceX (21 Starts 2025), echte Nischenführerschaft im Smallsat-Dedicated-Launch-Segment (Brian, 04.09.: "2. größter Space Player") – Marktstellung-Kriterium für Profi erfüllt, Marge/Kapitaldisziplin-Kriterium noch nicht (siehe Verwässerung oben), daher vorerst weiter Talent, kein klarer Profi-Fall wie Cellebrite** |
| HawkEye 360 | 🔘 GRAU – KEINE BELASTBARE AUSSAGE – **Anker: KGV ungeeignet** (jung, unprofitabel, kein tragfähiger Ersatzmaßstab recherchiert). **MoS-Hinweis:** bereits ca. -50% vom Allzeithoch (Mai 2026) und -32% unter IPO-Preis (26$) gefallen, keine belastbare Bewertungshistorie; Brian hat Position ohnehin als "erstmal voll" markiert, kein Nachkauf geplant. | Kein Live-Kurs, dünnste Datenlage im Depot |

## Änderungsprotokoll
- 2026-09-03: Erstanlage dieser Datei. Korrektur von 4 Fehlzuordnungen aus
  dem Strategiespiegel-Report vom 02.09. (Allianz, Bank Central Asia,
  Rambus, Tristel – alle vorher fälschlich Talent statt Champions/Profi).
  Auslöser: Brians Rückfrage, warum Jack/Conan/Jarvis bei der Zuordnung
  uneinig sind.
- 2026-09-03: Ziel-Positionsanzahl auf "10-6-4" festgesetzt (Brian), löst
  die alte Spanne (8-10/3-5/5-9 Rest) ab.
- 2026-09-03 (später am selben Tag): "10-6-4" im 3-KI-System-Audit (Jarvis/
  Jack/Conan) als rechnerisch fehlerhaft erkannt (Basen-Verwechslung
  Gesamtportfolio vs. Aktienanteil) und auf **"10-7-3"** korrigiert – siehe
  architecture.md für die vollständige Herleitung.
- 2026-09-03: CRV-Ampel (inkl. Margin-of-Safety/Drawdown-Hinweise) auch für
  alle 18 Depot-Positionen eingeführt (vorher nur Watchlist), 4-stufige
  Skala (🟢/🟡/🟠/🔴) statt 3-stufig – von Brian gefordert.
- 2026-09-03: Methodik-Fix – GuruFocus-"Fair Value"-Label bei CBOE/Rocket
  Lab (hier) und ASML/FICO/CPRT/ROL/MPWR/NVT/Rorze (watchlist.md) waren
  fälschlich als Urteil zitiert statt nur als Rohdaten-Input genutzt zu
  werden. Korrigiert (Brian: "andere Webseiten... aber nie als
  Benchmark") – Ampel-Farbe ist immer eigenes Urteil aus unserer
  Multiples-Logik, externe Quellen liefern nur Zahlen.
- 2026-09-04: Talent/Profi-Rebalancierungs-Diskussion (Talent 2 über Ziel)
  – frischer 3-fach-Scout-These-Check für die zwei stärksten Exit-
  Kandidaten (Cellebrite, Rocket Lab). **Cellebrite: einstimmig
  SCHROTT/DURCHGEFALLEN, VERKAUFEN-Empfehlung aktiv** (siehe
  `depot/offene_empfehlungen.md`). **Rocket Lab: K≤K-BASIS-2-Terminal-
  State vom 01.09. bestätigt unverändert (Sizing 0% für Neu-/Nachkauf),
  aber Uneinigkeit ob das auch die bestehende 10-Stück-Trace-Position
  betrifft** – Conan (frisch) plädiert für Exit, die ursprüngliche
  Analyse vom 01.09. (Jarvis) hatte die Trace-Position explizit
  ausgenommen. Bewusst NICHT einseitig aufgelöst, offener
  Diskussionspunkt mit Brian.
- 2026-09-04 (Korrektur, wenige Stunden später): Brian widersprach der
  vorschnellen Cellebrite-VERKAUFEN-Empfehlung ("erst gründlich die These
  durchgehen, nicht voreilig einen Verkauf in Erwägung ziehen") – zu
  Recht: 2 von 3 Re-Rating-Triggern waren mangels Q3-Zahlen noch gar
  nicht prüfbar, Guidance-Cut plausibel Timing- statt Struktur-Problem.
  Führte zu einer neuen systemweiten Regel (architecture.md,
  "Gründliche-These-Prüfung-vor-Verkaufsempfehlung-Pflicht"). Cellebrite:
  VERKAUFEN → HALTEN mit Checkpoint Q3-Earnings. Zusätzlich, unabhängig
  davon: Brian stufte Cellebrite als Profi statt Talent ein (profitabel,
  $500M+ ARR, echter regulatorischer Moat) – umgesetzt. Rocket Lab
  ebenfalls als Profi-Kandidat vorgeschlagen, aber von Jarvis mit
  Verweis auf die noch fehlende Gesamt-Profitabilität (Neutron-
  Testflug-Abhängigkeit) hinterfragt – Antwort von Brian steht noch aus,
  Rocket Lab bleibt vorerst Talent.
- 2026-09-04 (wenige Stunden später): Brian hakte nach ("nur weil ein
  Unternehmen unprofitabel ist, heißt das nicht automatisch Talent –
  differenziere Backlog-Wachstum vs. Verwässerung") – berechtigter
  Einwand zur Prüfung. Recherche ergab ein gemischtes Bild: Marktstellung
  spricht klar für Profi (#2 aktivster Launch-Anbieter der westlichen
  Welt nach SpaceX, echte Nischenführerschaft Smallsat-Segment), aber die
  Verwässerung ist real und beschleunigt (Aktien im Umlauf +14%/Jahr,
  1,53 Mrd. USD ATM-Emissionen allein in H1/2026) – genau das
  Warnsignal-Muster, das Brian selbst als Unterscheidungskriterium
  genannt hatte. Brian akzeptierte die Gegenrecherche: Rocket Lab bleibt
  Talent. Konkrete, recherchierte Nachkauf-Aufstufungs-Trigger hinterlegt
  (siehe CRV-Zelle oben: Neutron-Erstflug, Verwässerungstempo,
  Burn-Multiple/Cash-Runway – technische Lage nur als Bestätigung, nie
  als eigenständiger Auslöser).
- 2026-09-04 (direkt im Anschluss an die Depot-Übersicht): Brian schlug
  zwei weitere Hochstufungen vor – CBOE zu Champions ("extrem einmaliges
  Geschäftsmodell"), SoFi zu Profi. Beide gegenrechercht statt blind
  übernommen: **CBOE bestätigt** – Operating-Marge ~35-53%, echtes
  vertraglich/regulatorisch abgesichertes SPX-/VIX-Optionsmonopol
  (>98% des US-Index-Optionsvolumens läuft über CBOE, VIX ist CBOE-
  Markenzeichen) – stärkerer, konzentrierterer Moat als mehrere
  bestehende Champions, Umkategorisierung Profi→Champions umgesetzt.
  **SoFi bestätigt, aber mit Vorbehalt** – 9 Quartale GAAP-profitabel,
  Nettomarge-Trend 10%→15%→18% (Guidance), "eventuell noch
  unprofitabel" trifft nicht mehr zu, Umkategorisierung Talent→Profi
  umgesetzt – ABER ein laufender, ungeklärter Muddy-Waters-Short-Report
  (Vorwurf: zurückbehaltenes Kreditrisiko, zu niedrig ausgewiesene
  Ausfallrate, zirkuläre Finanzierung, mögliches SEC-/Restatement-
  Risiko) stellt genau die Zahlen infrage, auf denen die Hochstufung
  beruht – transparent in der Profi-Tabelle dokumentiert, nicht
  verschwiegen. Ergebnis: Champions 8→9, Profi 6→6 (CBOE raus, SoFi
  rein), Talent 4→3 – **Talent-Rebalancierung damit exakt auf Ziel
  abgeschlossen**, ohne eine einzige Position tatsächlich zu verkaufen.
