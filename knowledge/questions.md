# Nyitott kérdések

A lezárt kérdést áthúzzuk, odaírjuk, hová került (`positions/` vagy `topics/`), és a lap aljára
tesszük.

## Fogalmi

- [ ] Nagy szándéknál a szándék : spec arány 1:N legyen, vagy a nagy szándékot bontsuk több
      szándékra? (`topics/fogalmi-modell.md`, most 1:1)
- [ ] Mitől lesz egy szereplő saját állítása ellenőrizhető (például „preview környezetben
      készült”, „reverttel visszavonható”, „az AC felületet érint”)? Független második ágens, vagy
      gépi mérés az állítás mögött? (0003, 0004, 0006)
- [ ] Mikor független két ágens? Elég, ha más sávban, más utasítással dolgozik, vagy más modell is
      kell? (`glossary.md`: független, E3)

## Gyakorlati

- [ ] Hogyan védjük a tanuló hurkot a Goodhart-hatástól, vagyis attól, hogy a gyár kijátssza a
      saját mérőszámait?
- [ ] Milyen sorrendben lépnek a kapuk a létrán (a K2 elsőként?), és mik a pontos küszöbök
      (átcsúszási arány kapunként és kategóriánként, minimális mintaszám)? (0002)
- [ ] Mely mérőszámok mutatják meg, hogy egy gyár jól működik? Eddig: átcsúszási arány, emberi
      idő PR-onként a K3-nál, újramunka aránya, elakadási arány. (DORA-mérőszámok átdolgozva?)
- [ ] Hogyan kezeljük az e2e teszt költségét és a flaky teszteket?
- [ ] Hogyan védekezik a gyár az architektúra eróziója ellen? Részben: 0005 (refaktor-szándékok
      mint mérőszám, refaktor-kör). Kapcsolódik: fan-in alapú hatókör (0004).
- [ ] Hol fordul át a gazdaságosság: mikor olcsóbb az ágens, mint az ember, a teljes költséggel?
- [ ] Ki és mikor fogadja el a szándékot, ha több munkadarabra bomlott, és mindegyik külön ment át
      a K3-on? Kell szándék-szintű bizonyíték (e2e az összevont állapoton)? És mi van a main-nel a
      köztes állapotban (feature flag)? (0008)
- [ ] Kell-e merge utáni biztosíték az alacsony kockázathoz (monitorozás, automatikus revert,
      feature flag)? (0004)
- [ ] Rögzítse-e a tervezés AC-nként előre, milyen bizonyíték kell (a Factory Missions
      „validation contract”-ja mintájára)? (`topics/folyamat-osszevetes.md`)
- [ ] Legyenek-e rejtett forgatókönyvek, amelyeket a Builder nem lát (StrongDM)?
- [ ] Az újramunka-korlát a köröket számolja (0007, most 3), vagy az azonos okú hibát (super-board,
      root-cause hash)? És a landing ütközése számít-e újramunka-körnek?

## Emberi oldal

- [ ] Milyen szerepek maradnak az embernek, és milyen képességek kellenek hozzájuk? Részben: a 0001
      és a 0002 szerint az ember célt választ (közvetlenül vagy szabállyal), kapunál dönt vagy
      szabályt hagy jóvá, mintát néz, elakadást old fel, és dönt a gyár változtatási javaslatairól.
      Szét kell-e választani a szerepeit (megrendelő, jóváhagyó)?
- [ ] Hogyan tanul egy junior fejlesztő, ha a munka nagy részét ágensek végzik?

## A kísérletekről

- [ ] A négy kísérlet (super-board, fable-factory, opus-factory, warpdotdev-factory) közül melyik
      koordinációs modell skálázódik jobban: külső board (GitHub Project), helyi állapotfájl, vagy
      ágens-vezérlő (foreman)? (`experiments.md`)
- [ ] Hogyan oldják meg a párhuzamos munka ütközését: worktree, landing slot, merge gate, sync?
- [ ] Hol lép be az ember a négyben, és ez melyik autonómia-szintnek felel meg?
- [ ] Mit csinál a Warp scorer `selfImprovement` beállítása? Ha a gyár maga módosítja vele az
      ágens-utasítást, az sérti az E8-at. (`topics/folyamat-osszevetes.md`)

## Lezárt

- [x] ~~Hol húzzuk meg a határt AI-támogatott és AI-natív között?~~ → nem kérdés: a gyár AI-natív,
      L4 tanuló hurokkal; `positions/0001-mit-ertunk-szoftvergyar-alatt.md` (7. pont)
- [x] ~~Ellentmondás: a 0005 szerint a review-ból munkadarab lesz, a fogalmi modell szerint
      munkadarab csak tervből jöhet.~~ → minden gyár-javaslat szándék-javaslat, K0-n megy át;
      `positions/0005-scope-conformance.md` (3. pont), az I-0005-4 visszavonva
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
      → `positions/0002-emberi-kapuk-es-bizalom.md` (szabály és mintavétel kapunként és
      kategóriánként; a pontos küszöb nyitva maradt fent)
- [x] ~~Mi helyettesíti az emberi code review-t, és mikor elég?~~
      → `positions/0002-emberi-kapuk-es-bizalom.md`, `positions/0003-a-veg-a-pr-bizonyitekkal.md`,
      `positions/0004-alacsony-kockazat.md` (bizonyíték alapú elfogadás, diff csak kockázat szerint,
      szabály szerinti elfogadás alacsony kockázatnál, mintavétellel)
- [x] ~~Mi a „vége”, ahol mindig ember validál: a PR merge vagy a release?~~
      → `positions/0003-a-veg-a-pr-bizonyitekkal.md`
- [x] ~~Milyen legyen a bizonyíték? Mind a négy tulajdonság kell?~~
      → `positions/0003-a-veg-a-pr-bizonyitekkal.md`
- [x] ~~Igazítsuk a super-board-ot a 0003-hoz, vagy az álláspont túl szigorú?~~ → a 0003 módosult:
      alacsony kockázatnál szabály fogad el
- [x] ~~Mi az alacsony kockázat definíciója?~~ → `positions/0004-alacsony-kockazat.md`
