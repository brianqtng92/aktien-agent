# Arista Networks (ANET) — Full Deep Dive v2, 2026-09-17

Zweiter vollständiger 3-fach-Cross-Check, nach geschärfter Methodik (v11.23/v1.23) infolge mehrerer externer Gegenprüfungen (Gemini/ChatGPT) des ersten ANET-Reports vom 16.09.2026. Neutral, kein Depot-Bezug.

## Live-Daten (Aegis, Twelve Data)
Kurs $197,54 (16.09.2026 Schluss), 52W-Range $114,52-$214,89, Tagesbewegung +2,44%.

## Bridge-Status
JJ (Gemini) lief diesmal auf gemini-2.5-flash (2.5-pro weiterhin nicht erreichbar, mehrfach health-check-geprüft) — brach beim ersten Durchlauf nach dem DNA-Check ab (Antwortlängenlimit), wurde erfolgreich fortgesetzt. Bei der ersten Valuation-Antwort lieferte JJ nur Methodikbeschreibung statt echter Zahlen (Platzhalter-Symbole) — auf explizite Nachfrage lieferte JJ dann vollständige, konkrete Zahlen. Conan (ChatGPT/gpt-5.5) lief durchgehend fehlerfrei und lieferte auf Anhieb die vollständigste, primärquellenbelegteste Analyse (SEC-10-Q/10-K direkt zitiert).

## DNA-Check — konvergent zwischen JJ und Conan
Siehe PDF Seite 3. ROIC ~50% (Conan-Berechnung durch Netto-Cash-Basis verzerrt, methodisch erklärt), FCF-Marge SBC-bereinigt 44-54% je Berechnungsweg, Bruttomarge ~63%, Op.-Margin GAAP ~43-45%/Non-GAAP ~50%, Revenue-CAGR 27-32%, Net-Debt/EBITDA deutlich negativ (Netto-Cash), Capex/Umsatz ~1,4%. Piotroski-Divergenz (JJ 4/9, Conan ~6/9) — beide werten dies unabhängig als branchentypisch unkritisch bei einem Netto-Cash-Compounder.

## KSF-Scorecard + integrierte Moat-Komponenten-Zerlegung (Regel 53)
KSFs für Networking/AI-Infrastruktur: High-Speed-Ethernet-Roadmap (✅), Software/EOS-Konsistenz (✅), Hyperscaler-Design-Wins (🟡, konzentriert), Supply-Chain-Ausführung (🟡), Wettbewerbsposition/Moat gegen NVIDIA (🟡), Diversifikation jenseits MSFT/Meta (🟡).

Moat-Komponenten (Begründungsebene des Wettbewerbsfaktors, kein separates System):
- Software/EOS-Ökosystem: sehr stark, Trend stärker (beide KIs konvergent)
- Hardware-AI-Back-end: stark aber umkämpft — **Dissens**: JJ sieht Trend "stärker" (KI-Nachfrage spielt Arista in die Hände), Conan sieht Trend "schwächer" speziell im AI-Back-end (NVIDIA Spectrum-X gezielter Angriff auf wertvollste Cluster-Designs, IDC Q1-2026-Daten: NVIDIA #1 im Datacenter-Ethernet-Switching)
- Switching-Costs: mittel-stark, stabil-steigend
- Skalenvorteile/Hyperscaler-Co-Development: mittel, ambivalent (Kundenmacht)
- Offene Standards vs. NVIDIA-vertikale Integration: mittel, die eigentliche strukturelle Schlacht

## Financial Health + Kundenkonzentration/Capex-Verknüpfung (Regel 6-Erweiterung)
Bilanz Q2 2026 (Conan, SEC-10-Q-Primärquelle): Cash+Securities $13,34 Mrd., keine Finanzschulden, Current Ratio ~3,0x. Management-Score: Conan 5,5/7, JJ 6/7 — konvergent stark. Management-Tonalität zur NVIDIA-Frage: ehrlich, keine Übertreibung — explizite Segmentierung "sehr geringe Beteiligung bei vollständig vertikalen NVIDIA-Stacks, bessere Position bei Scale-out/Scale-across".

**Kundenkonzentration:** Top-2 ~42% des Umsatzes (Microsoft/Meta gemäß Vorjahresangaben). **Capex-Verknüpfung (neu):** Microsoft bestätigt FY27-Capex-Wachstum, CY2026 ~$190 Mrd. Konzernguidance. Meta guidet 2026 $130-145 Mrd. Capex explizit für AI-/Core-Infrastruktur. Beide Kunden bestätigen strukturell hohes, wachsendes Capex — der Engpass ist die interne Allokation (offene Ethernet-Fabrics vs. vertikale NVIDIA-Bundles), nicht das Budget selbst.

## Bewertung — drei unabhängige DCF-Ansätze
| Quelle | Bear | Base | Bull | Methode |
|---|---:|---:|---:|---|
| Aegis | $116 | $245 | $449 | 10J explizit, Exit-Multiple 18-34x, WACC 9,3% |
| JJ | $158,55 | $214,28 | $310,48 | 5J explizit, Gordon≈Exit-Multiple (Δ<3%, Zirkularitäts-Sperre nicht nötig) |
| Conan | $65 | $130-135 | $220 | Gordon 65%/Exit-Multiple 35% gewichtet nach Zirkularitäts-Sperre |

**Zirkularitäts-Sperre (Regel 38b):** Nur Conan hatte eine >30%-TV-Divergenz (Exit-Multiple ~30%+ über Gordon). Begründung für die 65/35-Gewichtung zugunsten Gordon: (1) unklare Terminal-Wettbewerbsposition gegen NVIDIA-Bundles in Jahr 10+, (2) bereits beobachtete Margin-Kompression durch Large-Customer-Discounts (Q2 2026 GM fiel auf 62,9%), (3) Wachstumsnormalisierungs-Risiko — explizit NICHT "näher am Kurs" begründet, regelkonform.

JJ musste die Sperre nicht anwenden (Konvergenz der beiden TV-Methoden), wich aber vom 10-Jahres-Horizont-Standard für Wachstumscompounder ab (nutzte nur 5 Jahre) — dokumentierter Methodik-Abweichungspunkt.

**Exit-Multiple-Sensitivität 3×3 (Regel 38c, Conan-Beispiel):**
| 5J-CAGR \ Multiple | 19,6x | 23,1x | 26,6x |
|---|---:|---:|---:|
| 12% | $129 | $147 | $165 |
| 17% | $157 | $179 | $201 |
| 22% | $190 | $216 | $244 |

**Known/Unknown/Unknowable:** Known = Umsatz/Margen/Cash/Konzentration/aktuelle NVIDIA-Marktanteilszahlen. Unknown = exakter 2026/27-Wallet-Share bei MSFT/Meta, tatsächliche Spectrum-X-Verdrängung je Cluster. Unknowable = ob offene Ethernet-Fabrics über 10J gegen vertikale GPU-Stacks dominieren, AI-Nachfrage 2030+.

**Peer-Vergleich inkl. EV/FCF (Regel 19-Erweiterung):** ANET EV/EBITDA ~45-46x, EV/FCF ~44-46x — höchste Bewertung UND überdurchschnittliche Marge im Peer-Set (Cisco, Broadcom, NVIDIA, HPE) — kein Inversions-Befund (Punkt 19), konsistentes Wachstums-/Margen-Premium.

## Historischer Max-Drawdown-Kontext (Regel 48, jetzt universell)
Eigene Berechnung aus Twelve-Data-Wochenschlusskursen seit 2016: **größter Drawdown -50,2%**, Peak $129,17 (20.01.2025) → Trough $64,37 (31.03.2025) — deutlich jünger und größer als die häufiger zitierte Covid-Korrektur oder der 2022er-Inflationsschock (-36,7%). These blieb danach intakt (Erholung auf $197,54 bis heute). Wichtige Erkenntnis: "günstig ggü. Historie" ist bei ANET keine Garantie gegen einen erneuten ~50%-Rückgang.

## Kill-Sheet mit graduierten Schwellenwerten (Regel 26-Erweiterung) + Meilenstein-Timeline
Siehe PDF Seite 8. Leitkatalysator ⭐: Q3 2026 Earnings (~November 2026).

## These-Monitoring-Kette (Regel 51, konsolidiert aus Kern-Annahmen+Kipppunkten)
6 Kernannahmen als verkettete Tabelle, siehe PDF Seite 9. JJ und Conan lieferten strukturell dieselben 5-6 Kernannahmen unabhängig — starkes Konvergenzsignal trotz unterschiedlicher Bewertungs-Schlussfolgerung.

## Struktur-Risiko + Insider-Transaktionen
NVIDIA Spectrum-X: IDC Q1-2026 zeigt NVIDIA als #1 im Datacenter-Ethernet-Switching (Markt +39,8% auf $15,4 Mrd.) — struktureller, mehrjähriger Risikofaktor. Insider: überwiegend 10b5-1-Planverkäufe (Ullal, Bechtolsheim, Duda), keine Open-Market-Käufe in 12 Monaten dokumentiert — kein Alarmsignal, aber bei aktueller Bewertung relevant.

## Dissensus-Map (Regel 52)
| Teildimension | JJ | Conan | Aegis |
|---|---|---|---|
| Business-Qualität | 🟢 | 🟢 | 🟢 |
| Moat/Wettbewerbsposition | 🟢 (Trend stärker) | 🟡 (AI-Back-end schwächer) | 🟡 |
| Leitrisiko NVIDIA | 🟡 gemanagt | 🟠 wesentlich | 🟡 |
| Bewertung (Base-FV vs. Kurs) | 🟢 $214 (über Kurs) | 🔴 $130 (unter Kurs) | 🟢 $245 (über Kurs) |
| Wachstumsverlässlichkeit | 🟢 | 🟡 | 🟢 |

Der Dissens entsteht NICHT bei den Fakten (alle drei bestätigen unabhängig Netto-Cash, Margen, Kundenkonzentration ~42%, NVIDIA-Spectrum-X-Realität), sondern bei der TV-Methoden-Gewichtung und dem DCF-Horizont.

## Aegis-Synthese
**Rating: BEOBACHTEN, Agent Score 7-8/10, Konfidenz 🟡 MITTEL.** Die faire-Wert-Spanne hat sich durch die geschärfte Methodik NICHT verengt, sondern verbreitert ($65-449 über drei unabhängige Ansätze) — ehrlicher Ausdruck echter, primärquellenbelegter Unsicherheit statt Scheinpräzision. Champions-Fit ja (Unternehmensqualität unbestritten), sofortige hohe Konviktion nein (Aktienqualität zum aktuellen Preis bleibt die offene Frage).

## Technische Analyse (JJ) — nachgezogen mit voller Methodik (NEU, 2026-09-17)

Nach externer Kritik (Gemini/ChatGPT) zur TA-Sektion des ERSTEN ANET-Reports (16.09.) wurde geprüft, ob es sich um Methodik- oder Compliance-Lücken handelt: **Compliance-Fund, keine Methodik-Lücke** — nahezu alle als "fehlend" kritisierten Punkte (Weekly/W1, Relative Stärke, Volumen/OBV, Support/Resistance) existierten bereits in `prompts/jack-technical-analyst-v1.9.md`, wurden im ersten Report aber nur mit 3 von ~15 Feldern gezeigt. Für den v2-Report wurden echte Twelve-Data-Werte gezogen (SMA20/50/200, RSI14, MACD, BBANDS, ATR14+20T-Ø, OBV, SPY-Zeitreihe für Relative Stärke) und die volle Methodik als neue Seite 6 in den PDF-Report aufgenommen (Report jetzt 13 statt 12 Seiten):

- **SMA-Stack:** $192,38/$186,87/$154,41 — Golden-Stack intakt (Kurs&gt;20&gt;50&gt;200)
- **RSI(14):** 54,6 (neutral) · **MACD/Signal/Hist:** 1,82/2,23/-0,41 (leicht bearish, flach) · **Bollinger:** $202,45/$192,38/$182,31
- **W1 (Weekly) seit Tief 31.03.2025:** durchgängige Higher-Highs/Higher-Lows — Struktur intakt, kein Bruch
- **Relative Stärke vs. SPY:** 6M +34,2pp, 3M +17,1pp, 1M +0,3pp (flach, keine Verschlechterung)
- **Support/Resistance:** R3 $214,89 / R2 $210-211 / R1 $200-201 / Kurs $197,54 / S1 $186-189 / S2 $181-183 / S3(SMA200) $154,41
- **ATR-Risiko-Modul:** ATR14 $8,22, ATR-20T-Ø $8,65 (leicht rückläufig); Stop-Loss (2×ATR) ~$181,10 deckt sich mit S2/unterem Bollinger; R/R zum 52W-Hoch ~1,05:1
- **Volumen-Bestätigung** (Regel-Umbenennung von "Institutional Footprint", v1.10): OBV letzte 5 Tage (+23,4 Mio.) klar stärker als die 5 Tage davor (+9,6 Mio.) → Kursanstieg volumen-bestätigt, keine Distributions-Divergenz
- **VETO-Modul:** kein aktives VETO; Formations-Modul [KEINE DATEN] (kein Chart-Pattern-Input vom Nutzer)
- **Technische These-Bruch-Prüfung (NEU, v1.10):** 0/3 Säulen gebrochen → kein Thesis-Break, normale Volatilität
- **TA-Gesamtverdikt:** HALTEN/BEOBACHTEN aus reiner TA-Sicht, Konfidenz 🟢 hoch — überschreibt wie immer nicht die fundamentale TMR-These

Parallel dazu wurden zwei genuine Methodik-Verfeinerungen in `prompts/jack-technical-analyst-v1.9.md` (intern v1.10) umgesetzt: die neue "Technical Thesis Break"-Prüfung sowie eine sprachliche Präzisierung des Institutional-Footprint-Blocks ("Volumen-Bestätigungsmuster"), plus eine explizite TECHNICAL-ANALYSIS-HIERARCHY-Klausel. Siehe CHANGELOG.md für Details.

## Quellen
SEC 10-K FY2025, 10-Q Q2 2026; Microsoft FY26 Q3/Q4 Earnings Calls; Meta Q2 2026 10-Q/Earnings Call; IDC Datacenter-Ethernet-Switching-Report Q1 2026; NVIDIA Spectrum-X Produktseite; SEC Form 4 Filings; Twelve Data (Live-Kurs, Wochenschlusskurse seit 2016); StockAnalysis/TipRanks/Yahoo Finance (Peer-Multiples, Analysten-Konsens).
