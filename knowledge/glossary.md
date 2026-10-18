# Fogalomtár

Közös szókincs, ábécérendben. **Elv: mindenki ugyanazt értse alatta.** Minden fogalom, amit a
jegyzetekben használunk, itt definícióval szerepel. Azok is, amelyek angolul maradnak, és azok is,
amelyeket „mindenki ismer”. Ha egy fogalom jelentése vitatott, a hozzá tartozó jegyzetre mutatunk.

| Fogalom | Jelentés | Bővebben |
|---|---|---|
| AC (acceptance criteria) | elfogadási kritérium: gép által ellenőrizhető állítás arról, mikor kész egy spec vagy egy munkadarab. A spec AC-je felhasználói szintű, a munkadarabé technikai | `topics/fogalmi-modell.md` |
| AI-natív szoftvergyár | olyan gyár, amelynek a folyamatát az ágensekre tervezték; az ember a hurok fölött áll | `topics/ai-nativ-vs-ai-tamogatott.md` |
| AI-támogatott szoftvergyár | meglévő, emberközpontú folyamat, amelyben az AI eszköz; az ember a hurokban áll | `topics/ai-nativ-vs-ai-tamogatott.md` |
| ágens (agent) | szereplő: modell, eszközök és utasítás egy szerephez; önállóan több lépést hajt végre | `topics/fogalmi-modell.md` |
| állomás | egy lépés a soron. Négy van: tervezés, build, ellenőrzés, landing. *Mit* csinálunk; a sorrendet a munkafolyamat adja. A backlog, az ütemezés és az utókövetés nem állomás | `topics/fogalmi-modell.md` |
| állomás-futás | tevékenység: egy állomás egyszeri végrehajtása egy munkaterméken; van szereplője, kezdete és vége. Vagy a várt kimenettel zárul, vagy elakadással | `positions/0006-grafmodell.md` |
| andon zsinór | a Toyota-gyárak zsinórja, amellyel bárki megállíthatja a sort, ha hibát lát. Nálunk: elakadás | `positions/0007-elakadas.md` |
| átcsúszási arány (escape rate) | az átcsúszott hibák aránya kapunként és kategóriánként; a kapu és a bizalom mérőszáma. Külön jelzés nélkül a merge utáni átcsúszást értjük alatta | `positions/0004-alacsony-kockazat.md` |
| átcsúszott hiba (escape) | hiba, amely átjutott egy kapun, és később találták meg. Mindig egy kapuhoz képest értjük; ha a kapu megfogja, az újramunka, nem átcsúszás. Lehet AC-sértés, a szándék sértése teljesült AC mellett (ez a K1-en csúszott át), vagy ki nem mondott elvárás sértése (regresszió, biztonság). Ha az ember meggondolta magát, az új szándék, nem átcsúszás. A besorolása ítélet, kezdetben emberé | `positions/0007-elakadas.md` |
| autonómia létrája | ahogy egy kapu kategóriánként halad: ember tételenként dönt → szabály dönt, ember mintát néz → szabály dönt, a gyár javasolja a szabály módosítását, ember hagyja jóvá. A szabályt soha nem élesíti a gyár | `elvek.md` |
| backlog | a még nem indítható munkadarabok és szándékok nézete; a gráfból levezetett, nem tárolt állapot. Angolul marad | `positions/0006-grafmodell.md` |
| befogadás (intake) | a szándékok beérkezése a backlogba, nem állomás. Forrás az ember, vagy a gyár javaslata (telemetria, átcsúszott hiba, refaktor). Hogy mit építünk, arról az ember dönt | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| beszámoló | munkatermék: a Builder saját leírása arról, mit csinált. A review csak az AC-k és a diff után olvassa | `positions/0005-scope-conformance.md` |
| bizonyíték (evidence) | munkatermék: a PR-hoz csatolt, emberi szemmel gyorsan ellenőrizhető igazolás (képernyőkép a futásról, e2e eredmény). AC-nként, a head commithoz kötve, független sávtól, preview környezetben | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| branch | git-ág: a kód egy külön fejlődési vonala. Egy munkadarabhoz egy branch tartozik | |
| build | állomás: az implementáció és a unit tesztek megírása; kimenete commit, PR és beszámoló. Angolul marad | `positions/0008-negy-allomas.md` |
| Builder | a build sáv ágense. Nem minősíti a saját munkáját | `positions/0004-alacsony-kockazat.md` |
| CI (continuous integration) | folyamatos integráció: minden PR-on és merge-en automatikusan lefutó build és teszt | |
| commit | munkatermék: a kód egy rögzített állapota a gitben, egyedi SHA-val | |
| dark factory | „sötét gyár”: autonóm termelés, amelyben ember nem ír és nem néz át kódot; a gyárvilág lights-out manufacturing fogalmából. Mi elvetjük. Angolul marad | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| diff | két kódállapot különbsége; amit egy PR változtat | |
| diffrész (hunk) | munkatermék: a diff egy összefüggő darabja. A scope-ellenőrzés egysége: mindegyikhez tartoznia kell egy AC-nek, amiért készült | `topics/invariansok.md` |
| e2e (end-to-end) teszt | a futó rendszer tesztje a felhasználó oldaláról, böngészőn vagy API-n át, az összes rétegen keresztül | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| elakadt | mellékállapot: a munkadarab elakadás miatt áll, és emberi ítéletig ott marad; a gráfból levezetett nézet | `positions/0008-negy-allomas.md` |
| elakadás | munkatermék: az állomás-futás nem a várt kimenetet állítja elő, hanem jelzi, hogy nem tud továbbmenni. Bármelyik sáv jelezheti. Oda mutat, ahol a hiba van (munkadarab, terv vagy spec), és emberi ítéletig megállítja a munkadarabot | `positions/0007-elakadas.md` |
| elfogadás | ítélet az eredményről (K3); vö. jóváhagyás | `topics/fogalmi-modell.md` |
| ellenőrzés | állomás: a PR head commitjának ellenőrzése két független sávval, párhuzamosan. A QA bizonyítékot állít elő, a Reviewer scope-ítéletet, review-leletet és kockázati besorolást. Ha nem megy át, újramunka | `positions/0008-negy-allomas.md` |
| eval (kiértékelés) | gépi, ismételhető ellenőrzés egy munkaterméken: teszt, invariáns-ellenőrzés, vagy rubrika szerinti pontozás (LLM mint bíráló). Eredménye átment / nem ment át, vagy pontszám. Minden kapu előtt kell, a review-val együtt | `positions/0008-negy-allomas.md` |
| escape, escape rate | lásd: átcsúszott hiba, átcsúszási arány | |
| fan-in, fan-out | hány modul hív egy adott modult (fan-in), és hány modult hív ő (fan-out). A nagy fan-in nagy hatókört jelent (0004). Angolul marad | `positions/0004-alacsony-kockazat.md` |
| feature flag | kapcsoló a kódban, amellyel egy funkció merge után is kikapcsolva maradhat. Így a félkész szándék munkadarabjai is merge-ölhetők | |
| flaky teszt | olyan teszt, amely ugyanazon a kódon és környezetben néha átmegy, néha elbukik. Okai: időzítés, sorrendfüggés, külső függés, versenyhelyzet. Nálunk fölösleges újramunkát vagy átcsúszott hibát okozhat. Angolul marad | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| gap elemzés | a visszavezethetőség hiányainak keresése: AC bizonyíték nélkül, diffrész AC nélkül, szándék elfogadás nélkül. Angolul marad | |
| Goodhart-hatás | ha egy mérőszám céllá válik, megszűnik jó mérőszám lenni. Nálunk: a gyár kijátszhatja a saját mérőszámait | `positions/0004-alacsony-kockazat.md` |
| human in the loop | „ember a hurokban”: az ember minden lépésnél jóváhagy | `topics/ai-nativ-vs-ai-tamogatott.md` |
| human on the loop | „ember a hurok fölött”: az ember felügyel, és csak kivételnél vagy kapunál lép be | `topics/ai-nativ-vs-ai-tamogatott.md` |
| intake | lásd: befogadás | |
| intent | lásd: szándék | |
| invariáns | a gyár gráfján gépi úton ellenőrizhető szabály; a döntéseink három formájának egyike (invariáns, ítélet, mérőszám) | `positions/0006-grafmodell.md` |
| irányelv | rövid, emberi mondat, amelyből álláspontok és invariánsok következnek; mellette ott áll, mely invariánsok valósítják meg (E1–E7). A munkánk elvei külön szerepelnek (M1–M3) | `elvek.md` |
| ítélet | munkatermék: egy szereplő (ember, ágens vagy szabály) döntése egy munkatermék adott verziójáról. Fajtái: kiválasztás, jóváhagyás, elfogadás, elutasítás, kockázati besorolás, hatókör-ítélet, mintavételi ítélet. Az invariánsok mondják meg, melyiket ki hozhatja | `positions/0006-grafmodell.md` |
| jóváhagyás | ítélet, mielőtt a munka elindul: K1 a specre, K2 a tervre; vö. elfogadás | `topics/fogalmi-modell.md` |
| K0, K1, K2, K3 | a négy emberi kapu: K0 a szándék kiválasztása (mindig él), K1 a spec jóváhagyása, K2 a terv jóváhagyása, K3 az eredmény elfogadása (mindig él) | `positions/0002-emberi-kapuk-es-bizalom.md` |
| kapu | döntési pont, ahol a munka megáll; dönthet ember vagy szabály. Kategóriánként be- és kikapcsolható, a K0 és a K3 mindig él | `positions/0002-emberi-kapuk-es-bizalom.md` |
| kártya | lásd: munkadarab | |
| kategória | a munkadarabok csoportja, amelyre a bizalmat és a kapukat külön mérjük és kapcsoljuk: változtatás-típus, kockázat, kódterület | `positions/0002-emberi-kapuk-es-bizalom.md` |
| kemény kategória | olyan terület, ahol automatikus merge soha nem lehet: pénz, auth és jogosultság, adat, személyes adat, publikus API, infrastruktúra és titkok, új függőség. A listát csak ember változtatja | `positions/0004-alacsony-kockazat.md` |
| kéretlen változás (scope drift) | a diff olyat változtat, amit a munkadarab AC-i nem kértek | `positions/0005-scope-conformance.md` |
| kiválasztás | ítélet (K0): melyik szándékon dolgozzon a gyár, és milyen sorrendben. Prioritás, nem ellenőrzés. Mindig ember hozza, a gyár által javasolt szándékra is; soha nem kapcsolható ki; kötegelhető | `positions/0002-emberi-kapuk-es-bizalom.md` |
| kockázat | mi romolhat el × mennyire látjuk × mennyire vonható vissza | `positions/0004-alacsony-kockazat.md` |
| kockázati besorolás | ítélet egy munkadarab kockázatáról. Csak felfelé módosítható: ágens emelheti, csökkenteni csak ember | `positions/0004-alacsony-kockazat.md` |
| landing | állomás: az ellenőrzött munkadarab bejuttatása a main-be: frissítés a main-re, sorosítás (egyszerre egy), CI az összevont állapoton, K3, merge. Angolul marad | `positions/0008-negy-allomas.md` |
| lane | lásd: sáv | |
| merge | git-művelet: egy branch változtatásainak beemelése egy másikba (nálunk a main-be) | |
| merge kapu (merge gate) | szabályalapú döntési pont: automatikus merge, vagy emberi elfogadás kockázat szerint | `positions/0004-alacsony-kockazat.md` |
| mérőszám | lekérdezés a gyár gráfján (például átcsúszási arány, elakadási arány); a döntéseink három formájának egyike. A küszöbe konfiguráció, emberi ítélettel változik | `positions/0006-grafmodell.md` |
| mintavétel | az automatikusan merge-ölt PR-ok egy részét (most 10%) utólag ember nézi meg; ebből jön az átcsúszási arány | `positions/0004-alacsony-kockazat.md` |
| munkadarab | munkatermék, a gyártás egysége: a terv terméke, saját technikai AC-vel, egy branch, egy PR. Ez halad állomásról állomásra. A board kártyája csak a megjelenése | `topics/fogalmi-modell.md` |
| munkafolyamat (workflow) | az állomások és a kapuk sorrendje; determinisztikus vezérlés, nem ágens | `topics/fogalmi-modell.md` |
| munkatermék (work product, artifact) | a gyár gráfjának csomópont-típusa: szándék, spec, AC, terv, munkadarab, commit, diffrész, PR, bizonyíték, beszámoló, ítélet, elakadás, átcsúszott hiba, konfiguráció | `positions/0006-grafmodell.md` |
| Planner | a tervezés sáv ágense: specet és tervet ír. Angolul marad | `positions/0008-negy-allomas.md` |
| PR (pull request) | munkatermék: egy branch merge-elésére tett javaslat, a diffel és a bizonyítékkal. A gyár kimenete | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| preview környezet (preview environment) | PR-onként egy, a PR megnyitásától a merge-ig vagy a lezárásig élő környezet, amelyen csak az adott PR head commitja fut; itt készül a bizonyíték. Nem azonos a közös UAT-val, staginggel vagy integrációs környezettel. Angolul marad | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| QA | sáv az ellenőrzés állomáson: a futó rendszer ellenőrzése (e2e, képernyőkép) a preview környezetben; ez állítja elő a bizonyítékot, a buildtől függetlenül | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| Ready | a munkadarab indítható: érvényes jóváhagyások tartoznak hozzá, és a függőségei készen vannak. A gráfból levezetett nézet. Angolul marad | `positions/0006-grafmodell.md` |
| revert | git-művelet: egy merge-ölt változtatás visszavonása egy új committal | `positions/0004-alacsony-kockazat.md` |
| review | független ágens ítélete egy munkatermékről, minden kapu előtt. A PR-nál a diff átnézése, ezen belül a scope-ellenőrzés; a tervezésnél a spec és a terv átnézése (visszavezethetőség, ellenőrizhetőség). Angolul marad | `positions/0005-scope-conformance.md` |
| Reviewer | a review sáv ágense: a tervezés végén a specet és a tervet, az ellenőrzés állomáson a PR-t nézi át, a K0 előtt a gyár-javasolt szándékot | `positions/0005-scope-conformance.md` |
| sáv (lane) | szerepkör: *ki* végzi az állomást (Planner, Builder, QA, Reviewer, szabály, ember). Egy sávban több állomás lehet. A függetlenségi szabályok sávok között élnek | `topics/fogalmi-modell.md` |
| scope conformance | lásd: scope-ellenőrzés | |
| scope drift | lásd: kéretlen változás | |
| scope-ellenőrzés (scope conformance) | a review része: a diff minden darabjához tartoznia kell egy AC-nek, amiért készült. Ami mellé nem tartozik, az kéretlen változás. Csak a diff → AC irányt nézi; a visszavezethetőség egyik iránya | `positions/0005-scope-conformance.md` |
| SHA (head SHA) | a commit egyedi azonosítója; a head SHA a PR legutolsó commitjáé. A bizonyíték és az elfogadás ehhez kötött | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| skill | újrahasznosítható eljárás vagy tudás, amit az ágens betölt. Angolul marad | `topics/fogalmi-modell.md` |
| spec | munkatermék: a szándék formalizálva. Probléma, felhasználói szintű AC, kockázat, és mi *nincs* benne. Ágens írja, ember hagyja jóvá (K1). Angolul marad | `topics/fogalmi-modell.md` |
| szándék (intent) | munkatermék: az ember által megfogalmazott cél egy változtatásra, a saját szavaival; a gyár bemenete. Egy szándékból több munkadarab és több PR lehet. Nem „igény”, mert az igényfelmérés a spec felé húz | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| szereplő | a gyár gráfjának csomópont-típusa: aki egy állomás-futást végez vagy ítéletet hoz. Ember, ágens vagy szabály | `positions/0006-grafmodell.md` |
| szoftvergyár (software factory) | rendszer, amely emberi szándékból ágensekkel, skillekkel és munkafolyamatokkal PR-t állít elő; az ember dönt és validál, a gyár javasol, végrehajt és tanul | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| tanuló hurok (learning loop) | a gyár elemzi az eredményeit és a hatékonyságát, és változtatást javasol a saját működésére; az ember dönt róla | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| terv | munkatermék: a spec megvalósításának módja. Megközelítés, felbontás munkadarabokra, függőségek. Ágens írja, ember hagyja jóvá (K2). A felbontás egyetlen helye | `topics/fogalmi-modell.md` |
| tervezés | állomás: a K0-n kiválasztott szándékból a Planner specet és tervet ír, a Reviewer eval-t és review-t végez; utána K1 és K2. A felbontás egyetlen helye | `positions/0008-negy-allomas.md` |
| tevékenység | a gyár gráfjának csomópont-típusa; nálunk az állomás-futás | `positions/0006-grafmodell.md` |
| traceability mátrix | táblázatos nézet két tételcsoport között (például AC × bizonyíték), a cellában a kapcsolattal; a gyár gráfjából levezethető. Angolul marad | |
| újramunka-kör | a munkadarab az ellenőrzésből (QA, review) visszamegy a buildbe. Legfeljebb 3, utána elakadás | `positions/0007-elakadas.md` |
| utókövetés | a kész után, nem állomás: mintavétel, átcsúszott hibák észlelése; innen jön a tanuló hurok jele | `topics/fogalmi-modell.md` |
| ütemezés | a vezérlés dolga, nem állomás: melyik munkadarab mikor indul (függőségek, párhuzamosság, WIP limit) | `topics/fogalmi-modell.md` |
| visszavezethetőség (traceability) | tételek összepontozása a lánc mentén, mindkét irányban: szándék ↔ spec AC ↔ munkadarab AC ↔ diffrész ↔ bizonyíték. Fenntartott szó: erre a kétirányú összepontozásra használjuk (gap elemzés, traceability mátrix), a scope-ellenőrzés csak az egyik iránya | |
| worktree izoláció | minden munkadarab saját git worktree-ben és branchen fut, hogy a párhuzamos munka ne ütközzön | `experiments.md` |
