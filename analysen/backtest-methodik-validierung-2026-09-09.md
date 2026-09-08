# Methodik-Backtest: 3 historische Fallstudien (2026-09-09)

**Auslöser:** Antwort auf Brians Frage "was fehlt zum professionellen
Fondsmanager" — Punkt 3 (Über-Engineering-Antwort): die DNA-Check-/
Fraud-Check-/Going-Concern-Kriterien wurden bisher NIE gegen historische
Fälle zurückgetestet, nur plausibel begründet. Ein quantitativ arbeitender
Fonds würde sein Modell vor Kapitaleinsatz validieren.

## ⚠️ Methodische Grenzen — vor den Ergebnissen zu lesen (No-False-Precision-Pflicht)

Das ist **kein statistischer Backtest**, sondern ein **Fallstudien-Check**
mit drei bewusst extremen, öffentlich sehr gut dokumentierten Fällen
(klarer Betrug, klares Governance-Desaster, klarer 10-Jahres-Gewinner).
Drei zentrale Einschränkungen, unverschleiert:

1. **N=3.** Statistisch bedeutungslose Stichprobe. Das ist ein
   Plausibilitäts-Check ("erkennt das Regelwerk offensichtliche Fälle
   überhaupt?"), kein Beweis für Trefferquote bei den viel häufigeren,
   uneindeutigen Fällen.
2. **Auswahl-Bias:** alle drei Fälle sind RÜCKBLICKEND eindeutig (Betrug
   kam heraus, IPO scheiterte sichtbar, Aktie lief nachweislich 10 Jahre
   gut) — genau deshalb wurden sie gewählt (überprüfbare Fakten
   vorhanden). Die meisten echten Analysefälle sind uneindeutiger als
   diese drei — ein Bestehen hier beweist nicht, dass das Regelwerk auch
   bei Grenzfällen richtig liegt.
3. **Rückschau-Verzerrung bei der Kriterien-Anwendung:** die Fakten unten
   stammen aus heutiger Recherche über die damalige Lage, nicht aus einer
   tatsächlich am damaligen Tag durchgeführten Live-Analyse. Es wurde
   versucht, nur Informationen zu verwenden, die zum jeweiligen
   Stichtag bereits öffentlich bekannt waren (mit Quellenbeleg je Fall),
   aber eine gewisse Verzerrung durch das Wissen des Ausgangs ist nicht
   vollständig ausschließbar.

**Fazit vorab:** dieser Check kann Vertrauen in offensichtliche Fälle
stärken, aber NICHT die eigentliche offene Frage beantworten, ob das
Regelwerk bei uneindeutigen Fällen (der Normalfall) tatsächlich Alpha
liefert. Das bliebe nur durch echte Zeit + eigene Live-Track-Record
belastbar zu beantworten (siehe `depot/performance_tracking.md`).

---

## Fall 1: Wirecard AG — Bilanzbetrug (Stichtag: März 2019)

**Warum dieser Fall:** direkter Test des Fraud-Check-Mechanismus
(Beneish M-Score, Schwelle > −1,78 = Betrugsverdacht) UND des
Going-Concern-Prechecks (SCHRITT 0C).

**Zum Stichtag öffentlich bekannt:**
- FY2018: Umsatz 2,016 Mrd. € (+35,4% YoY), EBITDA 560,5 Mio. € (+36,6%),
  EBITDA-Marge ~27,8% — auf dem Papier eine Wachstums-/Margen-Traumzahl.
- EY hatte die Jahresabschlüsse 2009-2018 durchgehend mit
  UNEINGESCHRÄNKTEM Bestätigungsvermerk versehen, KEIN
  Going-Concern-Vermerk.
- Ab Jan. 2019 berichtete die Financial Times über verdächtige
  Transaktionen in Singapur; ein Whistleblower (Pav Gill, ehemaliger
  Wirecard-Justiziar Singapur) hatte bereits 2018 interne
  Bilanzmanipulationen gemeldet, bevor er zur FT ging.

**Angewendet auf unsere aktuellen Regeln:**
- **SCHRITT 0C (Going-Concern-Precheck):** hätte NICHT ausgelöst — der
  Check basiert auf dem Auditor-Bestätigungsvermerk, und EY selbst hat
  jahrelang ein sauberes Testat ausgestellt. **Das ist die wichtigste
  einzelne Erkenntnis dieses Backtests: unser Going-Concern-Guardrail ist
  nur so gut wie der externe Wirtschaftsprüfer — bei einem Fall, in dem
  der Prüfer selbst getäuscht wird (oder wegschaut), versagt dieser
  spezifische Guardrail identisch zum echten Fall.**
- **Beneish M-Score:** eine unabhängige akademische Rückrechnung des
  M-Scores auf Wirecards 2016-2018-Zahlen fand tatsächlich frühe
  quantitative Anomaliesignale, die auf Bilanzmanipulation hindeuteten —
  VOR der öffentlichen Aufdeckung. Unser Regelwerk hätte den M-Score bei
  vollständig [LIVE]-verifizierten Inputs (die 2018er-Zahlen waren SEC-/
  Bundesanzeiger-öffentlich, also grundsätzlich [LIVE]-taggbar)
  ausgerechnet — und wäre damit plausibel selbst auf das
  Warnsignal gestoßen, das die akademische Forschung nachträglich fand.

**Ergebnis: GEMISCHT.** Ein Guardrail (Going-Concern via Auditor) hätte
identisch zur echten Welt versagt. Ein anderer Guardrail (Beneish
M-Score) wäre plausibel fündig geworden — WENN er tatsächlich
konsequent gerechnet worden wäre (in der echten Session-Praxis wird der
M-Score aber oft wegen fehlender [LIVE]-Vollständigkeit geskippt, siehe
`jack-moat-reaper-v11.7.md` Regel "nur wenn alle 8 [LIVE] → sonst SKIP" —
bei einem aktiven Verschleierer wie Wirecard könnten genau diese 8 Inputs
unauffällig manipuliert gewesen sein, was den Score selbst verzerrt hätte).
**Lehre:** kein Grund zur Selbstzufriedenheit — ein raffinierter,
mehrjähriger Betrug mit kooperierendem/getäuschtem Prüfer ist eine
Kategorie, die auch unser System nicht zuverlässig verspricht zu fangen.

---

## Fall 2: WeWork — Corporate-Governance-Kollaps (Stichtag: 14.08.2019, S-1-Veröffentlichung)

**Warum dieser Fall:** Test, ob die K-Kriterien + Management-Risiko-Prüfung
(Klasse C, Agent-Reality-Check) einen offensichtlichen Bucket-B/D-
Scout-Kandidaten mit extremen Governance-Red-Flags VOR dem Börsengang
zurückgewiesen hätten.

**Zum Stichtag öffentlich bekannt (aus der SEC-S-1 selbst, Primärquelle):**
- H1 2019: Nettoverlust >900 Mio. $ auf 1,54 Mrd. $ Umsatz — Verlust fast
  in Höhe des Umsatzes, Verluste beschleunigten sich GEGENÜBER dem
  Vorjahr, statt sich zu verbessern.
- Massive Related-Party-Transaktionen: Adam Neumann verkaufte die
  Markenrechte am Namen "We" an sich selbst und ließ sich diese von
  WeWork zurücklizenzieren (5,9 Mio. $), hatte zusätzlich
  Eigentumsanteile an mehreren von WeWork gemieteten Gebäuden.
  Klassischer Interessenkonflikt Gründer vs. Aktionäre.
- Governance: Super-Voting-Aktien für Neumann, eine Nachfolgeklausel, die
  im Ernstfall SEINE EHEFRAU als Nachfolgerin vorsah, kein wirksames
  Board-Oversight.

**Angewendet auf unsere aktuellen Regeln:**
- **K-Kriterien (Scout-Pfad):** Umsatzwachstum stark (erfüllt), aber
  Burn deutlich zu hoch relativ zum Umsatz (Nettoverlust nahe 100% des
  Umsatzes) — klarer Verstoß gegen die Burn-Multiple/Cash-Runway-Logik,
  selbst ohne exakten Burn-Multiple-Wert zu erfinden (No-False-Precision).
- **Agent-Reality-Check / Management-Risiko (Klasse C):** die
  Related-Party-Selbstbedienung UND die Nachfolgeklausel wären als
  hartes Management-Risiko-Flag zu werten gewesen — genau die Art von
  Befund, die unser System explizit als Prüfpunkt vorsieht.
- **Strukturelles Geschäftsmodell-Risiko** (nicht explizit als eigenes
  K/E-Kriterium codiert, aber Teil der "Gründliche-These-Prüfung"): eine
  fundamentale Fristen-Inkongruenz (langfristige, fixe Mietverpflichtungen
  vs. kurzfristig kündbare Mitgliedschafts-Umsätze) — genau das Muster,
  das sich 2020 bei COVID als existenzbedrohend erwies.

**Ergebnis: TREFFER.** Unser Regelwerk hätte WeWork mit hoher
Wahrscheinlichkeit bereits vor dem IPO-Versuch als Ablehnung/SCHROTT
eingestuft — primär wegen der Governance-Red-Flags und der extremen
Verlustquote, nicht erst wegen des späteren, öffentlich bekannten
Kollapses (Bewertung fiel binnen 6 Wochen von 47 Mrd. $ auf ~8 Mrd. $,
IPO am 30.09.2019 zurückgezogen, Neumann später vom Board entmachtet).
**Lehre:** bei öffentlich einsehbaren, unverschleierten Red Flags (anders
als bei aktivem Betrug wie Wirecard) funktioniert die Methodik wie
gedacht.

---

## Fall 3: Constellation Software — Langfrist-Gewinner (Stichtag: 2013/2014)

**Warum dieser Fall:** Test auf FALSE POSITIVES — lehnt die Methodik
einen echten Gewinner fälschlich ab, weil er "zu teuer"/"zu klein wirkt"
aussieht? Gegenprobe zum reinen "Rote-Flaggen-Erkennen" der Fälle 1+2.

**Zum Stichtag (2013) bekannt:**
- Wartungsumsatz +42% (davon 34 Prozentpunkte akquisitionsbedingt, 8%
  organisch), Combined Ratio (ROIC + organisches Umsatzwachstum) nahe
  Rekordniveau bei ~39% in 2013.
- 10-Jahres-Durchschnitts-ROIC von ~32% (deutlich über jeder
  ROIC-Schwelle im aktiven K-BASIS).
- Aggressiver, aber diszipliniert finanzierter Akquisitions-Ansatz
  (Serial-Acquirer-Modell, Nischen-Softwaremonopole).

**Angewendet auf unsere aktuellen Regeln:**
- **TMR K-Kriterien:** ROIC-Schwelle klar erfüllt (32% ≫ jede
  realistische Schwelle), FCF-Marge/Bruttomarge-Trend passend zu einem
  etablierten Software-Compounder — Bucket A (Compounder Candidate),
  TMR-Pfad korrekt zugeordnet.
- **Kein Fraud-/Going-Concern-Flag** — saubere, disziplinierte
  Akquisitionsfinanzierung, kein Alarmsignal.
- Erwartbares Ergebnis: KAUFEN, hohe Konfidenz.

**Tatsächlicher Ausgang:** 10-Jahres-annualisierte Rendite von **19,63%
p.a.**, gegenüber 13,95% p.a. beim S&P 500 im selben Zeitraum — deutliche
Outperformance über ein volles Jahrzehnt.

**Ergebnis: TREFFER, KEIN FALSE POSITIVE.** Die Methodik hätte den
tatsächlichen Gewinner korrekt und mit hoher Konfidenz als Kaufkandidat
erkannt — kein Fall, in dem strenge Kriterien einen echten Compounder
fälschlich aussortiert hätten.
**Bonus-Beobachtung (Aktualitätsbezug):** Constellation Software ist
HEUTE eine unserer Depot-Champions-Positionen mit einem laufenden
"Beobachtungspunkt" (organisches Wachstum verlangsamt auf 2% in Q2 2026,
Aktie -26% YTD/-50% über 12 Monate) — UND der Aktienkurs selbst zeigt
gerade jetzt einen scharfen Rücksetzer. Das ist eine unmittelbare
Bewährungsprobe für die "Gründliche-These-Prüfung"/Timing-vs-Struktur-
Logik, die bei diesem Rücksetzer bewusst NICHT zu einem Panik-Verkauf
geraten hat — derselbe Compounder, derselbe Test, zehn Jahre später.

---

## Gesamtfazit

| Fall | Getestet | Ergebnis |
|---|---|---|
| Wirecard (Betrug) | Going-Concern-Precheck + Beneish-Fraud-Check | Gemischt — Going-Concern hätte versagt (Prüfer selbst getäuscht), Beneish wäre plausibel fündig geworden |
| WeWork (Governance) | K-Kriterien + Management-Risiko-Check | Treffer — hätte vor IPO abgelehnt |
| Constellation Software (Gewinner) | K-Kriterien/ROIC-Schwelle, False-Positive-Test | Treffer — hätte korrekt gekauft, 10J-Outperformance bestätigt |

**2 von 3 klar bestätigt, 1 von 3 mit einer echten, benennbaren
Schwachstelle** (Going-Concern-Guardrail versagt bei aktivem,
mehrjährigem Betrug mit kooperierendem/getäuschtem Prüfer — eine
Kategorie, gegen die sich kein regelbasiertes System aus öffentlichen
Daten zuverlässig wappnen kann, das ist keine Playbook-spezifische
Schwäche, sondern eine grundsätzliche Grenze fundamentaler
Öffentliche-Daten-Analyse).

**Was dieser Test NICHT zeigt:** ob das Regelwerk bei den viel
häufigeren, uneindeutigen Fällen (keine Fraud, keine offensichtliche
Governance-Katastrophe, kein 20%-ROIC-Compounder, sondern "irgendwo in
der Mitte") tatsächlich Mehrwert liefert. Das bleibt nur über echte Zeit
und den eigenen Live-Track-Record verifizierbar.

## Prozess (ab sofort)

Kein wiederkehrender automatisierter Check (zu aufwendig, zu wenig neue
historische Fälle pro Monat) — aber bei Gelegenheit (z.B. wenn ein
bekannter historischer Fall im Gespräch auftaucht) kann diese Datei um
weitere Fallstudien ergänzt werden, um die Stichprobe über die Zeit
langsam zu vergrößern.

## Quellen

- [Reimagining audit quality using Wirecard and PCAOB standards](https://www.acfe.com/fraud-magazine/all-issues/issue/article?s=2021-marapr-caseinpoint)
- [Wirecard earnings 2018 full year (CNBC)](https://www.cnbc.com/2019/04/25/wirecard-earnings-2018-full-year.html)
- [Whistleblower warned EY of Wirecard fraud four years before collapse (Irish Times)](https://www.irishtimes.com/business/financial-services/whistleblower-warned-ey-of-wirecard-fraud-four-years-before-collapse-1.4367784)
- [Using Machine Learning to Detect Financial Statement Fraud: Wirecard AG (MDPI)](https://www.mdpi.com/1911-8074/18/11/605)
- [WeWork releases S-1 filing, reveals massive $900M loss (CNBC)](https://www.cnbc.com/2019/08/14/wework-releases-s-1-filing.html)
- [The strangest and most alarming things in WeWork's IPO filing (CNBC)](https://www.cnbc.com/2019/08/17/wework-ipo-filing-strangest-and-most-alarming-things.html)
- [WeWork's $47 Billion IPO Collapse in Six Weeks](https://ibinterviewquestions.com/case-studies/wework-failed-ipo)
- [Constellation Software president's letter 2013](https://www.csisoftware.com/docs/default-source/investor-relations/presidentletter/presidentletter_2013.pdf)
- [Constellation Software ROIC (GuruFocus)](https://www.gurufocus.com/term/ROIC/CNSWF/ROIC-/Constellation-Software-Inc)
- [Assessing Constellation Software valuation (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/assessing-constellation-software-tsx-csu-220925694.html)
