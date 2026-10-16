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

## Megfigyelések

- 🔍 **super-board, emberi kapuk** (2026-10-16, `staging`): a kártya formátuma spec (Problem, Fix,
  AC, Risk). A `super-collect` a Backlog oszlopba tesz, a Builder a Ready oszlopból dolgozik
  (`references/run.md`). Terv-kapu nincs. A merge-et a Reviewer ágens végzi, emberhez csak a
  `merge_policy` küldi (`bin/super-board-merge-policy.py`: default, money, auth, schema, 400 sor
  felett). A bizalom statikus config, nem mért érték. A 0002-es álláspont kapuival összevetve:
  K1 valószínűleg van, K2 nincs, K3 csak kockázat szerint van.
- 🔍 **super-board, bizonyíték** (2026-10-16, `staging`): a `super-qa` Playwrighttal fut, lépésenként
  képernyőképet, console és HAR naplót ment. Egy növekvő e2e készletet épít (`e2e/paths/`,
  `e2e/flows/`), amit a CI minden PR-nál futtat, steady state-ben AI nélkül. A `super-qa` független
  a `super-build`-től. Az emberi approval a head SHA-hoz kötött (`bin/super-board-approval.py`).
- 🔍 **super-board és a 0004** (2026-10-16): a kemény kategóriákból money, auth és schema megvan.
  A 400 soros küszöb ellentétes a 0004-gyel. Hiányzik: visszavonhatóság, fan-in alapú hatókör, új
  függőség, bizonyíték-lefedettség, előélet, mintavételezés.
- 🔍 **super-board, scope conformance** (2026-10-16, `staging`): a `super-review` a diffet és az AC-ket
  a Builder beszámolója *előtt* olvassa, és saját hipotézist ír. A találatok osztályai között van
  *Scope drift* (a diff olyat változtat, amit a kártya nem kért) és *Over-engineering*. A review
  közben észrevett refaktor külön kártya lesz a Backlog oszlopban, nem a Ready-ben, mert „senki nem
  nézte, és nincs AC-je” (`bin/super-review-file-refactor.sh`). Ellentmondás: ha a reviewer AC-t is
  ír a kártyához, az egyenesen a Ready oszlopba kerül (`super-review/SKILL.md`), vagyis kikerüli
  az emberi K1-et.
