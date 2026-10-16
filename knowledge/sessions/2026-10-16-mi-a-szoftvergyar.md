# 2026-10-16 — Mit értünk szoftvergyár alatt

## Kérdés

Mit értünk szoftvergyár alatt? A régi meghatározás („ismételhető, mérhető, iparszerű szervezés”)
túl tág volt, egy jó Scrum-csapat is belefért.

## Amit végiggondoltunk

- 🔍 A szónak három jelentése van: A. folyamat (Cusumano), B. platform (Greenfield–Short, DoD),
  C. autonóm termelés (dark factory). Mi a C-t választjuk, emberi végső kapuval.
- 🔍 A szoftvert ingyen lehet másolni. Ezért ami gyártható, az nem a termék, hanem a változtatás.
- 💭 Csak AI-val lehet igazán gyárat építeni, mert csak az ágens cserélhető munkavégző.
- 💭 A gyár az ismert munkára jó, a felfedező munkára rossz. Tehát a szervezet része, nem az egész.
- 💭 A végső emberi validálás skálázáskor szűk keresztmetszet. Javaslat: az ember az eredményt
  validálja a szándékhoz képest (bizonyíték, AC), a diffet csak kockázat szerint.
- 💭 A bizalom mérhető, kategóriánként épül (változtatás-típus, kockázat, kódterület), és
  elveszíthető. A super-board kockázat alapú merge kapuja ennek a kezdete.
- 💭 A tanuló hurok saját változtatásai is intent → PR úton mennek, ugyanazokon a kapukon.
  Veszély a Goodhart-hatás: a gyár kijátszhatja a saját mérőszámait. A fő jel ezért az emberi
  validálás eredménye legyen (elutasítás, újramunka), amit a gyár nem tud közvetlenül befolyásolni.

## Ahová eljutottunk

- 📌 [`positions/0001-mit-ertunk-szoftvergyar-alatt.md`](../positions/0001-mit-ertunk-szoftvergyar-alatt.md):
  intent → PR, a célt az ember választja, az ember validál (a végén mindig), skillek, ágensek,
  workflow-k, tanuló hurok. „A gyár javasol és végrehajt, az ember dönt és validál.”
- Következmény: az L5 („a backlogot is ágensek töltik”) a definíciónk szerint nem gyár-szint.
  A `super-collect` csak javasolhat. A topic jegyzetben jelöltem.
- Frissült a fogalomtár: szoftvergyár, intent, tanuló hurok, dark factory.

## Nyitva maradt

- Mit validál az ember a végén: a diffet vagy az eredményt?
- Hogyan mérjük a bizalmat, és mikor vonul ki az ember egy kapuból?
- Hogyan védjük a tanuló hurkot a Goodhart-hatástól?
- Ki finomítja a szándékot specifikációvá: a gyár vagy az ember?

---

## Folytatás: emberi kapuk

### Amit végiggondoltunk

- 📌 Az ember a végén az eredményt validálja a szándékhoz képest, a diffet csak kockázat szerint.
- 📌 Intent → spec: ágens írja, ember jóváhagyja. Spec → terv: ágens írja, ember jóváhagyja.
- 📌 A bizalmat mérjük, javítjuk, a kapukat ki- és bekapcsoljuk.
- 💭 K1 és K3 egy pár: a jóváhagyott spec AC-i a K3 elfogadás szerződése. K1 nélkül K3 drága.
- 💭 K2 a leggyengébb kapu, mert a „hogyan” kérdést validálja. Valószínűleg ez kapcsolható ki
  elsőként.
- 🔍 Megnéztük a super-board kódját (`staging`):
  - K1: a kártya formátuma (`ticket-format.md`) gyakorlatilag spec (Problem, Fix, AC, Risk).
    A `super-collect` csak a Backlog oszlopba tesz, a Builder a Ready oszlopból dolgozik. 💭 A
    Backlog → Ready lépés lehet az emberi K1, ezt még ellenőrizni kell.
  - K2: nincs. A Builder maga tervez.
  - K3: a Reviewer ágens merge-öl. Ember csak akkor kell, ha a `merge_policy` ezt kéri
    (`default: "human"`, money, auth, schema, 400 sornál nagyobb PR). Egyébként automatikus merge.
  - A bizalom statikus szabály a configban, nem mérés. Nincs tanuló hurok, ami a kapukat
    kapcsolná.

### Ahová eljutottunk

- 📌 [`positions/0002-emberi-kapuk-es-bizalom.md`](../positions/0002-emberi-kapuk-es-bizalom.md)
- Ellentmondás: a 0001 szerint a végén mindig van ember. A super-board viszont alacsony kockázatnál
  automatikusan merge-öl.

### Nyitva maradt

- A „vége” a PR merge, vagy a release? Ha az ember a release-t fogadja el, nem minden PR-t, az
  skálázódik.

---

## Folytatás: a vég és a bizonyíték

### Amit végiggondoltunk

- 📌 A vég a PR. Implementáció → PR, bizonyítékkal: képernyőkép a futásról, teszt a futó
  rendszeren, e2e is, nem csak unit és integrációs teszt.
- 💭 A K3 akkor skálázódik, ha a bizonyíték miatt egy PR elfogadása perc, nem óra. Mérőszám: emberi
  idő PR-onként a K3-nál.
- 💭 A bizonyíték négy tulajdonsága:
  1. AC-nként: minden AC mellett ott van a saját bizonyítéka (nyomon követhetőség).
  2. A commithoz kötött: a head SHA-ról készült. Ha a kód változik, a bizonyíték elavul.
  3. Független: nem a Builder állítja elő, hanem egy másik lane. Különben a Builder „megrendezheti”
     (megint Goodhart).
  4. Valódi környezet: PR-onként futó előnézeti környezet (preview environment) kell hozzá.
- 🔍 super-board (`staging`): a `super-qa` Playwrighttal fut, lépésenként képernyőképet, console
  és HAR naplót ment, és egy növekvő e2e készletet (`e2e/paths/`, `e2e/flows/`) épít, amit a CI
  minden PR-nál futtat. A `super-qa` független a `super-build`-től. Az approval head-hez kötött
  (`super-board-approval.py`).
- 💭 A növekvő e2e készlet maga is a tanuló hurok terméke: minden megtalált hiba új e2e tesztet
  hagy maga után, és a gyár ellenőrzési képessége nő.

### Ahová eljutottunk

- 📌 [`positions/0003-a-veg-a-pr-bizonyitekkal.md`](../positions/0003-a-veg-a-pr-bizonyitekkal.md)
- A super-board automatikus merge-e (alacsony kockázat) eltér a 0001-es és a 0003-as állásponttól.

### Nyitva maradt

- A bizonyíték négy tulajdonsága (AC-nként, commithoz kötött, független, valódi környezet):
  mind kell?

---

## Folytatás: alacsony kockázat

### Amit végiggondoltunk

- 📌 A bizonyíték négy tulajdonsága elfogadva (bekerült a 0003-ba).
- 📌 Alacsony kockázatnál lehet automatikus merge. A 0003 módosult.
- 💭 Javaslat az alacsony kockázatra: öt ÉS feltétel (kemény kategória, visszavonhatóság, hatókör,
  bizonyíték, előélet), három szabállyal (csak felfelé, a kemény listát csak ember változtatja,
  mintavételezés). Részletek: `topics/alacsony-kockazat.md`.

### Nyitva maradt

- Melyek a kemény kategóriák nálad? Mekkora a méret-küszöb? Mekkora legyen a mintavétel?

### Döntés

- 📌 [`positions/0004-alacsony-kockazat.md`](../positions/0004-alacsony-kockazat.md): a hét kemény
  kategória elég; a sorok száma nem számít, a hatókör igen (fan-in, közös mag); a mintavétel 10%,
  módosítható.
- 💭 Nyitott: egy nagy PR többet változtathat, mint amit az AC-k leírnak. Pótlék lehet a scope
  conformance ellenőrzés.

---

## Folytatás: kérdések rendezése, scope conformance

- Lezártunk négy kérdést, amelyekre az álláspontok már válaszoltak (metafora, bizalom mérése, mi
  helyettesíti a code review-t). A lezártak a `questions.md` aljára kerültek.
- 🔍 A super-review már tud scope conformance-t: *Scope drift* találati osztály, AC-t olvas a Builder
  beszámolója előtt, a mellékesen észrevett refaktor a Backlogba kerül. Ellentmondás: AC-vel
  rendelkező refaktor-kártya egyenesen a Ready oszlopba mehet, kikerülve a K1-et.
- 📌 [`positions/0005-scope-conformance.md`](../positions/0005-scope-conformance.md): a diff minden része
  visszavezethető egy AC-re; a scope drift kikerül vagy Backlog-kártya lesz; a gyár által javasolt
  kártya nem kerülheti ki a K1-et; a 0004 negyedik feltétele bővült; a refaktor-kártyák száma és kora
  az erózió mérőszáma.
