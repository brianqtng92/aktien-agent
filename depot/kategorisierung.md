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

## Ziel-Positionsanzahl: "10-6-4" (festgesetzt 2026-09-03)

**10 Champions / 6 Profi / 4 Talent = 20 Einzelwerte gesamt** (siehe
architecture.md, Abschnitt 3, für die vollständige Begründung inkl. der
10%-Positionscap-Logik hinter der 4er-Talent-Grenze).

| Kategorie | Ziel | Ist (03.09.2026) | Freie Slots |
|---|---|---|---|
| Champions | 10 | 8 | 2 frei |
| Profi | 6 | 5 | 1 frei |
| Talent | 4 | 5 | **1 über Ziel** – keine neuen Talent-Zukäufe, bis eine bestehende Position ausscheidet |

## CRV-Ampel (2026-09-03, von Brian gefordert: "das soll auch für Depot-Werte gelten")

Dieselbe CRV-Ampel wie in `watchlist.md` (Definition dort vollständig,
siehe "CRV-Ampel" + "Margin of Safety / historisches Drawdown-Verhalten"),
jetzt auch für alle 18 Depot-Positionen. **Vier Stufen** (2026-09-03 von
Brian auf 🟠 erweitert für mehr Differenzierung):
- 🟢 **KAUFEN/NACHKAUFEN** – klar unterbewertet ggü. eigener Historie/Peers, These intakt.
- 🟡 **HALTEN/BEOBACHTEN** – fair bewertet, kein starkes Signal in beide Richtungen.
- 🟠 **VORSICHT/TEUER** – spürbar teuer ggü. Historie/Peers, aber kein hartes Warnsignal (spekulativ, nicht fundamental gebrochen).
- 🔴 **MEIDEN/ÜBERBEWERTET** – deutlich überbewertet und/oder mehrere gleichzeitige Warnsignale.

**Wichtig:** Die CRV-Ampel bei einer bestehenden Depot-Position ist KEIN
automatisches Verkaufssignal – dafür gelten weiterhin ausschließlich die
in `analysen/*.md` dokumentierten Abstauber-/Stop-These-Trigger (siehe
"Verkaufsdisziplin & Gewinnmitnahme-Regeln", architecture.md). Die Ampel
zeigt nur, ob ein NACHKAUF zum aktuellen Preis eine gute Idee wäre – bei
🔴/🟠 heißt das "kein Nachkauf jetzt", nicht "verkaufen". Stand 2026-09-03
(WebSearch-Snapshot), Pflege ab jetzt wöchentlich über den Wochenfazit-Lauf
(analog Watchlist).

## Aktuelle Zuordnung (Stand 2026-09-03)

### Champions
| Position | CRV | Begründung Kategorie |
|---|---|---|
| Intuitive Surgical | 🟢 KAUFEN/NACHKAUFEN – KGV 40,1x, 42% unter 10J-Median (68,8x) | Named-Beispiel Brian (Quasi-Monopol Roboterchirurgie) |
| Münchener Rückversicherung | 🟢 KAUFEN/NACHKAUFEN – KGV ~10-11x, absolut günstig für Qualitäts-Rückversicherer | Named-Beispiel Brian (Oligopol Rückversicherung) |
| ServiceNow | 🟢 KAUFEN/NACHKAUFEN – KGV 80,3x, 45% unter 10J-Median (146,8x). **MoS-Hinweis:** absolute Bewertung bleibt hoch, "günstig" ist relativ zur eigenen Historie, nicht zu Sicherheitsmarge im klassischen Sinn. | Named-Beispiel Brian (Enterprise-Software-Standard) |
| Constellation Software | 🟡 HALTEN/BEOBACHTEN – KGV 55,6x, nur 17% unter 10J-Median (66,9x), moderater Abschlag | Serial-Acquirer, Nischen-Monopole, sehr hohe Marge |
| Hermès | 🟢 KAUFEN/NACHKAUFEN – KGV ~36-38x, 25-28% unter 10J-Median (49,2x) | Luxusmonopol, extreme Pricing Power |
| MercadoLibre | 🟢 KAUFEN/NACHKAUFEN – KGV 46,7x, 40% unter 10J-Median (77,4x). **MoS-Hinweis:** LatAm-Fintech/E-Commerce, historisch volatil bei Makro-/Währungsschocks. | Dominante E-Commerce/Fintech-Plattform LatAm |
| Allianz SE | 🟡 HALTEN/BEOBACHTEN – KGV ~14-15x, leicht über eigenem 3J/5J-Ø (~10-11x) und 10% über Branchen-Ø | Quasi-Monopol-Skala wie Münchener Rück, AA-Bonität, globaler Top-3-Versicherer/Vermögensverwalter (korrigiert 2026-09-03, vorher fälschlich Talent – Grund war Positionsgröße, kein zulässiges Kriterium) |
| Bank Central Asia | 🟢 KAUFEN/NACHKAUFEN – KGV ~12-14x, 52% unter 10J-Median (24,4x) | ROE >20%, dominante Marktstellung Indonesien, verlässliches Wachstum (korrigiert 2026-09-03, vorher fälschlich Talent – Grund war EM-Status, kein zulässiges Kriterium) |

### Profi
| Position | CRV | Begründung Kategorie |
|---|---|---|
| Broadridge Financial Solutions | 🟢 KAUFEN/NACHKAUFEN – Forward-KGV 17,0x, deutlich unter 12M-Ø (31,7x) | Named-Beispiel Brian |
| CBOE Holdings | 🟠 VORSICHT/TEUER – KGV ~22-24x, Forward-KGV 31% über Branchen-Ø – eigene Einordnung: spürbar teuer ggü. Sektor, kein Schnäppchen | Named-Beispiel Brian |
| A10 Networks | 🟠 VORSICHT/TEUER – TTM-KGV 59,8x deutlich über 5J-Ø (23,2x)/7J-Ø (29,9x); Forward-KGV moderater (26,5x) – Diskrepanz beobachten, evtl. temporärer Gewinneinbruch | Named-Beispiel Brian |
| Rambus | 🟡 HALTEN/BEOBACHTEN – KGV nahe eigenem 10J-Median (leicht darüber je nach Quelle) | Named-Beispiel Brian (22.08.), etablierte Semiconductor-IP-Firma seit 1990 (korrigiert 2026-09-03, vorher fälschlich Talent) |
| Tristel PLC | 🟢 KAUFEN/NACHKAUFEN – KGV 23,3x, 41% unter 10J-Median (39,8x) | Named-Beispiel Brian (22.08.) (korrigiert 2026-09-03, vorher fälschlich Talent) |

### Talent/Zock
| Position | CRV | Begründung Kategorie |
|---|---|---|
| SoFi Technologies | 🟡 HALTEN/BEOBACHTEN – KGV ~35-38x. **MoS-Hinweis:** bereits -53% Drawdown 2026 (Short-Seller-Attacke, Peak Ende 2025 → Tief 30.03.), aktuelle Bewertung nach der Korrektur moderater; Brian hat Position ohnehin als "erstmal voll" markiert, kein Nachkauf geplant. | Archetyp-Beispiel Brian für diese Kategorie |
| Cellebrite DI Ltd | 🔴 MEIDEN/ÜBERBEWERTET – KGV 52,7x, 25% über 10J-Median (42,1x), 46,8x vs. Branchen-fair-Ratio ~30x. **MoS-Hinweis:** zusätzlich -33% Kursrückgang 2026 – teuer UND im Abwärtstrend gleichzeitig, kein Nachkauf-Zeitpunkt. | Jung notiert (SPAC 2021), noch kein etablierter Track Record |
| Kraken Robotics | 🟠 VORSICHT/TEUER – KGV extrem verzerrt (nahe Gewinnschwelle, 100x+ teils berichtet), kaum aussagekräftig. **MoS-Hinweis:** bereits -41% vom 52-Wochen-Hoch – Vorsicht in beide Richtungen, Bewertung schwer greifbar. | Früher Umsatzaufbau, kein Live-Kurs, hohe Volatilität |
| Rocket Lab USA | 🔴 MEIDEN/ÜBERBEWERTET – unprofitabel (kein KGV berechenbar), Marktkap preist bereits deutliches künftiges Wachstum ein, ohne dass die Ertragslage das aktuell stützt – eigene Einordnung: Bewertung sportlich. **MoS-Hinweis:** bereits -61% vom Jahreshoch, historisch bis zu -70% Drawdown (2022) und im Schnitt -37% je Schock über 5 Marktphasen – auch nach Korrektur bleibt die Bewertung angespannt. | Wachstumsphase, historisch unprofitabel, kein Monopol |
| HawkEye 360 | 🟡 HALTEN/BEOBACHTEN – kein KGV (jung/unprofitabel). **MoS-Hinweis:** bereits ca. -50% vom Allzeithoch (Mai 2026) und -32% unter IPO-Preis (26$) gefallen, keine belastbare Bewertungshistorie; Brian hat Position ohnehin als "erstmal voll" markiert, kein Nachkauf geplant. | Kein Live-Kurs, dünnste Datenlage im Depot |

## Änderungsprotokoll
- 2026-09-03: Erstanlage dieser Datei. Korrektur von 4 Fehlzuordnungen aus
  dem Strategiespiegel-Report vom 02.09. (Allianz, Bank Central Asia,
  Rambus, Tristel – alle vorher fälschlich Talent statt Champions/Profi).
  Auslöser: Brians Rückfrage, warum Jack/Conan/Jarvis bei der Zuordnung
  uneinig sind.
- 2026-09-03: Ziel-Positionsanzahl auf "10-6-4" festgesetzt (Brian), löst
  die alte Spanne (8-10/3-5/5-9 Rest) ab.
- 2026-09-03: CRV-Ampel (inkl. Margin-of-Safety/Drawdown-Hinweise) auch für
  alle 18 Depot-Positionen eingeführt (vorher nur Watchlist), 4-stufige
  Skala (🟢/🟡/🟠/🔴) statt 3-stufig – von Brian gefordert.
- 2026-09-03: Methodik-Fix – GuruFocus-"Fair Value"-Label bei CBOE/Rocket
  Lab (hier) und ASML/FICO/CPRT/ROL/MPWR/NVT/Rorze (watchlist.md) waren
  fälschlich als Urteil zitiert statt nur als Rohdaten-Input genutzt zu
  werden. Korrigiert (Brian: "andere Webseiten... aber nie als
  Benchmark") – Ampel-Farbe ist immer eigenes Urteil aus unserer
  Multiples-Logik, externe Quellen liefern nur Zahlen.
