# 3-fach TMR Cross-Check Fazit – Hoya Corporation (7741 Tokyo / HOCPY)
## Stand: 2026-09-06

**Kontext:** Dieser Lauf war zugleich ein bewusster Test des am 2026-09-06
implementierten Fact-Pack-Tag-Fixes (siehe HANDOVER.md 10.13 "Block 7
ergänzt" und architecture.md "Fact-Pack-Tag-Disziplin"). Bisher hatte Jarvis'
eigenes Fact-Pack Kennzahlen wie Piotroski F-Score und FCF-Marge bei fehlender
Einzelquelle vorschnell als [N/V] getaggt, obwohl daneben eine plausible
qualitative Einschätzung stand – das brachte Jack (Gemini) wiederholt dazu
(Disco Corp 31.08., Lasertec 05.09.), dieses Tag unkritisch zu übernehmen und
mit SCHROTT/Terminal-State abzubrechen. Heute wurde die Fact-Pack-Erstellung
selbst korrigiert (TRAINING-vs-N/V-Schwelle konsequent angewendet) UND ein
zusätzlicher Bridge-Block 7 ergänzt ("Fact-Pack-Tags sind nicht bindend").

## TESTERGEBNIS: FIX GREIFT

**Jack (Gemini) brach diesmal NICHT ab.** Beide Kennzahlen, die bei Disco
Corp/Lasertec den Abbruch auslösten (Piotroski F-Score, FCF-Marge), waren in
Jarvis' Fact-Pack diesmal korrekt als [TRAINING] getaggt (Piotroski 7-8/9 aus
GF-Score+qualitativen Indikatoren, FCF-Marge ~23,4% aus CFO/Capex/Umsatz
berechnet) – nicht als [N/V]. Jack übernahm diese Tags unverändert, wertete
beide K-Kriterien als erfüllt (K: 5/5) und lief die komplette Analyse bis zum
MEIN VERDICT durch: Rating BEOBACHTEN, Reaper Score 6/10, Konfidenz NIEDRIG
(automatischer Deckel wegen 4 TRAINING-K-Kriterien – das ist der *korrekte*
Mechanismus, kein Abbruch, sondern ein Score-/Konfidenz-Malus).

**Conan (ChatGPT) bestätigt unabhängig:** ebenfalls kein Abbruch, ebenfalls
BEOBACHTEN, Reaper Score 6,5/10. Interessant: Conan nutzte seine eigene
Live-Websuche und rekonstruierte den Piotroski F-Score selbst auf ~6/9 (nicht
7-8/9 wie Jarvis) – fand dabei drei widersprüchliche externe Quellen (3/4/7).
Trotz dieser Abweichung UND trotz eines dadurch ausgelösten K-BASIS-1-
Grenzfalls (K: 4/5 statt 5/5) brach Conan NICHT ab, weil der Wert weiterhin
[TRAINING] blieb, nie [N/V] – exakt das Verhalten, das der Fix ermöglichen
sollte.

**Einordnung:** Dies ist der erste dokumentierte Lauf seit dem Fix, bei dem
Jack bei einer japanischen Firma ohne 10-K, mit denselben strukturellen
Datenlücken wie bei Disco Corp/Lasertec, NICHT abgebrochen ist. Da die
einzige Änderung zwischen den fehlgeschlagenen und diesem erfolgreichen Lauf
in der Fact-Pack-Tag-Vergabe lag (nicht in Gemini selbst), bestätigt das die
HANDOVER.md-10.13-Diagnose: die eigentliche Ursache lag in Jarvis' eigener
Fact-Pack-Erstellung, nicht in einem Gemini-spezifischen Modellverhalten.
Ein einzelner erfolgreicher Lauf ist noch kein endgültiger Beweis (n=1), aber
ein starkes positives Signal – bei Gelegenheit mit einem weiteren
datenarmen japanischen Kandidaten erneut testen, um die Wiederholungsrate zu
bestätigen.

## Inhaltliches Ergebnis – Rating-Übersicht

| Analyst | Rating | Score | Konfidenz | Sizing |
|---|---|---|---|---|
| Jarvis (Claude) | BEOBACHTEN | – (eigene Einordnung: Champions/🟠) | – | 0% (kein neuer Kauf) |
| Jack (Gemini) | BEOBACHTEN | Reaper 6/10 | NIEDRIG | 0% (Tier 4) |
| Conan (ChatGPT) | BEOBACHTEN | Reaper 6,5/10 | GELB 62% | 0% (Tier 4) |

**Hohe Übereinstimmung:** Alle drei Analysten kommen unabhängig zu
BEOBACHTEN – keine Kaufempfehlung, kein SCHROTT. Der Konsens: Hoya ist ein
qualitativ exzellentes Unternehmen (Duopol-Moat bei EUV-Mask-Blanks mit AGC,
Elite-Margen, sehr konservative Bilanz/Net-Cash-Position, Q1-FY2027-
Reakzeleration), aber aktuell ohne Sicherheitsmarge bewertet (KGV 28-37x je
nach Quelle/Datum, deutlich über Branchendurchschnitt ~16,6x, PEG 2,3-3,1x).

**Wichtigste Divergenz (Cross-Check-Mehrwert):** Conans eigene Live-Recherche
fand eine niedrigere aktuelle Bewertung (KGV trailing 30,6x/forward 28,2x)
als Jarvis' Fact-Pack (36,9x/34,9x) – vermutlich unterschiedliche
TTM-/Datenstichtage. Das drückt den EV/FCF trotzdem nicht unter die
Attraktivitätsschwelle (32x bei Conan). Conan fand zudem zwei für Jarvis'
Fact-Pack neue Corporate-Events: ein aktives Aktienrückkaufprogramm (bis 200
Mrd. JPY) und eine laufende strategische Prüfung des PENTAX-Medical-
Endoskopiegeschäfts (möglicher Verkauf, seit 31.07.2026) – beides potenziell
relevant für künftige Kapitalallokation/Fokussierung, aber ohne
Rating-Konsequenz in diesem Lauf.

**TA-Perspektive (Conan per Live-Suche, von Jarvis übernommen):** Kurs unter
SMA50/SMA200, RSI 37,83 (schwach, nicht überverkauft) – Konsolidierung
innerhalb eines längeren Aufwärtstrends (52W-Performance weiterhin +23,64%).
TA-Rating HOLD/NEUTRAL-WEAK, deckungsgleich mit dem fundamentalen
BEOBACHTEN-Bild.

## Depot-/Watchlist-Konsequenz

Hoya war bereits vor diesem Lauf Watchlist-Eintrag (Champions, CRV 🟠
VORSICHT/TEUER). Der 3-fach-Cross-Check bestätigt diese Einordnung
unverändert – **kein Kategorie-Wechsel, keine Watchlist-Neuaufnahme nötig**
(bereits vorhanden), keine Kaufempfehlung. Die Watchlist-Zeile wird mit den
aktualisierten Kennzahlen/Kursdaten aufgefrischt (siehe watchlist.md).

**Nächster gemeinsamer Prüfpunkt:** Q2-FY2027-Zahlen, ~Ende Oktober/Anfang
November 2026 (Jack: unbenannt genau, Conan: ~30.10.2026, Jarvis:
Ende Oktober/Anfang November) – Bestätigung der Q1-Reakzeleration, Trend bei
Piotroski-relevanten Bilanzkennzahlen, Status der PENTAX-Medical-Prüfung.

## Erstellte/aktualisierte Dateien dieses Laufs

- `analysen/HOYA-7741-TMR-quickfilter-jarvis-claude-2026-09-06.md`
- `analysen/HOYA-7741-TMR-quickfilter-jack-gemini-2026-09-06.md`
- `analysen/HOYA-7741-TMR-quickfilter-conan-chatgpt-2026-09-06.md`
- `analysen/HOYA-7741-cross-check-fazit-2026-09-06.md` (diese Datei)
- `watchlist.md` (Zeile 7741 aktualisiert)
- `depot/bridge_status.md` (Statuszeile ergänzt)
