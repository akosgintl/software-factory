# Mikor alacsony kockázatú egy PR?

Kérdés: mikor merge-ölhet a gyár ember nélkül (0003)?

📌 Az elfogadott változat: [`positions/0004-alacsony-kockazat.md`](../positions/0004-alacsony-kockazat.md).
Eltérés az alábbi javaslattól: a sorok száma nem számít, a mintavétel 10%, módosítható.

## Kockázat = mi romolhat el × mennyire látjuk × mennyire vonható vissza

## Javaslat: öt feltétel, mindnek teljesülnie kell (ÉS)

| # | Feltétel | Mit jelent | Ki dönti el |
|---|---|---|---|
| 1 | **Nincs kemény kategória** | nem érint pénzt, auth/jogosultságot, adatot (séma, migráció, törlés), személyes adatot, publikus API-t vagy szerződést, infrastruktúrát vagy titkot, új függőséget | determinisztikus szabály a diffen (útvonal, tartalom) |
| 2 | **Egy reverttel visszavonható** | nincs külső mellékhatás (e-mail, fizetés, harmadik fél), nincs adatírás, amit a revert nem hoz vissza | szabály + független ágens |
| 3 | **Kicsi hatókör** | levél-modul, nem közös mag; kevés fájl és sor; kevés hívó (fan-in) | szabály (méret, függőségi gráf) |
| 4 | **Teljes bizonyíték** | minden AC-hez van bizonyíték (0003 négy tulajdonsága), e2e zöld, a változott kódot teszt fedi | QA lane, szabály |
| 5 | **Jó előélet** | ebben a kategóriában és kódterületen a mért átcsúszási arány a küszöb alatt | tanuló hurok, mérés |

## Három szabály a definíció köré

- **A kockázat csak felfelé módosítható.** A ticket `Risk` mezőjét ágens írja. Emelheti a
  kockázatot, csökkenteni nem. A Builder nem minősítheti a saját munkáját.
- **A kemény kategóriák listáját csak ember változtatja.** A tanuló hurok az 5. feltétel küszöbét
  javasolhatja, az 1. listát nem lazíthatja.
- **Mintavételezés.** Az automatikusan merge-ölt PR-ok egy részét utólag ember megnézi. Enélkül
  nincs adat az 5. feltételhez: ahol nem néz ember, ott nem tudjuk mérni a hibát.

## Plusz biztosíték merge után

Alacsony kockázat akkor is, ha merge után gyorsan észrevesszük és visszavonjuk: monitorozás,
automatikus revert, feature flag.

## Mit csinál a super-board (`staging`, `bin/super-board-merge-policy.py`)

- 🔍 Van 1. feltétel: money, auth, schema kategória címke, útvonal és kulcsszó alapján.
- 🔍 A 400 soros küszöb (lockfile, generált fájl kivéve) ellentétes a 0004-gyel: nálunk a sorok száma
  nem számít.
- 🔍 A címke csak emberhez küldhet, felhatalmazást nem ad: „csak felfelé” már megvan.
- 💭 Nem láttam: visszavonhatóság, függőségi hatókör, új függőség, bizonyíték-lefedettség,
  előélet, mintavételezés.
