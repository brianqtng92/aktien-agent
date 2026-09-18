#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wochenfazit 2026-09-18 -- regulaerer Freitags-Lauf, 1-Tages-Fenster seit dem
Ad-hoc-Wochenfazit vom 17.09. Helles Farbschema gemaess Playbook-Vorgabe
vom 2026-09-07 (gilt fuer ALLE Report-Formate)."""

CSS = """
:root {
  --bg: #FFFFFF; --bg-panel: #F7F6F2; --bg-panel-2: #EFEDE6;
  --border: #D9D4C8; --border-soft: #E6E2D9;
  --text: #262420; --text-dim: #5C564A; --text-faint: #837C6C;
  --gold: #9C7A2E; --gold-bright: #8A6A22; --gold-dim: #C9AD6E;
  --green: #3F7D44; --green-bg: rgba(63,125,68,0.10);
  --yellow: #A6790A; --yellow-bg: rgba(166,121,10,0.10);
  --orange: #B0651E; --orange-bg: rgba(176,101,30,0.10);
  --red: #B03A2E; --red-bg: rgba(176,58,46,0.09);
}
* { box-sizing: border-box; margin:0; padding:0; }
html, body { background: var(--bg); color: var(--text); font-family:"Carlito","DejaVu Sans",Arial,sans-serif; font-size:9.6pt; line-height:1.4; }
.display { font-family:"DejaVu Sans Condensed","DejaVu Sans",Arial,sans-serif; font-weight:700; }
.page { width:210mm; height:297mm; padding:11mm 13mm 8mm 13mm; display:flex; flex-direction:column; gap:3.6mm; page-break-after: always; }
.page:last-child { page-break-after: auto; }
.masthead { display:flex; justify-content:space-between; align-items:flex-end; border-bottom:2px solid var(--gold); padding-bottom:3mm; }
.brand { font-size:24pt; letter-spacing:0.05em; }
.brand .accent { color: var(--gold-bright); }
.brand-sub { font-size:7.8pt; letter-spacing:0.13em; text-transform:uppercase; color:var(--text-dim); margin-top:0.6mm; }
.meta { text-align:right; font-size:8pt; color:var(--text-dim); }
.meta .big { color:var(--text); font-size:10pt; }
.section-label { font-size:7.4pt; letter-spacing:0.13em; text-transform:uppercase; color:var(--gold); display:flex; align-items:center; gap:2.5mm; }
.section-label::after { content:""; flex:1; height:1px; background:var(--border-soft); }
.ampel-box { display:flex; gap:4mm; align-items:center; background:var(--bg-panel); border:1px solid var(--border-soft); border-left:4px solid var(--yellow); border-radius:3px; padding:4mm 5mm; }
.ampel-dot { width:9mm; height:9mm; border-radius:50%; background:var(--yellow); flex-shrink:0; box-shadow:0 0 10px rgba(166,121,10,0.35); }
.ampel-text .status { font-size:14pt; }
.ampel-text .sub { font-size:8.4pt; color:var(--text-dim); margin-top:1mm; }
.cat-grid { display:flex; gap:3mm; }
.cat-card { flex:1; background:var(--bg-panel); border:1px solid var(--border-soft); border-radius:3px; padding:3mm 4mm; }
.cat-card .name { font-size:10pt; color:var(--gold-bright); }
.cat-card .fill { font-size:16pt; margin-top:1mm; }
.cat-card .fill .target { font-size:8pt; color:var(--text-faint); }
.cat-card .note { font-size:7.2pt; color:var(--text-dim); margin-top:1mm; }
.bar-track { height:2.4mm; border-radius:2px; background:var(--border-soft); margin-top:1.6mm; overflow:hidden; }
.bar-fill { height:100%; border-radius:2px; }
.pill { display:inline-block; padding:0.5mm 2.2mm; border-radius:8px; font-size:6.8pt; letter-spacing:0.03em; text-transform:uppercase; }
.pill.green { background:var(--green-bg); color:var(--green); border:1px solid var(--green); }
.pill.yellow { background:var(--yellow-bg); color:var(--yellow); border:1px solid var(--yellow); }
.pill.orange { background:var(--orange-bg); color:var(--orange); border:1px solid var(--orange); }
.pill.red { background:var(--red-bg); color:var(--red); border:1px solid var(--red); }
.tick { color:var(--text-faint); font-size:7.4pt; }
.box { background:var(--bg-panel); border:1px solid var(--border-soft); border-radius:3px; padding:3mm 4mm; }
.box h3 { font-size:8.6pt; text-transform:uppercase; letter-spacing:0.06em; color:var(--gold); margin-bottom:1.4mm; }
.box p { font-size:8pt; color:var(--text-dim); line-height:1.42; }
.box p b { color:var(--text); }
.event-list { display:flex; flex-direction:column; gap:2.4mm; }
.event { display:flex; gap:3mm; background:var(--bg-panel); border:1px solid var(--border-soft); border-radius:3px; padding:2.6mm 3.5mm; }
.event .tag { flex:0 0 24mm; font-size:8.6pt; }
.event .tag .t { display:block; font-size:6.4pt; color:var(--text-faint); text-transform:uppercase; }
.event .body { flex:1; font-size:7.9pt; color:var(--text-dim); line-height:1.4; }
.event .body b { color:var(--text); }
.cash-line { border:1px solid var(--gold-dim); border-radius:3px; padding:3.4mm 4mm; background:linear-gradient(135deg,var(--bg-panel-2),var(--bg-panel)); }
.cash-line .h { color:var(--gold-bright); font-size:9.4pt; margin-bottom:1mm; }
.cash-line p { font-size:8.4pt; color:var(--text); }
.footer { display:flex; justify-content:space-between; border-top:1px solid var(--border-soft); padding-top:1.6mm; font-size:6.2pt; color:var(--text-faint); margin-top:auto; }
.imgbox { text-align:center; }
.imgbox img { max-width:100%; max-height:78mm; border:1px solid var(--border-soft); border-radius:3px; background:#fff; }
.imgbox .cap { font-size:7.4pt; color:var(--text-dim); margin-top:1mm; }
.chart-grid { display:grid; grid-template-columns:1fr 1fr; gap:3mm; }
.src-list { font-size:7.6pt; color:var(--text-dim); line-height:1.7; }
table.simple { width:100%; border-collapse:collapse; font-size:7.8pt; }
table.simple th { text-align:left; text-transform:uppercase; letter-spacing:0.04em; font-size:6.6pt; color:var(--text-faint); border-bottom:1px solid var(--border-soft); padding:1.6mm 2mm; }
table.simple td { padding:1.4mm 2mm; border-bottom:1px solid var(--border-soft); color:var(--text-dim); }
table.simple td b { color:var(--text); }
.up { color:var(--green); } .down { color:var(--red); }
"""

page1 = """
<div class="page">
  <div class="masthead">
    <div>
      <div class="brand display">AGENT <span class="accent">WOCHENREPORT</span></div>
      <div class="brand-sub">3-KI Cross-Check &middot; Aegis &middot; Conan &middot; JJ</div>
    </div>
    <div class="meta">
      <div class="big">Woche zum 18. September 2026</div>
      <div>Gesamtdepot &middot; 15 Einzelwerte + Vanguard-FTSE-All-World-Sparplan + Gold-ETC</div>
    </div>
  </div>

  <div class="box" style="border-left:3px solid var(--gold);">
    <h3>Hinweis zu diesem Lauf</h3>
    <p>Regulärer Freitags-Wochenfazit-Lauf, diesmal mit einem bewusst <b>kurzen 1-Tages-Fenster</b> seit dem Ad-hoc-Wochenfazit vom 17.09.2026 (das bereits ein verlängertes 10-Tage-Fenster nachgeholt hatte). Trotz der Kürze ein inhaltlich dichter Tag: BoJ-Zinsentscheid, Rambus-Preisalarm, CBOE erstmals in der Nachkauf-Zone, und ein deutlicher Rücksetzer bei Hermès auf die dokumentierte Abstauber-Marke. Parallel lief heute auch der reguläre tägliche Trigger-Check (siehe <code>depot/bridge_status.md</code>) — beide Läufe sind über die Dateien synchronisiert, siehe CLAUDE.md &bdquo;Gemeinsames Gedächtnis&ldquo;-Regel.</p>
  </div>

  <div class="section-label">Depotstatus</div>
  <div class="ampel-box">
    <div class="ampel-dot"></div>
    <div class="ampel-text">
      <div class="status display">BEOBACHTEN &mdash; kein akuter Handlungsbedarf</div>
      <div class="sub">Depotwert 33.426,76&nbsp;€ (-0,63% ggü. 17.09., -4,59% ggü. Baseline 30.08. — Depot fällt damit weiter hinter S&amp;P 500/MSCI World zurück, Nasdaq 100 dagegen leicht positiv, siehe Seite 5). Kein struktureller Schaden: der Rückgang dieser Woche ist zu &gt;90% ein einzelner, bereits erwarteter Bewertungseffekt bei Hermès (-14% ggü. Vorwoche, praktisch auf der dokumentierten Nachkauf-Zone), keine neue fundamentale Verschlechterung. Kategorie-Struktur unverändert (10-7-1, Talent weiter unterbesetzt). Zwei Positionen (CBOE, Hermès) haben ihre Nachkauf-Zone diese Woche erstmals bzw. praktisch erreicht — beide OHNE bestätigtes Kaufsignal, da die jeweilige technische Zusatzbedingung noch nicht erfüllt ist (siehe Seite 6).</div>
    </div>
  </div>

  <div class="section-label">Kategorie-Füllstand (Depot-Ziel-Struktur &bdquo;10-7-3&ldquo;)</div>
  <div class="cat-grid">
    <div class="cat-card">
      <div class="name display">CHAMPIONS</div>
      <div class="fill display">10 <span class="target">/ Ziel 10</span></div>
      <div class="bar-track"><div class="bar-fill" style="width:100%; background:var(--green);"></div></div>
      <div class="note">Exakt auf Ziel, unverändert.</div>
    </div>
    <div class="cat-card">
      <div class="name display">PROFI</div>
      <div class="fill display">7 <span class="target">/ Ziel 7</span></div>
      <div class="bar-track"><div class="bar-fill" style="width:100%; background:var(--green);"></div></div>
      <div class="note">Exakt auf Ziel, unverändert.</div>
    </div>
    <div class="cat-card">
      <div class="name display">TALENT</div>
      <div class="fill display">1 <span class="target">/ Ziel 3</span></div>
      <div class="bar-track"><div class="bar-fill" style="width:33%; background:var(--yellow);"></div></div>
      <div class="note">2 Slots weiterhin frei (nur Rocket Lab). Japan-Kandidatenpipeline weiter auf Brians Wunsch pausiert.</div>
    </div>
  </div>

  <div class="section-label">Kernzahlen dieser Woche</div>
  <div class="cat-grid">
    <div class="cat-card"><div class="name">Depotwert</div><div class="fill display" style="color:var(--text);">33.426,76&nbsp;€</div><div class="note">-0,63% ggü. 17.09. (33.639,41€) &middot; -4,59% ggü. Baseline 30.08. Alle 4 Broker live/frisch geprüft.</div></div>
    <div class="cat-card"><div class="name">Watchlist</div><div class="fill display" style="color:var(--gold-bright);">37 Werte</div><div class="note">19 Champions / 13 Profi / 5 Talent, unverändert seit 17.09. Kein neuer Auf-/Abstufungstrigger.</div></div>
    <div class="cat-card"><div class="name">Nachkauf-Zonen erreicht</div><div class="fill display" style="color:var(--orange);">2 (ohne Signal)</div><div class="note">CBOE &amp; Hermès — beide Preis-Zone praktisch erreicht, technische Bestätigung fehlt jeweils noch.</div></div>
  </div>

  <div class="footer">
    <div>Agent Wochenreport &middot; Seite 1</div>
    <div>Regelwerk TMR v11.24 / Scout v1.16</div>
  </div>
</div>
"""

page2 = """
<div class="page">
  <div class="masthead">
    <div><div class="brand display" style="font-size:16pt;">AUFFÄLLIGKEITEN <span class="accent">DIESER WOCHE</span></div>
    <div class="brand-sub">Verdichtet aus dem heutigen Blitz-Scan, Trigger-Check und der eigenen Wochenfazit-Recherche</div></div>
  </div>

  <div class="event-list">
    <div class="event">
      <div class="tag"><span class="t">Hermès</span><b class="display">Nachkauf-Zone</b><br><span class="pill orange">Praktisch erreicht</span></div>
      <div class="body">Kurs fiel auf <b>1.352€</b> (TradingView-Monatschart Brian, live) — ein deutlicher Rücksetzer von -14% ggü. der letzten Bewertung (1.573€ am 08./09.09.) und liegt damit praktisch AUF dem dokumentierten fundamentalen Abstauber-Limit (≤1.350€, RMS-TMR-Quick-Filter 23.08.2026). Rein preisgetrieben (sektorweiter Luxus-Ausverkauf), keine fundamentale Verschlechterung laut JJ+Conan-Schnellanalyse (18.09.). <b>TA-Monatschart-Review (18.09.):</b> Kurs testet die 2022-Konsolidierungszone (~1.350-1.395€) von oben — Konfluenz mit dem fundamentalen Limit, aber Kurs bleibt weit unter dem langfristigen gleitenden Durchschnitt (1.776€), keine bestätigte Stabilisierung (nur eine Kerze). <b>Kein Order-Limit</b>, weiter beobachten.</div>
    </div>
    <div class="event">
      <div class="tag"><span class="t">CBOE</span><b class="display">Nachkauf-Zone</b><br><span class="pill orange">Erstmals erreicht</span></div>
      <div class="body">Kurs erreichte heute erstmals die dokumentierte Tranche-1-Zone ($268-270, Tagesspanne $265,28-271,39, Schluss $269,05/aktuell $269,16). Die technische Zusatzbedingung (RSI&gt;45 ODER MACD-Bodenbildung ODER OBV-Trendwechsel) ist aber weiterhin nicht erfüllt: RSI(14) 36,28 (Twelve Data) — leichte Verbesserung ggü. 33,99 (17.09.), aber klar unter der 45er-Schwelle. <b>Kein Order-Limit.</b> Nur 1 Handelstag in der Zone, keine bestätigte Stabilisierung.</div>
    </div>
    <div class="event">
      <div class="tag"><span class="t">Rambus</span><b class="display">Preisalarm</b><br><span class="pill green">Verarbeitet, kein Signal</span></div>
      <div class="body">Der $75-UP-Preisalarm löste heute (Blitz-Scan, ~05:33 UTC) aus — Kurs $85,87 (+5,48% Tagesbewegung), weiterhin deutlich über der Nachkauf-Zone $68-75. Kein neuer fundamentaler Treiber gefunden, reine Kursstärke-Bestätigung. Alarm ordnungsgemäß in <code>depot/price_alerts_processed.md</code> dokumentiert.</div>
    </div>
    <div class="event">
      <div class="tag"><span class="t">Makro</span><b class="display">BoJ-Zinsentscheid</b><br><span class="pill green">Realisiert, erwartet</span></div>
      <div class="body">Die Bank of Japan hob den Leitzins wie zu ~97% erwartet um 25&nbsp;Bp auf <b>1,25% an (höchster Stand seit 1995, 7-2-Votum)</b> — keine Überraschung (alle 52 befragten Bloomberg-Ökonomen erwarteten den Schritt), Marktreaktion "underwhelming"/dovish statt Schock, Yen sogar leicht schwächer trotz Hike. Damit sind beide diese Woche anstehenden Zentralbank-Termine (Fed 16.09., BoJ 18.09.) realisiert — der bisher hälftig gewertete Zentralbank-Event-Risiko-Punkt im Korrektur-Risiko-Score entfällt beim nächsten vollständigen Neu-Check.</div>
    </div>
    <div class="event">
      <div class="tag"><span class="t">Region</span><b class="display">Europa/UK</b><br><span class="pill yellow">Wieder unterbesetzt</span></div>
      <div class="body">Der Hermès-Rücksetzer drückt die Region Europa/UK knapp aus dem Zielband: 15,54% (17.09., im Zielband) → <b>14,98%</b> (18.09., wieder knapp unterbesetzt). Reiner Bewertungseffekt einer bestehenden Position, keine neue strukturelle Lücke — siehe Seite 4 für den vollständigen Portfolio-Regel-Check.</div>
    </div>
    <div class="event">
      <div class="tag"><span class="t">Prozess</span><b class="display">Rigor-Punkte 55-57</b><br><span class="pill green">Umgesetzt</span></div>
      <div class="body">Punkt 55 (Szenariomodell statt DCF bei TMR-Ramp-up-Fällen) direkt im JJ-Prompt umgesetzt (v11.23→v11.24). Neu: Punkt 56 (Thesis Dependency Map) und 57 (&bdquo;die 3 nächsten Infos&ldquo; aus der Unknown-Liste priorisieren). Danach bewusste Pause bei weiteren Regel-Ergänzungen (ChatGPTs eigene Mahnung vor &bdquo;Regelmonster&ldquo;) — Details siehe <code>Agent-Playbook.md</code>, Abschnitt 8.</div>
    </div>
  </div>

  <div class="footer">
    <div>Agent Wochenreport &middot; Seite 2</div>
    <div>Quelle: depot/bridge_status.md, offene_empfehlungen.md, price_alerts_processed.md, WebSearch (BoJ)</div>
  </div>
</div>
"""

page3 = """
<div class="page">
  <div class="masthead">
    <div><div class="brand display" style="font-size:16pt;">WATCHLIST-UPDATE</div>
    <div class="brand-sub">37 Werte &middot; Champions/Profi/Talent-Logik wie im Depot &middot; volle Liste in watchlist.md</div></div>
    <div class="meta"><div class="big">19 / 13 / 5</div></div>
  </div>

  <div class="box">
    <h3>Watchlist unverändert diese Woche</h3>
    <p>Die kanonische Watchlist (<code>watchlist.md</code>, Obergrenze 50) bleibt strukturell unverändert bei 37 Werten (19 Champions / 13 Profi / 5 Talent) — keine Auf-/Abstufung, keine Neuaufnahme, kein Ausschluss seit dem letzten Wochenfazit (17.09.). Der tägliche Watchlist-News-Ampel-Check (Trigger-Check, 18.09.) fand keine neuen 🔴/🟡-Funde bei den bereits bekannten Flags (MPWR: nur neutrale/positive News — Dividende + GlobalFoundries-Partnerschaft; FICO: VantageScore-Regulatorik bereits bekannt/eingepreist; SYK/WSO: keine neuen Funde). &bdquo;Watchlist unverändert diese Woche&ldquo; ist laut Playbook ein vollwertiges Ergebnis.</p>
  </div>

  <div class="box">
    <h3>Japan-Kandidatenpipeline weiterhin pausiert</h3>
    <p>Die am 08.09. gefundenen 10 Kandidatennamen (Sansan, Smaregi, VRAIN Solution, Shin-Etsu Chemical, Park Systems, OBIC, GMO Payment Gateway, eGuarantee, SMC Corp, AirTAC International) bleiben auf Brians ausdrücklichen Wunsch (17.09., Yen-Carry-Trade-Sorge) unbearbeiteter Backlog — kein neuer Rechercheauftrag diese Woche. Stattdessen bleibt der Fokus auf den bereits bekannten Japan-Watchlist-Werten mit hergeleiteten Zielzonen (Hoya €92-106, Disco €159-187 — beide Kurse weiterhin klar darüber, kein Nachkaufpunkt).</p>
  </div>

  <div class="section-label">Offene Nachkauf-/Beobachtungs-Zonen (Watchlist, unverändert)</div>
  <table class="simple">
    <tr><th>Ticker</th><th>Firma</th><th>Einordnung</th></tr>
    <tr><td><b>7741</b></td><td>Hoya Corp.</td><td>Kurs weiterhin deutlich über der hergeleiteten Zielzone (€92-106) — kein Nachkaufpunkt.</td></tr>
    <tr><td><b>6146</b></td><td>Disco Corp.</td><td>Kurs weiterhin deutlich über der hergeleiteten Zielzone (€159-187) — kein Nachkaufpunkt.</td></tr>
    <tr><td><b>7747</b></td><td>Asahi Intecc</td><td>Grundsätzlich attraktiv laut letzter Analyse, kein frischer Quick-Filter diese Woche — Preisalarm bei ¥16.000 aktiv (Scalable, unverändert).</td></tr>
  </table>
  <div class="box"><p><b>Watsco/Rollins/FICO-Beobachtungspunkte</b> (Margen-Normalisierung, H2-Guidance, VantageScore-Adoption) bleiben unverändert offen — keine neuen Daten diese Woche, siehe <code>master_status.md</code> Abschnitt 5.</p></div>

  <div class="footer">
    <div>Agent Wochenreport &middot; Seite 3</div>
    <div>Vollständige Liste inkl. Kurzthesen: watchlist.md</div>
  </div>
</div>
"""

page4 = """
<div class="page">
  <div class="masthead">
    <div><div class="brand display" style="font-size:16pt;">PORTFOLIO-REGEL-CHECK</div>
    <div class="brand-sub">Frische Live-Zahlen (18.09.) &middot; Regelverstöße klar benannt</div></div>
  </div>

  <table class="simple">
    <tr><th>Regel</th><th>Ziel</th><th>Ist (18.09.)</th><th>Status</th></tr>
    <tr><td>Größte Einzelposition</td><td>≤10% (Ausnahme bis 12%)</td><td><b>SoFi Technologies 11,04%</b></td><td><span class="pill orange">INNERHALB AUSNAHME</span></td></tr>
    <tr><td>ETF-Mindestanteil</td><td>≥50% (Ziel langfr. 60%)</td><td><b>24,41%</b></td><td><span class="pill red">VERSTOSS, langsamer Aufbau</span></td></tr>
    <tr><td>Region USA</td><td>≤55% (hart ≤60%)</td><td>53,70%</td><td><span class="pill green">ERFÜLLT</span></td></tr>
    <tr><td>Region Europa/UK</td><td>15-20%</td><td>14,98%</td><td><span class="pill orange">WIEDER KNAPP UNTERBESETZT (war im Zielband)</span></td></tr>
    <tr><td>Region Japan/Asien</td><td>10-15%</td><td>9,55%</td><td><span class="pill orange">UNTERBESETZT</span></td></tr>
    <tr><td>Region Sonstige (CA/IL)</td><td>kein festes Band</td><td>17,00%</td><td><span class="pill yellow">HINWEIS</span></td></tr>
    <tr><td>Region LatAm</td><td>kein festes Band</td><td>4,77% (MercadoLibre)</td><td><span class="pill green">OK</span></td></tr>
    <tr><td>Sektor Finanzwesen</td><td>20-25%</td><td><b>32,71%</b></td><td><span class="pill red">WEITERHIN KLAR ÜBER ZIEL</span></td></tr>
    <tr><td>Sektor Technologie/Halbleiter</td><td>30-35%</td><td>29,93%</td><td><span class="pill orange">KNAPP UNTERBESETZT</span></td></tr>
    <tr><td>Sektor Rest</td><td>5-10%</td><td><b>16,41%</b></td><td><span class="pill red">ÜBER ZIELBAND</span></td></tr>
    <tr><td>Sektor Industriewerte</td><td>10-15%</td><td>11,72%</td><td><span class="pill green">IM ZIELBAND</span></td></tr>
    <tr><td>Sektor Gesundheitswesen</td><td>10-15%</td><td>9,23%</td><td><span class="pill orange">UNTERBESETZT</span></td></tr>
  </table>

  <div class="box">
    <h3>Einordnung</h3>
    <p><b>Einzige echte Statusänderung ggü. 17.09.: Europa/UK ist aus dem Zielband gerutscht</b> (15,54%→14,98%) — ausschließlich der Hermès-Preisrückgang (-14% diese Woche), keine neue strukturelle Ursache. Sobald sich Hermès stabilisiert oder ein neuer Europa/UK-Kandidat aufgenommen wird, dürfte sich das wieder normalisieren. <b>SoFi (11,04%, leicht gestiegen von 10,89%)</b> bleibt innerhalb der 12%-Ausnahme. <b>Finanzwesen (32,71%) und &bdquo;Rest&ldquo; (16,41%)</b> bleiben strukturell über ihrem Band — dieselbe strukturelle Situation wie in den Vorwochen, kein neuer Einzelbefund. <b>Gesundheitswesen (9,23%) und Japan/Asien (9,55%)</b> bleiben die am stärksten unterrepräsentierten Töpfe — die Japan-Kandidatenpipeline zur Schließung dieser Lücke bleibt auf Brians Wunsch pausiert (siehe Seite 3).</p>
  </div>

  <div class="footer">
    <div>Agent Wochenreport &middot; Seite 4</div>
    <div>Basis: ETF+Aktien (32.926,34€) für Region/Sektor, Gesamtportfolio inkl. Gold+Cash (33.426,76€) für Positionsgrößen</div>
  </div>
</div>
"""

page5 = """
<div class="page">
  <div class="masthead">
    <div><div class="brand display" style="font-size:16pt;">CHARTS <span class="accent">&amp; MARKT-VERGLEICH</span></div>
    <div class="brand-sub">Frisch erzeugt mit den aktuellen Daten (Stand 18.09.2026)</div></div>
  </div>
  <div class="chart-grid">
    <div class="imgbox"><img src="chart_zusammensetzung.png"><div class="cap">Gesamt-Zusammensetzung (32.926,34€ Einzelwerte+ETF, ohne Gold/Cash)</div></div>
    <div class="imgbox"><img src="chart_regionen.png"><div class="cap">Regionen-Verteilung &mdash; Europa/UK wieder knapp unter Ziel (Hermès-Rücksetzer)</div></div>
    <div class="imgbox"><img src="chart_sektoren.png"><div class="cap">Sektor-Verteilung &mdash; Finanzwesen &amp; Rest weiterhin über Ziel</div></div>
    <div class="imgbox"><img src="chart_rendite.png"><div class="cap">Rendite je Position seit Kauf</div></div>
  </div>
  <div class="imgbox" style="margin-top:2mm;"><img src="benchmark_vs_depot.png" style="max-height:70mm;"><div class="cap">Depot vs. Markt seit Trackingbeginn (30.08.2026) &mdash; Depot -4,59%, S&amp;P 500 -1,69%, Nasdaq 100 +0,31%, MSCI World Proxy -0,76%. Depot fällt diese Woche weiter zurück (primär Hermès-Rücksetzer, siehe Rendite-Chart) &mdash; MSCI-World-Proxy-Wert konnte diesmal nicht frisch abgerufen werden (kein sauberer EUR-Kurs per WebSearch auffindbar), Stand 17.09. fortgeschrieben; S&amp;P/Nasdaq-Proxy-Werte aus SPY/QQQ-Live-Kursen abgeleitet (kein sauberer Tagesschluss-Einzelwert per WebSearch auffindbar).</div></div>
  <div class="footer">
    <div>Agent Wochenreport &middot; Seite 5</div>
    <div>reports/weekly_charts.py &amp; benchmark_chart.py, für diesen Lauf neu ausgeführt</div>
  </div>
</div>
"""

page6 = """
<div class="page">
  <div class="masthead">
    <div><div class="brand display" style="font-size:15pt;">TOP-BEWEGER <span class="accent">&amp; EXIT-/NACHKAUF-AMPEL</span></div>
    <div class="brand-sub">Depot-Einzelwerte mit frischen Kursen (18.09. vs. 17.09.) &middot; Watchlist nicht einzeln abgefragt (Kostengründe, siehe Hinweis unten)</div></div>
  </div>

  <div class="section-label">Top 3 Gewinner / Top 3 Verlierer (Depot, seit 17.09.)</div>
  <table class="simple">
    <tr><th>Position</th><th>Bewegung</th><th>Grund</th></tr>
    <tr><td><b>Rambus (Depot)</b></td><td class="up">+5,6%</td><td>Preisalarm $75 UP ausgelöst, keine fundamentale News — reine Kursstärke</td></tr>
    <tr><td><b>Intuitive Surgical (Depot)</b></td><td class="up">+2,8%</td><td>Kein klarer Einzelgrund identifiziert — allgemeine Kurserholung</td></tr>
    <tr><td><b>Cellebrite DI (Depot)</b></td><td class="up">+1,9%</td><td>Kein klarer Einzelgrund identifiziert</td></tr>
    <tr><td><b>Hermès (Depot)</b></td><td class="down">-14,1%</td><td>Sektorweiter Luxus-Ausverkauf, Kurs erreicht dokumentiertes Abstauber-Limit</td></tr>
    <tr><td><b>ServiceNow (Depot)</b></td><td class="down">-2,1%</td><td>Kein klarer Einzelgrund identifiziert — allgemeine Marktbewegung</td></tr>
    <tr><td><b>Broadridge (Depot)</b></td><td class="down">-1,9%</td><td>Kein klarer Einzelgrund identifiziert</td></tr>
  </table>
  <div class="box" style="margin-top:-1mm;"><p><b>Transparenz-Hinweis:</b> bei einem 1-Tages-Fenster wurden diese Woche nur die 15 Depot-Einzelwerte mit frisch abgerufenen Kursen verglichen, nicht das gesamte 37-Werte-Watchlist-Universum (Twelve-Data-Rate-Limit + Kostenpriorität) — Vollständigkeitsanspruch entsprechend eingeschränkt, siehe Playbook &bdquo;Top-3-Gewinner/-Verlierer&ldquo;.</p></div>

  <div class="section-label">Exit-/Gewinnmitnahme-/Nachkauf-Ampel (alle offenen Zonen)</div>
  <div class="event-list">
    <div class="event">
      <div class="tag"><span class="t">RMS</span><b class="display">Champions</b><br><span class="pill orange">Zone praktisch erreicht</span></div>
      <div class="body">Kurs 1.352€, praktisch auf dem Abstauber-Limit ≤1.350€. Technische Konfluenz mit der 2022-Zone, aber keine bestätigte Stabilisierung. Kein Order-Limit — weiter beobachten, nächste Prüfung bei einer Monatskerze, die hält.</div>
    </div>
    <div class="event">
      <div class="tag"><span class="t">CBOE</span><b class="display">Champions</b><br><span class="pill orange">Zone erstmals erreicht</span></div>
      <div class="body">Kurs $269,16 in der Tranche-1-Zone ($268-270), RSI(14) 36,28 weiterhin unter der 45er-Bestätigungsschwelle. Kein Order-Limit. Tranche 2 bei $255-262 unverändert offen.</div>
    </div>
    <div class="event">
      <div class="tag"><span class="t">RMBS</span><b class="display">Offene Zone</b><br><span class="pill green">Nachkauf-Zone, fern</span></div>
      <div class="body">Preisalarm $75 UP heute ausgelöst und verarbeitet — Kurs $85,87 weiterhin deutlich über der Nachkauf-Zone $68-75, kein Kaufsignal.</div>
    </div>
    <div class="event">
      <div class="tag"><span class="t">KRKN</span><b class="display">Offene Zone</b><br><span class="pill green">Nachkauf-Zone, fern</span></div>
      <div class="body">Zone ≤2,80 CAD unverändert offen seit 01.09.2026, kein frischer Kurs diese Woche (TSXV weiterhin nicht per Twelve Data abrufbar).</div>
    </div>
    <div class="event">
      <div class="tag"><span class="t">ATEN / RKLB</span><b class="display">Profi / Talent</b><br><span class="pill red">Kein Nachkauf</span></div>
      <div class="body">A10 Networks (überbewertet nach Full Deep Dive) und Rocket Lab (Terminal-State, 0% Sizing) unverändert — keine neuen Trigger diese Woche.</div>
    </div>
  </div>

  <div class="box">
    <h3>Umschichtungs-Prüfung</h3>
    <p>Keine Position steht aktuell in Kategorie 4 (Teilverkauf) oder 5 (Verkauf erwägen) — kein Umschichtungs-Kandidat. Unverändert seit 17.09.</p>
  </div>

  <div class="footer">
    <div>Agent Wochenreport &middot; Seite 6</div>
    <div>Vollständige offene Empfehlungen: depot/offene_empfehlungen.md</div>
  </div>
</div>
"""

page7 = """
<div class="page">
  <div class="masthead">
    <div><div class="brand display" style="font-size:15pt;">MAKRO-AUSBLICK <span class="accent">&amp; KLARE LINIE</span></div>
    <div class="brand-sub">Notenbank-Kalender, Investitionsklima, Fokus für die kommende Woche</div></div>
  </div>

  <div class="box">
    <h3>Notenbank-Doppelwoche abgeschlossen</h3>
    <p>Beide für September anstehenden Zentralbank-Entscheidungen sind jetzt realisiert und waren beide vollständig eingepreist: <b>Fed</b> hob am 16.09. um 25 Bp auf 3,75-4,00% an (12-0, erste Anhebung seit 2023), <b>BoJ</b> hob am 18.09. um 25 Bp auf 1,25% an (7-2, höchster Stand seit 1995). Beide Male keine Überraschung, beide Male eine eher ruhige statt geschockte Marktreaktion. Tagesniveau heute: VIX ~15,4 (rückläufig), Fear&amp;Greed 28,7 (Fear-Zone, unverändert), SPY -0,19%/QQQ +0,32% — kein Material Shift. Der Korrektur-Risiko-Score stand zuletzt (17.09.) bei ~48/126 (🟡 ERHÖHT, 38,1%) mit einem hälftig gewerteten Zentralbank-Event-Punkt; mit beiden Terminen jetzt realisiert entfällt dieser Sonderfall beim nächsten vollständigen Neu-Check (noch nicht durchgeführt in diesem Lauf).</p>
  </div>

  <div class="box">
    <h3>Nächste Kalendertermine</h3>
    <p>Keine weiteren FOMC-/EZB-/BoJ-Termine in den nächsten 4 Wochen (nächste: FOMC 27./28.10., EZB 28./29.10., BoJ 29./30.10.). Q3-Earnings-Season beginnt Mitte Oktober — relevante Depot-Termine: Rambus (02.11.), ServiceNow (~28.10.), Cellebrite (18.11.), siehe <code>depot/earnings_calendar.md</code>.</p>
  </div>

  <div class="cash-line">
    <div class="h display">KLARE LINIE FÜR DIE KOMMENDE WOCHE</div>
    <p>Champions und Profi bleiben beide exakt auf Ziel (10/10, 7/7) — kein Bedarf für eine komplett neue Position. Zwei Positionen haben diese Woche ihre Nachkauf-Zone praktisch erreicht (CBOE, Hermès), aber <b>keine trägt ein bestätigtes Kaufsignal</b> — bei beiden fehlt die technische Zusatzbedingung (RSI/Stabilisierung). Kein Grund für eine impulsive Order, aber beide verdienen tägliche Beobachtung in der kommenden Woche (die tägliche Trigger-Check-Automatisierung deckt das ab). Bank Central Asia bleibt der naheliegendste bereits laufende Nachkauf-Fokus (ROE 24%, klar unterbewertet, adressiert direkt die unterbesetzte Japan/Asien-Region) — kein neuer Kurs-Trigger diese Woche. Kraken Robotics und HawkEye 360 bleiben laut Brians eigener Festlegung &bdquo;erstmal voll&ldquo;.<br><br>
    Strukturell bleibt der <b>ETF-Anteil</b> (24,41%, weiter unter der 50%-Untergrenze, aber langsam steigend) der auffälligste Punkt, dazu die Übergewichtung Finanzwesen/Rest und die neu wieder unterbesetzte Region Europa/UK (reiner Bewertungseffekt, siehe Seite 4). <b>Nicht auf Teufel komm raus investieren — wenn nichts klar überzeugt, bleibt das Geld Cash.</b> Diese Woche brachte keinen neuen, zeitkritischen Kauf-Anlass — zwei Beobachtungspunkte (CBOE/Hermès) verdienen aber besondere Aufmerksamkeit in den nächsten Tagen.</p>
  </div>

  <div class="footer">
    <div>Agent Wochenreport &middot; Seite 7</div>
    <div>Keine Anlageberatung &middot; alle Einschätzungen sind Entscheidungsunterstützung, keine Order-Empfehlung</div>
  </div>
</div>
"""

page8 = """
<div class="page">
  <div class="masthead">
    <div><div class="brand display" style="font-size:15pt;">METHODIK <span class="accent">&amp; QUELLEN</span></div></div>
  </div>
  <div class="box">
    <h3>Methodik-Hinweise</h3>
    <p>Dieser Lauf deckt bewusst ein <b>kurzes 1-Tages-Fenster</b> (17.09.-18.09.2026) ab — der reguläre Freitags-Turnus, nachdem das vorherige Wochenfazit (17.09., Donnerstag) bereits ein verlängertes 10-Tage-Fenster nachgeholt hatte. Positionsgrößen-Prozente auf Basis Gesamtportfolio inkl. Gold-ETC und Cash (33.426,76€, alle 4 Broker, frisch geprüft). Region-/Sektor-Prozente auf Basis ETF+Aktien (32.926,34€, ohne Gold/Cash). Benchmark-Vergleich ist Vorwärts-Tracking ohne Währungsbereinigung (siehe depot/performance_tracking.md) — S&amp;P-500-/Nasdaq-100-Proxywerte diesmal aus SPY-/QQQ-Live-Kursen linear skaliert (Kalibrierungsfaktor aus der 17.09.-Zeile), da kein sauberer Tagesschluss-Einzelwert per WebSearch auffindbar war; MSCI-World-Proxy blieb mangels frischem EUR-Kurs auf dem 17.09.-Stand stehen — beide Abweichungen transparent in der performance_tracking.md-Zeile vermerkt. CRV-Ampel-Urteile sind stets eigene Herleitung aus KGV/Wachstum/Marge-Logik bzw. KBV/ROE bei Banken/Versicherern, externe Quellen dienen nur als Rohdaten.</p>
  </div>
  <div class="box">
    <h3>Primärquellen dieses Laufs</h3>
    <p class="src-list">
      Scalable Capital MCP (Live-Portfoliodaten, Cash, Transaktionen, Preisalarme) &middot; Twelve Data (Kurse SOFI/NOW/MELI/CBOE/BR/RMBS/ATEN/ISRG/CLBT/RKLB/HAWK, RSI(14) CBOE, EUR/USD) &middot; TradingView-Monatschart (Hermès, Brian direkt) &middot; WebSearch (BoJ-Zinsentscheid, S&amp;P 500/Nasdaq-100-Stand) &middot; depot/kategorisierung.md, watchlist.md, depot/master_status.md, depot/macro_context.md, depot/offene_empfehlungen.md, depot/performance_tracking.md, depot/price_alerts_processed.md, depot/bridge_status.md (Log des heutigen Trigger-Checks).
    </p>
  </div>
  <div class="box">
    <h3>Rechtlicher Hinweis</h3>
    <p>Dieser Report ist Recherche-/Entscheidungsunterstützung für Brians eigene manuelle Anlageentscheidung, keine regulierte Anlageberatung. Keine erfundenen exakten Wahrscheinlichkeiten (No-False-Precision-Prinzip). Alle Kauf-/Verkaufsorders werden ausschließlich manuell durch Brian ausgeführt.</p>
  </div>
  <div class="footer">
    <div>Agent Wochenreport &middot; Seite 8</div>
    <div>Ende des Reports</div>
  </div>
</div>
"""

html = f"""<!DOCTYPE html>
<html lang="de"><head><meta charset="UTF-8"><title>Agent Wochenreport</title>
<style>@page {{ size:A4; margin:0; }} {CSS}</style></head>
<body>
{page1}
{page2}
{page3}
{page4}
{page5}
{page6}
{page7}
{page8}
</body></html>
"""

with open("reports/Wochenfazit-2026-09-18.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Wochenfazit-2026-09-18.html geschrieben, 8 Seiten.")
