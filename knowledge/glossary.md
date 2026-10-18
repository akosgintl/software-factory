# Fogalomtár

Közös szókincs, ábécérendben. **Elv: mindenki ugyanazt értse alatta** (M1). Minden fogalom, amit a
jegyzetekben használunk, itt definícióval szerepel. Azok is, amelyek angolul maradnak, és azok is,
amelyeket „mindenki ismer”. A fogalomtár definiál, a szabályok az álláspontokban vannak (M4): a
„Bővebben” oszlop oda mutat.

| Fogalom | Jelentés | Bővebben |
|---|---|---|
| AC (acceptance criteria) | elfogadási kritérium: ellenőrizhető állítás arról, mikor kész egy spec vagy egy munkadarab. A spec AC-je felhasználói szintű, a munkadarabé technikai. Attribútuma, hogy felhasználói felületet érint-e | `topics/fogalmi-modell.md` |
| ADR (architecture decision record) | rövid, számozott döntési jegyzet: kérdés, döntés, indoklás. Az álláspontjaink ezt a formát követik | `CLAUDE.md` |
| AGENTS.md | a repóban tartott fájl, amely az ágenseknek írja le a projekt szabályait | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| AI-natív szoftvergyár | olyan gyár, amelynek a folyamatát az ágensekre tervezték; az ember a hurok fölött áll. Ezt építjük | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| AI-támogatott szoftvergyár | meglévő, emberközpontú folyamat, amelyben az AI eszköz; az ember a hurokban áll. Elvetjük | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| ágens (agent) | szereplő: modell, eszközök és utasítás egy szerephez; önállóan több lépést hajt végre | `topics/fogalmi-modell.md` |
| állomás | egy lépés a soron. Négy van: tervezés, build, ellenőrzés, landing. *Mit* csinálunk; a sorrendet a munkafolyamat adja. A backlog, az ütemezés és az utókövetés nem állomás | `positions/0008-negy-allomas.md` |
| állomás-futás | tevékenység: egy állomás egyszeri végrehajtása egy munkaterméken; van szereplője, kezdete és vége. Vagy a várt kimenettel zárul, vagy elakadással | `positions/0006-grafmodell.md` |
| andon zsinór | a Toyota-gyárak zsinórja, amellyel bárki megállíthatja a sort, ha hibát lát. Nálunk: elakadás | `positions/0007-elakadas.md` |
| átcsúszási arány (escape rate) | mérőszám: az átcsúszott hibák aránya kapunként és kategóriánként; a bizalom mérőszáma. Külön jelzés nélkül a merge utáni átcsúszást értjük alatta | `positions/0002-emberi-kapuk-es-bizalom.md` |
| átcsúszott hiba (escape) | munkatermék: hiba, amely átjutott egy kapun, és később találták meg. Mindig egy kapuhoz képest értjük; ha a kapu megfogja, az újramunka, nem átcsúszás. Lehet AC-sértés, a szándék sértése teljesült AC mellett (ez a K1-en csúszott át), vagy ki nem mondott elvárás sértése (regresszió, biztonság). Ha az ember meggondolta magát, az új szándék, nem átcsúszás. A besorolása ítélet, kezdetben emberé | `positions/0002-emberi-kapuk-es-bizalom.md` |
| autonómia létrája | ahogy egy kapu kategóriánként halad: ember tételenként dönt → szabály dönt, ember mintát néz → szabály dönt, és a gyár javasolja a szabály módosítását | `elvek.md` |
| autonómia-szint (L0–L5) | a gyár önállóságának skálája a kézi munkától (L0) az önirányítóig (L5). A mi gyárunk L4 | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| backlog | a K0 előtti szándékok nézete, az ember által adottaké és a gyár által javasoltaké együtt; a gráfból levezetett, nem tárolt állapot. Angolul marad | `positions/0008-negy-allomas.md` |
| befogadás (intake) | a szándékok beérkezése a backlogba; nem állomás. Forrás az ember, vagy a gyár (szándék-javaslat) | `positions/0005-scope-conformance.md` |
| beszámoló | munkatermék: a Builder saját leírása arról, mit csinált. A review csak az AC-k és a diff után olvassa | `positions/0005-scope-conformance.md` |
| bizonyíték (evidence) | munkatermék: a PR-hoz csatolt, gyorsan ellenőrizhető igazolás arról, hogy egy AC teljesült a futó rendszeren (e2e eredmény; felületnél képernyőkép vagy felvétel). Négy tulajdonsága van | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| branch | git-ág: a kód egy külön fejlődési vonala. Egy munkadarabhoz egy branch tartozik | |
| build | állomás: az implementáció és a unit tesztek megírása; kimenete commit, PR és beszámoló. Angolul marad | `positions/0008-negy-allomas.md` |
| Builder | a build sáv ágense. Nem minősíti a saját munkáját | `positions/0008-negy-allomas.md` |
| CI (continuous integration) | folyamatos integráció: minden PR-on és merge-en automatikusan lefutó build és teszt | |
| code review | a kód (a diff) emberi átnézése. Nálunk az ember a diffet csak kockázat szerint nézi; a review-t független ágens végzi | `positions/0002-emberi-kapuk-es-bizalom.md` |
| commit | munkatermék: a kód egy rögzített állapota a gitben, egyedi SHA-val | |
| dark factory | „sötét gyár”: autonóm termelés, amelyben ember nem dönt és nem néz át semmit; a gyárvilág lights-out manufacturing fogalmából. Mi elvetjük. Angolul marad | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| diff | két kódállapot különbsége; amit egy PR változtat | |
| diffrész (hunk) | munkatermék: a diff egy összefüggő darabja. A scope-ellenőrzés egysége: mindegyikhez tartoznia kell egy AC-nek | `positions/0005-scope-conformance.md` |
| DORA-mérőszámok | a DevOps-teljesítmény négy mérőszáma (*Accelerate*): telepítési gyakoriság, átfutási idő, hibás változások aránya, helyreállítási idő | `sources.md` |
| e2e (end-to-end) teszt | a futó rendszer tesztje a felhasználó oldaláról, böngészőn vagy API-n át, az összes rétegen keresztül | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| elakadás | munkatermék: az állomás-futás nem a várt kimenetet állítja elő, hanem jelzi, hogy nem tud továbbmenni. Bármelyik sáv jelezheti. Oda mutat, ahol a hiba van (munkadarab, terv, spec vagy szándék), és a feloldásig megállítja a munkadarabot | `positions/0007-elakadas.md` |
| elakadási arány | mérőszám: az elakadással zárult állomás-futások aránya állomásonként és kategóriánként | `positions/0007-elakadas.md` |
| elakadt | mellékállapot: a munkadarab elakadás miatt áll, és a feloldásig ott marad; a gráfból levezetett nézet | `positions/0008-negy-allomas.md` |
| elfogadás | ítélet az eredményről (K3), a landing előtt; vö. jóváhagyás | `positions/0002-emberi-kapuk-es-bizalom.md` |
| ellenőrzés | állomás: a PR head commitjának ellenőrzése két független sávval, párhuzamosan. A QA bizonyítékot állít elő, a Reviewer scope-ítéletet, review-leletet és kockázati besorolást. Ha nem megy át, újramunka; ha átmegy, K3 | `positions/0008-negy-allomas.md` |
| elutasítás | ítélet: a munkatermék az adott verziójában nem megy át a kapun; új verzió kell belőle, vagy elakadás lesz | `positions/0006-grafmodell.md` |
| escape, escape rate | lásd: átcsúszott hiba, átcsúszási arány | |
| eval (kiértékelés) | gépi, ismételhető ellenőrzés egy munkaterméken: teszt, megkötés-ellenőrzés, vagy rubrika szerinti pontozás (LLM mint bíráló). Eredménye eval-ítélet: átment / nem ment át, vagy pontszám. Minden kapu előtt kell, a review-val együtt | `positions/0008-negy-allomas.md` |
| fan-in, fan-out | hány modul hív egy adott modult (fan-in), és hány modult hív ő (fan-out). A nagy fan-in nagy hatókört jelent. Angolul marad | `positions/0004-alacsony-kockazat.md` |
| feature flag | kapcsoló a kódban, amellyel egy funkció merge után is kikapcsolva maradhat. Hogy a félkész szándékot így kezeljük-e, nyitott kérdés | `questions.md` |
| feloldás | ítélet: az ember döntése egy elakadásról: folytat, visszaküld (build, terv, spec, szándék), vagy lezár | `positions/0007-elakadas.md` |
| flaky teszt | olyan teszt, amely ugyanazon a kódon és környezetben néha átmegy, néha elbukik. Okai: időzítés, sorrendfüggés, külső függés, versenyhelyzet. Nálunk fölösleges újramunkát vagy átcsúszott hibát okozhat. Angolul marad | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| független | két futás vagy ítélet független, ha más sáv és más szereplő végzi. Ugyanaz a modell más utasítással más szereplő; hogy ez elég-e, nyitott kérdés | `elvek.md` (E3) |
| gap elemzés | a visszavezethetőség hiányainak keresése: spec AC munkadarab AC nélkül, AC bizonyíték nélkül, diffrész AC nélkül, szándék elfogadás nélkül. Angolul marad | `positions/0008-negy-allomas.md` |
| Goodhart-hatás | ha egy mérőszám céllá válik, megszűnik jó mérőszám lenni. Nálunk: a gyár kijátszhatja a saját mérőszámait | `positions/0004-alacsony-kockazat.md` |
| HAR | HTTP Archive: a böngésző hálózati forgalmának naplófájlja | `experiments.md` |
| hatókör | a változtatás kiterjedése a kód függőségi gráfjában: a közös magot érinti-e, hány hívója van (fan-in). Nem azonos a scope-pal (vö. scope-ellenőrzés) | `positions/0004-alacsony-kockazat.md` |
| human in the loop | „ember a hurokban”: az ember minden lépésnél jóváhagy; az AI-támogatott gyár jele | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| human on the loop | „ember a hurok fölött”: az ember kapunál, mintavételnél és elakadásnál lép be; az AI-natív gyár jele | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| intake | lásd: befogadás | |
| intent | lásd: szándék | |
| invariáns | lásd: megkötés | |
| irányelv | rövid, emberi mondat, amelyből álláspontok és megkötések következnek; mellette ott áll, mely megkötések valósítják meg (E1–E11). A munkánk elvei külön szerepelnek (M1–M4) | `elvek.md` |
| ítélet | munkatermék: egy szereplő (ember, ágens vagy szabály) döntése egy munkatermék adott verziójáról. A fajtái a 0006-ban vannak. A megkötések mondják meg, melyiket ki hozhatja | `positions/0006-grafmodell.md` |
| jóváhagyás | ítélet, mielőtt a munka elindul: K1 a specre, K2 a tervre; vö. elfogadás | `positions/0002-emberi-kapuk-es-bizalom.md` |
| K0, K1, K2, K3 | a négy kapu: K0 a szándék kiválasztása, K1 a spec jóváhagyása, K2 a terv jóváhagyása, K3 az eredmény elfogadása | `positions/0002-emberi-kapuk-es-bizalom.md` |
| kapu | döntési pont, ahol a munka megáll. Mindig van rajta ítélet; a kapu-konfiguráció szerint ember vagy szabály hozza. Kikapcsolt kapu nincs | `positions/0002-emberi-kapuk-es-bizalom.md` |
| kapu-konfiguráció | konfiguráció: kapunként és kategóriánként megmondja, hogy ember vagy melyik szabály hozza a kapu-ítéletet, és mekkora a mintavételi arány | `positions/0002-emberi-kapuk-es-bizalom.md` |
| kártya | lásd: munkadarab | |
| kategória | a munkadarabok csoportja (változtatás-típus és kódterület), amelyre a bizalmat külön mérjük és a kapukat külön állítjuk. Nem azonos a kemény területtel | `positions/0002-emberi-kapuk-es-bizalom.md` |
| kemény kategória | lásd: kemény terület | |
| kemény lista | a kemény területek listája; csak ember élesíti | `positions/0004-alacsony-kockazat.md` |
| kemény terület | olyan terület (például pénz, auth), ahol a K3-at szabály soha nem hozhatja, mindig ember dönt | `positions/0004-alacsony-kockazat.md` |
| kéretlen változás (scope drift) | a diff olyat változtat, amit a munkadarab AC-i nem kértek | `positions/0005-scope-conformance.md` |
| kész | a merge-ölt munkadarabok nézete; nem állomás | `positions/0008-negy-allomas.md` |
| kiválasztás | ítélet (K0): melyik szándékon dolgozzon a gyár, és milyen sorrendben. Prioritás, nem ellenőrzés. Kötegelhető | `positions/0002-emberi-kapuk-es-bizalom.md` |
| kockázat | mi romolhat el × mennyire látjuk × mennyire vonható vissza | `positions/0004-alacsony-kockazat.md` |
| kockázati besorolás | ítélet egy munkadarab kockázatáról, a 0004 öt feltétele szerint. Ágens csak emelheti | `positions/0004-alacsony-kockazat.md` |
| konfiguráció | munkatermék: minden, ami a gyár működését meghatározza: kapu-konfiguráció, küszöbök, mintavételi arányok, korlátok, kemény lista, a szabályok kódja, skillek, ágens-utasítások, munkafolyamat. Csak ember élesíti | `elvek.md` (E8) |
| közös mag | a kódnak az a része, amelyet sok modul használ; ha egy változtatás érinti, nagy a hatóköre | `positions/0004-alacsony-kockazat.md` |
| landing | állomás: a K3-on elfogadott munkadarab gépi bejuttatása a main-be: összevont állapot, CI rajta, sorosítás, merge. Angolul marad | `positions/0008-negy-allomas.md` |
| landing slot | az opus-factory megoldása a sorosításra: egyszerre egy job szinkronizál és merge-öl | `experiments.md` |
| lane | lásd: sáv | |
| lelet (review-lelet) | a review egy találata (például hiba, kéretlen változás). Újramunkát vagy szándék-javaslatot okoz | `positions/0005-scope-conformance.md` |
| levél-modul | olyan modul, amelyet kevés más modul hív (kis fan-in); a függőségi gráf széle | `positions/0004-alacsony-kockazat.md` |
| liveness, safety | a formális módszerek két tulajdonság-fajtája: safety = „rossz dolog soha nem történik meg”, bármely pillanatban ellenőrizhető (ez a megkötés); liveness = „a jó dolog egyszer megtörténik”, egy pillanatban nem dönthető el, megkötés csak időkorláttal lesz belőle. Angolul marad | `positions/0006-grafmodell.md` |
| LLM (large language model) | nagy nyelvi modell, az ágensek alapja. Ha LLM ítél, az ítélet, nem megkötés | `positions/0006-grafmodell.md` |
| main | a fő branch; ide kerül a kész változtatás | `positions/0008-negy-allomas.md` |
| megfigyelés | munkatermék: a gyáron kívülről vagy a mérőszámokból jövő jel (telemetria, riasztás); szándék-javaslat forrása lehet | `positions/0006-grafmodell.md` |
| megkötés (constraint) | a gyár gráfjáról szóló állítás, amely bármely pillanatban eldönthető kizárólag a gráfból, determinisztikus kóddal (nem LLM-mel); mindig igaz kell legyen; a szerkezetről szól, nem a tartalom minőségéről. Fajtái: szerkezeti, őrfeltétel, jogosultsági, sorrendi. Sérülésekor megelőző vagy észlelő, csendben soha. A döntéseink három formájának egyike. Azonosítója I-NNNN-n | `positions/0006-grafmodell.md` |
| mellékállapot | állapot a fő úton kívül; nálunk egy van: elakadt | `positions/0008-negy-allomas.md` |
| merge | git-művelet: egy branch változtatásainak beemelése egy másikba (nálunk a main-be) | |
| merge gate (merge kapu) | a kísérletek fogalma: a merge-et kockázat szerint engedő szabály. Nálunk két részre bomlik: a K3 szabály szerinti elfogadása (0004) és a landing őrfeltétele (I-0008-1). Angolul marad | `positions/0008-negy-allomas.md` |
| merge policy | lásd: merge gate | |
| mérőszám | lekérdezés a gyár gráfján (például átcsúszási arány, elakadási arány, mintavételi arány); a döntéseink három formájának egyike. A küszöbe konfiguráció | `positions/0006-grafmodell.md` |
| mintavétel | a szabály által hozott kapu-ítéletek egy részét utólag ember nézi meg; ebből jön a szabály-ítéletek átcsúszási aránya | `positions/0002-emberi-kapuk-es-bizalom.md` |
| mintavételi arány | mérőszám: a szabály-ítéletek közül hánynak van utólagos emberi mintavételi ítélete, időablakra. A célértéke kapunként konfiguráció | `positions/0002-emberi-kapuk-es-bizalom.md` |
| munkadarab | munkatermék, a gyártás egysége: a terv terméke, saját technikai AC-vel, egy branch, egy PR. Ez halad állomásról állomásra. A board kártyája csak a megjelenése | `topics/fogalmi-modell.md` |
| munkafolyamat (workflow) | konfiguráció: az állomások és a kapuk sorrendje; a vezérlés determinisztikus leírása, nem ágens | `topics/fogalmi-modell.md` |
| munkatermék (work product, artifact) | a gyár gráfjának csomópont-csoportja; a típusai a 0006-ban vannak | `positions/0006-grafmodell.md` |
| orchestrátor | az a vezérlő program vagy ágens, amely a munkát továbbítja az állomások között | `experiments.md` |
| őrfeltétel (guard) | a megkötés egyik fajtája: egy esemény csak akkor történhet meg, ha egy feltétel teljesül (például merge csak zöld CI-vel). A csak bővülő gráfban szerkezeti megkötéssé válik | `positions/0006-grafmodell.md` |
| Planner | a tervezés sáv ágense: specet és tervet ír. Angolul marad | `positions/0008-negy-allomas.md` |
| Playwright | böngészőautomatizáló eszköz e2e tesztekhez | `experiments.md` |
| PR (pull request) | munkatermék: egy branch merge-elésére tett javaslat, a diffel és a bizonyítékkal. A gyár kimenete | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| preview környezet (preview environment) | PR-onként egy, a PR megnyitásától a merge-ig vagy a lezárásig élő környezet, amelyen csak az adott PR head commitja fut; itt készül a bizonyíték. Nem azonos a közös teszt- vagy staging környezettel. Angolul marad | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| PROV (W3C PROV-DM) | a W3C származási adatmodellje (Entity, Activity, Agent); próbakő a gráfmodellünkhöz | `positions/0006-grafmodell.md` |
| QA | sáv az ellenőrzés állomáson: a futó rendszer ellenőrzése a preview környezetben; ez állítja elő a bizonyítékot, a buildtől függetlenül | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| Ready | a munkadarab indítható: érvényes jóváhagyások tartoznak hozzá, és a függőségei készen vannak. A gráfból levezetett nézet. Angolul marad | `positions/0006-grafmodell.md` |
| revert | git-művelet: egy merge-ölt változtatás visszavonása egy új committal | `positions/0004-alacsony-kockazat.md` |
| review | független ágens ítélete egy munkatermékről (review-ítélet), minden kapu előtt. A PR-nál a diff átnézése, ezen belül a scope-ellenőrzés; a tervezésnél a spec és a terv átnézése. Angolul marad | `positions/0008-negy-allomas.md` |
| Reviewer | a review sáv ágense: a K0 előtt a gyár-javasolt szándékot, a tervezés végén a specet és a tervet, az ellenőrzés állomáson a PR-t nézi át | `positions/0008-negy-allomas.md` |
| root-cause hash | a super-board módszere: a hiba okából képzett azonosító, amellyel az azonos okú hibákat számolja | `topics/folyamat-osszevetes.md` |
| sáv (lane) | szerepkör: *ki* végzi a munkát (Planner, Builder, QA, Reviewer, szabály, ember). Egy sávban több állomás lehet, és egy állomáson több sáv is dolgozhat. A függetlenségi szabályok sávok között élnek | `topics/fogalmi-modell.md` |
| scope conformance | lásd: scope-ellenőrzés | |
| scope drift | lásd: kéretlen változás | |
| scope-ellenőrzés (scope conformance) | a review része: a diff minden darabjához tartoznia kell egy AC-nek, amiért készült. Ami mellé nem tartozik, az kéretlen változás. Csak a diff → AC irányt nézi; a visszavezethetőség egyik iránya | `positions/0005-scope-conformance.md` |
| scope-ítélet | ítélet: a scope-ellenőrzés eredménye, vagyis van-e kéretlen változás | `positions/0005-scope-conformance.md` |
| Scrum | elterjedt, emberközpontú agilis keretrendszer (sprint, csapat, backlog); az AI-támogatott folyamat tipikus alapja | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| SHA (head SHA) | a commit egyedi azonosítója; a head SHA a PR legutolsó commitjáé. A bizonyíték és az elfogadás ehhez kötött | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| skill | konfiguráció: újrahasznosítható eljárás vagy tudás, amit az ágens betölt. Angolul marad | `topics/fogalmi-modell.md` |
| sorosítás | egyszerre csak egy munkadarab landol | `positions/0008-negy-allomas.md` |
| spec | munkatermék: a szándék formalizálva. Probléma, felhasználói szintű AC, kockázat, és mi *nincs* benne. A Planner írja, a K1 hagyja jóvá. Angolul marad | `topics/fogalmi-modell.md` |
| staging | közös előéles környezet, ahol több változtatás együtt fut; nem azonos a preview környezettel. A repóban egy branch neve is volt (ma `origin/super-board`) | `experiments.md` |
| szabály | szereplő: determinisztikus kiértékelő kód, amely ítéletet hoz (például a K3-at alacsony kockázatnál). A kódja konfiguráció | `positions/0006-grafmodell.md` |
| szándék (intent) | munkatermék: cél egy változtatásra; a gyár bemenete. Az ember fogalmazza meg, vagy a gyár javasolja (szándék-javaslat). Egy szándékból több munkadarab és több PR lehet. Nem „igény”, mert az igényfelmérés a spec felé húz | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| szándék-javaslat | a gyár által javasolt szándék (review-lelet, átcsúszott hiba, elakadás, telemetria vagy a tanuló hurok nyomán). K0-n megy át, mint bármelyik szándék | `positions/0005-scope-conformance.md` |
| szereplő | a gyár gráfjának csomópont-típusa: aki egy állomás-futást végez vagy ítéletet hoz. Ember, ágens vagy szabály | `positions/0006-grafmodell.md` |
| szoftvergyár (software factory) | rendszer, amely emberi szándékból ágensekkel, skillekkel, munkafolyamatokkal és szabályokkal PR-t állít elő; az ember dönt és validál, a gyár javasol, végrehajt és tanul. Nálunk AI-natív | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| tanuló hurok (learning loop) | a gyár elemzi az eredményeit és a hatékonyságát, és változtatást javasol a saját működésére; az ember dönt róla | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| telemetria | a futó rendszerből gyűjtött működési adat (hibák, használat, teljesítmény); megfigyelésként szándék-javaslat forrása lehet | `positions/0005-scope-conformance.md` |
| terv | munkatermék: a spec megvalósításának módja. Megközelítés, felbontás munkadarabokra, függőségek. A Planner írja, a K2 hagyja jóvá. A felbontás egyetlen helye | `topics/fogalmi-modell.md` |
| tervezés | állomás: a K0-n kiválasztott szándékból a Planner specet és tervet ír, a Reviewer eval-t és review-t végez; utána K1 és K2 | `positions/0008-negy-allomas.md` |
| tevékenység | a gyár gráfjának csomópont-típusa; nálunk az állomás-futás | `positions/0006-grafmodell.md` |
| traceability mátrix | táblázatos nézet két tételcsoport között (például AC × bizonyíték), a cellában a kapcsolattal; a gyár gráfjából levezethető. Angolul marad | `elvek.md` (E9) |
| újramunka-kör | a munkadarab az ellenőrzésből visszamegy a buildbe. A korlátja után elakadás jön | `positions/0007-elakadas.md` |
| utókövetés | a kész után, nem állomás: mintavétel, átcsúszott hibák észlelése; innen jön a tanuló hurok jele | `positions/0008-negy-allomas.md` |
| ütemezés | a vezérlés dolga, nem állomás: melyik munkadarab mikor indul (függőségek, párhuzamosság, WIP limit) | `positions/0008-negy-allomas.md` |
| validation contract | a Factory Missions fogalma: a tervezés előre rögzíti, milyen bizonyíték kell egy feature-höz | `topics/folyamat-osszevetes.md` |
| verzió | egy munkatermék egy állapota. Minden változás új verzió (*új verziója* él); az ítélet mindig egy verzióra vonatkozik | `positions/0006-grafmodell.md` |
| vezérlés | a munkafolyamat végrehajtása: melyik munkadarab mikor melyik állomásra megy. Determinisztikus, nem ágens | `positions/0008-negy-allomas.md` |
| visszavezethetőség (traceability) | tételek összepontozása a lánc mentén, mindkét irányban: szándék ↔ spec AC ↔ munkadarab AC ↔ diffrész ↔ bizonyíték. Fenntartott szó erre a kétirányú összepontozásra (gap elemzés, traceability mátrix); a scope-ellenőrzés csak az egyik iránya | `elvek.md` (E9) |
| WIP limit (work in progress) | hány munkadarab lehet egyszerre folyamatban | `positions/0008-negy-allomas.md` |
| worktree izoláció | minden munkadarab saját git worktree-ben és branchen fut, hogy a párhuzamos munka ne ütközzön | `experiments.md` |
