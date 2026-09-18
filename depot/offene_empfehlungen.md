# Offene Kauf-/Verkauf-Empfehlungen

**Zweck (2026-09-03, von Brian gefordert):** Liste aller aktuell offenen,
noch nicht ausgeführten Kauf-/Nachkauf-/Verkauf-/Teilverkauf-Empfehlungen.
Wird vom Täglichen Trigger-Check geführt: neue Empfehlungen werden
eingetragen, ausgeführte oder durch neue Analysen überholte Empfehlungen
werden entfernt, offene Empfehlungen ab einem gewissen Alter erneut
per Chat + E-Mail in Erinnerung gebracht (nicht täglich, um Ermüdung zu
vermeiden – siehe Agent-Playbook.md "Erinnerungs-Mechanismus für offene
Empfehlungen").

| Position | ISIN | Empfehlung | Zone/Preis | Quelle | Datum | Zuletzt erinnert |
|---|---|---|---|---|---|---|
| Kraken Robotics | CA50077N1024 | Nachkauf-Zone (Preisalarm) | ≤2,80 CAD (Downside-Alert aktiv) | E-Mail "Zwei Zonen im Blick", 2026-09-01 | 2026-09-01 | 2026-09-17 |
| Rambus | US7509171069 | Nachkauf-Zone (Preisalarm) | ≤$68-75 (Zone präzisiert nach Full Deep Dive, vorher pauschal $75) | RMBS-Full-Deep-Dive, 2026-09-09 | 2026-09-01 | 2026-09-17 |
| CBOE Holdings | US12503M1080 | Nachkauf-Zone, gestaffelt (KAUFEN, Tier 2) | Tranche 1: Stabilisierung über $268-270 (~1,5-2%) · Tranche 2: $255-262 | CBOE-Full-Deep-Dive, 2026-09-16 | 2026-09-16 | – |
| Hermès | FR0000052292 | Nachkauf-Zone, **Order-Limit: Zone erreicht, technische Bestätigung ausstehend** (Preisalarm) | ≤1.350€ (Abstauber-Limit aus RMS-Quick-Filter, 23.08.2026) – Kurs bei 1.352€ (18.09., TradingView-Monatschart Brian) praktisch AUF der Zone. **TA-Bestätigung fehlt noch:** Monatschart testet gerade die alte 2022-Konsolidierungszone (~1.350-1.395€) von oben, aber Kurs bleibt weit unter dem langfristigen gleitenden Durchschnitt (1.776€) – intakter Abwärtstrend, noch keine bestätigte Stabilisierung (z.B. Monatskerze, die hier hält). Fundamental- und Chart-Level fallen selten zusammen – starkes Signal, aber Order erst bei echter Bestätigung, nicht bei reiner Level-Berührung. | RMS-TMR-Quick-Filter (23.08.2026) + JJ/Conan-Schnellanalyse-Update (2026-09-18) + TA-Monatschart-Review (2026-09-18) | 2026-09-18 | – |

## Format bei neuem Eintrag
`| Position | ISIN | Empfehlung (KAUFEN/NACHKAUFEN/VERKAUFEN/TEILVERKAUF) | Zone/Preis | Quelle (Analyse-Datei oder Report) | Datum | Zuletzt erinnert (– falls noch nie) |`

## Entfernt wird ein Eintrag, wenn:
- eine entsprechende Transaktion erkannt wird (Scalable: `list_portfolio_transactions`; manuelle Broker: Brian bestätigt es im Chat oder aktualisiert die jeweilige `depot/*.md`),
- eine neue Analyse die Empfehlung explizit ersetzt/aufhebt (z.B. KAUFEN → BEOBACHTEN),
- Brian die Position manuell als "erledigt/verworfen" markiert.
