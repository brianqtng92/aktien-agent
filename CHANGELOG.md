# Changelog — Aktien-Agent System

Chronologisches Änderungsprotokoll für Agent-Playbook.md, die Methodik-Dateien (JJ/Conan/TA), Report-Formate und die Automatisierungs-Infrastruktur. Ergänzt (ersetzt nicht) die ausführlichen Herkunfts-/Begründungs-Notizen direkt in Agent-Playbook.md und HANDOVER.md — hier geht es um schnelle Scanbarkeit "was änderte sich wann", ohne das ganze Regelwerk lesen zu müssen. Neueste Einträge oben. **Hinweis:** Einträge vor den beiden 2026-09-16-Rebrandings (siehe unten) verwenden noch die damals gültigen Namen "Jack" statt "JJ" und "Jarvis" statt "Aegis" — bewusst nicht rückwirkend umbenannt, historisches Protokoll bleibt zeitgenau.

**2026-09-16, Risiko-Matrix (Punkt 45) zu Risiko-Quadrant-Chart umgebaut (Brian: "1:1 von Raketentonis PDF übernommen, unsere eigene Note einbringen?"):** Berechtigter Einwand — die reine Wort-Tabelle war strukturell identisch mit der Vorlage. Ersetzt durch einen echten 2D-Risiko-Quadrant (Matplotlib-Chart, Wahrscheinlichkeit×Schaden als Achsen, jeder Risiko-Punkt nach Herkunfts-Modul farbcodiert: KSF-Scorecard/Struktur-Risiko-Check/Debt-Maturity/DNA-Check mit Seitenangabe) statt einer Tabelle — visualisiert direkt die Herleitung aus dem eigenen 3-fach-Cross-Check-System. Begleittabelle bekam eine "Herkunft im Report"-Spalte statt der Wort-Ampeln. Musste dafür wieder eine eigene Seite bekommen (Kill-Sheet + Risiko-Quadrant passten mit Chart nicht mehr auf eine Seite) — Report jetzt 12 statt 11 Seiten. Betrifft Agent-Playbook.md (Punkt 45, Seitengerüst-Tabelle neue Zeile 7b) und den CBOE-Report.

**2026-09-16, Rebranding: Claude (Jarvis) → durchgängig Aegis (Brian, ausdrücklicher Wunsch):** Claude hieß bisher "Jarvis" in den meisten Rollen (Dateien schreiben, Git, PDFs, Chat mit Brian) und "Aegis" nur in der spezifischen Rating-/Sizing-Synthese-Rolle der 3-fach-Cross-Checks. Diese Unterscheidung entfällt — Claude heißt jetzt in JEDER Rolle Aegis. Durchgängig case-sensitiv, wortgrenzen-sicher umbenannt in Agent-Playbook.md, HANDOVER.md, allen drei Methodik-Prompts, den Bridge-Server-Docstrings, den 4 Scheduled-Task-SKILL.md-Dateien außerhalb des Repos sowie dem aktiven CBOE-Report (HTML + Analyse-Markdown, da an diesem Tag noch in Bearbeitung). Mehrere dadurch entstehende Redundanzen ("Aegis (Jarvis)" → nur "Aegis") von Hand bereinigt statt blind stehen gelassen. Prompt-Dateinamen und ältere CHANGELOG-Einträge bewusst unverändert (siehe Hinweis oben). Betrifft Agent-Playbook.md (Rebranding-Notiz im PDF-Report-Design-Abschnitt).

**2026-09-16, vier neue Rigor-Punkte 43-46 nach erneutem Vergleich mit Raketentonis MP-Materials-Report:** Brian teilte denselben Report, der ursprünglich unser Full-Deep-Dive-PDF-Format inspiriert hatte, und bat um einen aktuellen Vergleich. Zwei Techniken bestätigten bereits vorhandene Bausteine (Drittquellen-Fact-Check, Bear-Case neben der These), vier waren echte neue Funde — bewusst NICHT 1:1 übernommen, sondern auf unser Modulsystem aufgesetzt. Punkt 43: Verwässerungs-Wasserfall (ökonomisch voll verwässerte Aktienzahl bei komplexer Kapitalstruktur, nur bei ≥2 gleichzeitigen dilutiven Instrumenten, sonst entfällt). Punkt 44: Meilenstein-Timeline im Kill-Sheet um Positiv-/Warnsignal-Spalten erweitert. Punkt 45: Risiko-Matrix (Wahrscheinlichkeit×Schaden×Frühindikator), Zeilen zwingend aus KSF-Scorecard/Struktur-Risiko/Debt-Maturity abgeleitet statt frei erfunden. Punkt 46: Agent-Score-Breakdown — macht die bereits bestehende Anker-Bereich→Mali→Deckel-Herleitung als Tabelle sichtbar statt nur die Endzahl auszuweisen (erste Fassung wollte den Score fälschlich bottom-up aus sechs neuen Dimensionen neu berechnen, das hätte eine zweite, konkurrierende Rechenlogik zur bestehenden Anker-Methodik eingeführt — beim Umsetzen selbst korrigiert). Zwei weitere Ideen (benannte Entry-Varianten mit Einzel-Allokationen, Wertschöpfungsketten-Grafik) bewusst nicht übernommen (Over-Engineering bzw. kein universeller Baustein). Betrifft Agent-Playbook.md (Punkte 43-46, Seitengerüst-Tabelle Seite 7/8/10) sowie `prompts/jack-moat-reaper-v11.7.md` (v11.17→v11.18) und `prompts/conan-the-scout-v1.12.md` (v1.19→v1.20).

**2026-09-16, Rebranding: Jack (Gemini) → JJ, Report-Branding "Agent Deep Dive" → "J.A.C.K Deep Dive" (Brian, ausdrücklicher Wunsch):** Die Gemini-Persona heißt ab sofort "JJ" statt "Jack" — durchgängig umbenannt in Agent-Playbook.md, HANDOVER.md, `prompts/jack-moat-reaper-v11.7.md`, `prompts/jack-technical-analyst-v1.9.md`, `prompts/conan-the-scout-v1.12.md` sowie den Gemini-/OpenAI-Bridge-Server-Docstrings und den 4 Scheduled-Task-SKILL.md-Dateien außerhalb des Repos. Das Report-Masthead heißt ab dem nächsten neuen Full-Deep-Dive-Report "J.A.C.K DEEP DIVE" statt "AGENT DEEP DIVE" — das Akronym steht für die drei Agenten plus die KI-Ebene: J=JJ (Gemini), A=Aegis (Jarvis/Claude-Synthese), C=Conan (ChatGPT), K=KI. Bewusst NICHT rückwirkend geändert: Prompt-Dateinamen selbst (Referenzbruch-Vermeidung, gleiches Prinzip wie beim Reaper→Agent-Rebranding 2026-09-07), CHANGELOG-Einträge vor diesem Datum, sowie alle bereits abgeschlossenen `analysen/*.md`-Dateien und bereits gerenderten Reports (kein gemeinsames Template, jeder Report kopiert das Masthead individuell). Betrifft Agent-Playbook.md (neue Rebranding-Notiz im PDF-Report-Design-Abschnitt).

**2026-09-16, zwei neue Rigor-Punkte 41+42 nach externem Digital-Arts-Deep-Dive (uncoveredjapan.com, Brian bat um Prüfung gegen unsere Methodik):** Erst-Check gegen die eigenen Regeln ergab: die meisten Techniken des Artikels (Distributor-Konzentration mit Namen, Produktlinien-Tabelle, Management-Glaubwürdigkeits-Matrix, Kapitalrückführungs-Historie) existierten bei uns bereits identisch oder strenger (Punkte 5/6/8/9/25) — zwei waren ein echter, neuer Fund. Punkt 41: KSF-Scorecard — branchenspezifische Key Success Factors zuerst benennen, dann das Unternehmen je Faktor bewerten (✅/🟡/❌), gekoppelt an die Kill-Sheet-Trigger (jede 🟡/❌-Zeile wird automatisch Trigger-Kandidat). Punkt 42: Bookings/Backlog/Revenue-"Wedge"-Analyse bei Lizenz→Subscription-Transformation — macht die Lag-Struktur zwischen Bookings-/Backlog-Wachstum und Revenue/Op.Profit-Wachstum sichtbar, explizit als POSITIVES Signal statt Warnsignal eingeordnet. Ein dritter Vorschlag (Operating Profit pro Mitarbeiter) bewusst nicht übernommen (Data-Integrity-Risiko bei Personalzahlen). Betrifft Agent-Playbook.md (Punkte 41+42, Seitengerüst-Tabelle Seite 3+4) sowie symmetrisch `prompts/jack-moat-reaper-v11.7.md` (v11.16→v11.17) und `prompts/conan-the-scout-v1.12.md` (v1.18→v1.19).

**2026-09-16, CBOE Full Deep Dive abgeschlossen — erster echter 3-fach-Cross-Check nach dem Web-Search-Bugfix (siehe HANDOVER.md 10.14):** Rating KAUFEN (gestaffelt), Tier 2. Zentraler Fund: alle drei unabhängigen DCF-Rechnungen (Jarvis/Jack/Conan) kommen wegen CBOEs sehr niedrigem Beta strukturell über dem Analysten-Konsens heraus (WACC-Terminal-g-Spread zu eng, Terminal-Value-Anteil 84-87% EV) — Modell-Artefakt, kein Fehler. Peer-EV/EBITDA-Abschlag (14,25x vs. Peer-Median 17,3x) und Konsens stützen KAUFEN zusätzlich. Datenintegritäts-Fund: Jacks JSON meldete fälschlich `going_concern_flag: true`, widersprach eigener Prosa/Rating — als Generierungsfehler korrigiert. Nachkauf gestaffelt: Tranche 1 bei Stabilisierung über $268-270, Tranche 2 bei $255-262. Betrifft `analysen/CBOE-fulldeepdive-cross-check-2026-09-16.md`, `reports/CBOE-agent-deepdive-2026-09-16.{html,pdf}`, `depot/kategorisierung.md`, `depot/offene_empfehlungen.md`, `depot/prediction_ledger.md`.

**2026-09-16, Bugfix: `ask_gemini_agentic`/`ask_chatgpt_agentic` hatten NIE echten Web-Search-Zugriff (siehe HANDOVER.md 10.14):** Entdeckt beim CBOE-Full-Deep-Dive — Jack (Gemini) erfand Fundamentaldaten statt eine Datenlücke zu melden, weil die Funktion nur Depot-Tools im Payload hatte, nie `google_search`. Conan (ChatGPT) erkannte den fehlenden Zugriff korrekt und ehrlich, weil `ask_chatgpt_agentic` über die Chat-Completions-API lief, die gar kein Web-Search-Tool kennt. Fix: Gemini bekommt `enable_search`-Parameter (auf `gemini-2.5-flash` mit Depot-Tools gegenseitig ausschließend, da Google die Kombination erst ab Gemini-3 erlaubt — aktuell ohne Quota auf Brians Key); ChatGPT komplett auf die Responses-API umgebaut (dort laufen `web_search` und Depot-Tools zusammen, keine Einschränkung). Beide live end-to-end getestet nach Prozess-Neustart. Wichtige Alt-Einschränkung bleibt bestehen: bei Gemini + vollem 130KB-Methodik-Mega-Prompt weiterhin `enable_search=False` nötig (bekannter Trunkierungsbug, HANDOVER.md 10.10) — ein kondensierter Prompt (~15-20KB) ist der Weg, wenn Jack echte Suche UND die volle Methodik gleichzeitig braucht. Betrifft `~/.claude/mcp-servers/{gemini,openai}-bridge/server.py` (außerhalb des Repos), `HANDOVER.md` (neuer Abschnitt 10.14), `~/.claude/scheduled-tasks/taeglicher-trigger-check/SKILL.md`.

**2026-09-16, neuer Rigor-Punkt 40 — unternehmensspezifischer Leitindikator bei Rohstoff-/Preis-Abhängigkeit (Brian: "falls bei einer Aktie wie Shell oder Rio Tinto die Marktentwicklung eine Rolle spielt, die passenden Makro-Daten/Indikatoren mit reinpacken"):** Aegis identifiziert vor dem Dispatch an Jack den 1-3 wichtigsten unternehmensspezifischen Leitindikator/-en (z.B. Brent/WTI bei Shell, Eisenerz/Kupfer bei Rio Tinto) und liefert dessen Stand + Mehrjahres-Vergleich explizit ins Fact-Pack — ergänzt die bisher rein portfolio-generische Makro-Momentaufnahme. Technisch über neue LEITINDIKATOR-PFLICHT (Regel 39) in `prompts/jack-moat-reaper-v11.7.md` (v11.14→v11.15, MAKRO-KONTEXT-Sektion + SCHRITT 2C Zyklus-Overlay) umgesetzt. Bewusst nur Jack/TMR-Pfad, da Rohstoff-Großkonzerne nie über Scout laufen. Betrifft Agent-Playbook.md (Punkt 40) und `prompts/jack-moat-reaper-v11.7.md`. **Nachschärfung selben Tags (v11.15→v11.16):** der Leitindikator-Wert hatte in der ersten Fassung keine [LIVE]/[TRAINING]-Tag-Pflicht — Bruch mit der sonst ausnahmslosen Data-Integrity-Regel, auf Brians Rückfrage sofort korrigiert.

**2026-09-16, Head-to-Head-Ersatz-Gate um zwei Punkte 7+8 geschärft (Brian, nach Sichtung zwei echter Anwendungsberichte von Raketentonis "55555"-System — bewusst mit Abweichungen statt 1:1-Übernahme, auf unserem eigenen Rating-/Tooling-Fundament aufgebaut):** Punkt 7 konkretisiert "deutlich überzeugender" über einen Anker-Stufen-Sprung (TMR: voller AGENT-SCORE-Anker-Sprung, Scout: voller EV_Multiple-Band-Sprung) statt Raketentonis pauschaler 10-15%-Tauschhürde, die wir bewusst nicht übernommen haben (freistehende Prozentzahl ohne Herleitung wäre selbst falsche Präzision). Punkt 8 verlangt vor jeder "Ersetzen"-Empfehlung den über `get_portfolio_cash_breakdown` bestätigten Netto-Cash-Stand statt einer Annahme aus dem Brutto-Verkaufspreis (Gebühren/FX/Settlement) — bei uns über Live-Tooling gelöst statt wie bei ihm über manuelle Vorsicht, da wir direkten API-Zugriff auf den echten Cash-Stand haben. Betrifft Agent-Playbook.md, Abschnitt Head-to-Head-Ersatz-Gate.

**2026-09-15, zwei neue Rigor-Punkte 39 + Erweiterung von Punkt 19 (Abgleich mit Anthropics offiziellem Repo `anthropics/financial-services`, Brian fragte gezielt nach diesem Plugin):** Die meisten Bausteine des Repos (institutionelle Agents wie GL-Reconciler/KYC-Screener, Enterprise-Datenconnectoren wie FactSet/PitchBook/Moody's) sind für unseren privaten Einzeldepot-Agenten irrelevant. Der `/dcf`-Skill lieferte eine Bestätigung (TV>70%-EV-Warnung existierte bei uns bereits identisch, unabhängig entwickelt) und zwei echte kleine Ergänzungen: Punkt 39 Terminal-Value-Cross-Check über Exit-Multiple-Methode (Peer-Median-EV/EBITDA) neben der bestehenden Gordon-Growth-TV, nur im TMR-Pfad (Jack), kein Zusatzaufwand da dieselben Peer-Daten wie für Punkt 19 genutzt werden. Punkt 19 (Peer-Multiple-Tabelle) erweitert um volle Quartils-Statistik (Min/P25/Median/P75/Max) statt nur Median, sobald ≥5 Peers vorliegen (`/comps`-Skill-Vorbild) — ein reiner Median verschleiert sonst die Streuung der Peer-Gruppe. Betrifft Agent-Playbook.md (Punkt 19 + neuer Punkt 39) und `prompts/jack-moat-reaper-v11.7.md` (v11.13→v11.14, neue Regel 38 + SCHRITT 5 S3b/TV-Cross-Check). Conan/Scout bewusst nicht angefasst (kein DCF im Scout-Pfad, siehe bestehende Bucket-Ausnahme).

**2026-09-10, Korrektur-Risiko-Score neu eingeführt (Brian: "ich möchte, dass mein Agent mir eine Korrekturwahrscheinlichkeit berechnet"):** Bewusst KEIN Prozentwert (Core-Rule 13/No-False-Precision bleibt unangetastet) — statt einer erfundenen Wahrscheinlichkeit ein transparenter additiver 0-24-Score aus 10 quellenbelegten Einzelindikatoren (VIX, S&P/200D-SMA, Fear&Greed, HY-Spread, Zinskurve, CB-Event-Risiko, Geopolitik, Öl, Bewertungsbreite), Bucket-Ausgabe NIEDRIG/ERHÖHT/HOCH/SEHR HOCH statt einer Zahl. Noch nicht historisch zurückgetestet — als möglicher Ausbauschritt dokumentiert. Betrifft Agent-Playbook.md (neuer Abschnitt nach der S&P-200D-SMA-Heuristik), `depot/macro_context.md` (neue Tabelle + heutiger Erstwert 8/24 ERHÖHT), `~/.claude/scheduled-tasks/taeglicher-trigger-check/SKILL.md` (Schritt 2c.4).

**2026-09-15, erster Bucket-Wechsel des Korrektur-Risiko-Scores (ERHÖHT→HOCH), vollständiger Neu-Check am FOMC-Tag:** 51/126 (40,5%) — Fed-Hike jetzt ~90-92% gepreist (statt 58,7% Coin-Flip am 07.09.), BoJ-Hike ~97% gepreist für 17./18.09. auf 1,25% (höchster Leitzins seit ~31 Jahren), US-10J-Rendite auf 5,041% (höchster Stand seit Juli 2007), Straße von Hormuz "effektiv geschlossen" (95% Schiffsverkehrs-Einbruch) — Geopolitik-Flag deshalb von "bekannt" auf "neue Eskalation" hochgestuft (offener Punkt vom 10.09. jetzt mit Zweitquelle geklärt), Yen-Carry-Trade-Unwind bestätigt aktiv (Spekulanten erstmals seit Februar netto-long Yen). Gegenläufig: HY-OAS-Spread weiterhin stabil bei 270 Bps, MOVE-Index sogar leicht niedriger, SPY weiterhin klar über der (weiter steigenden) 200-Tage-Linie — der Aktienmarkt selbst hat noch nicht gebrochen. Escalation ist faktenbasiert, nicht methodenbedingt. Bucket-Wechsel als reine Risiko-Einordnung kommuniziert, keine automatische Handlungsempfehlung.

**2026-09-15, Korrektur-Risiko-Score v6 — Lücken-Check auf Brians Nachfrage ("Indikatoren die ich vergessen habe?"):** Zwei echte Lücken geschlossen: US-M2-Geldmenge (Tier 1, war im ursprünglichen Quantical-Vorbild enthalten, beim v2-Bau übersprungen) und China-Kredit-/Immobilien-Stress (Tier 1, war bereits qualitativ in macro_context.md getrackt, aber nie in den Score eingebunden — gleiches Muster wie der DXY-Fund im Jack-Audit). Fünf weitere legitime, aber bewusst NICHT ergänzte Indikatoren dokumentiert (Bankensektor-/Repo-Stress, Margin-Debt, Konsumentenkredit-Ausfallraten, Gewinn-Revisions-Breite, Marktkonzentrationsrisiko — letzteres explizit als Redundanz zu Marktbreite/RSP-SPY abgelehnt). Bei jetzt 25 Indikatoren wird die von Jacks Audit benannte Komplexitätsgrenze als erreicht markiert — künftige Ergänzungen sollen eher mit einer Streichung einhergehen als rein additiv erfolgen. Neuer Wert: 45/123 (36,6%) ERHÖHT (übrige Werte noch vom 10.09., kein vollständiger Neu-Check).

**2026-09-10, Korrektur-Risiko-Score v5 — Yen-Carry-Trade-Risiko + MOVE-Index + Globale Staatsanleihen (Brian: "Staatsanleihen und Yen Carry Trade mit reinnehmen"):** Drei neue, real recherchierte Indikatoren. Yen-Carry-Trade-Risiko (Tier 3) ist der bedeutendste Fund: USD/JPY 154,35 bereits unter der 155-160-Stabilitätszone, BoJ-Hike auf 1,25% (höchster Leitzins seit ~31 Jahren) für 17./18.09. "almost fully priced", mehrere Finanzpresse-Quellen beschreiben den Unwind bereits als aktiv laufend — Score 3/3 (kein hypothetisches Risiko, ein laut Quellenlage bereits laufender Prozess, vgl. August-2024-Präzedenzfall). MOVE-Index (Tier 2, Bond-Markt-Pendant zu VIX): 77,88, ruhig. Globale Staatsanleihen-Renditen (Tier 2, US10Y+Bund10Y+JGB10Y synchron): Bund-10J auf höchstem Stand seit April 2011, JGB-10J steigend im Kontext des höchsten BoJ-Leitzins seit ~31 Jahren — Score 3/3. Neuer Wert: 43/117 (36,8%) ERHÖHT, nahe der 40%-Schwelle zu HOCH — Anstieg durch echte neue Fakten getrieben, nicht durch Methodik-Änderung. Offener Punkt: mögliche Geopolitik-Flag-Hochstufung wegen erwähnter US-Iran-Eskalation, noch nicht mit Zweitquelle verifiziert.

**2026-09-10, Korrektur-Risiko-Score v4 — Audit durch Jack + Jarvis-Gegenprüfung (Brian: "die Agenten sollen das intensiv durchgehen"):** Conan-Bridge nach 4 Versuchen nicht erreichbar, Jarvis übernahm die Gegenprüfungs-Rolle transparent als Aegis-Fallback. Übernommene Funde: HYG/LQD-Ratio gestrichen (Redundanz zu HY-OAS-Spread), Chicago-Fed-NFCI Tier2→Tier1 abgestuft (Redundanz-Fix ohne Streichung), Bewertungsbreite (Depot-spezifisch) komplett aus dem Score entfernt und läuft jetzt als separater Portfolio-Overlay (Kategorienfehler: Score soll den Markt bewerten, nicht das eigene Depot), Öl-Preis-Regime um fehlende 3-Punkte-Stufe ergänzt, US-Dollar-Index (DXY) neu aufgenommen (war bereits getrackt, aber nie eingebunden). Abgelehnte Funde (dokumentierte Divergenz): Michigan-Sentiment und Buffett-Indikator NICHT gestrichen (Malus/niedrige Gewichtung ist bereits die richtige Antwort auf ihre bekannten Schwächen), Sahm-Regel/Erstanträge-Redundanz akzeptiert aber nicht aufgelöst (leading vs. lagging, beide haben eigenen Wert), Zentralbank-Event-Risiko bleibt Tier 2 mit dokumentierter Ausnahme-Regel statt permanenter Tier-3-Hochstufung. Neuer Wert: 28/96 (29,2%) ERHÖHT.

**2026-09-10, Korrektur-Risiko-Score v3 — Shiller-CAPE + Buffett-Indikator ergänzt (Brian, nach weiteren Quantical-Screenshots + justETF-Recherche):** Beide bewusst mit niedrigem Gewicht (Tier 1/×1) aufgenommen, da laut eigener justETF-Quelle explizit KEIN Timing-Signal ("kann über Jahre hinweg 'hoch' bleiben"). Aktuelle Werte real recherchiert: Shiller-KGV 40,6-40,8 (98,8. Perzentil seit 1881, nur 1999/2000 höher), Buffett-Indikator 237-241% ("Strongly Overvalued", strukturell verzerrt durch Auslandsumsatz-Anteil). Score jetzt 29/105 (27,6%) ERHÖHT — beide Indikatoren trotz historisch extremer Werte bewusst nicht dominant, da niedrig gewichtet.

**2026-09-10, Korrektur-Risiko-Score v2 — Tier-Gewichtung + 9 neue Indikatoren (nach Vorlage von Brians externem Referenzsystem "Quantical"):** Von flacher 10-Indikatoren-Skala auf Tier-gewichtetes System (×1/×2/×3 je Vorhersagekraft, 19 Indikatoren) umgestellt, Summe jetzt als % vom aktuellen Maximum statt absoluter Punktzahl. Neu: CBOE-SKEW (v.a. in Kombination mit niedrigem VIX = "gefährliche Divergenz"), Chicago-Fed-NFCI, Sahm-Regel, Michigan-Verbrauchervertrauen (mit Zuverlässigkeits-Malus wegen "Vibecession" seit 2022), 10J-TIPS-Realzins, Erstanträge Arbeitslosenhilfe, plus 4 neue Ratio-Indikatoren ohne eigene Historie (Marktbreite RSP/SPY, Sektorrotation XLU/XLY, Kupfer/Gold, Kreditstress HYG/LQD — erst nach ~20-30 Tagen eigener Baseline gepunktet). Heutiger Wert: 23/102 (22,5%) ERHÖHT, Haupttreiber SKEW/VIX-Divergenz + Fed/BoJ-Event-Risiko. Quanticals eigene Drawdown-Rückschau-Tabelle (-10/-15/-20/-25% → historische Folgerendite) NICHT übernommen (Methodik nicht einsehbar) — als eigenständiges Backtest-Projekt mit echten Twelve-Data-Kursdaten vorgemerkt.

**2026-09-10, Full-Deep-Dive-Vollständigkeits-Härtung (Brian, nach HAWK/RMBS-Nachbesserung):** "Kein Zwang zur vollen Länge" im kanonischen Seitengerüst darf nicht mehr pauschal aus Bucket/Pfad abgeleitet werden ("Scout braucht kein DCF" ≠ "Scout braucht keine Bewertungs-Charts") — jede Auslassung jetzt einzeln pro Zeile begründet. Zwei Referenz-PDFs statt einer: NVO (TMR-Pfad) und HAWK-Fassung vom 10.09.2026 (Scout-Pfad). Betrifft Agent-Playbook.md, Abschnitt "Kanonisches Seitengerüst für Full Deep Dive".

**2026-09-10, zwei neue Rigor-Punkte 37/38 (Gemini-Vorschlag, gemeinsam mit Gemini verfeinert):** Die von Gemini vorgeschlagene sequenzielle Jack→Conan-"Zahnrad"-Verkettung wurde verworfen (Ankereffekt-Risiko, zerstört die Unabhängigkeit hinter echten Divergenzen wie RMBS' Piotroski 4/9 vs. 7/9). Zwei ihrer Zusatzmodule waren aber ein echter Mehrwert und wurden übernommen: Punkt 37 Portfolio-Fit/Klumpenrisiko-Check (reine Aegis-Synthese, Seite 10, nutzt nur bestehende Depot-/Cluster-Daten) und Punkt 38 Management-Tonalität über 2-4 Earnings-Call-Transkripte (Tone-Shift/Promises-vs-Reality/Dodge-Factor, Teil von Jacks und Conans eigener Recherche). Betrifft Agent-Playbook.md (Punkte 37/38 + Seitengerüst-Tabelle), `prompts/jack-moat-reaper-v11.7.md` (v11.12→v11.13) und `prompts/conan-the-scout-v1.12.md` (v1.17→v1.18).

**Pflege (neu, 2026-09-09, Priorität 4 aus dem Playbook-Meta-Review):** Jede
künftige substantielle Änderung an Agent-Playbook.md, den Methodik-Dateien
(`prompts/*.md`) oder den Hermes-`SKILL.md`-Dateien bekommt zusätzlich zur
bisherigen inline-Dokumentation (Herkunft/Begründung direkt im Regeltext)
einen Kurz-Eintrag hier — ein Satz, Datum, betroffene Datei(en). Ausgelöst
durch die Erkenntnis, dass Agent-Playbook.md (6.000+ Zeilen) allein durch
inline-Versionierungsnotizen kaum noch überblickbar ist. Zusätzlich: **beim
ersten Playbook-editierenden Chat jedes Kalendermonats** einmal kurz prüfen
(siehe Agent-Playbook.md "Wartung & Redundanz-Check"), ob sich in den
letzten Wochen echte Redundanz angesammelt hat (mehrfach fast wortgleiche
Regeln, wie beim Conan-Prompt-Fund vom 08.09.) — bei Fund: verschlanken wie
bereits einmal geschehen (siehe 2026-09-08 unten), nicht stillschweigend
weiter anwachsen lassen.

---

## 2026-09-09

- Playbook-Härtung Prio 1+2: feste Primärquellen + Bridge-Health-Check/Fallback
- Playbook-Härtung Prio 3: Selbstwiderspruch-Check als achter Standard-Klarstellungsblock (HANDOVER.md 10.13) — gilt jetzt für ALLE Kennzahlen bei jedem Bridge-Aufruf, nicht nur die 5 Kennzahlen aus dem Primärquellen-Standard
- Playbook-Härtung Prio 4: dieses CHANGELOG.md angelegt (aus git log rekonstruiert) + monatlicher Redundanz-Check-Prozess dokumentiert
- Over-Engineering-Kürzung 1: nicht-bindende Methodik-Datei nicht mehr an Jack/Conan mitgeschickt (~204 KB → ~130 KB pro Bridge-Aufruf, -35-40%)
- Over-Engineering-Kürzung 2: HANDOVER.md-10.13-Blöcke 1-3 (SCHRITT-0/eigene Recherche/WACC-Schätzung/TRAINING-vs-N/V) zu einem konsolidierten Block 1 zusammengefasst (inhaltlich unverändert, weniger redundante Formulierung)
- Over-Engineering-Kürzung 3: Blitz-Scan löst den vollen 3-fach-Cross-Check nur noch bei "hartem" Auslöser (Fraud/Delisting/Rücktritt/Going-Concern/M&A/Limit-Bruch) sofort aus - reiner Kurssprung ohne strukturelles Ereignis bekommt zuerst nur eine Jarvis-Only-Einschätzung, voller Check folgt beim nächsten Trigger-Check
- Over-Engineering-Kürzung 4: Rigor-Standard-Punkte 29+30 (DNA-Check-Tabelle + Primärquellen-Pflicht) zu einem konsolidierten Punkt 29 zusammengelegt (inhaltlich unverändert, Punkt 30 entfällt als eigene Nummer)
- Neue Faktor-/Korrelations-Analyse (`depot/faktor_korrelations_analyse.md`): deckt 3 versteckte Cluster auf, die quer über die bestehende Sektor-Tabelle laufen - Regierungs-/Verteidigungsbudget-Abhängigkeit 14,7%, Hochbeta-Kleinkapitalisierer 11,3%/22,8%, zinssensitive Finanzwerte 10,3%. Monatlich im Monatsrecap aktualisiert (neuer Punkt 12b)
- Erster Methodik-Backtest (`analysen/backtest-methodik-validierung-2026-09-09.md`): 3 historische Fallstudien (Wirecard/WeWork/Constellation Software) gegen die 16 Core-Rules getestet - 2/3 korrekt, bei Wirecard eine echte Schwäche im Going-Concern-Precheck gefunden (hängt am Auditor-Testat) und in jack-moat-reaper-v11.7.md dokumentiert
- Neuer "🔄 Kontinuierlicher Verbesserungsprozess (KVP)": auf Brians Wunsch institutionalisiert - laufend/monatlich (Monatsrecap Punkt 16)/vierteljährlich (Punkt 16b, Jack+Conan-Bridge-Check) sucht das System aktiv nach Mehrwert-Verbesserungen. Zwei-Stufen-Klassifizierung: 🟢 sicher+autonom umsetzbar (Effizienz/Redundanz/Doku, nie Rating-Logik) vs. 🟡 nur Vorschlag, braucht Brians Zustimmung (jede Rating-/Schwellen-/Risiko-Änderung). FIXE GRENZEN (Order-Ausführung manuell) bleiben unberührt
- NVO-Report korrigiert nach Geminis Zweitprüfung: DCF-Margen-Korrektur nachgetragen (proportionale Bandbreite statt Scheingenauigkeit), WACC-Sensitivitätsmatrix + SBC-vs-Buyback-Netting ergänzt (Seite 6+8). 2 von 3 Punkten waren Compliance-Funde (Rigor-Punkte 23/24 existierten bereits, wurden aber nicht angewendet) - neuer Rigor-Standard-Punkt 33 (Checklist-Verifikation vor Report-Abschluss) soll das künftig verhindern
- NVO-Report um neue Seite 9 erweitert (Pipeline-Ausblick/Amycretin, Patent-Klippe/Biosimilar-Risiko, Insider-Transaktionen) nach Jarvis' eigener Zweitmeinung - 3 neue, sektorabhängig ausgeprägte Rigor-Standard-Punkte 34-36, ab sofort Pflicht bei JEDEM künftigen Full Deep Dive, nicht nur NVO-spezifisch
- NVO-Report finalisiert: FCF-Quellendivergenz aufgelöst (primärquellenbasiert DKK 28,3 Mrd., DNA-Check-FCF-Marge von 19,1% auf korrekte 9,2% korrigiert) + Amycretin-Timing ins Kill-Sheet/Fazit zurückverdrahtet (neuer Langfrist-Katalysator 2027-2030, getrennt vom kurzfristigen CMD-Trigger)
- Kanonisches 10-Seiten-Full-Deep-Dive-Seitengerüst dokumentiert (NVO-Report als Referenzfassung) - Zielrahmen von 7-9 auf 7-10 Seiten erweitert, neue Sektor-Vertiefungsseite 9 (Pipeline/Struktur-Risiko/Insider) explizit als Vorlage für alle künftigen Full Deep Dives markiert, mit klarer Universell-vs-Sektorabhängig-Kennzeichnung je Seite
- Asahi Intecc (7747): erste Schnellanalyse, erster echter Einsatz des Aegis-Fallback-Mechanismus (Conan/ChatGPT-Bridge-Totalausfall) - anschließend Kurskorrektur auf Brians Live-Quelle (¥3.313→¥3.261) nach Selbstwiderspruch-Check
- Aurinia Pharmaceuticals (AUPH): neue Schnellanalyse, Aegis-Fallback erneut nötig (Conan-Bridge erneut komplett ausgefallen, 4 Versuche verschiedener Modelle) - eigener Gegencheck deckte einen Piotroski-F-Score-Selbstwiderspruch (7 vs. 4 je Quelle) und Jacks methodisch inkonsistenten Tier-2-Sizing-Vorschlag bei BEOBACHTEN-Rating auf
- **KENNZAHLEN-RECHERCHE-PFLICHT (neu, ausgelöst durch den AUPH-Fall, Brian: "warum ziehen die Prompts nicht immer aktuelle Daten statt oft TRAINING/N/V?"):** `jack-moat-reaper-v11.7.md` (intern v11.11→v11.12) und `conan-the-scout-v1.12.md` (v1.16→v1.17) erzwingen jetzt einen benannten Suchversuch VOR jeder [TRAINING]/[N/V]-Tag-Vergabe bei DNA-Check-Kennzahlen (gilt für Full Deep Dive UND Quick Filter/Scout) - ein Tag ohne dokumentierten Suchversuch ist jetzt selbst ein Regelverstoß. Zusätzlich [LIVE]-Tag-Missbrauch behoben: Jack hatte ROIC/FCF-Marge/Piotroski im AUPH-Fall fälschlich als [LIVE] getaggt, obwohl das ausschließlich Echtzeit-Marktdaten (Kurs/Zinsen/FX/News) zusteht - in beiden Dateien jetzt explizit klargestellt. Primärquellen-Standard-Tabelle in beiden Dateien um 3-6 weitere Kennzahlen erweitert (Jack: FCF-Marge/Piotroski/EPS-CAGR/Revenue-CAGR/Net-Debt-EBITDA/CCC; Conan: Umsatz-CAGR/NRR/Insider-Ownership). Keine Schwelle/Abbruch-Logik verändert - reine Sourcing-/Tagging-Disziplin, siehe Agent-Playbook.md Rigor-Standard-Punkt 29 (Erweiterung)
- Asahi Intecc (7747): Wiederholungslauf zur Verifikation der KENNZAHLEN-RECHERCHE-PFLICHT (Brian: "probieren wir's nochmal") - Ergebnis bestätigt die Wirkung: 3 von 5 K-Kriterien kippten gegenüber dem ungeprüften Erstlauf (ROIC 23,21%→19,7%, EPS-CAGR ~20%→5,99%, Capex ~4%→8,07% neu verfehlt; FCF-Marge ~18%→21,43% korrigiert sich positiv). Bear/Base/Bull-FV entsprechend niedriger revidiert, Kurs fällt dadurch aus Zone 2 (ATTRAKTIV) in Zone 3 (FAIR) - CRV-Ampel 🟢→🟡, Abstauber-Zone ¥3.200-3.300→¥2.700-2.900. Dritter Tag in Folge Conan/ChatGPT-Bridge-Totalausfall
- **Schnellanalyse-DNA-Check-Tabelle: [LIVE]/[VERIFIED]/[TRAINING]-Tags aus der Ist-Wert-Zelle entfernt (Brian, nach dem Asahi-Wiederholungslauf: "kann man diese ganzen [TRAINING] und [VERIFIED] weglassen?").** Punkt-21-Korrektur (keine Tag-/Typ-SPALTEN) hatte diese Tags bisher nur aus eigenen Tabellenspalten verbannt, nicht aus dem inline in die Ist-Wert-Zelle geschriebenen Text - ab sofort zeigt die Zelle nur noch "Wert (Quelle)", kein Tag-Wort davor. [N/V] bleibt sichtbar (Aussage über fehlende Daten, kein Konfidenz-Label). Nur die Report-DARSTELLUNG betroffen, KENNZAHLEN-RECHERCHE-PFLICHT und interne Tag-Vergabe unverändert, aggregierter Konfidenz-Wert bleibt im Report sichtbar. Siehe Agent-Playbook.md Schnellanalyse-Format-Abschnitt

## 2026-09-08

- A10 Networks (ATEN): zweiter Full Deep Dive mit 10-Seiten-Rigor-Standard
- Widerspruch bei A10-Schulden-Zahl behoben + neue Cross-Check-Pflicht
- Umsatz-/OCF-Grafiken + Dividendenrendite in beide Deep Dives eingebaut
- Peer-Tabellen um Operating-Margin/Median erweitert, DCF-Kernannahmen ergaenzt
- DNA-Check-Datentyp-Tags als Farb-Badges statt Klammer-Text
- Jack-Prompt v11.9 -> v11.10: Persona/Sarkasmus raus, Makro zentralisiert, JSON-Summary ergaenzt
- Conan-Prompt v1.12 -> v1.13: symmetrisches JSON-Summary; Hermes-Job statt neuem Job erweitert
- Master-Agent bekommt einen Namen: Aegis
- Hermes-Gedaechtnis-Synchronisations-Pflicht dokumentiert + SKILL.md-Dateien nachgezogen
- Conan-Prompt v1.14 -> v1.15: Regeln 19-42 auf Kurzverweise gekuerzt (Redundanz-Fund)
- Conan-Prompt v1.15 -> v1.16: gezielte N/V-Ausnahme gegen Datenverfuegbarkeits-Bias
- On-Demand-Analyse-Trigger dokumentiert (Watchlist-Zusatz + E-Mail)
- Agent Deep Dive Report: Scout-Pfad-Mapping dokumentiert
- Blitz-Scan 08.09.: On-Demand-Watchlist-Trigger VEIL dokumentiert (Methodik-Mismatch, Fonds statt Einzelwert)
- VEIL-Frage geklaert: unabhaengig vom Aktien-Agent-System, keine Analyse
- Agent-Playbook.md verschlankt: Abschnitte 9-13 in Archiv-Datei ausgelagert
- Watchlist: 4 neue Werte aufgenommen, Obergrenze auf 50 angehoben
- Watchlist-Scalable-Sync jetzt bidirektional (Weg C ergaenzt)
- Blitz-Scan 08.09.: Weg-C-Sync (UCB/LGND/Itochu/Qnity/BONESUPPORT -> Scalable) + LGND-ISIN-Fix (US53219L1076 hatte ungueltige Pruefziffer, korrekt US53220K5048)
- Ligand Pharmaceuticals (LGND): vollstaendiger 3-fach Full-Deep-Dive-Cross-Check
- Trigger-Check 08.09.: ruhiger Tag, Japan/Asien-Lücken-Kandidatensuche (10 Namen), Kuchendiagramm aktualisiert
- Rigor-Standard um 6 Punkte aus ChatGPT/Gemini-Cross-Review des CLBT-Reports erweitert
- Rigor-Standard: Geminis Nachfassrunde zu fehlenden Visualisierungen eingearbeitet
- Novo Nordisk (NVO): Full-Deep-Dive-Cross-Check mit erweitertem 28-Punkte-Rigor-Standard
- Cross-Check-Prozess: beide KIs bekommen ab sofort dieselbe Methodik-Datei
- NVO-Report: Kurs+KGV-Verlaufs-Chart ergaenzt statt Jahres-Tabelle (neue Seite 5/9)
- NVO-Report: Seite 5 (Bewertungs-Chart) und 7 (Kursverlauf) zusammengelegt
- NVO-Report: vollstaendige DNA-Check-Tabelle nachgeholt (K+E-Kriterien)
- NVO-Report: Tag- und Typ-Spalten aus DNA-Check-Tabelle entfernt
- Neues Report-Format: Schnellanalyse (2-3 Seiten) zwischen Kompakt und Deep Dive
- Rambus (RMBS): erste Agent-Schnellanalyse (neues 2-3-Seiten-Format)

## 2026-09-07

- Master-Status um Kategorisierungs-Kriterien + Watchlist-Kompaktübersicht erweitert (fuer Jack/Conan-Kontext ohne volle architecture.md/watchlist.md)
- architecture.md zu Agent-Playbook.md umbenannt, alle Referenzen aktualisiert
- Jack/Conan werden jetzt auch als eigenstaendige Suchquelle eingesetzt
- Portfolio-Lücken-Trigger (Talent-Slot + Europa/Gesundheitswesen): BONESUPPORT neu in Watchlist, ersetzt Rorze
- Alle 4 Scheduled Tasks + Hermes-Cron-Piloten komplett entfernt (Brians Wunsch)
- Taeglicher-Report-Pflichtstruktur ergaenzt (4-Punkte-Format)
- Trigger-Check 07.09. Folgelauf: Scalable wieder ok, Transaktion+Cash+Pie aktualisiert, Kraken/Rambus-Erinnerung + Tages-Mail verschickt
- Wochenfazit 07.09.2026: BEOBACHTEN - kein akuter Handlungsbedarf (verkuerztes 3-Tage-Fenster)
- Wochenfazit 07.09. Nachtrag: PDF-Base64-Anhang-Fix als strukturell nicht machbar verifiziert
- SKILL.md-Backups nach Hermes-Rebuild-Testlauf aktualisiert
- Trigger-Check 07.09. Folgelauf 2: ruhiger Tag, Watchlist-Ampel (30/30 gruen)
- Portfolio-Sensitivitaets-Analyse bei Material Shift eingefuehrt
- Drei neue Prinzipien nach Vergleich mit Raketentonis Agent-System
- Nordstern um drittes Grundziel ergaenzt: langfristig != fuer immer
- Drittes Grundziel praezisiert: nur mit nachvollziehbarem Grund verkaufen
- Full Deep Dive PDF-Format erweitert (Reaper Deep Dive Report)
- Chart-Workflow-Anleitung: --rsi --macd fuer Full Deep Dive verankern
- render_chart.py: FutureWarning bei RSI-Berechnung beseitigt
- ADR-Fallback-Regel fuer Twelve-Data-Plan-Sperren ins Playbook aufgenommen
- Cellebrite (CLBT): Full Deep Dive als Timing-Test, 3-fach Cross-Check
- Projektweites Rebranding: Reaper -> Agent (auf Brians Wunsch)
- Agent Deep Dive Report: auf 5+ Seiten erweitert (jetzt 7), CLBT als Beispiel
- Agent Deep Dive Report: heller/weisser Hintergrund statt dunklem Anthrazit
- CLBT Deep Dive: Schriftgroesse um 2pt erhoeht fuer bessere Lesbarkeit
- Alle Report-Formate auf hellen/weissen Hintergrund umgestellt
- Full-Deep-Dive-Rigor-Standard nach uncoveredjapan.com-Vorbild ergaenzt
- CLBT Deep Dive auf 10 Seiten erweitert: uncoveredjapan.com-Rigor-Standard

## 2026-09-06

- taeglicher-trigger-check 2026-09-05: ruhiger Tag, keine Trigger
- TMR: Regel-Widerspruch bei >20%-Quellenabweichung behoben
- Echte Ursache des Jack-Reflex-Abbruch-Bugs gefunden und behoben
- Hoya Corp (7741): vollstaendiger 3-fach TMR-Cross-Check + Fact-Pack-Tag-Fix-Test
- Hoya Corp (7741): Reaper-Kompakt-PDF nachgetragen
- Jack/Conan bekommen jetzt bei jedem Bridge-Aufruf den vollen Master-Status

## 2026-09-05

- Jack und Conan bekommen get_quote (Twelve Data) und read_master_status
- Lasertec Corp (6920): vollstaendiger 3-fach TMR-Cross-Check + wichtiger Kursfehler-Fund
- Alle drei KIs bekommen jetzt alle drei Methodik-Dateien (TMR+Scout+TA)

## 2026-09-04

- Prediction Ledger: Luecke geschlossen (2026-09-03 im 3-KI-Pulse-Check gefunden)
- architecture.md: Prediction-Ledger-Korrektur dokumentiert
- HANDOVER.md: RKLB-Meta-Retro-Fall als geloest markiert (war bereits am 01.09. erledigt)
- Bridge-Status-Log eingefuehrt (Conans Vorschlag aus dem 3-KI-Pulse-Check)
- macro_context.md: EZB- und BoJ-Sitzungstermine fuer Rest-2026 ergaenzt
- HANDOVER.md: drei weitere veraltete Offene-Punkte korrigiert (Gaps-Abarbeitung)
- architecture.md: 9-Positionen-Datenluecke als geloest markiert
- Täglicher Trigger-Check 2026-09-04: keine neuen Transaktionen, Watchlist-Ampel ruhig, Pie-Chart aktualisiert
- Frischer 3-fach-Scout-These-Check: Cellebrite (Exit) + Rocket Lab (Terminal-State bestaetigt)
- Neue Pflicht: Gruendliche These-Pruefung vor Verkaufsempfehlung (bestehende Positionen)
- Cellebrite-Korrektur umgesetzt: VERKAUFEN->HALTEN+Checkpoint, Talent->Profi
- Täglicher Trigger-Check 04.09. (2. Durchlauf): Makro-Kontext befüllt, E-Mail-Nachtrag für Cellebrite-VERKAUFEN
- Rocket Lab: konkrete, recherchierte Nachkauf-Aufstufungs-Trigger hinterlegt
- CBOE zu Champions, SoFi zu Profi - Talent-Rebalancierung exakt auf Ziel
- Lasertec zu Champions, Asahi Intecc zu Profi (Watchlist-Rekategorisierung)
- Watchlist "geschärfter Blick"-Review: ANET und USLM zu Champions hochgestuft
- Watchlist "geschärfter Blick": vollständiger Review aller 30 Werte abgeschlossen
- Depot "geschärfter Blick": Review der restlichen 14 Positionen abgeschlossen
- Rorze Corp (6323): vollstaendiger 3-fach Scout-Quick-Filter fuer freien Talent-Slot
- Neue Regel: Automatisierte Portfolio-Luecken-Kandidatensuche-Pflicht
- Praezisierung: Portfolio-Luecken-Kandidatensuche meint vollstaendige Index-Durchsuchung
- Neue Regel: tieferer Zweck der Kandidatensuche - Bereicherung, Unter-Radar-Funde, Qualitaets-Vergleich
- Blitz-Scan 16:15 UTC: Disco Corp (6146) -5,4% - Jarvis-Only (Bridges nicht verfügbar)
- Täglicher Trigger-Check 04.09. (3. Durchlauf): ruhiger Tag, Mehrfachlauf-Ursache geklärt
- Drei Meta-Regeln von Raketentonis System uebernommen: Vorrang-Hierarchie, Regel-Disziplin, Master-Status
- Neue Datei: depot/master_status.md - konsolidiertes Status-Dashboard
- Portfolio-Regel-Check: echte Berechnung statt Schaetzung
- Wochenfazit 2026-09-04: BEOBACHTEN - ETF-Anteil kritisch niedrig (21,7%), SoFi ueber 10%-Cap
- Cellebrite/Israel-Region-Luecke geschlossen
- Regelwerk gilt fuer alle drei KIs - Bridge-Bloecke 5+6 fuer Jack/Conan ergaenzt
- Jack und Conan bekommen eigene Live-Web-Recherche

## 2026-09-03

- Kategorisierungs-Fix (feste 10-6-4-Struktur), Disco-Corp-Analyse, taegliche Watchlist-Ampel
- Erinnerungs-Mechanismus fuer offene Kauf-/Verkauf-Empfehlungen (5-Werktage-Rhythmus, Chat+Mail)
- CRV-Ampel je Watchlist-Wert (Bewertungssignal, getrennt von Champions/Profi/Talent-Qualitaet)
- Margin-of-Safety/Drawdown-Historie in CRV-Ampel eingebaut (AI-Trend-Werte)
- CRV-Ampel auf 4 Stufen erweitert (+ORANGE) und auf alle 18 Depot-Positionen ausgeweitet
- Methodik-Fix: CRV-Ampel-Urteil ist eigene Einordnung, externe Quellen nur Rohdaten
- Trend-Pfeile (🔺/🔻) fuer CRV-Ampel-Auf-/Abstufungen eingefuehrt
- Watchlist-Uebersicht-PDF (lesbare Ansicht aller 30 Werte mit CRV-Ampel)
- 3 Ergaenzungen aus Jack/Conan-Produkt-Feedback zur CRV-Ampel umgesetzt
- CRV-Ampel: Bewertungsanker je Geschaeftsmodell + 5. Farbe GRAU ergaenzt
- 10-7-3-Korrektur + Terminal-State-Pflicht in Bridge-Meta-Instruktion (3-KI-System-Audit)
- Taeglicher Trigger-Check 2026-09-03: CLBT-Jarvis-Only-Reassessment nach CEO-Wechsel/Guidance-News
- CLBT-Jarvis-Only-Reassessment vom 2026-09-03 entfernt (nicht mehr benötigt)
- Restliches 3-KI-Audit-Backlog umgesetzt (alle 8 offenen Punkte)
- Fix: Prompt-Änderungsrechte-Klarstellung an Abschnitt 2 angeglichen
- TMR-Prompt v11.7 -> v11.8: Korrelierte-Mali-Regel gegen Reaper-Score-Double-Counting
- HANDOVER.md: E-Mail-Bug-Diagnose + Fix dokumentiert (Abschnitt 11, Punkt 14)
- Taeglicher Markt-/Makro-Kontext-Check (Fear&Greed, VIX, Zinsen, Geopolitik)
- Markt-/Makro-Kontext erweitert: S&P-Level, Wahl-/Fed-Kalender, weitere Dimensionen

## 2026-09-02

- Jack/Conan von Browser-Automation auf direkte API-Bridges umgestellt (openai-bridge/gemini-bridge) + Depot-Transaktions-Erkennung
- Orion Oyj + Asahi Intecc Testlaeufe, ISIN-Gegenprobe-Regel, Jack-Abbruch-Bug gefixt, Depot-Kuchendiagramm aktualisiert

## 2026-09-01

- HANDOVER.md: Migrations-Update Cowork -> Claude Code (Repo-Pfad, Scheduling, PDF-Pipeline)
- reports/render_pdf.py: lokaler HTML->PDF-Renderer (Playwright + Google Chrome)
- Kraken Robotics & Rocket Lab: Nachhol-Analyse abgeschlossen, Meta-Retro-Fall RKLB aufgelöst
- HANDOVER.md: Eskalations-Kanal dokumentiert (Push funktioniert, E-Mail nicht verdrahtet)
- HAWK: Chart- und Einstiegslage-Sektion nachgetragen (Seite 2 PDF + Markdown)
- watchlist.md: Watsco-ISIN korrigiert (falsch identifizierte Firma)
- HANDOVER.md: Scalable-Watchlist-Spiegel + Watsco-ISIN-Bug dokumentiert
- Core-vs-Advisory-Rules-Trennung + Terminal-State-Mechanismus (Abschnitt 14)
- Earnings-Season-Automatisierung: Phase-4-Earnings-Kalender umgesetzt
- depot/earnings_calendar.md angelegt + beide Scheduled Tasks erweitert
- E-Mail-Kanal (Gmail) verdrahtet - alle 4 Scheduled Tasks erweitert
- Antizyklisches Grundprinzip explizit verankert (Verkaufsdisziplin-Sektion)
- Antizyklisches Grundprinzip auf TA-Modul (Charttechnik) ausgeweitet
- Systematische Herleitung Talent-langfristig-vs-Zock-Trade-Tag
- benchmark_chart.py: alten Cowork-Pfad (/root/aktien-agent) auf relative Pfade umgestellt
- Charttechnik-Ergaenzung: echte Candlestick-Charts + Bodenbildung-Proxy
- Charttechnik-Skripte im Regelwerk verankert
- Tranchen-Entscheidungslogik + Zonen-Benachrichtigung per E-Mail/Preisalarm
- Portfolio-Kontext-Pflichtprüfung vor Zonen-/Tranchen-Empfehlungen
- Kostenstruktur Scalable + Trade Republic ergaenzt (finanzen.net zero war schon da)
- Klarstellung: Scalable dient nur dem ETF-Sparplan, BBCA ist Ausnahme
- Konkrete-Eurosumme-Pflicht + Klarstellung: Preisalarm ist kein Kaufsignal
- Explizite Limit-Order-vs-Beobachtung-Kennzeichnung in Zonen-E-Mails
- RMBS: Kompaktes Update 2026-09-01 (Nachkauf-Nachfrage) + Preisalarm 65€ gesetzt
- Neue Umschichtungs-Logik: Kapitalrotation zwischen Positionen (Gewinnmitnahme/Verlust -> aktive Wiederanlage-Prüfung)
- Add .gitignore (schuetzt lokale .mcp.json vor versehentlichem Commit)

## 2026-08-31

- Initial commit
- Disco Corp (6146.T): 3-KI-Quick-Filter-Cross-Check + Reaper-Kompakt-PDF (2026-08-31)
- Regelwerk: TA-Pflicht (Twelve Data) + Chart-und-Einstiegslage-Sektion + EUR-Durchgaengigkeit fuer JEDE Einzelanalyse (Brian-Feedback nach Disco-Analyse)
- Klarstellung: Couche-Tard-PDF ist nur lose Inspiration fuer Chart-und-Einstiegslage-Sektion, kein 1:1-Klon (Brian-Praezisierung)
- Disco Corp: Chart-und-Einstiegslage-Sektion nachgetragen (Twelve-Data-Fallback, Zonen+EUR, Brian-Feedback umgesetzt)
- Disco 6146: Full Deep Dive (DCF/Reverse-DCF dual-beta, Management-Score, Debt-Maturity, verifizierte DNA-Korrekturen, Chartmuster)
- Vincorion (V1NC): 3-KI-Cross-Check + PDF-Methodikvergleich + Regelwerk-Erweiterung (IPO-Overhang-Modul, Post-IPO-Datenluecken-Konfidenz, No-False-Precision-Regel)
- HawkEye 360 (HAWK): Nachtrag zu Lock-up-Vorziehung (02.09.) + Russell-2000-Aufnahme (21.09.), Positions-Sizing-Check gegen Trace-Deckel
- Formulierungsstil der Kurz-Fazits/PDF-Fazits an Raketentonis Erzählstil angelehnt (No-False-Precision-Regel unangetastet)
- Klarstellung: Formulierungsregel dient Verstaendlichkeit der Analyse, nicht nur dem Erzaehlstil (Item 7 ergaenzt)
- Täglicher Trigger-Check 2026-08-31: WEG S.A. (WEGE3) als LatAm-Watchlist-Kandidat, 3-fach-Quick-Filter (BEOBACHTEN, einstimmig)
- HawkEye 360 (HAWK): Full Scout 3-fach-Cross-Check (Jarvis/Jack/Conan) - erster Live-Test der Verstaendlichkeits-Formulierungsregel
- Vollständige technische Übergabe (HANDOVER.md) für einen neuen Claude-Code-Agenten
