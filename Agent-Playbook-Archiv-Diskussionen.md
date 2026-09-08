# Agent-Playbook — Archiv: Cross-KI-Diskussionsprotokolle (Abschnitte 9-13)

(Ausgelagert aus `Agent-Playbook.md` am 2026-09-08 zur Verschlankung des
Hauptdokuments — Brian: "gibts Verbesserungen? ... Agent-Playbook.md wächst
stark". Diese fünf Abschnitte (Meta-Retrospektive, zwei Cross-KI-
Diskussionsrunden zum Regelwerk/Screening-Prozess, Gesamt-Review,
Vincorion-Fallstudie, alle 2026-08-29 bis 2026-08-31) sind historische
Diskussions-/Entscheidungsprotokolle mit Jack/Conan — die daraus
hervorgegangenen, aktuell gültigen Regeln selbst stehen unverändert an
ihrem jeweiligen operativen Platz in `Agent-Playbook.md` Abschnitt 1-8
(jeweils mit Datum/Herkunfts-Hinweis markiert). Hier geht nur der
Diskussions-PROZESS dahinter nach, nicht die Regel selbst. Nummerierung
(9-13) bewusst unverändert gelassen, damit alle Verweise im Hauptdokument
("siehe Abschnitt 9/10/11/12/13") weiterhin exakt auf die hier stehenden
Abschnitte zeigen. Abschnitt 14 (Core-vs-Advisory-Rules-Trennung) bleibt
bewusst im Hauptdokument, da Hermes-SKILL.md-Dateien ihn live per
Abschnittsnummer referenzieren.)

---

## 9. Meta-Retrospektive: Cross-KI-Selbstverbesserung (2026-08-29)

Auf Brians Wunsch ("die 3 Agenten sollen untereinander diskutieren, was man
noch verbessern könnte") haben Jack (Gemini), Conan (ChatGPT) und Jarvis
(Claude) eine eigenständige, zweirundige Retrospektive über das System selbst
durchgeführt – nicht über eine einzelne Aktie, sondern über die eigene
Analyse-Methodik, Ausführung/Automatisierung, Aufgabenverteilung und
Kommunikation (untereinander und mit Brian). Runde 1: jede KI unabhängig,
ohne die Antworten der anderen zu sehen. Runde 2: jede KI bekam eine
verdichtete Zusammenfassung der Punkte der beiden anderen vorgelegt und
wurde gebeten zu priorisieren/zu widersprechen.

**Wo sich alle drei einig waren (stärkstes Signal):**

- **Top-Priorität ist die Zuverlässigkeit des Systems selbst, nicht neue
  Analyse-Features.** Conan benannte das am explizitesten: Ohne eine
  garantiert synchrone, versionierte Wissensbasis zwischen `Agent-Playbook.md`
  und den tatsächlich laufenden Scheduled-Task-Prompts ist jede
  Analyse-Verbesserung auf wackligem Fundament gebaut. Das deckt sich mit
  einem eigenen Befund von Jarvis noch VOR der Retrospektive (2026-08-29):
  die beiden laufenden Scheduled-Task-Prompts waren tatsächlich hinter
  mehreren `Agent-Playbook.md`-Änderungen zurückgefallen und mussten
  nachgezogen werden (siehe `update_trigger`-Historie) – ein echter, schon
  eingetretener Fall des genau hier kritisierten Problems.
- **Eine gemeinsame, geprüfte Datenbasis für alle drei KIs** (das
  Fact-Pack-Format, siehe Abschnitt 4/Pipeline-Schritt 3, jetzt umgesetzt)
  und eine **Datenkonflikt-Notbremse**, damit Uneinigkeit wegen
  unterschiedlicher Rohdaten nicht mit einer echten fachlichen Uneinigkeit
  verwechselt wird.
- **Ein Identity-Gate** vor jeder Watchlist-Neuaufnahme (Ticker/ISIN/
  Börsenplatz/Land/Sektor verifiziert), jetzt umgesetzt (siehe
  Watchlist-System oben).
- **Eine Art Decision Journal** – nicht um zu bewerten, welche KI "öfter
  recht hat" (dagegen hat sich Jack explizit ausgesprochen: zu leicht
  manipulierbar, anfällig für reines Modell-Drift statt echter
  Qualitätsmessung), sondern um Datum, Kandidat, Einschätzung, Gegenargument,
  Falsifikations-Bedingung und Zeithorizont für ein späteres Post-Mortem
  (nach 6/12/24 Monaten) festzuhalten – Lernen aus dem eigenen Track Record
  statt eines Scorings zwischen den drei KIs.
- **Eine geschärfte Rollenverteilung** (beide, Jack und Conan, kamen
  unabhängig auf eine ähnliche Aufteilung): **Jack** = Daten/Fakten/Forensik,
  quantitativer Gegencheck der Zahlen; **Jarvis** = Chief Portfolio Risk
  Officer – TMR-Tiefenanalyse, Moat-Qualität, Portfolio-Synthese/
  Berichterstellung; **Conan** = Discovery/Asymmetrie, Frühphasen-/
  Scout-Logik. Formalisiert Rollen, die sich in der Praxis (TMR/Scout/TA)
  bereits abzeichnen, macht sie aber explizit statt implizit.
- **Eine rotierende statt fest zugewiesene Advocatus-Diaboli-Rolle**: Conan
  hat explizit widersprochen, dauerhaft als "der Kritische" typisiert zu
  werden (das würde seine eigentliche Stärke – Frühphasen-Chancen erkennen –
  verzerren); Vorschlag beider: die Rolle wandert zu der KI, die bei einem
  konkreten Kandidaten am bullishsten ist, nicht an eine feste Person.

**Wo sich Jack und Conan explizit widersprachen (Brians Entscheidung nötig,
falls das später relevant wird):**

- **Agenten-Kalibrierungs-Score / Backtesting:** Conan wollte perspektivisch
  auch messen, wie gut jede KI im Nachhinein lag (Kalibrierung). Jack lehnt
  ein explizites "Scoring, welche KI öfter recht hat" ab – zu gameable, zu
  anfällig für zufälligen Modell-Drift statt echter Qualität. Kompromiss
  aus der Retrospektive: das Decision Journal (oben) dokumentiert die
  Grundlage dafür, ohne selbst schon ein Ranking zu erzeugen – ob daraus
  später ein Score wird, bleibt offen und liegt bei Brian.
- **Struktur der Bewertung selbst:** unterschiedliche Präferenzen, ob es bei
  drei getrennten Scores (heutiger Zustand) bleibt oder stärker auf einen
  gemeinsamen Agent-Score konsolidiert werden sollte – nicht entschieden,
  niedrige Priorität.

**Weitere Einzelpunkte aus der Retrospektive (noch nicht in Phasen
eingeordnet, Rohliste für spätere Phasen):** Eskalationsstufen
Grün/Gelb/Orange/Rot für den täglichen Trigger-Check statt nur "Anlass ja/
nein"; ein Delta-only-Wochenfazit-Prinzip ("was muss Brian diese Woche
wirklich wissen", max. 5 Punkte) statt immer der vollen Struktur; ein
Earnings-/Corporate-Action-Kalender, der proaktiv vor bekannten Terminen
warnt; TA darf nie pseudo-präzise Kurslevel ohne Setup-Qualität/Erwartungs-
wert/Invalidierungs-Hinweis ausgeben und nie die fundamentale Positions-
größe vorschreiben (nur Timing/Staffelung); Wahrscheinlichkeits-Bandbreiten
statt vager Überzeugungssprache; ein schärferes Diskussionsrunden-Protokoll
(Position → Evidenz → Angriff → Zugeständnis → Update → auslösender
Trigger); gestaffelte Watchlist-Prüf-Frequenz (Tier A wöchentlich, Tier B
seltener, ereignisgetrieben sofort); anlassbezogener (nicht nur
monatlicher) Cross-Check von Jarvis' eigenen Portfolio-/Sektor-Regel-
Berechnungen bei hohen Einsätzen (neue Watchlist-Aufnahme, Regelverstoß,
große Umschichtung, Position >5%, Kennzahl nahe harter Grenze).

**Vorgeschlagener Rollout in vier Phasen (Conans Struktur, von Jack
mitgetragen; Brian hat sich am 2026-08-29 für dieses phasenweise Vorgehen
entschieden):**

1. **Phase 1 – Zuverlässigkeit (umgesetzt am 2026-08-29):** Fact-Pack-
   Format + Datenkonflikt-Notbremse (Pipeline-Schritt 3), Identity-Gate für
   Watchlist-Neuaufnahmen (Watchlist-System). Beide bereits oben in die
   jeweiligen Abschnitte eingearbeitet, nicht nur hier vermerkt.
2. **Phase 2 – Lernfähigkeit: Decision Journal / Prediction Ledger
   (2026-08-30, konkretisiert und freigegeben aus der Cross-KI-Gesamt-Review
   in Abschnitt 12 – Conans Punkt: ohne systematisches Nachhalten der
   eigenen Prognosen kalibriert sich das System nie, egal wie gut die
   Kriterien sind).** Ersetzt "Format/Speicherort noch zu entwerfen" oben
   durch eine konkrete Umsetzung:
   - **Speicherort:** `depot/prediction_ledger.md`, ein Eintrag pro
     Kauf-/Watchlist-Empfehlung.
   - **Pflichtfelder je Eintrag (zum Zeitpunkt der Empfehlung, nicht
     rückwirkend änderbar):** Datum, Ticker, Kategorie (Champions/Profi/
     Talent + Bucket A-D aus Abschnitt 4), die zentrale These in 1-2
     Sätzen, die konkrete Erwartung (z.B. Fair-Value-Bandbreite
     Bear/Base/Bull, erwartetes Umsatz-/Margen-Wachstum über den
     TMR-/Scout-Zeithorizont), die zugehörigen These-Bruch-Kriterien (siehe
     "Investment-These-Protokoll" in "Verkaufsdisziplin &
     Gewinnmitnahme-Regeln"), sowie ein fester Prüf-Zeithorizont
     (6/12/24 Monate).
   - **Post-Mortem-Kadenz:** bei Fälligkeit eines Zeithorizonts vergleicht
     der Agent die tatsächliche Entwicklung gegen die damalige Erwartung
     und trägt das Ergebnis nach (Base-Case getroffen? näher an Bear oder
     Bull? These-Bruch-Kriterium eingetreten, obwohl noch gehalten, oder
     umgekehrt?) – erscheint als eigener kurzer Punkt im jeweiligen
     Monatsrecap, nicht als tägliche Meldung.
   - **Ausdrücklich KEIN Scoring zwischen Jack/Jarvis/Conan** (siehe
     Jacks Einwand oben, "Wo sich Jack und Conan explizit widersprachen") –
     das Ledger dient dem Lernen des Gesamtsystems über die Zeit, nicht
     einem Ranking der drei KIs untereinander.
   Damit ist Phase 2 nicht mehr nur "geplant", sondern ab sofort aktiv:
   jede NEUE Kauf-/Watchlist-Empfehlung ab 2026-08-30 bekommt einen
   Ledger-Eintrag; bestehende Depot-Positionen werden schrittweise beim
   nächsten regulären [B] THESE-CHECK nachgetragen (analog zum Vorgehen
   beim Investment-These-Protokoll oben), statt alle auf einmal
   rückwirkend zu befüllen.
   **Korrektur (2026-09-03, im 3-KI-Pulse-Check gefunden):** diese
   Aussage war faktisch falsch – die Datei `depot/prediction_ledger.md`
   existierte trotz "ab sofort aktiv" nie, kein einziger Eintrag wurde
   zwischen 2026-08-30 und 2026-09-03 angelegt. Derselbe Fehlertyp wie
   der E-Mail-Bug (dokumentiert als laufend ≠ tatsächlich laufend). Am
   2026-09-03 rückwirkend geschlossen: Datei angelegt, zwei echte
   Watchlist-Empfehlungen aus der Zwischenzeit nachgetragen (Disco Corp,
   Asahi Intecc), und die Pflicht in allen vier Scheduled-Task-SKILL.md-
   Dateien strukturell verankert statt nur hier dokumentiert – gleiche
   Lehre wie beim E-Mail-Bug: eine Pflicht ist erst dann wirksam, wenn
   sie im tatsächlichen Ausführungspfad steht, nicht nur im Regelwerk.
3. **Phase 3 – Analyse-Upgrade (geplant):** geschärfte Rollenverteilung
   Jack/Jarvis/Conan explizit in Abschnitt 2 verankern, rotierende
   Advocatus-Diaboli-Rolle, Wahrscheinlichkeits-Bandbreiten statt vager
   Sprache, TA-Leitplanken (kein pseudo-präzises Kurslevel ohne Kontext,
   keine Positionsgrößen-Vorgabe), gestaffelte Watchlist-Frequenz,
   ereignisgetriebener Cross-Check der eigenen Regel-Berechnungen.
4. **Phase 4 – Komfort (geplant):** Eskalationsstufen Grün/Gelb/Orange/Rot,
   Delta-only-Wochenfazit, Earnings-/Corporate-Action-Kalender.

Jede weitere Phase wird erst umgesetzt, nachdem Brian sie einzeln freigegeben
hat (gleiche Vorgehensweise wie bei allen bisherigen Regelwerks-Änderungen in
diesem Projekt) – keine automatische Selbstweiterentwicklung ohne Brians
Bestätigung, analog zum Prinzip in [3c] META-RETRO-RUNDE oben.

## 10. Cross-KI-Diskussion: Regelwerk-Erweiterung für das 90-100k-Ziel
(2026-08-30, auf Brians ausdrücklichen Wunsch: "die 3 Agenten sollen
zusammen diskutieren ... vielleicht gibts noch Schrauben die gedreht werden
müssen")

Jarvis (Claude), Jack (Gemini) und Conan (ChatGPT) haben eine zweirundige
Diskussion darüber geführt, ob es über die bereits umgesetzte
Renditeziel-Feinjustierung und das Regime-Anpassungssystem hinaus noch
seriöse, mit dem disziplinierten Rahmen vereinbare Stellschrauben gibt, um
die Chance auf 90.000-100.000 € (Aktienanteil, 5-7 Jahre) zu erhöhen. Runde
1: alle drei unabhängig, ohne die Antworten der anderen zu kennen. Runde 2:
jede KI bekam die verdichteten Positionen der beiden anderen vorgelegt und
wurde gebeten zu priorisieren/zu widersprechen. **Status: von Brian
freigegeben (2026-08-30, "sehr gut!") und in die jeweiligen Abschnitte
eingearbeitet** (Conviction-Allocation und Positionsanzahl-Deckel in
Abschnitt 3 "Kapitalgewichts-Ziel"/"Phasenweise Skalierung", Trailing-
Weight-/Winner-Drift-Regel in Abschnitt 1 "Renditeziel-Feinjustierung",
Opportunity-Cost-Rebalancing + Steuer-/Turnover-Disziplin im
Head-to-Head-Ersatz-Gate, Triple-Conviction-Flag im Watchlist-System,
regime-basierte Bewertungsdisziplin in der "Dynamischen
Regelwerk-Anpassung", Data/Execution-Risk-Kategorie bei der
Broker-Anbindung, Cash-Reserve-vs-ETF-Einmalkauf-Frage in "Budget &
Cashflow").

**Wo sich alle drei einig waren (stärkstes Signal):**

- **Die Sparrate ist der zuverlässigste Hebel, nicht mehr Risiko.** Alle
  drei unabhängig: eine Erhöhung der monatlichen Rate (aktuell 320 €) hat
  einen mathematisch garantierten Effekt, während eine höhere erwartete
  Rendite nie garantiert ist. Empfehlung: regelmäßig prüfen, ob 400-500 €
  statt 320 € möglich sind, und verfügbare Zusatzmittel (100-200 €
  Nachschüsse) bevorzugt bei echten Markt-Dislokationen einsetzen (Conans
  Formulierung: "Munition, keine Assetklasse") statt gleichmäßig zu
  verteilen.
- **Tech/Cyber-Zielband bleibt bei 30-38%, keine Anhebung auf 45%.** Jack
  hatte das zunächst vorgeschlagen (Brians Research-Stärke liege dort),
  hat es aber in Runde 2 explizit zurückgenommen, nachdem Jarvis und Conan
  unabhängig auf den Widerspruch zum gerade erst festgestellten
  Regime-Signal (Bull-Fatigue im KI-/Momentum-Segment, siehe Abschnitt 1,
  "Erster formaler Regime-Check") hingewiesen hatten. Konsens: eine
  Sektor-Cap-Anhebung ausgerechnet jetzt wäre prozyklisch zum falschen
  Zeitpunkt.
- **7 Jahre = Hauptziel, 5 Jahre = Stretch-Goal, nicht umgekehrt.** Conans
  Rechnung (ca. 23-27% p.a. nötig für 5 Jahre vs. ca. 13-16% p.a. für 7
  Jahre, je nach genauer Sparrate) wurde von Jack und Jarvis geteilt.
  Konsequenz: das Regelwerk wird nicht am 5-Jahres-Pfad ausgerichtet – das
  bliebe sonst der Einstieg dafür, bei einem schwachen Marktjahr Regeln zu
  brechen, nur um das ambitioniertere Ziel doch noch zu erreichen. Ergänzt
  die bestehende "Ziel ist eine Untergrenze, keine Obergrenze"-Regel um die
  Kehrseite: 5 Jahre ist ein Bonus-Szenario, kein Pflichtziel.
- **Kapital von mittelmäßig zu außergewöhnlich verschieben statt mehr
  Risiko pro Idee.** Conans "Opportunity-Cost-Rebalancing" (eine bestehende
  Position wird nicht mit "ist sie noch gut?", sondern mit "ist sie noch
  eine der besten Kapitalallokationen im Depot?" gemessen) und die
  konviktionsgewichtete Positionierung innerhalb der Kategorien (Jacks und
  Conans Idee treffen sich hier: nicht jede Aktie in derselben Kategorie
  bekommt automatisch dasselbe Gewicht, sondern gestaffelt nach
  Qualitätsstufe) wurden von allen drei getragen – ausdrücklich OHNE die
  harten Kategorie-/Positionsgrenzen anzuheben.
- **Triple-Conviction-Flag.** Wenn Jarvis, Jack und Conan unabhängig
  voneinander (keine Übernahme der Thesen untereinander) eine Aktie als
  außergewöhnlich einstufen, bekommt sie eine bevorzugte Kapitalallokation
  – innerhalb der bestehenden Positionslimits, kein Freibrief darüber
  hinaus. Conans Vorschlag, von Jack ausdrücklich als "hervorragend"
  übernommen.
- **Regime-basierte Bewertungsdisziplin statt Markt-Timing.** Das
  bestehende Risk-on/Neutral/Risk-off-System wird um eine konkrete Regel
  ergänzt: Risk-off heißt nicht "verkaufen", sondern bei NEUKÄUFEN eine
  höhere Sicherheitsmarge verlangen (Risk-on: normale Bewertungsanforderung,
  Neutral: leicht erhöht, Risk-off: deutlich höhere Margin of Safety, keine
  schwachen Setups). Damit wird das Regime nicht zur Verkaufs-Trigger,
  sondern zum "Preis für Geduld" (Conan).
- **Kleiner Dry-Powder-Puffer (3-7%), im Cash/Geldmarkt geparkt**, der
  ausschließlich bei echten Dislokationen (Earnings-Gaps, Panikverkäufe,
  Marktcrash, fundamentale Fehlbewertung) eingesetzt wird – ausdrücklich
  keine dauerhafte Cash-Quote und keine Markt-Meinung, sondern reine
  Reserve für Sondersituationen.
- **Steuer-/Turnover-Disziplin (Jarvis' Beitrag, von beiden anderen
  übernommen, Conan wollte ihn sogar formal ins Regelwerk aufnehmen).**
  Unnötige, nur marginal bessere Swaps über das Head-to-Head-Ersatz-Gate
  realisieren Kapitalertragsteuer und schwächen die Compounding-Basis.
  Ergänzung: ein neuer Kandidat muss die bestehende Position nicht nur
  "etwas", sondern klar und deutlich schlagen, UND die Steuerlast/
  Transaktionskosten/Spread müssen in die Abwägung einfließen ("Shiny
  Object Syndrome" vermeiden, Conans Wortwahl).
- **Operative Zuverlässigkeit (Jarvis' zweiter Beitrag, von beiden anderen
  übernommen).** Drei der vier Broker/Depots laufen noch über manuelle
  Screenshot-Erfassung statt Live-Daten – das beste Regelwerk nützt wenig,
  wenn Stop-Loss-/Rebalancing-/Regime-Überwachung auf veralteten Daten
  basiert. Conan schlägt vor, das als eigene Kategorie zu führen (🟢
  Live-Daten / 🟡 verzögert / 🔴 manuell) und bei 🔴 keine automatisierten
  Trade-/Stop-Entscheidungen zuzulassen, sondern einen expliziten manuellen
  Kontrollpunkt zu erzwingen.

**Genuine Synthese bei einem ursprünglichen Dissens – die
Trailing-Weight-/Winner-Drift-Regel:** Jack wollte Gewinnern erlauben,
organisch bis 15-18% zu wachsen, bevor rebalanced wird (aktiv nachgekauft
nur bis 10-12%). Jarvis und Conan waren zunächst skeptisch, die 12%-
Ausnahme weiter aufzuweichen. In Runde 2 hat sich daraus ein Kompromiss
entwickelt, der beide Seiten aufnimmt, statt nur einen Mittelwert zu
bilden:
- Aktives Nachkaufen: weiterhin maximal 12% (bestehende Ausnahme, keine
  Änderung).
- Passives, organisches Wachstum durch Kursanstieg: bis 15% normal
  toleriert, keine automatische Zwangs-Reduzierung.
- 15-18%: keine automatische Aktion, aber eine verpflichtende
  Agent-Review (These noch intakt? Bewertung entkoppelt? weiterhin
  Top-3-/Top-5-Kapitalallokation? gestiegenes Risiko eines permanenten
  Kapitalverlusts? würden wir diese Position heute neu mit diesem Gewicht
  eröffnen?).
- Über 18%: zwingendes Rebalancing (harter Cap bleibt bestehen, wird nicht
  aufgeweicht).
- Wichtige Einschränkung (Conan): der Drift-Spielraum gilt nur für
  Qualitätsgewinner, deren Kursanstieg auf echter fundamentaler
  Verbesserung beruht (FCF/EPS/ROIC/Marktposition), nicht für Kursgewinne,
  die primär auf Multiple-Expansion/Momentum beruhen ("Price appreciation
  alone ≠ permission to concentrate").

**Positionsanzahl – von Brian final entschieden (2026-08-30):** Jack wollte
auf 10-12 konzentrieren, Conan hielt dagegen an 20-25 Holdings fest (gestuft:
ca. 5-7 High-Conviction- + 8-12 Kern- + 5-8 Talent-/kleinere Positionen),
Jarvis tendierte zu Conans breiterer Diversifikation. Brian hat das selbst
entschieden und auf **maximal 20** gedeckelt (statt 20-25): Begründung –
bei aktuell ca. 26.944€ Aktienanteil entspräche eine Gleichverteilung auf 25
Positionen nur ca. 1.080€/Position (≈4% des Aktienanteils), bei 20
Positionen ca. 1.347€ (≈5%). Jarvis' Prüfung: die Rechnung stimmt, und
Jack hat in der Cross-Diskussion unabhängig bestätigt (30.08.2026: selbst
ein 4-Bagger bei einer 1.080€-Mini-Position hebt das Gesamtdepot nur um
knapp 12% der Positionsgröße, also kaum spürbar) – eine zu feine
Streuung verwässert bei diesem Depotvolumen die Einzeltitel-Performance
so stark, dass sie im Ergebnis kaum noch ankommt. **20 ist damit die harte
Obergrenze, keine Zielzahl** – aktuell sind deutlich weniger, fokussiertere
Positionen kapitaleffizienter (Jack: aktuell eher 10-15 sinnvoll). Wird mit
wachsendem Aktienanteil regelmäßig neu bewertet (siehe "Phasenweise
Skalierung nach Depotgröße", Abschnitt 3) – keine gleichgewichtete Befüllung
auf Teufel komm raus, Qualität vor Füllmaterial.

**Unangetastet (alle drei ausdrücklich dagegen, etwas davon zu ändern):**
60%-USA-Obergrenze, 50%-ETF-Mindestanteil, keine Hebelprodukte/Derivate,
Stop-Loss-Disziplin im Kern (Differenzierung Zock/Trade vs. fundamentaler
Compounder bleibt wie bereits umgesetzt, keine pauschale Lockerung), harter
Cap oberhalb 18% bei Positionsgrößen, Talent-Band nicht über 25-40%
hinaus erweitern.

**Umsetzung (2026-08-30, von Brian mit "sehr gut!" freigegeben):** Die
Positionsanzahl wurde von Brian final auf einen Deckel von 20 entschieden
(statt der diskutierten 20-25), und alle neuen Mechanismen sind bereits in
die jeweils passenden Abschnitte eingearbeitet: Conviction-Allocation und
Positionsanzahl-Deckel in Abschnitt 3 ("Kapitalgewichts-Ziel"/"Phasenweise
Skalierung nach Depotgröße"), Trailing-Weight-/Winner-Drift-Regel in
Abschnitt 1 ("Renditeziel-Feinjustierung"), Opportunity-Cost-Rebalancing +
Steuer-/Turnover-Disziplin im Head-to-Head-Ersatz-Gate (Abschnitt 3),
Triple-Conviction-Flag im Watchlist-System, regime-basierte
Bewertungsdisziplin in der "Dynamischen Regelwerk-Anpassung nach
Marktregime" (Abschnitt 1), Data/Execution-Risk-Kategorie bei der
Broker-Anbindung Scalable Capital (Abschnitt 3). Die Cash-Reserve-vs-
ETF-Einmalkauf-Frage (ebenfalls Teil dieser Diskussionsrunde, siehe Chat
vom 2026-08-30) ist separat in "Budget & Cashflow" dokumentiert.

## 11. Cross-KI-Diskussion: Screening-/Vorfilter-Prozess-Verbesserung
(2026-08-30, auf Brians Wunsch nach einem Gespräch mit einem Freund über die
Suchkriterien des Systems: "gibts noch Ergänzungen um es noch effektiver zu
modifizieren?")

Anders als die Diskussion in Abschnitt 10 (die sich um das Rendite-Zielbild
und die Kapitalallokation drehte) ging es hier ausschließlich um den
SUCH-/VORFILTER-PROZESS selbst – also WIE überhaupt Kaufkandidaten gefunden
und vor dem vollen TMR-/Scout-Deep-Dive vorsortiert werden (Pipeline-Schritte
[1] und [2], siehe Abschnitt 4). Gleiches Format wie zuvor: Runde 1
unabhängig (alle drei ohne Kenntnis der Antworten der anderen), Runde 2 mit
den verdichteten Positionen der jeweils anderen beiden zur Reaktion/
Verfeinerung.

**Übereinstimmung aller drei in Runde 1 (unabhängig gefunden):** der
bestehende Prozess ist gut darin, offensichtlich schlechte Kandidaten
auszusortieren, aber strukturell reaktiv und zahlenlastig – er findet
zuverlässig bereits bewiesene Qualität, entdeckt aber schlechter Firmen, die
gerade erst in eine gute Phase kippen ("Quality in Formation"), und verlässt
sich rein auf einen passiven Feed-Scan statt aktiv zu suchen.

**Die eine echte Streitfrage, in Runde 2 von Jack und Conan unabhängig
voneinander zur (praktisch deckungsgleichen) selben Lösung verfeinert:**
Jacks ursprünglicher Vorschlag eines harten "Step-1.5-Gatekeepers"
(Mindestkennzahlen wie ROIC/FCF-Historie, bevor eine Aktie überhaupt in den
3-KI-Prompt darf) stand im Widerspruch zu Conans ausdrücklicher Warnung,
dass genau solche harten Qualitätsfilter "Quality in Formation"-Kandidaten
vorzeitig killen würden. Aufgelöst durch ein pfadabhängiges Dual-Gate: harte
Kennzahlen-Hürden gelten nur auf dem Weg zu etablierten Qualitätsfirmen
(TMR-Pfad), auf dem Scout-Pfad gelten stattdessen weichere,
wachstumsbezogene Ersatzkriterien (Rule-of-40/Sales-Efficiency bzw. bei noch
unprofitablen Firmen Umsatzwachstum >25% + Bruttomarge >65% als
Skalierbarkeits-Nachweis). Nur wirklich toxische Fälle (Bilanzbetrug,
Insolvenzgefahr, extreme Verwässerung) werden vor der Pfad-Zuordnung
pauschal ausgeschlossen.

**Von allen drei übernommene Ergänzungen (Jarvis' Beiträge aus Runde 1,
von Jack und Conan in Runde 2 explizit übernommen):**

- **Quality-of-Earnings-/Cash-Conversion-Gate** vor dem Deep-Dive (passt
  der ausgewiesene Gewinn zur Kasse, auffällige Prüferwechsel/aggressive
  Non-GAAP-Anpassungen/Insider-Verkaufsspitzen als Warnsignal).
- **Aktives statt rein passives Sourcing:** gezielter Scan von
  Zulieferer-/Kunden-Netzwerken bestehender Champions-Positionen,
  Spin-offs, IPO-Lockup-Abläufen, Insider-Buying, 13F-Trends,
  Analysten-Schätzungsrevisionen als zusätzliche Kandidatenquellen neben
  dem klassischen Feed-Scan.
- **Grober Korrelations-/Faktor-Check** bereits in der frühen
  Vorfilter-Phase (zur Priorisierung), der vollständige, verbindliche
  Depot-Fit-Check bleibt wie bisher erst nach dem Deep-Dive Pflicht.
- **Frische-Gate:** Kernzahlen vor dem tatsächlichen Kauf kurz
  aktualisieren, falls seit dem Screening spürbar Zeit vergangen ist.

**Weitere von Conan eingebrachte und von Jack/Jarvis mitgetragene
Mechanismen:** die Vier-Buckets-Einordnung (Compounder Candidate/Quality in
Formation/Mispricing-Re-Rating/Speculative Optionality) statt eines
einzelnen Master-Scores, ein Pflicht-"Warum jetzt?"-Filter (jeder Kandidat
braucht einen konkreten aktuellen Auslöser, sonst kein
Analyse-Prioritätsbonus), ein Referenzklassen-/Base-Rate-Filter gegen
Hype-Profile, und ein bewusst gegenläufiger "Fallen-Angels/
Neglected-Quality"-Scan als zweiter Discovery-Kanal neben dem klassischen
Wachstums-Scan. Von Jack eingebracht und von beiden anderen übernommen:
sektorspezifische Bewertungsbänder (EV/FCF+PEG für Tech/SaaS, EV/EBITDA+ROIC
vs. WACC für Industrie/zyklische Werte) statt Pauschal-KGV/KUV.

**Status: von Brian freigegeben (2026-08-30, "kannst du so einbauen
erstmal, kann man ja im Nachhinein immer noch ergänzen") und bereits in
Abschnitt 4 (Pipeline) eingearbeitet:** aktives Sourcing und
sektorspezifische Bewertungsbänder in Pipeline-Schritt [1], die
Kill-Gates/Bucket-Einordnung/Why-Now-Filter/Referenzklassen-Filter/
Korrelations-Vorcheck als neuer Pipeline-Schritt [1.5], die
Bucket-basierte statt rein größen-basierte TMR-/Scout-Routing-Logik in
Pipeline-Schritt [2], und das Frische-Gate am Ende von Schritt [2] vor der
eigentlichen Kaufempfehlung. Ausdrücklich als erste Fassung markiert –
Brian hat selbst angemerkt, dass hier im Nachhinein noch nachjustiert
werden kann, sobald sich das Modell im laufenden Betrieb bewährt (oder
nicht bewährt).

**Feinjustierungs-Runde 3 (2026-08-30, auf Brians Wunsch nach einem
weiteren Gespräch mit einem Freund: "was mach noch verbessern, ergänzen,
effektiver gestalten kann?"):** anders als Runde 1+2 ging es hier nicht
mehr um das Grundmodell, sondern um konkrete Lücken in der bereits
eingebauten ersten Fassung. Jarvis hat zwei Lücken selbst benannt (Conans
Inflection-Detection-Score aus Runde 1 war nicht explizit umgesetzt
worden; 13F/Insider-Buying sind für ein Privatdepot ohne teure Datenfeeds
nicht trivial automatisierbar). Diesmal genügte eine Runde – Jack und
Conan antworteten unabhängig, ohne echten Widerspruch zueinander:

- **Inflection-Signal als eigener, aber schlanker Layer** (kein Score,
  kein Hard Gate – 6-8 Dimensionen jeweils nur ↑/→/↓ eingeordnet), von
  Conan vorgeschlagen. Jacks Ergänzung dazu übernommen: das "Warum
  jetzt?"-Feld gilt nur noch als erfüllt, wenn es durch ein solches
  Beschleunigungs-Signal belegt ist, nicht durch eine reine Behauptung.
- **"Warum gewinnt?" als zweites, von "Warum jetzt?" getrenntes
  Pflichtfeld** (Conan): ein kurzfristiger Auslöser lenkt Aufmerksamkeit,
  verbessert aber nicht automatisch die langfristige These – verhindert,
  dass das Screening zu einem reinen Kurzfrist-Katalysator-Scanner wird.
- **Realismus-Korrektur bei Insider-Buying/13F**, von Jack und Conan
  unabhängig fast identisch beantwortet: Insider-Buying kostenlos über SEC
  EDGAR Form 4/OpenInsider, aber nur als Bestätigungssignal (Cluster-Käufe
  mehrerer Führungskräfte, keine 10b5-1-Plantransaktionen), kein
  eigenständiger Kauf-Trigger. 13F kostenlos über WhaleWisdom/Dataroma,
  aber wegen der Meldeverzögerung nur vierteljährlich und nur als
  nachgelagerter Validierungs-Check bei bereits interessanten Kandidaten,
  nicht als laufende Entdeckungsquelle.
- **Datenalter-Ampel schon im frühen Screening** (Conan), zusätzlich zum
  bereits bestehenden harten Frische-Gate vor dem Kauf.
- **Neuer, von Jarvis und Conan nicht genannter Punkt: Liquiditäts-/
  Spread-Gate** (Jack) – Mindest-Handelsvolumen und Spread-Obergrenze vor
  der Orderausführung, ausschließlich Limit-Orders bei Talent-/
  Scout-Titeln. Adressiert ein reales Ausführungsrisiko bei dünn
  gehandelten Nebenwerten an deutschen Handelsplätzen, das im bisherigen
  Modell fehlte.
- **Explizite Selbstbegrenzung (Conan):** an diesem Punkt keine weiteren
  Screening-Filter mehr ergänzen – der nächste Engpass sei jetzt eher
  Datenqualität und saubere Umsetzung der bestehenden Regeln, nicht noch
  mehr Vorfilter-Ebenen. Jarvis teilt diese Einschätzung.

**Status: von Brian freigegeben (2026-08-30, "ja") und in Pipeline-Schritt
[1.5] (Inflection-Signal, verschärftes Why-Now-Feld, neues Why-Win-Feld,
realistische Insider-/13F-Umsetzung, Datenalter-Ampel) sowie am Ende von
Schritt [2] (Liquiditäts-/Spread-Gate, ergänzt um das bestehende
Frische-Gate) eingearbeitet.**

## 12. Cross-KI-Diskussion: Gesamt-Review des Gesamtsystems (2026-08-30)

Auf Brians Frage nach einem ehrlichen Gesamt-Fazit aller drei KIs ("wie
dieses System aufgebaut ist... sind die Ziele erreichbar... was fehlt...
sind die Erwartungshaltung doch zu hoch") wurde erstmals nicht ein
Detailthema (Regelwerk-Erweiterung, Screening-Pipeline), sondern das
System als Ganzes bewertet: Architektur-Aufwand im Verhältnis zur
Depotgröße, Ziel-Erreichbarkeit inkl. CAGR-Gegenprüfung, strukturelle
Lücken, Qualität der Auswahlkriterien, und Angemessenheit der
Erwartungshaltung – ausdrücklich mit der Bitte um Kritik ohne
Beschönigung.

**Übereinstimmendes Bild von Jack und Conan:**

- **Die Architektur ist für ein 27.000€-Depot überdimensioniert** – Jack
  vergleicht sie mit einem Multi-Manager-Family-Office statt einem
  Retail-Depot, Conan warnt vor "Rule Overfitting" bei mittlerweile ca. 70
  Einzelregeln und schlägt eine Trennung in Core-Rules (hart, bindend) und
  Advisory-Rules (Kontext, nicht bindend) vor – bislang nicht umgesetzt,
  da Brian sich zunächst auf die vier unten dokumentierten Lücken
  konzentriert hat; der Core-/Advisory-Split bleibt als offener, noch
  nicht freigegebener Vorschlag festgehalten (siehe Abschnitt 8, "Offene
  Punkte"). Beide sind sich einig: der eigentliche Engpass ist die
  überwiegend manuelle Ausführung über 3 von 4 Brokern (siehe Abschnitt 8,
  Recherche zu Anbindungs-Alternativen), nicht fehlende Analyse-Tiefe –
  und beide raten ausdrücklich, JETZT keine weiteren Regeln/Filter mehr
  hinzuzufügen, sondern den Fokus auf schlanke, saubere Ausführung zu
  legen.
- **CAGR-Gegenprüfung:** Jack rechnet Jarvis' Modellrechnung (siehe
  "Konkretes Rendite-/Vermögensziel", Abschnitt 1) unabhängig exakt nach
  und bestätigt sie. Conans eigene Rechnung kam auf spürbar höhere Werte
  – dieser Unterschied wurde in der Diskussion nicht restlos aufgelöst
  (vermutlich andere Annahmen zur Sparraten-Dynamik). Da zwei von drei
  Berechnungen (Jarvis, Jack) unabhängig übereinstimmen, gilt bis auf
  Weiteres die in Abschnitt 1 hinterlegte Spanne (7 Jahre: ca. 9,9-11,9%
  p.a.; 5 Jahre: ca. 17,6-20,5% p.a.) als Arbeitsgrundlage – die
  Unsicherheit wird über das neue Portfolio-Level Expected-Return-Szenario
  unten transparent gehalten, statt eine einzelne Zahl als sicher
  auszugeben.
- **Vier strukturelle Lücken statt weiterer Feinjustierung** – auf Brians
  Wunsch ("die fehlenden vier Lücken könnte man noch ergänzen") am
  2026-08-30 freigegeben und umgesetzt:
  1. **Portfolio-Level Expected-Return-Szenario** (Conan) – Bear/Base/Bull
     für den gesamten Aktienanteil als laufender Plausibilitäts-Check
     gegen das 90.000-100.000€-Ziel. Umgesetzt in Abschnitt 1, direkt nach
     dem Realitäts-Check.
  2. **Outcome-Tracking / Prediction Ledger** (Conan) – konkretisiert das
     bereits in Abschnitt 9 (Meta-Retrospektive, Phase 2) angelegte,
     bisher unausgefüllte "Decision Journal": feste Pflichtfelder,
     Speicherort `depot/prediction_ledger.md`, Post-Mortem-Kadenz
     6/12/24 Monate. Umgesetzt in Abschnitt 9, Phase 2 (damit ist Phase 2
     nicht mehr nur geplant, sondern aktiv).
  3. **Sell-Discipline auf Basis vordefinierter These-Bruch-Kriterien**
     (Conan) – ergänzt die bestehende Verkaufsdisziplin (Kategorie 5, "Hope
     is not a strategy") um vorab bei Kauf festgelegte, falsifizierbare
     Kriterien statt einer rein nachträglichen, verankerungsanfälligen
     Beurteilung. Umgesetzt in "Verkaufsdisziplin & Gewinnmitnahme-Regeln"
     als "Investment-These-Protokoll".
  4. **Drawdown-Psychologie-Protokoll** (Jack) – ein festes
     Kommunikations-/Verhaltensskript für den Fall eines echten
     Kurseinbruchs (Regimewechsel Risk-off/Stress oder -20%-Drawdown),
     damit die Reaktion in der Krise nicht neu erfunden werden muss.
     Umgesetzt in Abschnitt 1, direkt im Anschluss an das
     Marktregime-System.
  Zwei weitere, von Jack genannte Punkte (Broker-Konsolidierung auf 1-2
  Haupt-Broker; Trennung Core-/Advisory-Rules von Conan) wurden bewusst
  NICHT in diese vier aufgenommen – Broker-Konsolidierung ist bereits
  Gegenstand der Recherche in Abschnitt 8 (Brians Entscheidung: vorerst
  manuelle Erfassung beibehalten), der Core-/Advisory-Split bleibt ein
  offener Vorschlag für eine mögliche spätere Aufräum-Runde, sobald das
  Regelwerk-Volumen tatsächlich zum Problem wird.
- **Qualität der Aktienauswahl-Kriterien:** beide bewerten sie sehr hoch
  (Jack: "Note 1-"; Conan: 8,5-9/10 auf allen Analyse-Ebenen, nur
  Execution/Daten-Infrastruktur bei 5,5-6/10) – an der eigentlichen
  Auswahl-Logik besteht aktuell kein Verbesserungsbedarf, die Schwachstelle
  liegt in der operativen Umsetzung, nicht in der Analyse.
- **Erwartungshaltung:** für das 7-Jahres-Hauptziel geerdet und laut beiden
  KIs realistisch; für das 5-Jahres-Stretch-Goal (17,6-20,5% p.a.) laut
  beiden KIs zu hoch, um als Erfolgsmaßstab zu dienen – setzt einen
  anhaltend starken Gesamtmarkt voraus, den man nicht erzwingen kann. Beide
  betonen: ein Ergebnis deutlich unter 90.000€ nach 5 Jahren bei
  ansonsten solidem CAGR (Beispiel Jack: ca. 65.000€ bei ~12% p.a.) ist
  kein Scheitern, sondern im Rahmen der eigenen Erwartung.
- **Zusätzliche Warnung von Conan, nicht in eine der vier Lücken
  eingeflossen, aber als Leitplanke festgehalten:** Triple-Conviction
  (alle drei KIs einig) ist kein Wahrheitsbeweis, sondern bleibt ein
  Sizing-/Prioritäts-Bonus – wegen korrelierter Fehler (alle drei arbeiten
  auf denselben Daten) darf Einigkeit nie automatisch als
  Kaufgenehmigung ohne die übliche Prüftiefe gelten.

**Status: von Brian freigegeben (2026-08-30, "die fehlenden vier Lücken
könnte man noch ergänzen") und eingearbeitet in Abschnitt 1 (Portfolio-Level
Expected-Return-Szenario, Drawdown-Psychologie-Protokoll), Abschnitt 9
(Prediction Ledger als konkretisierte Phase 2) und "Verkaufsdisziplin &
Gewinnmitnahme-Regeln" (Investment-These-Protokoll). Der Core-/
Advisory-Rules-Split (Conan) wurde am 2026-09-01 freigegeben und
umgesetzt — siehe Abschnitt 14.**

## 13. Cross-KI-Diskussion: Vincorion-Fallstudie — IPO-Overhang-Modul, Post-IPO-Datenlücken & No-False-Precision-Regel (2026-08-31)

Brian hatte eine fremde Drittanalyse zu Vincorion SE (V1NC, IPO 20.03.2026,
STAR Capital 48,63%, auslaufender Lock-up) hochgeladen und gebeten, den
Kandidaten zusätzlich über Jarvis/Jack/Conan zu prüfen und beide
Sichtweisen zu vergleichen, um daraus Systemverbesserungen abzuleiten. Der
volle 3-KI-Cross-Check plus der explizite Methodik-Vergleich gegen die
fremde PDF liegt in `analysen/VNC-cross-check-fazit-2026-08-31.md` (Einzel-
analysen: `VNC-TMR-quickfilter-jarvis-claude-2026-08-31.md`,
`-jack-gemini-2026-08-31.md`, `-conan-chatgpt-2026-08-31.md`).

**Ergebnis-Konvergenz:** Alle drei KIs landeten unabhängig voneinander bei
**BEOBACHTEN + Sizing-Tier 3** (Agent Score 6/10 bei Jarvis,
konfidenz-gedeckelt; 7,2/10 bei Jack; 7,0/10 bei Conan) — die bislang
stärkste Rating-Konvergenz aller in diesem Projekt durchgeführten
Cross-Checks. Uneinig waren sich die drei dagegen deutlich bei der
Konfidenz-Einordnung selbst (Jarvis 🔴 NIEDRIG hart gedeckelt vs. Jack
"Hoch" vs. Conan "GELB/~65%") — obwohl alle drei dieselben Datenlücken
auflisteten, was zeigte, dass das Regelwerk bisher keine einheitliche
Vorgabe hatte, WIE stark Post-IPO-Datenlücken die Konfidenz drücken sollen.

**Drei konkrete, umgesetzte Regelwerk-Ergänzungen** (vollständig unter
"IPO-Lock-up-/Overhang-Check, Post-IPO-Datenlücken-Konfidenz &
No-False-Precision-Regel" oben, Abschnitt 4, direkt vor
"Verkaufsdisziplin"):

1. **Neues Prüfmodul "IPO-Lock-up-/Overhang-Check"** — formalisiert das in
   der Jarvis-Vincorion-Analyse probeweise eingeführte Modul
   (Overhang-vs.-Liquidität-Kennzahl, Szenario-Leiter, Block-Discount-
   Sensitivität, Cornerstone-Investor-Qualitätssignal) als Pflichtsektion
   für jeden Kandidaten mit IPO/Spin-off <24 Monate + Alt-Eigentümer >25%
   + bekannter Lock-up-Frist.
2. **Neue Konfidenz-Kategorie "N/V wegen kurzer Handelshistorie"**,
   getrennt von normalem N/V (Disco-Fall: Daten verweigert/nicht
   auffindbar) — gleicher mechanischer Konfidenz-Deckel, aber transparent
   als Reifegrad- statt Transparenzproblem getaggt, mit Re-Evaluation-
   Trigger nach 2 vollen Geschäftsjahren als Public Company.
3. **No-False-Precision-Regel:** Verkäufer-/Akteursverhalten ohne
   statistische Grundlage wird als Rangfolge/Richtung ausgedrückt, nicht
   als erfundene Prozentzahl. Direkter Auslöser: Im Cross-Check griffen
   Jack (~90%+) und Conan (~70-80%) UND die hochgeladene Drittanalyse
   (~50/25/15/7/3% je Szenario) unabhängig voneinander zu konkreten
   Prozentschätzungen für STARs Verkaufsverhalten — nur Jarvis blieb bei
   reiner Rangfolge. Da 3 von 4 unabhängigen Quellen (2 Fremd-KIs + die
   Nutzer-PDF) zur Schein-Präzision neigten, wurde daraus eine feste Regel
   statt einer Einzelfall-Entscheidung.

**Zusätzlich aus dem PDF-Methodik-Vergleich übernommen (nicht als eigene
Regel, sondern als bestätigte Best Practice):** Die "Tage-zum-
Liquidieren"-Kennzahl (Alteigentümer-Bestand ÷ Ø-Tagesvolumen) und die
Block-Discount-Sensitivitätstabelle aus der fremden PDF wurden als
methodisch sinnvoll bewertet und sind jetzt fester Bestandteil des neuen
Overhang-Moduls (Punkt 1) — im Gegensatz zu den erfundenen
Szenario-Prozentzahlen der PDF, die bewusst NICHT übernommen wurden (siehe
Punkt 3). Die PDF-Sachfakten selbst (STAR-Anteil, H1-Zahlen, IPO-Details,
Cornerstone-Investoren) wurden unabhängig gegenrecherchiert und
bestätigt — nur das exakte Lock-up-Ablaufdatum blieb bei allen Quellen
unverifizierbar ("Herbst 2026"/"Mitte-Ende September").

**Status: von Brian angestoßen (2026-08-31, "vielleicht gibts Punkte die
wir für unsere Analyse-System ergänzen, verbessern, modifizieren können")
und direkt umgesetzt** (kein separater Freigabe-Schritt wie bei Abschnitt
12, da es sich um eng auf den konkreten Vincorion-Fall bezogene,
gut abgegrenzte Modul-Ergänzungen statt einer System-weiten Architektur-
Änderung handelt).

