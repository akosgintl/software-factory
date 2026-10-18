# Terepi kísérletek ebben a repóban

A repó négy szoftvergyár-kísérletet tartalmaz. Ezek a beszélgetés terepi bizonyítékai. Ha egy
állítás ellenőrizhető bennük, a kódot nézzük meg, nem az emlékezetünket.

A `knowledge` branch a tiszta `main`-ből indul, így a kísérletek kódja nincs rajta. Olvasás branch
váltás nélkül:

```bash
git ls-tree -r --name-only <branch>      # mi van a branchen
git show <branch>:<útvonal>              # egy fájl tartalma
```

| Kísérlet | Branch | Hol van | Lényeg |
|---|---|---|---|
| super-board | `origin/super-board` (korábban `staging`, a main `b2535fe` commitja nevezte át) | `.claude/skills/super-*`, `.claude/bin/super-board-*`, `.claude/workflows/` | GitHub Project board vezérli. Lane-ek: Build, QA, Review. Kockázat alapú merge gate. 1 kártya, 1 worktree, 1 branch. A `super-collect` telemetriából tölt backlogot. |
| fable-factory | `fable-factory` | `factory/`, `/factory` skill | `board.json` és `backlog.md`, eseményvezérelt orchestrátor, sync szakasz, backlog-függőségek, HTML dashboard. |
| opus-factory | `opus-factory` | `factory/`, `/factory` skill | `board.py` és `board.json`, eseményvezérelt hurok, landing slot a merge sorosítására, `jobs/` mappa, HTML dashboard. |
| warpdotdev-factory | `warpdotdev-factory` (2026-10-17) | `warp-factory/`, `.agents/skills/`, `.warp/workflows/`, `vendor/warp-skills/` | A Warp hivatalos issue → PR gyára (`warp-factory-examples` `02-sdlc-issue-to-pr`), helyben futtatva (`/factory-local`). Ágensek: foreman, triage, spec, implementer, reviewer. Két scorer (LLM eval, 25% mintavétel). A Warp skill-csomagjai. |

A négy kísérlet folyamatának összevetése: `topics/folyamat-osszevetes.md`. A rájuk vonatkozó
nyitott kérdések a `questions.md` fájlban vannak.

## Megfigyelések

- 🔍 **super-board, emberi kapuk** (2026-10-16, akkor még a `staging` branchen): a kártya
  formátuma spec (Problem, Fix, AC, Risk). A `super-collect` a Backlog oszlopba tesz, a Builder a
  Ready oszlopból dolgozik (`references/run.md`). A Backlog → Ready lépés egyszerre K0 és K1.
  Terv-kapu (K2) nincs, a Builder maga tervez. A merge-et a Reviewer ágens végzi, emberhez csak a
  `merge_policy` küldi (`bin/super-board-merge-policy.py`: default, money, auth, schema, 400 sor
  felett). A bizalom statikus konfiguráció, nem mért érték, és nincs mintavétel.
- 🔍 **super-board, bizonyíték** (2026-10-16): a `super-qa` Playwrighttal fut, lépésenként
  képernyőképet, console és HAR naplót ment. Egy növekvő e2e készletet épít (`e2e/paths/`,
  `e2e/flows/`), amit a CI minden PR-nál futtat, steady state-ben AI nélkül. A `super-qa` független
  a `super-build`-től. Az emberi approval a head SHA-hoz kötött (`bin/super-board-approval.py`).
- 🔍 **super-board és a 0004** (2026-10-16): a kemény területekből money, auth és schema megvan,
  útvonal és kulcsszó alapján. A címke csak emberhez küldhet, felhatalmazást nem ad, vagyis a
  „csak felfelé” megvan. A 400 soros küszöb ellentétes a 0004-gyel. Hiányzik: visszavonhatóság,
  fan-in alapú hatókör, új függőség, bizonyíték-lefedettség, előélet, mintavétel.
- 🔍 **super-board, scope-ellenőrzés** (2026-10-16): a `super-review` a diffet és az AC-ket a
  Builder beszámolója *előtt* olvassa, és saját hipotézist ír. A találatok osztályai között van
  *Scope drift* és *Over-engineering*. A review közben észrevett refaktor külön kártya lesz a
  Backlog oszlopban, nem a Ready-ben, mert „senki nem nézte, és nincs AC-je”
  (`bin/super-review-file-refactor.sh`). Ellentmondás: ha a reviewer AC-t is ír a kártyához, az
  egyenesen a Ready oszlopba kerül (`super-review/SKILL.md`), vagyis kikerüli a K0-t és a K1-et. A
  0005 szerint a refaktor szándék-javaslat, és K0-n megy át.
- 🔍 **warpdotdev-factory, kapuk** (2026-10-18): a foreman vezérel, a munkát nem maga végzi. Spec
  csak kétértelmű vagy nagy munkánál készül, és arra ember jóváhagyás kell. A reviewer verdiktje
  tanácsadó; az egyértelmű leleteket a foreman visszaküldi az implementernek, amíg a review tiszta,
  korlát nélkül. A merge mindig ember: „Never merge, and never approve a spec on a human's behalf.”
  (`warp-factory/agents/foreman/agent.md`). A 0002 kapuival összevetve: K1 van (nem mindig), K2
  nincs, K3 mindig ember.
- 🔍 **warpdotdev-factory, eval** (2026-10-18): a `task-compliance` és a `review-quality` scorer
  LLM bíráló (`claude-4-5-haiku`), címkékkel és pontszámmal, a futások 25%-án
  (`warp-factory/scorers/`). Ez utólagos, mintavételes eval, nem a kapu előtti.
