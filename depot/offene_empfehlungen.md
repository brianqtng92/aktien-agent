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
| Rambus | US7509171069 | Nachkauf-Zone (Preisalarm) | ≤$68-75 (bestätigt und gestärkt nach Full-Deep-Dive-Refresh 21.09.2026 – deckt sich fast exakt mit dem reconciliierten DCF-Base ~$60-70; **Kurs 25.09. (stockanalysis.com, Twelve Data diese Session nicht verbunden) $105,16**, weiterhin deutlich über der Zone, Rally seit 21.09. im Wesentlichen gehalten. Kein neuer fundamentaler Treiber.) | RMBS-Full-Deep-Dive-Refresh, 2026-09-21 | 2026-09-01 | 2026-09-17 |
| CBOE Holdings | US12503M1080 | Nachkauf-Zone, gestaffelt (KAUFEN, Tier 2) — **ZONE VERLASSEN (01.10.)** | Tranche 1: $268-270 · Tranche 2: $255-262. **01.10. (Twelve Data live): Kurs $277,35 (+7,5% seit 28.09.)** – klar raus aus beiden Zonen, kurzes Fenster verpasst, kein Handlungsbedarf mehr. | CBOE-Full-Deep-Dive, 2026-09-16 | 2026-09-16 | 2026-10-01 (Zone-Austritt vermerkt) |
| McDonald's | US5801351017 | Einstiegszone (Beobachtung, kein Kaufsignal) | Brians Marke **≤200 € (≈$225)**, Conan: erste Tranche $225-232, attraktiv <$215 (≈191 €); Kurs 02.10. 205,13 € (Scalable). Sizing klein (max. ½ Normalposition). Vorbehalt: US-Anteil 65 % über Band (≤55-60 %), MCD würde ihn auf ~67-68 % erhöhen. Preisalarm auf Scalable zweimal an `upstream_unavailable` gescheitert, nicht gesetzt – Trigger-Check prüft manuell. | MCD-Nachprüfung, `analysen/MCD-nachpruefung-investor-day-2026-10-02.md` | 2026-10-02 | – |

## Format bei neuem Eintrag
`| Position | ISIN | Empfehlung (KAUFEN/NACHKAUFEN/VERKAUFEN/TEILVERKAUF) | Zone/Preis | Quelle (Analyse-Datei oder Report) | Datum | Zuletzt erinnert (– falls noch nie) |`

**Entfernt 2026-10-02:** innoscripta-Zeile entfernt – Stop-Loss von Brian ausgelöst, Position komplett raus (@ 36,55 €, -75,00 €/-3,9%). Details `depot/finanzen-net-zero.md`.

**Entfernt 2026-09-24:** Hermès-Zeile entfernt – Position von Brian komplett verkauft (@ 1.362,00 €), Empfehlung damit gegenstandslos. Details `depot/finanzen-net-zero.md`.

## Entfernt wird ein Eintrag, wenn:
- eine entsprechende Transaktion erkannt wird (Scalable: `list_portfolio_transactions`; manuelle Broker: Brian bestätigt es im Chat oder aktualisiert die jeweilige `depot/*.md`),
- eine neue Analyse die Empfehlung explizit ersetzt/aufhebt (z.B. KAUFEN → BEOBACHTEN),
- Brian die Position manuell als "erledigt/verworfen" markiert.
