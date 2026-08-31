#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reaper Wochenreport generator - 2026-08-28"""

POSITIONS = [
    # ticker, name, kategorie, pfad, rating, rating_class, score, tier, konf_color, konf_label, abstauber, haupttreiber, rang
    ("6861", "Keyence Corp.", "Champions", "TMR", "BEOBACHTEN", "yellow", 6, 3, "red", "ROT", "¥65.000", "Weltklasse-Compounder (83% Bruttomarge, Netto-Cash), aber KGV 39x zu ambitioniert und Konfidenz-Deckel durch Einzelquellen.", "B"),
    ("8001", "Itochu Corp.", "Champions", "TMR", "BEOBACHTEN", "yellow", 4, 3, "red", "ROT", "¥1.850", "DNA-Gate-Abbruch (K 1/5) unter Standard-Schwellen — Moat/Bewertung nicht schwach genug für FINGER WEG.", "C"),
    ("ALV", "Allianz SE", "Champions", "TMR", "BEOBACHTEN", "yellow", 6, 3, "red", "ROT", "€410", "Struktureller Top-Versicherer mit Rekordkapitalausstattung, aber Bewertung nahe Allzeithoch ohne Sicherheitsmarge.", "B"),
    ("AMZN", "Amazon", "Champions", "TMR", "BEOBACHTEN", "yellow", 4, 3, "red", "ROT", "$220", "DNA-Gate-Abbruch (ROIC<WACC, negative FCF-Marge) in selbstgewählter Mega-Capex-Phase — Moat bleibt intakt.", "C"),
    ("ATEN", "A10 Networks", "Profi", "TMR", "SCHROTT", "red", 2, None, "red", "ROT", "n/a — kein Nachkauf", "DNA-Abbruch (4/5 K-Fails) + aktives Kundenkonzentrations-Flag bei teurer Bewertung ggü. schwacher Kapitalrendite.", "E"),
    ("BBCA", "Bank Central Asia", "Profi", "TMR", "KAUFEN", "green", 6, 3, "red", "ROT", "bereits im Kaufbereich", "Erstklassiges EM-Bank-Profil (ROE 22%, DNA 4/4), Score/Sizing hart gedeckelt durch Einzelquellen-Konfidenz + EM-Länderrisiko.", "A"),
    ("BR", "Broadridge Financial", "Champions", "TMR", "BEOBACHTEN", "yellow", 5, 3, "red", "ROT", "$170", "Exzellenter Moat/ROIC vs. K-Lücke bei ROIC trotz sonst starker Qualität — Grenzfall/Spekulation-Band.", "C"),
    ("CBOE", "CBOE Holdings", "Champions", "TMR", "KAUFEN", "green", 6, 3, "red", "ROT", "bereits im Kaufbereich", "Sauberster K/E-Pass der Serie trifft strukturell einzigartigen Moat + faire Bewertung — nur Konfidenz-Deckel bremst.", "A"),
    ("CSU", "Constellation Software", "Champions", "TMR", "BEOBACHTEN", "yellow", 4, 3, "red", "ROT", "CAD 2.600", "K-Kriterien am Grenzfall (Op.-Leverage-Fail) trotz solidem Moat und starkem Kapitalallokations-Track-Record.", "C"),
    ("CTAS", "Cintas Corp.", "Champions", "TMR", "BEOBACHTEN", "yellow", 6, 2, "yellow", "GELB", "~$180", "Exzellenter Moat/ROIC vs. strukturelle K-/E-Lücken (FCF-Marge) + hohe Bewertung + offene M&A-Antitrust-Unsicherheit.", "B"),
    ("GOOGL", "Alphabet A", "Champions", "TMR", "BEOBACHTEN", "yellow", 6, 3, "red", "ROT", "$290", "Exzellente Kapitalrendite/Bilanz vs. capex-bedingt gebrochene FCF-Metrik + Datenlücken dieser Session.", "B"),
    ("GRAB", "Grab Holdings", "Talent", "SCOUT", "BEOBACHTEN-SPEKULATIV", "yellow", 6, None, "yellow", "GELB", "&lt;$3,00 + 2 Upgrade-Trigger", "Etablierter SEA-Super-App-Champion mit Banklizenz-Moat, aber Hype-Strike + ungeklärte GoTo-Fusion + Insider-Verkäufe.", "D"),
    ("HAWKEYE360", "HawkEye 360", "Talent", "SCOUT", "BEOBACHTEN-SPEKULATIV", "yellow", 6, None, "yellow", "GELB", "deutlich unter $20,70, nur Trace", "Starkes, beschleunigendes Umsatzwachstum + Regierungskunden, aber Skalierungsfrage + Gründer-Score ungeprüft.", "D"),
    ("INTU", "Intuit Inc.", "Champions", "TMR", "BEOBACHTEN", "yellow", 6, 3, "red", "ROT", "$340", "Starke, aber nur einzelquellen-verifizierte DNA + zwei bevorstehende Binär-Katalysatoren (Q4-Zahlen diese Woche berichtet, gemischt).", "B"),
    ("ISRG", "Intuitive Surgical", "Champions", "TMR", "BEOBACHTEN", "yellow", 6, 3, "red", "ROT", "$330", "Solide DNA trifft frischen Doppel-Angriff auf den Kern-Burggraben (Regulierungsmonopol-Ende + Kartellrechts-Rückschlag 13.08.).", "B"),
    ("MELI", "MercadoLibre", "Champions", "TMR", "BEOBACHTEN", "yellow", 4, 3, "red", "ROT", "$1.700", "4 von 5 K-Kriterien verfehlt durch bewusste margin-komprimierende Wachstumsinvestition, nicht durch Moat-Erosion.", "C"),
    ("MUV2", "Münchener Rück", "Champions", "TMR", "BEOBACHTEN", "yellow", 6, 3, "red", "ROT", "€470", "Exzellente Kapitalausstattung und Zeichnungsdisziplin, aber zyklischer Rückversicherungs-Preisdruck ohne Sicherheitsmarge.", "B"),
    ("NTSK", "Netskope", "Talent", "SCOUT", "BEOBACHTEN-SPEKULATIV", "yellow", 4, None, "yellow", "GELB", "Moat-Deckel greift, kein Aufbau", "Reale Umsatz-/NRR-Substanz, aber schwacher nachgewiesener Burggraben in hart umkämpftem SASE-Markt.", "D"),
    ("RMBS", "Rambus", "Profi", "TMR", "BEOBACHTEN", "yellow", 5, 3, "red", "ROT", "$75", "Grenzfall/Spekulation-Band — Tier 1/2 durch Konfidenz UND Beta doppelt gesperrt.", "C"),
    ("RMS", "Hermès", "Champions", "TMR", "BEOBACHTEN", "yellow", 7, 2, "yellow", "GELB", "€1.350", "Erstklassiger Moat/ROIC, aber Bewertung nicht fair genug für die 9-10-Bandbreite.", "B"),
    ("SOFI", "SoFi Technologies", "Talent", "SCOUT", "BEOBACHTEN-SPEKULATIV", "yellow", 6, None, "yellow", "GELB", "Trace-Position, kein Aufbau vor Klärung", "Starkes, beschleunigendes Wachstum + Insider-Käufe, aber ungelöster Muddy-Waters-Flag (diese Woche: Ergebnis-Beat trotz Feud).", "D"),
    ("SPGI", "S&P Global", "Champions", "TMR", "BEOBACHTEN", "yellow", 5, 3, "red", "ROT", "$390", "Erstklassiges operatives Geschäft vs. echte DNA-Lücke bei ROIC/EPS-CAGR durch Post-Merger-Goodwill-Last.", "C"),
    ("SYK", "Stryker Corp.", "Champions", "TMR", "BEOBACHTEN", "yellow", 5, 3, "red", "ROT", "$295", "Solider Moat, aber ROIC klar unter 20%-Schwelle + FCF-Marge knapp verfehlt + anspruchsvolle Bewertung (EV/FCF ~29x).", "C"),
    ("TSTL", "Tristel PLC", "Profi", "TMR", "BEOBACHTEN", "yellow", 4, None, "red", "ROT", "360 GBX", "Starke Ertragskennzahlen werden durch schwache Cash-Konvertierung + Kundenkonzentrations-Flag bei CEO-Wechsel überschattet.", "C"),
    ("V", "Visa Inc.", "Champions", "TMR", "KAUFEN", "green", 7, 2, "yellow", "GELB", "bereits im Kaufbereich", "Makelloser DNA-K-Pass (4/4) und starker Moat treffen auf volle Bewertung nahe Allzeithoch.", "A"),
    ("WM", "Waste Management", "Champions", "TMR", "BEOBACHTEN", "yellow", 6, 3, "red", "ROT", "$205", "Starker struktureller Burggraben, aber nur mittelmäßige DNA-Kennzahlen (ROIC&lt;20%) bei ambitionierter Bewertung.", "B"),
    ("NOW", "ServiceNow", "Champions", "TMR", "BEOBACHTEN", "yellow", 6, 3, "red", "ROT", "siehe Vollanalyse", "Exzellente Moat-/Bilanzqualität trifft ungelöste Bewertungs-Methodik-Spannung — diese Woche +29%/1 Monat, BofA hebt PT an.", "B"),
    ("CLBT", "Cellebrite DI", "Talent", "TMR", "SCHROTT", "red", 1, 4, "yellow", "GELB (Widerspruch)", "kein Nachkauf — Exit-These prüfen", "Earnings-Miss/Guidance-Cut (-29%, 13.08.), CEO-Wechsel, Securities-Investigation-Notice — Jarvis SCHROTT vs. Conan/Jack BEOBACHTEN/HALTEN.", "E"),
]

CROSS_CHECK = {"CLBT", "NOW"}  # positions with full 3-way voice data (kept as note, not full gauge grid here)

CSS = """
:root {
  --bg: #1A1C1F; --bg-panel: #232629; --bg-panel-2: #2A2D31;
  --border: #3A3E43; --border-soft: #303337;
  --text: #EDE8DF; --text-dim: #A39B8E; --text-faint: #6E6860;
  --gold: #C6922C; --gold-bright: #E0B24E; --gold-dim: #7A5F24;
  --green: #5C9A5F; --green-bg: rgba(92,154,95,0.14);
  --yellow: #DDB13B; --yellow-bg: rgba(221,177,59,0.14);
  --red: #BC4F41; --red-bg: rgba(188,79,65,0.16);
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
.section-title { font-size:11pt; letter-spacing:0.03em; color:var(--gold-bright); margin-bottom:1mm; }
.section-label { font-size:7.4pt; letter-spacing:0.13em; text-transform:uppercase; color:var(--gold); display:flex; align-items:center; gap:2.5mm; }
.section-label::after { content:""; flex:1; height:1px; background:var(--border-soft); }
.ampel-box { display:flex; gap:4mm; align-items:center; background:var(--bg-panel); border:1px solid var(--border-soft); border-left:4px solid var(--yellow); border-radius:3px; padding:4mm 5mm; }
.ampel-dot { width:9mm; height:9mm; border-radius:50%; background:var(--yellow); flex-shrink:0; box-shadow:0 0 10px rgba(221,177,59,0.5); }
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
table.ranks { width:100%; border-collapse:collapse; font-size:8pt; }
table.ranks th { text-align:left; text-transform:uppercase; letter-spacing:0.05em; font-size:6.8pt; color:var(--text-faint); border-bottom:1px solid var(--border-soft); padding:1.6mm 2mm; }
table.ranks td { padding:1.4mm 2mm; border-bottom:1px solid var(--border-soft); vertical-align:top; }
table.ranks tr:last-child td { border-bottom:none; }
.rang-pill { display:inline-block; width:5mm; height:5mm; line-height:5mm; text-align:center; border-radius:50%; font-size:7.5pt; color:var(--bg); font-weight:bold; }
.pill { display:inline-block; padding:0.5mm 2.2mm; border-radius:8px; font-size:6.8pt; letter-spacing:0.03em; text-transform:uppercase; }
.pill.green { background:var(--green-bg); color:var(--green); border:1px solid var(--green); }
.pill.yellow { background:var(--yellow-bg); color:var(--yellow); border:1px solid var(--yellow); }
.pill.red { background:var(--red-bg); color:var(--red); border:1px solid var(--red); }
.tick { color:var(--text-faint); font-size:7.4pt; }
.box { background:var(--bg-panel); border:1px solid var(--border-soft); border-radius:3px; padding:3mm 4mm; }
.box h3 { font-size:8.6pt; text-transform:uppercase; letter-spacing:0.06em; color:var(--gold); margin-bottom:1.4mm; }
.box p { font-size:8pt; color:var(--text-dim); line-height:1.42; }
.box p b { color:var(--text); }
.event-list { display:flex; flex-direction:column; gap:2.4mm; }
.event { display:flex; gap:3mm; background:var(--bg-panel); border:1px solid var(--border-soft); border-radius:3px; padding:2.6mm 3.5mm; }
.event .tag { flex:0 0 22mm; font-size:8.6pt; }
.event .tag .t { display:block; font-size:6.4pt; color:var(--text-faint); text-transform:uppercase; }
.event .body { flex:1; font-size:7.9pt; color:var(--text-dim); line-height:1.4; }
.event .body b { color:var(--text); }
.cash-line { border:1px solid var(--gold-dim); border-radius:3px; padding:3.4mm 4mm; background:linear-gradient(135deg,var(--bg-panel-2),var(--bg-panel)); }
.cash-line .h { color:var(--gold-bright); font-size:9.4pt; margin-bottom:1mm; }
.cash-line p { font-size:8.4pt; color:var(--text); }
.card-grid { display:grid; grid-template-columns:1fr 1fr; gap:3mm; flex:1; }
.card { background:var(--bg-panel); border:1px solid var(--border-soft); border-radius:3px; padding:2.6mm 3.2mm; display:flex; flex-direction:column; gap:1mm; overflow:hidden; }
.card-top { display:flex; justify-content:space-between; align-items:flex-start; }
.card .ticker { font-size:11pt; }
.card .name { font-size:6.8pt; color:var(--text-faint); }
.card .cat { font-size:6.2pt; color:var(--text-faint); text-transform:uppercase; letter-spacing:0.04em; }
.card .thesis { font-size:7.1pt; color:var(--text-dim); line-height:1.34; flex:1; }
.card .foot { display:flex; justify-content:space-between; align-items:center; font-size:6.6pt; color:var(--text-faint); border-top:1px solid var(--border-soft); padding-top:1mm; margin-top:0.6mm; }
.card .score { font-size:9pt; color:var(--text); }
.footer { display:flex; justify-content:space-between; border-top:1px solid var(--border-soft); padding-top:1.6mm; font-size:6.2pt; color:var(--text-faint); margin-top:auto; }
.src-list { font-size:7.6pt; color:var(--text-dim); line-height:1.7; }
.src-list a, .src-list span.u { color: var(--gold-bright); }
"""

def score_color(c):
    return {"green":"var(--green)","yellow":"var(--yellow)","red":"var(--red)"}[c]

def rang_color(r):
    return {"A":"var(--green)","B":"#7DAE86","C":"var(--yellow)","D":"#C98A4A","E":"var(--red)"}[r]

def rating_pill(cls, label):
    return f'<span class="pill {cls}">{label}</span>'

def card_html(p):
    ticker,name,kat,pfad,rating,rcls,score,tier,konf_c,konf_l,abst,thes,rang = p
    tier_txt = f"Tier {tier}" if tier else "kein Tier"
    return f"""
    <div class="card">
      <div class="card-top">
        <div><span class="ticker display">{ticker}</span><div class="name">{name}</div></div>
        {rating_pill(rcls, rating.replace('-SPEKULATIV',' spek.'))}
      </div>
      <div class="cat">{kat} &middot; {pfad}-Pfad &middot; Rang {rang}</div>
      <div class="thesis">{thes}</div>
      <div class="foot">
        <span class="score" style="color:{score_color(konf_c)}">{score}/10</span>
        <span>{tier_txt}</span>
        <span class="pill {konf_c}">{konf_l}</span>
      </div>
      <div class="foot" style="border-top:none; padding-top:0; margin-top:0;">
        <span>Abstauber/Trigger:</span><span style="text-align:right; max-width:60%;">{abst}</span>
      </div>
    </div>
    """

def rank_row(p):
    ticker,name,kat,pfad,rating,rcls,score,tier,konf_c,konf_l,abst,thes,rang = p
    return f"""<tr>
      <td><span class="rang-pill" style="background:{rang_color(rang)}">{rang}</span></td>
      <td><b class="display">{ticker}</b> <span class="tick">&middot; {name}</span></td>
      <td>{kat}</td>
      <td>{rating_pill(rcls, rating.replace('-SPEKULATIV',' spek.'))}</td>
      <td>{score}/10</td>
      <td>{f"Tier {tier}" if tier else "&mdash;"}</td>
      <td><span class="pill {konf_c}">{konf_l}</span></td>
    </tr>"""

CHAMPIONS = [p for p in POSITIONS if p[2]=="Champions"]
PROFI = [p for p in POSITIONS if p[2]=="Profi"]
TALENT = [p for p in POSITIONS if p[2]=="Talent"]
RANG_ORDER = {"A":0,"B":1,"C":2,"D":3,"E":4}
SORTED_ALL = sorted(POSITIONS, key=lambda p: (RANG_ORDER[p[12]], p[0]))

kaufen_count = len([p for p in POSITIONS if p[4]=="KAUFEN"])
schrott_count = len([p for p in POSITIONS if p[4]=="SCHROTT"])

# ---------- PAGE 1: Deckblatt + Ampel + Kategorien ----------
page1 = f"""
<div class="page">
  <div class="masthead">
    <div>
      <div class="brand display">REAPER <span class="accent">WOCHENREPORT</span></div>
      <div class="brand-sub">3-KI Cross-Check &middot; Jarvis &middot; Conan &middot; Jack</div>
    </div>
    <div class="meta">
      <div class="big">Woche zum 28. August 2026</div>
      <div>Gesamtdepot &middot; 28 Einzelwerte + Vanguard-FTSE-All-World-Sparplan</div>
    </div>
  </div>

  <div class="section-label">Depotstatus</div>
  <div class="ampel-box">
    <div class="ampel-dot"></div>
    <div class="ampel-text">
      <div class="status display">BEOBACHTEN &mdash; kein akuter Handlungsbedarf</div>
      <div class="sub">Substanz im Depot überwiegend intakt (nur {schrott_count} von 28 Positionen SCHROTT). Aber: nur {kaufen_count} von 28 Positionen tragen aktuell KAUFEN &mdash; die Mehrheit trägt BEOBACHTEN mit 🔴-Konfidenz-Deckel, primär aus Quick-Filter-Einzelquellen-Limitierung, nicht aus fundamentaler Schwäche. Ein Problemfall (CLBT) verdient diese Woche besondere Aufmerksamkeit &mdash; siehe Auffälligkeiten.</div>
    </div>
  </div>

  <div class="section-label">Kategorie-Füllstand (Depot-Ziel-Struktur)</div>
  <div class="cat-grid">
    <div class="cat-card">
      <div class="name display">CHAMPIONS</div>
      <div class="fill display">{len(CHAMPIONS)} <span class="target">/ Ziel 8&ndash;10</span></div>
      <div class="bar-track"><div class="bar-fill" style="width:100%; background:var(--red);"></div></div>
      <div class="note">Deutlich übervoll &mdash; fast doppelt so viele Positionen wie das Zielband vorsieht. Kein akuter Verkaufsdruck, aber Konzentrationsrisiko im Blick behalten.</div>
    </div>
    <div class="cat-card">
      <div class="name display">PROFI</div>
      <div class="fill display">{len(PROFI)} <span class="target">/ Ziel ~5</span></div>
      <div class="bar-track"><div class="bar-fill" style="width:100%; background:var(--green);"></div></div>
      <div class="note">Knapp im Zielband, ein Slot rechnerisch noch frei &mdash; kein akuter Nachbesetzungsdruck.</div>
    </div>
    <div class="cat-card">
      <div class="name display">TALENT</div>
      <div class="fill display">{len(TALENT)} <span class="target">/ Ziel 3&ndash;5</span></div>
      <div class="bar-track"><div class="bar-fill" style="width:100%; background:var(--yellow);"></div></div>
      <div class="note">Am oberen Rand, voll. Enthält den aktuellen Problemfall CLBT.</div>
    </div>
  </div>

  <div class="section-label">Kernzahlen dieser Woche</div>
  <div class="cat-grid">
    <div class="cat-card"><div class="name">KAUFEN-Signale</div><div class="fill display" style="color:var(--green);">{kaufen_count}</div><div class="note">BBCA, CBOE, V &mdash; alle mit Konfidenz-Deckel, kein Vollgas-Signal.</div></div>
    <div class="cat-card"><div class="name">SCHROTT-Flags</div><div class="fill display" style="color:var(--red);">{schrott_count}</div><div class="note">ATEN (Kandidat, nie gekauft) &middot; CLBT (bestehende Position, Exit-These prüfen).</div></div>
    <div class="cat-card"><div class="name">Ø Konfidenz</div><div class="fill display" style="color:var(--yellow);">mehrheitlich 🔴</div><div class="note">Quick-Filter-Einzelquellen-Limitierung dominiert &mdash; kein fundamentales Warnsignal per se.</div></div>
  </div>

  <div class="footer">
    <div>Reaper Wochenreport &middot; Seite 1</div>
    <div>Regelwerk TMR v11.7 / Scout v1.12 &middot; Quick Filter</div>
  </div>
</div>
"""

# ---------- PAGE 2+3: Gesamtübersicht Ranggruppen A-E (auf 2 Seiten gesplittet, damit nichts überläuft) ----------
RANK_SPLIT = 14
half1 = SORTED_ALL[:RANK_SPLIT]
half2 = SORTED_ALL[RANK_SPLIT:]

def rank_page(chunk, part, pgnum):
    rows = "\n".join(rank_row(p) for p in chunk)
    legend = """
  <div class="cat-grid" style="font-size:7.2pt;">
    <div class="cat-card"><span class="rang-pill" style="background:var(--green)">A</span> Kaufattraktiv jetzt</div>
    <div class="cat-card"><span class="rang-pill" style="background:#7DAE86">B</span> Qualitäts-Kern, Konfidenz/Preis bremst</div>
    <div class="cat-card"><span class="rang-pill" style="background:var(--yellow)">C</span> Grenzfall/DNA-Lücken</div>
    <div class="cat-card"><span class="rang-pill" style="background:#C98A4A">D</span> Spekulativ/früh (Talent)</div>
    <div class="cat-card"><span class="rang-pill" style="background:var(--red)">E</span> Problemfall/Exit-Kandidat</div>
  </div>""" if part == 1 else ""
    return f"""
<div class="page">
  <div class="masthead">
    <div><div class="brand display" style="font-size:16pt;">GESAMTÜBERSICHT <span class="accent">&middot; RANGGRUPPEN A&ndash;E</span></div>
    <div class="brand-sub">Trennt Geschäftsqualität von aktueller Kaufattraktivität &mdash; Querschnitt über Champions/Profi/Talent (Teil {part}/2)</div></div>
    <div class="meta"><div class="big">28 Positionen</div></div>
  </div>
  {legend}
  <table class="ranks">
    <tr><th>Rang</th><th>Position</th><th>Kategorie</th><th>Rating</th><th>Score</th><th>Sizing</th><th>Konfidenz</th></tr>
    {rows}
  </table>
  <div class="footer">
    <div>Reaper Wochenreport &middot; Seite {pgnum}</div>
    <div>Vollständige Analysen: analysen/*.md</div>
  </div>
</div>
"""

page2 = rank_page(half1, 1, 2)
page2b = rank_page(half2, 2, 3)

# ---------- PAGE 3: Auffälligkeiten der Woche ----------
events = [
    ("CLBT", "Problem", "Earnings-Miss + Guidance-Cut für 2026 (<b>-29% am 13.08.</b>), CEO-Wechsel, Securities-Investigation-Notice (Levi &amp; Korsinsky) &mdash; zuletzt (26.08.) Short-Squeeze-Dynamik. Jarvis' <b>SCHROTT</b>-Rating (Score 1/10) bestätigt sich fundamental. Widerspruch mit Conan/Jack (BEOBACHTEN/HALTEN MIT EXIT-FESSEL) bleibt bestehen. <b>Handlungsempfehlung:</b> Exit-These bei nächster Erholung kritisch prüfen, kein Nachkauf."),
    ("NOW", "Positiv", "Aktie <b>+29% im letzten Monat</b>, Bank of America hebt Kursziel an, Management erwartet beschleunigte Subscription-Sales für 2026. Passt zum bereits überwiegend positiven 3-fach-Cross-Check-Bild (Konvergenz moderat positiv, BEOBACHTEN mit Kaufneigung)."),
    ("ISRG", "Ungelöst", "Kartellrechts-Rückschlag vor dem 9th Circuit (13.08., Tying-Vorwurf gegen das Aftermarket-Instrumentengeschäft) bleibt ein aktiver, nicht kurzfristig lösbarer Belastungsfaktor. Aktie weiterhin ca. -33% YTD, Analysten bleiben laut Marktbeobachtung aber langfristig bullish."),
    ("SOFI", "Beobachten", "Muddy-Waters-Short-These weiterhin ungelöst, aber Ergebnis diese Woche (25.08.) mit Umsatz-Beat ($1,1 Mrd.) &mdash; Aktie \"grinds higher\" trotz anhaltendem Bär-Bulle-Tauziehen. Kein Grund für Rating-Änderung, aber weiter beobachten."),
    ("INTU", "Update fällig", "Q4-Zahlen diese Woche berichtet (\"mixed earnings amid slowing growth concerns\") &mdash; dürfte einen der beiden in der Quick-Filter-Analyse genannten Binär-Katalysatoren aufgelöst haben. Empfehlung: Analyse bei Gelegenheit aktualisieren."),
    ("ATEN", "Unauffällig", "A10 Networks hebt operativen Ausblick an (Ziel 10% Jahreswachstum, AI-getriebenes Umsatzwachstum) &mdash; ändert nichts am SCHROTT-Rating (DNA-Abbruch + Kundenkonzentration), aber keine akute Verschärfung. Ein General-Counsel-Insiderverkauf (~$392k) ist routinemäßig, kein Flag."),
]
event_html = "\n".join(f"""
    <div class="event">
      <div class="tag"><span class="t">Position</span><b class="display">{e[0]}</b><br><span class="pill {'red' if e[1]=='Problem' else 'green' if e[1]=='Positiv' else 'yellow'}">{e[1]}</span></div>
      <div class="body">{e[2]}</div>
    </div>""" for e in events)

page3 = f"""
<div class="page">
  <div class="masthead">
    <div><div class="brand display" style="font-size:16pt;">AUFFÄLLIGKEITEN <span class="accent">DER WOCHE</span></div>
    <div class="brand-sub">Nur was sich wirklich bewegt hat &mdash; News-Check der letzten 7 Tage per WebSearch</div></div>
  </div>

  <div class="event-list">
    {event_html}
  </div>

  <div class="cash-line">
    <div class="h display">CASH-DISZIPLIN</div>
    <p>Nichts überzeugt aktuell klar genug für einen Vollangriffs-Kauf &mdash; nur 3 von 28 Positionen (BBCA, CBOE, V) tragen KAUFEN, und alle drei mit Konfidenz-Deckel statt Vollüberzeugung. <b>Nicht auf Teufel komm raus investieren &mdash; wenn nichts klar überzeugt, bleibt das Geld Cash.</b> Bei CLBT gilt das Umgekehrte: keine impulsive Panik-Reaktion, aber die Exit-These aktiv im Blick behalten.</p>
  </div>

  <div class="footer">
    <div>Reaper Wochenreport &middot; Seite 4</div>
    <div>Keine Anlageberatung</div>
  </div>
</div>
"""

# ---------- PAGES 4..: Positionskarten-Raster (6 pro Seite) ----------
CARDS_PER_PAGE = 6
card_pages = []
for i in range(0, len(SORTED_ALL), CARDS_PER_PAGE):
    chunk = SORTED_ALL[i:i+CARDS_PER_PAGE]
    cards_html = "\n".join(card_html(p) for p in chunk)
    pgnum = 5 + i // CARDS_PER_PAGE
    card_pages.append(f"""
<div class="page">
  <div class="masthead">
    <div><div class="brand display" style="font-size:14pt;">POSITIONS-KARTEN <span class="accent">&middot; KOMPAKT</span></div>
    <div class="brand-sub">Rating &middot; Reaper Score &middot; Sizing-Tier &middot; Konfidenz &middot; Abstauber-Trigger &mdash; je Position</div></div>
  </div>
  <div class="card-grid">
    {cards_html}
  </div>
  <div class="footer"><div>Reaper Wochenreport &middot; Seite {pgnum}</div><div>Vollständiges Reaper-Kompakt-Einzelblatt (3-Stimmen-Leiste, Gauge, DNA-Strang) auf Anfrage je Position &mdash; Standard bei Ad-hoc-/Trigger-Analysen</div></div>
</div>
""")

# ---------- METHODIK ----------
last_pgnum = 5 + (len(SORTED_ALL)-1)//CARDS_PER_PAGE
methodik = f"""
<div class="page">
  <div class="masthead">
    <div><div class="brand display" style="font-size:16pt;">METHODIK</div>
    <div class="brand-sub">Wie dieser Report entsteht &mdash; und wo seine Grenzen liegen</div></div>
  </div>

  <div class="box">
    <h3>6 Ampelcheck-Dimensionen</h3>
    <p>Jede Position durchläuft (mind.) eine unabhängige KI-Analyse nach dem TMR- (etablierte/große Titel) oder Scout-Regelwerk (junge/spekulative Titel): <b>DNA-Check</b> (K-Kriterien je Sektor-Override), <b>Moat</b>, <b>Management</b>, <b>Bewertung</b>, <b>Reaper-Reality-Check</b> (Litigation/Kundenkonzentration/Runway/Going-Concern) und eine <b>Daten-Konfidenz-Ampel</b>, die dokumentiert, wie viele Kennzahlen live/verifiziert vs. einzelquellen-/trainingsbasiert sind.</p>
  </div>
  <div class="box">
    <h3>Quick Filter vs. Full Deep Dive</h3>
    <p>Alle Positionen in diesem Wochenreport sind auf <b>Quick-Filter</b>-Tiefe analysiert (kein DCF, keine Zweitquellen-Verifikation jeder Kennzahl) &mdash; das ist der Grund, warum die meisten Positionen bei 🔴/🟡-Konfidenz landen, auch wenn die Fundamentaldaten stark sind. Ein <b>Full Deep Dive</b> (mit echtem DCF und Zweitquellen-Check) kann die Konfidenz auf 🟢 anheben, wurde aber aus Zeit-/Kostengründen nicht für alle 28 Positionen gefahren.</p>
  </div>
  <div class="box">
    <h3>3-fach-Cross-Check: nur bei ausgewählten Positionen</h3>
    <p>NOW, CLBT und SKWD (Nicht-Depot-Kandidat) haben diese Woche bzw. zuletzt einen vollen 3-fach-Cross-Check (Jarvis/Conan/Jack, inkl. Mehrrunden-Diskussion) durchlaufen. Die übrigen 26 Depot-Positionen zeigen aktuell nur Jarvis' Einzelmeinung &mdash; ein 3-fach-Cross-Check lohnt sich gezielt dort, wo eine Kauf-/Verkaufsentscheidung ansteht oder Datenlage kontrovers ist, nicht routinemäßig für das gesamte Depot jede Woche (Kosten-/Zeitgründe).</p>
  </div>
  <div class="box">
    <h3>Bekannte Einschränkungen</h3>
    <p>Keine Steuerprüfung (Kapitalertragsteuer/Quellensteuer bei ausländischen Titeln nicht berücksichtigt). Bei Nicht-US-Titeln (Keyence, Itochu, Hermès, Allianz, Münchener Rück, Constellation Software, Bank Central Asia, Tristel) Fremdwährungsrisiko nicht separat ausgewiesen. Marktabdeckung/Analysten-Konsens kann bei kleineren/nicht-US-Titeln lückenhafter sein als bei US-Large-Caps.</p>
  </div>

  <div class="footer">
    <div>Reaper Wochenreport &middot; Seite {last_pgnum+1}</div>
    <div>Kein Ersatz für individuelle Anlageberatung</div>
  </div>
</div>
"""

# ---------- QUELLEN ----------
quellen = f"""
<div class="page">
  <div class="masthead">
    <div><div class="brand display" style="font-size:16pt;">QUELLEN</div>
    <div class="brand-sub">Diese Woche verwendete Primärquellen (Auswahl, Auffälligkeiten-Recherche)</div></div>
  </div>

  <div class="src-list">
    1. Motley Fool &mdash; "Stock Market Today, Aug. 13: Cellebrite Shares Plummet 29%..." (fool.com)<br>
    2. Yahoo Finance &mdash; "Cellebrite (CLBT): CEO Shift and Guidance Cuts..." (finance.yahoo.com)<br>
    3. PR Newswire &mdash; "Cellebrite DI Ltd. (CLBT) Securities Investigation Notice - Levi &amp; Korsinsky" (prnewswire.com)<br>
    4. Squeeze Report &mdash; "Cellebrite DI Ltd. (NASDAQ:CLBT) Short Squeeze 2026-08-26" (news.squeezereport.com)<br>
    5. TheStreet &mdash; "ServiceNow investors must consider latest alert from Bank of America" (thestreet.com)<br>
    6. 24/7 Wall St. &mdash; "ServiceNow Just Ripped 29% in a Month..." (247wallst.com)<br>
    7. TipRanks &mdash; "SoFi Stock Plunges... Muddy Waters Feud..." (tipranks.com)<br>
    8. Timothy Sykes &mdash; "SOFI Stock Grinds Higher As Earnings Beat Fuels Bull-Bear Tug-Of-War" (timothysykes.com)<br>
    9. GuruFocus &mdash; "Intuit (INTU) Reports Mixed Earnings Amid Slowing Growth Concerns" (gurufocus.com)<br>
    10. Motley Fool &mdash; "Intuitive Surgical (ISRG) Stock Has Plunged 33% in 2026..." (fool.com)<br>
    11. law.justia.com / massdevice.com &mdash; 9th Circuit Kartellrechtsurteil Intuitive Surgical (13.08.2026)<br>
    12. Simply Wall St &mdash; "A10 Networks (ATEN) Lifts Outlook..." (simplywall.st)<br>
    13. Investing.com &mdash; "A10 Networks general counsel sells $392,435 in stock" (investing.com)<br>
    14. Vollständige Einzelanalysen (DNA-Check, Moat, Verdict je Position): <span class="u">analysen/*.md</span> im Projektordner
  </div>

  <div class="box" style="margin-top:auto;">
    <h3>Rechtlicher Hinweis</h3>
    <p>Dieser Report ist eine automatisiert erstellte Analyse-Zusammenfassung für Brian persönlich, <b>keine Anlageberatung</b> im Sinne des WpHG/FinSA. Alle Kauf-/Verkaufs-/Halte-Einschätzungen sind KI-generierte Einschätzungen auf Basis öffentlich zugänglicher Daten, keine Empfehlung eines lizenzierten Finanzberaters. Brian trifft alle Entscheidungen eigenverantwortlich.</p>
  </div>

  <div class="footer">
    <div>Reaper Wochenreport &middot; Seite {last_pgnum+2}</div>
    <div>Ende des Reports</div>
  </div>
</div>
"""

html = f"""<!DOCTYPE html>
<html lang="de"><head><meta charset="UTF-8"><title>Reaper Wochenreport</title>
<style>@page {{ size:A4; margin:0; }} {CSS}</style></head>
<body>
{page1}
{page2}
{page2b}
{page3}
{''.join(card_pages)}
{methodik}
{quellen}
</body></html>
"""

with open("/root/aktien-agent/reports/Wochenfazit-2026-08-28.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Positions:", len(POSITIONS), "Champions:", len(CHAMPIONS), "Profi:", len(PROFI), "Talent:", len(TALENT))
print("Total pages:", 3 + len(card_pages) + 2)
