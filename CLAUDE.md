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
