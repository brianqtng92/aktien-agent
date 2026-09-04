# Lasertec Corporation (6920, Tokyo) – 3-fach Cross-Check-Fazit
**Stand: 2026-09-05**

## Anlass

Brian bat um eine vollständige, ergebnisoffene Analyse von Lasertec
(Watchlist-Champions seit 2026-09-04). Dies ist zugleich der **erste
produktive Einsatz der neuen Jack/Conan-Live-Websuche** (eingeführt
2026-09-04) für eine volle TMR-Analyse mit dem kompletten
Methodik-Prompt.

## Kritischer Fund: veralteter Fact-Pack-Kurs korrigiert

Jarvis' eigenes SCHRITT-0-Fact-Pack nannte einen Kurs von **¥46.570**.
Conans eigene Live-Recherche fand den tatsächlichen Kurs vom 04.09.2026:
**¥33.180** – eine Abweichung von **~29%**. Jarvis bestätigte das per
zusätzlicher WebSearch (Preisspanne ¥32.650-39.250 in den letzten Tagen,
mehrere unabhängige Quellen). **Das ist exakt der Mehrwert, den die
gestrige Websuche-Erweiterung liefern sollte:** ein Fehler in Jarvis'
eigener Recherche wurde von einer unabhängigen KI aufgefangen, statt sich
unbemerkt auf alle drei Urteile zu vererben. Alle Bewertungskennzahlen in
diesem Fazit basieren auf dem korrigierten Kurs.

## Technischer Nebenbefund: Google-Search-Grounding + sehr langer Prompt

Der erste Jack/Gemini-Versuch (mit `google_search`-Tool aktiviert) brach
nach nur 359 Output-Tokens mit `finishReason: STOP` ab, obwohl 26.571
Prompt-Tokens + 29.040 Tool-Use-Tokens verarbeitet wurden – Gemini
"erledigte" offenbar die Suche und hörte danach vorzeitig auf, statt mit
der vollen ~74K-Zeichen-TMR-Methodik fortzufahren. **Fix für diesen
Lauf:** Retry ohne `google_search`-Tool (Fact-Pack lieferte ausreichend
Grundlage) – lief sauber durch. **Zu dokumentierende Erkenntnis:** die
Kombination aus sehr langem Methodik-Prompt (>70K Zeichen) + nativer
Google-Search-Grounding scheint bei Gemini 2.5 Flash ein
Frühzeitig-Stopp-Risiko zu bergen – für künftige volle TMR/Scout-Läufe
ggf. Suche vorerst deaktiviert lassen und stattdessen (wie bisher) auf
Jarvis' eigenes Fact-Pack + Conans Suche (die bei OpenAI sauber
funktionierte) setzen, bis das genauer untersucht ist.

## Einzelvoten

| KI | Rating | Kategorie-Einordnung | Sizing | Reaper/Score | Konfidenz |
|---|---|---|---|---|---|
| **Jarvis (Claude)** | BEOBACHTEN | Champions (Qualität) / CRV vorsichtig | – | – | – |
| **Jack (Gemini)** | ABBRUCH (SCHROTT) | n/a (Terminal-State) | 0% | n/a | n/a |
| **Conan (ChatGPT)** | BEOBACHTEN | Profi+ (nicht sauber Champions) | 0% / Tier 4 | 6,5/10 | 🟡 Mittel, 70% |

## Jacks Abbruch: bekanntes Datenlücken-Artefakt, kein belastbares Urteil

Jack brach wegen zweier [N/V]-K-Kriterien ab: Piotroski-F-Score (für
japanische Emittenten strukturell oft nicht sauber ermittelbar) und
FCF-Marge (durch eine einzelne Quartals-Verzerrung als "nicht belastbar"
eingestuft). **Das ist exakt derselbe Reflex-Abbruch-Bug, der bereits bei
Asahi Intecc und Disco Corp dokumentiert wurde** (siehe HANDOVER.md
10.13/Watchlist-Änderungsprotokoll) – trotz der expliziten
TRAINING-vs-N/V-Klarstellung (Block 2/3) und trotz eigener Websuche
entschied sich Jack für die strengste Lesart statt einer plausiblen
[TRAINING]-Schätzung. **Bemerkenswerter Kontrast:** Conan stand vor
GENAU denselben Datenlücken (Piotroski nicht direkt gefunden, FCF-Marge
knapp/verzerrt) und schätzte beide mit [TRAINING] (Piotroski 7-8/9,
FCF-Marge ~19,5-20,3%) statt abzubrechen – korrekt nach der Methodik.
**Konsequenz:** Jacks Terminal-State-Ergebnis wird NICHT als belastbares
Urteil gewertet, sondern als Datenlücken-Artefakt archiviert. Diese Bug-
Wiederholung sollte in einer künftigen Sitzung genauer untersucht werden
(evtl. ein noch expliziteres Beispiel für "plausible TRAINING-Schätzung
bei Piotroski für japanische Emittenten" in den Klarstellungsblock
aufnehmen).

## Konvergenz zwischen Jarvis und Conan (die beiden belastbaren Urteile)

1. **Marge/Bilanz sind Champions-Klasse:** operative Marge 43-46%,
   Netto-Cash, keine Schulden, hohe Kapitalrückführung (Dividenden +
   Buybacks ~¥43,1 Mrd. FY2026).
2. **Moat ist real, aber präziser als "100%" zu fassen:** im ENGEN
   actinic-EUV-Segment de facto Monopol (>90%, ACTIS A150 einzigartig),
   im BREITEREN EUV-/Masken-Inspektionsmarkt führt KLA mit ~34-38%. Die
   bisherige Watchlist-Formulierung war für die Nische korrekt, aber
   unpräzise kommuniziert.
3. **FY2026 war ein echter Rückgang** (Umsatz -8,3%, operatives Ergebnis
   -14,3%) – kein Bilanztrick, aber Auftragseingang (+126% auf ¥237,5
   Mrd.) und Backlog (¥323,0 Mrd.) stützen die FY2027-Erholungsguidance.
4. **Bewertung ist nach der Kurskorrektur moderater, aber kein
   Schnäppchen:** KGV 30-38x je nach EPS-Basis, EV/FCF ~60x+.
5. **Beide raten aktuell von einem sofortigen Kauf ab**, beide setzen
   die nächsten Earnings (04.11.2026) als zentralen Prüfpunkt.

## Uneinigkeit: Champions oder Profi?

Conan stuft die AKTIE (nicht nur das Geschäft) als "Profi+" ein –
Hauptargument: hohe Beta (1,67-1,87), FCF-Marge knapp an der 20%-Schwelle,
Kundenkonzentrationsrisiko. Jarvis hält an Champions auf der
QUALITÄTS-Achse fest (Moat/Marge/Bilanz sind eindeutig Spitzenklasse),
trennt das aber bewusst von der KAUFBARKEITS-Frage (CRV), wo Jarvis
ebenfalls Vorsicht walten lässt. Das ist kein echter Widerspruch, sondern
eine Frage, ob "Champions" bei uns eine reine Geschäftsqualitäts-Kategorie
ist (Jarvis' Lesart, konsistent mit der bestehenden Kategorien-Definition
"Marge, Marktstellung, Wachstumsverlässlichkeit") oder auch
Kursstabilität/Beta einschließen sollte (Conans Lesart). **Empfehlung:
Kategorie bei Champions belassen** (konsistent mit der etablierten
Definition und mit ASML/TSM, die ähnliche Beta-Profile haben und bereits
Champions sind), aber CRV-Ampel korrigieren.

## Gesamtfazit und konkrete Änderungen

**Watchlist-Eintrag wird aktualisiert:**
- Kurs korrigiert: ¥46.570 → ¥33.180 (Stand 04.09.2026)
- CRV-Ampel: von 🟡 BEOBACHTEN (basierend auf falschem Kurs) zu 🟡
  BEOBACHTEN bestätigt, aber mit korrigierter Begründung (KGV 30-38x
  statt 41,5x, EV/FCF ~60x als zusätzlicher Vorsichtsfaktor)
- Kategorie-Begründung präzisiert: actinic-EUV-Monopol (eng) vs.
  breiterer KLA-Wettbewerb (Gesamtmarkt) explizit unterschieden
- FY2026-Rückgang + Auftrags-/Backlog-Erholung als Beobachtungspunkt
  ergänzt, Checkpoint nächste Earnings (04.11.2026)

**Kein Kauf-Trigger aktuell.** Nächster Prüfpunkt: Q1-FY2027-Zahlen
(~04.11.2026) – Order-Trend, Operating Margin (>40% halten), FY2027-
Guidance-Bestätigung.
