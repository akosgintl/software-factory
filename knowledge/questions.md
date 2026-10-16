# Nyitott kérdések

A lezárt kérdést áthúzzuk, és odaírjuk, hová került (`positions/` vagy `topics/`).

## Fogalmi

- [ ] Hol húzzuk meg pontosan a határt AI-támogatott és AI-natív között? Elég az L3/L4 határ, vagy
      más tengely kell (például: kinek írjuk a dokumentációt)?
- [ ] A szoftvergyár metafora segít, vagy félrevisz? Mi az, ami a gyár-analógiából nem igaz a
      szoftverre?

## Gyakorlati

- [x] ~~Mit validál az ember a végén: a diffet, vagy az eredményt a szándékhoz képest (bizonyíték, AC)?~~
      → `positions/0002-emberi-kapuk-es-bizalom.md`
- [ ] Hogyan mérjük a bizalmat (változtatás-típus, kockázat, kódterület szerint), mikor vonul ki az
      ember egy kapuból, és mikor lép vissza?
- [ ] Hogyan védjük a tanuló hurkot a Goodhart-hatástól, vagyis attól, hogy a gyár kijátssza a
      saját mérőszámait?
- [x] ~~Ki finomítja a szándékot specifikációvá: a gyár vagy az ember? Ez külön emberi kapu?~~
      → `positions/0002-emberi-kapuk-es-bizalom.md`
- [x] ~~Mi a „vége”, ahol mindig ember validál: a PR merge vagy a release? A super-board alacsony
      kockázatnál emberi jóváhagyás nélkül merge-öl.~~ → `positions/0003-a-veg-a-pr-bizonyitekkal.md`
- [x] ~~Milyen legyen a bizonyíték: AC-nként, a commithoz kötött, független lane állítja elő, valódi
      (preview) környezetben? Mind a négy kell?~~ → `positions/0003-a-veg-a-pr-bizonyitekkal.md`
- [ ] Hogyan kezeljük az e2e teszt költségét és véletlenszerű hibáit (flakiness)?
- [x] ~~Igazítsuk a super-board-ot a 0003-hoz, vagy az álláspont túl szigorú?~~ → a 0003 módosult:
      alacsony kockázatnál lehet automatikus merge
- [x] ~~Mi az alacsony kockázat definíciója?~~ → `positions/0004-alacsony-kockazat.md`
- [ ] Kell scope conformance ellenőrzés (a diff nem csinál többet, mint az AC-k), ha a méret nem
      számít?
- [ ] Milyen sorrendben kapcsolhatók ki a kapuk (K2 elsőként?), és mi a pontos mérőszám (escape
      rate kapunként és kategóriánként)?

- [ ] Mi helyettesíti az emberi code review-t egy AI-natív gyárban, és mikor elég?
- [ ] Mely mérőszámok mutatják meg, hogy egy gyár valóban AI-natív? (DORA átdolgozva?)
- [ ] Hogyan védekezik egy AI-natív gyár az architektúra eróziója ellen?
- [ ] Hol fordul át a gazdaságosság: mikor olcsóbb az ágens, mint az ember, a teljes költséggel?

## Emberi oldal

- [ ] Milyen szerepek maradnak az embernek egy L4–L5 gyárban, és milyen képességek kellenek hozzájuk?
- [ ] Hogyan tanul egy junior fejlesztő, ha a munka nagy részét ágensek végzik?

## A kísérletekről

- [ ] A három kísérlet (super-board, fable-factory, opus-factory) közül melyik koordinációs modell
      skálázódik jobban, és miért?
