# Depot-Transaktions-Checkpoint (automatisch verwaltet vom Täglichen Trigger-Check)

**NICHT manuell bearbeiten**, außer zur Korrektur nach einem Fehler. Dieser
Timestamp markiert die zuletzt vom Trigger-Check gesehene Transaktion bei
Scalable Capital. Bei jedem Lauf wird `list_portfolio_transactions` mit
`fromTime` = diesem Wert abgefragt, um NUR neue Transaktionen seit dem
letzten Lauf zu erkennen (siehe Agent-Playbook.md, Abschnitt "Täglicher
Trigger-Check" → "Depot-Transaktions-Erkennung").

Zuletzt gesehene Transaktion (lastEventAt, ISO-8601 UTC): 2026-09-07T10:55:33.757Z

Lauf 2026-09-05 (regulärer taeglicher Lauf, ca. 20:14 UTC): keine neuen
Security-Transaktionen seit letztem Checkpoint (list_portfolio_transactions
fromTime=2026-09-04T20:35:00.000Z → 0 Treffer). Checkpoint auf aktuellen
Abfragezeitpunkt vorgezogen.

Lauf 2026-09-04 (3. Durchlauf desselben Tages, ca. 20:35 UTC): keine neuen
Security-Transaktionen seit letztem Checkpoint (list_portfolio_transactions
fromTime=2026-09-04T08:19:47.000Z → 0 Treffer). Checkpoint auf aktuellen
Abfragezeitpunkt vorgezogen. Dies ist bereits der DRITTE taeglicher-trigger-
check-Lauf für 2026-09-04 (nach ~08:00 und ~08:20 UTC, siehe
depot/bridge_status.md "Auffälligkeiten" – Ursache für die Mehrfachausführung
weiterhin ungeklärt).

Lauf 2026-09-04 (2. Durchlauf desselben Tages, ca. 08:20 UTC): keine neuen
Security-Transaktionen seit letztem Checkpoint (list_portfolio_transactions
fromTime=2026-09-04T07:54:27.070Z → 0 Treffer). Checkpoint auf aktuellen
Abfragezeitpunkt vorgezogen.

Lauf 2026-09-04 (1. Durchlauf, ca. 08:00 UTC): keine neuen Security-Transaktionen
seit letztem Checkpoint (list_portfolio_transactions fromTime=2026-09-03T07:48:51.000Z
→ 0 Treffer). Checkpoint auf aktuellen Abfragezeitpunkt vorgezogen.

Initial gesetzt am 2026-09-02 (Setup dieser Funktion). Letzte tatsächliche
Security-Transaktion zu diesem Zeitpunkt: Bank Central Asia BUY,
2026-08-21T20:12:08.997Z (Scalable Capital) – seither keine neue
Security-Transaktion. Checkpoint bewusst auf den Setup-Zeitpunkt (nicht auf
diese letzte Transaktion) gesetzt, damit der erste reguläre Lauf danach
nicht die gesamte bisherige Historie als "neu" meldet.

Format bei Aktualisierung: nur die Zeile "Zuletzt gesehene Transaktion: ..."
ersetzen, restlichen Text als Dokumentation stehen lassen oder kürzen.

Lauf 2026-09-06/07 ~22:55 UTC (vorheriger Versuch desselben Tages): Scalable-
Capital-MCP-Verbindung war zu diesem Zeitpunkt invalidiert ("needs to
reconnect", `ping`/`get_portfolio_overview`/`get_portfolio_cash_breakdown`
schlugen fehl) - `list_portfolio_transactions` konnte NICHT aufgerufen
werden, Checkpoint bewusst nicht vorgezogen, Lauf endete ohne Commit/E-Mail.

Lauf 2026-09-07 (Folgelauf, ~15:00 UTC): Scalable-Capital-Verbindung war
diesmal wieder funktionsfähig (`ping` → pong). `list_portfolio_transactions`
mit fromTime=2026-09-05T20:14:00.000Z → 1 Treffer: Vanguard FTSE All-World
(Acc), IE00BK5BQT80, SAVINGS_PLAN BUY, -599,9999 EUR, 2026-09-07T10:55:33.757Z.
Als routinemäßige monatliche ETF-Sparplanausführung des Kern-ETF gewertet,
nicht als diskretionäre Einzelwert-Transaktion mit Thesen-Prüfungsbedarf -
daher KEIN 3-fach-Cross-Check ausgelöst (kein handlungsrelevanter Anlass).
Checkpoint auf diesen Transaktionszeitpunkt vorgezogen.
