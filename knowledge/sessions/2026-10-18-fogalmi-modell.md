# 2026-10-18 — Fogalmi modell és gráf

## Kérdés

Miből áll egy szoftvergyár, melyek a folyamat lépései?

## Amit végiggondoltunk

- 💭 A gyár öt rétege: gyártósor (állomások), minőségkapuk, vezérlés, szerszámok, tanuló hurok.
- 💭 Az állomások: intake, spec, terv, ütemezés, build, ellenőrzés (QA ║ review, újramunka-hurok),
  landing, utókövetés.
- 💭 Négy hiány: a szándék és a PR aránya nem 1:1; nincs kivételkezelés (andon); a K1 két döntést
  mos össze (akarjuk-e, és jól értette-e); a tanuláshoz a merge utáni jel kell.
- 📌 A szándék és a PR aránya 1:N. Ebből jött: előbb a fogalmakat tisztázzuk (0. kör).
- 📌 Fogalmi modell: munkatermékek, szereplők, állomás és sáv, kapuk. A felbontás egyetlen helye a
  terv. A jóváhagyás (a munka előtt) és az elfogadás (az eredményről) külön fogalom.
- 📌 Állomás és sáv: az állomás az, *amit* csinálunk, a sorrendet a folyamat adja; a sáv az, *aki*
  csinálja. A sáv nem csak vizualizáció: a függetlenségi szabályok sávok között élnek.
- 📌 „Szándék” az „intent” helyett. Az „igény” szót elvetettük, mert az igényfelmérés a spec felé
  húz.
- 💭 A „kártya” helyett jelöltek: munkadarab (javasolt), munkalap, tétel. Nincs döntés.
- 📌 Hierarchia helyett típusos gráf. Most leíró modell (A), de minden döntést a működési modell
  (B) vezérel.
- 🔍 Próba: a 0002–0005 álláspontból 16 invariáns lett. Ami nem fért bele, abból három módosítás
  következett a 0006-ban.

## Ahová eljutottunk

- 📌 [`topics/fogalmi-modell.md`](../topics/fogalmi-modell.md)
- 📌 [`positions/0006-grafmodell.md`](../positions/0006-grafmodell.md): típusos, időbeli, csak
  bővülő gráf; három forma: invariáns, ítélet (ember, ágens vagy szabály), mérőszám; az állapot
  levezetett nézet; két gráf (munka és kód).
- 🔍 [`topics/megkotesek.md`](../topics/megkotesek.md): a típusok első változata és a 0002–0005
  invariánsai.
- Fogalomtár: szándék, állomás, sáv, kapu, jóváhagyás, elfogadás, munkatermék, invariáns, ítélet.
  Forrás: W3C PROV-DM.

## Nyitva maradt

- A „kártya” magyar neve.
- Nagy szándéknál a szándék : spec arány 1:N legyen?
- Mitől lesz egy ágens saját állítása ellenőrizhető?
- A folyamat kibontása: kivételkezelés (andon), a K1 kettéválása, utókövetés.

---

## Folytatás: elakadás és magyar szavak

### Amit végiggondoltunk

- 📌 Az elakadás munkatermék. Bármelyik sáv jelezheti, oda mutat, ahol a hiba van, és legfeljebb 3
  újramunka-kör lehet.
- 📌 Az escape tisztázása: átcsúszott hiba, mindig egy kapuhoz képest. Lehet AC-sértés,
  szándék-sértés teljesült AC mellett (K1-hiba), vagy ki nem mondott elvárás sértése. Ha az ember
  meggondolta magát, az új szándék.
- 📌 Elv: mindenki ugyanazt értse alatta. Minden használt fogalom definícióval szerepel a
  fogalomtárban, az angolul maradók is.
- 📌 Szavak: kártya → munkadarab; AC = elfogadási kritérium; escape → átcsúszott hiba; scope
  conformance → scope-ellenőrzés; scope drift → kéretlen változás; workflow → munkafolyamat; intake
  → befogadás. Angolul marad: flaky, preview környezet, dark factory, build, review, QA, Builder,
  Reviewer, landing, backlog, Ready, fan-in, fan-out, spec.
- 📌 A „visszavezethetőség” (traceability) fenntartott szó: a kétirányú összepontozásra (gap
  elemzés, traceability mátrix). A scope-ellenőrzés ennek csak egyik iránya.
- Elvetett szavak: hatókörhűség, beolvasztás, PR-környezet, ingadozó teszt.

### Ahová eljutottunk

- 📌 [`positions/0007-elakadas.md`](../positions/0007-elakadas.md)
- 📌 [`glossary.md`](../glossary.md) teljes; az elv a `CLAUDE.md`-be is bekerült.

---

## Folytatás: K0 és négy állomás

- 📌 K0: a szándék kiválasztása (prioritás), mindig ember, soha nem kapcsolható ki, kötegelhető.
  A 0002 módosult, új invariáns: I-0002-5.
- 🔍 Ellentmondás: a 0005 szerint review-ból munkadarab lesz, a fogalmi modell szerint munkadarab
  csak tervből jöhet. Feljegyezve, később döntünk (`questions.md`).
- 🔍 Összevetés: a három saját kísérlet 5–6 állomással dolgozik, a publikus rendszerek többsége
  néggyel (terv, build, ellenőrzés, merge). A mi vázlatunk kilenc volt.
- 📌 [`positions/0008-negy-allomas.md`](../positions/0008-negy-allomas.md): tervezés, build,
  ellenőrzés, landing, plusz az elakadt mellékállapot. A backlog, az ütemezés és az utókövetés nem
  állomás. Új sáv: Planner.
- 💭 Három ötlet a többiektől: a bizonyíték előre rögzítve (Factory Missions), rejtett
  forgatókönyvek (StrongDM), az azonos okú hiba számolása (super-board). Mind a `questions.md`-be
  került.
- Javítás: a super-board az `origin/super-board` branchen van, nem a `staging`-en.

---

## Folytatás: ábra, független ellenőrzés, irányelvek

- 📌 Folyamatábra: `abrak/gyar-folyamat.html`, élő változat:
  https://claude.ai/artifact/QfdY4btjwQMcAwXPBguZ2H
- 📌 Minden kapu előtt eval és review egy független szereplőtől, a kikapcsolt kapuk előtt is
  (I-0008-4). A tervezésen belül: Planner → Reviewer → K1/K2.
- 📌 Elakadás után: alapból ott folytatódik, ahol elakadt; az ember visszaküldheti a buildbe, a
  tervre, a specre vagy a szándékra, vagy lezárhatja. Előre ugrani nem lehet (0007).
- 📌 Az autonómia úgy nő, hogy az ember tételek helyett szabályokról dönt. A K0 is lehet nem
  kötelező tételenként, ha ember által írt szabály választ. A 0001 kiegészült.
- 📌 [`elvek.md`](../elvek.md): irányelvek (E1–E7) invariánsokkal, és a munkánk elvei (M1–M3).

---

## Folytatás: E8 és a megkötés pontos jelentése

- 📌 E8: a szabályt soha nem élesíti a gyár maga. A gyár saját szabályai és működése kemény
  kategória lett a 0004-ben (akkor I-0004-6).
- 📌 Mi a megkötés (0006, 4., 4a–4c): bármely pillanatban, kizárólag a gráfból, determinisztikus
  kóddal eldönthető, mindig igaz, a szerkezetről szól. Négy fajtája van; sérülésekor megelőző vagy
  észlelő, csendben soha. Az alakja rögzített, a paramétere konfiguráció.
- 📌 Az I-0004-5 (mintavétel) statisztikai volt, ezért mérőszám lett küszöbbel.
- Szó: „invariáns” helyett „megkötés”. Az `I-` előtag maradt.

---

## Folytatás: konzisztencia-vizsgálat

### Kérdés

Vannak-e a repóban ellentmondások, kimaradt és redundáns tételek? A vizsgálat 11 ellentmondást,
5 kétértelmű fogalmat, 11 kimaradt tételt és 8 redundanciát talált. Mindet átvezettük.

### Ahová eljutottunk

- 📌 **A gyár AI-natív.** Ez már nem kérdés. A 0001 kiegészült (7. pont, a két pólus és az L0–L5
  skála), a `topics/ai-nativ-vs-ai-tamogatott.md` beolvadt.
- 📌 **Minden kapun mindig van ítélet**, ember vagy ember által jóváhagyott szabály hozza, a
  kapu-konfiguráció szerint, kategóriánként; szabálynál mintavétellel (0002). Kikapcsolt kapu
  nincs. A K0 és a K3 ugyanazt a létrát járja, mint a K1 és a K2. Új megkötés: I-0002-6.
  Hidegindítás: új kategóriában ember dönt.
- 📌 **A szabály szereplő**: determinisztikus kiértékelő kód. Amit az E8 véd, az a
  **konfiguráció** (a szabályok kódja is). Az I-0004-4 és az I-0004-6 beolvadt az I-0002-4-be.
- 📌 **Minden gyár-javaslat szándék-javaslat**, K0-n megy át (0005). Munkadarab csak tervből jön.
  Az I-0005-4 visszavonva.
- 📌 **A K3 a landing előtt van, a landing gépi** (0008). A frissítés nem változtatja a head
  commitot; ütközésnél vissza az ellenőrzésre.
- 📌 Szavak: „hatókör-ítélet” → scope-ítélet; „kemény kategória” → kemény terület; a kategória
  változtatás-típus és kódterület (a kockázat nem dimenziója); független = más sáv, más szereplő.
- 📌 Bizonyíték: e2e mindig; képernyőkép vagy felvétel csak felületet érintő AC-nél; a gyár
  konfigurációját változtató PR-nál eval-futás (0003).
- 📌 A zárt típuslista a 0006-ba került, új csomópont: megfigyelés; új él: *hozta*; új megkötés:
  I-0006-1 (csak bővülő gráf).
- 📌 Irányelvek: E9 (visszavezethetőség), E10 (inkább megáll), E11 (a main-be az kerül, amit
  ellenőriztek és elfogadtak); M4 (egy állítás egy helyen). Mind a 27 megkötésnek van irányelve.
- 🔍 Negyedik kísérlet: `warpdotdev-factory` (`experiments.md`, `topics/folyamat-osszevetes.md`).
- Beolvadt és törölve: `topics/alacsony-kockazat.md` (a 0004-be), `topics/megkotesek.md` (a
  megkötések az álláspontokba, a típuslista a 0006-ba), `topics/ai-nativ-vs-ai-tamogatott.md` (a
  0001-be).

### Nyitva maradt

- Mikor független két ágens (más modell kell-e)?
- Kell-e merge utáni biztosíték az alacsony kockázathoz?
- Mit csinál a Warp scorer `selfImprovement` beállítása, és sérti-e az E8-at?
- A kísérletekről három kérdés átkerült az `experiments.md`-ből a `questions.md`-be.

## Kiegészítés: az ábra ellenőrzése, mintavétel minden kapun

- 📌 **A mintavétel minden szabály-ítéletre vonatkozik, mind a négy kapun** (0002, 5. pont). Az
  ábra és a 0008 az utókövetéshez kötötte, ez szűkítés volt. Az utókövetés most az átcsúszott
  hibák észlelése; a mintavétellel együtt adja a tanuló hurok jelét.
- 📌 Nem lett külön irányelv (KISS): az E4 mondja ki, hogy a szabály ítéleteiből az ember mindig
  mintát néz, és a létra 3. fokán is van mintavétel.
- Ábra (`abrak/gyar-folyamat.html`, artifact 4. verzió): mintavétel-vonal mind a négy kapu
  szabály-felétől; a jobb szélen „átcsúszott hiba”; a K3 kártyán I-0002-6; „max N kör (alapból
  3)”; jelmagyarázat és forrás-lábléc kiegészítve.
