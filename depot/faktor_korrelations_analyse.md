# Faktor-/Korrelations-Analyse (NEU, 2026-09-09)

**Zweck (aus dem Playbook-Meta-Review, "was fehlt zum professionellen
Fondsmanager" – Punkt 1 der Antwort):** die bestehende Region-/Sektor-
Tabelle in `master_status.md` gruppiert nach klassischen GICS-artigen
Sektoren (Technologie, Finanzwesen, Gesundheitswesen, Industrie, Rest).
Das übersieht Cluster, die QUER über diese Sektoren laufen, aber
tatsächlich vom selben zugrunde liegenden Faktor abhängen – genau die Art
von versteckter Konzentration, die ein professionelles Risikomanagement
über eine Korrelations-/Faktor-Matrix statt reiner Sektor-Etiketten
aufdeckt. Diese Datei ergänzt (ersetzt nicht) die bestehende Region-/
Sektor-Tabelle.

**Datengrundlage:** Positionswerte aus `reports/portfolio_pie_2026-09-08.png`
(Gesamtwert 34.523 €, Scalable live 08.09., übrige Broker Stand 05.09.).
Faktor-Zuordnung ist Jarvis' eigene Einordnung (Geschäftsmodell-Kenntnis
aus den jeweiligen Analysen/`kategorisierung.md`), keine externe
Faktor-Datenbank (die wäre kostenpflichtig, siehe Twelve-Data-
Plan-Entscheidung).

## Gefundene Cluster (Stand 09.09.2026)

### 🔴 Cluster 1: Regierungs-/Verteidigungsbudget-Abhängigkeit — 14,7% des Depots

| Position | Wert | Anteil | Abhängigkeit |
|---|---|---|---|
| Cellebrite DI Ltd | 2.056 € | 6,0% | Strafverfolgungsbehörden weltweit (forensischer Gerätezugriff) |
| HawkEye 360 | 1.494 € | 4,3% | NRO/US-Verteidigung + Verbündete (RF-SIGINT-Satelliten) |
| Kraken Robotics | 958 € | 2,8% | Marine-/Verteidigungskunden (Sonar/Unterwassertechnik) |
| Rocket Lab USA | 553 € | 1,6% | Staatliche + kommerzielle Launch-Aufträge |
| **Summe** | **5.061 €** | **14,7%** | |

**Warum das in der bestehenden Sektor-Tabelle unsichtbar bleibt:** die vier
Positionen verteilen sich über "Industriewerte", "Rest" und "Sonstige" –
auf dem Papier vier verschiedene Sektoren (Forensik-Software, Satelliten-
Intelligence, Marine-Robotik, Raumfahrt). Tatsächlich hängt ihr Umsatz zu
einem erheblichen Teil an DERSELBEN Variable: Regierungs-/
Verteidigungsbudgets (USA + Verbündete). Ein Budget-Einschnitt, ein
Regierungs-Shutdown mit Beschaffungsstopp oder ein politischer
Prioritätenwechsel würde alle vier gleichzeitig treffen, unabhängig von
ihrer jeweiligen Geschäftsqualität.
**Einordnung:** kein akutes Ausschlusskriterium, keine der vier Thesen ist
dadurch beschädigt – aber 14,7% des Depots an einem einzigen politischen
Faktor zu hängen haben, war bisher nicht bewusst gemessen, nur gefühlt
("mehrere Rüstungs-/Behörden-nahe Werte").

### 🟠 Cluster 2: Hochbeta-Kleinkapitalisierer / Risk-on-Risk-off-Sentiment — 11,3% (bzw. 22,8% inkl. SoFi)

| Position | Wert | Anteil |
|---|---|---|
| HawkEye 360 | 1.494 € | 4,3% |
| Kraken Robotics | 958 € | 2,8% |
| Rocket Lab USA | 553 € | 1,6% |
| A10 Networks | 447 € | 1,3% |
| Rambus Inc | 436 € | 1,3% |
| **Summe (ohne SoFi)** | **3.888 €** | **11,3%** |
| SoFi Technologies (separat, da bereits einzeln überwacht) | 3.985 € | 11,5% |
| **Summe inkl. SoFi** | **7.873 €** | **22,8%** |

**Warum relevant:** diese Werte sind fundamental unterschiedlich (Marine-
Robotik, Satelliten, Space-Launch, Netzwerk-Hardware, Halbleiter-IP), aber
alle jung/klein-kapitalisiert genug, um in einer Risk-off-Phase (Zinsangst,
Rezessionssorge, allgemeine Growth-Rotation) gemeinsam überproportional
zu fallen – unabhängig von unternehmensspezifischen News. **Überlappung
mit Cluster 1:** Kraken Robotics, HawkEye 360, Rocket Lab (3.005 €, 8,7%)
gehören zu BEIDEN Clustern – ein Doppel-Treffer-Szenario (Budget-Kürzung
UND Risk-off gleichzeitig) ist nicht rein hypothetisch.

### 🟡 Cluster 3: Zinssensitive Finanzwerte — 10,3%

| Position | Wert | Anteil |
|---|---|---|
| Bank Central Asia | 2.016 € | 5,8% |
| Münchener Rück | 1.031 € | 3,0% |
| Allianz SE | 518 € | 1,5% |
| **Summe** | **3.565 €** | **10,3%** |

Weniger akut als Cluster 1/2 (unterschiedliche Zins-Wirkungsrichtung –
Banken/Rückversicherer profitieren tendenziell EHER von höheren Zinsen
via Float-/Zins-Einkommen, anders als die zinssensitiven Wachstumswerte).
Bereits teilweise über die bestehende "Finanzwesen 33,32% über Zielband"-
Warnung sichtbar, hier nur als eigener Zins-Faktor präzisiert.

### Kein Cluster, aber einzeln schon dokumentiert
A10 Networks' 38%-Microsoft-Konzentration (siehe `kategorisierung.md`,
ATEN Full Deep Dive) bleibt ein Einzelpositions-Risiko, keine
Depot-weite Korrelation – durch die kleine Positionsgröße (1,3%) ohnehin
gedeckelt.

## Gesamteinschätzung

Kein Cluster verletzt für sich allein eine harte Grenze aus dem
Depot-Ziel-Raster (Champions/Profi/Talent-Kapitalgewichte, 10-12%-
Positions-Caps) – das ist eine ANDERE Risikodimension, die das bestehende
Raster nicht abdeckt. Am ehesten beobachtungswürdig: die 14,7%
Regierungs-/Verteidigungsbudget-Abhängigkeit, weil sie am wenigsten
offensichtlich ist (vier scheinbar unabhängige "Sektoren") und am
wenigsten in Brians eigener Kontrolle liegt (politische Entscheidung,
nicht Unternehmensqualität). Kein Handlungszwang, aber ein bewusst
gemessener Fakt statt eines Bauchgefühls.

## Prozess (ab sofort)

Diese Analyse wird nicht bei jeder Einzelanalyse neu gerechnet (zu
aufwendig, zu wenig Änderung von Woche zu Woche), sondern **im
Monatsrecap aktualisiert** (siehe Agent-Playbook.md) – neue Positionen
werden gegen die drei oben definierten Cluster geprüft, bevor sie
aufgenommen werden, nicht nur gegen Region/Sektor/Positionsgröße.

| Datum | Anlass | Ergebnis |
|---|---|---|
| 2026-09-09 | Erstanlage (Playbook-Meta-Review, Over-Engineering-Vorschlag 1) | 3 Cluster identifiziert (Gov/Defense 14,7%, Hochbeta 11,3-22,8%, Zinssensitiv 10,3%), kein Handlungszwang |
