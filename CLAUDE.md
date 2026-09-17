# Repo-Betriebsanweisungen für Claude Code

## Git-Commit/Push: automatisch, keine Rückfrage nötig (seit 2026-09-17, von Brian)

Für dieses Repo gilt: **Claude committet und pusht Änderungen an bestehenden,
bereits vom Nutzer bestätigten Arbeitsergebnissen automatisch, ohne vorher
im Chat nachzufragen.** Das ersetzt die vorherige Regel "nur auf explizite
Anweisung pro Fall". Gilt für den normalen Workflow: Datei ändern → stagen →
committen → pushen, in einem Zug.

**Weiterhin geltende Sorgfaltsregeln (unverändert):**
- Nur die konkret geänderten/relevanten Dateien stagen (`git add <datei>...`),
  **niemals** `git add -A` oder `git add .`.
- `.claude/` und `reports/tmp_charts/` nie mit committen.
- Commit-Message kurz, auf Deutsch, endet mit:
  `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`
- Vor dem Stagen kurz `git status`/`git diff` prüfen, dass nichts
  Unbeabsichtigtes/Sensibles mit hineinrutscht.

**Weiterhin NICHT automatisch erlaubt, bleibt an explizite Anweisung
gebunden:** Force-Push, `git reset --hard`, das Löschen von Branches, das
Amenden bereits gepushter Commits, oder jede andere destruktive/
history-verändernde Git-Operation. Diese Ausnahme gilt unabhängig von der
obigen Auto-Push-Freigabe.

## Gemeinsames Gedächtnis über Chat-Sessions UND automatisierte Läufe hinweg (seit 2026-09-17, von Brian gefordert)

Chat-Sessions (interaktiv) und die Hermes-Cron-Läufe (taeglicher-trigger-check/
blitz-scan/wochenfazit/monatsrecap) sind GETRENNTE Ausführungskontexte ohne
gemeinsames Live-Gedächtnis — sie teilen sich Zustand AUSSCHLIESSLICH über die
Dateien in diesem Repo. Ein Cron-Lauf, der gerade eben etwas erledigt hat,
ist einer neu gestarteten Chat-Session nicht automatisch bekannt, und
umgekehrt.

**Deshalb PFLICHT, bevor in irgendeiner Session eine depot-/watchlist-/
finanzbezogene Einschätzung, Empfehlung oder Aktion erfolgt:**
1. `depot/master_status.md` vollständig lesen (konsolidierter Status —
   Kategorie-Zählungen, offene Prüfpunkte, offene Empfehlungen, Cash-Stand).
2. Die letzten ~40 Zeilen von `depot/bridge_status.md` lesen (Log der
   jüngsten automatisierten Läufe — zeigt, was zuletzt automatisiert
   passiert ist, auch wenn diese Session davon nichts "weiß").
3. Bei Widersprüchen zwischen beiden Dateien oder zu älteren Annahmen: die
   Informations-Vorrang-Hierarchie aus `Agent-Playbook.md` anwenden
   (jüngste bestätigte Transaktion/Entscheidung > `master_status.md` >
   `Agent-Playbook.md` > ältere Analysen/`HANDOVER.md`).

Das gilt für JEDE Session-Art gleichermaßen — interaktiver Chat, Blitz-Scan,
Täglicher Trigger-Check, Wochenfazit, Monatsrecap. Ziel: keine Session
agiert auf einem Stand, der durch eine andere Session in der Zwischenzeit
bereits überholt wurde.
