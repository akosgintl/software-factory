# Nyitott kérdések

A lezárt kérdést áthúzzuk, odaírjuk, hová került (`positions/` vagy `topics/`), és a lap aljára
tesszük.

## Fogalmi

- [ ] Hol húzzuk meg pontosan a határt AI-támogatott és AI-natív között? Részben: a 0001 szerint a
      mi gyárunk L4 plusz tanuló hurok, az L5 nem gyár-szint. Kérdés, hogy az L3/L4 határ elég-e,
      vagy más tengely kell (például: kinek írjuk a dokumentációt).

- [ ] Nagy szándéknál a szándék : spec arány 1:N legyen, vagy a nagy szándékot bontsuk több
      szándékra? (`topics/fogalmi-modell.md`, most 1:1)

- [ ] Mitől lesz egy ágens saját állítása ellenőrizhető (például „preview környezetben készült”,
      „reverttel visszavonható”)? Független második ágens, vagy gépi mérés az állítás mögött?
      (`positions/0006-grafmodell.md`, `topics/invariansok.md`)

- [ ] **Ellentmondás:** a 0005 szerint a review közben talált kéretlen változásból munkadarab lesz,
      a fogalmi modell szerint viszont munkadarab csak tervből jöhet (a felbontás egyetlen helye).
      A review-ból született munkadarab megkerüli a K0-t, a K1-et és a K2-t. A gráfban ugyanez: a
      *munkadarab → munkadarab* irányú *származik* él és az I-0005-4. Javaslat (még nem döntöttünk):
      minden gyár-javaslat (review-lelet, telemetria, átcsúszott hiba, tanuló hurok) szándék-javaslat
      legyen, amely K0-n megy át; a *származik* él a szándéktól a lelet helyére mutasson; a 0005 3.
      pontja és az I-0005-4 helyére az I-0002-5 lépjen. (`positions/0005-scope-conformance.md`,
      `topics/fogalmi-modell.md`, `topics/invariansok.md`)

## Gyakorlati

- [ ] Hogyan védjük a tanuló hurkot a Goodhart-hatástól, vagyis attól, hogy a gyár kijátssza a
      saját mérőszámait?
- [ ] Milyen sorrendben kapcsolhatók ki a kapuk (K2 elsőként?), és mi a pontos küszöb (átcsúszási arány
      kapunként és kategóriánként)?
- [ ] Mely mérőszámok mutatják meg, hogy egy gyár jól működik? Eddig felmerült: átcsúszási arány, emberi
      idő PR-onként a K3-nál, újramunka aránya. (DORA átdolgozva?)
- [ ] Hogyan kezeljük az e2e teszt költségét és véletlenszerű hibáit (flakiness)?
- [ ] Hogyan védekezik a gyár az architektúra eróziója ellen? Részben: 0005 (refaktor-munkadarabok mint
      mérőszám, emberi refaktor-kör). Kapcsolódik: fan-in alapú hatókör (0004).
- [ ] Hol fordul át a gazdaságosság: mikor olcsóbb az ágens, mint az ember, a teljes költséggel?

- [ ] Ki és mikor fogadja el a szándékot, ha több munkadarabra bomlott, és mindegyik külön ment át
      a K3-on? Kell szándék-szintű bizonyíték (e2e az összevont állapoton)? És mi van a main-nel a
      köztes állapotban (feature flag)? (`positions/0008-negy-allomas.md`)
- [ ] Rögzítse-e a tervezés AC-nként előre, milyen bizonyíték kell (a Factory Missions „validation
      contract”-ja mintájára)? (`topics/folyamat-osszevetes.md`)
- [ ] Legyenek-e rejtett forgatókönyvek, amelyeket a Builder nem lát (StrongDM)?
- [ ] Az újramunka-korlát a köröket számolja (0007, most 3), vagy az azonos okú hibát (super-board,
      root-cause hash)? És a landing ütközése számít-e újramunka-körnek?

## Emberi oldal

- [ ] Milyen szerepek maradnak az embernek, és milyen képességek kellenek hozzájuk? Részben: a 0001
      és a 0002 szerint az ember célt választ, kapuknál validál, mintát néz, és dönt a gyár
      változtatási javaslatairól.
- [ ] Hogyan tanul egy junior fejlesztő, ha a munka nagy részét ágensek végzik?

## A kísérletekről

- [ ] A három kísérlet (super-board, fable-factory, opus-factory) közül melyik koordinációs modell
      skálázódik jobban, és miért?

## Lezárt

- [x] ~~Mi legyen a „kártya” magyar neve?~~ → munkadarab, `topics/fogalmi-modell.md`

- [x] ~~Kell scope conformance ellenőrzés, ha a méret nem számít?~~
      → `positions/0005-scope-conformance.md`
- [x] ~~A szoftvergyár metafora segít, vagy félrevisz? Mi az, ami a gyár-analógiából nem igaz a
      szoftverre?~~ → `positions/0001-mit-ertunk-szoftvergyar-alatt.md` (nem terméket gyártunk,
      hanem változtatást; a felfedező munkára a gyár kevésbé alkalmas)
- [x] ~~Mit validál az ember a végén: a diffet, vagy az eredményt a szándékhoz képest?~~
      → `positions/0002-emberi-kapuk-es-bizalom.md`
- [x] ~~Ki finomítja a szándékot specifikációvá: a gyár vagy az ember? Ez külön emberi kapu?~~
      → `positions/0002-emberi-kapuk-es-bizalom.md`
- [x] ~~Hogyan mérjük a bizalmat, mikor vonul ki az ember egy kapuból, és mikor lép vissza?~~
      → `positions/0002-emberi-kapuk-es-bizalom.md`, `positions/0004-alacsony-kockazat.md`
      (kategóriánként, escape rate, 10% mintavétel; a pontos küszöb nyitva maradt fent)
- [x] ~~Mi helyettesíti az emberi code review-t, és mikor elég?~~
      → `positions/0002-emberi-kapuk-es-bizalom.md`, `positions/0003-a-veg-a-pr-bizonyitekkal.md`,
      `positions/0004-alacsony-kockazat.md` (bizonyíték alapú elfogadás, diff csak kockázat szerint,
      automatikus merge alacsony kockázatnál, mintavétellel)
- [x] ~~Mi a „vége”, ahol mindig ember validál: a PR merge vagy a release?~~
      → `positions/0003-a-veg-a-pr-bizonyitekkal.md`
- [x] ~~Milyen legyen a bizonyíték? Mind a négy tulajdonság kell?~~
      → `positions/0003-a-veg-a-pr-bizonyitekkal.md`
- [x] ~~Igazítsuk a super-board-ot a 0003-hoz, vagy az álláspont túl szigorú?~~ → a 0003 módosult:
      alacsony kockázatnál lehet automatikus merge
- [x] ~~Mi az alacsony kockázat definíciója?~~ → `positions/0004-alacsony-kockazat.md`
