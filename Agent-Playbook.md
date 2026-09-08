# Architektur – Brians Aktien-Agent

Stand: 2026-08-23. Lebendes Dokument, wird mit dem Projekt weiterentwickelt.

## 1. Ziel

Ein Agenten-System, das eigenständig nach Aktien sucht, die zu Brians Depot und Regeln
passen, sie nach seinem eigenen dreiteiligen Regelwerk bewertet, die Bewertung durch
drei KI-Anbieter gegenseitig kontrollieren lässt, und daraus eine Watchlist +
Kauf-/Verkaufsvorschläge erzeugt. Order-Ausführung bleibt manuell bei Brian.
Vorbild (nicht Kopie): Raketentonis Multi-Agenten-Ansatz.

**Nordstern (2026-08-22, Brian):** Der übergeordnete Zweck des Depots ist, den Markt
langfristig zu schlagen. Der Agent soll dafür nicht nur auf Zuruf analysieren, sondern
proaktiv und eigenständig: laufend prüfen, ob/wann ein Kauf (und in welcher Höhe) Sinn
ergibt, oder ob es gerade sinnvoller ist, abzuwarten und Cash zu halten. Das umfasst
auch die regelmäßige Überwachung des bestehenden Depots (nicht nur Kandidaten-Suche),
inkl. Nachrichten-Check und These-Check zu bestehenden Positionen.

**Zweites Grundziel neben "Markt schlagen" (2026-08-29, von Brian ergänzt):**
Genauso wichtig wie die Outperformance ist Brian **Kapitalerhalt und
diszipliniert-emotionsloser Vermögensaufbau** – "Emotion hat an der Börse
bekanntlich nichts verloren" (Brians Formulierung). Das ist kein Widerspruch
zum Nordstern oben, sondern die Leitplanke, WIE dorthin gegangen wird: nicht
über riskante Alles-oder-Nichts-Wetten, sondern über ein diszipliniertes,
regelbasiertes Vorgehen, das Emotionen (Gier bei Rallys, Panik bei
Rücksetzern, Festhalten aus Sturheit) bewusst aus der Entscheidung
heraushält. Praktisch heißt das: die bereits bestehenden Mechanismen – der
3-fach-KI-Cross-Check statt Einzelmeinung, die feste Kategorie-Struktur mit
Kapitalgewichts-Zielen (Abschnitt 3), die Verkaufsdisziplin inkl.
"Hope is not a strategy" bei gebrochener These (siehe "Verkaufsdisziplin &
Gewinnmitnahme-Regeln"), das harte technische Stop-Loss für Talent/Zock-
Positionen, sowie die explizite Cash-Disziplin-Zeile im Wochenfazit ("wenn
nichts klar überzeugt, bleibt das Geld Cash") – sind genau die Werkzeuge,
die dieses zweite Grundziel operationalisieren. Bei jeder künftigen
Prompt-Anpassung (siehe Abschnitt 2, "Spielraum für Prompt-Anpassungen")
und jeder Kauf-/Verkaufsempfehlung ist dieses Prinzip mitzudenken: eine
Empfehlung, die zwar spekulativ attraktiv wirkt, aber Kapitalerhalt/
Disziplin unterläuft (z.B. Nachkaufen in eine fallende Talent-Position ohne
Stop-Loss-Respekt, "auf Erholung hoffen" bei gebrochener These), widerspricht
diesem Grundziel und darf nicht empfohlen werden, selbst wenn die reine
Rendite-Chance verlockend erscheint.

**Drittes Grundziel: langfristig halten heißt nicht für immer halten
(2026-09-08, von Brian ergänzt, nach einem Vergleich mit Raketentonis
System):** gute Unternehmen sollen möglichst lange gehalten werden – das
bleibt der Grundgedanke hinter Kapitalerhalt/diszipliniertem Vermögensaufbau
oben. Aber "langfristig" bedeutet für Brian ausdrücklich NICHT, eine
Position unabhängig von jeder Entwicklung für immer zu behalten. Das ist
keine neue Regel, sondern eine explizite Bestätigung/Verschärfung des
bereits bestehenden Prinzips "Hope is not a strategy" (siehe oben,
"Verkaufsdisziplin & Gewinnmitnahme-Regeln"): eine lange Haltedauer allein
ist NIE ein Grund, eine gebrochene These zu ignorieren oder einen
ausgelösten Abstauber-/Stop-These-Trigger zu übergehen ("wir halten das
schon so lange, jetzt nicht verkaufen" ist kein gültiges Gegenargument).
Gleichzeitig gilt weiterhin unverändert die "Gründliche-These-Prüfung-vor-
Verkaufsempfehlung-Pflicht" (Timing vs. Struktur unterscheiden, Checkpoints
respektieren) – dieses dritte Grundziel hebt diesen Schutz nicht auf,
sondern stellt nur klar, dass am Ende der Prüfung, wenn sich ein echter
struktureller Bruch bestätigt, die reine Haltedauer selbst niemals als
Gegenargument zählt. **Die andere Seite derselben Medaille (Brian, direkt
im Anschluss präzisiert): "es bedeutet, nur dann zu verkaufen, wenn es
einen nachvollziehbaren Grund gibt"** – dieses dritte Grundziel ist
AUSDRÜCKLICH kein Aufruf, schneller oder häufiger zu verkaufen. Genauso wie
lange Haltedauer allein kein Grund zum Halten ist, ist ein roter Tag,
allgemeine Marktnervosität oder Ungeduld allein KEIN nachvollziehbarer
Verkaufsgrund. Ein nachvollziehbarer Grund ist ausschließlich einer der
bereits dokumentierten Abstauber-/Stop-These-Trigger (siehe
"Verkaufsdisziplin & Gewinnmitnahme-Regeln", je Position konkret in
`analysen/*.md` festgehalten) bzw. ein im 3-fach-Cross-Check bestätigter
struktureller Thesenbruch – nichts Vageres. Beide Seiten zusammen: weder
"wir halten das schon so lange" noch "der Kurs ist gerade unangenehm" sind
für sich allein ein gültiges Argument, weder fürs Halten noch fürs
Verkaufen – nur ein konkreter, dokumentierter, nachvollziehbarer Grund
zählt in beide Richtungen.

**Rolle des FTSE-All-World-ETF vs. Aktienanteil (2026-08-29, von Brian
präzisiert):** Der Vanguard-FTSE-All-World-Sparplan ist NICHT der
strategische Kern von "Markt schlagen" – er dient ausdrücklich der
**Altersvorsorge** und läuft als eigener, davon unabhängiger Baustein
parallel (600 €/Monat, siehe "Budget & Cashflow"). Der Nordstern (Markt
schlagen) und das Zweite Grundziel (Kapitalerhalt UND Vermögensaufbau, siehe
oben) beziehen sich konkret auf den **Aktienanteil** (die Einzelwerte-Summe,
ohne ETF) – das ist der Teil, den Brian aktiv über die Champions/Profi/
Talent-Struktur (Abschnitt 3) steuern will. Praktische Konsequenz: das
Kapitalgewichts-Ziel je Kategorie (Abschnitt 3) wird ab jetzt gegen den
Aktienanteil berechnet, nicht gegen das Gesamtportfolio inkl. ETF (siehe
dortige Präzisierung). Die ETF-/Aktien-Verhältnis-Regel (mind. 50%, langfristig
60% ETF) bleibt als separate Kapitalallokations-Entscheidung bestehen – sie
regelt, wie viel überhaupt in den Altersvorsorge-Baustein vs. den aktiv
gesteuerten Aktienanteil fließt, nicht die interne Gewichtung innerhalb des
Aktienanteils selbst.

**Konkretes Rendite-/Vermögensziel (2026-08-30, von Brian beziffert und
mehrfach präzisiert):** Brian möchte eine Rendite von **15-20% p.a.**
erzielen und innerhalb der **nächsten 5-7 Jahre (Zielmarke ca. 2031-2033,
2026-08-30 von Brian bewusst von fest 5 auf 5-7 Jahre ausgeweitet) eine
Spanne von 90.000-100.000€ erreichen – ausdrücklich bezogen NUR auf den
Aktienanteil (Einzelwerte ohne ETF, und konsistent mit der Gold-Regel oben
auch ohne die Gold-ETC-Position), nicht auf das Gesamtportfolio inkl.
ETF-Sparplan.**
**Baseline (30.08.2026):** Aktienanteil = Gesamtportfolio (35.034,17€)
minus ETF (Vanguard FTSE All-World, 7.585,00€) minus Gold-ETC (505,50€) =
**ca. 26.943,67€**. Laufende Sparrate für dieses Ziel: **€320/Monat**
(finanzen.net zero) **plus gelegentliche Nachschüsse (€100-200, unregelmäßig,
siehe "Budget & Cashflow")** – NICHT die €800/Monat Scalable-Rate, die
größtenteils in den ausgeklammerten ETF fließt.

**Renditeziel-Feinjustierung (2026-08-30, von Brian entschieden):** Auf die
Frage, ob das bestehende, bewusst ausbalancierte Regelwerk (Kapitalerhalt
gleichrangig zu "Markt schlagen", siehe Zweites Grundziel oben) überhaupt
auf 15-20% p.a. ausgelegt ist, hat Brian klar entschieden: **das
ausbalancierte Regelwerk bleibt bestehen, wird NICHT über Bord geworfen**
– stattdessen wird an ein paar Stellschrauben moderat gedreht, um eine
**zweistellige Rendite (ca. 10-15% p.a., nicht mehr zwingend volle
15-20%)** zu erreichen, kombiniert mit dem ausgeweiteten 5-7-Jahres-Fenster.
Konkrete, bewusst MODERATE Anpassungen (keine der bestehenden harten
Leitplanken wird aufgehoben):
1. **Kapitalgewichts-Ziel leicht Richtung Talent verschoben:** Champions
   40-50% → **35-45%**, Talent von reiner Restgröße auf einen bewusst
   höher angesetzten Zielkorridor **25-40%** (Profi unverändert 20-30%,
   siehe Abschnitt 3).
2. **Positionsgrößen-Limit-Ausnahme für Top-Konviktion:** bei einer
   Position mit außergewöhnlich hoher Rating-Konfidenz (TMR/Scout) darf das
   sonst harte 10%-Limit auf **bis zu 12%** ausgedehnt werden – weiterhin
   eine echte Ausnahme, kein neues Standard-Limit.
   **Ergänzung: Trailing-Weight-/Winner-Drift-Regel (2026-08-30, aus der
   Cross-KI-Diskussion in Agent-Playbook-Archiv-Diskussionen.md Abschnitt 10, von Brian freigegeben).** Die 12%
   bleiben die Grenze für AKTIVES Nachkaufen (Kapital, das bewusst in eine
   Position hineinallokiert wird) – das ändert sich nicht. Wächst eine
   Position dagegen rein PASSIV durch Kursanstieg über dieses Gewicht
   hinaus, gilt eine gestufte Logik statt eines automatischen
   Zwangs-Verkaufs: bis **15%** normal toleriert (kein Eingriff), **15-18%**
   löst eine verpflichtende Agent-Review aus (These noch intakt? Bewertung
   stark entkoppelt? weiterhin Top-3-/Top-5-Kapitalallokation im Depot?
   gestiegenes Risiko eines permanenten Kapitalverlusts? würden wir diese
   Position heute neu mit diesem Gewicht eröffnen? – überwiegend positiv
   beantwortet: halten, sonst Teilgewinnmitnahme), über **18%** zwingendes
   Rebalancing zurück Richtung Zielgewicht (harter Cap, keine Ausnahme).
   **Wichtige Einschränkung:** der Drift-Spielraum gilt NUR für
   Qualitätsgewinner, deren Kursanstieg auf echter fundamentaler
   Verbesserung (FCF/EPS/ROIC/Marktposition) beruht – nicht für Kursgewinne,
   die primär auf Multiple-Expansion/Momentum beruhen ("Kursanstieg allein
   ist keine Erlaubnis zur Konzentration"). Damit werden echte Compounder
   nicht mehr automatisch beschnitten, ohne dass aus der Ausnahme ein
   Freibrief für unbegrenztes Anwachsen wird.
3. **Sektor-Zielband Technologie leicht angehoben:** 30-35% → **30-38%**
   (Ziel-Band, keine harte Grenze) – verhindert zu frühes Zwangs-
   Diversifizieren weg von einem gerade starken Thema. Die harte
   60%-Obergrenze bei USA/Nordamerika (Region) bleibt UNVERÄNDERT eine
   echte rote Linie, ebenso alle anderen bisherigen Ziel-Bandbreiten.
4. **Etwas mehr Spielraum bei Stop-Loss-Niveaus für Talent/Zock-Positionen
   mit Tag "Zock/Trade"** (siehe "Verkaufsdisziplin & Gewinnmitnahme-
   Regeln"): das technische Stop-Loss-Niveau wird beim nächsten TA-Modul-
   Update mit etwas größerem Abstand vom Einstieg/Hoch gesetzt, damit
   normale Volatilität nicht vorschnell zum Verkauf eines eigentlich
   intakten Gewinners führt. Bleibt ein Sicherheitsnetz gegen Totalschaden,
   wird nur nicht mehr so eng gezogen.

**Realitäts-Check (2026-08-30, Modellrechnung, NUR feste €320/Monat ohne
Nachschüsse):**
- 5 Jahre bei 15% p.a. → ca. **80.000€** (unter der 90.000€-Untergrenze)
- 5 Jahre bei 20% p.a. → ca. **95.500-96.000€** (innerhalb der Spanne)
- **7 Jahre bei 10% p.a.** → ca. **89.000€** (knapp unter der Untergrenze)
- **7 Jahre bei 11% p.a.** → ca. **93.500€** (komfortabel innerhalb der Spanne)
- **7 Jahre bei 12% p.a.** → ca. **98.300€** (nah an der Obergrenze)
Mit dem ausgeweiteten 5-7-Jahres-Fenster reicht also bereits eine
**"normale" zweistellige Rendite von ca. 11-12% p.a.** – deutlich näher am
langfristigen Marktdurchschnitt (Nasdaq 100 ca. 13-17% über 20-25 Jahre,
S&P 500 ca. 10-11% über 20-30 Jahre) als die ursprünglich genannten
15-20% – um die 90.000-100.000€-Spanne allein mit der Basis-Sparrate von
€320/Monat zu erreichen, ganz ohne die "gelegentlichen Nachschüsse"
einzurechnen. Genau das macht die Kombination aus "ausbalanciertes
Regelwerk beibehalten" + "moderate Stellschrauben" + "5-7 statt 5 Jahre"
in sich stimmig, ohne dass dafür hohe Konzentration/Risiko nötig wäre.
Brian nimmt laut eigener Aussage ausdrücklich in Kauf, dass einzelne Jahre
schlechter laufen ("das ist absolut normal") – das Ziel ist als
**Durchschnitt über den gesamten 5-7-Jahres-Zeitraum** zu verstehen, nicht
als Jahres-für-Jahr-Mindestanforderung.
**Portfolio-Level Expected-Return-Szenario (2026-08-30, aus der Cross-KI-
Gesamt-Review in Agent-Playbook-Archiv-Diskussionen.md Abschnitt 12, von Brian freigegeben):** Der Realitäts-Check
oben rechnet mit einer einzelnen angenommenen CAGR. Damit Brian nicht erst
am Ende des 5-7-Jahres-Fensters merkt, ob er auf Kurs ist, sondern laufend
eine ehrliche Bandbreite sieht, führt der Agent zusätzlich ein einfaches
**Bear/Base/Bull-Szenario für den GESAMTEN Aktienanteil** (nicht für
Einzelpositionen – das ist die Ebene der TMR-Fair-Value-Bandbreiten, siehe
"Gewinnmitnahme-Zielzonen"). Es dient als reiner Plausibilitäts-Check gegen
das 90.000-100.000€-Ziel, nicht als neue Steuerungsgröße:
- **Bear (ca. 4-6% p.a.):** ein länger anhaltender schwacher/seitwärts
  laufender Markt bzw. ein bis zwei größere Drawdown-Phasen im
  Betrachtungszeitraum, ohne dass die Kern-Positionen fundamental brechen.
- **Base (aktuell ca. 10-12% p.a.):** entspricht der in "Konkretes
  Rendite-/Vermögensziel" hergeleiteten, für das 7-Jahres-Hauptziel als
  realistisch eingestuften Zielspanne.
- **Bull (ca. 15-18% p.a.):** ein überdurchschnittlich starkes Marktumfeld
  und/oder mehrere Talent-Positionen, die überproportional aufgehen.
Für jedes Szenario wird der resultierende Aktienanteil-Endwert nach 5 und
nach 7 Jahren ausgewiesen (gleiche Formel wie im Realitäts-Check: aktueller
Stand + laufende Sparrate, ohne unregelmäßige Nachschüsse). **Update-
Rhythmus:** einmal berechnet als Baseline (siehe unten), danach im
Monatsrecap aktualisiert (neuer Ist-Stand als Startwert) sowie zusätzlich
sofort neu bewertet, wenn sich der Marktregime-Status (siehe oben) auf
Risk-off/Stress ändert oder ein Jahr vergangen ist – nicht bei jedem
Wochenfazit, um das Format nicht zu überladen. Zweck ist ausdrücklich
Erwartungssteuerung, nicht Handlungsauslöser: das Szenario selbst löst
keine Kauf-/Verkaufsentscheidung aus, es zeigt Brian nur transparent, in
welchem Korridor er sich gerade bewegt und ob das Bear-Szenario immer noch
in der Nähe der 90.000€-Untergrenze liegt oder deutlich darunter fällt
(Letzteres wäre ein Signal, die Erwartungshaltung oder die Sparrate zu
überdenken – siehe Fazit der Gesamt-Review in Agent-Playbook-Archiv-Diskussionen.md Abschnitt 12).

**Ziel ist eine Untergrenze, keine Obergrenze (2026-08-30, von Brian
klargestellt: "wenn das angegebene Ziel schneller erreicht wird, umso
besser"):** 90.000-100.000€ in 5-7 Jahren ist der akzeptierte Mindest-
Anspruch, keine Kappung. Wird das Ziel schneller oder deutlicher übertroffen
(z.B. durch eine besonders starke Marktphase oder gut aufgehende Talent-
Positionen), ist das ausdrücklich erwünscht – es gibt keinen Grund, bei
Zielerreichung Gewinne "künstlich" zu bremsen oder das Risiko-Dial wieder
zurückzudrehen, nur weil die Zielmarke erreicht ist. Die bestehende
Verkaufsdisziplin (Gewinnmitnahme bei überzogener Bewertung, siehe
"Verkaufsdisziplin & Gewinnmitnahme-Regeln") bleibt davon unberührt – die
gilt weiter nach ihren eigenen fundamentalen/technischen Kriterien, nicht
weil ein Vermögensziel erreicht wurde.

**Phasenübergang nach Zielerreichung (2026-08-30, von Brian festgelegt):**
Zu unterscheiden von "nicht künstlich bremsen, solange das Ziel noch nicht
erreicht ist" (siehe oben) ist die Frage, was NACH einer durable erreichten
90.000-100.000€-Marke gilt: Sobald das Ziel erreicht ist, kehrt der Agent
zur **Grundeinstellung des ausbalancierten Regelwerks zurück** – die vier
moderaten Stellschrauben aus der "Renditeziel-Feinjustierung" oben
(Kapitalgewicht Champions 35-45%/Talent 25-40%, 12%-Positions-Ausnahme,
Technologie-Band 30-38%, weiteres Stop-Loss-Niveau) werden dann wieder auf
die ursprünglichen, konservativeren Werte zurückgesetzt (Champions 40-50%/
Talent Rest, hartes 10%-Limit ohne Ausnahme, Technologie-Band 30-35%,
engeres Stop-Loss). Das Grundziel bleibt aber bestehen – weiterhin
diszipliniert-emotionsloses, risikokontrolliertes Wachstum, das über die
Jahre versucht, den Markt zu schlagen (siehe Nordstern oben), nur eben ohne
die zusätzliche Rendite-Dringlichkeit der Aufbauphase. "Durable erreicht"
heißt dabei: ein nachhaltiger Stand über der 90.000€-Marke, nicht ein
einzelner Tages-/Wochen-Ausreißer nach oben – der Agent soll das im
Wochenfazit/Monatsrecap explizit als Meilenstein melden und die
Umstellung transparent ankündigen, nicht stillschweigend vollziehen.

**Dynamische Regelwerk-Anpassung nach Marktregime (2026-08-30, von Brian
delegiert: "systematisch und automatisiert das Regelwerk anpassen, je nach
Marktstimmung/Momentum, ohne Rückabsprache, aber mit kurzer Mitteilung
warum und was ich mir davon verspreche"):** Der Agent darf die weichen
Stellschrauben aus der "Renditeziel-Feinjustierung" eigenständig je nach
Marktregime verschieben, ohne vorher Brians Zustimmung einzuholen. Damit
das systematisch bleibt und nicht selbst zur emotionalen Reaktion auf
Marktrauschen wird (genau das soll das Regelwerk ja verhindern), läuft das
über klar definierte Regime-Zustände statt freiem Bauchgefühl:

1. **Signal-Basis (beobachtbar, nicht subjektiv):** Trend der Leitindizes
   (S&P 500/Nasdaq 100 ggü. 50-/200-Tage-Linie), Volatilitätsniveau (VIX
   bzw. vergleichbares Maß, sobald über Twelve Data verfügbar), Tiefe eines
   laufenden Drawdowns vom letzten Hoch, Marktbreite (Anteil Index-
   Mitglieder über der 200-Tage-Linie, falls verfügbar), sowie die Anzahl
   aktuell überzeugender KAUFEN-Signale aus dem eigenen Kandidaten-Scan
   (viele überzeugende Kandidaten = eher Risk-on-Signal, wenige = eher
   Risk-off).
2. **Drei Regime-Zustände mit je eigenem Parameter-Satz:**
   - **Risk-on/Momentum-stark** (Indizes über 200-Tage-Linie, geringe
     Volatilität, viele überzeugende KAUFEN-Kandidaten): Stellschrauben an
     oder nahe dem oberen Ende der in der Renditeziel-Feinjustierung
     definierten Spannen (z.B. Talent Richtung 40%, Technologie-Band
     Richtung 38%, 12%-Positions-Ausnahme aktiv nutzen).
   - **Neutral** (Standardfall): Stellschrauben in der Mitte der
     definierten Spannen – das ist der in der Feinjustierung oben
     beschriebene Ausgangszustand.
   - **Risk-off/Stress** (Indizes unter 200-Tage-Linie, erhöhte Volatilität,
     spürbarer Drawdown, wenige überzeugende Kandidaten): Stellschrauben
     Richtung der konservativeren Grundeinstellung zurückgefahren (näher an
     Champions 40-50%/Talent-Rest, 10%-Limit ohne Ausnahme, engeres
     Technologie-Band, engerer Stop-Loss) – zusätzlich verstärkte
     Cash-Disziplin ("wenn nichts überzeugt, bleibt Geld Cash").
   **Regime-basierte Bewertungsdisziplin statt Markt-Timing (2026-08-30, aus
   der Cross-KI-Diskussion in Agent-Playbook-Archiv-Diskussionen.md Abschnitt 10, von Brian freigegeben):** Das
   Regime steuert nicht nur die obigen Kapitalgewichts-Dials, sondern auch
   die Sicherheitsmarge bei NEUKÄUFEN – Risk-off heißt ausdrücklich NICHT
   "verkaufen", sondern eine höhere Margin of Safety verlangen: Risk-on =
   normale Bewertungsanforderung, Neutral = leicht erhöht, Risk-off =
   deutlich höhere Sicherheitsmarge, keine schwachen Setups mehr kaufen,
   mehr Kapital für außergewöhnliche Dislocations reserviert. Das Regime
   wird damit nicht zum Verkaufs-Trigger, sondern zum "Preis für Geduld" –
   es versucht nicht, den Markt vorherzusagen, sondern bestimmt nur, wie
   überzeugend ein neuer Kauf sein muss, um das Kapital zu verdienen.
3. **Trägheit gegen Flip-Flopping:** Ein Regimewechsel wird nur bei einem
   klaren, mehrtägig bis mehrwöchig bestätigten Signal vollzogen, nicht bei
   einzelnen Tagesausschlägen – sonst würde das System selbst prozyklisch
   hin- und herspringen, was dem Kapitalerhalt-Grundziel widerspricht.
4. **Unantastbar bleiben, auch im Risk-on-Regime:** alle bisherigen
   HARTEN Grenzen – die 60%-Hartgrenze USA/Nordamerika, das absolute
   Positions-Maximum (auch die 12%-Ausnahme bleibt eine Ausnahme, kein
   Freibrief für 20%+), der ETF-Mindestanteil von 50%, die Order-
   Ausführungs-Grenze (Abschnitt 1), sowie die Prozess-Pflichten selbst
   (3-fach-Check, Identity-Gate, Head-to-Head-Ersatz-Gate) – angepasst
   werden nur die NUMERISCHEN Zielwerte innerhalb dieser Prozesse, nicht
   die Prozesse oder Hartgrenzen selbst.
5. **Mitteilungspflicht (nicht verhandelbar, siehe Brians Formulierung):**
   Jede Regime-basierte Anpassung wird Brian zeitnah mitgeteilt (im
   Wochenfazit oder, bei einer deutlichen/eiligen Umstellung, proaktiv wie
   bei einer Eskalation) – IMMER mit: (a) welches Signal/welche Signale den
   Wechsel ausgelöst haben, (b) was konkret geändert wurde, (c) was sich
   der Agent davon für die nächste Zeit verspricht. Keine stillschweigenden
   Anpassungen im Hintergrund.
Dieser Mechanismus wird erstmals beim nächsten Wochenfazit/Trigger-Lauf
aktiv geprüft (aktuelle Regime-Einschätzung erstmalig bestimmen und
mitteilen) und danach laufend fortgeführt.

**Drawdown-Psychologie-Protokoll (2026-08-30, aus der Cross-KI-Gesamt-Review
in Agent-Playbook-Archiv-Diskussionen.md Abschnitt 12, von Brian freigegeben; Jacks Punkt: "in der Theorie sagen
wir 'Trockenpulver einsetzen', in der Praxis schlägt die Psychologie zu").**
Ergänzt das Regime-System oben um ein konkretes Verhaltens-Protokoll für den
Moment, in dem es wirklich wehtut – nicht nur eine numerische
Stellschrauben-Anpassung, sondern eine feste Kommunikations- und
Verhaltensroutine, damit Emotionen (Panik, "diesmal ist es anders", Wunsch
alles zu verkaufen) nicht die Systematik überschreiben (siehe Zweites
Grundziel, Abschnitt 1):
1. **Auslöser:** Regimewechsel zu Risk-off/Stress (siehe oben) UND/ODER ein
   Drawdown des Aktienanteils von mehr als **-20% vom letzten Hoch**
   (unabhängig vom formalen Regime-Status, da ein depot-spezifischer
   Einbruch auch ohne breiten Marktcrash auftreten kann).
2. **Sofort-Mitteilung statt Abwarten:** Der Agent meldet sich proaktiv
   (nicht erst im nächsten regulären Wochenfazit) mit einer festen,
   knappen Struktur: (a) wie tief der Drawdown ist und seit wann, (b) ob
   die K-Kriterien/Kernthesen der größten Positionen nach aktuellem
   [B] THESE-CHECK-Stand intakt sind oder nicht, (c) die
   Erinnerung, dass ein Kursrückgang allein nach dem bestehenden Regelwerk
   KEIN Verkaufsgrund ist (siehe "Verkaufsdisziplin & Gewinnmitnahme-
   Regeln", Kategorie 5 gilt nur bei gebrochener These, nicht bei
   gefallenem Kurs), (d) die konkrete Handlungsoption laut Sparplan-Regel:
   Sparrate wie vorgesehen halten oder (Brians eigene Formulierung, siehe
   Abschnitt 1) dynamisch erhöhen, statt zu pausieren.
3. **Keine Entscheidung "aus dem Bauch heraus" in diesem Fenster:** Jede
   Verkaufsempfehlung, die WÄHREND eines aktiven Risk-off/Stress- bzw.
   -20%-Drawdown-Fensters entsteht, muss ausdrücklich denselben
   vollständigen [B] THESE-CHECK-Prozess durchlaufen wie in ruhigen
   Marktphasen (keine verkürzte Prüfung "weil sowieso schon alles fällt") –
   das gilt in beide Richtungen: weder vorschnelles Verkaufen aus Angst
   noch vorschnelles "Vollgas nachkaufen" ohne die übliche
   Sicherheitsmarge-Prüfung (siehe "Regime-basierte Bewertungsdisziplin"
   oben).
4. **Ende des Protokolls:** Sobald das Regime wieder auf Neutral oder
   besser zurückstuft UND der Drawdown auf unter -10% vom letzten Hoch
   zurückgegangen ist, kehrt die normale Kommunikationsfrequenz (Wochenfazit)
   zurück – mit einer kurzen Rückschau, wie sich die Positionen durch die
   Phase geschlagen haben.
Zweck: nicht neue Analyse, sondern ein vorab vereinbartes Skript für den
psychologisch schwierigsten Moment, damit die Reaktion in der Krise nicht
neu erfunden werden muss, sondern bereits feststeht.

**Erste konkrete Beobachtung, noch vor dem ersten formalen Regime-Check
(2026-08-30, von Brian eingebracht, per WebSearch bestätigt):** Brian weist
auf ein spürbares Nachlassen des KI-/Tech-Momentums hin – selbst sehr
starke Fundamentaldaten lösen keine großen Kurssprünge mehr aus, Rallys
werden schnell wieder verkauft. Bestätigt durch Nvidias Q2-2026-Zahlen vom
26.08.2026 (Umsatz 96,22 Mrd.$ vs. Konsens 92,2 Mrd.$, +106% YoY, EPS über
Erwartung) – die Aktie fiel trotzdem leicht nachbörslich ("priced for
perfection", Optionsmarkt hatte bereits ~5% Bewegung eingepreist, fehlendes
"drop-the-mic"-Moment nach vorheriger starker Rally). Zusätzlich gab es
bereits im Juli 2026 einen breiteren Tech-/KI-Ausverkauf (u.a. nach
enttäuschenden TSMC-/Netflix-Zahlen), mit Analysten-Warnungen vor einem
Zeit-Mismatch zwischen KI-Investitionen und tatsächlicher Monetarisierung
("Overbuild"-/Bubble-Sorge). **Praktische Einordnung:** das liest sich eher
als eine **Ermüdung speziell im engen KI-/Momentum-Segment** (Sektor-
spezifisch), nicht zwingend als breiter Risk-off der Gesamtmärkte – deckt
sich mit dem eigenen Kursverlaufs-Screening vom 2026-08-30 (CrowdStrike,
Fortinet, ASML, Keyence bereits stark gelaufen/überhitzt, während weniger
gehypte Werte wie Hoya/Disco Corp/Lasertec echte Rücksetzer zeigten).
Konsequenz für die Stellschrauben: das Technologie-Zielband (30-38%) eher
Richtung Mitte statt oberes Ende fahren, und bei stark gelaufenen KI-/
Momentum-Titeln (Talent/Zock-Tag) besonders auf das Stop-Loss-Sicherheitsnetz
achten statt auf weitere Kurssprünge zu setzen.

**Erster formaler Regime-Check (2026-08-30, komplettes Signalbild, per
WebSearch/WebFetch ermittelt):**

1. **Index-Trend:** S&P 500 bei 7.711,76 Punkten, über der 50-Tage-Linie
   (7.686,30) und über der 200-Tage-Linie (7.632,00) – mittel-/langfristig
   bullish (Wochen-/Monats-Signal "Strong Buy"), Tagessignal aber nur
   "Neutral", RSI bei 51,5 (neutral, keine Überhitzung). → für sich genommen
   ein Risk-on-Signal, aber ohne klare kurzfristige Dynamik.
2. **Volatilität:** VIX bei 14,51 – unteres Drittel der 10-Jahres-Spanne,
   deutlich unter dem 10-Jahres-Durchschnitt von 19,72. → klares
   Risk-on-Signal (niedrige Angst/Absicherungsnachfrage), mit der
   Einschränkung, dass ungewöhnlich niedrige Vola auch Sorglosigkeit/
   Kompression vor einem plötzlichen Ausbruch bedeuten kann.
3. **Marktbreite:** 70%+ der S&P-500-Werte über der 200-Tage-Linie (gesund),
   aber nur noch 54% über der 50-Tage-Linie (vor kurzem noch 70%),
   McClellan-Oszillator seit Mitte August im negativen Bereich trotz Index
   nahe Hoch, neue 52-Wochen-Hochs von normal 10-12% auf nur noch 1-4%
   eingebrochen. → deutliches Warnsignal ("Bull-Fatigue"): die Rally trägt
   sich zunehmend auf weniger Schultern, kurzfristig eher Risk-off-Tendenz
   trotz gesundem langfristigen Bild.
4. **Drawdown:** aktuell keiner (Indizes nahe Jahreshoch, über beiden
   Linien) – kein Risk-off-Signal.
5. **Eigener Kandidaten-Scan:** das Kursverlaufs-Screening vom 2026-08-30
   fand vergleichsweise wenige überzeugende, noch nicht "überhitzte"
   Kaufkandidaten (v.a. bei KI-/Momentum-Titeln); depot-relevante Chancen
   (Hoya, Disco Corp) laut Brian "noch nicht genug korrigiert". → eher
   neutral bis leicht zurückhaltend, kein klares Risk-on-Übergewicht an
   Kandidaten.

**Einstufung: Neutral (mit leichtem Vorsicht-Bias)** – nicht Risk-on, obwohl
Index-Trend und Volatilität isoliert dafür sprächen. Begründung: die
Marktbreite zeigt eine klare Verschlechterung (weniger Mitglieder tragen die
Rally, negativer McClellan, kollabierte Anzahl neuer Hochs) und deckt sich
mit Brians eigener Beobachtung der KI-/Momentum-Ermüdung – das ist ein
echtes, mehrtägig bestätigtes Warnsignal, kein einzelner Tagesausschlag.
Gleichzeitig gibt es keinen Drawdown und keine Stress-Signale (VIX niedrig,
Indizes über beiden Gleitenden), weshalb eine Einstufung als Risk-off/Stress
ebenfalls nicht gerechtfertigt ist.

**Tie-Breaker-Prinzip (ab jetzt gültig für alle künftigen Regime-Checks):**
Wenn sich die Signale widersprechen (hier: bullisher Trend + niedrige Vola
vs. schwache Breite/Momentum-Ermüdung), wird IMMER konservativ eingestuft –
im Zweifel Neutral statt Risk-on, im Zweifel Risk-off statt Neutral. Nie zur
optimistischeren Einstufung aufrunden, nur weil einzelne Signale das
hergeben – das würde dem Kapitalerhalt-Grundziel widersprechen.

**Konkrete Konsequenz für die Stellschrauben:** Da Neutral dem in der
Feinjustierung beschriebenen Ausgangszustand entspricht, bleiben die
Stellschrauben in der Mitte der definierten Spannen (Champions ~40%, Talent
~32%, Technologie-Band ~33-34%, Standard-Stop-Loss) – aktuell also keine
Verschiebung Richtung Risk-on-Ende. Passend zur Marktbreite-Warnung bleibt
die bereits notierte Vorsicht bei stark gelaufenen KI-/Momentum-Titeln
(Technologie-Band eher Richtung Mitte, engmaschiges Stop-Loss-Monitoring) in
Kraft und wird durch dieses Ergebnis zusätzlich bestätigt.

Wird beim nächsten Wochenfazit-Lauf erneut geprüft (Trägheitsregel: nur bei
mehrtägig/mehrwöchig bestätigtem neuen Signal wird die Einstufung
geändert).
Fortschritts-Tracking gegen dieses Ziel läuft über
`depot/performance_tracking.md` (Depot-GESAMT vs. Indizes, bestehender
Mechanismus) UND sollte zusätzlich separat die CAGR des reinen
Aktienanteils (ohne ETF/Gold) gegen die 10-15%-Zielspanne und die
90.000-100.000€-Marke zeigen, sobald genug Historie vorliegt (nicht
sinnvoll auf Wochen-/Monatsbasis, eher ab 1 Jahr Historie aufwärts) –
dafür wird eine eigene, vom Gesamt-Tracking getrennte Kennzahl gebraucht
(noch zu bauen, siehe Offene Punkte).

**Grenze bleibt fix (2026-08-22, nochmal explizit bestätigt):** Echte Order-Ausführung
durch den Agenten ist ohnehin nicht vorgesehen (Broker-AGB lassen das nicht zu) und
auch nicht das Ziel — der Agent trifft/empfiehlt die Entscheidung (Kaufen/Warten/Cash
halten, Höhe) proaktiv und meldet sich von sich aus bei Brian; die eigentliche
Order führt Brian wie gehabt manuell selbst aus. Das gilt dauerhaft, nicht nur als
Übergangslösung.

**Vertrauens-Delegation durch Brian (2026-08-30, explizit erklärt):** Brian hat
erklärt, dass er Kauf-/Verkaufs-Anweisungen des Agenten künftig grundsätzlich
1:1 ausführen will ("wenn du sagst kauf/verkauf, mach ich es") und Rückfragen
nur noch stellt, wenn ihn etwas konkret stutzig macht. Das ändert NICHTS an
den bestehenden Grenzen und Prozessen, im Gegenteil – es macht sie wichtiger:
1. Die Order-Ausführungs-Grenze bleibt exakt wie oben (Order-Submit-Tools
   werden nie vom Agenten aufgerufen, auch nicht bei ausdrücklicher
   Aufforderung).
2. Der Agent ist kein zugelassener Anlageberater – jede Kauf-/
   Verkaufsempfehlung bleibt eine regelbasierte Einschätzung nach Brians
   eigenem Regelwerk, keine Finanzberatung im rechtlichen Sinn. Brian bleibt
   der eigentliche Entscheider; der Agent liefert die Entscheidungsgrundlage
   so klar und handlungsfähig wie möglich (konkreter Kurs, Stückzahl/Betrag,
   Kategorie), aber IMMER mit der Begründung dazu – nie als reine
   Anweisung ohne nachvollziehbares "Warum", genau damit Brian im Bilde
   bleibt, auch wenn er standardmäßig zustimmt.
3. Gerade WEIL Brian standardmäßig folgt, gelten die bestehenden
   Sicherheitsmechanismen (3-fach-Check, Head-to-Head-Ersatz-Gate, Sektor-/
   Regionen-Vorab-Check, Stop-Loss-/Verkaufsdisziplin, Cash-Disziplin bei
   fehlender Überzeugung) ab jetzt umso strikter – keine Empfehlung ohne
   vollständig durchlaufenen Prozess, kein Abkürzen, "weil Brian eh zustimmt".
4. Brians eigener Impuls, bei Stutzigkeit nachzufragen, bleibt ausdrücklich
   erwünscht – der Agent hebt selbst hervor, wenn eine Empfehlung ungewöhnlich
   groß, riskant oder von der bisherigen Linie abweichend ist, statt das
   Brian allein überlassen.

**Informations-Vorrang-Hierarchie bei Widersprüchen (2026-09-04, von
Raketentonis "55555-Portfolio-System" übernommen und an unser System
angepasst – Brian: "wichtig finde ich die restlichen 3 Punkte wo sein
System voraus ist, darauf will ich jetzt aufbauen").** Raketentoni trennt
in seinem System explizit ein "Masterbook" (Strategie/Regeln) von einem
"Master-Status" (aktueller operativer Stand) und löst Widersprüche
zwischen beiden nach einer festen Reihenfolge auf – genau das übernehmen
wir, weil diese Session mehrfach gezeigt hat, dass veraltete Aussagen
(z.B. in `HANDOVER.md`) sonst stillschweigend wieder als aktuell behandelt
werden. Ab jetzt gilt bei WIDERSPRÜCHLICHEN Informationen zwischen
verschiedenen Quellen diese Rangfolge (höchste zuerst, IMMER die höchste
zutreffende Stufe gewinnt):
1. **Jüngste explizit bestätigte Entscheidung/Transaktion** – eine
   tatsächlich erkannte Transaktion (z.B. via `list_portfolio_transactions`)
   oder eine explizite Aussage/Bestätigung von Brian im aktuellen Chat.
   Schlägt IMMER alles andere, auch eine scheinbar aktuelle Datei.
2. **`depot/master_status.md`** (neu angelegt, siehe unten) – das
   konsolidierte, laufend aktualisierte Status-Dashboard (Kategorie-Zählungen,
   offene Prüfpunkte, offene Empfehlungen, offene Lücken-Suchen). Bei einem
   Widerspruch zwischen dieser Datei und einer der Detail-Dateien unten gilt
   diese Datei als der aktuellere Stand – ABER: für die vollständige
   Begründung/Historie einer einzelnen Position bleiben die Detail-Dateien
   (`depot/kategorisierung.md`, `watchlist.md` etc.) maßgeblich, dieser Status
   ersetzt sie nicht, er aggregiert nur die Kernzahlen.
3. **`Agent-Playbook.md`** (dieses Dokument, das "Masterbook") – das
   verbindliche Regelwerk selbst.
4. **Ältere Aussagen/Analysen** (`analysen/*.md`, ältere Chat-Historie,
   `HANDOVER.md`) – Kontext und Begründungshistorie, aber im Zweifel NICHT
   der aktuelle Stand, wenn eine der drei Stufen oben etwas anderes sagt.
   Genau dieser Fall trat mehrfach auf (siehe `HANDOVER.md`-Korrekturen
   2026-09-04) – künftig explizit gegen diese Rangfolge prüfen, statt eine
   ältere Datei unreflektiert als aktuell zu behandeln.

**Regel-Aufnahme-Disziplin / Ruleset-Hygiene (2026-09-04, ebenfalls von
Raketentoni übernommen: "nicht jede einzelne schlechte Erfahrung erzeugt
sofort eine neue pauschale Regel").** Ehrlicher Befund aus dieser Session:
allein am 2026-09-04 kamen mehrere neue, teils lange Regeln dazu (Gründliche-
These-Prüfung, Portfolio-Lücken-Kandidatensuche, Tieferer-Zweck-der-Suche) –
jede einzelne war berechtigt und von Brian angefordert, aber die Summe
zeigt ein reales Risiko: das Regelwerk kann durch lauter Einzelfall-Reaktionen
unübersichtlich wachsen, statt sauber zu bleiben. Ab jetzt gilt:
1. **Vor jeder neuen dauerhaften Regel** (ob von Brian gefordert oder vom
   Agenten vorgeschlagen) kurz prüfen: deckt eine BESTEHENDE Regel das
   Problem bereits ab und muss nur präzisiert/erweitert werden (siehe z.B.
   die Präzisierung "ganze Indizes durchforsten" heute – Erweiterung einer
   bestehenden Regel, keine neue), oder ist es wirklich ein neuer,
   eigenständiger Fall? Im Zweifel erweitern statt duplizieren.
2. **Einzelfall vs. Muster explizit benennen:** bei einer neu vorgeschlagenen
   Regel kurz sagen, ob dies der ERSTE Vorfall dieser Art ist (dann evtl.
   erstmal als Beobachtungspunkt/Notiz statt sofort als bindende Regel
   vorschlagen) oder ob sich das bereits wiederholt hat (dann ist eine feste
   Regel gerechtfertigt). Diese Einschätzung gehört explizit in den
   Änderungsvermerk der neuen Regel, nicht nur die Regel selbst.
3. **Ruleset-Hygiene beim monatlichen Recap (siehe `monatsrecap`-Task):**
   einmal im Monat kurz prüfen, ob mehrere kleinere, im Monatsverlauf
   entstandene Regeln zu einer saubereren, generalisierten Regel
   zusammengefasst werden könnten, oder ob eine Regel durch eine neuere
   bereits überholt ist und archiviert (nicht gelöscht – siehe
   Änderungsprotokoll-Prinzip) werden sollte, statt beide nebeneinander
   stehen zu lassen.
4. **Kein Freibrief gegen berechtigte neue Regeln:** diese Disziplin soll
   Wildwuchs verhindern, nicht dazu führen, dass echte, von Brian explizit
   geforderte Regeln verzögert oder abgelehnt werden – im Zweifel wird die
   Regel trotzdem angelegt, aber mit der ehrlichen Einordnung aus Punkt 2.
5. **Kein spontanes Regelbiegen für einen gerade gewünschten Kauf
   (2026-09-08, ebenfalls von Raketentoni übernommen: "Regeln dürfen
   weiterentwickelt werden, aber nicht spontan, um einen gerade gewünschten
   Kauf passend zu machen"):** eine Regeländerung (egal ob Schwellenwert,
   Kategorisierungs-Kriterium, Gate-Bedingung) darf NIE in unmittelbarem
   zeitlichem/inhaltlichem Zusammenhang mit einem konkreten, bereits
   ins Auge gefassten Kaufkandidaten motiviert oder begründet werden – das
   wäre die Regel der Entscheidung anzupassen, statt die Entscheidung an
   der Regel zu messen. Eine echte Regeländerung braucht eine von der
   aktuellen Kaufentscheidung UNABHÄNGIGE Begründung (z.B. ein
   systematischer Fehler, der bei mehreren, unterschiedlichen Fällen
   auffiel – siehe Punkt 2 oben, "Muster statt Einzelfall"). Erkennungs-
   Frage vor jeder Regeländerung: "Würde ich diese Änderung genauso
   vorschlagen, wenn gerade KEIN konkreter Kandidat davon profitieren
   würde?" – bei "nein" oder Unsicherheit: Änderung zurückstellen, mit
   Brian offen ansprechen statt sie einfach umzusetzen.

**Konsolidierter Master-Status (2026-09-04, dritter von Raketentoni
übernommener Punkt):** neue Datei `depot/master_status.md` – EIN
konsolidiertes Status-Dashboard (Kategorie-Zählungen Depot+Watchlist, offene
Prüfpunkte/Checkpoints, offene Empfehlungen, offene Portfolio-Regel-
Verstöße, offene gezielte Kandidatensuchen, letzte Scheduled-Task-Läufe)
statt den aktuellen Stand aus 6+ verstreuten Dateien selbst
zusammensuchen zu müssen. Wird am Ende jedes `taeglicher-trigger-check`-
und `wochenfazit`-Laufs aktualisiert (siehe jeweilige SKILL.md). Ersetzt
NICHT die Detail-Dateien (siehe Vorrang-Hierarchie oben, Stufe 2) – reine
Aggregation der Kernzahlen für den schnellen Überblick, v.a. beim Einstieg
in einen neuen Chat/Task-Lauf ohne Erinnerung an vorherige Sessions.
**Erweitert (2026-09-07):** enthält jetzt zusätzlich zwei kompakte, aus
dieser Datei bzw. `watchlist.md` destillierte Abschnitte – die
Kategorisierungs-Kriterien (Champions/Profi/Talent + Bucket-A/B/C/D-Logik,
knapp zusammengefasst statt der vollen Herleitung hier) und eine
Watchlist-Kompaktübersicht (eine Tabellenzeile je der 30 Watchlist-Werte:
Kategorie, CRV-Ampel, Kurzthese) – NICHT die vollständigen Dateien
`Agent-Playbook.md`/`watchlist.md` selbst, um das Kontextlängen-/Kosten-
Risiko bei Jack/Conan zu vermeiden (siehe HANDOVER.md 10.10). Zweck: Jack/
Conan können damit bei einer Analyse erkennen, ob ein Kandidat zu einer
offenen Depot-/Watchlist-Lücke passt, ohne vollen Zugriff auf diese beiden
großen Dateien zu benötigen.

**Geltungsbereich: das gesamte Regelwerk gilt für alle drei KIs, nicht nur
Jarvis (2026-09-04, von Brian gefordert: "das ganze System soll für alle
Agenten gelten, sowohl für Jack als auch für Conan").** Jack und Conan
lesen `Agent-Playbook.md` selbst NICHT – sie bekommen bei jedem Bridge-Aufruf
nur das FACT-PACK + die Methodik-Dateien (TMR+Scout+TA) + eine Handvoll
vorangestellter Klarstellungs-Blöcke (siehe HANDOVER.md 10.13). Das
bedeutet: eine neue Regel hier gilt automatisch NUR für Jarvis, es sei
denn, sie wird explizit in einen dieser Blöcke übersetzt und bei jedem
Bridge-Aufruf mitgeschickt – genau das Problem, das schon beim Terminal-
State-Mechanismus auftrat (Block 4, HANDOVER.md 10.13: "er erreichte
Jack/Conan im API-Betrieb möglicherweise gar nicht") und sich am selben
Tag beim Bridge-Block 5 wiederholte (die Gründliche-These-Prüfung-Pflicht
stand zunächst nur hier, nicht im tatsächlichen Bridge-Prompt-Text).
**Ausnahme seit 2026-09-06 (Brian: "alle Agenten sollen Zugriff auf das
master-status haben und wissen was zu tun ist"):** `depot/master_status.md`
selbst wird bei JEDEM Bridge-Aufruf mit vollem aktuellem Inhalt in Block 6
eingebettet (siehe HANDOVER.md 10.13) – das ist die einzige Datei außer den
Methodik-Dateien, die Jack/Conan tatsächlich im Volltext zu sehen bekommen,
bewusst begrenzt auf dieses eine kompakte Status-Dashboard, nicht das ganze
Regelwerk.
**Feste Pflicht ab jetzt:** bei jeder neuen Regel mit inhaltlicher
Rating-/Empfehlungs-Wirkung (nicht reine Datei-Pflege-/Commit-Mechanik,
die bleibt Jarvis-only) explizit prüfen, ob sie auch Jack/Conan erreichen
muss – wenn ja, als neuen Klarstellungs-Block in HANDOVER.md 10.13
ergänzen UND die Blockzahl in `taeglicher-trigger-check`/`blitz-scan`
SKILL.md aktualisieren. Diese Prüfung ist explizit Teil der Regel-
Aufnahme-Disziplin oben, nicht optional. Aktuell sieben Standard-Blöcke
(siehe HANDOVER.md 10.13): SCHRITT-0/WACC/TRAINING-vs-N/V/Terminal-State
(Blöcke 1-4, 2026-09-02/03), Gründliche-These-Prüfung (Block 5, 2026-09-04),
Master-Status mit Volltext-Einbettung (Block 6, erweitert 2026-09-06) und
Fact-Pack-Tags-sind-nicht-bindend (Block 7, 2026-09-06).

**Jack/Conan haben jetzt eigene Live-Web-Recherche (2026-09-04, von Brian
gefordert: "Jack und Conan sollen die Freiheit haben, selbst zu
recherchieren").** Beide Bridge-Tools (`ask_gemini`, `ask_chatgpt`)
rufen standardmäßig (`enable_search=True`) das jeweilige native
Such-Tool auf – Gemini's Google-Search-Grounding bzw. OpenAI's
`web_search` über die Responses-API – statt sich ausschließlich auf
Jarvis' vorab recherchiertes FACT-PACK zu verlassen. Beide mit echten
End-to-End-Tests bestätigt (siehe HANDOVER.md 10.9/10.10 für Details,
inkl. eines Tests mit dem VOLLEN ~77KB-Scout-Methodik-Prompt). Bewusste
Konsequenz: die drei KI-Beine des Cross-Checks können jetzt tatsächlich
unabhängig voneinander unterschiedliche Fakten finden, nicht nur
unterschiedliche Interpretationen desselben kuratierten Datensatzes –
macht den Cross-Check echter unabhängig, aber auch potenziell
divergenter. Eine Abweichung zwischen KI-Rechercheergebnis und Jarvis'
Fact-Pack ist ab jetzt ein zu erwartendes, gesundes Cross-Check-Signal,
kein Fehler – bei Bedarf im finalen Cross-Check-Fazit explizit benennen,
welche Quelle/welches Datum sich als aktueller/verlässlicher erwiesen hat.
Kosten-/Latenz-Trade-off bewusst in Kauf genommen (siehe HANDOVER.md für
Details) – `enable_search=False` bleibt für reine Diagnose-/
Formatierungs-Anfragen ohne Recherchebedarf verfügbar.

**Jack/Conan bekommen zusätzlich exakte Kursdaten und einen eng begrenzten
Datei-Zugriff (2026-09-05, siehe HANDOVER.md 10.11 für die vollständige
technische Beschreibung).** Im agentischen Modus (`ask_gemini_agentic`/
`ask_chatgpt_agentic`) können sie jetzt zusätzlich zu den bestehenden
Depot-Tools `get_quote(symbol)` (echter Twelve-Data-Live-Kurs statt
Websuche-Schätzung) und `read_master_status()` (liest
`depot/master_status.md`) anfordern – Jarvis führt beides aus und reicht
das Ergebnis zurück, wie bei allen anderen agentischen Tools auch.
**`read_master_status` ist bewusst die EINZIGE per Tool zugängliche
Repo-Datei** – kein Zugriff auf `Agent-Playbook.md` selbst oder sonstige
Dateien. Begründung: Jack/Conan sollen unabhängige Gutachter für eine
konkrete, von Jarvis gestellte Aufgabe bleiben, kein freier
Systembrowser – vollständiger Regelwerk-Zugriff würde die Vergleichbarkeit
der drei unabhängigen Urteile verwässern (sie könnten anfangen, Regeln zu
hinterfragen statt sie anzuwenden). Beide Tools mit echten End-to-End-Tests
bestätigt (parallele Anforderung beider Tools, korrekte Jarvis-Ausführung,
korrekte finale Synthese bei beiden Bridges).

## 2. Das Regelwerk (bereits vollständig von Brian geliefert)

Drei eigenständige Prompts, gespeichert unter `prompts/`:

1. **TMR – "Jack, The Moat Agent" (v11.8, 2026-09-03: Korrelierte-Mali-Regel
   gegen Agent-Score-Double-Counting ergänzt, siehe Abschnitt 4 [3b])**:
   Fundamentalanalyse etablierter Firmen.
   DNA-Check (K-/E-Kriterien), Data-Integrity-Tagging, DCF/Reverse-DCF, Agent Score
   1-10, Sizing-Tiers 1-4, Rating KAUFEN/BEOBACHTEN/SCHROTT, Exit-Strategie mit
   fundamentalen Stop-These-Triggern (kein starrer Kurs-Stop).
2. **Scout – "Conan the Scout" (v1.12)**: Frühphasen-/Spekulations-Screening für
   potenzielle künftige Compounder (SaaS/Pre-Revenue/Deep-Tech/Biotech-Overrides).
   Moat-in-Formation, Gründer-Score, Outcome-Wahrscheinlichkeiten statt DCF, sehr
   kleine Sizing-Stufen (<0,5-2%). Rating WATCHLIST-ELITE/BEOBACHTEN-STARK/
   BEOBACHTEN-SPEKULATIV/ZU FRÜH/DURCHGEFALLEN.
3. **TA – "Jack, Pure Technical Analyst" (v1.10, 2026-08-30: Twelve-Data-
   Connector LIVE, siehe unten)**: Reines Chart-/Timing-Modul, keine
   Fundamentaldaten. Läuft eigenständig (SWING) oder im INVESTOR-ENTRY-Handoff mit
   TMR-Fair-Values (Preiszonen, Margin of Safety, Entry-Ampel). Datenbasis seit
   2026-08-30: **Twelve-Data-Connector ist verbunden und liefert echte
   Live-Indikatoren** (MACD, RSI, SMA/EMA, Bollinger-Bänder, Volumen,
   Pivot-Punkte/Unterstützung-Widerstand) statt Schätzung – per Testabfrage
   (ServiceNow/NOW, 2026-08-30) verifiziert (siehe Abschnitt 5, "Technische
   Analyse via Twelve Data").

Diese drei Prompts SIND das Regelwerk. Der Agent führt sie aus, er ersetzt sie nicht.

**Spielraum für Prompt-Anpassungen (2026-08-29, von Brian ausdrücklich
erweitert):** Bisher galt, dass Änderungen an den drei Prompt-Dateien nur
nach Brians Freigabe passieren (siehe META-RETRO-RUNDE [3c] in Abschnitt 4).
Brian hat das jetzt bewusst gelockert, gerade weil der Agent zunehmend
systematisch/automatisiert an der Depotverwaltung mitwirkt: die drei Prompts
sind "eine gewisse Grundbasis" (Brians Formulierung), Jarvis darf sie
eigenständig modifizieren/ergänzen/abändern, wenn das dem übergeordneten Ziel
(Abschnitt 1, "Nordstern": den Markt langfristig schlagen) besser dient –
z.B. um die kategorie-spezifische Exit-Logik (Champions/Profi thesenbasiert
vs. Talent/Zock charttechnik-/stop-loss-basiert, siehe "Verkaufsdisziplin &
Gewinnmitnahme-Regeln") sauber in den TA-Prompt (aktuell v1.9) einzuarbeiten.
**Was NICHT gelockert wurde:** (a) jede substanzielle Änderung bekommt weiter
eine neue Versionsnummer und wird in diesem Dokument nachvollziehbar
dokumentiert, keine stillen Änderungen; (b) die Grenze aus Abschnitt 1
("Grenze bleibt fix") gilt unverändert weiter – echte Order-Ausführung bleibt
manuell bei Brian, und zwar unabhängig von jeder künftigen technischen
Broker-Anbindung (siehe Abschnitt 8, "Geplante Broker-Anbindung"). Der
Spielraum betrifft ausschließlich die Analyse-/Bewertungs-/Exit-Logik in den
Prompts, nicht die Ausführungsbefugnis.

**Hermes-Gedächtnis-Synchronisations-Pflicht (2026-09-08, von Brian
gefordert: "hermes cron job (gedächtnis) bitte auch die aktuellen
veränderungen im prompt oder analyse tools immer auf den aktuellen stand
bringen"):** Die vier Hermes-Cron-Jobs laufen als `claude -p`-Headless-
Aufrufe OHNE Erinnerung an diese oder frühere Chat-Sessions – ihr einziges
"Gedächtnis" sind die SKILL.md-Dateien unter
`~/.claude/scheduled-tasks/<job>/SKILL.md` plus die Repo-Dateien selbst.
Ändert sich künftig eine der drei Methodik-Dateien unter `prompts/`
(Versionsbump, umbenannte Konzepte wie zuletzt "Master-Agent" → "Aegis",
neue Pflicht-Abschnitte wie SCHRITT 8/PFLICHT-JSON-SUMMARY) oder eines der
Analyse-Tools (`reports/render_chart.py`, `reports/render_pdf.py` etc.),
ist die Prüfung/Aktualisierung der betroffenen SKILL.md-Dateien PFLICHT-
BESTANDTEIL DERSELBEN Änderung, kein späterer Aufräum-Schritt:
1. Betroffene SKILL.md-Dateien identifizieren: `grep -rn "<alter Begriff/
   alte Versionsnummer>" ~/.claude/scheduled-tasks/*/SKILL.md` (aktuell
   referenzieren `taeglicher-trigger-check` UND `blitz-scan` alle drei
   Methodik-Dateien samt interner Versionsnummer; `wochenfazit`/
   `monatsrecap` referenzieren sie nicht direkt).
2. Stale Versionsnummern-Kommentare (z.B. "v11.8 intern") auf den
   tatsächlichen aktuellen Stand korrigieren.
3. Neue Pflicht-Verhaltensweisen (wie das JSON-Summary-Parsing seit
   Jack v11.10/Conan v1.13, siehe "Jack-Prompt-Redesign-Anfrage
   abgewogen"-Abschnitt) in JEDEN SKILL.md-Job übernehmen, der volle
   3-fach-Cross-Checks fährt (aktuell: `taeglicher-trigger-check` UND
   `blitz-scan`), nicht nur in den zuerst bearbeiteten.
4. Neue Terminologie (z.B. "Aegis") dort ergänzen, wo sie für das
   Verständnis der Prompts relevant ist, auch wenn die SKILL.md selbst
   den Begriff nicht wörtlich braucht.
Diese SKILL.md-Dateien liegen AUSSERHALB des Git-Repos (`~/.claude/
scheduled-tasks/`, nicht `~/Downloads/aktien-agent/`) und werden daher
NICHT von `git pull` in den Hermes-Läufen aktualisiert – sie müssen direkt
bearbeitet werden, jede Session (auch künftige, die diesen Absatz hier
liest) prüft das aktiv, statt sich auf einen Git-Sync zu verlassen.

**Namensgebung der drei KI-Stimmen im Cross-Check (2026-08-22, von Brian festgelegt):**
Im Report/Vergleich (Pipeline-Schritt 3+4) werden die drei Anbieter nicht mit ihrem
Firmennamen, sondern mit diesen Spitznamen ausgewiesen:

| Anbieter | Spitzname im Report |
|---|---|
| Gemini | **Jack** |
| ChatGPT | **Conan** |
| Claude | **Jarvis** |

Wichtig zur Klarstellung: Das ist reine Report-Beschriftung, ändert nichts an der
Regel "alle drei laufen denselben Prompt parallel" (siehe Pipeline-Schritt 3). Die
Namen Jack/Conan stammen zwar aus den Personas der TMR/TA- bzw. Scout-Prompts selbst,
werden hier aber als feste Anbieter-Kürzel verwendet, unabhängig davon, welcher der
drei Prompts gerade läuft (z.B. auch wenn Gemini den Scout-Prompt durchrechnet, heißt
seine Stimme im Vergleich trotzdem "Jack", nicht "Conan").

**Vierter Name, andere Rolle – Aegis (2026-09-08):** Die Tabelle oben listet
die drei PARALLELEN Analyse-Stimmen. **Aegis** ist kein vierter Anbieter in
dieser Tabelle, sondern der Name für Jarvis' orchestrierende Rolle
DANACH – Cross-Check-Synthese, Depot-Regel-Prüfung, finale Sizing-/Rating-
Entscheidung (siehe "Jack-Prompt-Redesign-Anfrage abgewogen"-Abschnitt).
Jarvis bleibt also unter zwei Namen im Umlauf, je nach Funktion: als
gleichberechtigte dritte Analyse-Stimme heißt es weiterhin "Jarvis", in der
zusammenführenden Rolle danach heißt dieselbe Funktion "Aegis".

## 3. Depot-Ziel-Struktur (Portfolio-Konstruktion)

**Basis-Matrix: zentrale Prozentwerte auf einen Blick (2026-09-03,
ergänzt aus dem 3-KI-System-Audit, P2-Punkt Conans – "zentrale Basis-
Matrix statt verstreuter Werte"):** dies ist eine reine
Nachschlage-Zusammenfassung der unten im Detail hergeleiteten Werte,
KEINE eigenständige Quelle – bei Widerspruch gilt immer die ausführliche
Herleitung an der jeweils verlinkten Stelle, nicht diese Tabelle.

| Kennzahl | Wert | Bezugsgröße | Quelle/Details |
|---|---|---|---|
| USA/Nordamerika-Obergrenze | ≤60% | Gesamtportfolio | Core-Rule 2, Abschnitt 14 |
| ETF-Mindestanteil | ≥50% (Ziel langfristig 60%) | Gesamtportfolio | Core-Rule 3, unten "ETF-/Aktien-Verhältnis" |
| Einzelposition max. | 10% (Ausnahme bis 12% bei Top-Conviction) | Gesamtportfolio | Core-Rule 4, unten "Positionsgrößen-Limits" |
| Trailing-Weight-Hard-Cap | 18% (zwingendes Rebalancing) | Gesamtportfolio | Core-Rule 5, Advisory-Review-Schwelle bereits ab 15% |
| Einzelposition min. | 1% (sonst Grenzfall-Markierung) | Gesamtportfolio | unten "Positionsgrößen-Limits" |
| Max. Einzelpositionen gesamt | 20 (ohne ETF) | Stückzahl | Core-Rule 6 |
| Positionsanzahl-Ziel | 10 Champions / 7 Profi / 3 Talent | Stückzahl | unten "10-7-3", Randfälle/Rundung dort |
| Champions-Kapitalgewicht | 35-45% | Aktienanteil (ohne ETF/Gold/Cash) | unten "Kapitalgewichts-Zielkorridor" |
| Profi-Kapitalgewicht | 20-30% | Aktienanteil | unten "Kapitalgewichts-Zielkorridor" |
| Talent-Kapitalgewicht | 25-40% | Aktienanteil | unten "Kapitalgewichts-Zielkorridor" |
| Watchlist-Kapazität | 50 Werte (seit 2026-09-08, vormals 20-30) | Stückzahl | "Watchlist-System" |
| Sperrlisten-Recheck | 90 Tage (Standard) | Zeitraum | "Watchlist-System", Vorfilter-Schritt |
| Offene-Empfehlung-Erinnerung | 5 Werktage | Zeitraum | "Täglicher Trigger-Check" Schritt 3C |

**Von Brian festgelegt (2026-08-22):**

- **Max. 20 Einzelwerte ohne ETF** (der Vanguard FTSE All-World Sparplan zählt separat
  dazu, macht also ca. 21 Positionen gesamt). **Depot-Erfassung ist seit 2026-08-23
  vollständig** (von Brian bestätigt: "das sind meine ganzen Positionen") – vier
  Broker (Scalable Capital, finanzen.net zero, Trade Republic, Smartbroker+), siehe
  `depot/`-Ordner. Bestätigter Endstand (2026-08-23): **28 Einzelwerte ohne ETF**
  (+1 ETF-Sparplan Vanguard FTSE All-World) – also deutlich über dem Ziel von 20.
  **Update 2026-08-28 (Depot-Restrukturierung):** Brian hat 12 Positionen komplett
  verkauft (Itochu, Stryker, Cintas, Visa, Grab Holdings, Amazon, Alphabet, Intuit,
  Keyence, S&P Global, Netskope, Waste Management – davon 10 aus dem Champions-
  Bucket) und 2 neue Talent-Kandidaten gekauft (Kraken Robotics, Rocket Lab).
  **Neuer Stand: 18 Einzelwerte ohne ETF.** Champions ist damit von 19 auf 9
  Positionen gefallen – jetzt wieder sauber im Zielband 8-10. Details siehe
  `depot/`-Ordner und "Depot-Restrukturierung" unten.
- **Kategorie-Namen (2026-08-23, von Brian festgelegt):** Die drei Risiko-Buckets
  tragen ab jetzt feste Namen nach einem Fußball-Leistungsstufen-Bild – **Champions /
  Profi / Talent**. Jede Positions-Kategorisierung (Pipeline-Schritt 2, Reports,
  Wochenfazit) verwendet ausschließlich diese drei Namen, nicht mehr die alten
  Arbeitsbegriffe "Compounder/Small-Mid-Potenzial/Riskant".
- **Ziel-Aufteilung der 20 Werte nach Risiko/Chance:**
  - **Kategorie "Champions" (8-10 Positionen)** – "absolute/Welt-Compounder", der
    stabile Kern. Etablierte Qualitätsfirmen, laufen durch den **TMR**-Pfad (FULL
    DEEP DIVE). Beispiele aus dem bestehenden Depot, die in diese Kategorie fallen:
    S&P Global, ServiceNow, Broadridge, CBOE Holdings, MercadoLibre,
    Constellation Software.
  - **Kategorie "Profi" (3-5 Positionen)** – kleinere Werte aus Small-/Mid-Cap mit
    Potenzial, noch nicht die ganz etablierten Compounder, aber mit klarer Story/
    Aufholpotenzial. Läuft eher über den **Scout**-Pfad (oder TMR QUICK FILTER, je
    nach Reifegrad). Von Brian genannte Beispiele aus dem bestehenden Depot:
    **Rambus, A10 Networks, Tristel PLC**.
  - **Kategorie "Talent" (Rest-Slots bis 20 gesamt, also grob 5-9 Positionen)** –
    ausschließlich riskantere Werte mit viel Potenzial, die spekulative Spitze des
    Depots, bewusst kleine Positionsgrößen (Scout Sizing-Stufen, Trace-Position bis
    max. 2%). Läuft über den **Scout**-Pfad. Talent ist bewusst NICHT auf eine feste
    Bandbreite gedeckelt, sondern füllt das auf, was nach Champions- und
    Profi-Zuteilung an den 20 Slots übrig bleibt.
  - Zusammen ergeben Champions + Profi das, was Brian als "15-17 stabile Werte"
    bezeichnet hat; Talent sind die restlichen riskanten Werte on top.
- **Update (2026-09-03, von Brian festgesetzt, dann per 3-KI-System-Audit
  am selben Tag als rechnerisch fehlerhaft entlarvt und auf "10-7-3"
  korrigiert): feste Positionsanzahl-Formel.** Löst die ursprüngliche
  Spanne (Champions 8-10/Profi 3-5/Talent 5-9 Rest-Slots) durch eine feste
  Zielzahl ab: **10 Champions, 7 Profi, 3 Talent** = 20 Einzelwerte gesamt
  (passt exakt zur bestehenden Max.-20-Grenze).
  - **Verifizierter Rechenfehler in der ursprünglichen "10-6-4"-Version
    (2026-09-03, im 3-KI-System-Audit von Conan gefunden, von Jarvis gegen
    Agent-Playbook.md:913 verifiziert, von Jack nachgerechnet):** die
    ursprüngliche Begründung "4 Talent-Slots, weil 4×10%-Positionscap
    exakt die 40%-Talent-Obergrenze trifft" vermischte zwei verschiedene
    Bezugsgrößen – der 10%-Positionsdeckel (siehe "Positionsgrößen-Limits"
    oben) gilt für das **Gesamtportfolio**, die 40%-Talent-Obergrenze für
    den **Aktienanteil** (ohne ETF). Bei einem Aktienanteil von ca. 74%
    des Gesamtportfolios (Stand 2026-09-03) entsprechen 4 Positionen à
    10% Gesamtportfolio (=40% Gesamtportfolio) tatsächlich ca. 54% des
    Aktienanteils – weit über der 40%-Obergrenze, nicht exakt daran.
    Korrekt gerechnet: 40% Aktienanteil × 74% ≈ 29,6% Gesamtportfolio;
    29,6% / 10%-Positionscap ≈ 2,96 → **3 Positionen**, nicht 4.
  - **10 Champions** – oberes Ende der alten Spanne, unverändert.
  - **7 Profi** – gegenüber der alten Spanne (3-5) angehoben (der frei
    gewordene Slot aus der Talent-Korrektur geht hierhin), weil Profi in
    der Praxis (Stand 02./03.09.) sowohl bei Positionsanzahl als auch beim
    Kapitalgewicht (16,4% vs. Ziel 20-30%) strukturell unterrepräsentiert
    war. Ist ausdrücklich der Baustein, der als nächstes bevorzugt
    aufgefüllt wird.
  - **3 Talent** – rechnerisch korrekt hergeleitet aus dem
    10%-Positionsdeckel (Gesamtportfolio-Basis) im Verhältnis zur
    40%-Talent-Obergrenze (Aktienanteil-Basis) bei aktueller
    Portfolio-Zusammensetzung, siehe Herleitung oben.
  - **Wichtiger Vorbehalt (2026-09-03, aus dem System-Audit):** diese
    Herleitung hängt am AKTUELLEN Verhältnis Aktienanteil/Gesamtportfolio
    (~74%). Wächst der ETF-Anteil wie langfristig geplant Richtung 50-60%
    des Gesamtportfolios, sinkt der Aktienanteil-Anteil entsprechend, und
    dieselbe Rechnung würde eine NOCH niedrigere Talent-Positionszahl
    ergeben (bei 45% Aktienanteil z.B. nur noch ca. 2 Positionen). Die
    Zahl "3" ist also kein für alle Zeit stabiler Wert, sondern an die
    aktuelle Aufbauphase gebunden – bei spürbarer Verschiebung des
    ETF/Aktienanteil-Verhältnisses (Prüfpunkt: jedes Wochenfazit) muss
    diese Herleitung neu gerechnet werden, nicht nur einmalig festgelegt
    bleiben.
  - **Langfristiger Ausblick (von Jarvis empfohlen, noch nicht
    festgeschrieben):** unabhängig von der Positionscap-Rechnung spricht
    aus reiner Diversifikations-Sicht (Portfolio-Effekt bei spekulativen
    Wetten statt Dominanz einzelner Ausfälle/Volltreffer bei nur 2-3
    Positionen) einiges dafür, Talent perspektivisch eher auf 5-6
    Positionen aufzuweiten als weiter zu verengen – das steht in
    Spannung zum obigen Cap-Argument (das eher Richtung 2 tendiert, wenn
    der Aktienanteil weiter sinkt) und ist bewusst als ungelöste
    Zielkonflikt-Frage für eine spätere, bewusste Entscheidung vorgemerkt,
    nicht Teil der aktuellen Festlegung.
  - **Praktische Konsequenz zum Zeitpunkt der Korrektur:** Champions
    aktuell 8/10 (2 Slots frei), Profi aktuell 5/7 (2 Slots frei), Talent
    aktuell 5/3 (**2 über Ziel** – keine neuen Talent-Zukäufe, bis
    mindestens eine bestehende Position ausscheidet, auch wenn das
    Kapitalgewicht noch Spielraum hätte). Siehe `depot/kategorisierung.md`
    für die laufend aktuelle Zählung.
  - **Randfälle der Formel, explizit geklärt (2026-09-03, aus dem
    3-KI-System-Audit – Conan hatte angemerkt, dass eine formal richtige
    Formel trotzdem operativ instabil sein kann, solange diese Fälle offen
    sind):**
    - **Rundung:** kaufmännisch (nearest), nicht floor/ceil – siehe die
      obige Herleitung "29,6% / 10% ≈ 2,96 → 3", nicht abgerundet auf 2.
      Bei exakt x,5 (Gleichstand) wird aufgerundet, da eine zu enge
      Talent-Grenze mehr Nachkauf-Verbote erzeugt als eine zu weite
      Grenze Risiko – im Zweifel die praktisch handhabbarere Richtung.
    - **Cash zählt NICHT zum Gesamtportfolio-Nenner der Positionscap-
      Rechnung** – der 10%-Positionsdeckel und die 10-7-3-Formel beziehen
      sich auf den investierten Gesamtwert (Aktien + ETF + Gold), Cash-
      Bestand ist bewusst außen vor (sonst würde reine Cash-Haltung die
      zulässige Talent-Zahl künstlich verzerren).
    - **Illiquide/schwer handelbare Positionen** zählen normal als eine
      Position in der 10-7-3-Zählung – es gibt keine Sonderbehandlung,
      Illiquidität ist ein Risikofaktor der CRV-/Sizing-Einordnung, nicht
      der Positionsanzahl-Formel.
    - **Teilverkäufe:** eine Position, die nur teilverkauft wurde, aber
      weiter gehalten wird, zählt weiter als 1 volle Position in der
      Kategorie-Zählung, unabhängig vom verbleibenden Kapitalgewicht –
      erst ein VOLLSTÄNDIGER Ausstieg reduziert die Positionsanzahl.
    - **Sehr kleines Portfolio oder ungewöhnlich hohe Konzentration:**
      die 10-7-3-Formel setzt implizit voraus, dass das Depot groß genug
      ist, dass 10%-Positionen überhaupt sinnvoll diversifizieren (siehe
      Aktienanteil-Abhängigkeit im Vorbehalt oben). Fällt der
      Aktienanteil durch eine starke Konzentration in wenigen Positionen
      deutlich unter die aktuell zugrunde gelegte ~74%-Quote oder
      übersteigt eine Einzelposition durch reines Kursachterbahn-Wachstum
      vorübergehend den 10%/12%-Deckel (siehe Positionsgrößen-Limits),
      gilt: der Positions-CAP-Verstoß wird wie gehabt über die
      12%-Ausnahme/Trailing-Weight-Review behandelt (Abschnitt 3/
      Advisory-Rules), NICHT durch eine Neuberechnung der 10-7-3-Formel
      im laufenden Betrieb – die Formel wird nur bei den oben genannten
      strukturellen Prüfpunkten (jedes Wochenfazit bei Aktienanteil-
      Verschiebung) neu hergeleitet, nicht ad-hoc bei jeder
      Kursschwankung.
- **Update (2026-09-03, von Brian gefordert nach uneinheitlicher
  Kategorisierung im Strategiespiegel-Report): feste Nachschlage-Tabelle
  statt freier Einschätzung pro Analyse.** Auslöser: Jack, Conan und Jarvis
  ordneten dieselben Positionen (u.a. Allianz, Bank Central Asia, Rambus,
  Tristel) unterschiedlichen Kategorien zu – teils weil unzulässige Proxies
  wie Positionsgröße oder Emerging-Markets-Status statt der eigentlichen
  Kriterien (Marge/Marktstellung/Wachstumsverlässlichkeit) herangezogen
  wurden. Ab jetzt gilt: **die Kategorie-Zuordnung jeder Depot-Position ist
  in `depot/kategorisierung.md` fest hinterlegt und wird von KEINEM Report,
  keiner Analyse und keinem Scheduled Task neu erraten** – nur dort
  gepflegt, bei Neuaufnahme oder bewusster Neubewertung im Wochenfazit,
  jeweils mit Begründung und Datum. Diese Datei ist die Quelle der Wahrheit
  für Champions/Profi/Talent, nicht die Kriterien-Beschreibung unten (die
  bleibt die Regel, nach der eingeordnet wird – aber die Zuordnung selbst
  steht in der separaten Datei).
- **Update (2026-08-29, von Brian präzisiert): qualitative Kriterien je
  Kategorie, geschärfte Beispiele, und Kapitalgewichts-Ziel statt reiner
  Positionsanzahl.** Ergänzt/präzisiert die obige, ursprünglich 2026-08-22
  festgelegte Struktur – die drei Kategorie-Namen und der Grundgedanke
  bleiben, die Kriterien werden aber schärfer gefasst:
  - **Champions** – absolute Weltklasse-Unternehmen: hohe/sehr hohe Margen,
    Monopol- oder Quasi-Monopolstellung, hohe und verlässliche
    Wachstumsraten. Beispiele (Brians Formulierung): **Intuitive Surgical,
    Münchener Rück, ServiceNow**.
  - **Profi** – die "zweite Reihe": Firmen, denen die meisten Anleger wenig
    Aufmerksamkeit schenken, aber mit guten bis hohen Margen und guter bis
    hoher Wachstumsrate, teils auf dem Weg, selbst zum Compounder/Champion
    aufzusteigen. Beispiele (Brians Formulierung): **Broadridge, CBOE
    Holdings, A10 Networks**. **Wichtig:** Broadridge und CBOE galten in der
    ursprünglichen Fassung oben noch als Champions-Beispiele – nach dieser
    Präzisierung fallen sie unter die schärferen Champions-Kriterien
    (Monopolstellung, sehr hohe Marge) eher in die Kategorie Profi. Bei der
    nächsten Depot-Kategorisierung entsprechend berücksichtigen.
  - **Talent / Zock / Momentum** – aktuell eventuell noch unprofitabel, aber
    mit nischigem/interessantem Geschäftsmodell und Wachstumsfaktor, der
    schnell in Richtung Profitabilität führen kann, oder Werte, die wegen
    aktueller Marktereignisse/Momentum (z.B. der aktuelle KI-Hype) schnelle,
    hohe Kurssprünge machen können. Beispiele (Brians Formulierung): **SoFi
    Technologies, IREN** (Iris Energy – noch nicht im Depot/auf der
    Watchlist, dient hier nur als Archetyp-Beispiel). Für diese Kategorie
    gilt ausdrücklich ein anderer Exit-Ansatz als bei Champions/Profi:
    stärker charttechnik-/stop-loss-basiert statt rein thesenbasiert – siehe
    dazu die Ergänzung in "Verkaufsdisziplin & Gewinnmitnahme-Regeln" unten.
  - **Zeithorizont-Tag innerhalb Talent/Zock (2026-08-29, von Brian
    präzisiert):** Nicht jeder Talent/Zock-Wert ist ein reiner kurzfristiger
    "Zock"/Trade – manche sieht Brian bewusst als längerfristige
    Wette über mehrere Jahre, auch wenn sie aktuell (noch) unprofitabel oder
    klein sind. Damit diese nicht mit reinen Momentum-/Hype-Titeln "in
    einen Topf geworfen" werden, bekommt jede Talent/Zock-Position bei der
    Kategorisierung (Pipeline-Schritt 2, Watchlist-Eintrag, Depot-Übersicht)
    einen zusätzlichen Tag:
    - **Talent (langfristig)** – Brian sieht die These über mehrere Jahre,
      trotz aktuellem Klein-/Risikostatus. Der Exit-Ansatz bleibt näher am
      thesenbasierten Vorgehen wie bei Champions/Profi (siehe
      "Verkaufsdisziplin & Gewinnmitnahme-Regeln") – ein technisches
      Stop-Loss ist hier eher ein Sicherheitsnetz, nicht der primäre
      Auslöser, und kurzfristige Volatilität allein ist kein Verkaufsgrund.
    - **Zock/Trade** – bewusst kurzfristig/momentum-getrieben (z.B.
      aktuelles Marktthema wie der KI-Hype), ohne Anspruch auf eine
      mehrjährige These. Hier gilt der stop-loss-/charttechnik-primäre
      Exit-Ansatz wie ursprünglich beschrieben.
    Fehlt der Tag bei einer bestehenden Talent/Zock-Position, wird er beim
    nächsten Wochenfazit nachgetragen (systematisch hergeleitet, siehe
    unten – nicht mehr freie Einschätzung) statt die Position ungetaggt zu
    lassen.

    **Systematische Tag-Herleitung (2026-09-01, von Brian gefordert –
    ersetzt "Jarvis' Einschätzung" durch nachvollziehbare Kriterien).** Der
    Tag wird nicht mehr frei geschätzt, sondern automatisch aus den ohnehin
    vorliegenden Scout-Modulergebnissen abgeleitet (Full Scout oder Quick
    Scout, siehe `prompts/conan-the-scout-v1.12.md`) – kein zusätzlicher
    Analyseaufwand, nur eine feste Auswertungsregel oben drauf:
    - **Signale für "Talent (langfristig)"** (zutreffend = 1 Punkt je Signal):
      1. Moat-in-Formation ≥3/4 (solide/starke Ansätze, nicht nur "Story,
         kein struktureller Vorsprung").
      2. Trichter-Einordnung mindestens "auf dem Weg zu Stufe 2" (nicht
         reines Stufe-1-Rohtalent ohne erkennbare Weiterentwicklung).
      3. Killer-Thesis-Bruchwahrscheinlichkeit "Niedrig" oder "Mittel"
         (nicht "Hoch").
      4. Kein aktiver ☢ Hype-Strike.
      5. Die Kernthese (Scout Conviction) ist strukturell (Marktanteils-/
         Moat-Aufbau über Jahre) statt an einem einzelnen kurzfristigen
         Binärereignis hängend (z.B. "ein Produkt muss in den nächsten
         Monaten funktionieren").
    - **Auswertung:** ≥3 von 5 Signalen erfüllt → Tag **"Talent
      (langfristig)"**. ≤2 von 5 erfüllt → Tag **"Zock/Trade"**. Bei genau
      2/5 UND erkennbarem Aufwärtstrend der Signale gegenüber der letzten
      Bewertung (z.B. Moat-in-Formation hat sich verbessert) ist eine
      Ausnahme zugunsten "Talent (langfristig)" mit kurzer Begründung
      zulässig – ohne klaren Aufwärtstrend gilt im Zweifel die
      konservativere Einstufung "Zock/Trade" (gleiches Prinzip wie die
      "Minimale-Annahme-Pflicht" im Scout-Regelwerk: Datenlücken/Grenzfälle
      werden nie zugunsten der wohlwollenderen Einstufung ausgelegt).
    - **Herkunftsvermerk:** jede Tag-Zuweisung wird mit den ausschlaggebenden
      Signalen dokumentiert (z.B. "Zock/Trade – 2/5: Moat 2/4, Trichter
      Stufe 1, Killer-These Hoch, kein Hype-Strike, Kernthese
      Einzelereignis-getrieben"), damit die Einstufung nachvollziehbar
      bleibt statt eine Blackbox zu sein.
    - **Höherstufung möglich, nicht nur einmalige Festlegung:** verbessern
      sich die Signale über mehrere Quartale (z.B. im Rahmen des Prediction-
      Ledger-Post-Mortems, siehe Agent-Playbook-Archiv-Diskussionen.md Abschnitt 9), wird der Tag beim nächsten
      regulären Scout-Durchlauf neu bewertet, nicht nur bei Erstaufnahme
      einmal festgelegt.
    - Brian kann jede automatisch hergeleitete Einstufung weiterhin jederzeit
      manuell korrigieren – das System liefert einen begründeten Vorschlag,
      keine unumstößliche Festlegung.
  - **Kapitalgewichts-Ziel (löst die reine Positionsanzahl-Spanne oben für
    die GEWICHTUNG ab, die Positionsanzahl-Range bleibt als grober
    Diversifikations-Rahmen bestehen):** **Champions ca. 35-45%**,
    **Profi ca. 20-30%**, **Talent/Zock ca. 25-40%** (2026-08-30, von Brian
    moderat in Richtung Rendite-Ziel nachjustiert – Champions leicht von
    40-50% auf 35-45% gesenkt, Talent von reiner "Restgröße" auf einen
    bewusst höher angesetzten Zielkorridor 25-40% angehoben, siehe
    "Renditeziel-Feinjustierung" unten für die Begründung) – **jeweils
    gerechnet als Anteil am Aktienanteil
    (Einzelwerte-Summe ohne den FTSE-All-World-ETF), nicht am Gesamtportfolio
    (2026-08-29, von Brian präzisiert – siehe Abschnitt 1, "Rolle des
    FTSE-All-World-ETF vs. Aktienanteil": der ETF dient der Altersvorsorge und
    steht außerhalb der aktiv gesteuerten Champions/Profi/Talent-Struktur).**
    **Aufbauphase-Hinweis (2026-08-29, von Brian ergänzt):** Solange sich das
    Depot noch im Aufbau befindet (siehe "Phasenweise Skalierung nach
    Depotgröße" unten), spielt die exakte Einhaltung dieser Gewichtung eine
    eher untergeordnete Rolle – sie wird trotzdem jede Woche als Kennzahl
    mitgeführt, aber nicht als scharfe Regelverletzung behandelt wie z.B. die
    10%-Positionsgrenze. Ausdrücklich **"je nach Performance"** (Brians
    Formulierung) – organisches Über-/Unterschreiten durch Kursbewegung ist
    kein automatischer Regelverstoß wie bei den harten Positionsgrößen-
    Limits, sondern wird im Wochenfazit als Kennzahl mitgeführt, analog zur
    Regionen-/Sektor-Verteilung. Wird ab dem nächsten Wochenfazit als eigene
    Kennzahl im Portfolio-Regel-Check geführt.
    **Conviction-Allocation innerhalb der Kategorie (2026-08-30, aus der
    Cross-KI-Diskussion in Agent-Playbook-Archiv-Diskussionen.md Abschnitt 10, von Brian freigegeben):** Nicht
    jede Position in derselben Kategorie bekommt automatisch dasselbe
    Gewicht – innerhalb der Kategorie-Bandbreite wird zusätzlich nach
    Qualitätsstufe gestaffelt: **Exceptional** ca. 1,25-1,5× Basisgewicht,
    **Strong** 1,0×, **Average** 0,75×, **Weak/Unclear** 0,5× oder
    Exit-Kandidat. Ziel ist nicht mehr Risiko pro Idee, sondern Kapital
    konsequenter von mittelmäßigen zu außergewöhnlichen Ideen zu
    verschieben, ohne die harten Kategorie-/Positionsgrenzen anzutasten.
    Ergänzt durch das **Opportunity-Cost-Rebalancing** (siehe
    Head-to-Head-Ersatz-Gate unten): eine bestehende Position wird nicht nur
    mit "ist sie noch gut?", sondern mit "ist sie noch eine der besten
    Kapitalallokationen im Depot?" gemessen.
  - **Hintergrund/Ziel (Brians Formulierung):** Champions als stabilisierender
    Kern, während Brian plant, sein Scalable-Capital-Konto (dort liegen der
    Vanguard-FTSE-All-World-Sparplan und BBCA) in den nächsten Tagen an den
    Agenten anzubinden, um Käufe/Verkäufe zu systematisieren/automatisieren
    und so zusätzliche Stabilität ins Depot zu bringen – siehe dazu die neue
    Notiz "Geplante Broker-Anbindung (Scalable Capital)" in Abschnitt 8
    (Offene Punkte) für die wichtige Einschränkung, was der Agent dabei
    NICHT übernehmen kann/darf.
  - **Strategie-Fit-Gate für neue Kandidaten (2026-08-29, von Brian
    gefordert):** Nachdem alle drei KIs unabhängig voneinander Brians
    Strategie im "Strategiespiegel"-Test korrekt erkannt haben ("da liegt
    Conan nicht weit weg", Brians Formulierung), bittet Brian ausdrücklich
    darum, diese Erkenntnis auch bei der Kandidaten-Auswahl konsequent
    anzuwenden: **nicht jede beliebige Aktie landet auf der Watchlist oder im
    Depot.** Vor jeder Watchlist-Aufnahme (zusätzlich zum Identity-Gate oben)
    und jedem Kauf-Kandidaten aus der Pipeline muss explizit abgewogen und im
    Kurz-Fazit/Watchlist-Eintrag kurz begründet werden, ob der Wert **wirklich
    zur Strategie passt** – Champions-Moat-Qualität, Profi-Aufstiegspotenzial
    oder Talent/Zock-Asymmetrie mit klarer These (siehe Kategorie-Kriterien
    oben) – statt nur "irgendein Qualitätsname" oder "irgendein spekulativer
    Hype-Titel" zu sein. Ein Kandidat ohne einen dieser klaren Kategorie-Fits
    wird nicht aufgenommen, selbst wenn er isoliert betrachtet fundamental
    solide wirkt.
  - **Duplikations-Check gegenüber dem FTSE-All-World-ETF (2026-08-29, von
    Brian erklärt):** Der Grund, warum das Depot bestimmte Compounder enthält
    und nicht z.B. Amazon, Alphabet, Visa, S&P Global, Microsoft & Co.
    (obwohl die genauso gut in die Champions-Kriterien passen würden): diese
    Mega-Caps sind **bereits stark im FTSE-All-World-ETF vertreten** (siehe
    "Rolle des FTSE-All-World-ETF vs. Aktienanteil", Abschnitt 1) – sie
    einzeln zusätzlich zu halten wäre größtenteils Doppelung statt
    zusätzlicher Diversifikation/Alpha. Der Aktienanteil soll bevorzugt dort
    ansetzen, wo der ETF selbst wenig/keine gezielte Exposure liefert (z.B.
    Nischen-Champions, Software-Serial-Acquirer, Small-/Mid-Cap-Profis,
    asymmetrische Talent-Wetten). **Das ist eine bevorzugte Heuristik, kein
    hartes Ausschlusskriterium:** Brian hat ausdrücklich klargestellt, dass
    einige der zuletzt aus privaten (nicht strategischen) Gründen verkauften
    Mega-Caps (Amazon, Alphabet, Visa, S&P Global u.a., siehe
    "Depot-Restrukturierung" unten) mit hoher Wahrscheinlichkeit später wieder
    ins Depot zurückfinden werden – ein Wiederaufnahme-Vorschlag für diese
    konkreten, ihm bereits bekannten Titel ist also nicht grundsätzlich
    ausgeschlossen, wenn Timing/Bewertung passen. Der Duplikations-Check
    betrifft in erster Linie NEUE, bisher unbekannte Kandidaten aus dem
    Screening (Pipeline-Schritt [1]).
  - **Head-to-Head-Ersatz-Gate gegen die schwächste Depot-Position (2026-08-30,
    von Brian gefordert):** Brians Formulierung: "auch wenn der potenzielle
    Kandidat besser ist, muss er für das gesamt depot einen Mehrwert bringen
    und Sektorspezifisch im bereits angegebenen Rahmen sein." Zusätzlich zum
    Strategie-Fit-Gate und Duplikations-Check oben gilt ab jetzt: BEVOR eine
    tatsächliche KAUFEMPFEHLUNG für einen Kandidaten (aus Watchlist oder
    frischem Screening) ausgesprochen wird – nicht nur die reine
    Watchlist-Aufnahme, die weiter nach der bisherigen Obergrenzen-Logik läuft
    – durchläuft er einen expliziten Wettbewerbsvergleich gegen die aktuell
    schwächste Depot-Position seiner Zielkategorie:
    1. **Schwächste Position identifizieren:** innerhalb der Zielkategorie
       (Champions/Profi/Talent) die Position mit der geringsten aktuellen
       fundamentalen Überzeugungskraft bestimmen – nicht zwingend die mit der
       schlechtesten Kursperformance, sondern die mit dem niedrigsten zuletzt
       dokumentierten Rating/Agent-Score, einem bereits ausgelösten
       Downgrade-/Stop-These-Trigger, oder (bei mehreren ähnlich schwachen
       Positionen) die mit dem am wenigsten überzeugenden aktuellen
       Investment-Case – transparent benennen, welche Position das ist und
       warum.
    2. **Qualitäts-Vergleich:** Rating des Kandidaten (TMR-Quick-Filter/Deep-
       Dive bzw. Scout) gegen das aktuelle Rating dieser schwächsten Position
       stellen. Ist der Kandidat nicht klar überzeugender, bleibt es bei
       BEOBACHTEN/Watchlist-Status – keine Kaufempfehlung, unabhängig von den
       folgenden zwei Prüfungen.
    3. **Portfolio-Mehrwert-Check:** selbst wenn der Kandidat qualitativ
       vorne liegt – bringt seine Aufnahme wirklich zusätzlichen Wert fürs
       GESAMTE Depot (Diversifikation, neue Exposure), oder dupliziert er nur
       eine bereits gut abgedeckte Nische/ein ähnliches Geschäftsmodell (z.B.
       ein weiterer Zahlungsdienstleister, wenn schon mehrere im Depot sind)?
       Ohne echten Mehrwert für das Gesamtdepot besteht der Kandidat dieses
       Gate NICHT, egal wie gut er isoliert bewertet ist.
    4. **Sektor-/Kapitalgewichts-Rahmen-Check:** die Aufnahme (und ein
       eventueller Verkauf der schwächsten Position dafür) darf die bereits
       oben festgelegten Ziel-Bandbreiten NICHT sprengen – Sektor-Streuung,
       Kapitalgewichts-Ziel je Kategorie, geografische Streuung,
       Positionsgrößen-Limits. Ein Kandidat, der z.B. den Technologie-Sektor
       über die 30-38%-Zielspanne hinaustreiben würde, besteht dieses Gate
       NICHT, egal wie überzeugend er individuell ist.
    5. **Nur wenn ALLE DREI Prüfungen (2-4) bestanden sind**, erfolgt eine
       tatsächliche Handlungsempfehlung – entweder als "Ersetzen"
       (Teil-/Komplettverkauf der schwächsten Position + Kauf des Kandidaten)
       oder, falls kein Ersatz nötig ist, als regulärer Neukauf über frisches
       Kapital (Sparrate/Cash-Reserve). Besteht der Kandidat eine der drei
       Prüfungen nicht, bleibt es bei BEOBACHTEN/Watchlist mit einer knappen,
       ehrlichen Begründung, WELCHE Prüfung nicht bestanden wurde – kein
       stillschweigendes Fallenlassen einer guten Einzelbewertung ohne
       Erklärung.
    6. **Steuer-/Turnover-Disziplin bei Punkt 2 (2026-08-30, aus der Cross-KI-
       Diskussion in Agent-Playbook-Archiv-Diskussionen.md Abschnitt 10, von Brian freigegeben):** "Klar
       überzeugender" heißt nicht "auf dem Papier minimal besser". Ein neuer
       Kandidat muss die schwächste Position DEUTLICH schlagen, nicht nur
       marginal – zusätzlich müssen Kapitalertragsteuer, Transaktionskosten
       und Spread des Verkaufs in die Abwägung einfließen. Ein Swap, der nur
       eine leicht höhere erwartete Rendite verspricht, aber via realisierter
       Steuer die Compounding-Basis schmälert, besteht dieses Gate NICHT.
       Verhindert unnötigen Portfolio-Umschlag ("Shiny Object Syndrome") rein
       wegen marginaler Verbesserungen.
    **Geltungsbereich:** gilt für den proaktiven Bodenbildungs-Kauf-Anlass im
    täglichen Trigger-Check (Eskalationslogik, Anlass g), für die "Mögliche
    Käufe"-Abschnitte in Wochenfazit und Monatsrecap, für Sofort-Kauf-Funde aus
    dem täglichen Kandidaten-Scan, und für jede ad-hoc-Kaufberatung, wenn Brian
    direkt danach fragt.
    **Vorab-Check schon bei jeder Kurs-/Chancen-Vorauswahl (2026-08-30, von
    Brian ergänzt):** Punkt 4 (Sektor-/Kapitalgewichts-Rahmen-Check) wird nicht
    erst am Ende des Gates angewendet, sondern schon immer dann mitgedacht,
    wenn Watchlist- oder Depot-Kandidaten allein nach Kursverlauf/Chart-Chance
    als "aktuell interessant" eingestuft werden (z.B. bei einer reinen
    Pullback-/Rücksetzer-Analyse ohne vollen 3-fach-Check). Ein Kandidat, der
    in einen bereits überdehnten Topf fällt – aktuell z.B. USA/Nordamerika
    (über der 60%-Obergrenze) oder Finanzwesen (über der 20-25%-Zielspanne) –
    wird in so einer Vorauswahl klar niedriger priorisiert bzw. explizit als
    "eher nicht in Erwägung ziehen" markiert, auch wenn der Kursverlauf für
    sich genommen attraktiv aussieht. Trifft ein Kandidat gleich auf ZWEI
    bereits überdehnte Töpfe zugleich (z.B. USA UND Finanzwesen, wie S&P
    Global oder FICO), ist das ein besonders starkes Minus-Signal schon in der
    Vorauswahl. Kandidaten, die stattdessen einen unterbesetzten Topf auffüllen
    würden (z.B. aktuell Technologie unter 30% oder Japan/Asien-Region), werden
    umgekehrt positiv hervorgehoben – idealerweise beides zugleich (nicht-USA
    UND unterbesetzter Sektor).
    **Konkrete Anwendung auf USA/Finanzwesen-Schnittmenge im Depot
    (2026-08-30, von Brian entschieden):** Die drei aktuellen Depot-Positionen
    in der doppelt überdehnten Schnittmenge USA + Finanzwesen sind SoFi
    Technologies, Broadridge Financial Solutions und CBOE Holdings. Brian
    möchte **SoFi und CBOE ausdrücklich NICHT als Ersatz-Kandidaten** für das
    Head-to-Head-Gate heranziehen (CBOE will er sogar aktiv weiter ausbauen,
    trotz der Übergewichtung – bewusste Brian-Entscheidung, kein
    automatisches Gegensteuern gegen diese beiden Positionen). **Broadridge
    bleibt der einzige realistische Ersatz-Kandidat** aus dieser Schnittmenge.
    Auf der Gegenseite sind Hoya und Disco Corp (beide Watchlist, kein
    Zielkonflikt) aktuell im Gespräch, aber nach Brians eigener Einschätzung
    "noch nicht genug korrigiert" für einen Einstieg – Hoya mit einem eher
    milden Rücksetzer (-11 bis -14% über 3-6 Monate bei weiterhin +17% auf
    Sicht von 1 Jahr), Disco Corp mit einem bereits deutlicheren Rückgang
    (-13 bis -22% über 3-6 Monate), der aber als zyklischer Halbleiterausrüster
    historisch noch tiefer fallen kann. Kein sofortiger Handlungsbedarf – der
    tägliche Trigger-Check (Bodenbildungs-Anlass, Eskalationslogik g) soll
    Hoya, Disco Corp UND Broadridge weiter beobachten und erst melden, wenn
    sich bei einem der drei ein echtes Signal zeigt (Bodenbildung bei
    Hoya/Disco bzw. eine Verschlechterung der These bei Broadridge), statt
    einen Swap zu erzwingen, nur weil die Sektor-/Regionen-Zahlen es
    nahelegen.
  - **Steuerliches Rechenmodul für Punkt 6 (2026-08-30, von Brian mitgeteilt,
    macht die Steuer-/Turnover-Disziplin oben konkret statt nur qualitativ):**
    Brian ist **nicht kirchensteuerpflichtig** (2026-08-30 korrigiert –
    vorherige Annahme einer Kirchensteuerpflicht war falsch, hiermit
    verworfen). Effektiver Steuersatz auf realisierte Kursgewinne damit die
    normale Kapitalertragsteuer inkl. Solidaritätszuschlag, ohne
    Kirchensteuer-Komponente: **25% Kapitalertragsteuer + 5,5% Soli darauf =
    26,375%** – dieser Satz gilt ab jetzt fest für alle Steuer-Berechnungen
    in diesem Regelwerk.
    **Freistellungsaufträge (Sparerpauschbetrag), Stand 2026-08-30 (von Brian
    kontrolliert und neu verteilt – ersetzt die vorherige, unvollständige
    Aufteilung):** **Scalable Capital: 150€** (angehoben von 100€; von Brian
    bestätigt 2026-08-30 – das neue Limit von 150€ ist bereits **vollständig
    verbraucht, 0€ frei**) – **finanzen.net zero: 750€** (angehoben von 600€;
    zuletzt bekannt 330,23€ ausgeschöpft, unter dem neuen Limit damit
    vorläufig 419,77€ frei – Brian prüft den aktuellen Verbrauch noch und
    bestätigt später) – **Trade Republic: 80€** (neu zugeordnet, noch
    keine Ausschöpfungs-Daten bekannt) – **Unitplus-Konto (Notgroschen-
    Konto, kein Wertpapier-Depot, separat vom Aktienanteil): 20€**. Zusammen
    150+750+80+20 = **1.000€, damit der volle Sparerpauschbetrag (Einzel-
    veranlagung) jetzt vollständig zugeordnet** – keine ungenutzte Freistellung
    mehr offen. **Praktische Konsequenz für das Head-to-Head-Ersatz-Gate:**
    ein Swap wird pro Broker gegen dessen aktuell noch freien
    Freistellungsbetrag geprüft (siehe oben, Werte bei Bedarf von Brian
    aktualisieren) – erst darüber hinausgehende Gewinne werden mit dem vollen
    effektiven Steuersatz (26,375%) gerechnet. Diese Zahlen sind
    Momentaufnahmen (Stand 30.08.2026) und sollten bei Bedarf von Brian
    aktualisiert werden, statt unbegrenzt fortgeschrieben zu werden.
- **Geografische Streuung (aktualisiert 2026-08-28, von Brian präzisiert):**
  Ziel-Verteilung wird ab jetzt **über das GESAMTE Portfolio berechnet, ETF und
  Einzelwerte zusammengelegt** (nicht mehr nur ex-ETF wie in der ersten Fassung
  vom selben Tag): **USA maximal 55%** des Gesamtportfolios (**absolute
  Obergrenze 60%** – wird diese gerissen, ist das ein sofortiger Warnhinweis im
  Wochenfazit, kein Toleranzbereich), **15-20% Europa/Großbritannien**,
  **10-15% Japan/Asien**, **Rest (Lateinamerika, Naher Osten/Israel, sonstige
  nicht anders zuordenbare Länder)** – aber nur, **wenn es dort tatsächlich
  interessante Kandidaten gibt**. Gibt es aktuell keine überzeugenden
  Lateinamerika-Kandidaten (siehe z.B. das dünne Ergebnis im Nicht-Index-
  Screening vom 2026-08-28), wird der dafür vorgesehene Prozentanteil
  stattdessen zusätzlich auf Europa/UK und Japan/Asien verteilt, nicht einfach
  der USA-Quote zugeschlagen. Wird im Wochenfazit/Gesamtübersicht als eigene
  Kennzahl geführt, nicht nur die Champions/Profi/Talent-Aufteilung.
  **Methodik-Lücke geschlossen (2026-09-04, aufgefallen beim ersten echten
  Portfolio-Regel-Check mit Live-Daten statt Schätzung):** Cellebrite DI Ltd.
  (Israel) passte bis dahin in KEINEN der vier Töpfe – weder USA/Nordamerika,
  Europa/UK noch Japan/Asien, und der vierte Topf hieß explizit nur
  "Lateinamerika/sonstige Länder", ohne dass "sonstige" bisher klar genug
  definiert war. Israel zählt ab jetzt explizit in den vierten
  ("Rest"-)Topf – geografisch/wirtschaftlich näher an Europa als an den
  anderen drei benannten Töpfen, aber kein eigener Israel-Topf nötig für
  eine einzelne Position. Cellebrites Anteil (Stand 2026-09-04: 6,20% des
  Gesamtportfolios) zählt damit zum "Rest"-Topf, der dadurch faktisch
  bereits ausgelastet ist – ein weiterer Nicht-LatAm/Nicht-Europa/Nicht-
  Asien-Kandidat sollte entsprechend zurückhaltender priorisiert werden,
  analog zur bestehenden Logik für überdehnte Töpfe.
  **Klarstellung zur Länder-Zuordnung (2026-08-30, von Brian entschieden):**
  Kanada-domizilierte Positionen (z.B. Constellation Software, Kraken Robotics)
  zählen für diesen Check zum **USA/Nordamerika-Topf**, nicht zu "Rest" – es
  gilt für diesen kombinierten USA/Nordamerika-Topf weiterhin exakt dieselbe
  55%-Ziel-/60%-Hartgrenze wie für die USA allein, keine separate oder
  aufgeweichte Grenze für Nordamerika. Israel-domizilierte Positionen (z.B.
  Cellebrite) zählen NICHT zu Europa/UK, obwohl geografisch/kulturell oft mit
  Europa assoziiert – sie werden dem "Rest"-Topf zugeschlagen.
- **Positionsgrößen-Limits (2026-08-28, von Brian festgelegt):** Die **größte
  Einzelposition darf max. 10% des Gesamtportfolios** ausmachen – Ausnahmen nur
  in absoluten Sondersituationen (z.B. eine Position wächst durch reine
  Kursrally organisch über die Grenze, ohne dass Brian nachgekauft hat; kein
  Freibrief für aktives Übergewichten). Umgekehrt soll **keine Position kleiner
  als 1% des Gesamtportfolios** sein – Positionen, die durch Kursverfall oder
  bewusst kleine Trace-Sizing (z.B. Scout-Talent-Positionen) darunter rutschen,
  werden im Wochenfazit als Grenzfall markiert (entweder aufstocken oder
  konsequent ganz raus, keine dauerhaften Mini-Reste).
  **Konkrete Positionsgrößen-Entscheidung an den Agenten delegiert
  (2026-08-30, von Brian erklärt: "Portfolio Aufbau, Positionsgröße werd ich
  dir alles überlassen"):** Brian möchte nicht mehr selbst festlegen, wie
  groß ein einzelner Kauf ausfällt – der Agent entscheidet die konkrete
  Stückzahl/den konkreten Betrag pro Empfehlung eigenständig, innerhalb der
  bereits bestehenden Leitplanken (Positionsgrößen-Limits 1-10% hier,
  Kategorie-Kapitalgewichts-Ziele, Sektor-/Regionen-Bänder, Phasenweise
  Skalierung nach Depotgröße, verfügbares Budget laut "Budget & Cashflow").
  Praktische Konsequenz: jede Kauf-/Verkaufsempfehlung nennt ab jetzt IMMER
  eine konkrete Stückzahl oder einen konkreten Betrag (nicht nur "Kaufen
  ja/nein") – kein Nachfragen bei Brian, wie viel er investieren möchte. Das
  ändert nichts an der Order-Ausführungs-Grenze (Abschnitt 1) – Brian
  entscheidet weiterhin, OB er der Empfehlung folgt, führt aber die
  Größen-Entscheidung selbst nicht mehr.
- **ETF-/Aktien-Verhältnis (2026-08-28, von Brian festgelegt):** Der
  **ETF-Anteil (Vanguard FTSE All-World) soll jederzeit mindestens 50% des
  Gesamtportfolios ausmachen**, mit dem **langfristigen Ziel 60% ETF / 40%
  Einzelwerte**. Das ist eine Erweiterung/Präzisierung zur bisherigen
  Cashflow-Regel (siehe "Budget & Cashflow" unten, 600€/Monat ETF-Sparplan) –
  hier geht es zusätzlich um den tatsächlichen Bestands-Anteil, nicht nur den
  monatlichen Sparplan-Cashflow.
- **Sektor-Streuung (2026-08-29, von Brian festgelegt):** Analog zur
  geografischen Streuung wird auch die Sektor-Verteilung über das **gesamte
  Portfolio (ETF + Einzelwerte zusammen)** berechnet. Ziel-Bandbreiten:
  **Technologie/Halbleiter ca. 30-38%** (2026-08-30 leicht angehoben, siehe
  "Renditeziel-Feinjustierung" in Abschnitt 1), **Finanzwesen ca. 20-25%**,
  **Gesundheitswesen ca. 10-15%**, **Industriewerte (allgemein) ca. 10-15%**,
  **Rest (übrige Sektoren, z.B. Konsum, Rohstoffe, Versicherung sofern nicht
  unter Finanzwesen gezählt, Sonstiges) ca. 5-10%**. Wird wie die geografische
  Streuung im Wochenfazit/Gesamtübersicht als eigene Kennzahl geführt und beim
  Portfolio-Regel-Check mitgeprüft. Für den ETF-Anteil gilt auch hier eine
  Näherungs-Aufteilung nach den globalen Sektorgewichten des Vanguard FTSE
  All-World, analog zur Länder-Näherung bei der geografischen Streuung.
  **Klarstellung zur Sektor-Zuordnung (2026-08-30, von Brian entschieden):**
  Broadridge Financial Solutions zählt als **Finanzwesen** (Finanzdienstleister/
  Fintech-Infrastruktur für Banken/Broker), NICHT als Technologie – trotz
  Software-/Tech-Charakter des Geschäftsmodells.
  **Anteilige Sektor-Zuordnung bei Mehrsegment-Unternehmen (2026-08-30, von
  Brian am Beispiel Hoya Corp. festgelegt):** Ein Unternehmen mit klar
  disclosed Umsatzverteilung über mehrere, fundamental unterschiedliche
  Segmente wird für die Sektor-Streuungs-Berechnung NICHT komplett dem
  Hauptsegment zugeschlagen, sondern der Positionswert wird anteilig nach der
  tatsächlichen Umsatzverteilung auf die betroffenen Sektor-Töpfe aufgeteilt.
  Beispiel Hoya Corp. (ca. 60% Umsatz Technologie/Halbleiter [Photomasken-
  Rohlinge etc.], ca. 30% Gesundheitswesen [MedTech], Rest sonstige/nicht
  zugeordnet): bei einer Depot-Aufnahme fließen ca. 60% des Positionswerts in
  den Technologie-Topf und ca. 30% in den Gesundheitswesen-Topf ein, statt
  100% unter Technologie zu verbuchen. Faustregel: eine Aufteilung erfolgt,
  wenn ein Nebensegment einen nicht-trivialen Anteil (grob ab ca. 15-20%)
  des Umsatzes ausmacht und öffentlich disclosed ist (Geschäftsbericht/
  Segmentberichterstattung) – bei einem klar dominanten Einzelsegment
  (>85-90%) bleibt es bei der einfachen Ein-Sektor-Zuordnung wie bisher. Die
  Kurzthese/Kategorie-Tabelle (Watchlist/Depot) kann weiterhin ein
  Hauptsegment als Kurzbezeichnung führen (z.B. "Hoya – Optik/Halbleiter-
  Photomasken & MedTech") – nur die Sektor-Streuungs-PROZENTRECHNUNG im
  Portfolio-Regel-Check nutzt den anteiligen Split. Gilt analog auch für die
  geografische Streuung, falls ein Unternehmen Umsatz disclosed über mehrere
  Regionen verteilt und nicht eindeutig einer Region zuzuordnen ist.
- **Phasenweise Skalierung nach Depotgröße (2026-08-28, von Brian festgelegt):** Die
  volle 20-Positionen-Struktur ist ein Ziel für die Zukunft, kein Sofort-Zwang. Bei
  aktueller Depotgröße fährt Brian bewusst mit **10-15 Positionen** (Budget-/
  Investitionssumme aktuell begrenzt) statt sofort alle 20 Slots zu befüllen.
  **Sobald die Gesamt-Depotgröße ca. €50.000 erreicht, werden die restlichen Slots
  freigeschaltet** und das Depot darf Richtung 20 Positionen wachsen. Bis dahin gilt
  bei jedem Kaufvorschlag ein strengerer Maßstab ("nur die überzeugendsten Ideen"),
  nicht "jeder Slot muss gefüllt sein".
  **Positionsanzahl an den Agenten delegiert (2026-08-30, von Brian erklärt:
  "wenn du der Meinung bist, dass du z.B. in welcher Marktphase auch immer
  nur weniger als 10 Positionen haben möchtest, dann ist es deine
  Entscheidung"):** Die obigen Zahlen (10-15 jetzt, bis zu 20 ab €50.000)
  sind ab jetzt eine **Obergrenze/Orientierung, kein Mindest-Ziel** – wie
  viele Positionen das Depot TATSÄCHLICH hält, entscheidet der Agent
  eigenständig nach Marktlage, nicht Brian und nicht eine feste Zahl im
  Dokument. Erkennt der Agent eine Marktphase, in der deutlich weniger
  Positionen (auch klar unter 10) angemessener sind – z.B. weil aktuell zu
  wenige Kandidaten das Strategie-Fit-Gate und den Qualitäts-Anspruch
  wirklich überzeugend bestehen, eine breite Überbewertung über mehrere
  Sektoren erkennbar ist, oder ein bewusst defensiverer/konzentrierterer
  Ansatz mit mehr Cash-Reserve gerade die bessere Kapitalerhalt-Entscheidung
  ist (siehe Abschnitt 1, Zweites Grundziel) – ist das ausdrücklich erlaubt
  und erwünscht, keine Abweichung, die gerechtfertigt werden muss. Diese
  Entscheidung wird im Wochenfazit transparent benannt (aktuelle
  Positionsanzahl + kurze Begründung, warum bewusst mehr/weniger als die
  Orientierungs-Zahlen), damit Brian nachvollziehen kann, warum das Depot
  gerade so aussieht wie es aussieht. Die harten Leitplanken bleiben davon
  unberührt (Positionsgrößen-Limits 1-10%, Kategorie-Kapitalgewichte,
  Sektor-/Regionen-Bänder, ETF-/Aktien-Verhältnis) – delegiert ist die
  Positions-ANZAHL, nicht die übrigen Struktur-Regeln.
- **Praktische Konsequenz für die Pipeline:**
  - SCHRITT [2] KATEGORISIERUNG (siehe Pipeline unten) muss nicht nur TMR-vs-Scout
    entscheiden, sondern auch, in welche der drei Kategorien (Champions / Profi /
    Talent) ein Kandidat fallen würde.
  - SCHRITT [5] REPORT sollte bei jedem neuen Kandidaten-Vorschlag ausweisen, in
    welche Kategorie er fallen würde und ob dort überhaupt noch Platz ist (siehe
    aktueller Überhang oben).
  - Jetzt, wo das Depot vollständig erfasst ist, ist ein einmaliger "Depot-Cleanup"-
    Report der logische nächste Schritt: welche der 28 aktuellen Werte am ehesten
    raus sollten, um auf die Ziel-Struktur zu kommen (nach TMR-Rating/Qualität
    sortiert). Größter Hebel liegt im Champions-Bucket (deutlich mehr Kandidaten als
    die 8-10 Zielplätze). Noch nicht gebaut – siehe Offene Punkte.
  - **Tiefe für den Cleanup-Screening-Durchgang (2026-08-23, wegen Laufzeit von
    Brian angefragt):** Der ServiceNow-Testlauf mit FULL DEEP DIVE + echtem 3-fach-
    Cross-Check hat pro Kandidat 30-40 Minuten gebraucht. Für den ersten Durchgang
    durch alle Champions-Kandidaten ist das zu langsam. Default ab jetzt: erster
    Screening-Pass mit **TMR QUICK FILTER** (DNA-Check + Konfidenz + Rating, kein
    DCF, schnellere Websuche) – der volle FULL-DEEP-DIVE-3-fach-Cross-Check (wie bei
    ServiceNow) bleibt reserviert für Grenzfälle/Uneinigkeit oder wenn Brian explizit
    danach fragt.

### Depot-Restrukturierung (2026-08-28, von Brian initiiert, vollständig erfasst)

Brian hat am 27.08.2026 12 Positionen komplett verkauft und beginnt, gezielt in
Titel mit **sehr hohem Upside-Potenzial bzw. Kandidaten für einen zukünftigen
"Big Player"** umzuschichten. Das ist ein bewusster strategischer Schwenk weg vom
bisherigen, stark Champions-lastigen Depot (Wochenfazit vom 28.08.: 19 von 28
Positionen Champions, deutlich über dem 8-10-Zielband) hin zu mehr Talent-Gewicht.

**Verkäufe (alle 27.08.2026, vollständiger Exit, Details/Kurse in den jeweiligen
`depot/`-Dateien):** Itochu Corp. (11,11€), Stryker Corp. (279,75€), Cintas Corp.
(174,52€), Visa Inc. (326,40€), Grab Holdings (3,118€), Amazon (220,75€),
Alphabet A (291,65€), Intuit Inc. (294,70€), Keyence Corp. (439,90€), S&P Global
Inc (378,15€), Netskope (12,76€), Waste Management (187,35€). Davon 10 aus dem
Champions-Bucket, 2 aus Talent (Grab, Netskope).

**Neukäufe (Depot finanzen.net zero, Kategorie Talent, Scout-Pfad-Analyse noch
ausstehend):** Kraken Robotics Inc., 300 Stk. @ 3,50€ (24.08.2026, €1.050
investiert); Rocket Lab USA, Inc., 10 Stk. @ 55,40€ (28.08.2026, €554 investiert).

**Auswirkung auf Kategorie-Füllstand:** Champions fällt von 19 auf **9** – jetzt
sauber im 8-10-Zielband. Talent bleibt bei 5 (Grab/Netskope raus, Kraken
Robotics/Rocket Lab rein). Profi unverändert bei 4. **Neuer Gesamtstand: 18
Einzelwerte ohne ETF** (vorher 28). Nächste Schritte: (1) Kraken Robotics und
Rocket Lab über den Scout-Pfad analysieren, (2) geografische Streuung (Abschnitt 3)
mit dem neuen Stand neu berechnen, (3) nächstes Wochenfazit spiegelt den
bereinigten Stand wider.

### Budget & Cashflow (2026-08-28, von Brian festgelegt)

Laufende monatliche Mittelzuflüsse, als feste Rahmengröße für Sizing-/Cash-
Allokations-Überlegungen (siehe Offene Punkte, Cash-Allokations-Logik):

- **Scalable Capital: €800/Monat per Dauerauftrag**, davon:
  - **€600/Monat** per Sparplan in den **Vanguard FTSE All-World (Acc.)** ETF
  - **€200/Monat** verbleibt als **Cashreserve auf dem Verrechnungskonto**
    (2026-08-29, von Brian präzisiert: bewusst zurückgelegt für einen
    möglichen **Einmalkauf bei einer größeren Marktkorrektur** – kein
    beliebiger Puffer ohne Zweck, sondern gezielte "Trockenpulver"-Reserve).
    **Stehende Freigabe von Brian:** Falls ich (Jarvis) einschätze, dass diese
    Reserve auf absehbare Zeit nicht für einen Korrektur-Einmalkauf gebraucht
    wird (z.B. weil aktuell keine sinnvolle Korrektur-Gelegenheit erkennbar
    ist), darf ich Brian aktiv vorschlagen, das angesammelte Geld stattdessen
    auf das finanzen.net-zero-Konto umzuschichten, um dort konkrete Käufe zu
    ermöglichen (z.B. um die 500€-Gebührenschwelle zu erreichen, siehe unten).
    Das ist ein **Vorschlagsrecht, keine automatische Umbuchung** – Brian
    entscheidet am Ende, ich soll es nur proaktiv ansprechen, wenn ich es für
    sinnvoll halte.
    **Cross-KI-Check zu "Reserve vs. ETF-Einmalkauf" (2026-08-30, Brians
    Frage, alle drei einig):** Brian hat gefragt, ob die angesammelte Reserve
    (aktuell gut 1.000€) nicht besser sofort als ETF-Einmalkauf investiert
    statt als Cash gehalten werden sollte. Jarvis, Jack und Conan sind sich
    einig: **aktuell nicht.** Begründung – die Reserve ist keine
    Rendite-Position, sondern eine Optionalität ("Munition, keine
    Assetklasse", Conan) für eine echte Marktkorrektur; ein Einmalkauf
    ausgerechnet jetzt (Regime: Neutral mit Vorsicht-Bias, siehe Abschnitt 1)
    wäre zudem prozyklisch zum ungünstigen Zeitpunkt. Zwei konkrete Auslöser,
    ab denen die Reserve (teilweise) eingesetzt wird: **(a) Korrektur** –
    S&P 500/MSCI World fällt ≥7-10% vom Hoch oder der VIX schlägt spürbar
    aus → gezielter Nachkauf in Champions/Profi-Qualität bzw. Sonder-Tranche
    in den ETF; **(b) Regime-Wechsel** – das System stuft wieder auf breites,
    gesundes Risk-on um → schrittweise Einspeisung in den laufenden
    ETF-Sparplan statt Einmalkauf auf aktuellem Niveau. Ergänzend Conans
    Vorbehalt: die Reserve soll nicht unbegrenzt wachsen – **Cash-Cap von
    3-5% des Gesamtportfolios**; wird dieser überschritten, ohne dass eine
    Korrektur/ein Regime-Wechsel eingetreten ist, fließt der Überschuss in
    den normalen Anlageplan (ETF-Sparplan) statt als Cash liegen zu bleiben.
    Bis dahin gilt: 200€/Monat weiter ansammeln, Funktion bleibt
    Optionalität, keine Umwidmung zu einem regulären Investment.
  - Der bisherige Bank-Central-Asia-(BBCA)-Sparplan (100 €/Monat, siehe
    `depot/scalable-capital.md`) wurde **gestoppt** (kein Neukauf mehr, bestehende
    Position bleibt zunächst unverändert im Depot).
- **finanzen.net zero: €320/Monat**
- **Ad-hoc-Nachschuss möglich:** gelegentlich zusätzlich €100-200, wenn ein
  Kandidat es rechtfertigt – kein fester Bestandteil des Regel-Budgets.
- **Kostenstruktur finanzen.net zero (2026-08-29, von Brian klargestellt):**
  Ab einer Ordersumme von **≥500€ keine Ordergebühr**, bei einer Ordersumme
  **<500€ fällt 1€ Ordergebühr** an. **Praktische Konsequenz:** Das reguläre
  Monatsbudget von €320/Monat liegt UNTER dieser Schwelle – ein einzelner
  monatlicher Kauf in dieser Größenordnung würde also die 1€-Gebühr auslösen
  (≈0,31% der Ordersumme). Bei künftigen Sizing-/Kauf-Empfehlungen für
  finanzen.net-zero-Positionen deshalb mitdenken, ob es sinnvoller ist,
  (a) die 1€ Gebühr einfach in Kauf zu nehmen (bei diesem Betrag ökonomisch
  meist vernachlässigbar), oder (b) mehrere Monatsraten zu bündeln (z.B. 2
  Monate à 320€ = 640€, über der 500€-Schwelle) und seltener, dafür
  gebührenfrei zu kaufen. Keine pauschale Regel – abhängig davon, ob Brian
  eher zeitnahen Einstieg oder Gebührenoptimierung priorisiert; im Zweifel
  bei einer konkreten Kaufempfehlung kurz ansprechen.
- Trade Republic und Smartbroker+ haben laut bisherigem Stand keine eigenen
  laufenden Sparpläne/Daueraufträge (nur Einzelkäufe wie bei Allianz SE/WM
  historisch, bzw. HawkEye 360 als Einzelposition) – bei Bedarf mit Brian
  gegenchecken, falls sich das ändert.
- **Kostenstruktur Scalable Capital (2026-09-01, von Brian bestätigt):**
  Sparpläne sind **grundsätzlich kostenlos**, unabhängig von der
  Ordersumme – anders als bei finanzen.net zero gibt es hier keine
  500€-Schwelle zu beachten. Betrifft den laufenden Vanguard-FTSE-All-World-
  Sparplan direkt.
- **Kostenstruktur Trade Republic (2026-09-01, von Brian bestätigt):**
  **1€ pro Order**, unabhängig von der Ordersumme (kein Schwellenwert wie
  bei finanzen.net zero). Bei künftigen Kauf-/Nachkauf-Empfehlungen für
  Positionen auf Trade Republic (aktuell nur Allianz SE, Sparplan-artige
  monatliche Bruchstück-Käufe) mitdenken – bei den bisher üblichen kleinen
  Raten ist die 1€-Gebühr prozentual höher als bei größeren Einzelkäufen,
  ähnliche Bündelungs-Überlegung wie bei finanzen.net zero möglich, falls
  Brian das priorisiert.
- **Smartbroker+ Kostenstruktur:** noch nicht von Brian mitgeteilt – bei
  Bedarf nachfragen, sobald dort eine Kauf-/Nachkauf-Empfehlung ansteht
  (aktuell nur HawkEye 360, kein Nachkauf-Kandidat laut laufender
  Scout-Bewertung).

Das ist das **vorgegebene Budget**, an dem sich künftige Kaufvorschläge/Sizing-
Empfehlungen realistisch orientieren sollen – nicht nur am theoretischen
Sizing-Tier (1-4), sondern auch daran, ob das monatliche Budget einen Kauf in der
empfohlenen Größenordnung überhaupt hergibt, bzw. ob dafür mehrere Monate
Ansparzeit oder ein Ad-hoc-Nachschuss nötig wären.

**Cash-Reserven – aktueller Stand (2026-08-29, von Brian gemeldet):**
- **Scalable Capital (Korrektur-Reserve):** 447,14 €
- **finanzen.net zero (Verrechnungskonto):** 1,32 € (für September bereits
  eingeplant/verbraucht; die reguläre Sparsumme fließt erst wieder ab Oktober
  neu ein)

Konsequenz für die 500€-Gebührenschwelle (siehe oben): Auf finanzen.net zero
steht aktuell praktisch kein freies Cash für einen eigenständigen Kauf zur
Verfügung – ein gebührenfreier Kauf (≥500€) wäre dort frühestens möglich, wenn
sich über Oktober/November wieder ausreichend Sparsumme angesammelt hat, oder
falls Brian einen Teil der Scalable-Korrektur-Reserve (447,14 €) gezielt
rüberschickt (siehe Umschicht-Option oben). Dieser Stand ist eine Momentaufnahme
und sollte bei der nächsten Cash-Meldung von Brian aktualisiert werden, statt
unbegrenzt fortgeschrieben zu werden.

## 4. Pipeline (Gesamtablauf)

```
[1] UNIVERSUM-SCREENING (günstig, automatisiert, kein KI-Modell nötig)
     → breiter quantitativer Scan (Kursdaten/Fundamentaldaten-Feed, z.B. Yahoo Finance)
     → grobe Kennzahlen-Filter angelehnt an TMR-DNA / Scout-Triage
       (Wachstum, Marge-Trend, Bewertung grob, keine offensichtlichen Red Flags)
     → **Sektorspezifische Bewertungsbänder statt Pauschal-KGV/KUV
       (2026-08-30, aus der Cross-KI-Diskussion zum Screening-Prozess, siehe
       Agent-Playbook-Archiv-Diskussionen.md Abschnitt 11):** ein pauschales KGV-/KUV-Limit über das gesamte
       Universum sortiert Qualitäts-Highflyer (z.B. Software mit sehr hoher
       Bruttomarge) zu früh aus und lässt gleichzeitig Value-Traps in
       margenschwachen Branchen durch. Stattdessen branchentypische
       Bewertungslogik: Tech/SaaS primär über EV/FCF und PEG (inkl.
       FCF-Wachstum), Industrie/zyklische Werte über EV/EBITDA und ROIC vs.
       WACC.
     → Ergebnis: Kandidatenliste (klein, z.B. 10-40 Namen), nicht 3000 Ticker
     → **Aktives Sourcing zusätzlich zum passiven Scan (2026-08-30, aus der
       Cross-KI-Diskussion zum Screening-Prozess, siehe Agent-Playbook-Archiv-Diskussionen.md Abschnitt 11):** Der
       breite Feed-Scan wartet nur ab, was er hergibt. Ergänzend läuft ein
       gezielter Blick auf natürliche Kandidaten-Quellen, die im reinen
       Zahlen-Scan nicht auffallen: Zulieferer-/Kunden-Netzwerk bestehender
       Champions-Positionen (wer profitiert vom Wachstum von z.B.
       ServiceNow/Constellation Software/MercadoLibre), Spin-offs, IPO-
       Lockup-Abläufe, auffälliges Insider-Buying, 13F-Trends
       (institutionelle Positionsänderungen), Analysten-Schätzungsrevisionen.
       **Realistische Umsetzung ohne teure Datenfeeds (2026-08-30,
       Feinjustierungs-Runde 3, siehe Agent-Playbook-Archiv-Diskussionen.md Abschnitt 11):** Insider-Buying über
       kostenlose Quellen (SEC EDGAR Form 4, alternativ OpenInsider), aber
       ausdrücklich nur als Bestätigungs-/Prioritäts-Signal, kein
       eigenständiger Kauf-Trigger – relevant sind Cluster-Käufe (mind. 2
       Führungskräfte/Direktoren kaufen zeitnah echt am offenen Markt aus
       eigenen Mitteln, idealerweise nach einem Kursrückgang), planmäßige
       10b5-1-Transaktionen zählen ausdrücklich NICHT als Signal. 13F-Daten
       über kostenlose Aggregatoren (z.B. WhaleWisdom, Dataroma) NICHT als
       laufende Entdeckungsquelle (wegen der Meldeverzögerung von i.d.R.
       45 Tagen als Frühsignal ungeeignet), sondern nur vierteljährlich und
       nur als nachgelagerter Validierungs-Check bei bereits durch das
       normale Screening interessant gewordenen Kandidaten ("haben
       anerkannte Qualitätsinvestoren ihre Position hier neu aufgebaut oder
       ausgebaut?").
       Zusätzlich läuft bewusst ein GEGENLÄUFIGER Such-Kanal parallel zum
       klassischen Wachstums-Scan: ein "Fallen-Angels/Neglected-Quality"-Scan
       (Kriterien z.B. -25% bis -50% vom Hoch, aber langfristig starke
       Bilanz, FCF noch intakt oder nur temporär schwächer, stabiler/
       steigender Marktanteil, eher temporärer als struktureller Gegenwind).
       Begründung: ein reiner Wachstums-/Qualitäts-Scan findet zwangsläufig
       überwiegend bereits vom Markt entdeckte Aktien.

[1.5] KILL-GATES + OPPORTUNITY-SCAN (2026-08-30, neu, aus der Cross-KI-
      Diskussion zum Screening-Prozess, siehe Agent-Playbook-Archiv-Diskussionen.md Abschnitt 11 – ersetzt die
      bisherige rein größen-/alters-basierte TMR-vs-Scout-Vorsortierung)
     → **Universelle Kill-Gates (gelten für ALLE Kandidaten, unabhängig vom
       späteren Pfad):** nur wirklich toxische Fälle werden hier
       aussortiert – offensichtliche Bilanzbetrug-/Accounting-Red-Flags,
       Going-Concern-Zweifel, extreme Verwässerung, akute
       Insolvenzgefahr/existenzbedrohliche Bilanz, offensichtlich
       uninvestierbare Situationen (z.B. Delisting-Risiko). Bewusst NICHT
       hier: normale Qualitätskennzahlen wie ROIC/FCF-Historie – die
       würden junge, gerade erst gut werdende Firmen ("Quality in
       Formation") vorzeitig aus dem Prozess werfen.
     → **Quality-of-Earnings-/Cash-Conversion-Gate:** vor dem eigentlichen
       Deep-Dive wird grob geprüft, ob der ausgewiesene Gewinn zur Kasse
       passt (Operating Cashflow / Net Income ≈ 1), ob es auffällige
       Wirtschaftsprüfer-Wechsel, aggressive Non-GAAP-Anpassungen oder
       ungewöhnliche Insider-Verkaufsspitzen gibt. Auffälligkeiten hier
       führen nicht automatisch zum Ausschluss, aber zu einem expliziten
       Warnhinweis, der in den Deep-Dive mitgegeben wird.
     → **Einordnung in vier Buckets statt eines einzelnen Scores** (ein
       einzelner 0-100-Score würde bei mehrdimensionalen Profilen falsche
       Präzision vortäuschen):
       - **A – Compounder Candidate:** bereits bewiesene ökonomische
         Qualität (Wachstum, steigende Margen, FCF positiv/stark
         zunehmend, hohe Kapitalrendite, geringe Verschuldung, Pricing
         Power) → i.d.R. TMR-Pfad, dort gelten die vollen, harten
         Qualitätskriterien.
       - **B – Quality in Formation:** Wachstum über historischem
         Durchschnitt, Margen verbessern sich gerade, FCF kippt gerade ins
         Positive, ROIC verbessert sich deutlich, Wettbewerbsvorteil aber
         noch nicht vollständig bewiesen → Scout oder TMR je nach
         Reifegrad, geprüft über eine Rule-of-40-/Sales-Efficiency-Logik
         (Umsatzwachstum + FCF-Marge, bzw. bei noch unprofitablen Firmen
         ersatzweise Umsatzwachstum >25% UND Bruttomarge >65% als Beleg für
         Skalierbarkeit) statt über die harten TMR-Kennzahlen. Genau dieser
         Bucket verhindert, dass das Screening ausschließlich die
         heutigen, bereits offensichtlichen Gewinner findet.
       - **C – Mispricing/Re-Rating Candidate:** nicht unbedingt schnell
         wachsend, aber Bewertung stark gefallen bei stabilen
         Fundamentaldaten, robustem FCF, sauberer Bilanz und eher
         temporärem statt strukturellem Gegenwind → TMR-Deep-Dive. Dient
         als Gegengewicht zum sonst automatisch wachstumslastigen
         Screening.
       - **D – Speculative Optionality:** sehr junge/kleine Firma, großes
         Marktpotenzial, frühe Technologie, noch keine Profitabilität,
         aber messbare operative Fortschritte → Scout-Pfad, ausdrücklich
         NICHT durch dieselben Profitabilitätsfilter wie TMR geprüft.
     → **Inflection-Signal (2026-08-30, Feinjustierungs-Runde 3, siehe
       Agent-Playbook-Archiv-Diskussionen.md Abschnitt 11):** ergänzender, leichtgewichtiger Priorisierungs-Layer
       – KEIN Hard Gate, KEIN eigener 0-100-Score. Für 6-8 Dimensionen
       (Umsatzwachstum, Bruttomarge, operative Marge, FCF, ROIC, EPS,
       Guidance, Analystenschätzungen) wird jeweils nur grob eingeordnet:
       ↑ beschleunigt sich / → stabil / ↓ verschlechtert sich. 3 oder mehr
       positive Inflections → Prioritätsbonus im weiteren Screening,
       mehrere negative → niedrigere Priorität, keine klare Inflection →
       neutral (führt NICHT zum Ausschluss – ein hervorragendes
       Unternehmen ohne aktuelle Inflection bleibt ein gültiger Kandidat).
       Unterschied zu Bucket B "Quality in Formation": Bucket B fragt "wie
       gut wird die Qualität gerade", das Inflection-Signal fragt "wird die
       Entwicklung gerade schneller oder langsamer".
     → **"Warum jetzt?"-Filter (Pflichtfeld je Kandidat):** jeder Kandidat
       muss einen konkreten aktuellen Auslöser benennen können (z.B.
       Margen-Inflection, neues Produkt/neuer Markt, Turnaround,
       regulatorischer Wandel, Marktanteilsgewinn, Bewertungsreset,
       Spin-off, Insider-Buying, M&A, Kapazitätsausbau, neue Technologie,
       Konsolidierung einer fragmentierten Branche). Lautet die Antwort nur
       "gute Firma, wächst schnell" ohne konkreten Katalysator, bekommt der
       Kandidat keinen Analyse-Prioritätsbonus – er kann trotzdem gut sein,
       es gibt aber keinen Grund, JETZT knappe Analysezeit darauf zu
       verwenden. **Verschärfung (Runde 3):** "Warum jetzt?" gilt nur als
       erfüllt, wenn es durch mindestens ein tatsächliches
       Beschleunigungs-Signal aus dem Inflection-Signal oben belegt wird
       (z.B. Marge/FCF beschleunigen sich, Guidance/Analystenschätzungen
       wurden in den letzten 90 Tagen angehoben, sequenzielles
       Wachstum beschleunigt sich) – eine reine Behauptung ohne Beleg
       reicht nicht mehr.
     → **"Warum gewinnt?"-Feld, getrennt vom "Warum jetzt?" (2026-08-30,
       Runde 3, Conans Ergänzung):** ein kurzfristiger Katalysator lenkt
       zwar Aufmerksamkeit auf eine Aktie, verbessert aber nicht
       automatisch den langfristigen Compounder-Case. Deshalb zweites,
       getrenntes Pflichtfeld: warum sollte dieses Unternehmen über 5-10
       Jahre ökonomisch besser dastehen als seine Wettbewerber (Moat,
       Skaleneffekte, Netzwerkeffekte, Kostenvorteil, Marktstruktur)?
       Verhindert, dass das Screening zu einem reinen
       Kurzfrist-Katalysator-Scanner wird, der Aktien mit gutem Timing,
       aber schwacher langfristiger These bevorzugt.
     → **Referenzklassen-/Base-Rate-Filter gegen Hype-Profile:** ergänzend
       zur Frage "wie sehen die Zahlen aus?" wird gefragt, wie viele
       Unternehmen mit einem vergleichbaren Profil (Sektor, Wachstums-/
       Margenkombination) historisch tatsächlich zu langfristigen
       Compoundern wurden. Ein bekanntes Hype-Profil (z.B. "KI-
       Infrastruktur-Firma mit hohem Wachstum") braucht überdurchschnittlich
       gute Merkmale, um trotzdem als Investment Case zu gelten – reine
       Zugehörigkeit zum Hype-Profil reicht nicht.
     → **Grober Korrelations-/Faktor-Check (frühe, noch nicht finale
       Stufe):** ein erster, groben Abgleich, ob ein Kandidat trotz
       unterschiedlichem Sektor-Bucket stark mit bestehenden Positionen
       über denselben Makro-Treiber korreliert (z.B. Zinssensitivität,
       KI-Capex-Zyklus). Dient hier nur der Priorisierung; der
       vollständige, verbindliche Depot-Fit-Check (Duplikation, Sektor-/
       Geo-Streuung, Kapitalgewicht) bleibt wie bisher erst nach dem
       Deep-Dive Pflicht (siehe Abschnitt 3).

[2] KATEGORISIERUNG
     → pro Kandidat: Bucket A (Compounder Candidate) / Bucket C
       (Mispricing-Re-Rating) → TMR-Pfad, dort gelten die vollen harten
       Qualitätskriterien (u.a. mehrjährig FCF-positiv, ROIC-Schwelle,
       klare Preissetzungsmacht)
                      Bucket B (Quality in Formation) / Bucket D
       (Speculative Optionality) → Scout-Pfad, dort gelten die weicheren,
       wachstumsbezogenen Ersatzkriterien aus [1.5] statt der TMR-Kennzahlen
     → **Ersetzt die bisherige rein größen-/alters-basierte Heuristik
       ("etabliert/Large-Mid-Cap" vs. "jung/klein/spekulativ") durch das
       Bucket-Modell aus [1.5]:** eine schnell skalierende, bereits
       profitable Nischenfirma landet damit nicht mehr automatisch im
       Scout-Pfad, nur weil sie klein/jung ist, wenn ihre Fundamentaldaten
       (Bucket A) das nicht rechtfertigen – und umgekehrt wird eine junge
       Firma mit noch schwachem ROIC nicht automatisch von TMRs harten
       Kennzahlen aussortiert, wenn sie klar in Bucket B gehört.
     → **Fallback-Regel bei widersprüchlichen/fehlenden Reifemetriken
       (2026-09-03, Conans Vorschlag aus dem 3-KI-System-Audit, macht den
       bisher subjektiven Begriff "Reifegrad" operational):** die
       Bucket-Zuordnung ist nicht immer eindeutig – z.B. Umsatzwachstum
       >25% und Bruttomarge >65% (Bucket-B-typisch), aber Rule-of-40/
       Sales-Efficiency nicht verfügbar oder negativ. Für diesen Fall gilt
       eine klare Rangfolge statt freier Einschätzung: **TMR nur, wenn
       ausreichend Historie/Datenqualität vorhanden UND Rule-of-40 bzw.
       Sales-Efficiency-Kriterien erfüllt sind. Scout, wenn nur Wachstum+
       Bruttomarge erfüllt sind, aber die Monetarisierungs-/Effizienzqualität
       (noch) nicht belastbar geprüft werden kann – also im Zweifel Scout,
       nicht TMR.** Sind Umsatzbasis, Wachstum oder Bruttomarge selbst
       nicht sinnvoll messbar (z.B. Pre-Revenue, Biotech ohne Umsatz,
       Banken/Rohstofffirmen mit branchenuntypischer Kennzahlenlogik),
       gehört der Fall weder klar zu TMR noch zu Scout – dann manuelle
       Klärung durch Jarvis vor dem Deep-Dive, nicht automatische
       Zuordnung zu einem der beiden Pfade.
     → (Auto-Detection-Logik aus den Prompts selbst nutzen, siehe TMR "Analyse-Tiefe"
        / Scout "Sektor-Override-Detection")
     → **Alle drei KIs bekommen ab sofort alle drei Methodik-Dateien
       (2026-09-05, von Brian gefordert: "alle Agenten Zugriff auf alle 3
       Dateien haben, um viele Sichtweisen bei einer Analyse
       herauszufinden... alle bekommen die gleiche Voraussetzung, die
       gleichen Analysetools").** Bisher bekam Jack/Conan über die Bridge
       NUR die eine, per Bucket geroutete Methodik-Datei (TMR ODER Scout)
       zugeteilt – Jarvis las zwar alle drei, aber Jack/Conan sahen jeweils
       nur einen Ausschnitt des Werkzeugkastens. Ab sofort gilt: bei JEDER
       vollständigen Einzelanalyse (Quick Filter und Full/Deep-Dive) werden
       ALLE DREI Dateien (`jack-moat-reaper-v11.7.md`/TMR,
       `conan-the-scout-v1.12.md`/Scout, `jack-technical-analyst-v1.9.md`/TA)
       an Jarvis (liest sie ohnehin selbst), Jack UND Conan gegeben – nicht
       mehr nur die eine, laut Bucket "richtige". **Was sich dadurch NICHT
       ändert:** die Bucket-Zuordnung (TMR-Pfad vs. Scout-Pfad, siehe oben)
       bleibt bestehen und bestimmt weiterhin, welches Rating das
       OFFIZIELLE/PRIMÄRE Ergebnis für Kategorisierung, Sizing und
       Kurz-Fazit ist – TMR-Kennzahlen werden nicht plötzlich auf eine
       Pre-Revenue-Firma angewendet oder umgekehrt. Was sich ändert: jede
       KI hat jetzt zusätzlich die VOLLE Perspektive der jeweils anderen
       Methodik zur Verfügung und kann explizit benennen, wenn sie aus
       dieser zusätzlichen Linse eine relevante Beobachtung ableitet (z.B.
       Conan bringt bei einem TMR-Fall trotzdem einen Wachstumsqualitäts-
       Einwand ein, oder Jack/TMR bemerkt bei einem Scout-Fall eine bereits
       messbare Preissetzungsmacht) – das macht die Cross-Check-Vielfalt
       größer, ohne die Bucket-Logik selbst aufzuweichen. TA bleibt wie
       bisher bei jeder Einzelanalyse Pflicht (war schon immer Teil aller
       drei Dateien für jede Analyse, jetzt nur explizit auch an Jack/Conan
       mitgegeben statt implizit vorausgesetzt). **Technische Konsequenz
       (siehe HANDOVER.md 10.10):** die drei Dateien zusammen sind
       deutlich länger als eine einzelne Methodik-Datei – bei Gemini/Jack
       ist `enable_search` bei diesem kombinierten Mega-Prompt IMMER auf
       `False` zu setzen (bekanntes Kontextlängen-/Abbruch-Problem, siehe
       dort), bei Conan/ChatGPT ist das nicht nötig.
     → zusätzlich: Kategorie-Zuordnung nach Depot-Ziel-Struktur (siehe Abschnitt 3):
       Champions / Profi / Talent – inkl. Platz-Check pro Kategorie
     → **AUTOMATISCHE Kategorie-Zuordnung bei KAUFEN-Ergebnis (2026-08-29,
       von Brian gefordert):** Kommt aus dem 3-fach-Cross-Check ein
       Kauf-taugliches Ergebnis (TMR: KAUFEN, Scout: WATCHLIST-ELITE/
       BEOBACHTEN-STARK), wird NICHT nur "irgendeine" Kategorie notiert,
       sondern automatisch und nach den geschärften Kriterien aus
       Abschnitt 3 hergeleitet, in welche Kategorie (Champions/Profi/Talent)
       der Kandidat gehört – bei Talent zusätzlich der Zeithorizont-Tag
       ("Talent (langfristig)" vs. "Zock/Trade", siehe Abschnitt 3) – samt
       kurzer Begründung (welches Kriterium – Monopolstellung/Marge/
       Wachstum/Momentum – den Ausschlag gibt). Zusätzlich wird geprüft, ob
       in der jeweiligen Kategorie nach dem Kapitalgewichts-Ziel (Abschnitt
       3, Champions 35-45%/Profi 20-30%/Talent 25-40%) überhaupt noch
       "Platz" ist, nicht nur nach reiner Positionsanzahl. Das Ergebnis
       dieser automatischen Einordnung ist Pflichtbestandteil des
       Kurz-Fazits (Pipeline-Schritt 5), nicht optional. **Ist die
       Zielkategorie voll (kein "Platz" mehr), greift zusätzlich das
       "Head-to-Head-Ersatz-Gate gegen die schwächste Depot-Position"
       (2026-08-30, siehe Abschnitt 3) BEVOR eine tatsächliche
       Kaufempfehlung ausgesprochen wird – Qualitäts-Vergleich gegen die
       schwächste Position der Kategorie UND Portfolio-Mehrwert-Check UND
       Sektor-/Kapitalgewichts-Rahmen-Check, nicht nur "ist er besser als
       die schwächste Position".**
     → **Frische-Gate vor dem finalen Kauf (2026-08-30, aus der Cross-KI-
       Diskussion zum Screening-Prozess, siehe Agent-Playbook-Archiv-Diskussionen.md Abschnitt 11):** Liegt
       zwischen dem ursprünglichen Screening/Deep-Dive und der tatsächlichen
       Kaufausführung durch Brian spürbar Zeit (z.B. mehrere Wochen), werden
       Kernzahlen und Live-Kurs vor dem Kauf kurz aktualisiert, statt auf
       Basis veralteter Screening-Daten zu kaufen – Markt und
       Fundamentaldaten können sich in der Zwischenzeit verschoben haben.
       **Zweistufig ergänzt (2026-08-30, Feinjustierungs-Runde 3):** schon
       im frühen Screening ([1.5]) wird das Datenalter je Kandidat sichtbar
       gemacht (🟢 unter 90 Tage / 🟡 90-180 Tage / 🔴 über 180 Tage bei den
       zugrunde liegenden Fundamentaldaten), damit kein Kandidat auf Basis
       ein halbes Jahr alter Zahlen unbemerkt durch den ganzen Prozess
       läuft – das harte Frische-Gate unmittelbar vor dem Kauf bleibt davon
       unabhängig zusätzlich bestehen.
     → **Liquiditäts-/Spread-Gate vor der Orderausführung (2026-08-30,
       Feinjustierungs-Runde 3, siehe Agent-Playbook-Archiv-Diskussionen.md Abschnitt 11):** ergänzt das
       Frische-Gate um die reale Ausführungsseite bei Brians Brokern
       (Scalable Capital, finanzen.net zero, Trade Republic, Smartbroker+,
       Handelsplätze wie Tradegate/Gettex) – gerade bei dünn gehandelten
       Scout-/Talent-Kandidaten (Beispiele: Kraken Robotics, Tristel PLC)
       kann ein zu breiter Geld-Brief-Spread die beste Analyse in der
       Praxis entwerten. Vor dem Kauf: durchschnittliches Tagesvolumen
       prüfen (Richtwert >500.000€ bzw. Äquivalent an der Heimatbörse),
       Geld-Brief-Spread während der regulären Handelszeiten prüfen
       (Richtwert <1,5%). Bei Talent-/Scout-Titeln gilt zusätzlich: Kauf
       ausschließlich per Limit-Order, niemals per Market-Order.

[3] FUNDAMENTAL-/SCOUT-ANALYSE — 3-FACH CROSS-CHECK MIT DISKUSSIONSRUNDE
     → PARALLEL, nicht nacheinander (2026-08-23, Lehre aus ServiceNow-Testlauf: erst
       Claude/Jarvis komplett abwarten, DANACH ChatGPT/Gemini starten hat unnötig
       Zeit gekostet): der Claude-Subagent-Aufruf und die Browser-Prompts an
       ChatGPT/Gemini werden im selben Schritt gestartet, nicht sequenziell –
       Gesamtdauer richtet sich dann nach der langsamsten der drei KIs, nicht nach
       der Summe aller drei
     → **GEMEINSAMES SCHRITT-0-DATENPAKET (2026-08-28, von Brian gefordert, um
       Redundanz abzubauen ohne die Unabhängigkeit der Urteile zu verlieren):**
       Live-Kurs, 48-72h-News und die Kern-Kennzahlen (SCHRITT 0 des jeweiligen
       Prompts) werden EINMALIG recherchiert (i.d.R. von Jarvis/Claude als
       "Daten-Vorlauf" vor dem eigentlichen Cross-Check, mit Quellenangabe und
       Tags [LIVE]/[VERIFIED]/[TRAINING] wie gewohnt) und allen drei KIs als
       identisches, geprüftes Datenpaket vorgelegt, statt dass jede KI dieselben
       Zahlen einzeln zusammensucht. Das spart redundante Recherche-Arbeit und
       verhindert, dass die drei KIs allein wegen unterschiedlicher Rohdaten
       (z.B. leicht abweichender Kurs-Zeitstempel) zu unterschiedlichen Urteilen
       kommen. **Bewusste Grenze:** Nur die Datenbeschaffung wird geteilt – der
       DNA-Check (SCHRITT 2), Moat/Management-Einschätzung und das Verdict
       bleiben strikt UNABHÄNGIG pro KI. Würde man auch die Bewertung selbst
       aufteilen (z.B. eine KI macht nur Zahlen, eine nur Moat, eine nur
       Verdict), ginge der eigentliche Zweck des Cross-Checks verloren – ein
       gemeinsames Endergebnis statt drei unabhängiger Meinungen, die sich
       gegenseitig kontrollieren können (siehe SKWD-Präzedenz: der Jarvis-vs-
       Jack-Dissens zur ROIC-Frage wäre bei aufgeteilter Bewertung nie sichtbar
       geworden).
     → **Einheitliches Fact-Pack-Format (2026-08-29, aus der Meta-Retrospektive
       Jack/Conan/Jarvis, siehe Agent-Playbook-Archiv-Diskussionen.md Abschnitt 9, Phase 1 – von Brian freigegeben):**
       Das SCHRITT-0-Datenpaket bekommt ab jetzt einen festen Kopf, damit alle
       drei KIs nachweislich von identischen Fakten ausgehen, nicht nur von
       "ungefähr denselben": **Zeitstempel** (Datum+Uhrzeit der Abfrage),
       **Kurs** (mit Börsenplatz), **Währung**, **Marktkapitalisierung**,
       **Reporting-Periode** (welches Quartal/Jahr die Kennzahlen abbilden),
       **Quelle(n)** (Name + Link), **Konfidenz-Tag** ([LIVE]/[VERIFIED]/
       [TRAINING], wie gehabt). Fehlt eines dieser Felder, gilt das
       Datenpaket als unvollständig und muss vor Rundenstart nachgezogen
       werden, statt mit Lücken in den Cross-Check zu gehen.
     → **Fact-Pack-Tag-Disziplin bei Jarvis selbst / Fact-Pack-Tags sind für Jack/Conan NICHT bindend (2026-09-06, echte Ursache des wiederholten Jack-Reflex-Abbruch-Bugs gefunden, siehe HANDOVER.md 10.13):** Bei Disco Corp (31.08.) UND Lasertec (05.09.) stellte sich beim Nachlesen von Jacks eigener Begründung heraus, dass NICHT Gemini eigenständig zu strikt urteilte, sondern Jarvis' EIGENES Fact-Pack die Kennzahl (Piotroski F-Score, FCF-Marge) bereits als `[N/V]` taggte, obwohl direkt daneben eine plausible qualitative Einschätzung stand, die eigentlich `[TRAINING]` verdient hätte (z.B. Disco: "qualitative Indikatoren sprechen für einen hohen Score, aber keine belastbare Zahl gefunden" → trotzdem als `[N/V]` getaggt). Jack übernahm dieses bereits gesetzte Tag als vorentschieden, statt es selbst neu zu bewerten – Conan überschreibt es in der Praxis öfter eigenständig. **Zwei-teiliger Fix:** (1) Jarvis wendet beim ERSTELLEN des Fact-Packs dieselbe TRAINING-vs-N/V-Schwelle an, die für Jack/Conan gilt (siehe Klarstellungsblock 3 in HANDOVER.md 10.13) – ist aus qualitativen Indikatoren/allgemeinem Wissen eine halbwegs plausible Größenordnung ableitbar, wird im Fact-Pack `[TRAINING]` vergeben, `[N/V]` bleibt reserviert für Fälle mit wirklich GAR KEINER Einordnung. (2) Zusätzlich, als Sicherheitsnetz: jedem Bridge-Aufruf wird ab sofort explizit mitgegeben, dass Fact-Pack-Tags ein Ausgangspunkt sind, keine bindende Vorentscheidung – kann Jack/Conan selbst (aus Training oder eigener Live-Suche) eine plausible Schätzung ableiten, überschreibt das ein `[N/V]`-Tag im Fact-Pack zu `[TRAINING]`, mit eigener kurzer Begründung, statt das Fact-Pack-Tag unkritisch zu übernehmen.
     → **DATENKONFLIKT-Notbremse (2026-08-29, Meta-Retrospektive Phase 1):**
       Weichen die von den drei KIs zusätzlich selbst recherchierten
       Kernzahlen (Kurs, Quartalszahlen, Marktkapitalisierung) trotz
       gemeinsamem Fact-Pack spürbar voneinander ab (z.B. unterschiedliche
       Reporting-Perioden verwechselt, klar veraltete vs. aktuelle Quelle),
       darf daraus KEINE hoch-konfidente Handlungsempfehlung (KAUFEN/VERKAUFEN
       ERWÄGEN) abgeleitet werden. Das Ergebnis wird stattdessen explizit als
       **DATENKONFLIKT** geflaggt, mit Benennung der widersprüchlichen Werte
       und Quellen – Konsequenz ist BEOBACHTEN/keine Aktion bis der Konflikt
       aufgelöst ist, nicht ein Rating, das auf unsicherer Datenbasis beruht.
     → **Einheitliche EUR-Umrechnung für alle Kursangaben (2026-08-29, von
       Brian gefordert):** Unabhängig davon, in welcher Originalwährung ein
       Wert notiert (USD, JPY, GBP, IDR usw.) und unabhängig davon, um
       welche Aktie es sich handelt, wird JEDE im Fact-Pack, Kurz-Fazit,
       Wochenfazit oder PDF genannte Kursangabe zusätzlich in EUR
       umgerechnet ausgewiesen – der Live-Kurs selbst, die Gewinnmitnahme-
       Zielzonen und Nachkauf-Einstiegszonen (siehe "Verkaufsdisziplin &
       Gewinnmitnahme-Regeln"), TA-Entry-/Stop-Loss-Niveaus, und jede
       sonstige Preisangabe. Format: Originalwährung zuerst, EUR-Gegenwert
       in Klammern dahinter, z.B. "142,30 USD (≈131,80 €)", mit dem zum
       Abfragezeitpunkt aktuellen Wechselkurs (Quelle wie beim übrigen
       Fact-Pack, z.B. ECB-Referenzkurs/xe.com) inkl. Datum, falls der Kurs
       nicht taggleich vorliegt. Ziel: Brian soll Entry-/Exit-Niveaus direkt
       in seiner eigenen Depot-Währung (Euro) im Blick haben, ohne selbst
       umrechnen zu müssen. Fehlt ein aktueller Wechselkurs, wird das
       transparent vermerkt statt eine veraltete/geschätzte Umrechnung
       unkommentiert zu präsentieren.
     → derselbe Prompt (TMR oder Scout) + derselbe Ticker + dasselbe geprüfte
       SCHRITT-0-Datenpaket wird UNABHÄNGIG von Claude/Jarvis, ChatGPT/Conan und
       Gemini/Jack durchgerechnet
       (Runde 1 – unabhängige Einzelurteile, keiner sieht die Antwort der anderen)
     → **Depot-Einblick (2026-09-02, von Brian gefordert):** ChatGPT/Conan und
       Gemini/Jack können bei Bedarf über die `_agentic`-Varianten der jeweiligen
       Bridge (`ask_chatgpt_agentic`/`ask_gemini_agentic`) selbst read-only
       Depot-Tools anfordern (Holdings/Übersicht/Performance/Cash-Breakdown),
       um z.B. Konzentrationsrisiko oder Kategorie-Caps gegen den Kandidaten zu
       spiegeln, statt das nur nachträglich im optionalen Schritt [6] zu prüfen.
       Technisch ein von Jarvis gesteuerter Relay-Loop, kein direkter
       KI-Durchgriff aufs Depot (Details: HANDOVER.md Abschnitt 10.11).
     → strukturierte Kernwerte aus jeder Antwort extrahiert (Rating, Score,
       Fair Value Bear/Base/Bull, K-Kriterien-Status, aktive Flags)
     → Vergleich der drei Ergebnisse:
         - Rating stimmt bei allen dreien überein → hohe Konfidenz, weiter zu [3b]
         - Rating weicht ab (z.B. 1x KAUFEN, 2x BEOBACHTEN) → Diskrepanz-Flag
         - Fair Value weicht >X% ab → ebenfalls Diskrepanz-Flag

[3b] DISKUSSIONSRUNDE & SYNTHESE — MEHRRUNDEN-LOOP (2026-08-27, auf Brians
     Wunsch von einer einmaligen Stellungnahme zu einem echten Mehrrunden-
     Austausch erweitert: "die sollen untereinander diskutieren, analysieren
     und zu einem entsprechenden Ergebnis kommen") — läuft IMMER, auch bei
     Übereinstimmung, aber besonders wichtig bei Diskrepanz-Flag aus [3]:

     → Runde 2 (Pflicht): jede der drei KIs bekommt die vollständigen
       Einzelurteile der beiden anderen (inkl. Zahlen/Begründung) vorgelegt und
       wird gebeten, dazu explizit Stellung zu nehmen – zustimmen, widersprechen,
       oder die eigene Einschätzung revidieren, mit Begründung ("Was hat Conan
       gesehen, das ich nicht hatte? Ändert das mein Urteil?").
     → Konvergenz-Check nach Runde 2:
         - Ergebnis "stark" (alle drei einig) → LOOP STOPPT hier, keine
           weitere Runde nötig (würde nur Kosten ohne zusätzlichen Erkenntnis-
           gewinn verursachen).
         - Ergebnis "moderat" oder "widerspruch" → Runde 3 (optional, siehe
           Cap unten): jede KI bekommt die AKTUALISIERTEN Positionen der beiden
           anderen aus Runde 2 vorgelegt (inkl. eventueller Revisionen) und wird
           gezielt gefragt, ob das jeweilige Gegenargument etwas ändert.
     → HARTER CAP: maximal 2 Diskussionsrunden insgesamt (Runde 2 + Runde 3),
       kein unbegrenztes Hin und Her. Begründung (2026-08-27, von Jarvis
       vorgeschlagen, von Brian akzeptiert): (a) Kosten – jede Zusatzrunde sind
       nochmal 3 KI-Aufrufe; historisch waren zwei davon fragile Browser-
       Automation-Beine, seit 2026-09-02 laufen ChatGPT/Conan (`openai-bridge`,
       Modell `gpt-5.5`) UND Gemini/Jack (`gemini-bridge`, Modell
       `gemini-2.5-flash`) beide über direkten API-Call (siehe HANDOVER.md
       Abschnitt 10.9/10.10) und sind von Browser-Fragilität nicht mehr
       betroffen – die Kosten-Begründung bleibt trotzdem gültig (reine
       Zusatz-KI-Aufrufe kosten weiterhin Zeit/Tokens), (b) Erfahrungswert – Positionsänderungen durch
       Diskussion passieren fast immer in der ersten Runde, weitere Runden
       wiederholen meist nur die bestehenden Argumente, (c) Ping-Pong-Risiko –
       ohne Cap könnten sich zwei KIs theoretisch endlos gegenseitig
       widersprechen.
     → Ziel ist NICHT künstlicher Konsens um jeden Preis – ein begründeter
       Widerspruch, der nach Runde 3 (oder schon nach Runde 2, falls keine
       Positionsänderung mehr erkennbar ist) bestehen bleibt, ist ein valides
       und meldenswertes Endergebnis (siehe Konvergenz-Feld unten), keine
       unvollständige Analyse.
     → Ergebnis der Diskussionsrunde wird protokolliert als:
         - Konvergenz "stark": alle drei einig (nach Runde 2 oder 3)
         - Konvergenz "moderat": Tendenz gleich, Details unterschiedlich (z.B.
           unterschiedliche Agent Scores, gleiches Rating)
         - Konvergenz "widerspruch": Ratings bleiben nach Ausschöpfung des
           Runden-Caps unterschiedlich – das ist der Fall, der Brian im
           Kurz-Fazit (Schritt 5) am deutlichsten hervorgehoben werden muss,
           inkl. der Kernfrage, worüber die drei KIs uneins sind, UND wie viele
           Runden es gebraucht hat / ob sich die Positionen überhaupt bewegt haben
     → das ist die "gegenseitige Kontrolle", die Brian wollte – nicht nur
       parallele Einzelmeinungen und eine einmalige Stellungnahme, sondern ein
       echter (aber budgetiert begrenzter) Hin-und-her-Austausch bis Konvergenz
       oder bis der Rundencap erreicht ist
     → **Double-Counting-Prüfung beim Agent Score (2026-09-03, Conans
       Warnung aus dem 3-KI-System-Audit):** der Agent Score fasst mehrere
       Negativsignale zusammen (u.a. Kursverlust, Momentumbruch,
       Analystenrevisionen, Guidance-Cut) – diese Signale sind oft NICHT
       unabhängig voneinander, sondern Symptome desselben zugrunde
       liegenden Ereignisses (z.B. ein Guidance-Cut löst typischerweise
       auch Kursverlust, Momentumbruch UND Analystenrevisionen gleichzeitig
       aus). Wird jedes Symptom separat und additiv gewertet, kann ein
       einzelnes Ereignis den Score mehrfach drücken. **Behoben direkt an
       der Quelle (2026-09-03, TMR-Prompt v11.7 → v11.8):** die
       STAPEL-LOGIK im TMR-Prompt hat jetzt eine "KORRELIERTE-MALI-REGEL"
       – gehen zwei oder mehr aktive Mali erkennbar auf dasselbe
       auslösende Ereignis zurück, zählt nur der GRÖSSERE Einzel-Malus,
       nicht die Summe; die Zusammenführung muss im Output explizit
       benannt werden (siehe `prompts/jack-moat-reaper-v11.7.md`,
       Abschnitt "STAPEL-LOGIK"). Umgesetzt gemäß der in Abschnitt 2
       ("Spielraum für Prompt-Anpassungen") von Brian erteilten
       eigenständigen Änderungsbefugnis. Zur Absicherung bleibt es
       trotzdem sinnvoll, in der Diskussionsrunde [3b] gegenzuprüfen, ob
       die Zusammenführung im konkreten Fall korrekt begründet wurde,
       statt sie unhinterfragt zu übernehmen.

[3c] META-RETRO-RUNDE — SELBSTVERBESSERUNG DES REGELWERKS (2026-08-28, von
     Brian gefordert: "können die Agenten unter sich ausmachen, was sie
     verbessern können") — läuft NICHT nach jeder Analyse, sondern gezielt bei
     AUFFÄLLIGEN FÄLLEN:
     → Auslöser (einer reicht): (a) Konvergenz "widerspruch" nach Ausschöpfung
       des Runden-Caps in [3b], (b) ein dokumentierter Regelverstoß/methodischer
       Fehler einer KI (z.B. falsch gezählte K-BASIS wie bei Conan/Jack im
       SKWD-Fall), (c) derselbe Fehlertyp taucht bei mehreren unabhängigen
       Analysen wiederholt auf.
     → Ablauf: Die 3 KIs bekommen NICHT die Aufgabe, das Aktien-Urteil zu
       ändern, sondern gezielt die Meta-Frage: "Was am Regelwerk/an der
       Prompt-Formulierung hat zu dieser Uneinigkeit/diesem Fehler geführt, und
       wie würdest du die Formulierung präzisieren, damit das nicht wieder
       passiert?" – Diskussion ist auf Methodik/Formulierung begrenzt, nicht auf
       das konkrete Einzelurteil (das bleibt wie in [3b] protokolliert stehen).
     → Ergebnis: konkrete Formulierungsvorschläge für das Regelwerk (TMR/Scout/
       TA-Prompt), die ich (Jarvis/Claude als Architektur-Verantwortlicher)
       sichte, auf Widersprüche zum bestehenden Regelwerk prüfe und Brian zur
       Freigabe vorlege – KEINE automatische Selbst-Modifikation des Regelwerks
       durch die KIs. Erst nach Brians Freigabe wird eine neue Versionsnummer
       (z.B. v11.7 → v11.8) vergeben und die entsprechende Prompt-Datei
       aktualisiert.
     → Bewusst NICHT bei jeder Analyse: das wäre teuer (wieder 3 zusätzliche
       KI-Aufrufe) und die meisten Analysen laufen ohne methodische Reibung
       durch – die Retro-Runde lohnt sich nur dort, wo tatsächlich ein Lern-
       Signal vorliegt.
     → **Prompt-Änderungsrechte, explizit geklärt (2026-09-03, aus dem
       3-KI-System-Audit – Conan hatte einen scheinbaren Widerspruch
       zwischen "Jarvis darf eigenständig ändern" (Abschnitt 2,
       "Spielraum für Prompt-Anpassungen", 2026-08-29) und "keine
       automatische Selbst-Modifikation" (hier in [3c], 2026-08-28)
       bemängelt. Klarstellung nach Prüfung: KEIN echter Widerspruch,
       sondern zwei Zeitpunkte – Abschnitt 2 ist die spätere, von Brian
       BEWUSST gelockerte Fassung und damit die aktuell gültige Regel.
       [3c] beschreibt seither nur noch EINEN von zwei Wegen, wie eine
       Prompt-Änderung entstehen kann, nicht mehr die einzige/exklusive
       Freigabe-Voraussetzung):**
       - **Orchestrierungs-/Prozess-Ebene (Agent-Playbook.md selbst,
         `depot/*.md`, `watchlist.md`, `HANDOVER.md`, die Scheduled-Task-
         SKILL.md-Dateien):** laufend gepflegter Betriebszustand + Regelwerk-
         Dokumentation. Jarvis pflegt diese Ebene eigenständig, keine
         Versionsnummer nötig, nur nachvollziehbare Commits.
       - **Methodik-/Bewertungslogik-Ebene (die drei Prompt-Dateien unter
         `prompts/`: TMR/jack-moat-reaper, Scout/conan-the-scout,
         TA/jack-technical-analyst):** Brians eigene Bewertungs-Systeme
         (DNA-Check-Kriterien, Agent-Score, Kill-Gates, K-Kriterien-
         Schwellen usw.). Gemäß Abschnitt 2 **darf Jarvis diese
         eigenständig modifizieren/ergänzen/abändern, wenn das dem
         Nordstern (Abschnitt 1) besser dient – OHNE vorherige
         Freigabe-Runde** durch Brian oder die anderen KIs. Zwei
         Bedingungen bleiben dabei zwingend: (a) **neue Versionsnummer
         + nachvollziehbare Dokumentation der Änderung** (nie eine
         stille Änderung), (b) die Order-Ausführungs-Grenze aus
         Abschnitt 1 bleibt unberührt – der Spielraum betrifft
         ausschließlich Analyse-/Bewertungs-/Exit-Logik, nicht
         Ausführungsbefugnis. Der [3c]-Meta-Retro-Pfad (KI-Vorschlag →
         Jarvis sichtet → Brian gibt frei → Versionsnummer) bleibt der
         bevorzugte Weg für Fälle, die aus einem ECHTEN Cross-KI-
         Streitfall entstehen (Konvergenz "widerspruch", wiederholter
         Fehlertyp) – dort lohnt sich die strukturierte
         Mehrfach-Perspektive VOR der Umsetzung. Bei einer klar
         erkannten, unstrittigen Methodik-Lücke (wie dem Agent-Score-
         Double-Counting-Risiko oben) kann Jarvis auch direkt
         korrigieren und Brian danach im laufenden Gespräch informieren,
         statt einen eigenen Freigabe-Zyklus abzuwarten.
       - Kurzfassung: **beide Ebenen sind eigenständig editierbar – der
         Unterschied ist nicht "darf/darf nicht", sondern dass
         Prompt-Änderungen immer versioniert + dokumentiert werden
         müssen, während Betriebsdateien das nicht brauchen.**

[4] TECHNISCHE ANALYSE (TA) — ebenfalls 3-fach mit Diskussionsrunde [3b]-Logik,
    mit TMR-Handoff falls vorhanden
     → gleiche Cross-Check- und Diskussionslogik wie Schritt 3/3b, diesmal mit dem
       TA-Prompt
     → Ergebnis: Entry-Ampel + Kombinations-Score pro Kandidat, inkl. Konvergenz-Status

[5] REPORT / WATCHLIST-UPDATE
     → Zusammenfassung: neue Kandidaten, Rating-Änderungen bei bestehenden
       Watchlist-/Depot-Positionen, Konflikte/Diskrepanzen, Entry-Timing
     → KEINE automatische Order. Brian entscheidet und führt manuell aus.
     → WICHTIG (2026-08-22, Feedback von Brian): Die vollen TMR-/Scout-/
       TA-Ausgaben (mehrere hundert Zeilen, komplette Pflicht-Tabellen) laufen
       IMMER in voller Tiefe im Hintergrund (als Subagent), landen aber nur
       noch als Datei im Projektordner – Brian bekommt sie NICHT mehr
       standardmäßig zum Durchlesen vorgesetzt. Stattdessen bekommt er direkt
       im Chat ein kurzes Kurz-Fazit (5-8 Sätze, Fließtext statt Tabellen):
         - Rating (TMR) + Timing-Ampel (TA) in einem Satz
         - Der Haupttreiber, warum die Firma interessant ist (oder nicht) –
           Moat, Wachstum, Bewertung
         - Depot-Fit: Überschneidet sich das Geschäftsmodell/Sektor mit
           bestehenden Positionen (Klumpenrisiko/Diversifikation)? In welche
           Kategorie (Champions/Profi/Talent, siehe Abschnitt 3) würde die
           Position fallen, und ist dort noch Platz? Passt die Sizing-Tier-
           Empfehlung zur aktuellen Depotgröße?
         - Konvergenz der drei KIs (siehe Pipeline-Schritt 3b): einig, oder
           bestehender Widerspruch nach der Diskussionsrunde?
         - Klare Handlungsempfehlung: Jetzt kaufen / Watchlist / abwarten bis
           Kurs X
       Die volle Analyse-Datei bleibt abrufbar (SendUserFile), wird aber nur
       auf Nachfrage nachgereicht, nicht automatisch mitgeschickt.
     → **WICHTIG (2026-08-27, von Brian gefordert): PDF-Ausgabe auch für
       Einzelanalysen.** Bisher war das "Agent Wochenreport"-Ein-Seiten-Layout
       (siehe Abschnitt 5 "PDF-Report-Design") nur für den gebündelten
       Wochenfazit-Report verdrahtet. Ab jetzt gilt: JEDE abgeschlossene
       3-fach-Cross-Check-Analyse einer einzelnen Position – egal ob von Brian
       manuell angestoßen ("analysiere mir XY") oder vom täglichen Trigger-Check
       automatisch ausgelöst – erzeugt zusätzlich zur Markdown-Datei in
       `analysen/` sofort eine Ein-Seiten-PDF im Agent-Kompakt-Layout (3-Stimmen-
       Leiste, Agent-Score-Gauge, DNA-Check-Strang, Chancen/Risiken, Fazit) für
       genau diese eine Position und liefert sie per SendUserFile aus. Das
       Wochenfazit bündelt weiterhin ALLE Positionen in einem PDF (plus die
       Report-weiten Seiten Gesamtübersicht/Methodik/Quellen) – die Einzel-PDF
       pro Analyse ist zusätzlich, kein Ersatz dafür. Im Chat bleibt es trotzdem
       beim kurzen Kurz-Fazit (siehe oben) – das PDF liefert die Detailtiefe,
       nicht ein längerer Chat-Text.
       **Technische Umsetzung (validiert 2026-08-27 am Live-Testlauf SKWD):**
       Ein-Seiten-HTML (eigenes CSS, Agent-Kompakt-Design gemäß Abschnitt 5)
       wird lokal via Playwright/Chromium (headless) zu PDF gerendert (A4,
       `print_background=True`) – kein reportlab-Canvas, damit Gauge-Grafiken
       (SVG-Halbkreis-Arcs), DNA-Strang-Segmente und Farbverläufe frei gestaltbar
       bleiben. Font-Pairing mangels Internetzugriffs auf Google Fonts im
       Sandbox-Container: "DejaVu Sans Condensed" (Bold, Headings/Display) +
       "Carlito" (Body) – beide systemseitig vorinstalliert, kein Font-Download
       nötig. Vor Auslieferung wird das gerenderte PDF per `pdftoppm` in ein PNG
       konvertiert und visuell auf Overflow/Überlappung geprüft (Pflichtschritt,
       da Flexbox-Layouts bei festen Seitenhöhen sonst BOXEN überlaufen lassen
       können, ohne dass das beim reinen HTML-Schreiben auffällt).
     → **WICHTIG (2026-08-29, von Brian auf ALLE Ausgaben ausgeweitet):
       Universelle PDF-Auslieferung.** Die PDF-Pflicht gilt ab jetzt nicht
       mehr nur für abgeschlossene 3-fach-Cross-Check-Analysen und das
       wöchentliche Wochenfazit, sondern für JEDES inhaltlich substanzielle
       Ergebnis des Agenten – unabhängig vom Anlass. Egal ob es um eine
       Einzelanalyse geht, um eine Portfolio-/Depotübersicht, eine Antwort
       auf eine Ad-hoc-Frage zum Portfolio, ein Watchlist-Update oder eine
       Eskalations-Meldung aus dem täglichen Trigger-Check (siehe Abschnitt
       5): in jedem dieser Fälle wird zusätzlich zur kurzen Chat-Antwort
       eine PDF-Datei erzeugt und per SendUserFile ausgeliefert – Layout je
       nach Inhalt (Agent-Kompakt-Layout für eine einzelne Position,
       angelehnt an das Wochenfazit-Layout für Portfolio-/Mehrfach-
       Positionen-Übersichten). Ausnahme bleibt eine rein konversationelle
       Antwort ohne eigenständigen inhaltlichen Ergebniswert (z.B. eine
       reine Rückfrage von Brian oder eine Begriffsklärung) – dafür wird
       keine PDF erzwungen. Im Zweifel gilt: lieber ein PDF zu viel als
       eines zu wenig. Der tägliche Trigger-Check (siehe Abschnitt 5 bzw.
       Scheduled Task "Täglicher Depot-Trigger-Check") erzeugt demnach ab
       jetzt auch bei einer Eskalations-Nachricht (Schritt 6) zusätzlich
       eine kompakte PDF-Datei, nicht nur bei einem vollen 3-fach-Cross-
       Check.
     → **NEUES LAYOUT (2026-08-29, von Brian vorgegeben, Vorlage "Kleine
       Aktienanalysen" von rakentoni): Ampel-Batch-Scan-Layout für Mehrfach-
       Analysen "am Stück".** Wenn mehrere Kandidaten in einem Rutsch grob
       eingeordnet werden sollen (z.B. Watchlist-Sammelcheck, erste Sichtung
       einer Screening-Liste) – NICHT als Ersatz für den vollen 3-fach-
       Cross-Check, sondern als schnellere, einstimmige Vorstufe davor –
       kommt ein eigenes, kompakteres Layout zum Einsatz, im Aufbau an
       Brians Vorlage angelehnt, aber in unserer Agent-Optik (dunkler
       Hintergrund, Gold-Akzente, DejaVu Sans Condensed/Carlito) statt im
       Original-Navy/Weiß-Stil:
       - **Deckblatt:** Titel, Sektor-gruppierte Kandidaten-Übersicht (Tabelle),
         Auftrag/Ampel-Legende, Datenstand.
       - **Gesamtüberblick:** Ranggruppen A-E (stärkste Allrounder bis reine
         Spekulation) mit Gesamt-Ampel + Kurzbegründung, "Kompaktes Ergebnis"
         (3-5 Bullet-Kernaussagen), Hinweise zu Bewertungsdatenlücken.
       - **Eine Seite pro Kandidat:** Kopf (Nummer+Name, Sektor/Ticker/Börse/
         ISIN, Ampel-Badge oben rechts), Ein-Satz-These in Kasten,
         Kennzahlen-Kurztabelle (3-4 Zeilen), "Einordnung" (2 Absätze),
         "Ampelcheck"-Tabelle (6 Zeilen: Geschäftsmodell/Wachstum/
         Profitabilität/Bilanz/Bewertung/Risiko je mit Ampel+Begründung),
         Chancen/Risiken zweispaltig, "Beobachten"-Zeile (worauf achten),
         "Fazit"-Zeile (ein Satz Handlungsempfehlung).
       - **Ampel-Skala (4-stufig, bewusst FEINER/andere Achse als unser
         KAUFEN/BEOBACHTEN/SCHROTT-Rating):** 🟢 GRÜN (stark/allgemein
         interessant) · 🟡 GELB (gut, aber Preis/Risiko beachten) · 🟠 ORANGE
         (problematisch/spekulativ) · 🔴 ROT (fundamental schwach/sehr hohes
         Risiko). Das ist ein SCHNELLCHECK-System, kein Ersatz für die K-
         Kriterien-DNA/Agent Score – vor einer echten KAUFEN-Entscheidung
         oder Watchlist-Aufnahme bleibt der volle TMR-/Scout-Pfad (ggf.
         3-fach-Cross-Check) Pflicht, siehe Pipeline Abschnitt 4.
       - **3-fach-Format, KEIN Ein-KI-Format (2026-08-29, von Brian korrigiert
         nach dem ersten Praxislauf mit 6 Werten):** Ursprünglich lief dieses
         Layout NUR mit Jarvis. Brian hat das nach dem ersten Testlauf explizit
         korrigiert: **auch der Ampel-Batch-Scan läuft grundsätzlich mit allen
         drei KIs (Jarvis/Jack/Conan)** – unabhängig davon, ob pro Kandidat nur
         ein Quick Filter oder ein voller Deep Dive gefahren wird. Begründung
         (Brian wörtlich): "so bekommt man das neutralste aber gleichzeitig
         bestmögliche Ergebnis heraus." Das Ein-KI-Tempo-Argument wird also
         bewusst der Konvergenz-Absicherung durch drei unabhängige Meinungen
         untergeordnet – auch im Batch-Format. Das bedeutet konkret: pro
         Kandidat im Batch laufen Jarvis, Jack und Conan (je in der für den
         Batch festgelegten Tiefe, siehe unten), danach eine kurze Konvergenz-/
         Dissens-Einordnung wie beim regulären 3-fach-Cross-Check – nur eben
         kompakter im Ampel-Batch-Layout statt im vollen Agent-Kompakt-Report
         pro Einzelwert. Praktische Konsequenz: ein Batch mit mehreren Werten
         braucht entsprechend mehr Zeit/Aufwand (3x Browser-Automation bzw.
         API-Calls pro Kandidat) – das ist von Brian bewusst in Kauf genommen.
       - **Analyse-Tiefe = TMR QUICK FILTER / Scout-Kurzform, NICHT Full Deep
         Dive (2026-08-29, von Brian präzisiert):** Bei mehreren Analysen "am
         Stück" wird pro Kandidat standardmäßig die bereits bestehende
         QUICK-FILTER-Tiefe aus dem TMR-Prompt gefahren (DNA-Check + Konfidenz
         + Kompaktes Verdict, vereinfachtes WACC, kein Python-DCF, Zyklus/
         Moat/Management nur in Stichpunkten – siehe "ANALYSE-TIEFE" im
         TMR-Prompt) bzw. die entsprechende Scout-Kurzform bei jungen/
         spekulativen Werten. Das Ampel-Batch-Layout ist also NUR die
         Präsentationsschicht – die zugrunde liegende Prüftiefe bleibt das
         etablierte QUICK-FILTER-Raster, nicht eine neue, noch leichtere
         Ad-hoc-Prüfung. Ein FULL DEEP DIVE für einen einzelnen Wert aus dem
         Batch wird nur gefahren, wenn Brian (oder jemand anderes) das
         explizit für genau diesen Wert anfordert – das kommuniziert er dann
         gezielt, es passiert nicht automatisch.
       - Quellen-Seite am Ende (Primärquellen je Kandidat) und ein "Methodik
         und Grenzen"-Hinweis (kein DCF, keine Chartanalyse, Ampel ist
         qualitative Gesamtschau) analog zur Vorlage.
     → **WICHTIG (2026-08-23, Feedback von Brian, Erweiterung der obigen Regel):**
       Das gilt jetzt nicht nur für die Ergebnistiefe, sondern auch für den
       PROZESS selbst. Der komplette Analyse-Lauf (alle drei KI-Beine – seit
       2026-09-02 laufen ChatGPT/Conan UND Gemini/Jack beide per direktem
       API-Call über ihre jeweiligen MCP-Bridges statt Browser-Automation,
       Details HANDOVER.md 10.9/10.10 –, Diskussionsrunde [3b], Datei-
       Ablage) läuft ausschließlich im Hintergrund, ohne Zwischen-Status-
       Meldungen im Chat ("Tab X geöffnet", "Gemini antwortet noch", "Schritt Y
       läuft"). Brian bekommt währenddessen keine Prozess-Narration mehr –
       direkte Zwischenfragen von ihm werden natürlich weiterhin beantwortet,
       aber unaufgefordert wird nur am Ende das fertige Kurz-Fazit gepostet.
     → **Update (2026-08-29, von Brian präzisiert – gilt speziell für live im
       Chat angestoßene Einzelanalysen):** Schickt Brian in einer laufenden
       Chat-Session selbst eine Aktie zur Analyse ("analysiere mir XY"), gilt
       die "keine Prozess-Narration"-Regel oben nicht mehr uneingeschränkt.
       Hier möchte Brian zwischendurch kurze Status-Updates, an welchem
       Punkt der Analyse der Agent gerade steht, z.B.: "Suche gerade Ticker/
       ISIN heraus...", "Ziehe jetzt die Kernkennzahlen (Fact-Pack)...",
       "Rufe aktuelle News der letzten 48-72h ab...", "Fundamental-Cross-
       Check läuft (Jack/Conan/Jarvis)...", "Technische Analyse (TA)
       läuft...". Diese Updates sind bewusst knapp (ein Satz je Schritt) und
       ersetzen nicht das fertige Kurz-Fazit am Ende – sie geben Brian nur
       laufend mit, wo der Agent gerade steht, statt dass er minutenlang
       ohne jedes Lebenszeichen wartet. **Abgrenzung:** Für die
       automatisierten, unbeaufsichtigten Scheduled-Task-Läufe (täglicher
       Trigger-Check, Wochenfazit, siehe Abschnitt 5 und "Wochenfazit"
       unten) bleibt es bei der reinen Hintergrund-Verarbeitung OHNE
       Zwischen-Status im Chat wie bisher – dort liest niemand live mit, die
       Änderung betrifft ausschließlich Fälle, in denen Brian selbst gerade
       in einer aktiven Chat-Session eine Analyse anstößt und den
       Fortschritt live mitverfolgen möchte.

[6] (optional, wenn Brians Mac/Chrome verbunden ist) DEPOT-ABGLEICH
     → aktueller Depotstand (Trade Republic/Scalable Capital) wird read-only
       ausgelesen, fließt in Positionsgrößen-Berechnung und Watchlist-Abgleich ein
```

## 5. Monitoring & proaktive Benachrichtigung (laufender Betrieb)

Neben der Kandidaten-Suche (Pipeline oben) läuft ein zweiter, genauso wichtiger
Kreislauf: die laufende Überwachung dessen, was schon im Depot/auf der Watchlist
ist. Ziel: Brian muss nicht fragen "ist XY noch intakt?" – der Agent meldet sich
von sich aus, wenn sich etwas Relevantes ändert.

```
Für jede bestehende Depot-/Watchlist-Position, in regelmäßigem Rhythmus:

[A] NEWS-CHECK
     → Web-Search nach Nachrichten der letzten 24-72h zum Ticker
     → Relevanz-Filter: Kurstreiber, Earnings, Management-Wechsel,
       Rechtsstreit, Regulatorik, M&A – Rauschen wird nicht gemeldet

[B] THESE-CHECK (MODUS C aus dem TMR-Prompt: "Noch intakt? Halten oder raus?")
     → prüft, ob die K-Kriterien/Moat-These noch stehen, ohne die komplette
       Tiefenanalyse neu zu fahren (siehe TMR MODUS C: darf bei fehlenden
       Live-Daten mit ⚠ VERALTET-Flag weiterlaufen statt SCHRITT 0 zu blockieren)
     → prüft aktive STOP-THESE-TRIGGER aus der ursprünglichen TMR-Analyse
       (siehe EXIT-STRATEGIE in Pipeline-Schritt 3) – ist einer gerissen?

[C] ENTRY/TIMING-CHECK für Watchlist-Positionen (noch nicht gekauft)
     → TA-Prompt SWING/INVESTOR-Check: ist die Preiszone inzwischen attraktiver
       geworden (Entry-Ampel-Wechsel 🟡→🟢)? Abstauber-Limit erreicht?
     → Technische Kennzahlen (2026-08-29, von Brian gefordert) kommen jetzt aus
       dem Twelve-Data-Connector statt aus grober Schätzung: Trend (Kurs vs.
       50/200-Tage-Linie), MACD (Signal/Histogramm), RSI/Momentum, Volumen
       (auffällig hoch/niedrig ggü. Durchschnitt), nächste Unterstützungs-/
       Widerstandszone (Pivot-Punkte bzw. jüngste Hochs/Tiefs). Siehe
       "Technische Analyse via Twelve Data" unten.

[D] CASH-ALLOKATIONS-CHECK / TÄGLICHER MARKT-/MAKRO-KONTEXT (2026-09-03,
    vollständig spezifiziert – von Brian gefordert: "du sollst den Markt
    ständig im Auge behalten, Sentiment, Schwankungen, geopolitische
    Entscheidungen, Zinsentscheid, News an der Börse, immer up to date
    sein"):
     → **Bisher nur MONATLICH erfasst** (Monatsrecap, "Makro-Radar/
       Sentiment") – das ist für Brians Anspruch "ständig im Auge
       behalten" zu selten. Ab jetzt zusätzlich TÄGLICH, als Teil des
       Täglichen Trigger-Checks (siehe dortige SKILL.md, neuer Schritt),
       PLUS ein marktweiter Schock-Trigger im stündlichen Blitz-Scan (nicht
       nur Einzelwert-Ereignisse wie bisher).
     → **Tägliche Momentaufnahme** (WebSearch/WebFetch, kompakt, keine
       Tiefenrecherche): CNN Fear & Greed Index (Stand + Zone), VIX,
       S&P 500/Nasdaq 100 Tagesveränderung, US-10J-Rendite + Kurvenform
       (normal/invers/flach), EUR/USD, Gold als Risk-off-Indikator, sowie
       ein kurzer Blick auf den Wirtschaftskalender der nächsten 48h (Fed/
       EZB-Termine, wichtige Konjunkturdaten) und akute geopolitische
       Schlagzeilen mit erkennbarem Marktbezug (Kriege/Konflikte,
       Sanktionen, Handelskonflikte, Wahlen mit Marktrelevanz).
       Gespeichert/fortgeschrieben in `depot/macro_context.md` (neue
       Zeile pro Tag), damit ein Tag-über-Tag-Vergleich möglich ist, statt
       jeden Tag bei Null anzufangen.
     → **Material-Shift-Kriterien (lösen eine Eskalation aus, sonst reine
       stille Protokollierung):** VIX-Sprung >20% ggü. Vortag, Fear&Greed
       wechselt die Zone (z.B. Neutral→Extreme Fear oder Greed→Extreme
       Greed), S&P 500/Nasdaq 100 Tagesbewegung >±3%, eine ÜBERRASCHENDE
       Zins-/Notfallentscheidung einer Notenbank (nicht die regulär
       terminierten, erwarteten Sitzungen selbst – die werden im
       Wirtschaftskalender-Blick oben nur vorab angekündigt), oder ein
       gravierendes geopolitisches Ereignis mit unmittelbar erkennbarer
       Marktreaktion.
     → **Portfolio-Sensitivitäts-Analyse bei Material Shift (2026-09-08, von
       Brian angeregt nach einem Beispiel aus Raketentonis System – ein
       Discord-Screenshot zeigte dessen Agent bei einem drohenden
       US-Regierungsstillstand eine Ampel-Liste ALLER Depot-Positionen mit
       individueller Sensitivitäts-Einschätzung zu genau diesem Ereignis):**
       löst Schritt oben ("Material-Shift-Kriterien") tatsächlich aus, wird
       ZUSÄTZLICH zur reinen Einordnung eine vollständige Sensitivitäts-Liste
       über ALLE Depot-Positionen (alle 4 Broker, siehe `depot/*.md`)
       erstellt – für jede Position individuell, NICHT ein pauschaler
       Beta-/Volatilitäts-Wert, sondern eine Einschätzung, wie stark GENAU
       DIESES Ereignis (nicht Marktrisiko allgemein) über welchen
       Übertragungskanal auf diese konkrete Position wirkt (z.B. bei einem
       US-Shutdown: direkte US-Staatsabhängigkeit/Regulatorik-Verzögerung
       vs. nur indirekt über allgemeines Risk-off-Sentiment vs. praktisch
       unberührt). Format je Position: Ampel (🔴 hoch / 🟠 erhöht / 🟡 mittel
       / 🟢 niedrig) + Positionsname + EIN Satz Begründung mit dem konkreten
       Übertragungskanal, nicht nur "ist riskant". Kein Score, keine
       automatische Handlungsempfehlung (siehe "Einordnung, KEINE
       Handlungsanweisung" unten – gilt hier genauso) – reine
       Einordnungshilfe, damit Brian selbst sieht, welche Positionen bei
       DIESEM konkreten Ereignis am empfindlichsten wären. Wird Teil der
       Material-Shift-Eskalationsmail/-WhatsApp-Nachricht (siehe
       Tages-Sichtbarkeit unten), nicht eine separate Datei/Routine. Bei
       einem sehr generischen Shift ohne klaren thematischen Bezug (z.B.
       reine Sentiment-Schwankung ohne erkennbaren Auslöser) reicht ein
       kurzer Hinweis, dass keine differenzierte Positions-Zuordnung
       sinnvoll möglich ist, statt eine erzwungene Liste ohne echten Bezug.
     → **Einordnung, KEINE Handlungsanweisung:** aus der Momentaufnahme
       wird eine grobe Investitionsklima-Einordnung abgeleitet (eher
       günstig für Zukäufe / neutral / eher Vorsicht-Cash-halten) – das
       ist ein ADVISORY-Signal (siehe Abschnitt 14, Core-vs-Advisory), das
       in die ohnehin bestehende KAUFEN-/NACHKAUF-/Cash-Disziplin-
       Einordnung pro Einzelposition einfließt, sie aber NIE ersetzt oder
       überschreibt – eine fundamental intakte 🟢-KAUFEN-Position bleibt
       ein Kauf-Kandidat auch bei "Vorsicht"-Marktklima (ggf. mit
       kleinerer Tranche/vorsichtigerer Tranchierung), eine fundamental
       gebrochene These wird nicht durch "Markt ist gerade euphorisch"
       zum Kauf. **Ausdrücklich keine Anlageberatung im regulatorischen
       Sinn** – die Einordnung ist Recherche-/Kontext-Unterstützung für
       Brians eigene, manuelle Entscheidung, keine professionelle
       Finanzberatung und kein Ersatz dafür.
     → **Tages-Sichtbarkeit:** die Kernwerte (Fear&Greed, VIX, Zinskurve)
       erscheinen als Kurzzeile in JEDER täglichen Trigger-Check-Mail
       (auch an ruhigen Tagen ohne Aktien-Anlass, siehe dortige
       SKILL.md) – das ist der Kanal, über den Brian "immer up to date"
       bleibt, ohne dass jede Marktschwankung eine Eskalation auslöst.

**Erweiterung (2026-09-03, von Brian ergänzt + eigenständig vervollständigt
– "es gibt noch mehr Makro-Check die ich nicht erwähnt habe... das musst
du berücksichtigen... die Ergänzungen die ich unerwähnt gelassen habe,
musst du vollziehen"):**

- **S&P-500-Schlüssel-Level & Korrektur-Risiko-Einordnung:** täglich
  aktueller Kurs gegen 50-Tage- und 200-Tage-Durchschnitt (SMA) prüfen,
  in `depot/macro_context.md` mitführen. **No-False-Precision-Regel gilt
  auch hier (siehe Abschnitt 4, Core-Rule 13):** KEINE erfundene exakte
  Prozent-Wahrscheinlichkeit für "wie hoch ist die Wahrscheinlichkeit
  einer Korrektur" – stattdessen die recherchegestützte, qualitative
  Heuristik verwenden: der entscheidende Faktor bei einem Bruch der
  200-Tage-Linie ist nicht der Bruch selbst, sondern ob die 200-Tage-
  Linie zum Bruchzeitpunkt selbst noch STEIGT oder bereits FLACH/
  FALLEND ist. Bei steigender 200-Tage-Linie waren Unterschreitungen
  historisch meist kurze Whipsaws mit schneller Erholung (Beispiel
  Anfang 2023). Bei flacher/fallender 200-Tage-Linie waren
  Unterschreitungen historisch häufiger der Auftakt zu einem
  nachhaltigeren Rückgang (Beispiele 2000, 2008, 2022, März 2025 mit
  ca. -15%). Unterhalb der 200-Tage-Linie ist historisch zusätzlich die
  Volatilität strukturell höher und die durchschnittliche Rendite
  niedriger als oberhalb – das allein ist aber kein Timing-Signal für
  einen bestimmten Tag. Diese Einordnung immer mit Quellenangabe/
  Recherche-Beleg versehen, nie als eigene Vorhersage ausgeben.
- **Politischer/Wahlkalender (langfristiger Horizont, nicht täglich neu
  recherchiert – Pflege im Wochenfazit, nur Erinnerungs-Hinweis im
  Trigger-Check ab ca. 14 Tage vorher):** US-Midterms (2026-11-03) als
  nächster großer marktrelevanter Termin – historisch häufig erhöhte
  Volatilität im Vorfeld, tendenziell Erleichterungs-/Rally-Muster nach
  Auflösung der Unsicherheit, aber KEINE verlässliche Regel für jeden
  Zyklus (auch hier keine erfundene Erfolgsquote angeben). Zusätzlich
  regionale Wahlen/politische Termine mit Relevanz für gehaltene
  Positionen im Blick behalten (u.a. Indonesien/Bank Central Asia,
  Brasilien/Argentinien-Umfeld/MercadoLibre, EU/Deutschland wegen
  Allianz/Münchener Rück/ASML), sowie US-Fiskalrisiken (Debt-Ceiling-
  Fristen, Shutdown-Risiko), falls terminlich absehbar.
- **Fed-/Notenbank-Zinspfad, nicht nur reaktiv bei Überraschungen:**
  vollständiger FOMC-Terminkalender (2026: 27.-28.01, 17.-18.03,
  28.-29.04, 16.-17.06, 28.-29.07, 15.-16.09, 27.-28.10, 08.-09.12 –
  März/Juni/September/Dezember inkl. Summary of Economic Projections/
  Dot Plot) in `depot/macro_context.md` mitführen, aktueller Fed-Funds-
  Zielkorridor immer aktuell halten, vor jeder Sitzung kurz auf
  markt-implizite Erwartungen (falls recherchierbar, z.B. über
  CME-FedWatch-artige Quellen) hinweisen. Ergänzend die EZB- und (wegen
  starker Japan-Gewichtung im Depot) BoJ-Sitzungstermine im selben
  Kalender mitführen.
- **Weitere Dimensionen (eigenständig ergänzt, da Brian selbst nicht
  jede einzelne benennen konnte):** US-Dollar-Index (DXY) als breiteres
  FX-Risikosignal zusätzlich zu EUR/USD (relevant für die LatAm-/EM-/
  Asien-Positionen); High-Yield-Credit-Spreads als Frühindikator für
  Risk-off-Stimmung (läuft VIX teils voraus); Öl/Energiepreis als
  Inflations-/Konjunktur-Frühindikator; chinesische Regulatorik-/
  Konjunktur-Nachrichten (Exportkontrollen, PBoC-Maßnahmen) wegen der
  Halbleiter-/Tech-Lastigkeit des Depots. Diese vier NICHT täglich in
  voller Tiefe recherchieren (Aufwand/Nutzen), sondern als Teil des
  wöchentlichen Wochenfazit-Makro-Blicks pflegen und nur bei einer
  offensichtlichen akuten Auffälligkeit vorzeitig in den täglichen
  Check ziehen.
- **Beratungs-Charakter (Brian, 2026-09-03: "du kannst mich ausführlich
  beraten, mit entsprechenden Argumenten"):** die tägliche/wöchentliche
  Makro-Einordnung soll nicht nur Zahlen auflisten, sondern eine
  begründete Einschätzung mit Argumenten liefern (z.B. "Fear&Greed im
  Greed-Bereich UND S&P deutlich über der noch steigenden 200-Tage-
  Linie spricht eher für Fortsetzung des Trends, ABER die enge
  Kombination mit hoher Bewertung mehrerer Depot-Schwergewichte
  rechtfertigt trotzdem eher normale Tranchierung statt Euphorie-
  Nachkäufe" statt nur "Fear&Greed: 62"). Bleibt dabei innerhalb der
  bestehenden Grenze: begründete Einschätzung/Diskussionsgrundlage für
  Brians eigene Entscheidung, keine professionelle Anlageberatung im
  regulatorischen Sinn und kein Ersatz dafür.

[E] EXIT-/GEWINNMITNAHME-/NACHKAUF-CHECK für bestehende Depot-Positionen
    (2026-08-29, von Brian gefordert – siehe "Verkaufsdisziplin &
    Gewinnmitnahme-Regeln" unten für die volle Logik inkl. der 2026-08-29
    ergänzten Kaufseite) – kombiniert [B] (These noch intakt?) mit dem
    technischen Bild aus Twelve Data:
     → These gebrochen (K-Kriterien/Moat dauerhaft verletzt, Betrug/
       Regulatorik-Treffer, Übernahme/Delisting)? → VERKAUF ERWÄGEN, auch bei
       Buchverlust – "hoffen, dass es sich erholt" ist keine Strategie.
     → These intakt, aber Bewertung/Chart deutlich überzogen (Kurs weit über
       TMR-Fair-Value UND technisch überhitzt, z.B. RSI dauerhaft >70, Kurs
       weit über 20/50-Tage-Linie, Position dazu evtl. schon über der
       10%-Positionsgrenze) → TEILVERKAUF/GEWINNMITNAHME ERWÄGEN, kein
       Komplettausstieg bei intakter These.
     → These intakt, aber Kurs deutlich UNTER TMR-Fair-Value UND/oder
       technisch überverkauft/Bodenbildung erkennbar (siehe
       "Chartmuster-Erkennung") → NACHKAUF ERWÄGEN (unterbewertet) –
       ausdrücklich nur, wenn [B] die These als intakt bestätigt; ein
       niedriger Kurs bei gebrochener These ist kein Nachkauf-Signal,
       sondern fällt unter VERKAUF ERWÄGEN oben.
     → Rein technische Warnsignale ohne fundamentalen Bruch (z.B. bärischer
       MACD-Crossover auf hohem Volumen, Bruch einer wichtigen
       Unterstützungszone) → BEOBACHTEN ENGER, noch kein Handlungsaufruf.
     → Sonst: HALTEN.

→ NUR bei etwas Meldenswertem (nicht bei "alles unverändert") schickt der Agent
  Brian proaktiv eine kurze Nachricht (Kurz-Fazit-Format, siehe Pipeline-Schritt 5):
  z.B. Rating-Verschlechterung, gerissener Stop-These-Trigger, Watchlist-Position
  jetzt im Kaufbereich, wichtige Nachrichtenlage, oder eine der [E]-Kategorien
  außer HALTEN.
```

### Technische Analyse via Twelve Data (2026-08-29 gefordert, 2026-08-30 LIVE verbunden)

Brian will, dass der Agent Depot- UND Watchlist-Werte auch technisch
einschätzt (nächste Unterstützungs-/Widerstandszonen, MACD, Volumen, "alles
was zur technischen Analyse dazugehört"), um Chancen/Risiken und speziell
Gewinnmitnahme-/Verkaufs-Timing besser zu beurteilen. Es gibt keinen
offiziellen TradingView-Konnektor; nach Rücksprache mit Brian (2026-08-29)
wurde stattdessen der **Twelve Data MCP-Connector** angebunden (Echtzeitkurse
+ 60+ technische Indikatoren, u.a. MACD, RSI, SMA/EMA, Bollinger-Bänder,
Volumen, Pivot-Punkte/Support-Resistance, ATR, Stochastic, ADX, VWAP und
weitere).

**Status (2026-08-30): LIVE.** Brian hat den Connector über claude.ai
verbunden (OAuth, kein manueller API-Key nötig). Verifiziert per Testabfrage
auf ServiceNow (NOW): `auth_status` bestätigt, `get_quote` und
`get_technical_indicator` (MACD, BBANDS) liefern echte aktuelle Werte statt
Schätzungen. API-Kontingent: 800 Credits/Tag im aktuellen Plan, davon zum
Testzeitpunkt 1 verbraucht – für den täglichen Monitoring-Kreislauf (18
Depot-Positionen + Watchlist) mehr als ausreichend, wird aber im Blick
behalten (`get_api_usage`), falls die Nutzung mit wachsender Watchlist
spürbar steigt. Damit ist der zuvor einzige noch offene technische Punkt
erledigt – die bisherige Fallback-Praxis (grobe Chart-Einschätzung per
WebSearch/WebFetch, ohne strukturierte Indikator-Werte) entfällt ab sofort,
alle unten genannten Stellen nutzen ab jetzt Twelve Data als Datenbasis.

**Wo das reingespielt wird:**
- **TA-Prompt-Modul ("Jack, Pure Technical Analyst", jetzt v1.10, siehe
  Abschnitt 2)** nutzt ab jetzt echte Live-Indikatoren aus Twelve Data statt
  geschätzter Werte als Grundlage für SWING-/INVESTOR-ENTRY-Einschätzungen.
- **[C] ENTRY/TIMING-CHECK** (Watchlist) und **[E] EXIT-/GEWINNMITNAHME-CHECK**
  (Depot, siehe unten) im täglichen Monitoring-Kreislauf.
- **3-fach-Cross-Check-Analysen** (Pipeline-Schritt 3): TA-Bein bekommt
  Twelve-Data-Kennzahlen als Input, damit alle drei KI-Stimmen dieselbe
  technische Datenbasis nutzen statt unterschiedlicher Schätzungen.
- **Wöchentliches Wochenfazit**: kurzer technischer Kommentar je auffälliger
  Position (nicht für alle 18+ Positionen jede Woche im Detail, um den
  Report nicht zu überladen — Priorität auf Positionen mit [E]-Handlungs-
  empfehlung ungleich HALTEN oder mit auffälligem technischem Signal).
- **Talent/Zock-Stop-Loss-Ausweisung (siehe "Kategorie-spezifischer
  Exit-Ansatz für Talent/Zock" unten):** ab jetzt aktiv – jede Talent/Zock-
  Position bekommt ein Stop-Loss-Niveau ausgewiesen, bei "Talent
  (langfristig)" weiterhin als Sicherheitsnetz gekennzeichnet, nicht als
  primäres Handlungssignal.
- **Chartmuster-Erkennung (Bodenbildung, Doppeltop, siehe unten):** wird ab
  jetzt anhand echter Kursdaten bestätigt statt nur aus grober
  WebSearch-Chart-Beschreibung.

**Bis 2026-08-30** galt hier noch die grobe Chart-Einschätzung per
WebSearch/WebFetch auf Finanzseiten als Fallback ohne strukturierte
Indikator-Werte – seit der Live-Verbindung entfällt dieser Fallback für alle
Werte, die Twelve Data abdeckt (US-/internationale Standard-Ticker); nur für
den seltenen Fall, dass ein einzelner Depot-/Watchlist-Wert dort nicht
geführt wird, bleibt die WebSearch-Schätzung als Ausnahme bestehen und wird
dann weiterhin explizit als ungenauer gekennzeichnet.

### TA-Pflicht bei JEDER Einzelanalyse inkl. Ad-hoc-Quick-Filter + "Chart- und Einstiegslage"-Sektion (2026-08-31, von Brian gefordert)

**Lücke, die diesen Eintrag ausgelöst hat:** Bei der Disco-Corp-Analyse
(6146.T, 2026-08-31) hat der 3-fach-Cross-Check (Jarvis/Jack/Conan) rein
fundamental gearbeitet – keine der drei KIs hat das TA-Modul/Twelve Data
für Unterstützungs-/Widerstandszonen herangezogen, und der Kurs wurde nur in
JPY genannt, nicht zusätzlich in EUR (Verstoß gegen die bereits bestehende
Regel "Einheitliche EUR-Umrechnung", siehe Pipeline-Schritt [3] oben – dort
bislang nur für Depot-/Watchlist-Monitoring gelebt, nicht für eine frei von
Brian angestoßene Einzelanalyse). Brian hat daraufhin eine fremde
Beispiel-PDF geteilt (Research-Report eines Dritten zu "Alimentation
Couche-Tard Aktienanalyse", 2026-08-26, dortiges Kapitel "7. Chart- und
Einstiegslage") und dabei ausdrücklich klargestellt (2026-08-31, analog zur
früheren Raketentoni-Klarstellung bei "PDF-Report-Design" unten): Diese
fremde PDF dient AUSSCHLIESSLICH als lose inhaltliche Inspiration dafür,
DASS eine solche Sektion existieren soll (Trend-/Zonen-Ampel + konkrete
Unterstützungs-/Widerstandszonen + Verknüpfung mit der fundamentalen
Bewertung) – KEIN 1:1-Layout- oder Struktur-Klon. Aufbau, Tabellen-
Formulierungen, Bezeichnungen und Optik dieser Sektion bleiben unser
eigenes, im Rest dieses Regelwerks etabliertes Agent-Vokabular (Ampel-
Farbwelt, Beobachten-Protokoll-Sprache, Agent-Score-Logik usw.), nicht die
Gliederung/Wortwahl der fremden Vorlage.

**Ab sofort gilt (gilt für Quick-Filter GENAUSO wie für Full Deep Dive –
anders als DCF/Vollformat-Zusatzmodule ist dieser Schritt NICHT
überspringbar):**

1. **TA-Modul ist Pflichtbestandteil jeder Einzelanalyse**, unabhängig davon,
   ob sie von Brian ad-hoc angestoßen ("analysiere mir XY") oder vom
   täglichen/wöchentlichen Trigger automatisch ausgelöst wird, und
   unabhängig von Quick-Filter- oder Full-Deep-Dive-Tiefe. Datenbasis:
   Twelve Data (`get_technical_indicator` für EMA20/50/200, Bollinger-Bänder,
   RSI, MACD, ATR; `get_time_series`/Pivot-Punkte für Unterstützung/
   Widerstand), analog zum bestehenden TA-Prompt-Modul ("Jack, Pure
   Technical Analyst" v1.10, siehe Abschnitt 2). Nur wenn Twelve Data den
   Ticker nachweislich nicht führt (seltener Ausnahmefall, siehe oben),
   entfällt dieser Schritt – dann aber explizit als Lücke vermerkt, nicht
   stillschweigend ausgelassen.
2. **Eigene Sektion "Chart- und Einstiegslage"** in jeder Einzelanalyse
   (Markdown-Datei UND Agent-Kompakt-PDF) – der Name der Sektion und die
   Grundidee (Trend-Ampeln + Zonen-Tabelle) sind von der fremden Vorlage
   inspiriert, die konkrete Umsetzung ist aber komplett eigenständig in
   unserer bereits etablierten Agent-Optik/-Terminologie zu halten (gleiche
   Vorgehensweise wie beim Wochenreport-Layout ggü. Raketentoni, siehe
   "PDF-Report-Design" unten – dort ebenfalls "nur lose Inspiration, kein
   1:1-Klon"): Ampel-Zeilen für Langfrist-/Mittelfristtrend,
   Momentum, Volatilität, GEFOLGT von einer Tabelle konkreter
   Unterstützungs-/Widerstandszonen (Zone → Bedeutung/technischer Bezug
   [z.B. EMA20/Bollinger-Mitte, letzter Pivot, EMA50/unteres Bollinger-Band]
   → mögliche Marktreaktion).
   **Echtes Chart-Bild (seit 2026-09-01, Pflicht wo Zeitreihendaten
   vorliegen):** zusätzlich zu den Tabellen wird ein echter Candlestick-Chart
   gerendert und in die PDF-Sektion eingebettet – `get_time_series` (Twelve
   Data, 120-180 Tage) abrufen, Rohausgabe in eine Datei schreiben, dann
   `python3 reports/render_chart.py --json <Datei> --out reports/<TICKER>_chart.png
   --ema 20,50 --zone "<Kurs>:<Label>" --title "<TICKER> -- <Börse>"`
   ausführen (Details/Format im Skript-Docstring). Ersetzt die bisher reine
   Tabellen-Optik durch ein echtes Bild, im Agent-Design statt
   Fremd-Screenshot.
   **Bei Full Deep Dive zusätzlich Pflicht (seit 2026-09-08, siehe "Agent
   Deep Dive Report" unten):** denselben Befehl um `--rsi --macd` ergänzen
   → rendert zwei zusätzliche RSI(14)-/MACD(12,26,9)-Subplots unter dem
   Hauptchart. Bei Quick Filter/Ampel-Batch-Scan entfallen beide Flags
   weiterhin (einfacher Haupt-Chart reicht dort, Renderzeit klein halten).
   **ADR-Fallback bei Twelve-Data-Plan-Sperre (2026-09-08, am echten
   Testfall DISCO Corp/6146 gefunden):** liefert `get_time_series` für die
   native Notierung die Meldung "requires upgrading to Pro/Venture plan"
   (typischerweise bei Tokyo/TSE- und anderen nicht-US-Börsenplätzen), NICHT
   aufgeben oder auf synthetische/erfundene Daten ausweichen. Stattdessen:
   `search_symbol` mit dem Firmennamen bzw. Ticker + Zusatz "ADR" aufrufen,
   um eine im Standard-Plan verfügbare ADR-Notierung zu finden (z.B. DISCO
   Corp/6146 → **DSCSY**, OTC, USD). Chart/Kurszahlen dann auf Basis der
   ADR erzeugen, mit **explizitem Hinweis im Titel/Label** ("6146 /
   DSCSY-ADR"), damit klar bleibt, dass die Datenquelle die ADR und nicht
   die native TSE-Notierung ist (ADR-Kurse können minimal von der nativen
   Notierung abweichen: Zeitzonenversatz, ADR-Ratio, ADR-Gebühren). Gilt
   nur als Chart-/Zeitreihen-Fallback – Fundamentaldaten (Bilanz,
   Geschäftsbericht) weiterhin bevorzugt aus Primärquellen der Heimatbörse
   recherchieren, siehe Datenintegritäts-System. Findet sich auch keine
   ADR/Cross-Listing, entfällt das Chart-Bild für diese Analyse ersatzlos
   mit Vermerk "kein Zeitreihen-Zugang verfügbar" – kein Platzhalter-Chart.
3. **Kombinierte Einstiegszonen-Empfehlung (technisch + fundamental):** Nicht
   nur die reine Charttechnik nennen, sondern explizit verknüpfen mit der
   TMR-/Scout-Fair-Value-Einschätzung (Bear/Base/Bull) bzw. der Margin-of-
   Safety-/Unterbewertungs-Einschätzung aus dem DNA-/Bewertungs-Check –
   analog zum bestehenden "INVESTOR-ENTRY-Handoff" und den
   "Einstiegszonen bei NACHKAUF ERWÄGEN" weiter unten, aber jetzt explizit
   auch für brandneue Watchlist-Kandidaten ohne Kaufhistorie, nicht nur für
   bereits gehaltene/schon länger beobachtete Positionen. Format:
   mindestens 2 gestaffelte Zonen (z.B. "erste Unterstützung/moderateres
   Signal" und "tiefere Zone/stärkeres Signal, sofern These intakt
   bleibt"), jede mit kurzer Begründung, warum sie technisch UND
   fundamental attraktiv wäre – nicht nur eine Zahl ohne Kontext.
4. **EUR-Durchgängigkeit ausdrücklich auch hier:** Jede in dieser Sektion
   genannte Zahl (Unterstützungs-/Widerstandszonen, Einstiegszonen,
   Stop-Loss-Niveaus) folgt der bereits bestehenden Regel "Einheitliche
   EUR-Umrechnung" (Originalwährung zuerst, EUR-Gegenwert in Klammern,
   Wechselkurs-Quelle+Datum) – keine Ausnahme mehr für ad-hoc angestoßene
   Einzelanalysen wie bisher bei Disco.
Diese Ergänzung ändert nichts an der bereits bestehenden Charttechnik-Logik
für Depot-/Watchlist-Monitoring (siehe "Verkaufsdisziplin &
Gewinnmitnahme-Regeln" unten) – sie schließt nur die Lücke, dass eine frei
angestoßene Einzelanalyse (Quick Filter wie Disco) bisher nicht denselben
TA+EUR-Standard erfüllen musste wie der laufende Monitoring-Kreislauf.

### IPO-Lock-up-/Overhang-Check, Post-IPO-Datenlücken-Konfidenz & No-False-Precision-Regel (2026-08-31, ausgelöst durch Vincorion-Fallstudie)

**Lücke, die diesen Eintrag ausgelöst hat:** Brian hat eine fremde
Drittanalyse ("Szenarios_Vincorion.pdf", Fact-Check/Verfeinerung einer
Forumsthese zum STAR-Capital-Lock-up bei Vincorion SE/V1NC) hochgeladen und
gebeten, den Kandidaten zusätzlich über unser eigenes 3-KI-System (Jarvis/
Jack/Conan) zu prüfen und gegen die fremde Analyse zu spiegeln, um daraus
Systemverbesserungen abzuleiten (Einzelanalysen:
`VNC-TMR-quickfilter-jarvis-claude-2026-08-31.md`,
`-jack-gemini-2026-08-31.md`, `-conan-chatgpt-2026-08-31.md`; volle
Cross-Check-Gegenüberstellung inkl. PDF-Vergleich:
`VNC-cross-check-fazit-2026-08-31.md`). Wie schon bei der Alimentation-
Couche-Tard-PDF gilt: die fremde PDF dient AUSSCHLIESSLICH als Anstoß/lose
Inspiration, nicht als 1:1-Vorlage — Wortwahl, Tabellenformate und
Score-Logik bleiben unser eigenes Agent-Vokabular.

Vincorion (IPO 20.03.2026, <6 Monate Handelshistorie zum Analysezeitpunkt,
STAR Capital hält 48,63% mit auslaufendem 180-Tage-Lock-up) hat zwei
strukturelle Lücken im bisherigen Regelwerk sichtbar gemacht, die weder das
Standard-K-Basis-Raster noch die Scout-DNA (Conan-the-Scout, für
vorbörsliche/Pre-Revenue-Kandidaten gedacht) sauber abdecken: (a) ein
Sondersituations-Risiko (PE-Sponsor-Overhang nach Lock-up-Ende), für das es
bisher kein eigenes Prüfmodul gab, und (b) eine Datenlücken-Ursache
("Unternehmen erst seit wenigen Monaten börsennotiert"), die das Regelwerk
bisher identisch wie gewöhnliche Intransparenz (Disco-Fall: Capex/Umsatz,
CCC nicht auffindbar) behandelt hätte, obwohl beides analytisch
grundverschieden ist. Zusätzlich fiel im 3-KI-Cross-Check UND in der
fremden PDF ein wiederkehrendes Muster auf: alle Beteiligten (Jack ~90%+,
Conan ~70-80%, die fremde PDF ~50/25/15/7/3% je Szenario) neigten dazu,
für ein grundsätzlich nicht statistisch herleitbares Verkäuferverhalten
(wird ein PE-Fonds nach Lock-up-Ende verkaufen, und wie?) konkrete
Prozent-Wahrscheinlichkeiten zu erfinden — nur Jarvis verzichtete bewusst
darauf und lieferte nur eine Rangfolge. Da drei von vier unabhängigen
KI-Antworten zur Schein-Präzision neigten, ist das ein systematischer
Bias, der eine feste Regel braucht, keine Einzelfall-Disziplin.

**Ab sofort gilt:**

1. **Neues Prüfmodul "IPO-Lock-up-/Overhang-Check"**, auszulösen immer wenn
   ALLE folgenden Bedingungen zutreffen: (a) Börsengang/Spin-off vor
   weniger als 24 Monaten, (b) ein einzelner Alt-Eigentümer (PE-Sponsor,
   Gründerfamilie, Konzernmutter bei Spin-off) hält nach IPO weiterhin
   >25%, (c) eine vertragliche oder marktübliche Lock-up-Frist mit
   bekanntem/geschätztem Ablaufdatum besteht. Pflichtinhalte, im Quick-
   Filter als eigene Sektion "🔓 IPO-Lockup-/Overhang-Analyse":
   - **Overhang-Größe vs. Liquidität** ("Tage-zum-Liquidieren": Alt-
     eigentümer-Bestand ÷ durchschnittliches Tagesvolumen der letzten
     ~3 Monate) als objektive Kennzahl dafür, ob ein Börsenverkauf
     überhaupt praktikabel ist oder zwingend eine Blockplatzierung
     (Accelerated Bookbuild) nötig wird.
   - **Szenario-Wahrscheinlichkeits-Leiter** (z.B. Teilblock-Platzierung /
     Abwarten / gestaffelte Platzierungen / Nahezu-Komplettausstieg /
     sukzessiver Börsenverkauf) — **als Rangfolge/Richtung, NICHT als
     Prozentzahlen**, außer eine benannte, datierte Primärquelle
     veröffentlicht selbst eine belastbare Zahl (siehe Regel 3 unten).
   - **Block-Discount-Sensitivitätstabelle**: Ausgangskurs × plausible
     Discount-Bandbreite (branchenüblich, mit Quellenverweis) → sich
     ergebender Platzierungskurs, explizit als Rechenbeispiel getaggt,
     keine Kursprognose.
   - **Bereits-eingepreist-Einschätzung** (qualitativ: nicht / teilweise /
     vollständig) unter Verweis auf bereits erfolgte Kursabschläge und
     ggf. explizite Analysten-Kommentare zum Overhang als Bewertungsdeckel.
   - **Cornerstone-/Anker-Investor-Qualitätssignal**: bereits vor dem
     Lock-up-Ereignis engagierte, benannte institutionelle Investoren
     (z.B. Fidelity, Invesco, T. Rowe Price bei Vincorion) reduzieren —
     ersetzen aber nicht — das Platzierungsrisiko, weil ein
     institutionelles Käuferbuch nachweislich bereits existiert. Dies ist
     ein qualitativer Kontextpunkt, kein eigenes K/E-Scoring-Kriterium.
2. **Neue Konfidenz-Kategorie "N/V wegen kurzer Handelshistorie" (Post-IPO-
   Datenlücke), getrennt von normalem N/V:** Wenn eine Kennzahl fehlt, WEIL
   das Unternehmen strukturell noch keine ausreichend lange Berichtshistorie
   als eigenständiger Börsenwert hat (i.d.R. <2 Jahre bzw. <2 testierte
   Jahresabschlüsse als Public Company — typisch betroffen: 3-5J-CAGR,
   Piotroski F-Score, historischer ROIC/ROCE-Trend, Beta, Management-Score),
   wird das explizit als **"N/V wegen kurzer Handelshistorie"** statt als
   generisches N/V getaggt — zur Abgrenzung von "N/V" im Disco-Sinne (Daten
   existieren, wurden aber nicht offengelegt/gefunden — ein
   Beschaffungs-/Transparenzproblem). Beide Fälle führen weiterhin zum
   GLEICHEN mechanischen Konfidenz-Deckel (🔴 NIEDRIG bei Überschreiten der
   üblichen N/V-Schwelle → Tier ≤3, Agent Score ≤6, EDGE-Deckel ≤🟡 —
   unverändert ggü. bestehender Regel), aber der Tag macht in der Analyse
   selbst transparent, DASS der Deckel eine Reifegrad-Frage ist, kein
   Warnsignal über die Unternehmensqualität — wichtig für die spätere
   Neubewertung, sobald die Historie lang genug ist (Re-Evaluation-Trigger:
   sobald 2 volle Geschäftsjahre als Public Company vorliegen, automatisch
   auf normale K-Basis-Prüfung zurückwechseln, nicht dauerhaft gedeckelt
   lassen).
3. **No-False-Precision-Regel für Verkäufer-/Akteursverhalten:** Wenn eine
   Analyse das künftige Verhalten eines identifizierbaren Akteurs
   einschätzen muss (PE-Sponsor-Exit, Insider-Verkauf, M&A-Wahrscheinlich-
   keit u.ä.) OHNE eine belastbare statistische Grundlage (z.B. eine
   veröffentlichte Verkaufsabsichtserklärung, ein SEC-Filing mit Termin),
   ist die Einschätzung als **Rangfolge + Richtung** auszudrücken (z.B.
   "am wahrscheinlichsten... deutlich möglich... unwahrscheinlich, aber
   nicht ausgeschlossen"), NICHT als erfundene Prozentzahl (z.B. "70-80%
   Wahrscheinlichkeit") — auch wenn eine befragte Fremd-KI (Jack, Conan)
   oder eine vom Nutzer hochgeladene Drittquelle das tut. Ausnahme: die
   Prozentzahl stammt selbst direkt und zitierfähig aus einer benannten,
   datierten Primärquelle (z.B. ein Analysten-Report, der explizit "wir
   schätzen X% Wahrscheinlichkeit" schreibt) — dann wird sie als Zitat mit
   Quellenangabe übernommen, nicht als eigene Herleitung ausgegeben.
   Hintergrund: im Vincorion-Cross-Check griffen 2 von 3 KIs (Jack, Conan)
   UND die vom Nutzer hochgeladene Drittanalyse unabhängig voneinander zu
   erfundenen Prozentzahlen — nur Jarvis hielt sich an Rangfolge ohne
   Zahlen. Das zeigt, dass Schein-Präzision ein systematisches Muster ist,
   das eine feste Regel statt Einzelfall-Disziplin braucht.
4. **Katalysator-gebundene Einstiegszonen als zulässiges Alternativformat:**
   Wenn ein bekanntes, terminierbares Ereignis (Lock-up-Ablauf,
   Earnings-Termin, Zulassungsentscheid) das kurzfristige Kursbild
   dominiert, dürfen Einstiegszonen explizit an dieses Ereignis gebunden
   werden (z.B. "Zone X, falls Blockplatzierung mit Y% Discount erfolgt")
   statt ausschließlich rein technische Niveaus (EMA/Pivot) zu nennen —
   ergänzt, ersetzt aber nicht die bestehende TA-Pflicht-Sektion "Chart-
   und Einstiegslage" (siehe oben) für den technischen Blickwinkel.

Diese Ergänzung ändert nichts an der bestehenden Standard-K-Basis-Logik für
reguläre (>2 Jahre börsennotierte) Kandidaten und nichts an der separaten
Scout-DNA (Conan-the-Scout, für vorbörsliche Deep-Tech-Kandidaten) — sie
schließt nur die Lücke für den spezifischen Zwischenfall "profitabel,
schnell wachsend, aber erst seit kurzem börsennotiert mit PE-Overhang", der
bisher weder ins Standard- noch ins Scout-Raster passte.

### Verständlichkeit der Kurz-Fazits & PDF-Fazits: Analyse dahinter muss nachvollziehbar sein, Vorbild Raketentonis Erzählstil (2026-08-31, von Brian gefordert, ausgelöst durch "HawkEye360Szenarien.pdf")

**Lücke, die diesen Eintrag ausgelöst hat:** Brian hat eine von Raketentonis
Agent erstellte HawkEye-360-Analyse ("HawkEye360Szenarien.pdf") hochgeladen.
Die Faktenbasis wurde gegengecheckt (Lock-up-Termin 2. September, Russell-
2000-Aufnahme 21. September, Q2-Zahlen, Aktionärsstruktur — alles bestätigt).
Danach hat Brian ausdrücklich gefordert: die ANALYSE-TIEFE UND DER PROZESS
bleiben exakt wie bisher (Full Deep Dive, Quick Filter, Ampel-Batch-Scan,
Blitz-Scan-Voreinschätzung — je nach Anlass unverändert), aber die
ABSCHLIESSENDE ZUSAMMENFASSUNG (Chat-Kurz-Fazit UND das Fazit-/Verdict-
Element im PDF) soll sich in Formulierung und Satzbau an Raketentonis
erzählerischem Stil orientieren — NICHT 1:1 übernommen, sondern "auf unsere
Art". Wie schon bei der Vincorion-Fallstudie und beim Ampel-Batch-Layout
gilt: eine fremde Vorlage ist Anstoß, kein Klon-Auftrag.

**Wichtige Abgrenzung (von Brian auf Nachfrage bestätigt, 2026-08-31): die
No-False-Precision-Regel (siehe IPO-Lock-up-/Overhang-Check oben) bleibt
vollständig in Kraft.** Raketentonis Stil arbeitet mit erfundenen Szenario-
Prozentzahlen (z.B. "55% Wahrscheinlichkeit"). Das übernehmen wir explizit
NICHT. Wahrscheinlichkeitsartige Einschätzungen bleiben Rangfolge/Richtung
("am wahrscheinlichsten... deutlich möglich... unwahrscheinlich, aber nicht
ausgeschlossen"), außer eine benannte Primärquelle liefert selbst eine
zitierfähige Zahl. Übernommen wird ausschließlich der ERZÄHLERISCHE STIL und
die STRUKTUR der Zusammenfassung, nicht der Inhalt oder die
Zahlen-Schein-Präzision.

**Eigentliches Ziel dieser Regel (von Brian am 2026-08-31 präzisiert, nachdem
die erste Fassung dieses Eintrags zu sehr nach Stilfrage klang):** Es geht
NICHT darum, dass die Zusammenfassung "netter klingt" oder wie Raketentonis
Agent tönt. Es geht darum, dass Brian beim Lesen die eigentliche Analyse
dahinter wirklich VERSTEHT — warum genau dieser Agent Score, warum genau
diese Ampel-Farbe, warum genau diese Einstiegszone — statt nur auf ein PDF
oder eine Tabellenzeile zu starren und nachfragen zu müssen, was damit
gemeint ist. Die Formulierungsregeln unten (direkte Ansprache, nummerierte
Gedankenschritte, Entscheidung als Antwort auf eine Frage) sind Mittel zu
diesem Zweck, kein Selbstzweck. Konkrete Konsequenz: JEDE Erwähnung eines
Scores, einer Ampel-Farbe, einer Kennzahl oder eines Fachbegriffs im
Fließtext der Zusammenfassung muss in einem kurzen Nebensatz mitliefern, was
sie bedeutet und warum sie für die Entscheidung relevant ist — nie eine
nackte Zahl/ein nacktes Label ohne Einordnung stehen lassen. Maßstab: Brian
soll die Zusammenfassung lesen und sofort wissen, worauf sich die Empfehlung
stützt, ohne beim Agenten nachfragen zu müssen.

**Ab sofort gilt für JEDE Abschluss-Zusammenfassung — unabhängig von der
Analyse-Tiefe (Full Deep Dive, Quick Filter, Ampel-Batch-Scan,
Blitz-Scan-Voreinschätzung):**

1. **Kurzfazit zuerst.** Der allererste Satz bzw. die ersten zwei Sätze der
   Zusammenfassung sind die Kernaussage/Handlungsempfehlung selbst, fett
   hervorgehoben — nicht die Herleitung. Beispiel-Duktus: "Für Brian würde
   ich aktuell sagen: [Kandidat] ist fundamental spannend, aber ich würde
   jetzt nicht blind bei [Kurs] kaufen." Erst danach folgt die Begründung.
2. **Direkte Ansprache statt unpersönlicher Tabellenlogik im Fließtext.** Wo
   bisher ein isolierter Fakt stand (z.B. "Depot-Fit: Sektorüberschneidung
   mit Position X"), wird das in einen an Brian gerichteten Satz übersetzt
   ("Das würde bei dir mit [Position X] ins gleiche Sektor-Töpfchen fallen,
   ..."). Betrifft NUR den verbindenden Fließtext, nicht die Pflicht-
   Tabellen selbst (Ampelcheck, DNA-Strang, Agent-Score-Gauge,
   Einstiegszonen-Tabelle) — die bleiben tabellarisch wie bisher.
3. **Kurze, in sich abgeschlossene Gedankenschritte statt Stakkato-
   Stichpunkte**, vor allem im PDF-Fazit-Element bzw. der Agent-Kompakt-
   Einzelseite, wo Platz dafür ist ("Das ist wichtig, weil...", "Genau
   daraus entsteht..."). Im knappen Chat-Kurz-Fazit (weiterhin 5-8 Sätze,
   siehe Pipeline-Schritt 5) reicht ein durchgehender Fließtext-Absatz in
   diesem Duktus statt einer Aufzählung.
4. **Die Entscheidung als Antwort auf eine gestellte Frage formulieren**,
   wenn ein konkretes Timing-/Kauf-Dilemma vorliegt: "Wenn Brian mich
   fragt: 'Soll ich heute kaufen oder abwarten?' — dann lautet meine
   Antwort: ..." mit kurzer Best-Case-/Worst-Case-Gegenüberstellung des
   Wartens in Prosa, nicht als Tabelle.
5. **Abschließende Status-Zeile mit Ampel + Ein-Satz-Begründung**, getrennt
   nach kurz- und mittelfristiger Einschätzung, falls diese auseinander-
   fallen (z.B. "kurzfristig 🟠, mittelfristig eher 🟢") — Ampel-Farben und
   -Bedeutung bleiben unser etabliertes Agent-Vokabular (siehe die
   verschiedenen Ampel-Skalen oben), nicht Raketentonis eigene Ampel-Achse.
6. **Keine Einschränkung der Pflichtinhalte.** Alle bisher vorgeschriebenen
   Bestandteile des Kurz-Fazits (Pipeline-Schritt 5: Rating+Timing-Ampel,
   Haupttreiber, Depot-Fit, Konvergenz-Status, klare Handlungsempfehlung)
   bleiben Pflicht — diese Regel ändert nur, WIE sie in Sätze gefasst
   werden, nicht WAS gesagt werden muss.
7. **Keine unerklärte Zahl, keine unerklärte Fachvokabel.** Jede
   Score-/Ampel-/Kennzahlen-Erwähnung im Fließtext bekommt eine kurze
   Einordnung mitgeliefert (Beispiel: "Agent Score 7/10 — das heißt: solide
   Substanz, aber kein Ausnahmewert" statt nackt "Agent Score: 7/10").
   Gleiches gilt für Fachbegriffe (EBITDA-Marge, Free Float, Lock-up,
   Overhang, EDGE-Deckel usw.) bei der ersten Erwähnung in einer
   Zusammenfassung: ein Halbsatz Erklärung, was der Begriff hier konkret
   bedeutet. Test vor Auslieferung: Könnte Brian nach dem Lesen der
   Zusammenfassung (ohne die Detail-Tabellen daneben zu legen) einer
   dritten Person erklären, warum die Empfehlung so lautet? Wenn nein,
   fehlt eine Einordnung, und der Absatz muss nachgebessert werden.

Diese Regel gilt sowohl für den Chat-Kurz-Fazit (Pipeline-Schritt 5) als
auch für das Fazit-/Verdict-Element im Agent-Kompakt-PDF sowie im
Wochenfazit/Monatsrecap — überall dort, wo der Agent Brian gegenüber eine
eigene, wertende Schlussfolgerung formuliert. Reine Fakten-/Kennzahlen-
Tabellen (Fact-Pack, Ampelcheck, DNA-Strang, Bilanz-Kennzahlen) sind von
dieser Regel nicht betroffen und bleiben tabellarisch/kompakt wie bisher.

### Verkaufsdisziplin & Gewinnmitnahme-Regeln (2026-08-29, von Brian gefordert)

Bisher lag der Fokus des Regelwerks stark auf der Kaufseite (TMR/Scout/TA
als Filter für neue Positionen). Brian will jetzt genauso systematisch die
Verkaufsseite für bestehende Depot-Positionen: erkennen, wann ein Kurs
bereits eingepreist ist ("zu hoch bewertet"), wann eine Gewinnmitnahme
(auch nur Teilverkauf) sinnvoll ist, und wann ein Verkauf – auch mit Verlust
– in Erwägung gezogen werden sollte, weil die ursprüngliche These gebrochen
ist. Das ist keine neue vierte KI-Stimme, sondern eine explizite
Auswertungs-Ebene, die TMR-Fundamentaldaten (Fair-Value, K-Kriterien, Exit-
Trigger) mit dem technischen Bild aus Twelve Data (siehe oben) kombiniert.

**Antizyklisches Grundprinzip (2026-09-01, von Brian explizit bestätigt und
verallgemeinert):** Für Champions, Profi und Talent-Positionen mit Tag
"Talent (langfristig)" gilt als Standardhaltung: wird ein Wert vom Markt
abgestraft (Kursrückgang wegen hoher Bewertung, enttäuschendem Ausblick,
Sektor-Rotation, allgemeiner Marktschwäche o.ä.), OBWOHL die fundamentale
Lage laut aktuellem [B] THESE-CHECK weiterhin intakt ist (DNA-Kriterien,
Moat, Kernthese unverändert bestätigt), wird das NICHT als Warnsignal
gelesen, sondern als potenzielle Kaufgelegenheit – das ist inhaltlich
bereits Kategorie 1 unten (NACHKAUF ERWÄGEN), hier nur als bewusstes,
allgemeines Grundprinzip benannt statt nur als Einzelkategorie. **Ausdrückliche
Ausnahme für Talent/Zock mit Tag "Zock/Trade"** (siehe Abschnitt 3,
"Zeithorizont-Tag innerhalb Talent/Zock"): bei diesen bewusst kurzfristig-/
momentum-getriebenen Positionen darf – je nach Situation – auch in Stärke
statt nur in Schwäche gekauft werden (Momentum-Bestätigung als eigenständiges
Kaufsignal, nicht nur Rücksetzer). Das ist kein Widerspruch zum
antizyklischen Grundprinzip, sondern folgt derselben Logik wie beim bereits
etablierten unterschiedlichen Exit-Ansatz dieser Kategorie (charttechnik-/
momentum-primär statt thesenbasiert) – Einstieg UND Ausstieg folgen bei
"Zock/Trade" konsistent der Charttechnik, nicht nur einer der beiden Seiten.
Für "Talent (langfristig)" bleibt dagegen das antizyklische Grundprinzip
unverändert die Norm, wie bei Champions/Profi.

**Anwendung auf die Charttechnik (TA-Modul, 2026-09-01 ergänzt):** Das
TA-Modul (Jack, Pure Technical Analyst, siehe Abschnitt 2) kennt bereits
zwei Modi – SWING (eigenständig, Momentum-/Setup-getrieben) und
INVESTOR-ENTRY (Handoff mit TMR-/Scout-Fair-Values, Preiszonen/Margin-of-
Safety/Entry-Ampel). Diese Modi werden ab sofort explizit an die
Kategorie/den Zeithorizont-Tag der Position gekoppelt, statt nur implizit
davon abzuhängen, ob gerade Fair-Value-Daten vorliegen:
- **Champions / Profi / Talent (langfristig):** TA läuft bevorzugt im
  INVESTOR-ENTRY-Modus (TMR-/Scout-Fair-Value wird dafür aktiv mitgeliefert,
  nicht nur falls zufällig vorhanden). Kaufzonen werden konsistent zum
  antizyklischen Grundprinzip aus Unterstützungs-/Überverkauft-Zonen
  abgeleitet (siehe "Chart- und Einstiegslage"-Sektion, oben) – ein rein
  technisches VETO-Signal (z.B. Überdehnung, bärische Divergenz) deckelt das
  Rating NICHT automatisch, wenn der [B] THESE-CHECK die fundamentale Lage
  weiterhin als intakt bestätigt; es wird im Fazit als Kontext benannt
  ("charttechnisch angeschlagen, fundamental unverändert intakt"), nicht als
  eigenständiger Ausschlussgrund behandelt.
- **Talent/Zock mit Tag "Zock/Trade":** TA läuft im SWING-Modus. Kaufsignale
  kommen hier bevorzugt aus Momentum-/Ausbruchsbestätigung (siehe
  "Chartmuster-Erkennung als aktiver Impuls" oben – Bodenbildung/neuer
  Aufwärtstrend), nicht primär aus Überverkauft-Zonen. Ein technisches
  VETO-Signal wird hier ERNSTER genommen als bei den anderen Kategorien,
  weil die Charttechnik in dieser Kategorie der primäre, nicht nur
  unterstützende Faktor ist (konsistent zum bereits etablierten
  charttechnik-primären Exit-Ansatz dieser Kategorie).

**Fünf Ergebnis-Kategorien je Position (2026-08-29 um die Kaufseite
erweitert, von Brian gefordert: "wenn es überbewertet gibt, muss es
natürlich auch unterbewertete Titel geben")** – ersetzt/ergänzt die
bisherige KAUFEN/BEOBACHTEN/SCHROTT-Skala für bereits gehaltene Positionen:

1. **NACHKAUF ERWÄGEN (unterbewertet)** – das symmetrische Gegenstück zu
   Kategorie 3 unten: These weiterhin intakt, aber der Kurs ist
   (mutmaßlich) günstiger, als fundamental gerechtfertigt ist. Typische
   Trigger-Kombination (nicht jeder einzelne Punkt muss erfüllt sein, aber
   mehrere zusammen erhärten das Signal):
   - Kurs deutlich unter der TMR-Fair-Value-Einschätzung (Base, ggf. sogar
     nahe der Bear-Fair-Value trotz sonst intakter fundamentaler Lage),
   - technisch überverkauft bzw. **Bodenbildung** erkennbar (siehe
     "Chartmuster-Erkennung" oben) – z.B. RSI nachhaltig <30, Rücksetzer auf
     eine wichtige Unterstützungszone ohne fundamentalen Auslöser,
   - Position liegt (auch dadurch) unter der 1%-Mindestgrenze oder deutlich
     unter der ursprünglich vorgesehenen Sizing-Tier-Größe (siehe Abschnitt
     3) – ein natürlicher Anlass, zu prüfen, ob Aufstocken sinnvoll ist.
   **Wichtige Sicherheitsregel (Kapitalerhalt/Disziplin, siehe Abschnitt
   1):** Ein günstiger Kurs allein ist KEIN Nachkauf-Grund, wenn er das
   Symptom einer gebrochenen These ist ("falling knife") – diese Kategorie
   setzt zwingend voraus, dass der [B] THESE-CHECK die Kernthese als
   weiterhin intakt bestätigt. Ist die These fraglich oder gebrochen, gilt
   stattdessen Kategorie 5 (VERKAUF ERWÄGEN), nicht diese Kategorie – ein
   niedriger Kurs rechtfertigt niemals automatisch einen Nachkauf.
2. **HALTEN** – These intakt, Bewertung/Chart unauffällig. Standardfall,
   braucht keine proaktive Meldung.
3. **BEOBACHTEN ENGER** – kein fundamentaler Bruch, aber ein technisches
   Warnsignal (z.B. bärischer MACD-Crossover auf überdurchschnittlichem
   Volumen, Bruch einer wichtigen gleitenden Linie/Unterstützungszone,
   Divergenz zwischen Kurs und Momentum). Wird im Wochenfazit vermerkt,
   noch keine Handlungsempfehlung.
4. **TEILVERKAUF/GEWINNMITNAHME ERWÄGEN** – These weiterhin intakt, aber der
   Markt hat (mutmaßlich) schon mehr eingepreist, als fundamental
   gerechtfertigt ist. Typische Trigger-Kombination (nicht jeder einzelne
   Punkt muss erfüllt sein, aber mehrere zusammen erhärten das Signal):
   - Kurs deutlich über der TMR-Fair-Value-Einschätzung bzw. Reverse-DCF
     impliziert unrealistisches künftiges Wachstum,
   - technisch überhitzt (z.B. RSI nachhaltig >70, Kurs weit über der
     50-Tage- bzw. 200-Tage-Linie ausgedehnt, Kurs nahe/über der nächsten
     großen Widerstandszone ohne klaren fundamentalen Auslöser),
   - Position ist (auch dadurch) über die 10%-Positionsgrenze gewachsen
     (siehe Abschnitt 3, Positionsgrößen-Limits) – ein natürlicher Anlass,
     einen Teil der organisch gewachsenen Gewinne mitzunehmen, statt aktiv
     nachzukaufen oder einfach laufen zu lassen.
   Empfehlung ist explizit ein **Teilverkauf**, kein Komplettausstieg – die
   These ist ja noch intakt.
5. **VERKAUF ERWÄGEN (auch mit Verlust)** – die ursprüngliche Investment-
   These ist gebrochen: K-Kriterien/Moat dauerhaft verletzt (nicht nur ein
   schwaches Quartal), Betrugs-/Regulatorik-/Rechtstreit-Treffer mit echtem
   Substanzrisiko, Übernahme/Delisting, oder ein SCHROTT-Rating aus einer
   3-fach-Analyse, das über mehrere Prüfungen hinweg bestehen bleibt (siehe
   z.B. Cellebrite DI Ltd, aktuell SCHROTT-Rating nach Earnings-Miss/
   CEO-Wechsel/Securities-Investigation-Notice – laufender Prüffall für diese
   neue Exit-Logik). Ausdrücklich unabhängig vom aktuellen Buchgewinn/
   -verlust: ein Verlust wird realisiert, wenn die These weg ist, statt auf
   Erholung zu hoffen ("Hope is not a strategy").

**Investment-These-Protokoll: vordefinierte These-Bruch-Kriterien statt
nachträglicher Bewertung (2026-08-30, aus der Cross-KI-Gesamt-Review in
Agent-Playbook-Archiv-Diskussionen.md Abschnitt 12, von Brian freigegeben; Conans Kritik: eine rein nachträgliche
Einschätzung "ist die These noch intakt?" ist anfällig für Verankerung/
Rationalisierung – man neigt dazu, an einer einmal gekauften These
festzuhalten).** Ergänzt Kategorie 5 (VERKAUF ERWÄGEN) oben um einen festen
Mechanismus, der VOR diesem Moment ansetzt, statt erst danach zu urteilen:
1. **Bei jeder Neuaufnahme (Watchlist wie Depot-Kauf)** hält der jeweilige
   Deep-Dive (TMR bzw. Scout) zusätzlich zur Fair-Value-Einschätzung **2-4
   konkrete, falsifizierbare These-Bruch-Kriterien** fest – so spezifisch
   wie möglich formuliert, keine vagen Aussagen wie "wenn es schlecht
   läuft". Beispiele: "Bruttomarge fällt unter X% über zwei aufeinander-
   folgende Quartale", "Kundenabwanderungsrate steigt über Y%", "Kern-
   Wachstumstreiber Z verliert nachweislich Marktanteil an Konkurrent",
   "Regulatorische Änderung untersagt Geschäftsmodell-Baustein W". Diese
   Kriterien werden zusammen mit Kauf-Datum, Einstiegskurs und der
   Kernthese selbst in der Watchlist-/Depot-Erfassung (siehe `depot/`-
   Ordner) hinterlegt.
2. **Der [B] THESE-CHECK im laufenden Monitoring prüft ab jetzt primär
   gegen diese vorab festgelegten Kriterien**, statt jedes Mal neu und
   frei zu beurteilen, ob "die These noch passt" – das reduziert die
   Gefahr, eine mittlerweile ungünstige Entwicklung schönzureden, weil
   die Position schon länger gehalten wird oder im Gewinn liegt.
3. **Ist eines der hinterlegten Kriterien eindeutig eingetreten**, wird das
   automatisch als starkes Signal Richtung Kategorie 5 (VERKAUF ERWÄGEN)
   gewertet – bleibt aber, wie die gesamte Verkaufsdisziplin, eine
   Empfehlung mit Begründung, keine automatische Order (siehe Abschnitt 1,
   "Grenze bleibt fix").
4. **Kein Kriterium ist in Stein gemeißelt:** Stellt sich im Nachhinein
   heraus, dass ein Kriterium zu eng oder zu weit gefasst war, kann es bei
   der nächsten regulären Analyse der Position nachjustiert werden – aber
   nur mit expliziter Begründung im Positions-Log, nicht stillschweigend,
   damit aus dieser Disziplin nicht wieder eine nachträgliche
   Rationalisierung wird.
Für bereits bestehende Depot-Positionen, die noch keine explizit
hinterlegten These-Bruch-Kriterien haben, werden diese schrittweise beim
nächsten regulären [B] THESE-CHECK bzw. Wochenfazit nachgetragen (Jarvis'
Einschätzung auf Basis der ursprünglichen TMR-/Scout-Bewertung, von Brian
jederzeit korrigierbar), statt alle 18 Positionen auf einmal nachzuziehen.

**Gründliche-These-Prüfung-vor-Verkaufsempfehlung-Pflicht (2026-09-04, von
Brian gefordert nach dem Cellebrite-Fall):** Auslöser: ein frischer
3-fach-Scout-These-Check kam am 04.09.2026 für die bestehende Cellebrite-
Position vorschnell zu SCHROTT/VERKAUFEN – obwohl (a) zwei der drei
bereits vordefinierten Re-Rating-Trigger noch gar nicht prüfbar waren
(die Q3-Zahlen standen erst noch aus, "0/3 erfüllt" verwechselte "noch
nicht testbar" mit "durchgefallen"), und (b) das Wachstums-K-Kriterium
mechanisch gegen den für junge/spekulative Firmen gebauten Scout-Maßstab
(≥30% Umsatz-CAGR) geprüft wurde, obwohl Cellebrite ein etabliertes,
profitables Unternehmen mit echtem regulatorischem Moat ist (lizenzierter
forensischer Gerätezugriff für Strafverfolgung – Zertifizierungen, Chain-
of-Custody-Anforderungen, Behördenbeziehungen als reale Eintrittsbarriere,
kein reines Wachstumsstory-Geschäft). Brian: "erst gründlich die These
durchgehen, wie bei Cellebrite grad der Fall war, und nicht schon
voreilig einen Verkauf in Erwägung ziehen." **Bleibt die These nach dieser
Prüfung nachweislich gebrochen, bleibt die Verkaufsempfehlung
selbstverständlich bestehen** – die Regel verlangt eine gründliche
Prüfung, kein automatisches Pro-Halten-Bias.

Ab sofort PFLICHT, bevor eine Kategorie-5-Empfehlung (VERKAUF ERWÄGEN) für
eine BEREITS GEHALTENE Depot-Position allein aus einem ausgelösten Scout-/
TMR-Mechanismus (Abbruch-Logik, K≤K-BASIS-2, Terminal-State, SCHROTT-
Rating) abgeleitet wird:
1. **Timing vs. Struktur explizit unterscheiden:** Ist der auslösende
   negative Befund (Guidance-Cut, Umsatz-Verfehlung, Margen-Delle) plausibel
   ein temporäres/zyklisches Ereignis (z.B. verzögerte statt verlorene
   Großaufträge, ein Sondereffekt, ein einzelnes schwaches Quartal) oder ein
   strukturelles Problem (nachgewiesene Kundenabwanderung, Wettbewerbs-
   verlust, Moat-Erosion)? Beide Lesarten benennen und begründen, welche
   nach den vorliegenden Fakten wahrscheinlicher ist – NICHT reflexhaft die
   negativste Interpretation übernehmen, nur weil ein mechanischer
   Abbruch-Trigger gegriffen hat.
2. **Bereits definierten Checkpoint respektieren:** Existiert aus der
   Erstanalyse oder dem Investment-These-Protokoll bereits ein konkreter
   künftiger Prüfpunkt (z.B. die nächsten Quartalszahlen), der genau diese
   offene Frage klären soll, und liegt dieser Checkpoint noch in der
   Zukunft? Dann bleibt es bei HALTEN mit explizit benanntem Checkpoint,
   KEIN Verkauf vor dessen Erreichen – es sei denn, ein hartes,
   UNABHÄNGIGES Ausschluss-Kriterium (Fraud, bestätigter Going-Concern,
   nachgewiesener Moat-Verlust, Übernahme/Delisting) ist bereits JETZT
   eingetreten, unabhängig vom offenen Checkpoint.
3. **Reifegrad-Methodik-Mismatch prüfen:** Greift bei einer bereits
   etablierten, umsatzstarken Position mechanisch ein für junge/
   spekulative Firmen gebauter Scout-Wachstumsmaßstab (K-BASIS, ≥30%
   CAGR usw.)? Falls ja, das explizit benennen und im Gesamturteil gegen
   die tatsächliche Geschäftsqualität/den Moat abwägen, statt den rohen
   K-Count unreflektiert eins-zu-eins als Handlungsempfehlung zu
   übernehmen (derselbe Mismatch war bereits beim RKLB-Fall vom 01.09.
   dokumentiert – "das Deep-Tech-Override-Raster ist eigentlich für
   kleine Vorab-Umsatz-Firmen gebaut, nicht für diese 'etabliertes
   Kerngeschäft + Moonshot-Anhängsel'-Konstellation").
4. **Ergebnis dieser drei Prüfpunkte explizit im Output ausweisen**
   ("These-Prüfung vor Verkaufsempfehlung: Timing/Struktur-Einordnung +
   Checkpoint-Status + Methodik-Fit-Check"), nicht nur das rohe Scout-/
   TMR-Abbruch-Ergebnis unkommentiert als finale Handlungsempfehlung
   weiterreichen.
5. Erst wenn die These nach dieser Prüfung weiterhin als gebrochen gilt
   (oder ein hartes, unabhängiges Ausschluss-Kriterium bereits erfüllt
   ist), bleibt es bei Kategorie 5 (VERKAUF ERWÄGEN) – sonst HALTEN
   (mit Checkpoint) oder BEOBACHTEN ENGER.

**Bewusste Asymmetrie, gilt NUR für bereits gehaltene Depot-Positionen:**
diese vertiefte Prüfpflicht gilt NICHT für die Erstprüfung neuer
Watchlist-/Kauf-Kandidaten – dort bleibt die strengere, reflexive
Abbruch-Logik unverändert in Kraft (ein neuer Kandidat, der die Kriterien
nicht erfüllt, wird weiterhin ohne Nachsicht aussortiert). Die Begründung
für die Asymmetrie: die Hürde für NEUES Kapital darf hoch bleiben, aber
eine bereits mit echtem Geld finanzierte These verdient vor einem
Exit-Vorschlag dieselbe Sorgfalt wie beim ursprünglichen Kauf – analog
zum bereits etablierten Prinzip "reine Kursrückgänge sind kein
automatischer Ausschlussgrund" bei der Watchlist (siehe "Watchlist-
System", Ausschluss-/Abstiegs-Kriterien).

**Einstiegszonen bei NACHKAUF ERWÄGEN, symmetrisch zu den
Gewinnmitnahme-Zielzonen (2026-08-29):** Ebenfalls zusätzlich in EUR
umgerechnet (siehe "Einheitliche EUR-Umrechnung" oben). Analog zu
"Zielzone 1/2" oben, aber
in die andere Richtung:
- **Einstiegszone 1:** Kurs nahe/unter der TMR-Base-Fair-Value bzw. einer
  wichtigen technischen Unterstützungszone.
- **Einstiegszone 2:** Kurs deutlich unter der TMR-Bear-Fair-Value UND
  technisch nachhaltig überverkauft/Bodenbildung erkennbar – stärkeres
  Signal, aber auch hier gilt: nur relevant, wenn der [B] THESE-CHECK
  bestätigt, dass der Rückgang keinen fundamentalen Grund hat.
Auch hier gilt: die qualitative Einschätzung ("unterbewertet", These
intakt) bleibt der fundamentale Kern und wird immer benannt; die
Einstiegszone ist eine zusätzliche, konkretere Angabe, wo die Datenlage es
hergibt – ohne belastbare Basis transparent als "noch keine belastbare
Einstiegszone" kennzeichnen statt eine Zahl zu erfinden. Ein Nachkauf-
Vorschlag berücksichtigt außerdem das monatliche Budget (siehe "Budget &
Cashflow", Abschnitt 3) und die Positionsgrößen-/Kapitalgewichts-Limits –
auch eine attraktive Einstiegszone rechtfertigt kein Überschreiten der
10%-Positionsgrenze oder des Kategorie-Kapitalgewichts-Ziels.

**Kategorie-spezifischer Exit-Ansatz für Talent/Zock (2026-08-29, von Brian
präzisiert):** Die fünf Kategorien oben gelten unverändert für Champions und
Profi (fundamentale These + technisches Bild kombiniert, wie beschrieben).
Für Positionen in der Kategorie **Talent/Zock/Momentum** (siehe Abschnitt 3,
Update 2026-08-29) hängt der Exit-Ansatz vom **Zeithorizont-Tag** der
jeweiligen Position ab (siehe Abschnitt 3):
- **Tag "Zock/Trade"** – hier gilt ein stärker **charttechnik-/
  stop-loss-basierter** Ansatz statt eines primär thesenbasierten: bei
  diesen Werten (z.B. ein reiner Momentum-Fall wie IREN) ist die
  fundamentale These oft ohnehin dünn oder gar nicht erst der Punkt – ein
  hartes technisches Stop-Loss-Niveau (z.B. Bruch einer wichtigen
  gleitenden Linie, definierter Prozent-Abstand vom Einstieg/lokalen Hoch)
  ist hier die primäre Absicherung, nicht erst ein fundamentaler
  These-Bruch.
- **Tag "Talent (langfristig)"** – hier bleibt der Exit-Ansatz näher am
  thesenbasierten Vorgehen (wie Champions/Profi): ein technisches
  Stop-Loss dient als Sicherheitsnetz gegen einen Totalschaden, ist aber
  NICHT der primäre Auslöser – kurzfristige Volatilität allein (z.B. ein
  Kursrutsch ohne fundamentalen Anlass) ist bei dieser Unterkategorie kein
  Verkaufsgrund, sonst würde eine bewusst langfristig gedachte Position wie
  ein reiner Trade behandelt, was Brian ausdrücklich vermeiden will. Ein
  Beispiel aus dem aktuellen Depot mit dieser Einordnung: SoFi Technologies
  (von Jarvis als "Talent (langfristig)" eingeschätzt, da Brian die
  fundamentale Wachstumsstory über mehrere Jahre sieht – bei Bedarf von
  Brian zu bestätigen/korrigieren).
Sizing bleibt für beide Unterkategorien entsprechend klein (siehe Scout
Sizing-Stufen, Abschnitt 3) – der Tag ändert nur den Exit-Ansatz, nicht die
Positionsgröße. **Seit 2026-08-30 (Twelve-Data-Connector live, siehe
"Technische Analyse via Twelve Data")** weist das TA-Modul für ALLE
Talent/Zock-Positionen ein Stop-Loss-Niveau mit aus (nicht nur
Entry-Ampel/Unterstützung-Widerstand wie bei Champions/Profi), bei "Talent
(langfristig)" weiterhin explizit als Sicherheitsnetz gekennzeichnet, nicht
als primäres Handlungssignal – umgesetzt in TA-Prompt v1.10, siehe
Abschnitt 2 "Spielraum für Prompt-Anpassungen".

**Gewinnmitnahme-Zielzonen ZUSÄTZLICH zur qualitativen Einschätzung
(2026-08-29, von Brian gefordert; 2026-08-29 präzisiert: die qualitative
Einschätzung "Bewertung/Chart überzogen" bleibt ausdrücklich bestehen, ist
für die fundamentale Seite weiterhin wichtig und wird NICHT durch die
Zielzonen ersetzt):** Zusätzlich zur reinen Kategorie-Einstufung
(TEILVERKAUF-GEWINNMITNAHME ERWÄGEN etc.) UND zur weiterhin gültigen
qualitativen Begründung ("Bewertung/Chart deutlich überzogen") soll der
Agent, wo die Datenlage es hergibt, ERGÄNZEND konkrete **Zielzonen**
benennen – kombiniert aus TMR-Fair-Value-Bandbreite (Bear/Base/Bull, siehe
TMR-Prompt) und technischen Widerstandszonen (Twelve Data, seit 2026-08-30
live). Alle Zonen-Angaben werden zusätzlich in EUR umgerechnet
ausgewiesen (siehe "Einheitliche EUR-Umrechnung", Pipeline-Schritt [3]):
- **Zielzone 1 (erste Teilverkauf-Stufe):** Kurs nähert sich/übertrifft die
  TMR-Base-Fair-Value UND/ODER eine wichtige technische Widerstandszone →
  ein kleinerer Teil der Position (z.B. ein Viertel bis ein Drittel, grobe
  Richtgröße, keine starre Regel) als erste Gewinnsicherung vorschlagen.
- **Zielzone 2 (weitere Stufe):** Kurs deutlich über der TMR-Bull-Fair-Value
  UND technisch nachhaltig überhitzt (siehe RSI/gleitende-Linien-Kriterien
  oben) → eine weitere Tranche zur Gewinnmitnahme vorschlagen.
Diese Zonen werden je Position im Rahmen der [E]-Bewertung (Wochenfazit
und/oder Ad-hoc-Analyse) explizit benannt, sobald die zugrundeliegenden
Fair-Value-/Widerstandsdaten vorliegen – ohne belastbare Datenbasis (z.B.
TMR noch nicht gelaufen, oder ein einzelner Wert bei Twelve Data nicht
geführt) wird das transparent als "noch keine belastbare Zielzone"
gekennzeichnet statt eine Zahl zu erfinden.

**Portfolio-Kontext-Pflichtprüfung vor jeder Zonen-/Tranchen-Empfehlung
(2026-09-01, von Brian gefordert).** Eine Einstiegs-/Zielzone und die
zugehörige Tranchen-Empfehlung (siehe unten) werden nie isoliert aus
Kurs-/Fair-Value-Daten einer einzelnen Position hergeleitet, sondern immer
zuerst gegen fünf Portfolio-Ebenen gespiegelt – jede davon ist bereits an
anderer Stelle im Regelwerk verankert, hier nur als verbindlicher
Cross-Check-Schritt vor der Zonen-Empfehlung zusammengeführt:
1. **Chance-Risiko-Verhältnis (CRV):** bei Scout-Kandidaten das bereits
   berechnete EV_Multiple + Downside-Summe aus den
   Outcome-Wahrscheinlichkeiten (siehe `prompts/conan-the-scout-v1.12.md`),
   bei TMR-Werten die Bear/Base/Bull-Fair-Value-Bandbreite – wird in der
   Zonen-Empfehlung explizit als Verhältnis benannt ("Aufwärtspotenzial zu
   Zielzone X vs. Abwärtsrisiko zu Stop-Loss/Bear-FV Y"), nicht nur implizit
   in den Einzelzahlen belassen.
2. **Cashreserve:** aktueller Cash-Stand (`get_portfolio_cash_breakdown`
   bei Scalable, bzw. `depot/*.md` für die anderen Broker, siehe "Budget &
   Cashflow"). Reicht das verfügbare Cash für die vorgeschlagene erste
   Tranche nicht, wird die Tranche verkleinert oder explizit auf die
   nächste reguläre Sparrate verschoben – keine Empfehlung, die faktisch
   mehr Kapital voraussetzt als verfügbar ist.
3. **Depotstruktur:** aktuelle Kategorie-Gewichtung (Champions/Profi/
   Talent, Zielkorridor siehe Abschnitt 3) UND Regionen-/Sektor-Verteilung
   gegen die bestehenden Zielbänder. Würde die volle vorgeschlagene Tranche
   ein Band sprengen (z.B. USA-Cap, Sektor-Band, Kategorie-Kapitalgewicht),
   wird die Tranchengröße reduziert oder der Kauf explizit als "würde
   Depotstruktur-Ziel X verletzen" gekennzeichnet statt stillschweigend
   empfohlen.
4. **Strategie-Konsistenz:** Abgleich gegen das antizyklische Grundprinzip
   bzw. die Momentum-Ausnahme für Zock/Trade (oben) UND die Core-Rules aus
   Abschnitt 14 – eine Zonen-Empfehlung, die einem bereits aktiven
   Terminal-State/Core-Rule-Abbruch widerspricht, ist ausgeschlossen, keine
   Ausnahme.
5. **Zielfortschritt:** aktueller Stand gegen das 90.000-100.000€-Ziel
   (Abschnitt 1, inkl. Portfolio-Level Expected-Return-Szenario) – bei
   bereits dauerhaft erreichtem Ziel greift die dort beschriebene
   Rückkehr zur konservativeren Grundeinstellung (kleinere Tranchen/engere
   Bänder), nicht die während der Aufbauphase geltenden moderat
   erweiterten Stellschrauben.
Diese fünf Punkte werden knapp (1 Satz je Punkt reicht, wenn unauffällig)
in jeder Zonen-/Tranchen-Empfehlung mitgeführt – kein separates,
aufwendiges Extra-Modul, sondern eine Pflicht-Gegenprobe, bevor eine Zahl
als Empfehlung rausgeht.

**Tranchen-vs-Einmalkauf-Entscheidung (2026-09-01, von Brian gefordert –
systematisch statt frei entschieden).** Für jede Einstiegszonen-/
Zielzonen-Empfehlung wird zusätzlich festgelegt, ob der Kauf/Verkauf als
Einmal-Order oder gestaffelt über mehrere Tranchen erfolgen sollte:
- **Standard/Default: 2-3 Tranchen** (Richtgröße z.B. 40/30/30 oder 50/50
  über Einstiegszone 1/2 verteilt) – Timing lässt sich selten präzise
  treffen, Staffelung ist die risikoärmere Grundhaltung, konsistent mit dem
  Kapitalerhalt-Grundziel (Abschnitt 1).
- **Für WENIGER Tranchen/größere Einzeltranche sprechen** (mehrere
  zusammen erhärten das Signal, keine Einzelregel reicht):
  1. Konfidenz 🟢 über alle drei KIs hinweg.
  2. Kurs bereits in Einstiegszone 2 (Bear-FV + technisch überverkauft),
     UND Bodenbildung bestätigt (echtes Signal ODER algorithmischer Proxy,
     siehe `reports/detect_bodenbildung.py` oben).
  3. Niedrige Volatilität (ATR relativ zum Kurs moderat, kein akuter
     Ausreißertag).
  4. Champions/Profi mit vollständig erfüllter DNA (kein Grenzfall).
  → bei allen vier Punkten erfüllt: Einmalkauf oder 2 große Tranchen
  vertretbar.
- **Für MEHR/kleinere Tranchen sprechen** (Default verstärkt sich):
  1. Talent/Zock JEDER Ausprägung – hier gilt IMMER mindestens 3 Tranchen,
     unabhängig von den übrigen Kriterien (passt zur ohnehin kleinteiligen
     Scout-Sizing-Logik, Abschnitt 3).
  2. Konfidenz 🟡 (der Normalfall) oder Dissens zwischen den drei KIs
     (Diskussionsrunde [3b] ausgelöst).
  3. Kurs erst in Einstiegszone 1 (frühes, noch unbestätigtes Signal).
  4. Hohe Volatilität (ATR relativ zum Kurs erhöht).
- Die konkrete Tranchen-Empfehlung (Anzahl + grobe Gewichtung) wird immer
  explizit benannt und kurz begründet, nie stillschweigend vorausgesetzt –
  "wie üblich gestaffelt" reicht nicht, die ausschlaggebenden Kriterien
  werden genannt (analog zur Herkunftsvermerk-Pflicht beim
  Zeithorizont-Tag oben).

**Aktive Umschichtungs-Logik: Kapitalrotation zwischen Positionen (2026-09-01,
von Brian gefordert).** Bisher behandelt das Regelwerk Kauf- und
Verkaufs-Empfehlungen weitgehend isoliert je Einzelposition. Brian will, dass
der Agent das Depot aktiv als Ganzes verwaltet: löst eine Position eine der
beiden Verkaufs-Kategorien (4 oder 5, siehe "Fünf Ergebnis-Kategorien" oben)
aus, prüft der Agent zusätzlich EIGENSTÄNDIG, ob das freiwerdende Kapital
woanders (bestehende Depot-Position mit aktivem NACHKAUF-ERWÄGEN-Signal ODER
Watchlist-Kandidat mit frischem KAUFEN-Rating) aktuell mehr Potenzial bietet,
und präsentiert Verkauf + Wiederanlage als **gepaarten
Umschichtungs-Vorschlag** statt zweier isolierter Meldungen. Der Agent
"entscheidet frei" im Sinne von: er wählt eigenständig, WELCHE Umschichtung
er vorschlägt (oder auch keine, wenn kein überzeugender Kandidat da ist) –
die Order-Ausführung selbst bleibt exklusiv Brians Sache (Grenze aus
Abschnitt 1 unverändert, `submit_buy_order`/`submit_sell_order` bleiben
tabu, `preview_*` darf zur Vorbereitung genutzt werden).

- **Zwei Auslöser, kein neuer unabhängiger Verkaufsgrund:** Die
  Umschichtungs-Prüfung wird NIE selbst zum Verkaufsauslöser – sie startet
  erst, NACHDEM Kategorie 4 oder 5 bereits unabhängig (aus eigenem Recht)
  ausgelöst hat. Die Aussicht auf einen vermeintlich attraktiveren Kandidaten
  woanders ist niemals allein ein Grund, eine fundamental intakte These zu
  verkaufen – das widerspräche dem Kapitalerhalt-Grundziel (Abschnitt 1) und
  dem antizyklischen Grundprinzip (oben).
  1. **Gewinnmitnahme-Rotation:** Kategorie 4 (TEILVERKAUF/GEWINNMITNAHME
     ERWÄGEN) ist für Position A aktiv (These intakt, aber überbewertet/
     überhitzt) UND es existiert mindestens ein Kandidat B mit klar
     besserem aktuellem CRV (bestehende Position mit NACHKAUF-ERWÄGEN-
     Signal oder frischer Watchlist-KAUFEN-Kandidat) → Umschichtung
     vorschlagen.
  2. **Verlust-Rotation:** Kategorie 5 (VERKAUF ERWÄGEN) ist für Position A
     aktiv (These gebrochen) → hier IMMER aktiv nach einem
     Umschichtungsziel suchen, unabhängig vom CRV-Vergleich, weil das
     Kapital ohnehin nicht in der gebrochenen These bleiben soll. Die Frage
     ist dann nur noch "wohin", nicht "ob raus" – das "ob raus" ist über
     das Investment-These-Protokoll (oben) bereits entschieden.
- **Format des Vorschlags:** gepaart darstellen – Verkauf X€/Y Stück aus
  Position A zum aktuellen Kurs, Wiederanlage Z€ in Position/Kandidat B zum
  aktuellen Kurs, mit kurzer Gegenüberstellung der beiden CRVs/Thesen
  ("A: These gebrochen wegen [Kriterium] / B: [Kernthese], aktuelles
  Aufwärtspotenzial X vs. Abwärtsrisiko Y"). Auf die EMPFANGENDE Seite
  (Kandidat B) wird die volle Portfolio-Kontext-Pflichtprüfung (5 Punkte,
  oben) angewendet wie bei jeder anderen Zonen-Empfehlung, inklusive
  Konkrete-Eurosumme-Pflicht und Tranchen-Entscheidung.
- **Kein erzwungener Vorschlag:** Findet sich kein überzeugender
  Umschichtungs-Kandidat (typischer Fall bei reiner Kategorie-4-
  Gewinnmitnahme ohne aktuell attraktive Alternative), bleibt es bei der
  reinen Teilverkauf-Empfehlung, das Kapital fließt zurück in Cash/die
  nächste reguläre Sparrate – transparent als "aktuell kein besserer
  Umschichtungs-Kandidat identifiziert" benennen statt eine schwache
  Umschichtung zu erzwingen.
- **Verankerung im Ablauf:** Wochenfazit (Schritt "Exit-/Gewinnmitnahme-/
  Nachkauf-Ampel") und Täglicher Trigger-Check (bei ausgelöstem Trigger)
  prüfen ab sofort bei jeder Kategorie-4/5-Meldung zusätzlich aktiv auf ein
  Umschichtungsziel, bevor das Ergebnis an Brian geht – nicht erst auf
  Nachfrage.

**Zonen-Benachrichtigung per E-Mail + Scalable-Preisalarm (2026-09-01, von
Brian gefordert, seit E-Mail-Anbindung technisch möglich).** Wird für eine
Depot- oder Watchlist-Position eine NEUE oder GEÄNDERTE Einstiegs- bzw.
Zielzone festgelegt (aus einem frischen 3-fach-Cross-Check, Ad-hoc-Analyse
oder Wochenfazit-Update – nicht bei unveränderten Zonen, die schon letzte
Woche galten, um Benachrichtigungs-Ermüdung zu vermeiden):
1. **Scalable-Preisalarm setzen:** `create_price_alert` für jede genannte
   Zone (Einstiegszone 1/2 UND/ODER Zielzone 1/2, je nachdem was gerade
   festgelegt wurde). Wurde eine ältere Zone durch eine neue ersetzt,
   zuerst den alten Alarm per `remove_price_alert` entfernen, damit keine
   veralteten Alarme stehen bleiben. Beide Tools sind laut
   Scalable-Whitelist bereits ohne Rückfrage nutzbar (siehe
   HANDOVER.md 10.7).
2. **E-Mail an `brianqtng@outlook.de`:** Betreff nennt Ticker + Anlass
   (z.B. "HAWK: neue Einstiegszone festgelegt"). Inhalt: die genaue(n)
   Zone(n) in Originalwährung UND EUR, die Tranchen-Empfehlung (siehe
   oben) MIT konkreter Eurosumme (siehe Pflicht unten), kurzer Begründung,
   und ein expliziter Hinweis, dass Brian selbst ein Limit-Order bzw.
   Stop-Loss auf diesem Niveau bei Scalable setzen kann – **niemals eine
   Formulierung, die eine automatische Order-Ausführung suggeriert**
   (Grenze aus Abschnitt 1 bleibt fix, die Mail bereitet nur die manuelle
   Entscheidung vor).
3. **Kein Spam bei unveränderten Zonen:** Im wöchentlichen Wochenfazit
   werden alle aktuell gültigen Zonen weiterhin vollständig aufgeführt wie
   bisher – aber nur eine ECHTE Änderung (neue Zone, verschobene Zone,
   ausgelöste/erreichte Zone) löst zusätzlich die dedizierte E-Mail +
   Preisalarm-Aktualisierung aus, nicht jede wöchentliche Wiederholung
   derselben Zahl.
4. **Konkrete-Eurosumme-Pflicht (2026-09-01, von Brian gefordert – "damit
   ich ein Limit-Order setzen kann, auch unterwegs ohne selbst zu
   rechnen").** Jede Einstiegszonen-/Nachkauf-Empfehlung nennt ZUSÄTZLICH
   zur Prozent-/Tier-Angabe (Sizing-Tier bzw. Scout-Sizing-Stufe) eine
   konkrete Eurosumme je Tranche: aktueller Gesamtdepotwert bzw. relevante
   Berechnungsbasis (Aktienanteil bei Talent/Scout-Positionen, siehe
   Abschnitt 1) × Ziel-Sizing-Prozentsatz × Tranchen-Anteil (siehe
   Tranchen-Logik oben) = Eurobetrag DIESER Tranche, gerundet auf einen
   praktikablen Order-Betrag. Beispielrechnung wird im Fazit kurz gezeigt
   (Basis → Prozentsatz → Ergebnis), nicht nur die nackte Endzahl, damit
   nachvollziehbar bleibt, wie sie zustande kam. Cash-Reserven-Check
   (Portfolio-Kontext-Pflichtprüfung oben) bleibt davon unberührt – reicht
   das Cash für die berechnete Summe nicht, wird das explizit benannt statt
   die Zahl unkommentiert stehen zu lassen.
5. **Preisalarm-Auslösung ist KEIN automatisches Kaufsignal.** Erreicht der
   Kurs eine gesetzte Zone (Scalable benachrichtigt Brian direkt UND der
   nächste Trigger-Check/Blitz-Scan erkennt es über den bestehenden
   Abstauber-Limit-Abgleich, siehe "Täglicher Trigger-Check"), bedeutet das
   NUR: die Vorbedingung für eine Nachkauf-Prüfung ist erreicht, keine
   automatische Kaufempfehlung. Der [B] THESE-CHECK läuft dann frisch
   (ist die fundamentale Lage noch intakt? wurde zwischenzeitlich ein
   Downgrade-Trigger ausgelöst? ist die Position ggf. bereits über dem
   eigenen Sizing-Deckel, wie z.B. aktuell bei Kraken Robotics – dann bleibt
   es bei "kein Nachkauf", unabhängig vom erreichten Kurs). Nur wenn der
   These-Check weiterhin grün ist UND kein Sizing-Deckel überschritten
   würde, geht eine ECHTE Kauf-Empfehlung mit konkreter Eurosumme (Punkt 4)
   per E-Mail/Push raus – sonst eine kurze, ehrliche Information "Zone
   erreicht, aber [Grund] – weiterhin kein Nachkauf".
6. **Explizite Handlungs-Kennzeichnung in JEDER Zonen-E-Mail (2026-09-01,
   von Brian gefordert – "muss mir explizit mitteilen, ob Limit-Order oder
   nur Preisalarm zur Beobachtung").** Jede E-Mail zu einer Zone beginnt
   mit einer unmissverständlichen Kopfzeile, welche der beiden Kategorien
   zutrifft – niemals nur implizit aus dem Fließtext erschließbar:
   - **"🎯 LIMIT-ORDER EMPFOHLEN"** – nur wenn der These-Check aktuell grün
     ist UND kein Sizing-Deckel überschritten würde (siehe Punkt 5). Direkt
     darunter: Kurs, konkrete Eurosumme (Punkt 4), Tranchen-Hinweis, und
     dass Brian selbst das Limit-Order bei seinem Broker setzen kann.
   - **"👁 NUR BEOBACHTUNG – Preisalarm gesetzt, keine Kaufempfehlung"** –
     der Normalfall bei neu festgelegten Einstiegszonen, oder wenn eine
     Zone erreicht wurde, der These-Check aber nicht grün ist bzw. ein
     Sizing-Deckel bereits überschritten ist (wie aktuell bei Kraken
     Robotics, siehe oben). Kurz benennen, warum (noch) keine Kaufempfehlung
     folgt, damit Brian nicht rätseln muss, ob eine Handlung erwartet wird.
   Dieselbe Kennzeichnung gilt sinngemäß auch für Zielzonen/Gewinnmitnahme
   ("🎯 TEILVERKAUF EMPFOHLEN" vs. "👁 NUR BEOBACHTUNG").

**Chartmuster-Erkennung als aktiver Impuls, nicht nur reaktive Kennzahl
(2026-08-29, von Brian gefordert):** Das TA-Modul soll gezielt auf zwei
Musterarten achten und daraus PROAKTIV etwas machen, nicht nur eine
Kennzahl in einer Tabelle ablegen:
- **Bodenbildung / Start eines neuen Aufwärtstrends** (z.B. höhere Tiefs,
  Ausbruch über eine wichtige gleitende Linie oder eine Abwärtstrendlinie,
  idealerweise mit Volumen-Bestätigung): Wird das bei einem Watchlist-Wert
  oder einem neuen Kandidaten erkannt UND passt die fundamentale These
  ("passt hervorragend ins Portfolio", Brians Formulierung – z.B. Lücke in
  Region/Sektor/Kategorie-Kapitalgewicht, siehe Abschnitt 3), wird das
  AKTIV als Kauf-Vorschlag an Brian herangetragen (nicht erst auf Nachfrage
  warten), mit Begründung, warum Timing UND These gerade zusammenpassen.
  **Automatisierte Erkennung im unbeaufsichtigten Betrieb (seit 2026-09-01,
  echte Lücke geschlossen):** Das TA-Modul schätzt Chartformationen laut
  eigenem Wortlaut nur aus Nutzer-Input, nicht selbst aus Zahlenreihen – in
  einem Scheduled Task ohne Brian am Rechner konnte dieser Impuls deshalb
  bisher gar nicht auslösen. Ersatz: `reports/detect_bodenbildung.py`
  (Twelve-Data-`get_time_series`-Rohausgabe als Eingabe) liefert eine
  **algorithmische Annäherung** (höhere Pivot-Tiefs + EMA20-Breakout +
  Volumen-Trend, siehe Skript-Docstring für die genaue Methodik) – kein
  echtes Muster-Erkennen, ausdrücklich als Proxy gekennzeichnet
  (No-False-Precision-Regel). Ergebnis "JA" ersetzt nicht die
  Fundamental-Prüfung, sondern löst sie erst aus: nur bei "JA" UND
  bestätigtem Depot-Fit wird der Kauf-Vorschlag herangetragen, mit dem
  Proxy-Ergebnis explizit als "algorithmische Annäherung" benannt, nicht als
  bestätigtes Chartmuster.
- **Doppeltop / bärische Topbildung:** Wird dieses Muster bei einer
  bestehenden Depot-Position erkannt, fließt es als zusätzliches
  technisches Warnsignal in den [E] EXIT-/GEWINNMITNAHME-CHECK ein – in
  Kombination mit dem fundamentalen Bild: bei ohnehin überzogener,
  aber intakter These bestätigt/verstärkt ein Doppeltop die Einstufung
  TEILVERKAUF/GEWINNMITNAHME ERWÄGEN (bzw. löst eine der oben genannten
  Zielzonen aus); bei ansonsten unauffälliger, nicht überzogener These
  reicht ein Doppeltop allein nur für BEOBACHTEN ENGER, kein automatischer
  Verkaufsgrund. Bei "Talent (langfristig)"-Positionen (siehe Abschnitt 3)
  bleibt die fundamentale These weiterhin ausschlaggebend, ein Doppeltop
  wird dort explizit nur als Beobachtungssignal behandelt, nicht als
  eigenständiger Verkaufsauslöser (siehe "Kategorie-spezifischer
  Exit-Ansatz für Talent/Zock" oben). **Seit 2026-08-30 (Twelve-Data-
  Connector live)** werden beide Muster wo möglich anhand echter Kursdaten
  bestätigt statt nur aus grober WebSearch-Chart-Beschreibung.

**Wo das auftaucht:** [E] EXIT-/GEWINNMITNAHME-CHECK im täglichen
Monitoring-Kreislauf (siehe oben) und als eigener Punkt im wöchentlichen
Wochenfazit – jede Position mit Kategorie ungleich HALTEN wird dort benannt,
mit 1-2 Sätzen Begründung (fundamental, technisch, oder beides). Die
eigentliche Order bleibt wie immer bei Brian (siehe Abschnitt 1, "Grenze
bleibt fix") – der Agent empfiehlt, führt aber nichts automatisch aus.

**Technisch:** Dieser Kreislauf läuft am besten als wiederkehrender geplanter Lauf
("Scheduled Task", nicht der interne Cron-Mechanismus der Session – siehe
Technische Bausteine unten) statt als etwas, das Brian jedes Mal manuell anstoßen
muss. Rhythmus grob wie in Abschnitt 6 skizziert: täglicher schneller Watchlist-/
Depot-Check, wöchentlicher breiterer Scan nach neuen Kandidaten.

### Wochenfazit (2026-08-23, von Brian gefordert, Vorbild: Raketentonis Format)

Zusätzlich zu den anlassbezogenen Kurz-Fazits (Pipeline-Schritt 5) und den
proaktiven Einzelmeldungen (oben, [A]-[D]) bekommt Brian **jeden Freitagabend**
(22:00 Uhr, Europe/Berlin) eine kompakte Wochenzusammenfassung über das gesamte
Depot – unabhängig davon, ob in der Woche ein voller 3-fach-Cross-Check gelaufen
ist. Format (angelehnt an das von Brian gezeigte Beispiel, knapp, Fließtext/kurze
Absätze statt Tabellen):

```
Wochenfazit

[🟢/🟡/🔴] Depotstatus: [KEIN AKUTER HANDLUNGSBEDARF / BEOBACHTEN / HANDLUNGSBEDARF]

Kurzer Status pro Kategorie:
  Champions [X/Y voll]:  ...
  Profi     [X/Y voll]:  ... (freie Slots falls vorhanden)
  Talent    [X/Y voll]:  ...

Auffälligkeiten der Woche (nur was sich wirklich bewegt hat – neue Trigger,
gerissene Stop-These, Entry-Ampel-Wechsel, relevante News, Konvergenz-
Widersprüche aus 3-fach-Checks dieser Woche).

Watchlist-Update (siehe `watchlist.md`): neu aufgenommene Werte und
Werte, die diese Woche rausgeflogen sind, jeweils mit 1-2 Sätzen Begründung
(z.B. katastrophale Zahlen, gerissene These, Übernahme). Keine Veränderung
ist ein vollwertiges Ergebnis ("Watchlist unverändert diese Woche").

Portfolio-Regel-Check (2026-08-28, von Brian festgelegt, siehe Abschnitt 3):
  - Größte Einzelposition ≤10% des Gesamtportfolios? Falls nicht: benennen,
    welche Position und warum (organischer Kursanstieg vs. bewusster
    Nachkauf-Fehler).
  - Keine Position <1% des Gesamtportfolios (außer bewusst kleine
    Talent-Trace-Positionen, die als solche gekennzeichnet sind)?
  - ETF-Anteil ≥50% des Gesamtportfolios (Ziel langfristig 60%)?
  - Regionen-Verteilung übers GESAMTE Portfolio (ETF+Aktien zusammen):
    USA ≤55% (harte Obergrenze 60%), Europa/UK 15-20%, Japan/Asien 10-15%,
    Rest (Lateinamerika, Naher Osten/Israel, sonstige – siehe "Geografische
    Streuung" oben für die vollständige Definition inkl. Cellebrite/Israel-
    Klarstellung 2026-09-04; nur bei echten Kandidaten, sonst Umverteilung auf
    Europa/UK + Japan/Asien).
  - Sektor-Verteilung übers GESAMTE Portfolio (2026-08-29, von Brian
    festgelegt, siehe Abschnitt 3): Technologie/Halbleiter 30-35%,
    Finanzwesen 20-25%, Gesundheitswesen 10-15%, Industriewerte 10-15%,
    Rest 5-10%.
  - Bei Regelverstoß: klar benennen, nicht nur stillschweigend in der
    Kennzahlen-Tabelle verstecken. Kein Verstoß ist ebenfalls explizit als
    "alle Portfolio-Regeln eingehalten" zu vermerken.

Portfolio-Charts (2026-08-29, von Brian gefordert): vier Grafiken, frisch
erzeugt mit den aktuellen Wochendaten, werden in jedes Wochenfazit-PDF
eingebettet (siehe "Charts & Benchmark-Tracking im Wochenfazit" unten) –
Gesamt-Zusammensetzung, Regionen-Verteilung, Sektor-Verteilung, Rendite je
Position.

Markt-Vergleich / Benchmark (2026-08-29, von Brian gefordert): eine Zeile/
ein Chart, das zeigt, ob das Depot seit Trackingbeginn (29.08.2026) besser
oder schlechter läuft als S&P 500, Nasdaq 100 und MSCI World (siehe
"Charts & Benchmark-Tracking im Wochenfazit" unten für Methodik).

Top 3 Gewinner / Top 3 Verlierer der Woche (2026-08-29, von Brian gefordert,
Beispiel seiner Formulierung: "ServiceNow +13,4%" oder "Hawkeye -4,5%"):
reine Kurs-Performance-Rangliste für die abgelaufene Woche (Freitag-zu-
Freitag bzw. seit dem letzten Wochenfazit-Lauf), über das GESAMTE getrackte
Universum – Depot-Positionen UND Watchlist-Werte zusammen, nicht nur Depot –
damit Brian auf einen Blick sieht, was sich diese Woche wirklich bewegt hat,
unabhängig davon ob er die Position hält. Format je Zeile: Ticker, Firmenname,
Wochenperformance in %, plus ein knapper Ein-Satz-Grund falls bekannt/
recherchierbar (Earnings, Guidance, M&A-News, Sektor-/Marktbewegung, sonst
"kein klarer Einzelgrund identifiziert – allgemeine Marktbewegung"). Kein
Ranking-Anspruch auf Vollständigkeit bei extremer Marktbreite (60+ Werte
gesamt aus Depot+Watchlist) – Kursdaten kommen wie gehabt per WebSearch/
WebFetch, keine Twelve-Data-Pflicht dafür. Eine Depot-Position UND ein
Watchlist-Wert können beide in derselben Top-3-Liste auftauchen; wird knapp
kenntlich gemacht, ob es sich um eine Depot-Position oder einen Watchlist-Wert
handelt (z.B. "ServiceNow (Depot) +13,4%" vs. "Hawkeye (Watchlist) -4,5%").

Exit-/Gewinnmitnahme-/Nachkauf-Ampel (2026-08-29, von Brian gefordert und um
die Kaufseite ergänzt, siehe "Verkaufsdisziplin & Gewinnmitnahme-Regeln"):
jede Depot-Position mit Kategorie ungleich HALTEN (NACHKAUF ERWÄGEN /
BEOBACHTEN ENGER / TEILVERKAUF ERWÄGEN / VERKAUF ERWÄGEN) wird hier explizit
benannt, mit 1-2 Sätzen fundamentaler und/oder technischer Begründung
(Twelve-Data-Kennzahlen wo verbunden, plus Zielzone bzw. Einstiegszone wo
vorhanden). Keine Auffälligkeit ist auch hier ein vollwertiges Ergebnis
("keine Position mit Exit-/Gewinnmitnahme-/Nachkauf-Signal diese Woche").

Klare Linie fürs Wochenende/die kommende Woche: konkrete Kauf-Kandidaten falls
vorhanden, sonst ausdrücklicher Hinweis "nicht auf Teufel komm raus investieren
– wenn nichts klar überzeugt, bleibt das Geld Cash" (Cash-Disziplin ist expliziter
Bestandteil des Formats, nicht nur Nebensatz).
```

Wichtig: Das Wochenfazit ersetzt nicht die vollen Analysen/Kurz-Fazits einzelner
Kandidaten – es ist die verdichtete Draufsicht aufs Gesamtdepot, die auch dann
kommt, wenn in der Woche nichts Aufregendes passiert ist ("kein akuter
Handlungsbedarf" ist ein vollwertiges, gewünschtes Ergebnis, kein Ausfall).
Technisch als eigener wöchentlicher Scheduled Task umgesetzt (siehe Technische
Bausteine).

**Ausgabeformat (2026-08-26, von Brian gefordert):** Wird nicht mehr nur als
Chat-Text geliefert, sondern zusätzlich als PDF-Datei erstellt (via pdf-Skill)
und per SendUserFile ausgeliefert, damit Brian sie herunterladen/archivieren
kann. Im Chat selbst nur noch 1-2 Sätze Kernaussage/Ampel-Status, die volle
Gliederung (siehe Format oben) steckt im PDF.

### Charts & Benchmark-Tracking im Wochenfazit (2026-08-29, von Brian gefordert)

Brian möchte die Übersichts-Grafiken (die er im Chat als Kuchendiagramme/
Balkendiagramm gesehen und gut fand) fest im wöchentlichen PDF-Report sehen,
automatisiert neu erzeugt statt manuell nachgereicht, plus einen Vergleich
seiner Depot-Performance gegen den breiten Markt ("schlage ich den Markt?").

**Vier Charts, jede Woche neu erzeugt (`reports/weekly_charts.py`):**
1. **Gesamt-Zusammensetzung** (Donut, alle Positionen inkl. ETF)
2. **Regionen-Verteilung** (Donut, 4-Regionen-Split ETF+Aktien zusammen)
3. **Sektor-Verteilung** (Donut, 5-Sektor-Split ETF+Aktien zusammen)
4. **Rendite je Position** (Balkendiagramm, Investsumme → aktueller Wert,
   grün/rot, sortiert nach Performance)

Ablauf beim Wochenfazit-Lauf: die `DATA`-Liste in `reports/weekly_charts.py`
(Name, Investsumme, aktueller Wert, Region, Sektor je Position) mit den
frisch nachgezogenen Zahlen aus `depot/finanzen-net-zero.md` aktualisieren
(neue/verkaufte Positionen entsprechend ergänzen/entfernen), Skript laufen
lassen. Es schreibt vier PNGs mit FESTEN Dateinamen (`chart_zusammensetzung
.png`, `chart_regionen.png`, `chart_sektoren.png`, `chart_rendite.png`,
alle unter `reports/`), damit `build_wochenfazit.py` sie unverändert als
`<img>` in eine eigene Charts-Seite des PDFs einbetten kann, ohne dass der
Dateiname jede Woche im Code angepasst werden muss. Die ETF-Innenverteilung
(Region/Sektor) wird über die zuletzt abgerufenen Vanguard/justetf-Gewichte
angenähert (siehe Abschnitt 3) – bei Bedarf in `ETF_REGION_SPLIT`/
`ETF_SECTOR_SPLIT` im Skript aktualisieren, wenn ein frischerer Abruf andere
Zahlen liefert (nicht jede Woche zwingend nötig, reicht alle paar Monate).

**Markt-Vergleich (Benchmark-Tracking), Methodik von Brian gewählt
(2026-08-29): reines Vorwärts-Tracking ab Trackingbeginn, keine
rückwirkende Rekonstruktion seit den tatsächlichen Kaufdaten.** Baseline
ist der 29.08.2026 (Gesamt-Depotwert 33.403,32€, S&P 500 7.711,76, Nasdaq
100 29.433,43, MSCI-World-Proxy [iShares Core MSCI World UCITS ETF,
IE00B4L5Y983] 127,735€ – siehe `depot/performance_tracking.md` für die
volle Baseline-Doku und Einschränkungen, u.a. dass USD/EUR-Wechselkurse
bei S&P 500/Nasdaq 100 NICHT herausgerechnet werden, es geht um die reine
Wachstumsrate). Ablauf jede Woche:
1. Aktuellen Gesamt-Depotwert berechnen (wie beim Rendite-Chart).
2. Aktuelle Stände von S&P 500, Nasdaq 100, MSCI-World-Proxy per
   WebSearch/WebFetch abrufen (gleiche Quellentypen wie Baseline).
3. Neue Zeile an `depot/performance_tracking.csv` UND die Verlaufs-Tabelle
   in `depot/performance_tracking.md` anhängen (Datum, Depotwert, drei
   Indexstände).
4. `reports/benchmark_chart.py` ausführen → schreibt
   `reports/benchmark_vs_depot.png` (Linienchart, % Veränderung seit
   29.08.2026 für Depot vs. alle drei Indizes) neu, fester Dateiname.
5. Kurzer Satz im Wochenfazit (Chat + PDF), ob und gegen welche(n) Index/
   Indizes das Depot aktuell vorne oder hinten liegt.

Alle fünf Charts (die vier Portfolio-Charts + der Benchmark-Chart) werden
auf einer eigenen Seite ("Charts & Markt-Vergleich") ins Wochenfazit-PDF
aufgenommen (siehe PDF-Report-Design unten für die technische Einbettung).

### Monatsrecap (2026-08-29, von Brian gefordert)

Zusätzlich zum wöchentlichen Wochenfazit bekommt Brian am jeweiligen
**Monatsende** (egal ob 28./29./30./31., siehe "Technische Umsetzung Timing"
unten) einen deutlich breiteren **Monats-Rückblick** – Brians Formulierung:
"eine Art Rewind vom Monat", der sowohl das eigene Depot als auch den
Gesamtmarkt einordnet. Kein Ersatz für das Wochenfazit (das läuft weiter
unverändert jeden Freitag) – der Monatsrecap ist die verdichtete,
höherfliegende Draufsicht über den ganzen Monat plus einen echten
Makro-/Marktteil, den das Wochenfazit bewusst nicht in dieser Tiefe hat.

**Pflichtinhalte (Brians eigene Aufzählung, 2026-08-29):**

1. **Gesamtperformance des Portfolios im Monat** (in % und in €): Depotwert
   Ende Vormonat vs. Ende aktueller Monat, unter Herausrechnung der im Monat
   eingezahlten Sparraten (siehe "Budget & Cashflow"/Cash-Reserven-Abschnitt)
   – reine Sparraten-Zuflüsse sind kein Performance-Beitrag und würden die
   Zahl sonst schönen. Das ist eine Annäherung (kein exaktes zeitgewichtetes
   Renditemaß, siehe Methodik-Hinweis unten), aber transparent nachvollziehbar
   aus `depot/performance_tracking.csv`.
2. **Monatsperformance je Depot-Position**: Kurs Anfang Monat vs. Ende Monat
   in %, je Position (analog zum wöchentlichen "Rendite je Position"-Chart,
   aber auf Monatsbasis statt "seit Kauf") – eigener Chart
   (`reports/monthly_performance_chart.py` bzw. Erweiterung des bestehenden
   Chart-Skripts um einen Monats-Modus).
3. **Wichtigste Ereignisse des Monats** (portfolio-bezogen): verdichtete
   Zusammenfassung aus den 4-5 Wochenfazits des Monats – gelaufene volle
   3-fach-Cross-Checks mit Ergebnis, Watchlist-Auf-/Abgänge (inkl. der
   Ergebnisse aus dem täglichen automatisierten Kandidaten-Scan, siehe
   Watchlist-System), Kategorie-Wechsel, ausgelöste Exit-/Gewinnmitnahme-/
   Nachkauf-Signale, sonstige marktbewegende News zu Depot-Positionen.
4. **Ausblick auf den kommenden Monat**: bekannte anstehende Katalysatoren
   für Depot- UND Watchlist-Werte (v.a. erwartete Earnings-Termine, siehe
   offener Punkt "Earnings-Kalender" in Agent-Playbook-Archiv-Diskussionen.md Abschnitt 9 – sobald der existiert,
   hier einspeisen, bis dahin per gezielter WebSearch pro Position "nächster
   Earnings-Termin" recherchieren), plus bekannte Makro-Termine im kommenden
   Monat (nächste Fed-Sitzung/FOMC-Termin, wichtige Konjunkturdatenpunkte
   wie CPI/Jobs-Report-Termine, falls bekannt).
5. **Mögliche Käufe/Verkäufe, die im kommenden Monat anstehen könnten**:
   Ableitung aus aktuellem Trigger-/Watchlist-Zustand (welche Werte nahe an
   einer Einstiegs-/Zielzone stehen, siehe "Verkaufsdisziplin &
   Gewinnmitnahme-Regeln"), aktuellem Cash-Reserven-Stand auf Scalable/
   finanzen.net zero (siehe "Budget & Cashflow", inkl. der stehenden
   Freigabe zur Cashreserve-Umschichtung) und ob ein Watchlist-Kandidat kurz
   vor einer vollen Kauf-Empfehlung steht. Keine Spekulation ohne Grundlage
   – wo nichts Konkretes ansteht, das auch so benennen ("aktuell kein
   konkreter Kauf-/Verkaufskandidat in Sicht").
6. **Depot-Performance gegenüber dem Markt für den Monat**: Erweiterung des
   bestehenden wöchentlichen Benchmark-Trackings (S&P 500, Nasdaq 100,
   MSCI-World-Proxy) auf eine Monatssicht – Monatsanfangs- vs.
   Monatsend-Stand aus derselben `depot/performance_tracking.csv`-Reihe,
   plus die kumulierte Kernaussage seit Trackingbeginn (29.08.2026) bleibt
   ebenfalls genannt, nicht nur der Monatswert isoliert.
7. **Wichtigste Marktereignisse des Monats (Makro-Rückblick, NICHT
   Portfolio-spezifisch)**: Fed-Sitzung(en)/FOMC-Entscheidungen im Monat
   (Zinsentscheidung, Ton der Pressekonferenz), wichtige Konjunkturdaten
   (US-Inflation/CPI, Arbeitsmarktbericht, ggf. EZB-Entscheidung bei
   Europa-Relevanz), marktbewegende Mega-Cap-/Sektor-Earnings auch außerhalb
   des eigenen Portfolios (z.B. Big-Tech-Berichtssaison), sowie relevante
   geopolitische/regulatorische Ereignisse, falls marktbewegend.
8. **Makro-Radar / Sentiment**: CNN Fear & Greed Index (aktueller Stand +
   grober Verlauf über den Monat, per WebFetch von cnn.com/markets/fear-and-
   greed o.ä.), VIX-Stand als ergänzender Volatilitäts-Indikator, wichtige
   Rohstoffe (Gold, Rohöl/WTI oder Brent, ggf. Kupfer als Konjunktur-
   Frühindikator), 10-Jahres-US-Treasury-Rendite als Zins-Signal, EUR/USD-
   Kursverlauf über den Monat (relevant für die EUR-Umrechnung aller
   USD-Positionen). Kurze Einordnung, nicht nur Zahlen ohne Kontext ("Markt
   aktuell im Bereich X = Gier/Angst, weil...").

**Ergänzende Inhalte (2026-08-29, von Brian nach eigener Rückfrage bestätigt
– "alle sehr gute punkte! alle einbauen"):**

9. **Transaktions-Log des Monats**: alle im Monat tatsächlich ausgeführten
   Käufe/Verkäufe (Datum, Ticker, Kurs, Stückzahl, kurze Begründung), aus
   den Wochenfazits des Monats zusammengezogen. Das Pendant zu Punkt 5
   ("mögliche Käufe/Verkäufe") – dort der Ausblick, hier das tatsächlich
   Geschehene. Falls im Monat keine einzige Transaktion stattfand, das
   explizit so benennen ("keine Transaktionen diesen Monat").
10. **Watchlist-Qualitätsbilanz**: Bilanz des täglichen automatisierten
    Kandidaten-Scans für den Monat – wie viele neue Kandidaten wurden
    automatisch aufgenommen, wie viele wieder aussortiert (Duplikat/
    Strategie-Fit/Identity-Gate-Fails zählen nicht mit, nur tatsächlich
    aufgenommene und später wieder entfernte Werte), und – sobald genug
    Historie vorliegt (ältere Zugänge, nicht erst diesen Monat
    aufgenommen) – wie sich diese Werte seit Aufnahme in der Watchlist
    tatsächlich entwickelt haben (Kursperformance seit Aufnahmedatum).
    Ist noch zu wenig Historie da, das offen so benennen statt zu
    spekulieren.
11. **Dividenden-/Einkommensübersicht**: erhaltene Dividenden-
    Ausschüttungen im Monat je Position (falls Depot-Positionen
    überhaupt Dividenden zahlen), plus grober Forward-Yield des
    Gesamtdepots. Enthält das Depot keine oder kaum dividendenzahlende
    Werte, diesen Abschnitt entsprechend kurz halten oder explizit als
    "aktuell nicht relevant" markieren statt ihn aufzublähen.
12. **Sektor-/Regionen-Drift**: wie sich die Gewichtung des Depots über
    Sektoren und Regionen im Monatsverlauf verschoben hat (durch
    Kursbewegungen einzelner Positionen und/oder durch Käufe/Verkäufe) –
    Vergleich Anfangs- vs. End-Gewichtung des Monats. Zeigt an, ob sich
    unbeabsichtigt Klumpenrisiken aufbauen (z.B. durch überproportionales
    Wachstum eines Sektors), unabhängig von bewussten Entscheidungen.
13. **Gebühren-/Kosten-Übersicht**: im Monat angefallene Orderkosten
    (Käufe/Verkäufe) und, soweit ermittelbar, Spread-Kosten – ehrlicher
    Blick auf die Kostenseite der Strategie, nicht nur auf die
    Bruttoperformance.
14. **"Was lief gut / was lief schlecht"-Rückschau**: kurze Reflexion über
    die eigenen Entscheidungen des Monats – z.B. ob ein Exit-/Nachkauf-
    Signal zu früh oder zu spät kam, ob eine Einschätzung/Prognose aus dem
    Ausblick des VORHERIGEN Monatsrecaps eingetroffen ist oder nicht (echter
    Ist-Soll-Abgleich, nicht nur Wiederholung). Das ist im Kern ein
    Mini-Decision-Journal und überschneidet sich bewusst mit dem noch
    offenen "Decision Journal"-Punkt aus der Meta-Retrospektive (Abschnitt
    9) – bis dieses eigenständig existiert, deckt der Monatsrecap diesen
    Bedarf in kompakter Form mit ab. Ehrlich bleiben, auch bei eigenen
    Fehleinschätzungen – kein nachträgliches Schönreden.
15. **Soll-Ist-Vergleich der Sparrate**: geplante vs. tatsächlich
    eingezahlte Sparbeträge im Monat (siehe "Budget & Cashflow"), falls es
    hier zu Abweichungen kam – bei planmäßiger Einzahlung reicht ein
    kurzer bestätigender Satz statt eines eigenen Abschnitts.

**Methodik-Hinweis (explizit im Report zu vermerken):** Die
Monats-Performance-Berechnung ist eine Annäherung, kein exaktes
zeitgewichtetes Renditemaß (TWR) – bei unterjährigen Zu-/Abflüssen (v.a.
die monatlichen Sparraten) kann die reale Rendite geringfügig abweichen.
Das ist bewusst in Kauf genommen (Einfachheit/Nachvollziehbarkeit vor
buchhalterischer Präzision), aber transparent zu benennen statt so zu tun,
als sei die Zahl exakt. Gleiches gilt sinngemäß für die
Watchlist-Qualitätsbilanz (Punkt 10) und die Sektor-/Regionen-Drift
(Punkt 12) – beides sind Näherungen auf Basis der vorhandenen
Trackingdaten, keine buchhalterisch exakten Attributionsanalysen.

**Technische Umsetzung – Timing (Monatsende ist kein fixer Kalendertag):**
Da Monate unterschiedlich lang sind (28/29/30/31 Tage), läuft der
zugehörige Scheduled Task an JEDEM der Tage 28-31 eines Monats (Cron
`0 21 28-31 * *`), prüft aber zuerst: ist HEUTE tatsächlich der letzte Tag
des Monats (d.h. morgen beginnt ein neuer Monat)? Nur dann wird der volle
Monatsrecap erstellt und ausgeliefert – an den übrigen Tagen (z.B. dem 28.
und 29. in einem 31-Tage-Monat) läuft der Task still durch, ohne Nachricht/
PDF ("kein Monatsende heute, kein Recap"). Das stellt sicher, dass der
Monatsrecap in jedem Monat exakt einmal kommt, unabhängig von dessen Länge.

**Ausgabeformat:** Wie Wochenfazit als eigenständige PDF-Datei
(`Monatsrecap-YYYY-MM.pdf`) per SendUserFile ausgeliefert (Agent-Optik,
eigenes Layout in Anlehnung an den Wochenreport, mit eigener Makro-Seite
für Punkte 7-8 sowie einer zusätzlichen Seite/Sektion für die
Ergänzungspunkte 9-15), plus eine sehr kurze Chat-Zusammenfassung
(2-3 Sätze Kernaussage: Monatsperformance vs. Markt, wichtigstes Ereignis,
Blick auf den kommenden Monat). Bei mageren Monaten (keine Transaktionen,
keine Dividenden, kaum Drift) fallen die entsprechenden Ergänzungspunkte
im Layout knapp aus statt künstlich aufgebläht zu werden – Kürze bei
fehlendem Inhalt ist hier bewusst richtig. Technisch als eigener, vom
Wochenfazit unabhängiger Scheduled Task umgesetzt (siehe Technische
Bausteine).

### PDF-Report-Design: "Agent Wochenreport" (2026-08-27, eigenständiges Layout)

Brian hat eine Beispiel-PDF eines Bekannten ("Raketentoni", ebenfalls 3-KI-
Agent) geteilt. Nach seiner ausdrücklichen Klarstellung (2026-08-27) dient
diese NUR als lose Inspiration, KEIN 1:1-Layout-Klon – wir brauchen ein
eigenes Alleinstellungsmerkmal in Aufbau, Farbwelt und Typografie. Was von
Raketentoni übernommen wurde, ist ausschließlich die Grundidee "eine
kompakte Seite pro Position mit klarer Ampel-Logik" – Struktur, Optik und
Reihenfolge sind bewusst eigenständig gestaltet.

**Eigene Marke/Identität:** Der Report heißt "AGENT WOCHENREPORT" (Bezug zum
Jack-Moat-Agent-Regelwerk, nicht Raketentonis generischer Titel), Untertitel
"3-KI Cross-Check · Jarvis · Conan · Jack".

**Farbwelt (bewusst abgesetzt von Raketentonis Navy-Corporate-Look):**
**Korrigiert 2026-09-07 (von Brian gefordert: "zu dunkel und schwer zu
lesen", gilt seitdem für ALLE Report-Formate, nicht nur Deep Dive):**
Basis heller, weißer Hintergrund statt dunklem Anthrazit – Kopfzeilen/
Masthead auf Weiß mit Gold-/Bernstein-Signaturlinie, statt hellem Text auf
dunklem Grund. Ein scharfer, aber auf Weiß kontraststarker Bernstein-/
Gold-Ton bleibt Signatur-Akzent (Agent-Score-Gauge, Masthead-Linie,
Hervorhebungen) – kein Grün/Gelb/Rot, das bleibt exklusiv für die
Ampel-Semantik reserviert, aber in eigenen, satteren Tönen (Tannengrün /
warmes Bernstein / sattes Karmesinrot statt Raketentonis flacherem
Grün/Orange/Rot), jeweils dunkel genug für Lesbarkeit auf hellem Grund.
Neutrale Textfarbe warmes Dunkelgrau statt reinem Schwarz. Konkrete Token
(Referenzimplementierung: `reports/render_chart.py`, `reports/
build_wochenfazit.py`, `reports/templates/ampel-batch-scan-template.html`,
`reports/CLBT-reaper-deepdive-2026-09-07.html`): `--bg:#FFFFFF`,
`--bg-panel:#F7F6F2`, `--text:#262420`, `--gold:#9C7A2E`,
`--green:#3F7D44`, `--red:#B03A2E`, `--yellow:#A6790A`. Alte, bereits
fertige Reports (vor 2026-09-07) bleiben unverändert im dunklen Schema als
Archiv – nur neu erzeugte Reports nutzen ab sofort die helle Variante.

**Typografie:** Kräftige, kondensierte Display-Schrift für Positionsnamen/
Masthead (industriell-scharfer Charakter, passend zum "Agent"-Thema),
kombiniert mit einer klaren, gut lesbaren serifenlosen Fließtext-Schrift.

**Strukturelle Alleinstellungsmerkmale (bewusst andere Reihenfolge/Optik als
Raketentoni, nicht nur andere Farben):**

- **3-Stimmen-Leiste ganz oben** (unser Kernunterschied, kommt VOR der
  These, nicht versteckt): drei farbige Badges "Jarvis · Conan · Jack" mit
  jeweiligem Einzel-Rating + Konvergenz-Label ("STARK KONVERGENT" /
  "MODERAT" / "WIDERSPRUCH") – Raketentonis Report zeigt nur ein stilles
  synthetisiertes Endergebnis, wir zeigen bewusst die Kontroverse/den
  Konsens zwischen den drei KIs als erstes.
- **Agent-Score-Gauge**: der Score (0-10) als grafischer Halbkreis-Zeiger
  statt einer stillen Tabellenzeile, daneben das Sizing-Tier als
  "Clip"-Symbol (1-4 gefüllte Segmente) – ein optisches, kein rein
  tabellarisches Element.
- **DNA-Check-Strang**: die K-Kriterien als schmaler Streifen aus 4-5
  farbigen Segmenten (Pass/Fail), angelehnt an einen DNA-Strang/Barcode,
  statt einer generischen Ampel-Tabellenzeile.
- **Chart- und Einstiegslage-Box (2026-08-31, von Brian gefordert, siehe
  "TA-Pflicht bei JEDER Einzelanalyse" oben):** feste Pflicht-Box in jedem
  Einzelpositions-PDF (Quick Filter wie Full Deep Dive) – Trend-/Momentum-
  Ampelzeilen (Twelve-Data-basiert) plus eine kompakte Zonen-Tabelle
  (Unterstützung/Widerstand → mögliche Reaktion) und die daraus mit der
  fundamentalen Margin-of-Safety-Einschätzung kombinierte Einstiegszonen-
  Empfehlung. Alle Kursangaben darin zusätzlich in EUR (Klammer-Format wie
  überall im Regelwerk).
- Danach folgen (in eigener Optik, aber vom Grundgedanken her bewährt):
  Kurzthese, Kennzahlen, Einordnung, Chancen/Risiken nebeneinander,
  Beobachten (Upgrade-/Downgrade-Trigger, Abstauber-Limit), und ein fett
  hervorgehobenes Fazit als Abschluss.

Zusätzliche Report-weite Seiten (nicht pro Position, einmal je PDF), inhaltlich
inspiriert von Raketentonis Grundidee, aber in eigener Optik umgesetzt:
- **Gesamtübersicht mit Ranggruppen A-E**: trennt Geschäftsqualität von
  aktueller Kaufattraktivität, als Querschnitt über Champions/Profi/Talent.
- **Methodik-Seite**: kurze Erklärung der Bewertungslogik + explizite Grenzen
  (Quick Filter vs. Full Deep Dive, keine Steuerprüfung, Fremdwährungs-/
  Marktabdeckungs-Einschränkungen bei Nicht-US-Titeln).
- **Quellen-Seite**: nummerierte Liste der verwendeten Primärquellen mit
  Links, plus rechtlicher Hinweis (keine Anlageberatung).
- **Charts & Markt-Vergleich-Seite (2026-08-29, von Brian gefordert):** die
  fünf in "Charts & Benchmark-Tracking im Wochenfazit" oben beschriebenen
  PNGs (`reports/chart_zusammensetzung.png`, `chart_regionen.png`,
  `chart_sektoren.png`, `chart_rendite.png`, `benchmark_vs_depot.png`)
  werden als `<img>`-Tags in eine eigene HTML-Seite eingebettet (lokaler
  Dateipfad reicht, Playwright rendert lokale Bilder beim PDF-Export
  problemlos mit; alternativ als base64-Data-URI, falls Pfadauflösung im
  Sandbox-Kontext Probleme macht). Reihenfolge: Zusammensetzung → Regionen
  → Sektoren → Rendite → Markt-Vergleich, mit je 1-2 Sätzen Kontext
  darunter (z.B. Regelverstoß-Hinweis, Benchmark-Kernaussage).

Freiheitsgrad für die Umsetzung: Die genaue grafische Feinausgestaltung
(exakte Farbwerte, Schriftwahl innerhalb der obigen Leitplanken, Feinlayout
der Gauge/des DNA-Strangs) liegt im Ermessen der jeweiligen Umsetzung
(pdf-Skill) – wichtig ist die Einhaltung der oben genannten strukturellen
Alleinstellungsmerkmale, nicht eine pixelgenaue Spezifikation.

Diese Struktur ersetzt ab sofort die bisherige knappe Bullet-Fließtext-Vorgabe
für das Wochenfazit-PDF (siehe Format weiter oben) – die inhaltlichen Punkte
dort (Depotstatus-Ampel, Kategorie-Füllstand, Auffälligkeiten, Cash-Disziplin-
Zeile) bleiben Pflichtbestandteil, werden aber jetzt in diesem saubereren
Layout statt als reiner Fließtext präsentiert.

### PDF-Report-Design: "Agent Deep Dive Report" (Full Deep Dive, 2026-09-08)

Brian hat eine weitere, deutlich ausgereiftere Beispiel-PDF von Raketentonis
System geteilt ("MP Materials – Große Aktienanalyse", 13 Seiten, mehrstufiger
Report statt Kompakt-Layout) und ausdrücklich als Inspiration für einen
eigenen "Full Deep Dive"-PDF-Standard gewünscht – **gleiche Regel wie beim
Agent Wochenreport oben: lose strukturelle Inspiration, KEIN 1:1-Klon.**
Aufbau/Reihenfolge/Sprache bleiben unser eigenes Agent-Vokabular (Ampel-
Farbwelt, Score-Gauge, 3-Stimmen-Leiste, DNA-Check-Strang), NICHT
Raketentonis Kapitel-Nummerierung oder Formulierungen. Gilt NUR für Full
Deep Dive (Quick Filter bleibt beim bestehenden Agent-Kompakt-Einseiter,
siehe "PDF-Report-Design: Agent Kompakt" – ein 13-Seiten-Report für jeden
Quick-Filter-Kandidaten wäre nicht mit dem Aufwand-/Realismus-Prinzip
vereinbar, siehe Abschnitt 6).

**Was aus der Vorlage strukturell übernommen wird (jeweils in eigener
Agent-Optik, nicht 1:1):**

1. **Mehrseitiges Format statt Einseiter** – Full Deep Dive bekommt ab
   sofort ein eigenständiges PDF (`reports/<TICKER>-deep-dive-<Datum>.pdf`,
   Agent-Deep-Dive-Layout), NICHT mehr das Agent-Kompakt-Layout gequetscht
   – der Kompakt-Einseiter bleibt für Quick Filter/Blitz-Scan-Treffer.
2. **Multi-Panel-Chart statt reiner Kurs+EMA-Grafik (technische Erweiterung
   von `reports/render_chart.py`):** zusätzlich zum bestehenden
   Haupt-Chart (Candlestick + EMA + Zonen) werden RSI(14)- und MACD-Subplots
   als eigene Panels UNTER dem Hauptchart gerendert (neue Flags
   `--rsi` und `--macd`, Rohdaten aus denselben Twelve-Data-Indikatoren, die
   das TA-Modul ohnehin schon abruft – keine zusätzliche Datenquelle nötig,
   nur zusätzliche Visualisierung dessen, was bereits berechnet wird). Nur
   für Full Deep Dive Pflicht – Quick Filter bleibt beim einfachen
   Haupt-Chart, um die Renderzeit klein zu halten.
3. **"Was steckt wirklich dahinter"-Sektion bei mehrstufigen
   Geschäftsmodellen (optional, nur wenn zutreffend):** bei Unternehmen mit
   einer klaren Wertschöpfungskette (Rohstoff→Verarbeitung→Endprodukt→Kunde,
   o.ä.) eine kompakte Kettendarstellung (Textblöcke mit Pfeilen reichen,
   kein aufwändiges Grafikelement nötig) VOR der eigentlichen These – hilft
   bei komplexen Geschäftsmodellen, den Kontext vor den Zahlen zu setzen.
   Bei einfachen Geschäftsmodellen (Standard-Software, Einzelhandel usw.)
   entfällt dieser Punkt ersatzlos, kein Zwang zur künstlichen Aufblähung.
4. **"Der unterschätzte Punkt"-Kasten (neu, Pflicht bei Full Deep Dive):**
   ein eigener, kurzer Absatz, der GEZIELT die eine Sache benennt, die bei
   oberflächlicher Betrachtung leicht übersehen wird, aber die Bewertung/
   These material beeinflusst (z.B. versteckte Verwässerung durch
   Wandelanleihen, ein Vertrag mit Kündigungsklausel, eine buchhalterische
   Besonderheit). Zwingt zur echten Tiefenrecherche statt nur der
   Oberflächen-Kennzahlen – kein Pflichtfund um jeden Preis, bei wirklich
   sauberen Fällen explizit "kein versteckter Sonderpunkt gefunden"
   vermerken statt einen künstlich zu konstruieren.
5. **Bear/Base/Bull-Wertebalken als Grafik statt nur Tabelle:** die bereits
   bestehenden TMR-/Scout-Fair-Value-Bandbreiten (Bear/Base/Bull) werden bei
   Full Deep Dive zusätzlich als horizontales Balkendiagramm visualisiert
   (Balken je Szenario + eine vierte Markierung für den aktuellen Kurs),
   nicht mehr nur als Zahlenzeile – macht auf einen Blick sichtbar, wo der
   aktuelle Kurs relativ zur Bandbreite liegt.
6. **Gepaarte "Aufstufungs-Trigger" / "Abstauber-Trigger"-Kästen:** unsere
   bereits bestehenden Nachkauf-Aufstufungs-Trigger (siehe z.B. Rocket Lab
   in `depot/kategorisierung.md`) und Abstauber-/Stop-These-Trigger (siehe
   "Verkaufsdisziplin & Gewinnmitnahme-Regeln") werden bei Full Deep Dive
   konsequent als zwei nebeneinanderstehende Kästen dargestellt statt nur
   im Fließtext verstreut – macht auf einen Blick sichtbar, was für UND was
   gegen die These sprechen würde.
7. **Score-Aufschlüsselungs-Tabelle:** die bereits bestehende Agent-Score-
   Stapel-Logik (siehe "AGENT-SCORE-STAPEL-LOGIK") wird bei Full Deep Dive
   zusätzlich als Tabelle mit den Einzeldimensionen (z.B. Moat/Burggraben,
   Wachstum, Bilanz/Finanzierung, Profitabilität/Cashflow, Bewertung,
   Ausführungsrisiko, Chart/Timing – Dimensionen je nach TMR/Scout-Pfad
   leicht unterschiedlich) sichtbar gemacht statt nur das Endergebnis zu
   zeigen – Transparenz, wo genau Punkte verloren gehen, nicht nur die
   Summe.
8. **Formale Abschluss-Seite "Quellen, Annahmen und Hinweise":** eine
   nummerierte Quellenliste (Primärquellen: SEC-Filings/Investor-Relations/
   Geschäftsberichte zuerst, siehe Datenintegritäts-System) mit Links,
   ein kurzer "Modellannahmen"-Absatz (verwendete Diskontsätze/Exit-
   Multiples/Zeithorizont für die Bear/Base/Bull-Herleitung, damit die
   Zahlen nachvollziehbar bleiben, nicht als Black Box), und der bereits
   bestehende Anlageberatungs-Disclaimer – als letzte Seite jedes Full-
   Deep-Dive-PDFs.
9. **Fact-Check-Tabelle bei mitgelieferten Drittquellen (nur wenn
   zutreffend, z.B. wenn Brian selbst einen fremden Report/Artikel als
   Kontext mitgibt):** Format "Fremdaussage | saubere Lesart (unsere
   eigene Herleitung) | warum das relevant ist" – ist bereits inhaltlich
   durch die bestehende Regel "Externe Quellen nie Benchmark" abgedeckt,
   hier nur als saubere Tabellen-Visualisierung übernommen statt reinem
   Fließtext-Widerspruch.

**Erweiterung 2026-09-07 (von Brian gefordert: "noch ausführlicher, noch
informativer, 5 oder mehr Seiten"):**

10. **Mindestlänge 5 Seiten, mehr wenn die Informationslage es hergibt.**
    Die bisherigen 3 Seiten waren ein Startpunkt, keine Obergrenze – bei
    einem Full Deep Dive mit guter Datenlage (Primärquellen verfügbar,
    3-fach-Cross-Check mit echten Funden) ist ein 3-Seiten-Report zu knapp.
    Kein künstliches Aufblähen mit Füllstoff, aber jeder der Punkte unten
    verdient echten Raum statt einer Kurzzeile.
11. **Neue Pflicht-Eröffnungsseite: narrative Burggraben-/Unternehmens-
    Einführung**, direkt nach dem Masthead, VOR der 3-Stimmen-Leiste. Analog
    zu Raketentonis Positionierungs-Aufhängern (z.B. "Das X der Y mit
    Monopolstellung bei Z") eine prägnante, eigene Kern-Aussage voranstellen,
    die die Investment-These in einem Satz einfängt – dann in mehreren
    vollständigen Absätzen (nicht Stichpunkte) erzählen: Unternehmens-
    geschichte/Entstehung, wie der Burggraben konkret entstanden ist (nicht
    nur DASS er existiert – siehe Moat-Verifikation weiter unten, die bleibt
    als kompakte Ampel-Box erhalten), Marktstellung mit konkreten Zahlen
    (Lizenzen/Kunden/Länder o.ä., wo verfügbar), und warum ein Nachbau durch
    Wettbewerber strukturell schwer ist. Diese Seite ist Erzählung/Kontext,
    keine Wiederholung der später folgenden Kennzahlen-Tabellen.
12. **Neue Pflicht-Sektion: Management.** Kurzporträt der Schlüsselpersonen
    (CEO immer, CFO/CTO wo strategisch relevant) mit vorherigem Werdegang,
    warum ihre Berufung ein Signal ist (z.B. Produkt- statt Vertriebsfokus,
    Turnaround-Erfahrung, Kapitaldisziplin-Historie), plus Grossaktionärs-/
    Insider-Struktur (wer hält wie viel, Governance-Implikation) und, sofern
    recherchierbar, eine Einschätzung des bisherigen Kapitalallokations-
    Track-Records. Ergänzt, ersetzt NICHT die bestehende kompakte
    "Management-Score (0-7)"-Tabelle aus dem älteren Reaper-Kompakt-Layout –
    hier geht es um die erzählerische Einordnung dahinter.
13. **Katalysator-Ausblick statt nur genereller Trigger-Bedingungen.** Die
    bestehenden Aufstufungs-/Abstauber-Trigger-Kästen (Punkt 6 oben) bleiben,
    werden aber um einen eigenen Abschnitt "Was als Nächstes passiert"
    ergänzt: die konkret terminierten nächsten Ereignisse (Earnings-Termin,
    Investor-Events, Shareholder-Meetings, bekannte regulatorische/
    Produkt-Termine), jeweils mit einem Satz, warum das Ereignis
    kursrelevant sein könnte.
14. **Durchgehend ausführlicherer Sprachstil.** Nicht nur die vier
    Ampel-Boxen (Moat/Going-Concern/SBC/Reality-Check, siehe 2026-09-07-
    Vorgabe) bekommen Fließtext in 3-4 Sätzen – dieselbe Prosa-statt-
    Stichpunkt-Regel gilt jetzt für den gesamten Full-Deep-Dive-Report,
    wo immer eine Einordnung mehr ist als eine reine Zahl.

**Was AUSDRÜCKLICH NICHT übernommen wird:** Raketentonis Navy-Corporate-
Farbwelt, Kapitel-Nummerierung/-Titel, Formulierungen und die reine
Multiples-/DCF-Bewertungslogik (unsere TMR-/Scout-Fair-Value-Herleitung
bleibt methodisch unverändert die eigene, siehe jeweilige Methodik-Datei) –
nur die strukturellen/visuellen Elemente oben, in unserer bereits
etablierten Agent-Optik (kondensierte Display-Schrift, 3-Stimmen-Leiste
ganz oben).

**Farbwelt:** heller, weißer Hintergrund statt dunklem Anthrazit – siehe
"Agent Wochenreport" oben für die vollständige Token-Liste, gilt seit
2026-09-07 identisch für ALLE Report-Formate (Deep Dive, Wochenreport,
Kompakt, Batch-Scan), nicht nur diesen. `render_chart.py` ist als
einziges eigenständiges Skript mit identischer Token-Liste separat
mitgezogen (Chart-PNGs müssen zum hellen PDF-Hintergrund passen, kein
dunkler Chart-Kasten mehr auf hellem Report).

**Scout-Pfad-Mapping (2026-09-08, von Brian gefordert: CLBT/ATEN liefen
beide über den TMR-Pfad — Conan/Scout-Analysen sollen dieselbe 11-Seiten-
Struktur/Tiefe bekommen, mit Scout-eigenem Inhalt statt 1:1 TMR-Vokabular
reinzupressen).** Das Seitengerüst bleibt identisch (11 Seiten, gleiche
Agent-Optik, gleiche Prosa-statt-Stichpunkt-Regel, gleiche Pflicht-
Elemente Punkt 1-14 oben), nur die INHALTLICHE Füllung je Seite wechselt
auf Conans eigenes Vokabular (siehe `conan-the-scout-v1.12.md`, aktuell
v1.16) statt TMR-Konzepte künstlich auf eine junge/spekulative Firma zu
pressen:

| Seite (TMR-Fassung, CLBT/ATEN) | Scout-Fassung (Conan-Pfad) |
|---|---|
| 1: Hook + Burggraben-Einführung | Hook + Unternehmensgeschichte, Aufhänger ist die Scout-These ("warum könnte das der nächste Compounder sein"), nicht ein bereits bewiesener Burggraben |
| 2: Management + Kapitalallokation + Glaubwürdigkeits-Matrix (0-7) | Gründer-/Führungs-Score (0-5) + Insider-Ownership/-Nachkäufe stärker gewichtet als Track-Record, der bei jungen Firmen oft fehlt |
| 3: 3-Stimmen-Leiste + DNA-Check (Badges) | 3-Stimmen-Leiste + Compounder-DNA-Check (aktiver Sektor-Override im Header: SaaS-Default/Pre-Revenue-SaaS/Deep-Tech/Biotech), gleiche Badge-Optik |
| 4: 5-Jahres-Finanzhistorie + Guidance-Track-Record | Wachstumshistorie (oft nur 2-3 Jahre, explizit als kurze Historie kennzeichnen statt künstlich 5 Jahre zu erzwingen) + Guidance-Track-Record NUR falls vorhanden, sonst "noch keine belastbare Guidance-Historie" |
| 5: Umsatz-/OCF-Grafik + Dividendenrendite | Umsatz-Grafik + Cash-Runway-/Burn-Multiple-Historie (relevanter als OCF bei unprofitablen Firmen) + Dividendenrendite (fast immer 0%, bleibt Pflichtpunkt) |
| 6: Produktlinien + Peer-Multiple-Tabelle (Op-Margin+Median) | Zukunfts-Moat-Check (4 Dimensionen: Tech-Vorsprung/Early-Adopter/Skalierung/Wettbewerbsfenster) + Referenzklassen-Vergleichstabelle (3-5 Peers gleicher Reifephase statt etablierter Multiples) |
| 7: Vier Boxen Moat/Going-Concern/SBC/Reality-Check | Vier Boxen Moat-in-Formation/Fraud-Promotion-Check/Dilution/TAM-Reality-Check |
| 8: Offene Schwächen + Root-Cause-Analyse | Killer-Thesis-Check (tragende Kernannahme) + Hype-Bias-Check (Referenzklassen-Frage) |
| 9: Chart + DCF Bear/Base/Bull + Reverse-Engineering + Downside-Boden | Chart + Outcome-Wahrscheinlichkeiten (Payoff-Verteilung, EV-Multiple) + TAM-Reality-Check-für-Tenbagger + Cash-Runway-vs-Catalyst-Guardrail |
| 10: Unterschätzter Punkt + Katalysator + Bear-Case-Katalog + Trigger | Trichter-Einordnung (Stufe 1/2/3, kein TMR-Äquivalent, prominent) + Catalyst-Check + Base-Rate-Floor-Kontext + Beobachten-Protokoll-Trigger |
| 11: Score-Aufschlüsselung + Devil's Advocate + Fazit + Quellen | Scout-Score-Aufschlüsselung + Nullhypothese-Ergebnis + Scout Conviction (10-Jahres-10x-Satz) + Fazit + Quellen |

**Was unverändert bleibt:** DQ-Badge-System (Ⓥ/Ⓣ/Ⓔ/Ⓝ), Farbwelt/Typo,
Zwei-Runden-Cross-Check-Pflicht (Rigor-Inhalte gehen in Runde 2 zurück an
Jack/Conan), PFLICHT-JSON-SUMMARY am Ende (Conans eigenes Schema, siehe
Regel 43), Quellen-Seite mit Korrektur-Historie-Konvention. **Was NICHT
1:1 übernommen wird:** kein DCF/WACC/Reverse-DCF (Scout arbeitet mit
EV/Sales+TAM-Sanity-Check statt DCF, siehe Conan-Prompt "BEWERTUNG – KEIN
DCF-ZWANG"), kein Piotroski/ROIC-DNA-Check (Compounder-DNA-Kriterien sind
strukturell andere), kein Rating "KAUFEN" (Scout vergibt bewusst nur
WATCHLIST-ELITE/BEOBACHTEN-*/ZU FRÜH/DURCHGEFALLEN, nie eine vollständige
Kauffreigabe — das bleibt im Fazit-Text erklärt, nicht verwässert).

### Full-Deep-Dive-Tiefe: Rigor-Standard nach uncoveredjapan.com-Vorbild (2026-09-07)

Brian hat die 5-teilige Digital-Arts-(2326)-Deep-Dive-Serie von
uncoveredjapan.com als Qualitätsmaßstab vorgegeben ("das nenn ich einen
Deep Dive!") und ausdrücklich verlangt, eine ähnliche Tiefe/Ausführlichkeit
in unsere eigenen Full-Deep-Dive-Analysen einzubringen. **Gleiches Prinzip
wie bei allen bisherigen externen Vorbildern (Raketentoni, MP Materials):
lose methodische Inspiration, KEIN 1:1-Klon** – die konkreten Techniken
unten werden in unser eigenes TMR-/Scout-/Agent-Vokabular übersetzt, nicht
Autor-Formulierungen oder fremde Struktur kopiert. Alle 5 Teile wurden
einzeln durchgearbeitet (nicht nur Teil 1), da die Serie bewusst Business/
Moat, Zahlen, Kapitalallokation, Strategie und Bewertung in getrennten,
jeweils vollwertigen Teilen behandelt – die Summe daraus definiert den
Tiefe-Maßstab, nicht ein einzelner Teil.

**Was konkret als neue Full-Deep-Dive-Pflicht bzw. Best-Effort-Ergänzung
übernommen wird (jeweils nur wo die Datenlage es zulässt – siehe
No-False-Precision-Regel, kein Erfinden von Zahlen):**

1. **5-Jahres-Finanzhistorie statt nur TTM-Snapshot.** Umsatz und
   Betriebsergebnis/Operating Profit über die letzten 5 Geschäftsjahre in
   einer Tabelle, inkl. CAGR. Einmaleffekte (Verkäufe, Akquisitionen,
   Sondererträge) explizit benennen und eine "like-for-like"-bereinigte
   Wachstumsrate danebenstellen, statt eine durch Einmaleffekte verzerrte
   YoY-Zahl unkommentiert stehen zu lassen.
2. **Guidance-Track-Record-Tabelle (neu, sofern Management eigene
   Jahres-Guidance kommuniziert).** Für die letzten 3-5 Jahre: Guidance
   vs. tatsächliches Ergebnis (Umsatz UND operatives Ergebnis), daraus
   Durchschnitts-Erreichungsgrad, Streuung/Standardabweichung, Trend-
   richtung (verbessert/verschlechtert sich die Prognosequalität?), und
   wo erkennbar eine zeitliche Clusterung der Fehlschläge (z.B. immer
   Q4-lastig wegen öffentlicher Aufträge). Das ist ein eigenständiges,
   objektives Managementglaubwürdigkeits-Signal, unabhängig von Rating/
   Score – Ziel: "Discount company forecasts" so weit wie die Historie es
   nahelegt, nicht blind übernehmen.
3. **Cashflow-Normalisierung bei Sondereffekten.** Wenn Working-Capital-/
   Deferred-Revenue-Bewegungen den operativen Cashflow einmalig auf- oder
   abblähen: explizit herausrechnen und die "wahre" wiederkehrende
   Cash-Erzeugungsfähigkeit danebenstellen, mit einem Satz Begründung,
   warum die Rohzahl irreführend wäre.
4. **Bilanzkennzahlen-Fallstrick-Check.** Bevor ein auf den ersten Blick
   negativ wirkender Bilanztrend (z.B. sinkende Eigenkapitalquote)
   kommentiert wird: prüfen, ob die Ursache tatsächlich Schwäche ist oder
   ein an sich positiver Grund (z.B. Wachstum der Deferred-Revenue-
   Passivposition durch mehr Cloud-/Subscription-Verträge bei gleichzeitig
   steigendem Cash-Bestand). Beide Lesarten benennen, nicht nur die
   pessimistische.
5. **Produktlinien-/Segment-Tabelle mit benannten Wettbewerbern.** Wo das
   Geschäftsmodell mehrere klar unterscheidbare Produktlinien hat: pro
   Zeile Produkt, adressiertes Problem, wichtigste 1-2 namentlich genannte
   Wettbewerber, statt nur eine aggregierte "Moat ist stark"-Aussage für
   das Gesamtunternehmen.
6. **Konzentrations-Transparenz mit Namen statt nur Prozent, wo
   auffindbar.** Bei Kunden-/Vertriebspartner-Konzentration nach Möglichkeit
   den/die konkreten Namen nennen (z.B. bestimmter Großdistributor/-kunde
   mit Umsatzanteil), nicht nur eine anonyme "Top-X = Y%"-Zahl – macht das
   Risiko greifbar statt abstrakt. Wenn nicht auffindbar: wie bisher
   anonymisiert, aber explizit vermerken, dass keine Namen recherchierbar
   waren (kein stilles Weglassen).
7. **Eigenständige, proaktive "Offene Schwächen"-Sektion.** Getrennt vom
   bestehenden Devil's Advocate (der die BULL-These angreift): eine Sektion,
   die strukturelle Schwächen so benennt, wie das Management selbst sie
   einräumen würde – inkl. direkter Management-Zitate, wenn in Earnings-
   Calls/Transkripten auffindbar (z.B. ein CEO, der einen Prognosefehler
   selbst zugibt). Nicht am Ende versteckt, sondern gleichrangig zu den
   Stärken platziert.
8. **Kapitalrückführungs-Historie statt nur aktuellem Status.** Dividenden-
   Historie (Streak aufeinanderfolgender Erhöhungen, falls zutreffend),
   Gesamtausschüttungsquote (Dividende + Buybacks) über mehrere Jahre als
   Trend, und Buyback-Timing als Glaubwürdigkeits-Indiz (z.B. Rückkäufe
   direkt nach einem Kurscrash = starkes Signal, dass Management den
   eigenen Kurs für unterbewertet hält).
9. **Management-Glaubwürdigkeits-Matrix statt einzelnem Management-Score.**
   Mehrere GETRENNTE Achsen bewerten statt einer Gesamtnote: Guidance-
   Treffsicherheit, Aktionärsrückgabe-Konsistenz, Transparenz (werden
   Booking/Backlog/Segment-Daten offengelegt?), Selbstreflexion (werden
   Fehler eingeräumt oder schöngeredet?) – ein Unternehmen kann bei
   Kapitalrückführung exzellent und bei Prognosetreue schwach sein
   gleichzeitig, das muss sichtbar bleiben statt zu einer Note verschmolzen
   zu werden.
10. **Peer-Multiple-Vergleichstabelle mit benannten Wettbewerbern.**
    Mindestens 2-3 namentlich genannte, wirklich vergleichbare Wettbewerber
    mit Forward-KGV, P/B, EV/EBITDA nebeneinander – und wenn eine Anomalie
    auffällt (z.B. höchste Marge im Vergleichsfeld bei gleichzeitig
    niedrigstem Multiple), das explizit als Spannung benennen statt nur
    Zahlen tabellarisch abzulegen.
11. **DCF-Cross-Check per Reverse-Engineering.** Zusätzlich zum bestehenden
    Bear/Base/Bull-DCF: aus dem AKTUELLEN Kurs rückwärts rechnen, welches
    implizite Wachstum/welche implizite Marge der Markt gerade einpreist –
    macht sichtbar, ob der Markt bereits pessimistischer/optimistischer ist
    als das eigene Base-Case-Szenario, als zusätzliche Plausibilitätsprüfung
    neben der bestehenden TV-Anteil-Warnung.
12. **Downside-Boden explizit quantifizieren.** Wo eine Netto-Cash-Position
    signifikant ist: explizit als Cash-pro-Aktie ausweisen und als
    "effektiver Bewertungsboden" einordnen (z.B. "selbst im Extrem-Bear-Fall
    liegt der Cash-Wert pro Aktie bei X, was Y% Downside-Schutz ab dem
    aktuellen Kurs bedeutet").
13. **Bear-Case als benannter Wahrscheinlichkeits-Katalog statt Fließtext-
    Liste.** 3-5 konkrete, einzeln benannte Risiken, jeweils mit eigener
    Eintrittswahrscheinlichkeits-Einschätzung (Niedrig/Mittel/Hoch) statt
    einem undifferenzierten Absatz "es gibt Risiken".
14. **Root-Cause-Analyse bei jeder Guidance-Kürzung/negativen Überraschung.**
    Nicht nur feststellen DASS gekürzt wurde, sondern explizit einordnen:
    Nachfrage-Problem (strukturell, schlechter) oder Ausführungs-/Timing-
    Problem (Vertriebskanal, Verzögerung, potenziell vorübergehend)? Diese
    Unterscheidung ist entscheidend für die Bull/Bear-Einordnung und wird
    oft übersprungen, wenn nur die Prozentzahl der Kürzung genannt wird.
15. **SWOT-Synthese-Tabelle als optionale Zusatz-Visualisierung**, wenn die
    übrigen Sektionen (Moat, Reality-Check, Devil's Advocate, offene
    Schwächen, Katalysator-Ausblick) bereits genug Substanz für alle vier
    Felder liefern – kein Pflichtelement, aber eine sinnvolle Ein-Blick-
    Zusammenfassung bei komplexen Fällen mit vielen beweglichen Teilen.
16. **Umsatz-Historie als echte Balkengrafik, nicht nur Tabelle (neu,
    2026-09-08, von Brian gefordert nach Vorbild uncoveredjapan.com).** Die
    5-Jahres-Umsatztabelle (Punkt 1 oben) bekommt zusätzlich eine visuelle
    Balkengrafik (ein Balken je Jahr, Guidance-/Schätzjahr optisch abgesetzt
    in hellerem Gold statt vollem Akzentton) – macht Wachstum/Dezeleration
    auf einen Blick sichtbar, wo eine reine Zahlenspalte es nicht tut.
17. **Operating-Cashflow-Historie als eigene Pflicht-Grafik + Tabelle (neu).**
    Bisher wurde nur FCF (Free Cashflow) gezeigt – OCF (Operating Cashflow,
    vor Capex) fehlte komplett. Mehrjährige OCF-Balkengrafik analog zur
    Umsatzgrafik ergänzen, da OCF-Trend (z.B. "OCF verdreifacht sich in 4
    Jahren" oder "OCF fällt trotz Umsatzwachstum") oft aussagekräftiger ist
    als die bereits vorhandene FCF-Marge-Diskussion allein.
18. **Dividendenrendite als expliziter Pflicht-Datenpunkt (neu), auch wenn
    NICHT zutreffend.** Jede Full-Deep-Dive-Analyse zeigt explizit: zahlt
    das Unternehmen eine Dividende (Ja/Nein), aktuelle Rendite, Historie
    (seit wann, Wachstumsrate der Ausschüttung), oder bei Nichtzutreffen
    einen expliziten Vermerk "keine Dividende" statt stillschweigendem
    Weglassen. **Wichtige Lektion aus dem ersten Praxis-Fall (A10
    Networks, 2026-09-08):** ein erster Report hatte fälschlich "zahlt
    keine Dividende" behauptet, obwohl A10 tatsächlich seit ~2023 eine
    wachsende Quartalsdividende zahlt (Rendite ≈1,4%) – der Fehler wurde
    erst durch Brians Nachfrage nach genau diesem Datenpunkt aufgedeckt.
    Das unterstreicht: Dividendenrendite gehört ab jetzt zur festen
    Prüfliste, nicht zu einer Annahme aus dem Bauchgefühl heraus (junge
    Wachstumsfirmen zahlen oft keine Dividende, aber das ist eine zu
    verifizierende Tatsache, keine sichere Vermutung).
19. **Peer-Multiple-Tabelle bekommt zusätzlich eine Operating-Margin-Spalte
    UND einen Median-Bezug (neu, 2026-09-08, von Brian gefordert nach
    Vorbild uncoveredjapan.com Teil 5).** Die bestehende Peer-Multiple-
    Vergleichstabelle (Punkt 10 oben) zeigte bisher nur Forward-KGV +
    Größenordnung. Jetzt zusätzlich: Operating-Margin je Peer (Non-GAAP wo
    das die branchenübliche Vergleichsbasis ist, sonst GAAP/EBIT explizit
    kennzeichnen) UND eine explizite Median-Zeile/Referenz, sobald
    mindestens 3 direkt vergleichbare börsennotierte Peers vorliegen (bei
    weniger Peers: Einzelvergleich statt Median, transparent so benennen,
    kein künstlicher Median aus 1-2 Werten). Ziel: die "hohe Marge, aber
    unterdurchschnittliches Multiple"-Anomalie (oder umgekehrt) auf einen
    Blick erkennbar machen, wie im Digital-Arts-Vorbild (dort: höchste
    Marge im Sektor bei gleichzeitig niedrigstem Multiple als zentraler
    Bewertungs-Fund).
20. **Bear/Base/Bull-DCF-Tabelle bekommt zusätzlich explizite qualitative
    Kernannahmen je Szenario (neu, gleicher Anlass wie Punkt 19).** Bisher
    zeigte die Tabelle nur Wachstumsraten/Terminal-g als Zahlen. Direkt
    darunter (als kurze Stichpunkt-Liste, nicht als zusätzliche
    Tabellenspalte, um die Tabellenbreite nicht zu sprengen) je 1 Satz pro
    Szenario, WAS konkret passieren müsste – z.B. "Bear: Kundenkonzen-
    trations-Risiko materialisiert sich, Guidance wird erneut gekürzt" statt
    nur der abstrakten Wachstumsrate dahinter. Macht die DCF-Szenarien
    nachvollziehbar mit der übrigen Analyse (Offene Schwächen, Katalysator-
    Ausblick, Bear-Case-Katalog) verknüpft, statt isoliert dazustehen.
21. **Datentyp-Tags in der DNA-Check-Tabelle als kompakte Farb-Badges statt
    Klammer-Text (neu, 2026-09-08, von Brian gefordert: "kann man das
    Klammer-Geschreibsel nicht weglassen").** Die zugrunde liegende
    Tag-Disziplin selbst ([LIVE]/[VERIFIED]/[TRAINING]/[ESTIMATE]/[N/V],
    Klasse-A-Regel aus dem Datenintegritäts-System) bleibt UNVERÄNDERT –
    sie bestimmt weiterhin Daten-Konfidenz, Score-Deckel und Sizing-Limits
    und wird in den textlichen Divergenz-Einordnungen (z.B. "Jacks Zahl
    [VERIFIED] vs. Conans [TRAINING]") weiterhin ausgeschrieben, wo sie
    argumentativ gebraucht wird. Nur die WIEDERHOLTE Anzeige in jeder
    einzelnen Tabellenzelle wird visuell verschlankt: statt
    "12,0% ❌ [VERIFIED]" steht jetzt "12,0% ❌ Ⓥ" – ein kleines farbiges
    Badge (Ⓥ grün = Verified/Live, Ⓣ gelb = Training, Ⓔ blau = Estimate,
    Ⓝ rot = Nicht verfügbar), mit einer einzeiligen Legende direkt unter
    der Tabelle. Gilt NUR für die DNA-Check-Tabelle selbst – Prosa-Stellen
    (z.B. im Modellannahmen-DCF-Absatz auf der Quellen-Seite, "Rf 4,1%
    [TRAINING]") behalten die ausgeschriebene Klammer-Form, da dort keine
    repetitive Tabellen-Unruhe entsteht. CSS-Referenzimplementierung:
    `.dqtag`/`.dqtag-v`/`.dqtag-t`/`.dqtag-e`/`.dqtag-n`/`.dqtag-legend` in
    den bestehenden Full-Deep-Dive-HTML-Dateien.

22. **Eigene historische Bewertungs-Bandbreite statt nur Einzel-Peer-
    Vergleich (neu, 2026-09-08, ausgelöst durch ChatGPTs Cross-Review des
    CLBT-Reports).** Zusätzlich zur Peer-Multiple-Tabelle (Punkt 10): das
    eigene Forward-/Trailing-KGV (oder branchenübliches Multiple) über die
    letzten 3-5 Jahre als Band/Median darstellen und den aktuellen Wert
    dagegen einordnen (z.B. "KGV 18,7x liegt X% unter eigenem 3J-Median").
    Anders als ein Einzel-Peer-Vergleich (der bei nur 1-2 vergleichbaren
    Börsentiteln schwach aussagekräftig ist, siehe CLBT/MSAB) ist das ohne
    Datenverfügbarkeits-Risiko umsetzbar – eigene Kurs-/EPS-Historie ist
    über Twelve Data direkt abrufbar. Wird bereits an einzelnen watchlist.md-
    Einträgen informell so gemacht (z.B. Copart, Rollins), ab jetzt fester
    Full-Deep-Dive-Bestandteil.
23. **SBC-Trendverlauf über 3 Jahre statt nur Ist-Wert (neu, 2026-09-08,
    Gemini-Cross-Review).** Der bestehende SBC-Infection-Check (Ist-Wert,
    z.B. "11-13% vom Umsatz") bekommt eine Trendkomponente: SBC/Umsatz-Quote
    der letzten 3 Geschäftsjahre nebeneinander, um zu unterscheiden, ob die
    Quote sinkt (Skalierungseffekt – SBC wächst langsamer als Umsatz, Signal
    für sich normalisierende Kapitalallokation) oder steigt (eskalierendes
    Verwässerungsrisiko für Altaktionäre). Ein einzelner Ist-Wert kann beide
    sehr unterschiedlichen Situationen nicht unterscheiden.
24. **Sensitivitätsmatrix (3×3 WACC × FCF-Wachstum) für das DCF-Reverse-
    Engineering (neu, 2026-09-08, Gemini-Cross-Review).** Das bestehende
    Reverse-DCF (Punkt 11) liefert bisher nur einen Einzelwert (implizites
    Wachstum bei EINEM WACC). Ergänzend: kleine Matrix mit 3 WACC-Stufen
    (z.B. -0,5pp/Basis/+0,5pp) × 3 Wachstumsannahmen, um zu zeigen, wie
    empfindlich der implizierte Fair Value auf Zinsänderungen reagiert –
    reiner Python-Rechenschritt, keine neue Datenquelle nötig, daher ohne
    Ausnahme umsetzbar.
25. **Konzentrations-Check wird um einen expliziten 10-K-Risikoabschnitts-
    Suchschritt ergänzt (Schärfung von Punkt 6, 2026-09-08, Gemini-Cross-
    Review).** Statt nur allgemein nach benannten Distributoren/Großkunden
    zu suchen: gezielt den "Risk Factors"-Abschnitt des aktuellen 10-K/20-F
    nach einer expliziten &gt;10%-Konzentrationsangabe durchsuchen (Unternehmen
    sind SEC-meldepflichtig, sobald ein einzelner Kunde/Partner diese
    Schwelle überschreitet) – ein gezielter Suchschritt statt einer
    allgemeinen Recherche, bevor der Datenpunkt als "nicht auffindbar"
    vermerkt wird (siehe Datenintegritäts-Philosophie: fehlender Nachweis
    ist kein positiver Befund, aber ein gezielter Suchschritt schöpft die
    verfügbare Quelle wenigstens aus).
26. **"Kill-Sheet" als eigenständig benannte, konsolidierte Sektion statt
    verteilter Trigger-Listen (neu, 2026-09-08, ChatGPT-Cross-Review).** Die
    bereits bestehenden Nachkauf-/Abstauber-Trigger-Boxen (siehe
    "Bei KAUFEN/BEOBACHTEN"-Pflichtabschnitte in den Methodik-Dateien) werden
    im PDF-Report zusätzlich unter einer eigenen, klar benannten Überschrift
    "🔪 Thesis-Kill-Sheet" gebündelt UND mit dem konkreten nächsten
    Prüfpunkt-Datum (nächste 1-2 Earnings-Termine) direkt verknüpft. Inhalt
    bereits vorhanden (4 Aufstufungs- + 4 Abstauber-Trigger mit Ist-Werten
    im CLBT-Report), reine Konsolidierungs-/Auffindbarkeits-Verbesserung,
    kein neues Analyse-Element.
27. **ARR-/Umsatzwachstums-Qualitätszerlegung als Best-Effort-Zusatz (neu,
    2026-09-08, ChatGPT-Cross-Review) – NUR wo offengelegt.** Wo ein
    Unternehmen New-Logo- vs. Expansion-/Cross-Sell-Anteil am ARR-Wachstum
    offenlegt (z.B. Investor-Deck, nicht bei allen Firmen der Fall): diese
    Zerlegung ergänzen, um "gesundes" (Neukunden-getriebenes) von
    "verlangsamtem, aber durch Bestandskunden kaschiertem" Wachstum zu
    unterscheiden. Ebenso: bei einer Guidance-Kürzung nach Möglichkeit
    Region/Kundensegment/Vertragsgröße der betroffenen Deals recherchieren
    (Earnings-Call-Transkript/Analysten-Q&A, nicht 10-Q-Fließtext). **Explizit
    als Best-Effort markiert, kein Pflichtelement:** beide Datenpunkte sind
    bei den meisten Unternehmen aus wettbewerblichen Gründen nicht öffentlich
    granular verfügbar – wo nicht auffindbar, gilt wie bisher: explizit als
    Lücke vermerken (Punkt 6/25-Prinzip), nicht stillschweigend weglassen
    oder rückwirkend erzwingen. Realistischster Zeitpunkt für einen Fund:
    Analysten-Q&A im nächsten Earnings-Call, nicht rückwirkende Recherche.

**Herkunft Punkte 22-27:** Brian hat den CLBT-Full-Deep-Dive-Report
unabhängig sowohl ChatGPT als auch Gemini zur Bewertung vorgelegt (außerhalb
dieses Systems, als externe Zweitmeinung zur eigenen Methodik). Beide
Rückmeldungen wurden von Jarvis gegen den tatsächlichen Report-Inhalt
verifiziert (keine der genannten Zahlen/Lücken war erfunden) und
unabhängig voneinander bewertet – bemerkenswert: die sechs konkreten
Verbesserungsvorschläge beider KIs überschneiden sich praktisch nicht
(ChatGPT: Guidance-Cut-Forensik, ARR-Qualitätszerlegung, eigene
historische Bewertung, Kill-Sheet-Konsolidierung; Gemini: Distributoren-
Konzentration im 10-K, SBC-3-Jahres-Trend, Reverse-DCF-Sensitivität) – ein
Muster, das dem Grundprinzip des eigenen 3-fach-Cross-Checks entspricht:
unterschiedliche Perspektiven finden unterschiedliche blinde Flecken.

**Was AUSDRÜCKLICH NICHT übernommen wird:** die Serien-Aufteilung in 5
separate Veröffentlichungen (unser Full Deep Dive bleibt EIN
zusammenhängender Report, auch wenn er dadurch länger wird), die englische
Sprache/der Autoren-Ton, und die Praxis "AI-generated from primary
Japanese sources" als Selbstzweck zu betonen – unsere eigene
Datenintegritäts-/Tagging-Disziplin (LIVE/VERIFIED/TRAINING/ESTIMATE/N/V)
bleibt die eigene, bereits etablierte Methode, um Quellenqualität
transparent zu machen.

**Prozess-Pflicht: Rigor-Standard-Inhalte werden an Jack/Conan
zurückgespielt (2026-09-08, von Brian gefordert, ausgelöst durch einen
echten Fund):** Beim ersten CLBT- und ATEN-Full-Deep-Dive wurden die 15
Rigor-Techniken oben (5-Jahres-Historie, Guidance-Track-Record,
Produktlinien-Tabelle, Peer-Multiples, Management-Porträts,
Kapitalrückführungs-Historie usw.) ausschließlich von Jarvis SOLO
recherchiert, NACHDEM Jack und Conan bereits mit dem ursprünglichen
(schlankeren) Fact-Pack fertig geantwortet hatten – diese Inhalte
durchliefen also nie den eigentlichen 3-fach-Cross-Check. Genau das führte
bei A10 zu einem realen, unbemerkten Widerspruch (zwei unterschiedliche
Gesamtschulden-Zahlen aus zwei Quellen in zwei Report-Abschnitten, nie
gegeneinander geprüft) – von Brian entdeckt, nicht vom System selbst.

**Ab sofort verbindlich:** Full Deep Dive läuft zweistufig statt
einstufig. **Runde 1** (wie bisher): schlankes Fact-Pack → Jack + Conan →
DNA-Check/Moat/Score/Reality-Flags/Devil's-Advocate. **Runde 2 (neu,
Pflicht):** Jarvis recherchiert die Rigor-Standard-Inhalte (die 15 Punkte
oben), fasst sie in einem zweiten, kompakten Zusatz-Fact-Pack zusammen und
schickt dieses ERNEUT an Jack und Conan, mit der expliziten Bitte, die
neuen Zahlen (5-Jahres-Historie, Guidance-Zahlen, Konzentrations-/
Bilanzangaben, Peer-Multiples) per eigener Live-Suche gegenzuprüfen und
Abweichungen zu benennen – genau wie in Runde 1 bei DNA-Check-Kennzahlen
bereits etabliert. Erst nach dieser zweiten Rückkopplung gilt der Rigor-
Teil des Reports als vollständig cross-gecheckt, nicht nur Jarvis-solo-
recherchiert. Gefundene Abweichungen werden wie bei Runde 1 transparent
im Report benannt (siehe z.B. CLBT NRR 112%/117%-Divergenz), nicht
stillschweigend geglättet. Diese zweite Runde kostet zusätzliche Zeit/
Tokens pro Report – das ist ein bewusster Tausch für echte statt nur
behauptete Cross-Check-Tiefe.

### Jack-Prompt-Redesign-Anfrage abgewogen, additiv statt Komplett-Rewrite umgesetzt (2026-09-08, ausgelöst durch Brians externes Gespräch mit Jack/Conan)

Brian hatte am Vorabend mit Jack (Gemini) und Conan (ChatGPT) außerhalb
dieser Session über eine mögliche Komplett-Neufassung von Jacks
72.000-Zeichen-Systemprompt diskutiert. Conans Vorschlag ("TMR COMPACT
ENGINE v13.0"): Persona/Sarkasmus raus, Sizing-Tiers/Portfolio-Logik
komplett aus Jack raus und zentral in einem "Master-Agent" bündeln,
einheitliches JSON-Output-Schema für alle 3 KIs, Makro/Prediction-
Tracking/Exit-Mechanik zentralisieren. Brian bat Jarvis um eine
Einschätzung, ob man den kompletten Prompt so neu aufsetzen soll.

**Jarvis' Bewertung:** Ein Komplett-Rewrite wurde abgelehnt. Die
Detailtiefe des aktuellen Prompts (Sektor-Override-Tabellen, DNA-Check-
Schwellen, Entscheidungshierarchie, Debt-Maturity-Check, CRP-Sourcing-
Kaskade, die 36 Klasse-A-Regeln) ist genau die Mechanik, die in dieser
Session reale Fehler gefangen hat (Kundenkonzentration 37%→38% bei ATEN,
GAAP/Non-GAAP-Verwechslung, Schulden-Diskrepanz $226M vs. $219,5M,
A10-Dividenden-Fehler bei CLBT/ATEN-Deep-Dives) – eine generischere,
kürzere Version hätte diese vermutlich nicht gefangen. Außerdem: es
existiert noch kein programmatischer Master-Agent, der JSON mechanisch
verarbeitet – Jarvis liest aktuell die volle Prosa-Antwort und wertet
qualitativ aus; ein reines JSON ohne die begründende Prosa (Devil's-
Advocate-Argumentation, benannte Quellen, Management-Zitate) würde genau
die Nachvollziehbarkeit nehmen, die für Cross-Checks gebraucht wird.

**Umgesetzt wurden stattdessen additiv drei Ideen mit echtem Mehrwert**
(in `prompts/jack-moat-reaper-v11.7.md`, v11.9 → v11.10):
1. **Persona/Sarkasmus-Pflicht entfernt** (MANDAT-Sektion gekürzt) – das
   System wird primär von einer anderen KI ausgewertet, nicht von einem
   Menschen gelesen, Ton-Overhead kostet nur Tokens ohne Analysewert.
2. **Makro-Radar zentralisiert** – lief zuvor redundant bei allen 3 KIs
   einzeln, läuft jetzt zentral bei Jarvis, Jack referenziert nur noch
   mitgelieferten Kontext statt eigenen Web-Search-Aufwand zu betreiben.
3. **Neuer SCHRITT 8 – PFLICHT-JSON-SUMMARY** ergänzt (Regel 37): ein
   strukturierter JSON-Block am Ende von MODUS A/EARNINGS-PREP, der die
   bereits ausgewiesenen Prosa-Werte (Agent Score, Moat, Valuation,
   Rating, Sizing-Vorschlag, aktive Flags) zusammenfasst – erleichtert
   künftige Cross-Checks, ERSETZT aber nicht die Prosa-Herleitung.
   Sizing-Vorschlag im JSON ist explizit als "Vorschlag, keine
   Portfolioentscheidung" gekennzeichnet – die finale Gewichtung bleibt
   bei Jarvis als Master im Cross-Check mit Conan/Claude, unabhängig
   davon, was Jack selbst vorschlägt (dessen unabhängige Sizing-Meinung
   bleibt als Cross-Check-Signal erhalten, siehe z.B. die informative
   Divergenz Jack SCHROTT/0% vs. Conan BEOBACHTEN/1-1,5% bei ATEN).

Analyse-Substanz (DNA-Check, alle Sektor-Overrides, Entscheidungs-
hierarchie, Stapel-Logik, Klasse-A-Regeln 1-36) bewusst unverändert
gelassen. Conans Kompakt-Entwurf selbst wurde nicht übernommen.

**Nachtrag (2026-09-08): kein neuer "Master-Agent"-Hermes-Job — bestehenden
Cross-Check-Schritt stattdessen um JSON-Parsing erweitert.** Brian hatte
gefragt, ob der im Redesign-Diagramm gezeigte "Master Agent" (vergleicht
Daten/prüft Risiken/prüft Depot-Regeln) von Hermes übernommen werden
könnte, als eigener neuer Cron-Job. Beim Blick in
`~/.claude/scheduled-tasks/taeglicher-trigger-check/SKILL.md` zeigte sich:
diese Rolle existiert dort bereits (Schritt 5 – voller 3-fach-Cross-Check
mit Jack/Conan-Bridge-Aufruf, Depot-Regel-Prüfung, UND die "Order-
Ausführung ist IMMER manuell"-Grenze ist dort schon hart eincodiert, siehe
Abschnitt "FIXE GRENZEN"). Ein zweiter, paralleler Hermes-Job hätte diese
Logik nur dupliziert/auseinandergerissen statt sie zu verbessern.

Stattdessen wurde die eigentliche Lücke geschlossen: der bestehende
Cross-Check-Schritt hat Jack/Conan bisher nur als Prosa gelesen, nicht
über die neuen JSON-Summary-Blöcke (SCHRITT 8 bei Jack v11.10 /
PFLICHT-JSON-SUMMARY bei Conan v1.13). Ergänzt in
`~/.claude/scheduled-tasks/taeglicher-trigger-check/SKILL.md` (Abschnitt
"Jack (Gemini) / Conan (ChatGPT) per API-Bridge"): nach jedem Bridge-Call
wird jetzt zusätzlich der JSON-Block aus der Antwort geparst und im
Cross-Check-Vergleich (Schritt 5) explizit gegenübergestellt (Rating,
Score, Sizing-Vorschlag, aktive Flags), statt nur die Prosa zu lesen und
den Vergleich implizit im Fließtext zu ziehen. Gilt auch für interaktive
Full-Deep-Dive-Sitzungen (wie CLBT/ATEN in dieser Session) – dort läuft
derselbe Vergleich manuell durch Jarvis, jetzt mit derselben strukturierten
Grundlage.

**Namensgebung (2026-09-08, von Brian gefordert): der Master-Agent heißt
Aegis.** Analog zu Jack (Gemini) und Conan (ChatGPT) bekommt die bisher nur
als Rollenbeschreibung geführte vierte Position im Redesign-Diagramm
("Master Agent" – vergleicht Daten/prüft Risiken/prüft Depot-Regeln) einen
Eigennamen: **Aegis**. Wichtig: Aegis ist KEINE vierte, separate KI oder
ein eigenständiges Programm – es ist Jarvis (Claude) in genau der
orchestrierenden Rolle, die in diesem Playbook und in den Prompts bereits
beschrieben ist (Cross-Check-Synthese, Depot-Regel-Prüfung, finale Sizing-/
Rating-Entscheidung, NIE Order-Ausführung). Umgesetzt: `jack-moat-reaper-
v11.7.md` (v11.10→v11.11) und `conan-the-scout-v1.12.md` (v1.13→v1.14) –
alle operativen "Master-Agent"-Referenzen (MANDAT, MAKRO-KONTEXT, SCHRITT
8/PFLICHT-JSON-SUMMARY, Regel 37/43, JSON-Feld `sizing_proposal.note`)
durch "Aegis" ersetzt, historische Changelog-Einträge unverändert gelassen
(gleiche Konvention wie beim Reaper→Agent-Rebrand). Sollte Aegis künftig
tatsächlich zu einem eigenständigen, programmatischen Master-Agent
ausgebaut werden (siehe Diskussion oben zu "noch kein programmatischer
Master-Agent"), bleibt der Name unverändert – nur die dahinterliegende
Implementierung würde sich ändern, nicht die Bezeichnung.

**Zweiter Nachtrag (2026-09-08): Conan-Redesign-Diskussion mit ChatGPT —
kein Neubau, sondern gezielte Redundanz-Kürzung.** Brian ließ dieselbe
Frage (Komplett-Neubau vs. Anpassung) parallel noch für Conan von ChatGPT
prüfen. ChatGPT schlug zunächst eine "CONAN SCOUT ENGINE v2.0" vor (7-18
Module, 300-500 statt 824 Zeilen), zog das aber nach Prüfung der
tatsächlichen v1.12-Datei selbst zurück: praktisch jedes vorgeschlagene
"neue" Modul existierte bereits (Future-Moat-4-Achsen = `🚀 ZUKUNFTS-MOAT-
CHECK`, "was muss für 10x wahr sein" = `🔍 TAM-REALITY-CHECK FÜR DEN
TENBAGGER-FALL`, Base-Rate/Referenzklasse = `🎲`-Modul +
`REFERENZKLASSEN-VERGLEICH`, Kill-Switch = `🕵 FRAUD-/PROMOTION-RED-FLAGS-
CHECK` — sogar umfangreicher als ChatGPTs Vorschlag, u.a. VIE-Struktur-
Check —, IPO-Modul = `🚨 NEGATIV-CATALYST-CHECK`, Gründer-Score bereits
5-faktorig statt "Founder-CEO = automatischer Punkt"). Jarvis' eigene
Gegenprüfung (volle 824 Zeilen zeilenweise gelesen) kam zum selben
Ergebnis, fand aber einen echten, bis dahin übersehenen Punkt: die 24
zuletzt ergänzten Regeln (19-42) im Abschnitt GLOBALE REGELN waren fast
wortgleiche ZWEITFORMULIERUNGEN von Mechaniken, die im Fließtext bereits
vollständig ausformuliert stehen — anders als Jacks Prompt, wo der
Regelabschnitt am Dokumentende schon immer nur als Kurzverweis auf die
einzige verbindliche Formulierung diente ("Diese Sektion klassifiziert
NUR..."), nicht als Zweitformulierung.

**Umgesetzt** (`conan-the-scout-v1.12.md`, v1.14→v1.15): Regeln 19-42 von
voller Wiederholung auf kompakte "siehe [Abschnitt] oben"-Verweise
gekürzt, exakt nach Jacks eigener GLOBALE-REGELN-Konvention. Keine
einzige Schwelle, Formel, Override-Tabelle oder Konsequenz wurde entfernt
oder verändert — nur die doppelte Formulierung, ~50 Zeilen (~6%)
eingespart. Alle Selbstverweise im Fließtext auf Regelnummern (Zeile
197→Regel 26 Moat-Deckel, Zeile 231→Regel 32 Minimale-Annahme, Zeile
619→Regel 31 Vorrang-Prinzip) bleiben gültig, da Regelnummerierung und
-reihenfolge unverändert blieben. Persona/Ton, Sektor-Overrides,
EV-Multiplikatoren-Disclaimer und die N/V-Abbruch-Logik (bereits über die
vier Sektor-Overrides abgefedert, siehe Gegenprüfung oben) blieben
bewusst unangetastet — kein Rewrite, keine neue Architektur, reine
Verschlankung. Die Hermes-SKILL.md-Dateien (`taeglicher-trigger-check`,
`blitz-scan`) wurden im selben Schritt auf "v1.15 intern" nachgezogen
(siehe Hermes-Gedächtnis-Synchronisations-Pflicht oben).

**Dritter Nachtrag (2026-09-08): erneute ChatGPT-Prüfung der tatsächlichen
v1.15-Datei — 9 von 10 Punkten bereits erledigt, ein echter Fund
umgesetzt (v1.16).** Brian gab ChatGPT die reale v1.15-Datei zur Prüfung.
Ergebnis: ChatGPT bestätigt erneut "kein Neubau", listet aber 10
Verbesserungspunkte. Jarvis' Bewertung je Punkt:

- **Bereits erledigt/kein Handlungsbedarf** (6 von 10): Outcome-
  Wahrscheinlichkeiten sind bereits im PFLICHT-DISCLAIMER explizit als
  "KEIN statistisches Modell" deklariert (ChatGPT bestätigt das selbst im
  eigenen Text); Conan hat keinen eigenen Makro-Radar-Block, nur die
  Kontext-Zeile MAKRO-RÜCKENWIND (schon so); Jack/Conan haben bereits
  unterschiedliche Score-Vokabulare (Scout Score ≠ Agent Score); die
  Cross-Check-JSON-Felder sind bereits vergleichbar strukturiert; die
  große Redundanz-Fundstelle (Regeln 19-42) ist bereits behoben (siehe
  zweiter Nachtrag oben); ein konkreter JSON-Optimierungsvorschlag fehlte.
- **Abgelehnt** (2 von 10): Sizing komplett auf reine Konvictions-Label
  ohne %-Spanne reduzieren — Conan gibt bereits Spannen statt Punktwerten
  aus, explizit als "kein Beschluss" markiert; eine Spanne ist
  informativer als ein Label ohne Zahl, kein Erkenntnisgewinn durch
  weiteres Entfernen. Persona "massiv" kürzen — bei genauer Prüfung ist
  der Abschnitt zu ~80% Substanz (Skepsis-Grundhaltung als echte
  Anti-Hype-Instruktion), nur ~2 Zeilen sind reine Ausschmückung.
- **Echter, neuer Fund, umgesetzt** (1 von 10): das K-Kriterium-[N/V]-
  Sofort-Abbruch (Klasse A, bis dahin "keine Ausnahme") benachteiligt
  systematisch schwer recherchierbare, aber nicht per se schwächere
  Märkte (ChatGPTs Beispiel: ein japanisches Small Cap mit dünner/nicht-
  englischer Offenlegung) gegenüber gut abgedeckten US-Werten. Das ist
  ein ANDERER Einwand als der ursprünglich abgewiesene (der betraf
  konzeptionelle Nicht-Anwendbarkeit von Kriterien, längst über die vier
  Sektor-Overrides gelöst) — hier geht es um echte Auffindbarkeits-Lücken
  bei konzeptionell anwendbaren Kriterien. Direkt relevant für dieses
  Projekt: im Repo liegen bereits reale Analysen zu japanischen Werten
  (HOYA, RORZE, Disco Corp, Lasertec), und der tägliche Kandidaten-Scan
  durchsucht explizit Nikkei/TOPIX vollständig bei Portfolio-Lücken.

**Umgesetzt** (`conan-the-scout-v1.12.md`, v1.15→v1.16): neuer Tag
`[N/V-RECHERCHIERT]` im DATA-INTEGRITY-SYSTEM + entsprechend ergänzte
ABBRUCH-LOGIK + neue Regel 44. Bewusst eng geschnitten, kein Freifahrt-
schein: Ausnahme vom Sofort-Abbruch gilt NUR wenn alle drei Bedingungen
erfüllt sind — (1) Kriterium ist für den aktiven Sektor-Override
konzeptionell anwendbar (keine Override-Mischung mit Punkt 1), (2) eine
dokumentierte, im Output konkret benannte Recherche liegt vor (welche
Quellen geprüft wurden), (3) höchstens EIN K-Kriterium pro Analyse trägt
diesen Tag — ein zweites fällt zurück auf den normalen Sofort-Abbruch,
keine Kumulierung. Konsequenz: Status zählt als ⚠ (Grenzfall) in die
bestehende K-BASIS−1/−2-Logik ein statt Sofort-Disqualifikation,
Konfidenz-Deckel max. 🟡 (nie 🟢). PFLICHT-JSON-SUMMARY um
`data_gap_exception_used` (Boolean) ergänzt, damit Aegis sieht, wann die
Ausnahme gezogen wurde. Die Beweislast-Doktrin ("unbelegte Story = K.O.")
bleibt unangetastet — nur eine NACHGEWIESENE Recherche mit Negativ-
Ergebnis qualifiziert, keine pauschale Aufweichung. Hermes-SKILL.md-
Dateien im selben Schritt auf "v1.16 intern" nachgezogen.

### Watchlist-System (2026-08-28, von Brian gefordert)

Zusätzlich zum eigentlichen Depot führt der Agent eine eigenständige
**Watchlist** unter `watchlist.md` im Projektwurzelverzeichnis. Zweck (Brians
Formulierung): Werte, die als möglicher **Ersatz für bestehende Depot-
Positionen** dienen könnten, oder die einfach **interessant für eine
künftige Portfolio-Aufnahme** sind.

**Kern-Eigenschaften:**
- **Feste Obergrenze: max. 50 Werte gesamt** (2026-09-08 von Brian ausdrücklich
  auf 50 angehoben, vormals 20-30: "obergrenze aufheben und auf 50 Plätze
  hochschrauben"). Bewusst begrenzt, damit Brian nicht den Überblick
  verliert – kein unbegrenztes Sammelbecken.

**Direkte Brian-Vorgaben ohne vollen 3-fach-Cross-Check (2026-09-08,
neuer Präzedenzfall).** Brian bat direkt um Aufnahme von vier konkret
benannten Firmen (Ligand Pharmaceuticals, UCB SA, Itochu, Qnity
Electronics) – anders als beim automatisierten Kandidaten-Scan (dort
Pflicht: Identity-/Strategie-Fit-/Duplikations-Gate + 3-fach-Quick-Filter
vor Aufnahme) wurden diese vier NUR mit Jarvis-Solo-Recherche kategorisiert
und mit CRV versehen, kein Bridge-Aufruf an Jack/Conan. Das ist bewusst so
gehandhabt worden (Zeitaufwand vs. Direktvorgabe des Nutzers), aber jeder
Eintrag ist im Kurzthese-Feld explizit als "kein voller 3-fach-Cross-Check
gelaufen" markiert – falls Brian vor einer echten Kaufentscheidung die
volle Absicherung will, muss das noch nachgeholt werden. Gleichzeitig
wurde die Obergrenze auf 50 angehoben, damit direkte Brian-Vorgaben nicht
automatisch einen Ersatz eines bestehenden Werts erzwingen.
- **Gleiche Kategorie-Logik wie das Depot** (siehe Abschnitt 3): Jeder
  Watchlist-Wert wird **Champions / Profi / Talent** zugeordnet, je nachdem,
  in welche Depot-Kategorie er bei einer Aufnahme fallen würde. Brian möchte
  ausdrücklich alle drei Kategorien gefüllt sehen, nicht nur eine
  Ansammlung von Mega-Caps.
- **Strategie-Fit vor Vollständigkeit (2026-08-29, von Brian gefordert):**
  siehe Abschnitt 3, "Strategie-Fit-Gate für neue Kandidaten" und
  "Duplikations-Check gegenüber dem FTSE-All-World-ETF" – beide gelten auch
  für die Watchlist. Alle drei Kategorien gefüllt zu sehen (Punkt oben)
  bedeutet ausdrücklich NICHT, Lücken mit beliebigen Kandidaten aufzufüllen,
  nur damit eine Kategorie voll aussieht. Lieber eine Kategorie bleibt
  vorübergehend dünner besetzt, als dass ein Wert ohne klaren Strategie-Fit
  aufgenommen wird.
- **ISIN-Pflicht:** Jeder Watchlist-Eintrag führt zusätzlich zu Ticker/Börse
  auch die ISIN, damit ein Kauf direkt ausführbar recherchiert ist, ohne
  dass Brian das selbst nachschlagen muss.
- **Identity-Gate (2026-08-29, aus der Meta-Retrospektive Jack/Conan/Jarvis,
  siehe Agent-Playbook-Archiv-Diskussionen.md Abschnitt 9, Phase 1):** Bevor ein Kandidat neu in `watchlist.md`
  aufgenommen wird, müssen fünf Identitätsmerkmale explizit verifiziert und
  im Eintrag vermerkt sein: **Ticker, ISIN, Börsenplatz (Exchange), Land
  (Country), Sektor**. Grund (Jacks Punkt aus der Retrospektive): bei
  Kandidaten mit mehreren Notierungen, ähnlichen Firmennamen oder
  Ticker-Kollisionen zwischen Börsen ist sonst nicht sauber ausgeschlossen,
  dass Brian am Ende beim Broker das falsche Wertpapier findet. Fehlt eines
  der fünf Merkmale, bleibt der Kandidat vorläufig außen vor, bis es
  nachgezogen ist – kein Platzhalter-Eintrag ohne verifizierte Identität.
- **ISIN-Gegenprobe bei JEDER WebSearch-Fundamentaldaten-Recherche
  (2026-09-02, von Brian gefordert – ausgelöst durch einen echten
  Beinahe-Fehler):** Das Identity-Gate oben gilt bisher nur für die
  Watchlist-NEUAUFNAHME. Beim Orion-Oyj-Fall (ad-hoc Einzelanalyse auf
  Brians Wunsch, kein Watchlist-Eintrag) lieferte eine WebSearch nach
  "Free Cashflow/Net Debt" scheinbar passende Zahlen – tatsächlich gehörten
  sie zu **"Orion S.A."** bzw. **"Orion Group Holdings"**, zwei völlig
  andere, börsennotierte Firmen (US-Industrie/Carbon-Black bzw.
  Bauwesen), nicht zu Orion Oyj (FI0009014377, finnischer Pharmakonzern).
  Nur durch Plausibilitätsprüfung (falsche Größenordnung, falsche Währung/
  Kennzahlen-Charakteristik) fiel das auf, nicht durch eine strukturierte
  Prüfung. **Neue Pflicht, gilt für JEDE Fundamentaldaten-Recherche per
  WebSearch/WebFetch, nicht nur Watchlist-Neuaufnahmen:** Bei Firmennamen,
  die nicht eindeutig sind (mehrere börsennotierte Firmen mit ähnlichem/
  gleichem Namen, unterschiedliche Aktienklassen, ADRs auf anderen Börsen)
  muss jede übernommene Kennzahl gegen mindestens EIN Identitätsmerkmal der
  Quelle gegengeprüft werden (ISIN, exakter Ticker inkl. Börsenplatz, oder
  bei Fehlen dessen zumindest Land + Sektor + Größenordnung/Währung
  plausibilisiert). Passt die Quelle nicht eindeutig zum recherchierten
  Wertpapier, gilt die Kennzahl als **[N/V]**, nicht als "wahrscheinlich
  richtig" – lieber eine Datenlücke im Fact-Pack als eine falsch
  zugeordnete Kennzahl. Bei Namens-Ambiguität in der eigentlichen
  WebSearch-Anfrage nach Möglichkeit ISIN oder Ticker+Börsenplatz explizit
  in die Suchanfrage aufnehmen, um Kollisionen von vornherein zu
  vermeiden, statt sie erst im Ergebnis zu bemerken.
- **Wöchentlicher automatisierter Check (jeden Freitag, Teil des
  Wochenfazit-Laufs, siehe unten):** Für jeden Watchlist-Wert wird per
  WebSearch geprüft, ob es in der Woche etwas Meldenswertes gab (Earnings,
  Guidance-Änderung, News, Kursbewegung). Begründung, warum ein wöchentlicher
  statt nur gelegentlicher Check nötig ist (Brians Formulierung): Werte
  können jederzeit aus beliebigem Grund von der Liste fliegen – schlechte
  Schlagzeilen, katastrophale Quartalszahlen, gerissene These usw. – das
  System muss dafür "ständig auf der Suche" und aktuell sein.
- **CRV-Ampel je Watchlist- UND Depot-Wert (2026-09-03, von Brian gefordert):
  Bewertungs-/Timing-Signal zusätzlich zur Champions/Profi/Talent-
  Qualitätskategorie.** Grund (Brians Formulierung, Beispiele): "DISCO
  CORP 🟡 ABWARTEN/BEOBACHTEN, noch im Abwärtstrend oder noch überbewertet"
  bzw. "ALPHABET 🟢 KAUFEN, Unterbewertung obwohl fundamental intakt".
  Champions/Profi/Talent sagt NUR etwas über Geschäftsqualität aus, nichts
  über den aktuellen Einstiegszeitpunkt – die CRV-Ampel schließt diese
  Lücke als eigene Spalte in `watchlist.md` UND (seit 2026-09-03, "das soll
  auch für die Werte gelten, die bereits im Depot enthalten sind") in
  `depot/kategorisierung.md` für alle 18 aktuellen Depot-Positionen.
  **Vier Stufen** (2026-09-03 von Brian auf 🟠 erweitert, "verschiedene
  Farben mit einbringen um flexibel zu sein"):
  - 🟢 **KAUFEN/NACHKAUFEN** – klar unterbewertet ggü. eigener Historie/Peers, These intakt.
  - 🟡 **ABWARTEN/BEOBACHTEN (bzw. HALTEN bei Depot-Werten)** – fair bewertet, kein starkes Signal in beide Richtungen.
  - 🟠 **VORSICHT/TEUER** – spürbar teuer ggü. Historie/Peers, aber kein hartes Warnsignal (spekulativ, nicht fundamental gebrochen).
  - 🔴 **MEIDEN/ÜBERBEWERTET** – deutlich überbewertet und/oder mehrere gleichzeitige Warnsignale
    (z.B. Bewertung läuft der Ertragsentwicklung erkennbar davon).
  **Kursverlust-Nachkauf-Bias-Schutz (2026-09-08, angeregt durch einen
  Vergleich mit Raketentonis System, dort explizit formuliert: "Ein
  Kursverlust ist allein kein Argument für einen Nachkauf"):** ein
  gefallener Kurs allein rechtfertigt NIE eine 🟢-Hochstufung – die
  CRV-Ampel bleibt ausschließlich an der tatsächlichen Bewertung
  (KGV/KBV vs. Historie/Peers) und der Unternehmensqualität festgemacht,
  nicht am Ausmaß des Rückgangs selbst. Ein -30%-Kursrückgang bei einer
  Position, die vorher bereits teuer war, landet bestenfalls bei fair
  bewertet (🟡), nicht automatisch bei 🟢 – "ist stark gefallen" und "ist
  jetzt günstig" sind zwei unterschiedliche Aussagen, die nicht verwechselt
  werden dürfen (bewusste Ergänzung zur bereits bestehenden Trennung von
  Geschäftsqualität und Einstiegszeitpunkt, siehe oben – hier zusätzlich:
  auch INNERHALB der Einstiegszeitpunkt-Bewertung selbst nicht den
  Kursverlauf mit dem Bewertungsniveau verwechseln).
  **Bei Depot-Positionen ausdrücklich kein automatisches Verkaufssignal**
  – 🔴/🟠 heißt "kein Nachkauf jetzt", nicht "verkaufen"; dafür gelten
  weiterhin ausschließlich die dokumentierten Abstauber-/Stop-These-
  Trigger (siehe "Verkaufsdisziplin & Gewinnmitnahme-Regeln").
  Basiert auf KGV vs. historischem Durchschnitt (10J-Median wo verfügbar)
  und Peer-/Branchenvergleich. Erstbefüllung aller 30 Watchlist- und 18
  Depot-Werte am 2026-09-03 per WebSearch-Snapshot. **Pflege:** wird ab
  jetzt beim wöchentlichen Watchlist-Check (siehe oben, Teil des
  Wochenfazit-Laufs) mitaktualisiert – Bewertungen ändern sich schneller
  als Geschäftsqualität, ein einmaliger Snapshot veraltet sonst unbemerkt.
  Kein eigener täglicher Check nötig
  (das würde die tägliche Ampel aus dem folgenden Punkt unnötig
  überladen) – wöchentlicher Rhythmus reicht für ein Bewertungssignal.
  **Methodik-Klarstellung (2026-09-03, von Brian korrigiert: "du sollst
  nach unserem System die Aktie bewerten... andere Webseiten kann man
  dazu nehmen, aber nie als Benchmark"):** die Ampel-Farbe ist immer das
  EIGENE Urteil (Jarvis bzw. bei vollen Cross-Checks das 3-KI-Team),
  hergeleitet aus unserer eigenen Logik (KGV im Kontext von Wachstumsrate/
  Marge/Moat-Qualität, analog zur Multiples-Schnellcheck-Logik aus
  `jack-moat-reaper-v11.7.md`). Externe Quellen (GuruFocus,
  stockanalysis.com u.ä.) liefern ausschließlich ROHDATEN (aktueller/
  historischer KGV, Branchen-Durchschnitt) – ein fertiges
  Drittanbieter-Urteil ("Significantly Overvalued", "X% above/below Fair
  Value") wird NIEMALS direkt als eigene Einschätzung übernommen oder
  zitiert, da ein proprietärer fremder Algorithmus keine nachvollziehbare,
  im eigenen Regelwerk verankerte Methodik ist. Bei der Erstbefüllung am
  2026-09-03 wurde das an mehreren Stellen nicht sauber getrennt, seither
  korrigiert – gilt ab jetzt als feste Regel für jede künftige Pflege.
  **Trend-Pfeile bei Auf-/Abstufung (2026-09-03, von Brian gefordert):**
  ändert sich die CRV-Farbe eines Werts gegenüber der vorherigen
  wöchentlichen Pflege, wird das zusätzlich mit 🔺 (Aufstufung, Ampel
  verbessert sich, z.B. 🟠→🟡 oder 🟡→🟢) bzw. 🔻 (Abstufung, Ampel
  verschlechtert sich, z.B. 🟢→🟡 oder 🟡→🟠/🔴) markiert – Format
  "Farbe+Pfeil KURZLABEL (hoch-/abgestuft von [alte Farbe]) – Grund".
  Unveränderte Ampeln bekommen keinen Pfeil. Voraussetzung: der
  wöchentliche Pflege-Schritt muss die BISHERIGE Farbe lesen, bevor er sie
  überschreibt, um den Vergleich ziehen zu können. Stand 2026-09-03 ist
  die Basislinie ohne Vorwert – erste Pfeile entstehen frühestens beim
  nächsten wöchentlichen Watchlist-/Depot-Check.
  **Drei Ergänzungen nach 3-KI-Produkt-Feedback-Runde (2026-09-03, Jack UND
  Conan unabhängig um Verbesserungsvorschläge gebeten, überschneidende
  Punkte priorisiert umgesetzt):**
  1. **MoS-Drawdown-Hinweis gilt jetzt für ALLE 48 Werte** (Watchlist +
     Depot), nicht mehr nur für AI-Trend-exponierte – beide KIs bemängelten
     unabhängig, dass der Fokus nur auf AI-Hype-Werte fälschlich den
     Eindruck erweckt, andere Werte seien vor scharfen Korrekturen sicherer.
  2. **Qualität-×-CRV-Matrix ergänzt** (siehe `watchlist.md` und
     `depot/kategorisierung.md`) – beide KIs nannten das die wichtigste
     strukturelle Ergänzung: eine Kreuztabelle Champions/Profi/Talent ×
     CRV-Farbe macht sofort sichtbar, wo Qualität UND Preis zusammenpassen
     ("Champions+Grün" = höchste Priorität) und wo eine gute Firma nur
     gerade teuer ist ("Champions+Rot" ≠ schlechtes Unternehmen).
  3. **Depot-CRV-Wortwahl entschärft:** "MEIDEN/ÜBERBEWERTET" klingt bei
     einer bestehenden Position wie ein Verkaufssignal, obwohl es keins
     ist – für Depot-Positionen jetzt "NACHKAUF ATTRAKTIV" / "HALTEN-
     BEOBACHTEN" / "KEIN NACHKAUF (TEUER)" / "KEIN NACHKAUF – ÜBERBEWERTET
     (Review empfohlen)" statt der Watchlist-Formulierungen KAUFEN/MEIDEN.
  **Zwei weitere Ergänzungen (2026-09-03, auf Brians ausdrücklichen
  Wunsch nach der ersten Runde nachgezogen):**
  4. **Bewertungsanker je Geschäftsmodell (Conans Vorschlag):** KGV ist
     der Standard-Anker, aber nicht überall sachlich richtig. Banken/
     Versicherer (Münchener Rück, Allianz, Bank Central Asia) bekommen
     explizit den Zusatz "Anker: KBV/ROE statt KGV" – diese
     Geschäftsmodelle werden am Markt strukturell über Buchwert-Multiples
     bewertet, nicht Gewinn-Multiples. Kein Ankerhinweis in der Zelle
     bedeutet: KGV ist der passende Standard-Anker.
  5. **5. Farbe 🔘 GRAU – "keine belastbare Aussage" (Conans Vorschlag):**
     für Fälle, in denen weder KGV noch ein tragfähiger Ersatzmaßstab aus
     dem Fact-Pack ableitbar ist (Gewinn nahe null/stark verzerrt, keine
     Historie) – methodisch sauberer, als eine nicht belastbare Zahl
     künstlich in eine der vier Farben zu pressen. Aktuell angewendet auf
     CrowdStrike (Watchlist) sowie Kraken Robotics und HawkEye 360
     (Depot).
  Weitere Vorschläge aus der Feedback-Runde (PEG/FCF-Yield/Insider-Käufe/
  Short-Interest als Sekundärsignale, Confidence-Level, Revisionstrend)
  sind weiterhin bewusst NICHT umgesetzt – als offener Punkt für eine
  spätere, gezielte Erweiterung vorgemerkt, um das System nicht in einem
  Schritt zu überladen.
  **Margin of Safety / historisches Drawdown-Verhalten (2026-09-03, von
  Brian ergänzt: "auch die Kurse aus der Vergangenheit mit einbeziehen,
  z.B. dass Nvidia in der Vergangenheit auch mal 40-50% korrigieren
  kann"):** ein 🟢-KAUFEN-Signal (günstig ggü. eigener Historie) ist KEINE
  Garantie gegen eine erneute scharfe Korrektur – insbesondere bei
  AI-Trend-/Hype-getriebenen Werten sind 30-50%+ Drawdowns historisch
  normal, auch wenn die fundamentale These im Nachhinein intakt blieb
  (Beispiel Nvidia: -56% 2018, -66% 2021/22, trotzdem seither jeweils
  wieder deutlich höhere Hochs). Bei AI-Trend-exponierten Watchlist-Werten
  wird das historische Max-Drawdown-Muster zusätzlich zur reinen
  KGV-Kennzahl in der CRV-Begründung dokumentiert (siehe `watchlist.md`,
  Feld "MoS-Hinweis"). Ersetzt nicht die bestehende Positionsgrößen-
  Disziplin (Sizing-Tiers/Positions-Cap) – "günstig" heißt nicht
  "risikofrei".
- **Tägliche Watchlist-News-Ampel (2026-09-03, von Brian gefordert, als
  schnelle Vorstufe zum wöchentlichen Check oben, nicht als Ersatz):**
  Auslöser – Brian bemerkte anhand eines fremden Beispiel-Systems (tägliche
  E-Mail mit Rot/Gelb/Grün-Einstufung je Watchlist-/Depotwert), dass sein
  eigener wöchentlicher Rhythmus bei akuten Ereignissen (Rückruf,
  Regulatorik-Warnung, Cybervorfall, Analysten-Down-/Upgrade) bis zu 6 Tage
  Verzögerung bedeutet. Ab jetzt läuft zusätzlich TÄGLICH (Teil des
  Täglichen Trigger-Checks, siehe unten, Schritt 3B) ein kompakter
  News-Scan über alle aktuellen Watchlist-Werte mit einer Ampel:
  - 🔴 ROT – erfüllt eines der bestehenden Ausschluss-Kriterien (siehe
    "Ausschluss-/Abstiegs-Kriterien" in `watchlist.md`) → sofortige
    Entfernung von der Watchlist, Chat + PushNotification + E-Mail.
    **Archivierung statt Löschen (2026-09-03, P2-Punkt aus dem
    3-KI-System-Audit):** die Zeile wird dabei nicht ersatzlos gestrichen,
    sondern in den Abschnitt "Ausschluss-Archiv" am Ende von
    `watchlist.md` verschoben (Format dort dokumentiert) – Historie bleibt
    nachvollziehbar.
  - 🟡 GELB – kein Ausschlussgrund, aber These-relevante Entwicklung → Wert
    bleibt, Status auf ⚠️ RISIKO gesetzt, kurzer Kommentar im Eintrag,
    Erwähnung im Tages-Fazit.
  - 🟢 GRÜN – keine relevante Änderung oder positive Bestätigung → keine
    Aktion, bei echtem Neuigkeitswert kurz im Tages-Fazit erwähnt, sonst
    still (kein Rauschen bei 20-30 Werten täglich).
  Der wöchentliche Freitags-Check bleibt als tiefere, breitere Prüfung
  zusätzlich bestehen – die tägliche Ampel ist die schnelle Vorstufe, kein
  Ersatz.
- **Erinnerungs-Mechanismus für offene Empfehlungen (2026-09-03, von Brian
  gefordert: "bei Aktien, die für einen Kauf oder Verkauf in Frage kommen,
  mich erinnern, falls ich es vergessen haben sollte, auch per Mail").**
  Grund: eine einmalige Benachrichtigung bei Empfehlungs-Entstehung reicht
  nicht – wenn Brian eine Kauf-/Verkaufszone übersieht oder vergisst, gibt
  es bisher keinen Nachfass-Mechanismus. Neue, feste Datei
  `depot/offene_empfehlungen.md` führt alle aktuell offenen KAUFEN/
  NACHKAUFEN/VERKAUFEN/TEILVERKAUF-Empfehlungen (nicht BEOBACHTEN – das ist
  nicht handlungsrelevant, gehört nicht in diese Liste).
  - **Eintrag:** jede volle 3-fach-Analyse oder Zonen-Benachrichtigung mit
    KAUFEN/NACHKAUFEN/VERKAUFEN/TEILVERKAUF-Ergebnis wird dort mit Datum
    und Quelle vermerkt.
  - **Tägliche Prüfung (Teil des Täglichen Trigger-Checks):** für jeden
    offenen Eintrag wird geprüft, ob inzwischen eine passende Transaktion
    erkannt wurde (Scalable via `list_portfolio_transactions`; bei den
    drei manuellen Brokern über Brians Bestätigung/aktualisierte
    `depot/*.md`-Datei) – wenn ja, Eintrag entfernen.
  - **Erinnerungs-Rhythmus:** bleibt ein Eintrag **5 Werktage** ohne
    Ausführung offen (ab Ursprungsdatum bzw. seit der letzten Erinnerung),
    wird erneut erinnert – Chat-Nachricht UND E-Mail (Brians ausdrücklicher
    Wunsch), Format kompakt ("Erinnerung: <Position> steht seit <Datum> als
    <Empfehlung> offen, noch keine Ausführung erkannt. Zone/Preis: <...>").
    Kein täglicher Spam – Intervall bewusst auf 5 Werktage gesetzt, um
    Erinnerungsmüdigkeit zu vermeiden, aber ein Vergessen nicht auf
    unbestimmte Zeit unbemerkt zu lassen.
  - **Eintrag wird entfernt**, wenn: Ausführung erkannt, eine neue Analyse
    die Empfehlung ersetzt/aufhebt, oder Brian sie manuell als erledigt/
    verworfen markiert.
  **Präzisierung (2026-09-03, von Brian gefordert – "auf unsere Strategie
  angepasst", nicht das fremde Beispiel unverändert übernommen):** Vier
  zusätzliche, verbindliche Anpassungen an das eigene System:
  1. **Kategorie-abhängige Schwelle.** Dieselbe News wird bei Champions
     zurückhaltender eingestuft als bei Talent/Zock – ein bewiesener,
     breiter Moat (Champions-Kriterium) übersteht einzelne Ereignisse eher
     als eine per Definition noch unbewiesene Talent-These. Faustregel:
     bei Champions/Profi nur 🔴, wenn ein echtes Ausschluss-Kriterium hart
     erfüllt ist (siehe watchlist.md); bei Talent reicht dafür schon eine
     deutliche Verschlechterung der ohnehin dünneren Datenlage/These.
  2. **Zeithorizont-Tag beachten (siehe "Zeithorizont-Tag innerhalb
     Talent/Zock" oben).** Bei Talent-Werten mit Tag **Zock/Trade** ist
     laut Regelwerk ohnehin die Charttechnik/das Stop-Loss maßgeblich für
     Exit-Entscheidungen, nicht die fundamentale These – die tägliche
     Ampel bewertet solche Werte NICHT eigenmächtig thesenbasiert auf 🔴,
     sondern verweist bei News-Funden auf die bestehende
     chart-/stop-loss-basierte Logik. Bei Tag **Talent (langfristig)**
     gilt dagegen dieselbe thesenbasierte Ampel-Logik wie bei Champions/
     Profi.
  3. **Abgleich gegen die dokumentierte Kurzthese.** Die Ampel-Einstufung
     bewertet nicht generisch "ist das schlechte News", sondern konkret:
     widerspricht der Fund der in `watchlist.md` für genau diesen Wert
     hinterlegten Kurzthese/Moat-Begründung? Eine News kann negativ klingen
     und trotzdem 🟢/🟡 bleiben, wenn sie den eigentlichen Investment-Case
     nicht berührt (z.B. eine Rechtsstreitigkeit in einem irrelevanten
     Nebensegment).
  4. **ISIN-Gegenprobe gilt auch hier** (siehe "ISIN-Gegenprobe bei JEDER
     WebSearch-Fundamentaldaten-Recherche" weiter unten) – bei mehrdeutigen
     Firmennamen wird jeder News-Fund gegen ISIN/Ticker+Börsenplatz der
     watchlist.md-Zeile gegengeprüft, bevor er einer Ampel-Farbe zugeordnet
     wird. Unklare Zuordnung zählt als [N/V], nicht als 🔴/🟡-Fund.
- **Täglicher automatisierter Kandidaten-Scan (2026-08-29, von Brian gefordert
  – Erweiterung, nicht Ersatz des wöchentlichen Checks oben):** Brian möchte
  ausdrücklich NICHT nur, dass bestehende Watchlist-Werte wöchentlich auf
  News geprüft werden, sondern dass "die 3 Agenten ständig im Hintergrund auf
  der Suche sind, um interessante Werte für die Watchlist zu finden" –
  täglich, automatisiert, systematisch, unabhängig davon ob Brian aktiv ist.
  Deshalb läuft ab sofort als Teil des Täglichen Depot-Trigger-Checks (siehe
  unten, 19:00 UTC) zusätzlich ein Kandidaten-Scan-Schritt:
  1. **Screening (Schritt 1, kein Browser nötig):** WebSearch/WebFetch gegen
     Screener-Seiten (stockanalysis.com/screener, finviz.com u.ä.) plus
     Branchen-/Themen-Recherche nach neuen, plausiblen Kandidaten – orientiert
     an Sektor-/Regionslücken der aktuellen Watchlist (siehe "Offene Punkte"
     in `watchlist.md`, z.B. der noch leere Lateinamerika-Slot) und an
     Duplikations-/Strategie-Fit-Logik (Abschnitt 3). Läuft täglich mit
     Jarvis (Claude-Subagent) – dafür wird kein Browser gebraucht.
     **Kandidaten-Universum (2026-08-29, von Brian vorgegeben):** Die Suche
     rotiert systematisch durch die großen Welt-Indizes statt nur beliebig zu
     googeln, damit die Abdeckung breit UND nachvollziehbar bleibt – u.a.
     Russell 2000 (US Small/Mid-Cap, ergänzt bestehende Übergewichtung von
     US-Mega-Caps aus Champions), STOXX Europe 600 (breite europäische
     Abdeckung über die bereits vertretenen Einzelwerte wie ASML hinaus),
     S&P MidCap 400 (US-Mid-Cap-Ergänzung neben Russell 2000), Nikkei 225 /
     TOPIX (Japan, ergänzt die bereits guten Tokyo-Werte), MSCI Emerging
     Markets bzw. regionale Indizes für Lateinamerika/Asien-Schwellenländer
     (adressiert direkt den offenen Lateinamerika-Slot). Nicht jeden Tag der
     komplette Index auf einmal – rotierender Ausschnitt (z.B. ein Index bzw.
     ein Sektor-Ausschnitt eines Index pro Tag), damit der tägliche Scan
     schnell und stabil bleibt statt an einem Tag Tausende Werte prüfen zu
     müssen. Ergänzend weiterhin freie Themen-/Branchenrecherche (wie bisher
     beim Nicht-Index-Screening), aber die Index-Rotation ist ab jetzt das
     strukturierte Rückgrat der täglichen Suche.
  2. **Vorfilter:** Jeder gefundene Roh-Kandidat durchläuft sofort das
     Strategie-Fit-Gate und den Duplikations-Check gegenüber dem
     FTSE-All-World-ETF (Abschnitt 3) sowie das Identity-Gate (Ticker/ISIN/
     Börsenplatz/Land/Sektor). Kandidaten, die daran scheitern, werden
     verworfen und nicht erneut vorgeschlagen (kurze Sperrliste führen, damit
     nicht jeden Tag dieselben abgelehnten Namen erneut auftauchen).
     **Recheck-Termin statt Dauersperre (2026-09-03, aus dem
     3-KI-System-Audit, P2-Punkt Conans):** ein Ablehnungsgrund kann sich
     ändern (z.B. Duplikations-Check schlägt heute fehl, weil der ETF eine
     ähnliche Position hält, aber der ETF-Anteil verschiebt sich; oder das
     Strategie-Fit-Gate scheitert an einer aktuell unpassenden Kennzahl, die
     sich über Quartale verbessert). Jeder Sperrlisten-Eintrag bekommt daher
     ein Recheck-Datum (Standard: 90 Tage nach Ablehnung, bei eindeutig
     dauerhaften Gründen wie Delisting/Fraud/fehlender Börsenplatz auch
     länger oder unbegrenzt) – erst NACH diesem Datum wird der Kandidat
     wieder regulär geprüft, nicht bei jedem täglichen Scan sofort erneut.
     Vor Ablauf des Recheck-Datums bleibt er weiter stillschweigend
     ausgefiltert.
  3. **3-fach-Quick-Filter-Bestätigung (gemäß der 2026-08-29 von Brian
     bestätigten Regel "immer alle drei KIs, auch im Quick-Filter"):** Für
     jeden Kandidaten, der Schritt 2 übersteht, folgt ein TMR-Quick-Filter
     (bzw. Scout-Kurzform) mit Jarvis, Jack UND Conan. **Update
     2026-09-03 (Mechanismus veraltet, im 3-KI-System-Audit von Jack UND
     Conan unabhängig voneinander bemängelt):** Jack/Conan laufen seit
     2026-09-02 primär per **API-Bridge** (`gemini-bridge`/`openai-bridge`,
     siehe HANDOVER.md 10.9-10.11) – die vorherige Chrome-Browser-
     Abhängigkeit ("Laptop muss an und Chrome verbunden sein") ist damit
     nur noch ein **letzter Fallback**, falls BEIDE Bridges an einem Lauf
     ausfallen. Sind auch dann Jack/Conan nicht erreichbar, wird der
     Kandidat mit einem klar markierten Jarvis-Only-Vorabbefund konkret in
     die Datei `watchlist_pending_3fach.md` (Repo-Root, NICHT der
     veraltete Pfad `/root/aktien-agent/...`) eingetragen (feste
     Warteschlangen-Datei, Format dort dokumentiert) – kein automatisches
     Aufnehmen in die Watchlist nur auf Jarvis-Basis, das widerspräche der
     "immer alle drei"-Regel. **Automatischer Nachhol-Mechanismus
     (2026-08-29, von Brian gefordert, nachdem er fragte "wie behebt man das,
     wenn der Laptop aus war"; Auslöser seit 2026-09-03 auf Bridge-Ausfall
     statt Chrome-Ausfall umgestellt):** Jeder tägliche Trigger-Check prüft
     VOR dem eigentlichen Tages-Screening zuerst diese Datei (siehe
     "Täglicher Trigger-Check" Schritt 1) – liegen dort offene Einträge und
     sind die Bridges (bzw. als letzter Fallback Chrome) JETZT erreichbar,
     wird die fehlende Jack/Conan-Bestätigung sofort nachgeholt, der
     Kandidat entweder regulär in `watchlist.md` aufgenommen oder
     verworfen, und der Eintrag in den "Erledigt"-Bereich der
     Warteschlangen-Datei verschoben. Sind auch beim nächsten Lauf weder
     Bridges noch Chrome erreichbar, bleibt der Eintrag unverändert stehen
     und wird beim übernächsten Lauf erneut versucht – so wird kein
     zurückgestellter Kandidat stillschweigend vergessen. Da die Bridges
     serverseitig laufen (kein Laptop/Chrome-Zustand nötig), sollte dieser
     Fallback-Fall in der Praxis deutlich seltener eintreten als früher.
  4. **Automatische Aufnahme (2026-08-29, von Brian so entschieden):** Besteht
     ein Kandidat den vollen 3-fach-Quick-Filter UND Strategie-Fit-Gate UND
     Duplikations-Check, wird er OHNE Rückfrage direkt in `watchlist.md`
     aufgenommen (Kategorie automatisch nach der etablierten Champions/Profi/
     Talent-Logik zugeordnet) – Brian erfährt davon spätestens im
     Wochenfazit, nicht vorab. Die feste Obergrenze (max. 20-30 Werte) gilt
     weiter: ist die Liste voll, wird ein neuer Kandidat nur aufgenommen, wenn
     er klar überzeugender ist als der schwächste Wert seiner Zielkategorie
     (sonst zurückgestellt, nicht verworfen).
     **Triple-Conviction-Flag (2026-08-30, aus der Cross-KI-Diskussion in
     Agent-Playbook-Archiv-Diskussionen.md Abschnitt 10, von Brian freigegeben):** Stufen Jarvis, Jack und Conan
     unabhängig voneinander (keine Übernahme der Thesen untereinander) einen
     Kandidaten als außergewöhnlich ein – nicht nur als "kaufenswert" –, wird
     das explizit als **Triple-Conviction** im Watchlist-/Kauf-Eintrag
     markiert. Das ist kein Freibrief über die bestehenden Positions-/
     Kategorie-Grenzen hinaus, aber ein Signal für bevorzugte
     Kapitalallokation INNERHALB dieser Grenzen (siehe Conviction-Allocation,
     Abschnitt 3) – drei unabhängig zum selben Extrem-Urteil kommende
     Analysen sind ein stärkeres Signal als drei durchschnittlich positive.
  5. **Sofort-Eskalation bei "Sofort-Kauf"-Signal (2026-08-29, von Brian
     gefordert):** Ist ein neu gefundener Kandidat nicht nur watchlist-würdig,
     sondern zusätzlich ein Fall mit besonders günstiger Bewertung, sehr
     starkem Depot-Fit oder einem klaren, zeitkritischen Kaufsignal, wird
     NICHT bis zum Freitags-Wochenfazit gewartet – Brian bekommt sofort eine
     E-Mail/Push-Benachrichtigung (analog zur bestehenden Eskalationslogik
     des Täglichen Trigger-Checks), inkl. kurzer Begründung, warum es
     zeitkritisch erscheint. Das ist eine bewusste Ausnahme vom sonst üblichen
     "keine Zwischen-Benachrichtigungen"-Prinzip. **Begriffs-Klarstellung
     (2026-09-03, aus dem 3-KI-System-Audit, P2-Punkt Conans):** "Sofort-
     Kauf" bezeichnet ausschließlich die DRINGLICHKEIT der Benachrichtigung
     (sofort statt bis Freitag warten), NIEMALS eine automatische
     Order-Ausführung – die bleibt wie überall im System ausnahmslos
     Brians manuelle Entscheidung (siehe FIXE GRENZEN, Order-Tools). Jede
     Formulierung in Chat/E-Mail/PDF zu einem solchen Fund muss das
     erkennbar als Vorschlag/Zeitfenster-Hinweis rahmen, nicht als bereits
     erfolgte oder ausgelöste Handlung.
  6. **Aufwand/Realismus:** Screening (Schritt 1) läuft günstig und stabil
     täglich. Die 3-fach-Bestätigung (Schritt 3) ist der teurere Teil und
     bleibt auf die wenigen Kandidaten beschränkt, die den Vorfilter
     überstehen – nicht auf einen kompletten Marktscan mit 3-fachem Cross-
     Check täglich, das wäre nicht robust finanzierbar/stabil (siehe
     Abschnitt 6, "Warum nicht alles täglich voll automatisch?").
- **Automatisierte Portfolio-Lücken-Kandidatensuche-Pflicht (2026-09-04, von
  Brian gefordert: "die Agenten müssen automatisch agieren können, weil
  kein passender Kandidat in der Watchlist gefunden wird, dann müssen die
  Agenten automatisiert auf die Suche gehen, und nicht warten bis ich das
  erwähne").** Auslöser des Tages: bei der Depot-Talent-Neuzählung sank
  Talent auf 1/3 (2 freie Slots), Japan/Asien lag mit ~9% klar unter dem
  Zielband (10-15%), und Rorze (der einzige naheliegende Watchlist-
  Kandidat für diese spezifische Lücke) fiel nach vollem 3-fach-Scout-Check
  durch (siehe `analysen/RORZE-cross-check-fazit-2026-09-04.md`). Bis
  dahin wäre die Lücke einfach offen geblieben, bis Brian von sich aus
  nachfragt – genau das darf nicht mehr passieren.
  1. **Auslöser (jeder einzelne reicht):** (a) ein Kategorie-Slot ist offen
     (Ist < Ziel in der "10-7-3"-Struktur, siehe `depot/kategorisierung.md`),
     (b) der wöchentliche Portfolio-Regel-Check (Region/Sektor-Bänder,
     siehe oben) meldet einen unterbesetzten Topf, (c) ein zur Behebung
     einer solchen Lücke geprüfter Kandidat (egal ob aus der Watchlist oder
     neu gefunden) fällt nach vollem 3-fach-Check durch (KEIN Kauf, KEINE
     Sizing-Freigabe).
  2. **Pflicht-Reaktion, SOFORT im selben Lauf, nicht erst beim nächsten
     turnusmäßigen Scan-Slot:** eine GEZIELTE Kandidatensuche für genau
     diese Lücke anstoßen. **Klarstellung (2026-09-04, von Brian präzisiert:
     "ich meinte damit die ganzen Indizes durchforsten"):** "gezielt" heißt
     hier NICHT nur ein, zwei Kandidaten grob anschauen, sondern den bzw.
     die für die Lücke einschlägigen Index/Indizes aus dem
     "Kandidaten-Universum" oben (z.B. bei einer Japan/Asien-Lücke Nikkei
     225/TOPIX vollständig, nicht nur die tagesübliche Rotations-Scheibe;
     bei einer Sektor-Lücke die einschlägigen Branchen-Ausschnitte über
     mehrere Indizes hinweg) systematisch UND VOLLSTÄNDIG durchgehen, nicht
     nur einen kleinen täglichen Ausschnitt. Diese Vollständigkeits-Pflicht
     gilt NUR für den Lücken-Auslöser-Fall hier – die normale tägliche
     Index-Rotation (Schritt 1 oben) bleibt bewusst scheibenweise, damit sie
     günstig/stabil bleibt (siehe Aufwand/Realismus-Punkt oben). Ein
     Lücken-Lauf darf dafür mehrere Tage/mehrere aufeinanderfolgende
     Scheduled-Task-Läufe brauchen, um einen ganzen Index abzudecken, ohne
     dass das ein Fehlschlag ist – Fortschritt (welcher Index-Ausschnitt
     schon geprüft wurde) wird zwischen Läufen festgehalten (z.B. kurze
     Notiz in `depot/bridge_status.md` oder Commit-Message), damit nicht bei
     jedem Lauf wieder bei Null angefangen wird. Mehrere Kandidaten pro
     Lücke prüfen, nicht nach dem ersten Fehlschlag aufgeben. Jeder
     gefundene Kandidat durchläuft dieselben Gates wie beim normalen
     Kandidaten-Scan (Identity-/Strategie-Fit-/Duplikations-Gate, dann
     voller 3-fach-Check).
  2b. **Jack/Conan als zusätzliche, unabhängige Suchquelle (2026-09-07, von
     Brian gefordert: "die ganzen Indizes auf der ganzen Welt durchforsten,
     um interessante Kandidaten fürs Watchlist oder das Portfolio zu
     finden... alle 3 KI-Agenten sollen gegenseitig kontrollieren,
     miteinander diskutieren, verbessern, weil jeder die Stärken mit
     einbringen kann").** Bisher screente NUR Jarvis selbst (Jack/Conan
     bewerteten nur bereits von Jarvis vorgelegte Einzelkandidaten). Bei
     JEDEM Lücken-Auslöser (siehe Punkt 1 oben) zusätzlich zu Jarvis'
     eigenem systematischem Index-Durchlauf einen GEZIELTEN Such-Auftrag an
     Jack (`ask_gemini`) UND Conan (`ask_chatgpt`) schicken – NICHT den
     Einzelwert-Analyse-Prompt (keine Methodik-Dateien, keine Klarstellungs-
     Blöcke nötig, das ist hier kein Rating-Auftrag), sondern einen
     kompakten Rechercheauftrag: Index/Region/Sektor der Lücke benennen (z.B.
     "Nikkei 225, Talent-Kategorie, Kriterien: Marge/Marktstellung/
     Wachstumsverlässlichkeit aus dem Kategorisierungs-Kriterien-Abschnitt in
     `depot/master_status.md`"), eigene Live-Suche nutzen (`enable_search=True`
     bei beiden – hier KEIN langer Methodik-Prompt, also nicht das
     Gemini-Kontextlängen-Risiko aus HANDOVER.md 10.10), 3-5 plausible
     Kandidaten mit je 1-2 Sätzen Begründung nennen, KEIN vollständiges
     Rating (das ist nur ein Vorfilter). Jarvis sammelt die Vorschläge aus
     beiden Quellen (eigener Scan + Jack + Conan), dedupliziert gegen bereits
     geprüfte/gesperrte Kandidaten, und schickt ALLE neuen Namen durch
     dieselben Gates wie jeden anderen Kandidaten (Identity-/Strategie-Fit-/
     Duplikations-Gate, dann voller 3-fach-Check) – ein Jack- oder
     Conan-Vorschlag bekommt KEINEN Qualitäts-Bonus/-Rabatt nur weil er von
     einer der beiden KIs kam, er muss dieselbe Hürde nehmen wie jeder
     andere Kandidat. Zweck: echte zusätzliche Perspektive statt nur
     Jarvis' eigenem Screening-Blickwinkel – Jack/Conan könnten Kandidaten
     finden, die Jarvis' eigene Suchstrategie/Suchbegriffe übersieht.
  3. **Kein Qualitäts-Rabatt wegen Strukturbedarf:** ein struktureller
     Bedarf (offener Slot, unterbesetzter Topf) darf einen Kandidaten in
     der Vorauswahl positiv hervorheben (siehe bereits bestehende Regel
     oben, "Vorab-Check schon bei jeder Kurs-/Chancen-Vorauswahl"), aber
     NIE eine schwache Einzelthese überschreiben oder einen im 3-fach-Check
     durchgefallenen Kandidaten doch aufnehmen. Findet die gezielte Suche
     keinen echten Kandidaten: das explizit so benennen ("Lücke X geprüft,
     kein passender Kandidat gefunden trotz gezielter Suche, weiter
     beobachten") statt die Lücke stillschweigend fallen zu lassen – dieselbe
     Ehrlichkeits-Pflicht wie bei "kein Verstoß" im Portfolio-Regel-Check.
  3b. **Proaktive Suche ist keine Kaufpflicht – Watchlist-Aufnahme ≠
     Depot-Kauf (2026-09-08, Brian nach einem Vergleich mit Raketentonis
     Prinzip "kein Zwang, freie Plätze sofort zu besetzen" – bei uns
     angepasst, weil wir bewusst AKTIV suchen, siehe Punkt 1-2b oben,
     Brian: "die Werte die wir suchen kommen ja trotzdem erstmal auf die
     Watchlist, danach wird trotzdem sondiert welche Werte es wirklich ins
     Portfolio schaffen").** Die Pflicht zur aktiven Suche (Punkt 1-2b oben)
     bleibt unverändert – KEIN Widerspruch dazu. Aber: ein gefundener,
     erfolgreich durch den 3-fach-Check gelaufener Kandidat landet zunächst
     NUR in `watchlist.md`, nicht automatisch im Depot. Eine offene
     Kategorie-/Regionen-Lücke erzeugt KEINEN Zeitdruck, einen
     Watchlist-Kandidaten zeitnah tatsächlich zu kaufen – das bleibt
     Brians eigene, in Ruhe getroffene manuelle Entscheidung, unabhängig
     davon, wie lange ein Slot schon offen ist. Die Suchpflicht sorgt dafür,
     dass IMMER geeignete Kandidaten bereitstehen, wenn Brian kaufen
     möchte – sie ist keine Kauf-Empfehlung mit Dringlichkeit. Sizing-/
     Kauf-Empfehlungen bleiben an die üblichen Kriterien gebunden (CRV-Ampel,
     eigene Einstiegsüberlegung Brians), nicht an die Slot-Lücke selbst.
  4. **Kein Dauerlauf ohne Ende:** eine erfolglose gezielte Suche muss nicht
     bei jedem einzelnen Lauf wiederholt werden (das wäre reine
     Rechenverschwendung ohne neue Information) – sie wird erneut
     ausgelöst, sobald sich die Datenlage ändert (neuer Kandidat aus dem
     normalen täglichen Scan taucht in der betroffenen Region/Sektor auf,
     ein bereits abgelehnter Kandidat erreicht sein Recheck-Datum, oder der
     nächste Wochenfazit-Lauf bestätigt die Lücke erneut) – dann aber
     wieder ohne dass Brian es erst ansprechen muss.
  5. **Benachrichtigung:** ein gefundener, bestätigter Kandidat läuft durch
     die normale Eskalationslogik (automatische Watchlist-Aufnahme, siehe
     oben). Eine erfolglose gezielte Suche braucht KEINE Sofort-
     Benachrichtigung (kein handlungsrelevanter Fund), wird aber im
     nächsten Wochenfazit als "geprüft, noch offen" kurz erwähnt statt
     kommentarlos zu verschwinden.
- **Tieferer Zweck der ständigen Suche – Watchlist-Bereicherung UND
  Qualitäts-Benchmark, nicht nur Lücken-Füllung (2026-09-04, von Brian
  präzisiert: "der Grund warum ich die Agenten ständig auf die Suche
  schicke möchte, ist eventuell sogar tiefer als du denkst").** Brians
  drei ausdrücklich genannte Gründe, warum der tägliche/gezielte
  Kandidaten-Scan wichtiger ist als reine Lücken-Reparatur:
  1. Die Suche soll die Watchlist grundsätzlich BEREICHERN – neue,
     interessante Kandidaten sind für sich genommen wertvoll, nicht nur als
     Mittel zum Zweck einer offenen Kategorie-/Region-/Sektor-Lücke.
  2. Die Suche soll gezielt Werte finden, die **unterm Radar der meisten
     Anleger laufen** – nicht nur die immer gleichen bekannten Mega-Caps
     eines Index. Bei der Index-Durchsuchung (siehe oben) bewusst NICHT nur
     bei den größten/bekanntesten Marktkap-Werten hängen bleiben, sondern
     gezielt auch kleinere, weniger analystenabgedeckte Titel innerhalb des
     jeweiligen Index prüfen (z.B. niedrige Analysten-Coverage, geringe
     institutionelle Eigentümerquote, oder schlicht Namen, die in der
     Finanzpresse selten auftauchen) – solange sie die üblichen
     Qualitätskriterien (Marge/Marktstellung/Wachstumsverlässlichkeit)
     erfüllen. "Unbekannt" ist kein Qualitätsmerkmal für sich, aber ein
     bewusstes Gegengewicht gegen den natürlichen Bias, immer nur die
     ohnehin schon bekannten Namen zu finden.
  3. Die Suche soll aktiv prüfen, ob ein neuer Fund SOGAR BESSER ist als
     bereits vorhandene Watchlist-Kandidaten – nicht nur "besteht er die
     Mindestkriterien", sondern ein echter Qualitäts-Vergleich.
  **Watchlist-interner Qualitäts-Vergleich (neue, eigenständige Praxis,
  analog zum bestehenden "Head-to-Head-Ersatz-Gate gegen die schwächste
  Depot-Position", siehe Abschnitt 3 – hier aber Watchlist-intern, nicht
  Depot-Ersatz-getrieben):** JEDER neue Kandidat, der das Vorfilter-Gate
  (Identity/Strategie-Fit/Duplikation) und den 3-fach-Quick-Filter besteht,
  wird zusätzlich – unabhängig davon, ob die Watchlist bereits voll ist
  oder nicht – kurz gegen die bestehenden Watchlist-Werte SEINER
  Zielkategorie (Champions/Profi/Talent) UND, wo sinnvoll, seiner
  Region/seines Sektors verglichen ("schnelle Gegenüberstellung", kein
  komplett neuer 3-fach-Check für die Vergleichswerte nötig – die
  bestehende Kurzthese/CRV/Rating aus `watchlist.md` reicht als
  Vergleichsbasis). Ergebnis-Fälle:
  - Neuer Kandidat ist klar überzeugender als der schwächste bestehende
    Wert seiner Kategorie → das wird EXPLIZIT im Aufnahme-Eintrag vermerkt
    ("möglicher Qualitäts-Upgrade ggü. [bestehender Wert]") und im
    Wochenfazit hervorgehoben – auch wenn noch freie Slots vorhanden sind
    und daher kein Zwang besteht, etwas zu ersetzen. Das ist eine
    Diskussionsgrundlage für Brian, keine automatische Ersetzung – die
    Watchlist verliert dadurch nicht automatisch den schwächeren Wert.
  - Neuer Kandidat ist grundsätzlich watchlist-würdig, aber nicht klar
    stärker als vorhandene Vergleichswerte → normale Aufnahme ohne
    besonderen Vermerk.
  - Die Watchlist-Obergrenze (20-30) ist bereits erreicht → hier greift
    weiterhin zusätzlich die bestehende Regel oben ("nur aufnehmen, wenn
    klar überzeugender als der schwächste Wert der Zielkategorie") als
    hartes Aufnahme-Kriterium, nicht nur als Vermerk.
- **Ad-hoc-Einzelwert-Check auf Zuruf (2026-08-30, von Brian gefordert):**
  Zusätzlich zum systematischen täglichen Scan oben kann Brian jederzeit
  einen konkreten, selbst benannten Wert einreichen (eigene Idee oder z.B.
  ein Tipp von einem Kumpel: "kannst du XYZ analysieren, ob das für unser
  Portfolio passt") – dieser durchläuft automatisiert dieselbe Gate-Logik wie
  ein selbst gefundener Scan-Kandidat, nur ausgelöst per Zuruf statt per
  Entdeckung:
  1. Identity-Gate (Ticker/ISIN/Börsenplatz/Land/Sektor verifizieren).
  2. Strategie-Fit-Gate + Duplikations-Check ggü. FTSE-All-World-ETF
     (Abschnitt 3).
  3. Sektor-/Regionen-Vorab-Check inkl. anteiliger Mehrsegment-Zuordnung, wo
     zutreffend (siehe Sektor-Streuung, Beispiel Hoya Corp.).
  4. Voller 3-fach-Check (Jarvis/Jack/Conan, TMR-Quick-Filter bzw. Scout) –
     bei fehlendem Chrome-Zugriff greift dieselbe Warteschlangen-Logik wie
     beim täglichen Scan (`watchlist_pending_3fach.md`).
  5. Besteht der Kandidat alle Gates: automatische Aufnahme in `watchlist.md`
     in der passenden Kategorie, Herkunft als "Ad-hoc (Brian/Zuruf,
     Datum)" vermerkt. Besteht er eines der Gates nicht: KEINE Aufnahme,
     keine eigene Ablehnungs-Historie nötig – kurze Begründung reicht im
     Chat.
  **Kein eigenes PDF für diesen Check** – das Ergebnis wird direkt im Chat
  mitgeteilt und ausschließlich über die Watchlist-Datei selbst festgehalten
  (Aufnahme oder eben nicht). Eine bei diesem Weg neu aufgenommene Position
  taucht dann ganz normal wie jede andere Watchlist-Änderung im nächsten
  Wochenfazit unter "neu rein" auf – dafür wird kein separater
  Analyse-Report erstellt.
- **Auf-/Abstiegs-Kriterien:** siehe die entsprechenden Abschnitte in
  `watchlist.md` selbst (Aufnahme-Kriterien / Ausschluss-Kriterien) – dort
  gepflegt statt hier dupliziert, damit es nur eine Quelle der Wahrheit gibt.
- **Erscheint im Wochenfazit:** Jedes Wochenfazit bekommt einen eigenen
  Watchlist-Abschnitt mit der KOMPLETTEN Watchlist zum aktuellen Stand
  (Champions/Profi/Talent, alle Werte) sowie einer Zusammenfassung ALLER
  Änderungen der ganzen Woche (aggregiert aus den täglichen Scans, nicht nur
  ein Freitags-Schnappschuss): welche Werte diese Woche neu aufgenommen
  wurden (mit 1-2 Sätzen Begründung je Wert) und welche rausgeflogen sind
  (mit Grund). Bleibt die Watchlist in einer Woche unverändert, wird das kurz
  explizit vermerkt ("keine Veränderung diese Woche"), kein Ausfall.
- **Erstbefüllung (2026-08-28):** 21 Werte von Brian direkt vorgegeben
  (u.a. Nvidia, Visa, S&P Global, Stryker, Keyence, CrowdStrike, Palantir,
  Arista Networks – teils bewusst ehemalige, im Zuge der Restrukturierung
  verkaufte Depot-Positionen, die er weiter im Blick behalten will), plus
  8 von Jarvis systematisch ergänzte Qualitäts-Compounder (u.a. ASML, TSMC,
  Mastercard, Fortinet, Fair Isaac, Copart, Watsco, Rollins), um alle drei
  Kategorien sauber zu füllen und die Liste sektoral/geografisch breiter
  aufzustellen. Endstand: 29 Werte (Champions 13 / Profi 9 / Talent 7).
  Lateinamerika/Sonstige-Schwellenländer-Slot bewusst noch leer gelassen
  (siehe Offene Punkte in `watchlist.md`) – kein überzeugender Kandidat aus
  dem parallel laufenden Nicht-Index-Screening (siehe
  `analysen/nicht-index-screening-konsolidiert-2026-08-28.md`) erfüllt beide
  Kriterien (Qualität + echte Lateinamerika-Zuordnung) gleichzeitig.

### Täglicher Trigger-Check (2026-08-26, von Brian gefordert)

Ergänzend zum Wochenfazit (das immer kommt, egal was passiert ist) gibt es
seit 2026-08-26 einen täglichen, schlanken Scheduled Task (19:00 Uhr UTC ≈
21:00 Uhr Europe/Berlin), der NICHT jeden Tag alle Positionen voll neu
analysiert (zu teuer/instabil, siehe Session-Limit-Vorfall vom 24./25.08.),
sondern:

1. täglich einen schnellen News-/Kurs-Scan über das gesamte Depot fährt,
2. gegen die in den `analysen/`-Dateien dokumentierten Abstauber-Limits,
   Upgrade-/Downgrade-Trigger und Stop-These-Trigger prüft,
3. NUR bei echtem Anlass (Limit gerissen, Trigger ausgelöst, marktbewegende
   News) den vollen 3-fach-Cross-Check inkl. Diskussionsrunde [3b] für die
   betroffene(n) Position(en) anstößt,
4. bei einem echten, handlungsrelevanten Ergebnis Brian sofort per E-Mail/
   Push benachrichtigt ("um handlungsfähig zu bleiben" – Brians Formulierung),
5. an ruhigen Tagen ohne Anlass nur einen unauffälligen Ein-Zeiler abschließt,
   damit keine unnötigen Benachrichtigungen entstehen.

Technische Einschränkung, Stand 2026-09-02 (historisch relevant, aktuell
entschärft): Früher benötigten die Browser-Automation-Beine (ChatGPT/Conan,
Gemini/Jack) Zugriff auf Brians verbundenen Chrome-Browser, der in einem
unbeaufsichtigt laufenden Scheduled Task nicht garantiert verfügbar war
(z.B. wenn Brians Desktop-App gerade nicht offen war) – der Trigger-Check
lieferte dann nur die Jarvis-Einzelmeinung. Seit 2026-09-02 laufen sowohl
ChatGPT/Conan (`openai-bridge`-MCP-Server, Modell `gpt-5.5`) als auch
Gemini/Jack (`gemini-bridge`-MCP-Server, Modell `gemini-2.5-flash`) über
direkten API-Call statt Browser-Automation (siehe HANDOVER.md Abschnitt
10.9/10.10) – **beide sind damit von Chrome/Desktop-App-Verfügbarkeit
unabhängig.** Ein unbeaufsichtigt laufender Scheduled Task kann dadurch
jetzt regulär den vollen 3-fach-Check (Jarvis + Jack + Conan) fahren, auch
wenn Brians Desktop-App gerade nicht offen ist. Chrome-Browser-Automation
bleibt als Fallback dokumentiert (falls eine der beiden Bridges mal
ausfällt, siehe HANDOVER.md 10.4), ist aber nicht mehr der Standardweg.
**Depot-Transaktions-Erkennung (2026-09-02, von Brian gefordert):** Dritter,
eigenständiger Auslöser-Typ neben Kurs-/News-Anlass und Earnings-Terminen –
der Trigger-Check erkennt jetzt auch tatsächlich AUSGEFÜHRTE Transaktionen
bei Scalable Capital (`list_portfolio_transactions`, gefiltert per `fromTime`
gegen einen Checkpoint in `depot/last_transaction_check.md`) und stößt dafür
automatisch den vollen 3-fach-Cross-Check an – unabhängig davon, ob ein
Kurs-/News-Trigger vorliegt. Jeder von Brian ausgeführte Kauf/Verkauf wird so
automatisch allen drei KIs zur Einordnung vorgelegt ("These nach Nachkauf
noch intakt?" bzw. "war der Verkauf folgerichtig?"), nicht nur system-eigene
Empfehlungen. Gilt NUR für Scalable Capital (einzige Live-Transaktionsquelle)
– die drei manuellen Broker haben keine API, dort bleibt Brians eigene
Meldung per `depot/*.md`-Update der einzige Weg. Details zum Ablauf:
`~/.claude/scheduled-tasks/taeglicher-trigger-check/SKILL.md`.

**Tägliches Depot-Kuchendiagramm (2026-09-02, von Brian gefordert – "ohne
dass ich jedes Mal ansprechen muss"):** Der Trigger-Check aktualisiert als
Teil des Depot-Scans (Schritt 2) automatisch `reports/portfolio_pie.py` mit
den frisch gesammelten Werten (Scalable live + `depot/*.md`, inkl. Cash und
Gold-ETC) und rendert ein neues `reports/portfolio_pie_<Datum>.png` – ohne
dass Brian danach fragen muss, jeden Tag. Kein eigener Benachrichtigungs-
Anlass dafür, das PNG wird einfach mitcommittet.

"Ständig im Hintergrund im Austausch" (Brians ursprüngliche Formulierung) ist
im Kern als täglicher anlassbezogener Check umgesetzt – für echte Kurzfrist-
Lücken (z.B. 1-2 Stunden Abwesenheit) siehe den separaten "Blitz-Scan" direkt
unten, der das teilweise abfedert. Kein echtes Sekunden-Echtzeit-Polling: ein
voller 3-fach-Check mehrmals stündlich für ALLE Positionen wäre nicht robust
finanzierbar/stabil – deshalb bleibt der Blitz-Scan bewusst auf einen schnellen,
browserlosen Jarvis-Only-Scan beschränkt, der nur bei echtem Treffer eskaliert.

### Earnings-Season-Automatisierung (2026-09-01, von Brian gefordert — setzt den bisher zurückgestellten "Earnings-/Corporate-Action-Kalender" aus Agent-Playbook-Archiv-Diskussionen.md Abschnitt 9, Phase 4, um)

**Auslöser:** Brian möchte, dass für jeden Depot- ODER Watchlist-Wert, der
Quartalszahlen veröffentlicht, automatisch und systematisch eine kompakte
Zahlen-Zusammenfassung vorgelegt wird — nicht erst auf Nachfrage. Als
Stil-Inspiration hat er eine fremde NVIDIA-Earnings-Zusammenfassung
(Raketentonis Jack-Persona) geteilt. Wie bei jeder bisherigen fremden
Vorlage (Couche-Tard-PDF, Wochenreport-Vorbild, HawkEye-Szenarien-PDF)
gilt: **lose stilistische Inspiration, kein 1:1-Klon.** Übernommen wird die
Grundidee (Kernzahlen vs. Erwartung, Segment-Treiber, Guidance, kurzer
Risiko-Gegenpol, klare Schlusslinie) und der direkte, verständliche
Erzählstil (siehe "Verständlichkeit der Kurz-Fazits", oben). NICHT
übernommen: erfundene Konsens-Zahlen ohne Quelle, eine neue eigenständige
Rating-Skala (Raketentonis "🟢🔥🔥🔥") — Ampel-Farben und Rating-Begriffe
bleiben unser etabliertes Agent-/TMR-/Scout-Vokabular.

**Technische Einschränkung:** Twelve Data führt `get_earnings` (Termine UND
historische EPS-Daten) nur ab "grow"-Plan aufwärts — auf dem aktuellen Plan
gesperrt (gleiche Einschränkung wie `get_financials`, siehe HANDOVER.md
Abschnitt 10.6). Earnings-Termine werden deshalb wie andere
Fundamentaldaten per WebSearch/WebFetch recherchiert (IR-Seiten,
Finanzportale), nicht über eine API abgefragt.

**Ablauf:**

1. **Wöchentliche Terminaktualisierung** (Teil des Wochenfazit-Laufs):
   für jeden Depot- UND Watchlist-Wert den nächsten erwarteten
   Earnings-Termin per WebSearch prüfen und in einer neuen Datei
   `depot/earnings_calendar.md` festhalten (Ticker, Firma, erwarteter
   Termin, Quelle/Datum der Recherche, Status "bestätigt"/"geschätzt").
   Kein täglicher Vollabruf über alle ~45 Werte nötig — die Termine
   ändern sich selten kurzfristig.
2. **Tägliche Fälligkeitsprüfung** (Teil des Täglichen Trigger-Checks,
   Schritt 2 oben): `earnings_calendar.md` gegen das heutige Datum prüfen.
   Steht ein Termin heute an oder ist er in den letzten 24h fällig
   geworden, gezielt per WebSearch/WebFetch prüfen, ob der Bericht bereits
   veröffentlicht wurde.
3. **Bei tatsächlicher Veröffentlichung: Earnings-Kompakt-Fazit erstellen**
   (Jarvis-Only reicht hier, kein 3-fach-Cross-Check nötig — das ist reine
   Zahlen-Berichterstattung, keine Bewertungsfrage):
   ```
   📊 Earnings-Kompakt: [TICKER] – [Quartal/Jahr]

   [1-2 Sätze Kurzfazit im Verständlichkeits-Duktus: was heißt das
   konkret für Brians Position/Watchlist-Beobachtung]

   Kernzahlen (Ist vs. Erwartung, EUR-Gegenwert bei USD-Werten):
   - Umsatz: X Mio./Mrd. [Währung] (Erwartung: Y) → +/-Z% YoY, +/-W% QoQ
   - [wichtigstes Segment, falls fundamental relevant für die These]:
     X → +/-Z% YoY
   - EPS (GAAP/Non-GAAP): X (Erwartung: Y)
   - Bruttomarge / Nettogewinn / Op. Income, falls aussagekräftig

   Guidance nächstes Quartal: X (Konsens-Erwartung falls verfügbar: Y)

   Kurzer Risiko-/Bewertungs-Gegenpol (Pflicht, kein reiner Jubel-Text):
   [1-2 Sätze — was relativiert die Zahlen, z.B. Bewertung bereits hoch,
   Guidance nur in Line statt Beat, Sondereffekt in der Marge]

   Trigger-Check: [löst dieses Ergebnis eines der hinterlegten Upgrade-/
   Downgrade-Trigger bzw. These-Bruch-Kriterien aus? Ja/Nein + welches]

   Status: 🟢/🟡/🔴 [kurzfristig], ggf. getrennt mittelfristig, falls
   auseinanderfallend (unser Ampel-Vokabular, siehe etablierte Skalen)
   ```
4. **Trigger-Eskalation:** Löst das Ergebnis einen hinterlegten Upgrade-/
   Downgrade-Trigger oder ein These-Bruch-Kriterium aus (siehe
   "Verkaufsdisziplin & Gewinnmitnahme-Regeln", Investment-These-Protokoll),
   wird — wie bei jedem echten Anlass — der volle 3-fach-Cross-Check
   angestoßen (Terminal-State-Mechanismus aus Abschnitt 14 gilt dabei
   unverändert). Löst es keinen Trigger aus, bleibt es bei diesem
   kompakten Fazit — kein PDF nötig, Chat-Nachricht reicht, plus
   PushNotification bei Depot-Positionen (Watchlist-Werte ohne bestehende
   Position lösen keine PushNotification aus, erscheinen aber im nächsten
   Wochenfazit unter Watchlist-Update).
5. **Bündelung bei mehreren Terminen am selben Tag:** meldet mehr als ein
   Wert am selben Tag Zahlen, werden die Kompakt-Fazits gesammelt in EINER
   Chat-Nachricht/PushNotification zusammengefasst statt mehrerer
   Einzel-Unterbrechungen (Notification-Ermüdung vermeiden, siehe
   PushNotification-Regeln oben).

**Abgrenzung zu bestehenden Formaten:** Ersetzt NICHT die volle
Fundamentalanalyse (TMR/Scout) — ein Earnings-Kompakt-Fazit ist reine,
schnelle Zahlen-Einordnung, keine neue DNA-Check-/Agent-Score-Bewertung.
Länger etablierte Positionen mit bereits hinterlegten Triggern profitieren
am meisten (die Zahlen werden direkt gegen die eigene Beobachtungsbasis
gehalten, nicht isoliert kommentiert).

**Status: von Brian am 2026-09-01 angefordert und damit die bisher
zurückgestellte Phase 4 (Agent-Playbook-Archiv-Diskussionen.md Abschnitt 9, "Earnings-/Corporate-Action-
Kalender") in diesem Teilaspekt freigegeben und umgesetzt.**

### Blitz-Scan (2026-08-30, von Brian gefordert)

Brians konkreter Anlass: er ist zwischendurch 1-2 Stunden weg (Einkaufen,
Hund ausführen) und wollte wissen, wie er auch dann zeitnah informiert wird,
statt erst beim nächsten planmäßigen Check um 19:00 Uhr. Lösung: ein
zusätzlicher, sehr schlanker Scheduled Task, der **stündlich während der
Handelszeiten** läuft (Cron `0 7-21 * * 1-5`, UTC, Mo-Fr ≈ 09:00-23:00 Uhr
Europe/Berlin im Sommer / 08:00-22:00 Uhr im Winter – die feste UTC-Spanne
deckt beide Zeitzonen-Fälle ausreichend ab, keine Umstellung nötig) – bewusst
NICHT rund um die Uhr, da an Wochenenden/nachts an den Kursen ohnehin nichts
Relevantes passiert (Brians eigene Entscheidung gegen 24/7 aus Kostengründen).

Der Blitz-Scan ist ausdrücklich KEIN Ersatz für den täglichen 19-Uhr-Trigger-
Check oder das Wochenfazit, sondern eine schnelle Zwischen-Absicherung:

1. Kurzer WebSearch-Scan (kein Browser, kein voller Agent-Playbook.md-Reread
   nötig) über alle Depot- UND Watchlist-Werte, aber NUR auf akute Treffer
   der letzten Stunde: Kurssprung >5% seit letztem Schlusskurs/letztem
   Blitz-Scan, Earnings-Überraschung, Gewinnwarnung, M&A-Meldung, Regulatorik-/
   Rechtsstreit-Schock, Management-Rücktritt, Fraud-Vorwurf, Delisting, oder
   ein dokumentiertes Abstauber-/Stop-These-/Upgrade-Downgrade-Limit, das
   gerade gerissen wurde. KEIN täglicher automatisierter Kandidaten-Scan
   (neue Werte suchen) an dieser Stelle – das bleibt dem 19-Uhr-Trigger
   vorbehalten, ein stündlicher Vollmarkt-Scan wäre nicht finanzierbar.
2. Nur bei einem wirklich akuten Treffer (nicht bei gewöhnlicher Tages-
   volatilität ohne klaren Auslöser): sofortige, kurze Chat-Nachricht + Push/
   E-Mail. Ist Brians Chrome-Browser in diesem Moment zufällig verbunden
   (z.B. weil der Rechner nur gesperrt, nicht ausgeschaltet ist), wird direkt
   der volle 3-fach-Cross-Check versucht wie im 19-Uhr-Trigger; ist der
   Browser nicht verbunden, liefert der Blitz-Scan eine klar markierte
   vorläufige Jarvis-Only-Einschätzung mit dem Hinweis "volle 3-fach-
   Bestätigung folgt automatisch beim nächsten Blitz-Scan mit Browser-Zugriff
   oder spätestens beim 19-Uhr-Check" – der reguläre 19-Uhr-Trigger deckt
   dasselbe Ereignis über seinen eigenen 24-48h-Scan ohnehin erneut ab, ein
   gesonderter Warteschlangen-Eintrag ist dafür nicht nötig (anders als beim
   täglichen Kandidaten-Scan, wo neue Kandidaten sonst verlorengingen).
3. Ohne akuten Treffer: keine Nachricht, keine PDF, kein Log – bewusst
   still, damit an ruhigen Stunden keine unnötigen Benachrichtigungen
   entstehen (gleiches Prinzip wie beim täglichen Trigger-Check).

**On-Demand-Trigger (2026-09-08, von Brian gefordert: automatisierte
Analyse-Auslösung ohne Chat-Session, "wenn ich eine Aktie in die Analyse
schicken möchte").** Ergänzung zum bisherigen reaktiven Scan, im selben
stündlichen Blitz-Scan-Job (kein neuer Job — dieselbe Begründung wie beim
"kein neuer Master-Agent-Hermes-Job"-Punkt oben: die 3-fach-Cross-Check-
Infrastruktur ist hier schon vorhanden, ein zweiter, paralleler Job hätte
sie nur dupliziert). Zwei Auslöse-Wege, beide von Brian ausdrücklich
gewünscht ("beides"):

- **Watchlist-Trigger:** Ticker direkt in der Scalable-Capital-App zur
  Watchlist hinzufügen (2 Taps am Handy). `list_watchlist_items` gegen
  `watchlist.md` abgeglichen — jeder Eintrag, der in Scalable, aber noch
  nicht in `watchlist.md` steht, ist ein neuer Auftrag. Ergänzt den
  bestehenden umgekehrten Spiegel-Mechanismus (watchlist.md → Scalable)
  aus `taeglicher-trigger-check`, ohne ihn zu ersetzen.
- **E-Mail-Trigger:** E-Mail an `brianqtng@outlook.de` mit Betreff
  `Analysiere: <Ticker/Firmenname>` (Standardtiefe Quick Filter) oder
  `Deep-Dive: <Ticker/Firmenname>` (erzwingt Full Deep Dive). Gmail-
  `search_threads` nach ungelesenen Treffern, Ticker aus dem Betreff
  extrahiert, verarbeitete Mail wird gelabelt (nicht gelöscht), um
  Doppel-Verarbeitung zu verhindern.

Beide Wege münden in denselben vollen 3-fach-Cross-Check wie ein regulärer
akuter Treffer (TMR-/Scout-Routing über die bestehende Bucket-/Fallback-
Regel, TA-Pflicht, PDF-Pflicht, Prediction-Ledger bei Kauf-Empfehlung,
Aufnahme in `watchlist.md` bei bestandenem Ergebnis oder dokumentierter
Ablehnungs-Vermerk bei Abbruch — verhindert wiederholtes Neu-Triggern
desselben abgelehnten Tickers). Sicherheitsgrenze unverändert: ausschließ-
lich read-only Analyse, keine Order/Watchlist-Löschung/Kontoänderung.
Vollständig in `~/.claude/scheduled-tasks/blitz-scan/SKILL.md` (Abschnitt
"On-Demand-Trigger" + neuer Ablauf-Schritt 0) umgesetzt.

**Weg C ergänzt (2026-09-08): Rücksync watchlist.md → Scalable.** Fund
desselben Tages: als Brian vier Werte (Ligand/UCB/Itochu/Qnity) direkt im
Chat in `watchlist.md` aufnehmen ließ, blieb die Scalable-App-Watchlist
unsynchronisiert — der bestehende Spiegel-Mechanismus lief bisher nur als
Nebeneffekt des täglichen Kandidaten-Scans (`taeglicher-trigger-check`),
nicht bei Chat-Session-Aufnahmen. Lösung: `blitz-scan` gleicht jetzt bei
JEDEM stündlichen Lauf zusätzlich alle `watchlist.md`-Einträge gegen
Scalable ab und trägt Fehlende per `add_watchlist_item` nach — reine
Synchronisation ohne Cross-Check-Trigger (der Wert ist in `watchlist.md`
bereits bewertet). Damit ist der Watchlist-Scalable-Abgleich jetzt in
BEIDE Richtungen automatisiert, unabhängig davon, wo ein Wert zuerst
auftaucht (App, Chat-Session oder automatisierter Scan).

## 6. Warum nicht alles täglich voll automatisch?

Ehrliche Einschränkung, mit Brian abgestimmt: Schritt 1 (quantitatives Screening)
kann automatisiert/geplant laufen. Schritt 3+4 (3-facher KI-Cross-Check über
ChatGPT/Gemini/Claude) braucht Browser-Zugriff auf die Web-Oberflächen dieser
Anbieter, da keine API-Keys vorhanden sind — das funktioniert nur, wenn Brians
Mac/Chrome verbunden ist, nicht als stille Cloud-Automatisierung über Nacht. Realistischer
Rhythmus: täglicher Watchlist-Recheck (schnell, wenige Kandidaten) + wöchentlicher
breiter Scan nach neuen Kandidaten (aufwändiger).

## 7. Technische Bausteine (Entwurf, wird in den nächsten Schritten gebaut)

**Wichtige technische Korrektur (2026-08-22):** Die Cloud-Umgebung, in der dieses
Projekt läuft, hat keinen allgemeinen Internetzugriff (kein `pip install yfinance`,
kein direkter API-Zugriff auf z.B. Yahoo Finance) – nur die eingebauten Web-Tools
(WebFetch/WebSearch) können das offene Web erreichen, und die laufen über einen
separaten, kontrollierten Kanal. Ein klassisches "Python-Skript zieht Bulk-Marktdaten
via yfinance"-Vorgehen funktioniert hier also nicht. Stattdessen:

- **Screener-Schritt läuft über WebFetch/WebSearch** gegen öffentliche Screener-Seiten
  (z.B. stockanalysis.com/screener, finviz.com) mit den gewünschten Filterkriterien –
  die Filterung passiert serverseitig auf der Screener-Seite, hier wird nur die
  bereits gefilterte Kandidatenliste abgerufen. Kein eigener Datenpipeline-Aufbau nötig.
- Das passt tatsächlich gut zum Charakter der drei Prompts selbst: TMR/Scout/TA sind
  ohnehin als Web-Search-getriebene Analysen konzipiert (SCHRITT 0 in TMR z.B. verlangt
  explizit Live-Web-Search für den Kurs), nicht als Konsumenten einer Bulk-Datenbank.
- **Prompt-Runner** (aktuell umgesetzt als Subagent pro Analyse-Lauf): nimmt Kandidat
  + Prompt-Typ (TMR/Scout/TA), lässt den kompletten Prompt inkl. Live-Web-Search
  laufen, schreibt das volle Ergebnis in eine Datei unter `analysen/` und liefert
  ein Kurz-Fazit zurück (siehe Pipeline-Schritt 5). Läuft für Claude als Subagent;
  seit 2026-09-02 laufen ChatGPT/Conan (`openai-bridge`-MCP-Server, `ask_chatgpt`,
  Modell `gpt-5.5`) UND Gemini/Jack (`gemini-bridge`-MCP-Server, `ask_gemini`,
  Modell `gemini-2.5-flash`) beide per direktem API-Call statt Browser-
  Automation (siehe HANDOVER.md Abschnitt 10.9/10.10); der komplette
  Methodik-Prompt/das Fact-Pack wandert dabei 1:1 als `prompt`-Argument rein,
  kein Browser-Tab mehr nötig. Alt (Fallback, falls eine Bridge mal ausfällt):
  Browser-Automation per `document.execCommand('insertText', ...)` in das
  jeweilige Eingabefeld.
  **Wichtige Lehre (2026-08-23, ServiceNow-Testlauf, betraf den damaligen
  Gemini-Browser-Betrieb, seit dem Umstieg auf `gemini-bridge` nicht mehr
  relevant, aber als Fallback-Wissen aufbewahrt):**
  Bei Gemini wurde der Text beim Absenden mehrfach nach dem ersten Absatz
  abgeschnitten, sobald die Nachricht mehrere durch Leerzeilen getrennte Absätze
  enthielt (Zeilenumbrüche scheinen den Sende-Vorgang vorzeitig auszulösen) –
  ChatGPT hatte dieses Problem auch im damaligen Browser-Betrieb nicht, ist aber
  ohnehin seit dem Umstieg auf die API nicht mehr relevant. Fix bei Gemini:
  den kompletten Prompt als EINEN durchgehenden Fließtext ohne interne
  Absätze/Zeilenumbrüche einfügen, dann erst senden.
- **Vergleichs-/Diskrepanz-Modul**: extrahiert die Kernfelder aus allen drei
  Antworten, markiert Übereinstimmung/Abweichung, und fährt danach die
  Diskussionsrunde [3b] (jede KI bekommt die beiden anderen Urteile vorgelegt und
  nimmt Stellung), bevor das Konvergenz-Ergebnis ins Kurz-Fazit geht. Erstmals
  end-to-end durchgespielt am 2026-08-22 für CLBT (Claude/Jarvis vs. ChatGPT/Conan
  vs. Gemini/Jack) – dabei aber nur Runde 1 (unabhängige Einzelurteile), die
  Diskussionsrunde [3b] selbst ist technisch noch nicht gebaut (offener Punkt).
- **Wochenfazit-Job**: eigener wöchentlicher Scheduled Task (freitags 22:00 Uhr
  Europe/Berlin, siehe Abschnitt 5), fasst Depotstatus + Kategorie-Status +
  Auffälligkeiten der Woche im Wochenfazit-Format zusammen und schickt es proaktiv
  an Brian.
- **Depot-Reader**: liest Trade-Republic-/Scalable-Capital-Depotstand read-only aus
  (Browser-Automation, mit Brians Mithilfe bei 2FA). Noch nicht gebaut – aktuell
  werden Depot-Daten manuell per Screenshot erfasst (siehe `depot/`-Ordner).
- **Report-Generator**: fasst alles in einem Tages-/Wochenreport zusammen.

## 8. Offene Punkte (werden im Verlauf mit Brian geklärt)

- **ERLEDIGT (2026-09-01, siehe Abschnitt 14): Core-Rules-vs-Advisory-Rules-
  Split (Conans Vorschlag vom 2026-08-30).** Ausgelöst durch einen real
  aufgetretenen Beleg für Conans "Rule Overfitting"-Warnung (RKLB-
  Meta-Retro-Fall, siehe Abschnitt 14) hat Brian den Split am 2026-09-01
  freigegeben und per Cross-KI-Diskussionsrunde mit Jack und Conan
  umgesetzt: 16 Core-Rules, ein Terminal-State-Mechanismus (Abbruch wird
  echter Systemzustand statt reiner Texterwähnung) und Advisory-Rules als
  situativer Rest. Volle Herleitung, beide KI-Antworten und der
  RKLB-Canonical-Failure-Case in Abschnitt 14.
- **ERLEDIGT (2026-08-30): Broker-Anbindung Scalable Capital LIVE über
  offiziellen Scalable-MCP-Connector ("Agentic Investing", scalable.capital).**
  Brian hat den Connector über Scalable Capitals eigene MCP-Schnittstelle
  (`https://mcp.scalable.capital/mcp`) aktiviert und mit Claude verbunden.
  Verfügbare Tools decken laut Scalable drei Kategorien ab: Analyse
  (read-only Depotdaten: Bestand, Cash, Performance, Transaktionshistorie),
  Monitoring (Kursalarme, Watchlists, Kursdaten) und Order-Ausführung (Kauf/
  Verkauf/Sparpläne, inkl. Preview- und Submit-Funktionen).
  **Die bereits vorher festgelegte Grenze bleibt UNVERÄNDERT bestehen, obwohl
  die Order-Ausführungs-Tools technisch verfügbar sind:** der Agent (Jarvis/
  Claude) nutzt AUSSCHLIESSLICH die read-only Analyse-/Monitoring-Funktionen
  (Depotabgleich, Kurse, Watchlist, Preview-Funktionen für Kauf-/Verkaufs-
  bzw. Sparplan-Vorschläge) – die tatsächlichen Order-Submit-Funktionen
  (`submit_buy_order`, `submit_sell_order`, `submit_savings_plan`,
  `cancel_order` u.ä.) werden NIEMALS vom Agenten selbst aufgerufen, auch
  nicht wenn Brian das im Chat ausdrücklich verlangt – das bleibt technisch
  UND als Grundsatzregel exklusiv Brians eigene Handlung direkt im Scalable-
  Interface (App/Web), unabhängig davon, dass Scalable selbst eine
  Bestätigungspflicht in den Order-Flow eingebaut hat. Diese Grenze ist keine
  lockerbare Projekt-Policy, sondern eine grundsätzliche, dauerhafte Grenze
  (siehe Abschnitt 1, "Grenze bleibt fix").
  **Praktischer Nutzen ab jetzt:** (a) **Live read-only Depotabgleich für
  Scalable Capital** ersetzt die bisherige manuelle Screenshot-Erfassung
  (siehe `depot/scalable-capital.md`, ab 2026-08-30 live abgeglichen) – (b)
  **fertig vorbereitete Kauf-/Verkaufsvorschläge** können über die
  Preview-Funktionen (`preview_buy_order`/`preview_sell_order`/
  `preview_savings_plan`) inhaltlich vorbereitet und Brian zur eigenen
  Bestätigung im Broker vorgelegt werden, ohne dass der Agent selbst
  submitted. **Erster Live-Abgleich (2026-08-30) deckte sofort eine
  Datenlücke auf:** eine bisher in KEINER Erfassung/keinem Screenshot
  enthaltene vierte Position, Boerse Stuttgart EUWAX Gold II (physisches
  Gold-ETC, 4 Stück, gekauft 30.01.2026), plus einen um +600€ höheren
  Cash-Bestand als zuletzt notiert (vermutlich die noch nicht abgebuchte
  Sparrate vor der Sparplan-Ausführung am 07.09.2026) – siehe
  `depot/scalable-capital.md` für Details. **Einordnung der Gold-Position
  (2026-08-30, von Brian entschieden): bleibt bewusst außerhalb der
  Champions/Profi/Talent-Struktur** und fließt auch NICHT in die Sektor-
  und Geografische-Streuung-Berechnung ein – reine defensive
  Diversifikation, keine aktive Einzelwert-These, kein sinnvoll
  zuordenbarer Sektor/Region.
  **Nur diese eine Portfolio-ID ist aktuell verbunden** (Scalable Capital) –
  finanzen.net zero, Trade Republic und Smartbroker+ bleiben bis auf
  Weiteres bei der manuellen Screenshot-Erfassung, da dort keine
  vergleichbare MCP-Anbindung bekannt ist.
  **Recherche zu Anbindungs-Alternativen (2026-08-30, von Brian
  angestoßen):** finanzen.net zero verbietet automatisiertes Auslesen der
  eigenen Daten ausdrücklich in den Nutzungsbedingungen ("Das Auslesen der
  Daten von finanzen.net ist nicht gestattet... auch für das
  automatisierte Auslesen über eine API") – hier bleibt die manuelle
  Erfassung die einzig regelkonforme Option, kein weiterer
  Handlungsbedarf. Trade Republic hat keine offizielle Kunden-API, nur
  inoffizielle, reverse-engineerte Community-Projekte (z.B. `pytr`) mit
  unklarem AGB-Status – bewusst nicht genutzt, passt nicht zum
  bisherigen Grundsatz, nur offizielle/sanktionierte Anbindungen zu
  verwenden (wie beim Scalable-MCP-Connector). Smartbroker+ bietet seit
  Mai 2026 tatsächlich eine offizielle REST-API (Depotabfragen,
  Transaktionsdaten, volle Order-Funktionalität) – kostenlos nur ab
  VIP-Status (45 Orders/Quartal, für Brians Buy-and-Hold-Ansatz
  unrealistisch), sonst 29,90€/Monat Grundgebühr. **Brians Entscheidung
  (2026-08-30): erstmal bei der manuellen Erfassung bei allen drei
  Brokern bleiben** ("vielleicht kommt es ja über die Zeit +") – keine
  der Alternativen rechtfertigt aktuell den Aufwand/die Kosten. Bei
  Smartbroker+ ggf. später erneut prüfen, falls sich Orderfrequenz oder
  Kosten-Nutzen-Abwägung ändern.
  **Data/Execution-Risk-Kategorie (2026-08-30, aus der Cross-KI-Diskussion
  in Agent-Playbook-Archiv-Diskussionen.md Abschnitt 10, von Brian freigegeben):** Das beste Regelwerk (Stop-Loss-
  Überwachung, Rebalancing-Grenzen, Regime-Einstufung, Positionsgrößen-
  Kontrolle) nützt wenig, wenn die zugrundeliegenden Daten nicht aktuell
  sind. Jeder Broker/jedes Depot führt deshalb ab jetzt einen expliziten
  Datenqualitäts-Status: 🟢 **Live-Daten** (aktuell nur Scalable Capital) /
  🟡 **verzögerte Daten** / 🔴 **manuell/Screenshot-basiert** (aktuell
  finanzen.net zero, Trade Republic, Smartbroker+). Bei 🔴 gilt: KEINE
  automatisierten Trade-/Stop-Entscheidungen allein auf Basis dieser Daten –
  stattdessen wird explizit ein manueller Kontrollpunkt erzeugt (z.B. "bitte
  aktuellen Stand von Trade Republic bestätigen, bevor diese
  Stop-Loss-Einschätzung verlässlich ist") statt stillschweigend mit
  veralteten Zahlen weiterzurechnen.
  **Werkzeug-Freigabe im Detail (2026-08-30, von Brian entschieden, nach
  Durchsicht aller 39 verfügbaren Scalable-MCP-Tools):**
  1. **Reine Analyse/Konten-Einblick (immer erlaubt, keine Rückfrage nötig):**
     `ping`, `get_account_profile`, `list_accessible_portfolios`,
     `get_portfolio_overview`, `get_portfolio_holdings`,
     `get_portfolio_cash_breakdown`, `get_portfolio_performance`,
     `get_overnight_summary`, `list_portfolio_transactions`,
     `get_transaction_details`, `get_security_quote`, `get_security_chart`,
     `get_security_news`, `search_securities`, `search_derivatives`,
     `list_order_venues`, `list_savings_plans`, `get_savings_plan_config`,
     `list_watchlist_items`, `list_price_alerts`, `list_portfolio_groups`,
     `get_portfolio_group` – keine Nebenwirkung, verändert nichts.
  2. **Verwaltung ohne Geldbewegung (2026-08-30, von Brian ausdrücklich
     freigegeben, darf der Agent künftig automatisch nutzen, ohne jedes Mal
     zu fragen):** `add_watchlist_item`/`remove_watchlist_item` (Scalables
     eigene Watchlist pflegen, z.B. spiegelnd zu `watchlist.md`),
     `create_price_alert`/`remove_price_alert` (Kursalarme setzen/löschen,
     z.B. für einen Kandidaten auf einen bestimmten Zielkurs),
     `create_portfolio_group`/`remove_portfolio_group`/
     `upsert_portfolio_group`/`add_portfolio_group_holdings`/
     `remove_portfolio_group_holdings` (Positions-Ordner bei Scalable
     organisieren). Bewegt kein Geld und platziert keine Order, deshalb
     freigegeben.
  3. **Vorschau-Funktionen (unbedenklich, da nichts ausgelöst wird):**
     `preview_buy_order`, `preview_sell_order`, `preview_savings_plan` –
     bereiten eine Order/einen Sparplan inhaltlich vor, lösen aber nichts
     aus. Werden vom Agenten genutzt, um Brian fertige Kauf-/
     Verkaufsvorschläge zur eigenen Bestätigung vorzulegen.
  4. **Tatsächliche Ausführung – NIEMALS vom Agenten aufgerufen, unabhängig
     von jeder Freigabe:** `submit_buy_order`, `submit_sell_order`,
     `submit_savings_plan`, `cancel_order`. Siehe Grenze oben – diese vier
     bleiben exklusiv Brians eigene Handlung im Scalable-Interface.
- **ERLEDIGT (2026-08-28, geprüft und als gelöst markiert 2026-09-04):
  Datenlücken blockieren einen sofortigen Portfolio-Regel-Check.** Die
  neuen Regeln (max. 10%/min. 1% Positionsgröße, ETF-Anteil ≥50%,
  Regionen-Verteilung übers Gesamtportfolio) sind dokumentiert und im
  Wochenfazit-Trigger verankert. Die damals genannten 9 Positionen
  (Intuitive Surgical, Constellation Software, Hermès, ServiceNow,
  MercadoLibre, Cellebrite, Broadridge, CBOE Holdings, Rambus) haben
  inzwischen alle vollständige, laufend gepflegte Daten in
  `depot/kategorisierung.md` (inkl. CRV-Ampel, KGV, MoS-Hinweis) – keine
  offenen Datenlücken mehr gefunden.

- Genaue quantitative Vorfilter-Kriterien für Schritt 1 (Universum-Screening)
- Diskrepanz-Schwellenwerte (ab wann gilt ein Fair-Value-Unterschied als "Konflikt"?)
- Depot-Cleanup-Report: Vorschlag, welche der aktuell ~27 Einzelwerte am ehesten
  raus sollten, um auf die Ziel-Struktur von max. 20 zu kommen (siehe Abschnitt 3)
- Ausschlusskriterien (Brian ergänzt diese im Laufe der Zeit)
- Cash-Allokations-Logik (Abschnitt 5, Punkt D) – noch nicht spezifiziert: wann ist
  "abwarten und Cash halten" die richtige Antwort statt Kaufen, auch wenn einzelne
  Kandidaten ein KAUFEN-Rating haben?
- ~~Rhythmus/Scheduling für den täglichen Watchlist-/Depot-Check~~ – **erledigt
  (2026-08-26)**, siehe neuer Abschnitt "Täglicher Trigger-Check" unten.
- Diskussionsrunde [3b] (KIs sehen die Urteile der anderen und nehmen Stellung) ist
  in der Architektur beschrieben, aber technisch noch nicht gebaut/getestet –
  bisher lief beim CLBT-Testlauf nur Runde 1 (unabhängige Einzelurteile ohne
  gegenseitige Diskussion)
- **NEU (2026-08-28): Scheduled-Task-Zuverlässigkeit beim Wochenfazit.** Der
  reguläre Freitags-Trigger (trig_01TM7yKJ5Lhuq8Qa7BFLrotb, 20:00 UTC) sowie ein
  von Brian angeforderter manueller Sofort-Lauf (`fire_trigger`) liefen beide
  als "SUCCEEDED" durch, aber der manuelle Lauf war nach nur ~50 Sekunden fertig
  und hat **keine PDF-Datei erzeugt** (keine Datei im Projektordner, keine
  SendUserFile-Auslieferung) – für 28 Positionen mit News-Check + mehrseitigem
  PDF unrealistisch schnell, die Session ist offenbar leer durchgelaufen, ohne
  dass das im Trigger-Status sichtbar wurde ("SUCCEEDED" bedeutet nur "Session
  ohne Absturz beendet", nicht "Aufgabe erledigt"). Das Wochenfazit vom
  28.08.2026 wurde daraufhin manuell in der laufenden Chat-Session nachgebaut
  (siehe `reports/build_wochenfazit.py` + `reports/Wochenfazit-2026-08-28.pdf`).
  **Zu beobachten:** ob der reguläre Freitags-Lauf kommende Woche wieder nur
  eine Kurz-Session ohne echten Output produziert – falls ja, braucht der
  Scheduled-Task-Prompt eine härtere Erfolgsprüfung (z.B. Pflicht-Check am Ende
  der Routine: "Wurde tatsächlich eine PDF-Datei geschrieben und per
  SendUserFile ausgeliefert? Falls nein, das explizit als Fehler behandeln,
  nicht als leises Ende.").
- **NEU (2026-08-28): Praxis-Scope-Entscheidung fürs Wochenfazit-PDF.** Die in
  Abschnitt 5 beschriebene volle "Agent-Kompakt"-Einzelseite (3-Stimmen-Leiste,
  Score-Gauge, DNA-Strang) bleibt der Standard für Ad-hoc-/Trigger-Analysen
  einzelner Positionen (siehe SKWD-Präzedenz), ist aber für alle 28
  Depot-Positionen JEDE Woche zu aufwendig (~30 Seiten Vollgrafik wöchentlich).
  Praxis-Kompromiss: Das Wochenfazit nutzt für die 28 Einzelpositionen ein
  kompakteres Karten-Raster (6 Positionen/Seite: Ticker, Kategorie, Rating,
  Score, Tier, Konfidenz, Kurzthese, Abstauber-Trigger) statt 28 Vollseiten;
  die Gesamtübersicht (Ranggruppen A-E), Auffälligkeiten, Methodik und Quellen
  bleiben volle Agent-Wochenreport-Seiten. Das volle Einzelblatt-Layout bleibt
  auf Anfrage bzw. automatisch bei echten Anlässen (Kauf-/Verkaufsentscheidung)
  verfügbar.
- **NEU (2026-08-28): Auffälliger Fall für die META-RETRO-RUNDE [3c] – RKLB-
  Scout-Quick-Filter.** Beim ersten Live-Einsatz des Scout-Regelwerks (Conan-
  the-Scout v1.12) auf zwei neue Talent-Positionen (Kraken Robotics, Rocket Lab)
  kamen Jarvis (Claude) und Jack (Gemini) für Rocket Lab UNABHÄNGIG zur exakt
  gleichen DNA-Check-Diagnose (K-Erfüllung 3/5 unter Deep-Tech-Override →
  Abbruch-Logik greift laut Wortlaut des Regelwerks: "K ≤ K-BASIS−2 → ABBRUCH →
  direkt Scout-Urteil"). Jarvis hat daraus konsequent RATING: ZU FRÜH (Sizing 0%
  für Neukauf) abgeleitet. Jack hat den Abbruch zwar explizit benannt ("ABBRUCH-
  LOGIK GREIFT"), ist aber trotzdem durch Moat-/Gründer-/Outcome-Module
  gegangen und kam am Ende auf RATING: BEOBACHTEN-STARK (Sizing 0,5-1,5%) –
  das widerspricht dem eigenen Abbruch-Befund und dem Vorrang-Prinzip (Regel
  31: Rating/Guardrail schlägt Score, nie umgekehrt). Conan (ChatGPT) hat die
  strikte K-Zählung/Abbruch-Logik gar nicht erst tabellarisch durchgespielt,
  sondern eher narrativ bewertet (RATING: BEOBACHTEN, Score 7,4/10) – dritte
  Variante der Regel-Anwendung. **Das ist ein sauberer Kandidat für Pipeline-
  Schritt [3c] (Meta-Retro-Runde):** die Frage ist nicht, ob RKLB ein gutes
  Investment ist, sondern ob/wie die Abbruch-Logik nach einem festgestellten
  DNA-Abbruch verbindlich verhindern soll, dass trotzdem ein normales
  BEOBACHTEN-Rating vergeben wird – aktuell bewerten alle drei KIs diesen
  Mechanismus unterschiedlich streng. Noch nicht mit Brian durchgeführt (siehe
  Analysedateien `KRKN-RKLB-scout-quickfilter-*-2026-08-28.md`); Trigger wartet
  auf Brians Entscheidung, ob die Retro-Runde jetzt oder gesammelt mit weiteren
  Fällen laufen soll.

## 9-13. [Ausgelagert ins Archiv — siehe `Agent-Playbook-Archiv-Diskussionen.md`]

Die früheren Cross-KI-Diskussionsprotokolle (Meta-Retrospektive,
Regelwerk-Erweiterung 90-100k-Ziel, Screening-Vorfilter-Verbesserung,
Gesamt-Review, Vincorion-Fallstudie — ursprünglich hier als Abschnitte
9-13, 2026-08-29 bis 2026-08-31) wurden am 2026-09-08 zur Verschlankung
dieses Dokuments in eine separate Archiv-Datei ausgelagert:
`Agent-Playbook-Archiv-Diskussionen.md`. Die Nummerierung (9-13) blieb
dort unverändert erhalten, damit alle bestehenden Verweise im Rest dieses
Dokuments (bisher "siehe Abschnitt 9/10/11/12/13") weiterhin exakt
auffindbar sind — sie wurden alle auf die neue Datei umgestellt. Die tatsächlichen,
aktuell gültigen Regeln, die aus diesen Diskussionen hervorgingen, stehen
unverändert an ihrem jeweiligen operativen Platz in Abschnitt 1-8 (jeweils
mit Datum/Herkunfts-Hinweis markiert) — hier geht nur der
Diskussions-Prozess dahinter verloren, nicht die Regel selbst.

Abschnitt 14 (Core-vs-Advisory-Rules-Trennung) bleibt bewusst in DIESER
Datei, da er von den Hermes-SKILL.md-Dateien direkt per Abschnittsnummer
referenziert wird ("Agent-Playbook.md Abschnitt 14") und daher live/
operativ ist, nicht nur historisches Diskussionsprotokoll.

## 14. Cross-KI-Diskussion: Core-vs-Advisory-Rules-Trennung + Terminal-State-Mechanismus (2026-09-01)

**Auslöser:** Conans Vorschlag vom 30.08. (siehe Agent-Playbook-Archiv-Diskussionen.md Abschnitt 12), das
Regelwerk in harte Core-Rules und kontextabhängige Advisory-Rules zu
trennen, wurde damals zurückgestellt ("bis das Regelwerk-Volumen in der
Praxis tatsächlich zum Problem wird"). Am 01.09.2026 wurde beim Aufräumen
des Rocket-Lab-Falls (siehe `analysen/KRKN-RKLB-nachholanalyse-final-2026-09-01.md`)
ein konkreter, real aufgetretener Beleg dafür gefunden: Jack (Gemini) hatte
beim Scout-Quick-Filter vom 28.08. selbst korrekt erkannt und benannt
"ABBRUCH-LOGIK GREIFT" (K-Erfüllung unter K-BASIS-2), ist danach aber
regulär durch Moat-in-Formation, Gründer-Score und Outcome-Wahrscheinlichkeiten
weitergelaufen und hat am Ende ein reguläres BEOBACHTEN-STARK-Rating mit
echter Sizing-Freigabe (0,5-1,5%) vergeben — ein direkter Selbst-
Widerspruch, der die Rocket-Lab-Bewertung im System faktisch verfälscht
hätte, wäre er nicht beim Aufräumen aufgefallen. Brian hat daraufhin
angeordnet, den Core-/Advisory-Split jetzt ernsthaft umzusetzen, inklusive
einer eigenen Cross-KI-Diskussionsrunde mit Jack und Conan (nicht nur
Jarvis-Entscheidung).

**Jarvis' Ausgangsvorschlag** (15 Punkte, an Jack/Conan zur unabhängigen
Prüfung vorgelegt): Order-Ausführung ausschließlich manuell; USA-Cap 60%;
ETF-Mindestanteil 50%; Positions-Cap 10%/12%; Max. 20 Positionen; TMR
Going-Concern-Precheck → SCHROTT; TMR K [N/V] → Abbruch; TMR
Entscheidungshierarchie; Scout K [N/V] → Abbruch; Scout K≤K-BASIS-2 →
Abbruch; Scout Vorrang-Prinzip; Scout Fraud-Check-Abbruch; No-False-
Precision; "immer alle drei KIs"; Datenintegritäts-Tag-Hierarchie.

**Jacks unabhängige Antwort:** stimmt der Liste grundsätzlich zu, ergänzt
zwei Punkte — (a) der harte 18%-Trailing-Weight-Cap (Rebalancing-
Notfallgrenze) muss explizit als Core-Rule geführt werden, nicht nur als
Kontrast zur 15%-Review-Schwelle erwähnt; (b) eine explizite Regel, dass
niemals eine Sizing-Freigabe >0% erteilt werden darf, wenn ein
vorgelagerter Core-Breaker bereits ausgelöst hat. Jacks zentraler
Lösungsvorschlag: ein **"Circuit Breaker"**-Mechanismus — löst eine
Core-Rule/Abbruch-Logik aus, muss die Ausgabe SOFORT mit einem
standardisierten Abbruch-Block enden ("🛑 CIRCUIT BREAKER TRIGGERED",
auslösende Regel + Status "ANALYSE BEENDET, nachgelagerte Module
DEAKTIVIERT" + Endurteil + Sizing 0,0%), kein weiterer Text/Score/Sizing
danach.

**Conans unabhängige Antwort** (ohne Kenntnis von Jacks Antwort, eigener
Chat): stimmt der 15er-Liste zu ~90-95% zu, schlägt strukturell dieselbe
Grundidee wie Jack vor, aber formaler gefasst:
- **CORE RULE 16 — TERMINAL-STATE-INTEGRITÄT** (Conans wichtigste
  Ergänzung): Löst eine Core-Rule einen Abbruch/SCHROTT/PASS/sonstigen
  finalen Zustand aus, wird dieser Zustand sofort **terminal**. Nach
  Eintritt eines terminalen Zustands dürfen keine nachgelagerten Analyse-,
  Bewertungs-, Scoring-, Sizing- oder Ratingmodule mehr
  **entscheidungsrelevant** ausgeführt werden — höchstens noch
  diagnostisch/loggend, niemals ratingwirksam.
- **Präzisierung von Regel 11:** nicht "Rating schlägt Score" (zu vage,
  semantisch angreifbar), sondern **"Guardrail > Entscheidung > Score"**
  — ein höher priorisierter Guardrail schlägt jedes nachgelagerte
  numerische Ergebnis, Scores dürfen eine durch eine Core-Rule ausgelöste
  Entscheidung niemals überschreiben, relativieren oder kompensieren.
- **Core-Precedence-Law:** bei Konflikten entscheidet ausschließlich die
  höchste Core-Priorität; eine später erkannte oder positivere
  Information (z.B. ein starker Moat) kann einen bereits ausgelösten
  terminalen Core-Zustand NICHT rückgängig machen.
- **Modul-Eintrittsbedingungen ("Gates"):** jedes ratingrelevante Modul
  (Moat-in-Formation, Gründer-Score, Valuation, Outcome, Rating, Sizing)
  bekommt eine Eintrittsbedingung "Status == ANALYSE_AKTIV" — bei Status
  "ABBRUCH" ist der Eintritt in ein solches Modul gesperrt. Das ist der
  eigentliche Schutz gegen ein "Vergessen" des Abbruchs im Textfluss.
- **Kein Core-Override durch Advisory:** Advisory-Regeln dürfen den
  Analyseprozess innerhalb des von Core-Rules gesetzten Zustandsraums
  interpretieren, aber niemals einen Core-Zustand selbst verändern oder
  aufheben.
- Conans Kernsatz, wörtlich übernommen, weil er den Unterschied zum
  bisherigen Regelwerk am besten trifft: **"Core Rules are execution
  constraints, not recommendations"** — eine Core-Rule ist keine
  Information, die dem Modell übergeben wird, sondern verändert den
  zulässigen Analysezustand selbst.
- Empfiehlt, den RKLB-Fall explizit als **Canonical Failure Case** in
  diesem Abschnitt zu dokumentieren (siehe unten).

**Synthese (Jarvis, aus beiden unabhängigen Antworten zusammengeführt —
Jack und Conan kamen, ohne voneinander zu wissen, auf strukturell
dieselbe Grundidee: ein erkannter Abbruch muss den Prozess wirklich
stoppen, nicht nur im Text erwähnt werden. Das ist ein starkes Signal,
dass dies der richtige Fix ist, nicht nur eine von mehreren
gleichwertigen Optionen):**

### Core-Rules (16, unverhandelbar, execution constraints statt Empfehlungen)

1. Order-Ausführung ausschließlich manuell durch Brian — `submit_buy_order`/
   `submit_sell_order`/`submit_savings_plan`/`cancel_order` werden NIE
   vom Agenten aufgerufen.
2. USA/Nordamerika-Region: harte Obergrenze 60%.
3. ETF-Mindestanteil: mindestens 50% des Gesamtportfolios.
4. Einzelposition: max. 10% (Ausnahme bis 12% nur bei Top-Conviction,
   echte Ausnahme, kein neues Standard-Limit).
5. **Trailing-Weight-Hard-Cap 18%** (ergänzt von Jack): über 18% zwingendes
   Rebalancing, kein Ermessen — die 15%-Review-Schwelle bleibt Advisory.
6. Max. 20 Einzelpositionen.
7. TMR Going-Concern-Precheck bei Auditor-Zweifel → sofort SCHROTT, keine
   Ausnahme.
8. TMR K-Kriterium [N/V] → Sofort-Abbruch.
9. TMR Entscheidungshierarchie (Datenintegrität > Going-Concern >
   DNA-Abbruch > Risiko-Overrides > Valuation > Score > Sizing > Rating).
10. Scout K-Kriterium [N/V] → Sofort-Abbruch.
11. Scout K ≤ K-BASIS−2 → Abbruch → direkt Scout-Urteil, Moat-/Gründer-/
    Bewertungs-Module werden NICHT ratingwirksam.
12. Scout Fraud-Check ≥3 Flags ODER Going-Concern → automatischer Abbruch.
13. No-False-Precision-Regel — keine erfundenen Wahrscheinlichkeiten/
    Schein-Genauigkeit.
14. "Immer alle drei KIs" — niemals wird ein Kandidat allein auf
    Jarvis-Basis in Watchlist/Depot übernommen.
15. Datenintegritäts-Tag-Hierarchie (LIVE > VERIFIED > TRAINING > ESTIMATE;
    [N/V] bei K-Kriterien = Abbruchgrund).
16. **GUARDRAIL > ENTSCHEIDUNG > SCORE** (präzisierte Fassung von "Rating
    schlägt Score", Conans Formulierung übernommen) — ein höher
    priorisierter Guardrail schlägt jedes nachgelagerte numerische
    Ergebnis. Scores dürfen eine durch eine Core-Rule ausgelöste
    Entscheidung niemals überschreiben, relativieren oder kompensieren.
    Keine Sizing-Freigabe >0% ist möglich, wenn ein vorgelagerter
    Core-Breaker bereits ausgelöst hat (Jacks Ergänzung).

### Terminal-State-Mechanismus (Pflicht, ersetzt bisherige reine Textregel-Formulierung)

Löst eine der 16 Core-Rules einen Abbruch/SCHROTT/PASS/sonstigen finalen
Zustand aus, gilt ab sofort:

1. **Der Zustand wird sofort terminal.** Kein nachgelagertes Modul (Moat-
   in-Formation, Gründer-/Führungs-Score, Bewertung, Asymmetrie-Check,
   Outcome-Wahrscheinlichkeiten, Rating, Sizing) darf danach noch
   **entscheidungsrelevant** ausgeführt werden — höchstens diagnostisch/
   loggend (z.B. "informell, da Abbruch — nur als Kontext", wie Jarvis es
   beim RKLB-Fall bereits richtig gemacht hat), niemals ratingwirksam.
2. **Ausgabeformat bei Terminal-State (Pflicht ab sofort für TMR/Scout-
   Läufe, Jacks Vorschlag):** die Analyse endet mit einem klar markierten
   Abbruch-Block statt normal weiterzulaufen:
   ```
   🛑 ABBRUCH-ZUSTAND ERREICHT
   Auslösende Core-Rule: [z.B. Scout K ≤ K-BASIS−2]
   Festgestellter Wert: [z.B. K-Erfüllung 2/5]
   Status: ANALYSE BEENDET — nachgelagerte Module (Moat/Gründer/Outcome/
   Bewertung) NICHT ratingwirksam
   Urteil: [z.B. ZU FRÜH / SCHROTT]
   Sizing: 0%
   ```
3. **Core-Precedence-Law (Conan):** bei Konflikten entscheidet
   ausschließlich die höchste Core-Priorität. Eine später im selben Lauf
   erkannte oder positivere Information (z.B. ein außergewöhnlich starker
   Moat) kann einen bereits ausgelösten terminalen Core-Zustand NICHT
   rückgängig machen.
4. **Kein Core-Override durch Advisory-Rules.** Advisory-Regeln
   interpretieren den Prozess innerhalb des von den Core-Rules gesetzten
   Zustandsraums, verändern oder überschreiben aber niemals einen
   Core-Zustand selbst.
5. **Selbstprüfung vor Abgabe eines Ratings (Pflicht):** bevor ein
   TMR-/Scout-Urteil final ausgegeben wird, prüft der Agent explizit:
   "Wurde irgendwann in diesem Lauf ein Core-Rule-Abbruch-Zustand
   festgestellt? Falls ja: entspricht das Endergebnis exakt dem
   Abbruch-Ausgabeformat oben, ohne dass ein nachgelagertes Modul das
   Rating/Sizing beeinflusst hat?" Diese Prüfung ist selbst eine
   Core-Rule (Meta-Ebene) und gilt für Jarvis genauso wie für Jack/Conan.

### Advisory-Rules (Beispiele, nicht abschließend — situativ gewichtet, dürfen Core nie überschreiben)

Sektor-/Regionen-Zielbänder (bereits als "Ziel-Band, keine harte Grenze"
markiert); Screening-Index-Rotation; Formulierungs-/Erzählstil-Regeln
(Verständlichkeits-Regel); Trailing-Weight-Review-Schwelle bei 15%;
Sizing-Tier-Feinabstufungen innerhalb der Caps (z.B. 0,5%/1%/1,5% —
solange innerhalb der Core-Caps frei interpretierbar); regimebasierte
dynamische Anpassungen (dürfen Gewichtungen INNERHALB der Core-Grenzen
verändern, nie die Core-Grenzen selbst); Chartmuster-Erkennungs-
Feinheiten; Watchlist-Kategorisierungslogik (Champions/Profi/Talent-
Zuordnung).

**Sizing-Tier-Basis, explizit geklärt (2026-09-03, aus dem
3-KI-System-Audit, P2-Punkt Conans):** die Sizing-Tier-Prozentwerte
(z.B. 0,5%/1%/1,5%/2%...) beziehen sich, wie der 10%/12%-Positionsdeckel
selbst (Core-Rule 4), auf das **Gesamtportfolio**, NICHT auf den
Aktienanteil – ein Sizing-Tier von "1%" heißt also 1% des
Gesamtportfolios inkl. ETF/Gold/Cash, nicht 1% der Aktienpositionen
allein. Das ist dieselbe Bezugsgrößen-Unterscheidung, die bei der
10-6-4→10-7-3-Korrektur zum Fehler führte (siehe Abschnitt 3) – deshalb
hier explizit festgehalten, um denselben Fehlertyp an anderer Stelle zu
vermeiden. Die Kategorie-Kapitalgewichtsbänder (Champions 35-45%/Profi
20-30%/Talent 25-40%, Abschnitt 3) bleiben davon unberührt weiter auf
Aktienanteil-Basis – zwei unterschiedliche Kennzahlen mit zwei
unterschiedlichen, jeweils fest zugeordneten Bezugsgrößen.

### Canonical Failure Case: Rocket Lab (RKLB), 28.08.-01.09.2026

Zur Dokumentation, warum dieser Mechanismus eingeführt wurde (Conans
Vorschlag): Beim Scout-Quick-Filter für Rocket Lab hat Jack (Gemini)
korrekt erkannt und wörtlich notiert "ABBRUCH-LOGIK GREIFT" (K-Erfüllung
3/5, unter K-BASIS−2), ist aber danach regulär weitergelaufen: Moat-in-
Formation (4/4) → Gründer-Score → Outcome-Wahrscheinlichkeiten →
BEOBACHTEN-STARK-Rating → Sizing-Freigabe 0,5-1,5%. Das ist kein
Zahlenfehler und keine abweichende Einschätzung, sondern ein fehlender
Terminal-State: die Erkenntnis "Abbruch greift" wurde nicht in einen
unveränderlichen Systemzustand übersetzt, sondern blieb eine Textzeile,
die von den folgenden Modulen faktisch ignoriert wurde. Aufgelöst am
01.09.2026 zugunsten von Jarvis' ursprünglichem, regelkonformem Ergebnis
(RATING: ZU FRÜH, 0% für Neu-/Nachkauf) — siehe
`analysen/KRKN-RKLB-nachholanalyse-final-2026-09-01.md`. Bestehende
10-Stück-Position bleibt unangetastet (reine Aufstockungssperre, keine
Exit-These).

**Status: von Brian am 01.09.2026 angeordnet, Cross-KI-Diskussion mit Jack
und Conan durchgeführt (beide unabhängig befragt, ohne dass eine KI die
Antwort der anderen kannte), Ergebnis oben synthetisiert und mit
sofortiger Wirkung freigegeben.** Betrifft nur, WIE Core-Rules technisch
durchgesetzt werden (Terminal-State statt reine Texterwähnung) — keine
einzige inhaltliche Analyse-/Portfolio-Regel wurde dadurch verändert. Die
drei Methodik-Prompt-Dateien (`prompts/*.md`) bleiben unverändert, wie in
Abschnitt 2 festgelegt — der Terminal-State-Mechanismus ist eine
Ausführungs-Vorgabe für den Agenten (dieses Agent-Playbook.md-Dokument),
keine Änderung an Brians eigenen Prompt-Texten.
