# Depot Scalable Capital – Brian

**Klarstellung zur Rolle dieses Kontos (2026-09-01, von Brian erklärt):**
Das Scalable-Konto dient bei Brian **ausschließlich für den ETF-Sparplan**
(Vanguard FTSE All-World) – **nicht** als aktives Aktiendepot. Das eigentliche
Aktiendepot mit den Einzelwerten liegt bei **finanzen.net zero**
(`depot/finanzen-net-zero.md`). **Bank Central Asia (BBCA)** ist eine
bewusste Ausnahme: gekauft, weil zum Kaufzeitpunkt Cash auf dem Scalable-
Verrechnungskonto lag und Brian nicht extra hin- und herschieben wollte –
**keine strategische Entscheidung, Profi-Positionen bei Scalable zu
halten.** BBCA wird früher oder später zum eigentlichen Aktiendepot
(finanzen.net zero) übertragen. Bis zur Übertragung bleibt BBCA
inhaltlich unverändert Teil der Profi-Kategorie-Berechnung (Region/Sektor/
Kapitalgewicht) – der Broker, bei dem eine Position technisch liegt, ändert
nichts an ihrer strategischen Einordnung. Das Gold-ETC bleibt wie bisher
bewusst außerhalb der Champions/Profi/Talent-Struktur (siehe unten).

**Update 2026-08-30: Live-Anbindung über Scalable MCP aktiv (siehe
Agent-Playbook.md, "Broker-Anbindung Scalable Capital").** Ab jetzt read-only
Live-Daten statt manueller Screenshot-Erfassung.

**Update 2026-09-07 (Wochenfazit-Folgelauf, live):** monatliche
600-€-ETF-Sparplanrate wurde am 07.09. ausgeführt (siehe
`depot/last_transaction_check.md`), Kaufkraft dadurch entsprechend gesunken.

| Position | Wert aktuell | Kaufwert | Gewinn/Verlust | Kurs/Stück | Kurs bei Kauf | Anteile | Sparplan |
|---|---|---|---|---|---|---|---|
| Boerse Stuttgart EUWAX Gold II | 498,40 € | 532,58 € | -34,18 € (-6,42 %) | 124,57 € | 138,21 € | 4 | kein Sparplan |
| Bank Central Asia | 2.003,54 € | 1.999,94 € | +3,60 € (+0,18 %) | 0,323 € | 0,32 € | 6.183,767567 | GESTOPPT (seit 2026-08-28) |
| Vanguard FTSE All-World (Acc) | 8.186,86 € | 6.753,40 € | +1.433,46 € (+21,23 %) | 167,73 € | 136,09 € | 48,786235 | 600 €/Monat, nächste Ausführung ca. 07.10.2026 |

**Cash/Verrechnungskonto (live, Stand 07.09.2026 ~15:00 UTC):** 460,33 €
(Kaufkraft identisch, keine offenen Kredite/Orders) – Rückgang ggü. dem
letzten Stand durch die am 07.09. ausgeführte Sparplanrate.

**Gesamtwert Scalable Capital (live, Stand 07.09.2026): 11.149,13 €**
(Wertpapiere 10.688,80 € + Cash 460,33 €).

**Update 2026-09-09 (Depot-Update, live über Scalable-MCP):**

| Position | Wert aktuell | Kaufwert | Gewinn/Verlust | Kurs/Stück |
|---|---|---|---|---|
| Boerse Stuttgart EUWAX Gold II | 496,59 € | 532,58 € | -35,99 € (-6,8%) | 124,15 € |
| Bank Central Asia | 1.984,99 € | 1.999,94 € | -14,95 € (-0,7%) | 0,321 € |
| Vanguard FTSE All-World (Acc) | 8.103,88 € | 6.753,40 € | +1.350,48 € (+20,0%) | 166,11 € |

**Cash/Verrechnungskonto: 0,00 €** (weiterhin die bereits am 08.09. vermerkte
unerklärte Abweichung von den zuvor gemeldeten 460,33 € – `list_portfolio_transactions`
zeigt keine erklärende Buchung seit dem letzten Checkpoint, bleibt offenes
Beobachtungsfeld, kein Anlass für eine Eskalation).

**Gesamtwert Scalable Capital (live, Stand 09.09.2026): 10.585,46 €**
(nur Wertpapiere, kein Cash) – Rückgang ggü. 07.09. (11.149,13 €) primär
durch den ungeklärten Cash-Rückgang, nicht durch Kursverluste (BCA/Vanguard
zusammen fast stabil, Gold-ETC leicht schwächer).

**Update 2026-09-17 (Depot-Update, live über Scalable-MCP — Verbindung war seit 17.09. kurzzeitig unauthentifiziert, von Brian re-autorisiert, siehe Agent-Playbook.md/HANDOVER.md):**

**Offener Punkt vom 09.09. jetzt geklärt:** die "unerklärte" Cash-Abweichung
(460,33 €→0,00 €) war eine **interne Überweisung/Umbuchung von -460,33 €
am 07.09.2026**, jetzt sichtbar in `list_portfolio_transactions` – keine
Dateninkonsistenz, sondern eine reguläre, von Brian selbst veranlasste
Buchung. Cash/Kaufkraft bleibt bei **0,00 €**.

| Position | Wert aktuell | Kurs/Stück | Anteile |
|---|---|---|---|
| Boerse Stuttgart EUWAX Gold II | 494,05 € | 123,513 € | 4 |
| Bank Central Asia | 1.952,96 € | 0,315 € | 6.199,871861 |
| Vanguard FTSE All-World (Acc) | 8.149,30 € | 167,04 € | 48,786235 |

**Gesamtwert Scalable Capital (live, Stand 17.09.2026 ~08:30 UTC): 10.596,26 €**
(nur Wertpapiere, Cash weiterhin 0,00 €) – leicht über dem 09.09.-Stand
(10.585,46 €), keine Auffälligkeit. **Performance laut Scalable (absolute
Rendite, nicht %):** YTD +1.013,81 €, 1 Jahr +1.272,41 €, seit Kontoeröffnung
(MAX) +2.414,25 €. Letzte Transaktionen: BCA-Dividende 15.09. (5,25 €,
reinvestiert 16.09.), Vanguard-Sparplanrate 07.09. (600 €), Einzahlung
28.08. (800 €), größerer BCA-Nachkauf 21.08. (4.112 Stück @ 0,3411 €) plus
mehrere Teilverkäufe (L&G Global Quality Dividends komplett liquidiert,
VanEck Morningstar/iShares Nasdaq 100 teilverkauft) – ältere Umschichtung,
nicht neu.

**NEU entdeckt über die Live-Anbindung: Boerse Stuttgart EUWAX Gold II**
(physisches Gold-ETC, 4 Stück, Kauf 30.01.2026 @ 138,21€). War in keiner
bisherigen Erfassung/keinem Screenshot enthalten. **Einordnung (2026-08-30,
von Brian entschieden): bleibt bewusst außerhalb der Champions/Profi/
Talent-Struktur** – keine aktive Einzelwert-These, reine defensive
Diversifikation/Absicherung. Fließt außerdem NICHT in die Sektor- und
Geografische-Streuung-Berechnung ein (dort ohnehin kein sinnvoller
Sektor/Region zuordenbar, ähnlich wie Cash separat ausgewiesen wird).

**Keine Krypto-Bestände** trotz freigeschalteter Krypto-Funktion im Depot
(alle Krypto-Positionen bei 0, laut Live-Abfrage 2026-08-30).

**Laufende Sparpläne/Dauerauftrag (Stand 2026-08-28, noch nicht live
gegengecheckt außer dem Vanguard-Sparplan selbst):** 800 €/Monat Dauerauftrag
gesamt auf das Scalable-Capital-Konto, davon 600 €/Monat per Sparplan in den
Vanguard FTSE All-World (Acc., live bestätigt: nächste Ausführung 07.09.2026)
und 200 €/Monat als Puffer auf dem Verrechnungskonto (kein aktiver Sparplan).
Der BCA-Sparplan (zuvor 100 €/Monat) läuft nicht mehr – siehe
`Agent-Playbook.md`, Abschnitt "Budget & Cashflow (2026-08-28)".

**Update 2026-09-18 (Wochenfazit-Lauf, live über Scalable-MCP, Verbindung wieder stabil):**

| Position | Wert aktuell | Kurs/Stück | Anteile |
|---|---|---|---|
| Boerse Stuttgart EUWAX Gold II | 500,42 € | 125,105 € | 4 |
| Bank Central Asia | 1.921,96 € | 0,31 € | 6.199,871861 |
| Vanguard FTSE All-World (Acc) | 8.159,01 € | 167,24 € | 48,786235 |

**Gesamtwert Scalable Capital (live, Stand 18.09.2026): 10.581,88 €** (nur Wertpapiere, Cash weiterhin 0,00 €) — leicht unter dem 17.09.-Stand (10.596,26 €), BCA leicht schwächer, ETF-Sparplan-Anteilswert leicht höher. Keine neuen Transaktionen seit 17.09. (`list_portfolio_transactions` seit 2026-09-17T00:00:00Z → 0 Treffer).

Hinweis (2026-08-23): Depot-Erfassung insgesamt abgeschlossen – von Brian bestätigt
("das sind meine ganzen Positionen"). Zusammen mit `finanzen-net-zero.md`,
`trade-republic.md` und `smartbroker-plus.md` ist das jetzt das vollständige Depot.
Update 2026-08-28: nach der Depot-Restrukturierung (siehe `Agent-Playbook.md`) sind
es 18 Einzelwerte ohne ETF + Vanguard-FTSE-All-World-ETF-Sparplan (Update
2026-08-30: plus die neu entdeckte Gold-ETC-Position, siehe oben – zählt
NICHT zu den aktiven Einzelwerten, siehe Klarstellung ganz oben). BBCA
zählt weiterhin als aktiver Profi-Einzelwert (siehe Klarstellung ganz
oben, 2026-09-01) – der Broker-Standort ändert nichts an der Einordnung.
