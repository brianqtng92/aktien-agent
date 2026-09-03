# CLBT (Cellebrite DI Ltd.) — Täglicher Trigger-Check: Diagnostische Neubewertung

**Datum:** 2026-09-03
**Typ:** Täglicher Trigger-Check (kein neuer FULL DEEP DIVE)
**⚠ METHODIK-KENNZEICHNUNG (Pflicht-Hinweis):** **Jarvis-Only.** Weder Jack (Gemini,
`gemini-bridge`-MCP) noch Conan (ChatGPT, `openai-bridge`-MCP) waren in dieser Session
erreichbar (beide API-Bridges nicht verbunden, ToolSearch findet sie nicht). Der
Chrome-Browser-Fallback (`claude-in-chrome`) war ebenfalls nicht verbunden. Es fand
**kein 3-fach-Cross-Check** statt — dies ist eine vorläufige Einzelmeinung, kein
regelkonform vollständiges Cross-KI-Ergebnis. Bei nächster Gelegenheit mit
verfügbaren Bridges sollte diese Einschätzung gegen Jack/Conan gegengeprüft werden,
insbesondere falls der Sofort-Alarm unten doch näher an der Auslöseschwelle liegt
als hier eingeschätzt.

---

## 1. Ausgangslage (Referenz)

Volle TMR-Analyse `analysen/CLBT-TMR-jarvis-claude-2026-08-22.md`: **RATING: SCHROTT**,
ausgelöst durch DNA-Gate-Abbruch (K-Score 2,0/5, unter K-BASIS−2 = 3). **Terminaler
Zustand** gemäß Terminal-State-Mechanismus (architecture.md Abschnitt 14): Moat-,
Bewertungs- und Outcome-Module wurden regelkonform NICHT ratingwirksam durchgerechnet.
**SIZING: Tier 4 (0%)** — kein Neukauf, kein Nachkauf.

Hinterlegte Trigger aus der Alt-Analyse:
- **Re-Rating-Trigger (≥2 von 3 für Neubewertung):** (1) Q3'26 reale FCF-Marge
  (SBC-bereinigt) ≥20%, (2) NRR ≥120%, (3) Guidance bei Q3 bestätigt statt erneut
  gekürzt.
- **Sofort-Alarm (unabhängig davon, einer reicht):** (a) DRITTE Guidance-Kürzung
  in Folge, (b) neuer Going-Concern-Vermerk, (c) materialisierte Kosten aus der
  Securities-Investigation >15% des operativen Cashflows.

---

## 2. Verifizierte Fakten (WebSearch, 2026-09-03)

**CEO-Wechsel:** Bereits am **13.08.2026** vollzogen (nicht neu seit der Alt-Analyse
vom 22.08. — war dort bereits vollständig eingepreist). Thomas E. Hogan trat per
gegenseitigem Einvernehmen zurück, verlässt auch den Board. Shiven Ramji (seit Mai
2026 President Products & Technology im Haus) wurde CEO, "planned succession".
Hogan bleibt 6 Monate als Berater eingebunden — geordnete, nicht chaotische
Übergabe. [Quelle: investors.cellebrite.com, theglobeandmail.com, finance.yahoo.com]

**Guidance-Kürzung:** Ebenfalls am **13.08.2026**, zeitgleich mit dem CEO-Wechsel
verkündet (FY26 ARR-Guidance $567–573 Mio → $550–560 Mio; Revenue $565–571 Mio →
$555–561 Mio; Adj.-EBITDA-Ziel dagegen angehoben). Das ist **dieselbe Kürzung**, die
die Alt-Analyse vom 22.08. bereits als "zweite Guidance-Kürzung binnen eines Jahres"
verarbeitet hat — **keine neue, dritte Kürzung seit dem 22.08.** Recherche nach
weiteren Guidance-Anpassungen zwischen 22.08. und heute (03.09.) ergab **keinen
Treffer**. Der vorgelagerte News-Scan hat hier vermutlich denselben Aug-13-Cluster
erneut aufgegriffen, keine neue Verschlechterung identifiziert.

**Securities-Investigation:** Stand unverändert **"Investigation"**, keine
eingereichte Klage. Mehrere Kanzleien (Kaplan Fox, Levi & Korsinsky, Block &
Leviton) haben seit Mitte August "Investor Alerts" veröffentlicht (übliche
Sammelklage-Werbung nach Kurssturz) — keine bezifferten Kosten, kein Klageeingang,
kein Vergleich. Kein Fortschritt seit der Alt-Analyse feststellbar.

**Going-Concern:** Keine Hinweise auf einen neuen Going-Concern-Vermerk in den
verfügbaren 6-K-Meldungen gefunden. **[N/V für lückenlose Bestätigung]** — der
vollständige 20-F-/6-K-Volltext wurde nicht Wort für Wort durchgelesen, aber keine
Sekundärquelle (Finanzportale, SEC-Filing-Aggregatoren) berichtet von einem solchen
Vermerk. Bilanz weiterhin netto-cash-stark ($522,5 Mio zum 30.06.), was einen
Going-Concern-Vermerk fundamental unwahrscheinlich macht.

**Kurs:** Aktuell **$11,84–11,86** (Live-Kurs via Twelve Data, 2026-09-03,
[LIVE]). Vorbörslicher Crash-Tiefpunkt am 13.08. bei $9,58 (52-Wochen-Tief),
Schlusskurs am Vortag der Zahlen (12.08.) bei $15,25 → Tiefpunkt-Rückgang
**−37,2%**, deckt sich mit der im Auftrag genannten "~−36% seit Q2-Zahlen".
Seither hat sich der Kurs bei $10,32–$12,43 stabilisiert, aktuell im oberen Teil
dieser Spanne. 52-Wochen-Hoch $19,98.

**AGM:** Bestätigt für **24.09.2026** (Israel). Tagesordnung: zwei
Director-Wiederwahlen, Vergütungspaket für den neuen CEO, neue
Vergütungsrichtlinie, Wiederbestellung EY Israel als Abschlussprüfer — Standard-AGM-
Agenda, keine außerordentlichen Sonderpunkte (kein Delisting-, Kapitalmaßnahmen-
oder Fusionsantrag erkennbar).

---

## 3. Sofort-Alarm-Prüfung (Pflicht, ein Kriterium reicht)

| Kriterium | Status | Begründung |
|---|---|---|
| (a) Dritte Guidance-Kürzung in Folge | **❌ NICHT ausgelöst** | Nur eine (die bereits bekannte) Kürzung vom 13.08.; keine weitere seit 22.08. gefunden |
| (b) Neuer Going-Concern-Vermerk | **❌ NICHT ausgelöst** | Kein Hinweis gefunden, Bilanz netto-cash-stark ($522,5 Mio) — [N/V für lückenlose 20-F-Volltextprüfung, aber keine Sekundärquelle deutet darauf hin] |
| (c) Materialisierte Investigation-Kosten >15% OCF | **❌ NICHT ausgelöst** | Weiterhin nur "Investigation"-Stadium, keine Klage, keine bezifferten Kosten |

**→ Sofort-Alarm: NICHT ausgelöst.** Der vorgelagerte News-Scan hat im Kern
dieselben Ereignisse erneut aufgegriffen, die bereits in die Alt-Analyse vom
22.08. eingeflossen sind (CEO-Wechsel + Guidance-Kürzung vom 13.08., seither
laufende Investigation). Keine der drei Sofort-Alarm-Schwellen wurde seither
neu gerissen.

---

## 4. Terminal-State-Bestätigung (Pflicht)

Gemäß Terminal-State-Mechanismus (architecture.md Abschnitt 14, Core Rule 16 +
Conans Terminal-State-Integrität): der DNA-Gate-Abbruch vom 22.08. bleibt ein
unveränderlicher Systemzustand. Diese Neubewertung ist **rein diagnostisch** —
Moat, Bewertung, DCF, Outcome-Wahrscheinlichkeiten wurden **nicht neu
durchgerechnet** und dürfen es auch nicht sein, solange kein Re-Rating-Trigger
(≥2 von 3, siehe Abschnitt 1) erfüllt ist. Kein einziger der drei Re-Rating-Trigger
ist heute erfüllt (Q3'26-Zahlen stehen noch aus, voraussichtlich Mitte/Ende
November 2026).

**RATING bleibt: SCHROTT**
**SIZING bleibt: Tier 4 (0%)** — kein Neukauf, kein Nachkauf.

---

## 5. TA-Einschätzung (Pflicht bei jeder Einzelanalyse, auch SCHROTT-Positionen)

Daten: Twelve Data `get_time_series`, CLBT, 1day, 150 Kerzen (30.01.–03.09.2026),
Chart gerendert: `reports/CLBT_chart_2026-09-03.png` (EMA20/EMA50).

- **Vor dem Crash:** Kurs pendelte April–Anfang August zwischen ~$11 und ~$17,
  mit Aufwärtstrend Juni–Anfang August (bis $16,43 am 11.08.).
- **Crash-Tag 13.08.:** Gap-Down von $15,25 (Vortagesschluss) auf Eröffnung
  $10,32, Tagestief $9,58 (52W-Tief), Schluss $10,80 — Volumen-Explosion auf
  36,75 Mio. Aktien (ggü. Ø ~2 Mio.) = klassischer News-Schock, kein
  charttechnisches Signal im engeren Sinne.
- **Seit 14.08. bis heute (03.09.):** Seitwärtsbewegung/Basisbildung in einer
  Range von grob $10,32–$12,43, ohne neues Tief seit dem Crash-Tag und mit
  leicht steigenden Tiefs (17.08. Tief $10,325 → 21.08. Tief $11,01 → seither
  durchgehend über $11). Das ist **eher eine Stabilisierung/beginnende
  Bodenbildung als eine Fortsetzung des Abwärtstrends** — der Kurs hat sich
  bei rund −22% vom 52W-Hoch eingependelt, statt weiter Richtung Crash-Tief
  zu fallen.
- **EMA20/EMA50:** Der EMA50 zieht (durch die vor-Crash-Werte $13–16 in der
  Berechnung) noch deutlich über dem aktuellen Kurs, der EMA20 nähert sich von
  unten an. Ein charttechnisch "sauberer" Boden wäre erst bestätigt, wenn der
  Kurs den fallenden EMA50 zurückerobert (aktuell keine Nähe dazu).
- **Einordnung:** Der Chart **widerspricht dem fundamentalen Abwärtsurteil
  nicht**, bestätigt es aber auch nicht aktiv weiter — er zeigt einen Markt,
  der den Schock verarbeitet hat und aktuell abwartet (Volumen seit 20.08.
  wieder auf normalem Niveau, 1,3–4 Mio./Tag). Für die SCHROTT-Einstufung
  bleibt das irrelevant (Terminal-State, kein Einstiegssignal wird daraus
  abgeleitet) — dient hier rein der Pflicht-Chartkommentierung.

---

## 6. Handlungsempfehlung für Brians bestehende Position

Bestehende Position bei finanzen.net zero: 200 Stk. (Käufe 20.05.2025 @ 11,58€,
22.07.2026 @ 13,62€, 17.08.2026 @ 8,98€), Investsumme 2.166,15 €, aktueller Saldo
**−3,9%**. Regel 19 ("Kurs fällt ≠ These kaputt") gilt hier **umgekehrt bereits
seit der Alt-Analyse**: Die These ist fundamental angeschlagen (reale FCF-Marge
unter Schwelle, negativer EPS-CAGR), der Kursverlust ist eine **Folge**, keine
unabhängige Übertreibung.

**Empfehlung: Position unverändert halten, kein Nachkauf, keine Vollständige
Kaufempfehlung — aber auch kein akuter Verkaufszwang aus dieser Prüfung heraus.**
Begründung: Der Sofort-Alarm ist NICHT ausgelöst, es gibt also keinen neuen,
zusätzlich eskalierenden Grund für eine Notfall-Reaktion über die bereits
bekannte SCHROTT/Tier-4-Einstufung hinaus. Gleichzeitig hebt die aktuelle
Situation die SCHROTT-Einstufung auch nicht auf (kein Re-Rating-Trigger erfüllt).
Der 17.08.-Nachkauf @ 8,98€ war laut Kaufhistorie bereits nach dem Crash erfolgt
— hier bewusst kein Kommentar zur Vergangenheit, sondern reiner Blick nach vorn.

**Nächster harter Prüfpunkt:** Q3'26-Zahlen (ca. Mitte/Ende November 2026) —
dort entscheidet sich, ob ≥2 von 3 Re-Rating-Triggern erfüllt sind (reale
FCF-Marge ≥20%, NRR ≥120%, Guidance bestätigt statt gekürzt). Bis dahin bleibt
diese Position im reinen Beobachtungsmodus, kein aktiver Handlungsbedarf.
AGM am 24.09.2026 hat keine erkennbare direkte Kursrelevanz über die üblichen
Corporate-Governance-Punkte hinaus, wird aber der Vollständigkeit halber im
nächsten Trigger-Check nochmal knapp mitverfolgt (insb. ob die
CEO-Vergütung/Compensation Policy überraschend abgelehnt wird — wäre ein
ungewöhnliches, potenziell governance-relevantes Signal, aktuell aber reine
Vorsichtsmaßnahme, kein konkreter Hinweis darauf).

**Fazit für den Trigger-Check:** Kein "echter Anlass" im Sinne einer
eskalierenden Verschlechterung — die Lage hat sich seit 22.08. weder
bestätigt-verschlechtert noch verbessert, sondern ist im Wesentlichen
unverändert (derselbe bereits bekannte News-Cluster, Kurs stabilisiert statt
weiter fallend). Trotzdem grenzwertig benachrichtigungswürdig, da Brian eine
laufende Position hält und der vorgelagerte Scan dies als potenziell neu
markiert hatte — siehe Zusammenfassung an Brian für die finale Einordnung, ob
eine Push-Benachrichtigung sinnvoll ist.

---

**Quellen (Auswahl):** investors.cellebrite.com (CEO-Wechsel-PR), theglobeandmail.com
(CEO-Wechsel, Q2-Call-Transcript, Kaplan-Fox-Investigation-PRs), finance.yahoo.com
(Q2-Highlights, CEO-Shift-Artikel), simplywall.st (Kursreaktion −30,4%),
stocktitan.net (AGM/6-K-Zusammenfassung), tipranks.com (AGM-Details), investing.com
(Analysten-Kurszielsenkungen DA Davidson, Needham), stockanalysis.com/marketbeat.com
(Kurs, 52W-Range), Twelve Data MCP (Live-Kurs + 150-Tage-Zeitreihe für Chart).
