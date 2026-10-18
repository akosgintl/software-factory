# Tudásbázis: AI-natív szoftvergyár

Ez a tartós beszélgetésünk a szoftvergyárakról (software factory): mi az, és hogyan épül fel egy
**AI-natív** gyár. Az AI-támogatott változatot elvetettük (`positions/0001`). A beszélgetés nem a
chat ablakban él, hanem ebben a mappában. Bármelyik új munkamenet innen folytatja.

Branch: `knowledge`. A tiszta `main`-ből indul, és nem megy vissza sem a `staging`-be, sem a
`main`-be. Csak a tudás él rajta.

## Folytatás új munkamenetben

Elég ennyit írni: „folytassuk a knowledge beszélgetést”. Claude ekkor:

A. elolvassa a [`STATE.md`](STATE.md) és az [`elvek.md`](elvek.md) fájlt,
B. elolvassa a legutóbbi [`sessions/`](sessions/) naplót,
C. onnan folytatja, ahol abbahagytuk.

A munkamódszer részletei a [`CLAUDE.md`](CLAUDE.md) fájlban vannak. Claude ezt automatikusan betölti.

## Térkép

| Fájl / mappa | Mit tartalmaz | Mikor változik |
|---|---|---|
| [`STATE.md`](STATE.md) | aktuális fókusz, a következő lépés, a futó szálak | minden munkamenet végén |
| [`sessions/`](sessions/) | munkamenet-naplók, `ÉÉÉÉ-HH-NN-<téma>.md` | munkamenetenként egy új fájl |
| [`positions/`](positions/) | álláspontok, amelyekben megegyeztünk (ADR-szerű, számozott), a megkötéseikkel | amikor egy vita lezárul |
| [`elvek.md`](elvek.md) | irányelvek (E1–E11) a megkötéseikkel, megkötés-nyilvántartás, és a munkánk elvei (M1–M4) | amikor új irányelv vagy megkötés születik |
| [`topics/`](topics/) | témajegyzetek: a fogalmi modell és a folyamat-összevetés | amikor egy téma megérik |
| [`questions.md`](questions.md) | nyitott kérdések listája | folyamatosan |
| [`glossary.md`](glossary.md) | fogalomtár, a közös szókincs | amikor új fogalmat használunk |
| [`sources.md`](sources.md) | források, megbízhatósági jelöléssel | amikor forrásra hivatkozunk |
| [`abrak/`](abrak/) | ábrák HTML-ben; a `gyar-folyamat.html` a 0008 folyamatábrája, élő változata: https://claude.ai/artifact/QfdY4btjwQMcAwXPBguZ2H | amikor egy álláspont vizuálisan változik |
| [`experiments.md`](experiments.md) | a repó négy saját gyár-kísérlete mint terepi bizonyíték | amikor egy kísérlet változik |

## A tudás érettségi szintjei

Minden állítás valamelyik szinten áll. Ezt a jegyzetekben jelöljük.

| Jel | Szint | Jelentés |
|---|---|---|
| 💭 | hipotézis | felvetés, még nem vitattuk meg |
| 🔍 | vizsgált | megvitattuk, van mellette és ellene érv |
| 📌 | álláspont | megegyeztünk; álláspontban (`positions/`), irányelvben (`elvek.md`) vagy elfogadott jegyzetben rögzítve |
| 🧪 | igazolt | kísérlet vagy forrás támasztja alá |
