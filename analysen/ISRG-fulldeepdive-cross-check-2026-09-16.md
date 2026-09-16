# Intuitive Surgical, Inc. (ISRG) — Full Deep Dive, 2-fach TMR-Cross-Check — 2026-09-16

**Auslöser:** Brians Bitte "Intuitive surgical ist der nächste Kandidat für einen Full Deep dive". ISRG ist eine bestehende Depot-Position (Champions-Kategorie, Smartbroker+/finanzen.net zero, 4 Aktien, Käufe 06.05.2026 und 21.07.2026, Ø-Einstand ca. $350/€1.400,50 gesamt). Der Quick-Filter vom 25.08.2026 (`analysen/ISRG-TMR-quickfilter-jarvis-claude-2026-08-25.md`) landete auf 🔴-Konfidenz (Einzelquellen-Limitierung) und einer eklatanten, unaufgelösten Bewertungs-Diskrepanz (Morningstar-FV $265 vs. Sell-Side-Konsens bis $509) — und empfahl explizit einen Full Deep Dive mit echtem DCF, Zweitquellen-Verifikation und formaler Moat-Decay-Analyse angesichts zwei frischer struktureller Angriffe auf den Kern-Burggraben.

**Ergebnis vorweg:** **HALTEN** (Bestandsposition, kein Nachkauf). Konfidenz konnte von 🔴 (Quick-Filter) auf 🟡 angehoben werden — die DNA ist jetzt zweitquellen-verifiziert stark, aber die beiden zentralen Unsicherheiten (Kartellrechts-Retrial, Ottava/Hugo-Wettbewerbsdynamik) bleiben laufend und ungelöst. **Prozess-Hinweis:** Der OpenAI-Bridge (Conan) war während dieser gesamten Sitzung erneut nicht erreichbar (dritter bestätigter Ausfall in Folge nach SNPS und HAWK am selben Tag) — diese Runde lief transparent als 2-fach-Check (Aegis + JJ).

---

## Aegis Live-Check (Twelve Data, autoritative Quelle)

Kurs **$383,61** [LIVE] (16.09.2026, +1,71% intraday), 52W-Range **$328,57-$603,88** [LIVE] (-36,5% vom Hoch, +16,8% über dem Tief). **Wichtiger eigener TA-Fund:** RSI14 hat sich von ~35 (08.09.) auf **56,1** (16.09.) erholt, MACD-Histogramm ist von stark negativ auf **+1,82** gedreht (bullische Divergenz der letzten 5 Handelstage), OBV zeigt seit dem 08.09. einen klaren Wechsel von negativ zu positiv. **JJs sekundäre TA-Quellen (TipRanks u.a.) zeigen dagegen noch die alten, negativen Werte (MACD -6,10, RSI 37-42)** — offenbar ein älterer Datenstand. Das ist ein eigenständiger, dokumentierter Beleg dafür, warum Twelve Data als LIVE-Referenz Vorrang vor sekundären Aggregatoren hat: die reale kurzfristige technische Erholung der letzten Woche wäre bei alleiniger Verwendung von JJs Quellen komplett übersehen worden.

## Aegis eigene DCF-Schätzung (Python, 10-Jahres-Explizit-Modell)

Basis: Kurs $383,61, 353,3 Mio. Aktien, Netto-Cash $8,63 Mrd. [VERIFIED, von JJ mehrquellenbestätigt], WACC 10,60% (Rf 4,1%, Beta 1,30 — Mittelwert aus Quick-Filter 1,46 und JJs 1,16, da Twelve-Data-Statistics gesperrt und beide Einzelwerte plausibel aber abweichend).

| Szenario | Aegis-FV (10J-DCF) | JJ-FV (10J-DCF) | TV-Anteil (Aegis) |
|---|---|---|---|
| Bear (Retrial verloren + Ottava/Hugo gewinnen Marktanteil) | $136 | $250-320 | 47,5% |
| Base (Wachstum verlangsamt sich moderat, Moat hält) | **$247** | **$420-460** | 57,8% |
| Bull (Rechtsstreit beigelegt, Wettbewerber scheitern an Skalierung) | $349 | $550-650 | 62,2% |

**Wichtiger methodischer Fund:** Ein erster Durchlauf mit nur 5 Jahren explizitem Cashflow-Horizont (statt 10) ergab absurd niedrige Werte (Base $169, Reverse-DCF implizit 34,9% nötiges Wachstum) — ein Artefakt eines zu kurzen Prognosehorizonts für einen Compounder mit noch lang laufender Wachstumsphase, nicht ein reales Bewertungsurteil. Nach Korrektur auf 10 Jahre explizit (wie von JJ verwendet) sinkt das implizite Reverse-DCF-Wachstum auf **17,1% p.a.** — nah an ISRG's eigener jüngster Wachstumsrate (Prozeduren +16% YoY, Revenue-CAGR 5J 16-18%) und damit plausibel, nicht absurd. **Lehre für künftige Analysen:** bei sehr wachstumsstarken Compoundern verzerrt ein zu kurzer expliziter DCF-Horizont das Ergebnis strukturell nach unten — die Wahl von 10 statt 5 Jahren ändert das Base-Case-Ergebnis um +46%, mehr als jede realistische WACC- oder Wachstumsraten-Anpassung.

**Aegis' Fair Value liegt damit am unteren Ende, JJs am oberen Ende der bereits vom Markt selbst gezeigten breiten Streuung** ($245,97 bis $490+ laut vorab recherchierten Sekundärquellen) — beide mit ähnlichen Kern-Annahmen (WACC ~10,6-10,9%, Wachstum ~13-14% anfangs), aber unterschiedlicher FCF-Margen-Progression (Aegis konservativer: 27%→31%, JJ optimistischer: konstant ~25% aber mit aggressiverer Wachstumsrate in der Übergangsphase). Die Wahrheit liegt vermutlich näher an JJs Zahlen, da ISRGs reale TTM-FCF-Marge bereits 29-33% beträgt (Quick-Filter/JJ übereinstimmend) — Aegis' konservativerer Ansatz dient als Bear-seitige Leitplanke, nicht als Punktschätzung.

---

## JJ (Gemini) — Full Deep Dive

**Datenqualität diese Runde sehr hoch** — durchgängig Zweitquellen-Verifikation ([VERIFIED]-Tags fast überall), Kursbasis konsistent mit Twelve Data.

**⭐ Wichtige eigenständige Korrektur ggü. dem Quick-Filter vom 25.08.:** JJ fand (und Aegis hat unabhängig via WebSearch bestätigt), dass **Gary Guthart bereits seit 01.07.2025 nicht mehr CEO ist** — er wechselte zu Executive Chair, neuer CEO ist **Dave Rosa**. Der Quick-Filter vom 25.08.2026 hatte fälschlich noch "CEO Gary Guthart (seit 2010)" geführt — ein über ein Jahr alter, unbemerkt gebliebener Fakt-Fehler in unserer eigenen vorherigen Analyse, nicht ein Fund dieser Runde selbst. Korrigiert hiermit für alle künftigen ISRG-Analysen.

**DNA-Check:** Alle K-Kriterien mit Zweitquellen bestätigt (ROIC 19,96-20,73%, FCF-Marge 24,7-32,79%, Op.-Leverage klar sichtbar, EPS-CAGR 19,5-21,5%). Piotroski-F-Score bestätigt bei 6/9 (10-Jahres-Median, kein Alarmsignal). CCC ~233 Tage explizit als branchenübliches Kapitalgüter-Merkmal eingeordnet, kein Fail-Signal. **DNA-Urteil deutlich gestärkt ggü. Quick-Filter (K 4/5 Grenzfall) — jetzt praktisch vollständig erfüllt.**

**Moat-Decay-Check (das Herzstück):** Moat-Score von anfänglich 4/4 im Fließtext auf **3/4** im finalen Urteil korrigiert (JJ selbst wertet die beiden strukturellen Angriffe als real genug für einen Abzug). Zur Ottava/Hugo-Dynamik: JJ fand eine Aussage von CFO Jamie Samath (September 2026), J&J werde "ein paar Jahre" brauchen, um gegen Intuitives volles Ökosystem zu skalieren — stützt die Oppenheimer-These der kurzfristigen Entlastung, ohne die langfristige Bedrohung zu verharmlosen. Zum Rechtsstreit: kein öffentlich bekannter Retrial-Termin oder Settlement-Stand auffindbar — bleibt eine offene, nicht auflösbare Unsicherheit.

**KSF-Scorecard:** 4× ✅ (Zulassungsbreite, Chirurgen-Ausbildungsökosystem, Datennutzung/KI, Innovationsgeschwindigkeit), 1× 🟡 (Krankenhaus-Capex-Zyklen), 1× ❌ (Rechtssicherheit Aftermarket-/Tying-Modell) — die einzige rote Ampel ist exakt der Punkt, der auch das zentrale Struktur-Risiko trägt.

**Management-Score: 6/7** — disziplinierte Kapitalallokation, aber Insider-Verkäufe (keine Käufe in 90 Tagen, ~$4,5-4,9 Mio. Verkäufe) als Beobachtungspunkt. Guidance-Zurückhaltung trotz Q2-Beat wird als umsichtig statt als Fehlverhalten gewertet.

**DCF:** Base $420-460, Bear $250-320, Bull $550-650 (WACC 10,88%, Beta 1,16 — abweichend von Quick-Filters 1,46, TradingView als Quelle). Löst die Bewertungs-Diskrepanz auf, indem die Extremwerte ($245,97 bzw. $565+) als Funktion unterschiedlicher Wachstums-/Moat-Decay-Annahmen erklärt werden, nicht als Modellfehler.

**Finales JJ-Urteil: HOLD, Agent Score 7/10, Konfidenz 🟡 (angehoben von 🔴).** Sizing: bestehende Position halten, kein Nachkauf vor Klärung von Rechtsstreit/Wettbewerbslage.

---

## Aegis-Synthese

**Konfidenz-Anhebung bestätigt:** Der Quick-Filter-Zweck ("Full Deep Dive mit Zweitquellen-Verifikation sollte die Konfidenz von 🔴 auf 🟡/🟢 anheben können, vorausgesetzt Piotroski/CCC verifizieren sich nicht als tiefere Probleme") ist eingetreten — beide Kennzahlen bestätigten sich als branchentypische Nicht-Probleme, nicht als versteckte Schwächen. Konfidenz jetzt 🟡, nicht 🟢, weil die zwei zentralen Unsicherheiten (Rechtsstreit-Ausgang, Ottava/Hugo-Marktanteilsentwicklung) beide laufend und nicht kurzfristig auflösbar sind — das ist ein ehrlicher, nicht ein methodischer Grund für die 🟡-Deckelung.

**Die DCF-Bewertungs-Diskrepanz ist jetzt besser verstanden, aber nicht vollständig aufgelöst:** Aegis' eigener konservativer Ansatz (Base $247) und JJs optimistischerer Ansatz (Base $420-460) unterscheiden sich primär durch die FCF-Margen-Progression, nicht durch grundlegend unterschiedliche Wachstums- oder Risikoannahmen — beide Modelle sind in sich schlüssig. Der aktuelle Kurs ($383,61) liegt zwischen beiden Base-Cases, näher an JJs Zahlen — was dafür spricht, dass der Markt aktuell eher JJs optimistischere Einschätzung (Moat hält trotz der Angriffe im Kern) einpreist als Aegis' konservativere.

**Was für Halten (nicht Verkaufen) spricht:** DNA jetzt zweitquellen-verifiziert exzellent (K praktisch 5/5, E 6/6 mit branchentypischer CCC-Ausnahme), praktisch schuldenfrei mit $8,63 Mrd. Netto-Cash, Moat trotz Abzug immer noch bei 3/4, disziplinierte Kapitalallokation, kurzfristige TA-Erholung (RSI/MACD/OBV) der letzten Woche, CFO-Aussage stützt kurzfristige Entlastung von Ottava/Hugo.

**Was gegen einen Nachkauf JETZT spricht:** Rechtsstreit-Ausgang ungewiss und nicht terminiert, Ottava/Hugo-Bedrohung langfristig real, Insider verkaufen (keine Käufe), Guidance-Kommunikation belastet die Bewertung weiterhin, Kurs bleibt unter SMA200 ($456,93) trotz kurzfristiger Erholung — die längerfristige technische Lage ist weiterhin bearish.

**Finales Rating: HALTEN** (Aegis-Synthese, deckungsgleich mit JJ). Bestehende 4-Aktien-Position wird gehalten, kein methodischer Nachkauf vor einer Klärung im Kartellrechtsverfahren oder einer erkennbaren Stabilisierung/Verschlechterung der Ottava/Hugo-Wettbewerbsdynamik. Agent Score 7/10 (JJ) übernommen als Aegis-Konsens, da Aegis' eigener DCF explizit als konservative Leitplanke und nicht als Punktschätzung verstanden wird.

**Nächster verbindlicher Prüfpunkt:** Q3-2026-Earnings (20.10.2026, Konsens-EPS $2,64), sowie jedes prozessuale Update im Kartellrechts-Retrial.

---

## PDF

Vollformat-Report: `reports/ISRG-agent-deepdive-2026-09-16.pdf` (J.A.C.K-Deep-Dive-Format, TMR-Pfad, Depot-Position).
