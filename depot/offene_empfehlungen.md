# Offene Kauf-/Verkauf-Empfehlungen

**Zweck (2026-09-03, von Brian gefordert):** Liste aller aktuell offenen,
noch nicht ausgeführten Kauf-/Nachkauf-/Verkauf-/Teilverkauf-Empfehlungen.
Wird vom Täglichen Trigger-Check geführt: neue Empfehlungen werden
eingetragen, ausgeführte oder durch neue Analysen überholte Empfehlungen
werden entfernt, offene Empfehlungen ab einem gewissen Alter erneut
per Chat + E-Mail in Erinnerung gebracht (nicht täglich, um Ermüdung zu
vermeiden – siehe architecture.md "Erinnerungs-Mechanismus für offene
Empfehlungen").

| Position | ISIN | Empfehlung | Zone/Preis | Quelle | Datum | Zuletzt erinnert |
|---|---|---|---|---|---|---|
| Kraken Robotics | CA50077N1024 | Nachkauf-Zone (Preisalarm) | ≤2,80 (Downside-Alert aktiv) | E-Mail "Zwei Zonen im Blick", 2026-09-01 | 2026-09-01 | – |
| Rambus | US7509171069 | Nachkauf-Zone (Preisalarm) | ≤65 (Downside-Alert aktiv) | RMBS-Update, 2026-09-01 | 2026-09-01 | – |
| Cellebrite DI Ltd | IL0011794802 | VERKAUFEN (Talent-Rebalancierung) | zum aktuellen Kurs, kein Limit-Timing nötig – These ist gebrochen, kein Bewertungs-Timing-Fall | Frischer 3-fach-Scout-These-Check (Jarvis/Jack/Conan einstimmig SCHROTT, 0/3 Re-Rating-Trigger erfüllt), 2026-09-04 | 2026-09-04 | – |

## Format bei neuem Eintrag
`| Position | ISIN | Empfehlung (KAUFEN/NACHKAUFEN/VERKAUFEN/TEILVERKAUF) | Zone/Preis | Quelle (Analyse-Datei oder Report) | Datum | Zuletzt erinnert (– falls noch nie) |`

## Entfernt wird ein Eintrag, wenn:
- eine entsprechende Transaktion erkannt wird (Scalable: `list_portfolio_transactions`; manuelle Broker: Brian bestätigt es im Chat oder aktualisiert die jeweilige `depot/*.md`),
- eine neue Analyse die Empfehlung explizit ersetzt/aufhebt (z.B. KAUFEN → BEOBACHTEN),
- Brian die Position manuell als "erledigt/verworfen" markiert.
