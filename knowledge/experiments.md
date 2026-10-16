# Terepi kísérletek ebben a repóban

A repó három szoftvergyár-kísérletet tartalmaz. Ezek a beszélgetés terepi bizonyítékai. Ha egy
állítás ellenőrizhető bennük, a kódot nézzük meg, nem az emlékezetünket.

A `knowledge` branch a tiszta `main`-ből indul, így a kísérletek kódja nincs rajta. Olvasás branch
váltás nélkül:

```bash
git ls-tree -r --name-only <branch>      # mi van a branchen
git show <branch>:<útvonal>              # egy fájl tartalma
```

| Kísérlet | Branch | Hol van | Lényeg |
|---|---|---|---|
| super-board | `staging` | `.claude/skills/super-*`, `.claude/bin/super-board-*`, `.claude/workflows/` | GitHub Project board vezérli. Lane-ek: Build, QA, Review. Kockázat alapú merge kapu. 1 kártya, 1 worktree, 1 branch. A `super-collect` telemetriából tölt backlogot. |
| fable-factory | `fable-factory` | `factory/`, `/factory` skill | `board.json` és `backlog.md`, eseményvezérelt orchestrátor, sync szakasz, backlog-függőségek, HTML dashboard. |
| opus-factory | `opus-factory` | `factory/`, `/factory` skill | `board.py` és `board.json`, eseményvezérelt hurok, „landing slot” a merge sorosítására, `jobs/` mappa, HTML dashboard. |

## Megfigyelésre váró kérdések

- 💭 Miben tér el a három gyár koordinációs modellje: külső board (GitHub Project) vagy helyi
  állapotfájl?
- 💭 Hogyan oldja meg mindhárom a párhuzamos munka ütközését: worktree, landing slot, merge kapu?
- 💭 Hol lép be az ember mindháromban, és ez melyik autonómia-szintnek felel meg?
