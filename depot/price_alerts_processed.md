# Verarbeitete Preisalarme

**Zweck (2026-09-17, siehe Agent-Playbook.md "Preisalarm-Auslösungs-Check +
systematische Kauf-Bewertung"):** Verhindert, dass ein bereits ausgelöster
und bewerteter Preisalarm bei jedem weiteren Blitz-Scan-/Trigger-Check-Lauf
erneut gemeldet wird. Bei JEDEM Lauf `list_price_alerts(activeOnly: false)`
gegen diese Tabelle abgleichen — jeder Alarm mit gesetztem
`triggeredTimestampUtc`, der hier noch NICHT steht, ist ein neuer,
zu bewertender Fund (unabhängig davon, wie lange er zurückliegt).

| Alert-ID | Position (ISIN) | Preis | Ausgelöst am | Verarbeitet am | Ergebnis |
|---|---|---|---|---|---|
| 7bAzBSNDvGk2gtqzVgnFss | Kraken Robotics (CA50077N1024) | 2,80 | 2026-09-14T13:31:07Z | 2026-09-17 (nachträglich) | **Rückwirkend gefunden, keine Echtzeit-Bewertung möglich** — Twelve-Data-OTC-Proxy (KRKNF) zeigt für 09-14 keinen vergleichbaren Tagestief (Low $3,19), Diskrepanz zur primären TSXV-Notierung nicht abschließend geklärt (Datenlücke vs. echter kurzer Intraday-Ausschlag auf der weniger liquiden Primärnotierung). Kein Nachkauf ausgelöst, da Preis zum Zeitpunkt der nachträglichen Prüfung bereits wieder bei ≈4,59 CAD lag — weit über der Zone. Alarm bleibt inaktiv (Einweg), kein neuer Alarm gesetzt, solange kein frischer Rücksetzer Richtung Zone erkennbar ist.

## Format bei neuem Eintrag
`| Alert-ID | Position (ISIN) | Preis | Ausgelöst am (triggeredTimestampUtc) | Verarbeitet am (Datum dieses Laufs) | Ergebnis (Ja/Nein/Noch abwarten + 1-Satz-Begründung) |`
