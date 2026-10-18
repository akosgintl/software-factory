# Munkamódszer a knowledge beszélgetéshez

Ez a mappa egy tartós, több munkameneten át tartó beszélgetés. A téma: szoftvergyár, AI-natív és
AI-támogatott. A branch a tiszta `main`-ből indul: nincs rajta super-board, nincs ticket, nincs
board, nincs PR. A gyár-kísérleteket más branchekről olvassuk, lásd `experiments.md`.

## Nyelv

- A beszélgetés és a jegyzetek nyelve magyar.
- Az angol szakkifejezést meghagyjuk, ha nincs jó magyar megfelelője, vagy a magyar fejlesztők is
  angolul mondják.
- **Mindenki ugyanazt értse alatta.** Minden fogalom, amit használunk, definícióval szerepel a
  [`glossary.md`](glossary.md) fájlban: az angolul maradók és a „mindenki által ismertek” is. Új
  fogalom első használatakor a definíció is bekerül.

## Munkamenet eleje

1. Olvasd el a `STATE.md` és az `elvek.md` fájlt.
2. Olvasd el a legutóbbi naplót a `sessions/` mappában.
3. Egy-két mondatban mondd el, hol tartunk, és mi a javasolt következő kérdés.

## Munkamenet közben

- Gondolkodótárs vagy, nem jegyzetelő. Mondj ellent, ha gyenge egy érv. Hozz ellenpéldát.
- Minden új állítást jelölj érettségi szinttel (💭 🔍 📌 🧪, lásd `README.md`).
- Forrást ne találj ki. Ha egy hivatkozásban nem vagy biztos, `[ellenőrizendő]` jelet kap a
  `sources.md` fájlban.
- Ha egy fogalom megérik, írd át a `topics/` mappába. A napló ne nőjön végtelenre.
- A repó saját gyár-kísérletei (`experiments.md`) terepi bizonyítékok. Ha egy állítás ellenőrizhető
  a kódban, nézd meg a kódot, ne a memóriádra hagyatkozz.

## Munkamenet vége

1. Írd meg vagy egészítsd ki a napi naplót: `sessions/ÉÉÉÉ-HH-NN-<téma>.md`.
2. Frissítsd a `STATE.md` fájlt: fókusz, következő lépés, futó szálak.
3. Vidd át az új nyitott kérdéseket a `questions.md` fájlba. A lezártakat húzd át, és írd mellé,
   hová kerültek.
4. Commitold a `knowledge` branchre. Formátum: `📝 [docs] knowledge: <téma>`.

## Napló formátum

```markdown
# ÉÉÉÉ-HH-NN — <téma>

## Kérdés
<amivel a munkamenet indult>

## Amit végiggondoltunk
- <pontok, érettségi jellel>

## Ahová eljutottunk
- <új álláspont, átírt topic, elvetett ötlet>

## Nyitva maradt
- <kérdések, amelyek a questions.md fájlba kerültek>
```

## Álláspont formátum (`positions/NNNN-<cím>.md`)

```markdown
# NNNN — <cím>

Állapot: 📌 elfogadva · ÉÉÉÉ-HH-NN

## Kérdés
## Álláspont
## Miért
## Mi szólt ellene
## Mi változtatná meg
```
