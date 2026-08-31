# Nachhol-Analyse & Meta-Retro-Auflösung: Kraken Robotics & Rocket Lab
**Datum:** 2026-09-01 · **Analyst:** Jarvis (Claude) · **Anlass:** Brians Auftrag, die seit
2026-08-28 offene Analyse dieser beiden Neukäufe abzuschließen (siehe HANDOVER.md Abschnitt 11,
Punkt 13 und Abschnitt 7).

**Wichtig zur Einordnung:** Dies ist KEINE komplett neue Full-Scout-Analyse von Null. Am
28.08.2026 lief bereits ein vollständiger 3-fach-Quick-Scout (Jarvis/Jack/Conan) auf identischer
Schritt-0-Datenbasis (siehe `SCHRITT0-datenpaket-kraken-rocketlab-2026-08-28.md`,
`KRKN-RKLB-scout-quickfilter-*-2026-08-28.md`, `KRKN-RKLB-cross-check-fazit-2026-08-28.md`).
Diese Datei schließt zwei offene Lücken aus diesem Lauf: (1) den in HANDOVER.md dokumentierten
Meta-Retro-Fall bei Rocket Lab (Abbruch-Logik-Anwendung uneins zwischen den drei KIs), und (2)
die fehlenden formalen Scout-Beobachten-Protokolle (Pflicht laut Global Rule 14) für beide Werte.
Frischer Kurs-Check zum 2026-09-01 ergänzt.

---

## Teil 1: Meta-Retro-Auflösung Rocket Lab (Abbruch-Logik)

### Der Streitpunkt
Alle drei KIs kamen beim rohen DNA-Check auf strukturell dasselbe Ergebnis: K-Erfüllung klar
unter K-BASIS−2 (Jarvis: 2/5 klar erfüllt, Jack: 3/5 – beide explizit "ABBRUCH-LOGIK GREIFT"
benannt). Laut Regelwerk (`conan-the-scout-v1.12.md`, Abbruch-Logik-Block):

> K ≤ K-BASIS−2 → ABBRUCH → SCOUT-URTEIL

Das bedeutet wörtlich: bei Erreichen dieser Schwelle springt die Analyse DIREKT zum Scout-Urteil
– Moat-in-Formation, Gründer-Score, Bewertung, Asymmetrie-Check und Outcome-Wahrscheinlichkeiten
sind ab diesem Punkt keine regulären, ratingwirksamen Module mehr (Jarvis hat das korrekt so
gehandhabt: Moat-in-Formation nur "informell, da Abbruch – nur als Kontext, kein formaler Score").

**Was Jack tatsächlich getan hat:** Jack hat den Abbruch selbst explizit festgestellt
("ABBRUCH-LOGIK GREIFT" – Jacks eigener Wortlaut), ist aber danach trotzdem regulär durch
Moat-in-Formation (4/4), Fraud-Check, Hype-Bias, Killer-Thesis und Outcome-Wahrscheinlichkeiten
gegangen und hat am Ende ein reguläres Rating BEOBACHTEN-STARK mit echter Sizing-Freigabe
(0,5-1,5%) vergeben – so, als wäre kein Abbruch passiert.

### Warum das ein Regelfehler ist, keine gleichwertige Auslegung
Global Rule 31 (Vorrang-Prinzip) ist eindeutig:

> RATING VOR SCORE: ... Bei Widerspruch (z.B. Score deutet auf 8/10, aber ein Guardrail deckelt
> auf ZU FRÜH) gewinnt IMMER der Guardrail/das Rating, nie der Score.

Die Abbruch-Logik ist strukturell exakt so ein Guardrail – ihr eigener Wortlaut lautet "→
SCOUT-URTEIL", nicht "→ weiter mit reduzierter Konfidenz" oder "→ Moat-Modul entscheidet". Es
gibt im gesamten Regelwerk (ich habe die Datei vollständig neu gelesen, 823 Zeilen) **keine
Ausnahmeklausel**, die einen starken Moat-in-Formation-Score gegen einen bereits festgestellten
DNA-Abbruch aufwiegen lässt – im Gegenteil, die Moat-Deckel-Regel (26) und die
Nullhypothese-Pflicht (30) laufen in dieselbe Richtung: strengere Module dürfen ein Rating nur
nach UNTEN deckeln, nie ein bereits ausgelöster Abbruch nach OBEN durchbrechen.

Conan hat die Abbruch-Logik gar nicht formal durchgerechnet ("narrativ, kein harter Abbruch") –
methodisch unvollständig, aber kein Widerspruch zu einem eigenen Befund wie bei Jack.

### Auflösung
Jacks Ergebnis widerspricht sich selbst (eigener Abbruch-Befund vs. reguläres Rating danach) und
weicht damit vom Regelwerk ab – nicht nur graduell, sondern in der Kernlogik. **Jarvis' ursprüngliches
Ergebnis vom 28.08. war die regelkonforme Anwendung** und wird hiermit als offizielles System-Ergebnis
bestätigt:

> **RATING: ZU FRÜH** · Sizing-Empfehlung für Neu-/Nachkauf: 0% · Konfidenz 🟡
> (Details/Herleitung: `RKLB-scout-quickfilter-jarvis-claude-2026-08-28.md`, oben vollständig gelesen)

**Klarstellung, keine Verkaufsempfehlung:** Das ist eine Scout-Filter-Einordnung für weiteres
Aufstocken, keine Aussage zu Brians bereits gehaltenen 10 Stück (Trace-Position, bleibt unangetastet).

### Ehrlicher Hinweis an Brian (echte Methodik-Erkenntnis, keine bloße Förmelei)
Jarvis' eigene Notiz vom 28.08. bleibt berechtigt: Rocket Lab ist ein bereits skaliertes
$38-Mrd.-Unternehmen mit etabliertem Kerngeschäft (93+ erfolgreiche Launches), an das ein
unbewiesenes Frühphasen-Programm (Neutron) angehängt ist – das Deep-Tech-Override-Raster ist für
kleine Vorab-Umsatz-Firmen gebaut, nicht für diese "etabliertes Kerngeschäft + Moonshot-Anhängsel"-
Konstellation. Der DNA-Abbruch wird hier stark von Datenlücken (F&E-Prozentsatz, exakte
Burn-Multiple) UND vom hohen Neutron-Investitionstempo eines im Kern gesunden Unternehmens
getrieben, nicht von einem klassischen "diese Firma scheitert"-Muster. Das rechtfertigt nicht,
die Abbruch-Logik zu ignorieren (das bleibt ein Regelfehler), ist aber ein echter Kandidat für
eine bewusste Regelwerks-Ergänzung: z.B. eine explizite Formulierung, ob/wie die Abbruch-Logik bei
bereits skalierten Unternehmen mit einem einzelnen Frühphasen-Wachstumssegment anders greifen
soll. **Das ist eine Entscheidung für dich, keine, die ich einseitig in `conan-the-scout-v1.12.md`
eintrage** – die Datei bleibt unverändert, bis du das explizit freigibst.

---

## Teil 2: Formale Scout-Beobachten-Protokolle (bisher fehlend, Pflicht laut Global Rule 14)

### 🔭 Kraken Robotics (TSXV:PNG/OTC:KRKNF) – bestätigtes Rating: BEOBACHTEN-SPEKULATIV
(3-fach-Konvergenz stark, siehe `KRKN-RKLB-cross-check-fazit-2026-08-28.md` – alle drei KIs
landen unabhängig bei vorsichtiger Trace-Sizing, keiner sieht Kaufgrund. Wird hiermit final
bestätigt statt neu verhandelt.)

**Frischer Kurs-Check (2026-09-01):** ~C$5,34 (TSXV) – ggü. C$6,12 am 07.08./28.08. ein weiterer
Rückgang von ~13% in wenigen Tagen, 52W-Range C$3,31–C$10,72. Bestätigt die bereits am 28.08.
identifizierte Marktskepsis (Kursreaktion -6,25% nach Q2-Zahlen trotz Rekord-Auftragslage).

- **ABSTAUBER-LIMIT:** C$4,00–4,50 (Nähe zum unteren Drittel der 52W-Range, unter dem Niveau der
  Q1-Kapitalerhöhung von C$8,50/Receipt – wäre ein Signal, dass der Markt die Covelya-Integration
  bereits als gescheitert einpreist, nicht nur vorsichtig). Kein aktiver Nachkauf vor Erreichen
  dieser Zone ODER vor Klärung der Punkte unten.
- **UPGRADE-TRIGGER (mind. 2 von 3):**
  → Organisches Wachstum (ohne Covelya-Konsolidierung) kehrt über 2 aufeinanderfolgende Quartale
    auf >15% zurück (aktuell 4-9%)
  → F&E-Prozentsatz und Gründer-/Insider-Ownership werden erstmals belastbar offengelegt (aktuell
    [N/V] bzw. nur 2,20% Insider-Ownership bekannt – unter der 10%-E-Schwelle)
  → Schiedsverfahrens-Rückstellung aus Q2 2026 wird ohne weitere negative Überraschung abgewickelt
- **DOWNGRADE-TRIGGER (einer reicht):**
  → Weiteres organisches Wachstum <5% für 2 Quartale in Folge (M&A-Integration verdeckt
    Kernproblem)
  → Neue, unerwartete Rechtsstreit-/Integrations-Rückstellung
  → Covenant-Druck aus dem neuen $125M-Term-Loan/$60M-Revolver (Leverage-Anstieg ohne
    EBITDA-Wachstum)
- **BEOBACHTUNGSHORIZONT:** bis inkl. Q3 2026-Zahlen (~November 2026, erster sauberer
  Quartals-Blick nach vollständiger Covelya-Konsolidierung)

### 🔭 Rocket Lab (NASDAQ:RKLB) – bestätigtes Rating: ZU FRÜH (0% für Neu-/Nachkauf)
Kein formales Beobachten-Protokoll nötig (ZU FRÜH liegt unter der Beobachten-Schwelle), aber
Vertiefungs-Trigger aus der Original-Analyse bleibt gültig und wird hier bestätigt:

- **VERTIEFUNGS-TRIGGER (Wiedervorlage-Punkt):** Sobald Neutron einen erfolgreichen Erstflug
  hinter sich hat UND der Cash-Burn über 2 aufeinanderfolgende Quartale nachweislich sinkt – dann
  volle Fundamentalprüfung (TMR-Pfad möglich, da Kerngeschäft bereits etabliert) statt erneutem
  Scout-Durchlauf.
- **Nächster Prüfpunkt:** Q3 2026-Zahlen (~November 2026) + Neutron-Stage-1-Tank-Übergabe an die
  Startrampe (Q4 2026 avisiert, CEO hat feste Jahresend-Erstflug-Zusage bereits einmal relativiert).
- Bestehende 10-Stück-Trace-Position bleibt unangetastet – dies ist ausschließlich eine
  Aufstockungs-Sperre, keine Exit-These.

---

## Zusammenfassung für Brian

| | Kraken Robotics | Rocket Lab |
|---|---|---|
| Finales Rating | BEOBACHTEN-SPEKULATIV | ZU FRÜH |
| Sizing Neu-/Nachkauf | <0,5% (Trace) | 0% |
| Bestehende Position | 300 Stk. – unangetastet | 10 Stk. – unangetastet |
| Nächster Prüfpunkt | Q3 2026 (~Nov.) | Q3 2026 + Neutron-Erstflug |
| Offener Punkt für dich | – | Soll die Abbruch-Logik-Regel für "etabliert + Moonshot-Anhängsel"-Fälle ergänzt werden? (keine Änderung ohne deine Freigabe) |

Beide Positionen sind damit offiziell durch den 3-fach-Cross-Check-Prozess gelaufen und mit
vollständigen Beobachten-Protokollen versehen – der offene Punkt 13 aus HANDOVER.md ist damit
inhaltlich aufgelöst.
