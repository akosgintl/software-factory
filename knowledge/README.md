# Tudásbázis: AI-natív és AI-támogatott szoftvergyár

Ez a tartós beszélgetésünk a szoftvergyárakról (software factory), és arról, hogy mi a különbség az
**AI-natív** és az **AI-támogatott** változat között. A beszélgetés nem a chat ablakban él, hanem
ebben a mappában. Bármelyik új munkamenet innen folytatja.

Branch: `knowledge`. A tiszta `main`-ből indul, és nem megy vissza sem a `staging`-be, sem a
`main`-be. Csak a tudás él rajta.

## Folytatás új munkamenetben

Elég ennyit írni: „folytassuk a knowledge beszélgetést”. Claude ekkor:

A. elolvassa a [`STATE.md`](STATE.md) fájlt (hol tartunk, mi a következő kérdés),
B. elolvassa a legutóbbi [`sessions/`](sessions/) naplót,
C. onnan folytatja, ahol abbahagytuk.

A munkamódszer részletei a [`CLAUDE.md`](CLAUDE.md) fájlban vannak. Claude ezt automatikusan betölti.

## Térkép

| Fájl / mappa | Mit tartalmaz | Mikor változik |
|---|---|---|
| [`STATE.md`](STATE.md) | aktuális fókusz, a következő lépés, a futó szálak | minden munkamenet végén |
| [`sessions/`](sessions/) | munkamenet-naplók, `ÉÉÉÉ-HH-NN-<téma>.md` | munkamenetenként egy új fájl |
| [`topics/`](topics/) | témajegyzetek, egy fogalom vagy kérdéskör fájlonként | amikor egy téma megérik |
| [`positions/`](positions/) | álláspontok, amelyekben megegyeztünk (ADR-szerű, számozott) | amikor egy vita lezárul |
| [`questions.md`](questions.md) | nyitott kérdések listája | folyamatosan |
| [`glossary.md`](glossary.md) | fogalomtár, a közös szókincs | amikor új fogalmat használunk |
| [`sources.md`](sources.md) | források, megbízhatósági jelöléssel | amikor forrásra hivatkozunk |
| [`experiments.md`](experiments.md) | a repó saját gyár-kísérletei mint terepi bizonyíték | amikor egy kísérlet változik |

## A tudás érettségi szintjei

Minden állítás valamelyik szinten áll. Ezt a jegyzetekben jelöljük.

| Jel | Szint | Jelentés |
|---|---|---|
| 💭 | hipotézis | felvetés, még nem vitattuk meg |
| 🔍 | vizsgált | megvitattuk, van mellette és ellene érv |
| 📌 | álláspont | megegyeztünk, a `positions/` mappában rögzítve |
| 🧪 | igazolt | kísérlet vagy forrás támasztja alá |
