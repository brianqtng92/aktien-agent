# Depot-Transaktions-Checkpoint (automatisch verwaltet vom Täglichen Trigger-Check)

**NICHT manuell bearbeiten**, außer zur Korrektur nach einem Fehler. Dieser
Timestamp markiert die zuletzt vom Trigger-Check gesehene Transaktion bei
Scalable Capital. Bei jedem Lauf wird `list_portfolio_transactions` mit
`fromTime` = diesem Wert abgefragt, um NUR neue Transaktionen seit dem
letzten Lauf zu erkennen (siehe architecture.md, Abschnitt "Täglicher
Trigger-Check" → "Depot-Transaktions-Erkennung").

Zuletzt gesehene Transaktion (lastEventAt, ISO-8601 UTC): 2026-09-03T07:48:51.000Z

Initial gesetzt am 2026-09-02 (Setup dieser Funktion). Letzte tatsächliche
Security-Transaktion zu diesem Zeitpunkt: Bank Central Asia BUY,
2026-08-21T20:12:08.997Z (Scalable Capital) – seither keine neue
Security-Transaktion. Checkpoint bewusst auf den Setup-Zeitpunkt (nicht auf
diese letzte Transaktion) gesetzt, damit der erste reguläre Lauf danach
nicht die gesamte bisherige Historie als "neu" meldet.

Format bei Aktualisierung: nur die Zeile "Zuletzt gesehene Transaktion: ..."
ersetzen, restlichen Text als Dokumentation stehen lassen oder kürzen.
