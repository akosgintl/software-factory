# 0008 — A gyár folyamata: négy állomás

Állapot: 📌 elfogadva · 2026-10-18 · módosítva 2026-10-18 (független ellenőrzés minden kapu előtt;
a K3 a landing előtt, a landing gépi; a mintavétel nem az utókövetés része)

## Kérdés

Milyen állomásokon megy végig a munka? Az első vázlat kilenc állomást tartalmazott (befogadás,
spec, terv, ütemezés, build, QA, review, landing, utókövetés). Ez túl sok.

## Álláspont

Négy állomás, egy mellékállapot, négy kapu (KISS):

Ábra (sávok, állomások, kapuk): [`abrak/gyar-folyamat.html`](../abrak/gyar-folyamat.html), élő
változat: https://claude.ai/artifact/QfdY4btjwQMcAwXPBguZ2H

```
backlog ─[K0]─▶ tervezés ─[K1, K2]─▶ build ⇄ ellenőrzés ─[K3]─▶ landing ─▶ kész
                       bármelyik állomásból ──▶ elakadt ──[ember]──▶ vissza
```

| Állomás | Mit használ | Mit állít elő | Sáv | Utána |
|---|---|---|---|---|
| **tervezés** | a K0-n kiválasztott szándékot | spec (felhasználói szintű AC, kockázat, mi nincs benne) és terv (megközelítés, felbontás munkadarabokra technikai AC-vel, függőségek); utána eval és review | Planner, majd Reviewer | K1 a specre, K2 a tervre |
| **build** | egy Ready munkadarabot és az AC-it; újramunkánál az ellenőrzés leleteit | commit, PR, beszámoló | Builder | ellenőrzés |
| **ellenőrzés** | a PR head commitját, a munkadarab AC-it | QA: bizonyíték AC-nként, preview környezetben. Reviewer: scope-ítélet, review-leletek, kockázati besorolás | QA és Reviewer, párhuzamosan, egymástól függetlenül | átment: K3. Nem ment át: vissza a buildbe (újramunka) |
| **landing** | a K3-on elfogadott PR head commitját és az aktuális main-t | összevont állapot, CI rajta, merge | szabály | kész. Ütközésnél vissza az ellenőrzésre |

**A landing gépi.** A frissítés nem változtatja meg a PR head commitját: a CI egy ideiglenes
összevont állapoton fut (a head és az aktuális main összevonása). Ha az összevonás ütközik, a
feloldás új head commit, és a munkadarab visszamegy az ellenőrzésre (I-0008-2).

**Független ellenőrzés minden kapu előtt** (E2). Minden kapu előtt egy, az előállítótól független
szereplő eval-t (gépi kiértékelés) és review-t végez, akkor is, ha a kapun szabály dönt. Az ember e
fölé kerül, nem helyette van.

| Kapu | Mit ellenőriznek előtte | Ki |
|---|---|---|
| K0 | gyár-javasolt szándéknál: van-e mögötte adat, nem duplikátum-e, ütközik-e mással | Reviewer |
| K1, K2 | szándék → spec: minden elemhez van AC, és nincs kéretlen AC; spec AC → munkadarab AC: a felbontás lefed mindent (gap elemzés); minden AC-hez megadható bizonyíték; a kockázati besorolás | Reviewer, előbb a szándékot olvassa, csak utána a Planner indoklását |
| K3 | bizonyíték AC-nként; scope-ítélet; kockázati besorolás | QA, Reviewer |

Bármelyik állomás-futás zárulhat **elakadással** (0007). Ekkor a munkadarab az *elakadt*
mellékállapotba kerül, és a feloldásig ott marad.

Ami nem állomás:

- **backlog**: a K0 előtti szándékok nézete, a gyár-javasolt szándékokkal együtt. Ott nem dolgozik
  senki.
- **ütemezés**: a vezérlés dolga. A Ready nézet: a munkadarab indítható.
- **utókövetés**: a kész után, a tanuló hurok része (átcsúszott hibák). A mintavétel nem ide
  tartozik: minden szabály-ítéletre vonatkozik, mind a négy kapun (0002).

## Megkötések

- **I-0008-1** Merge csak akkor történhet, ha a CI a PR elfogadott head commitjának és az aktuális
  main-nek az összevont állapotán zöld.
- **I-0008-2** A merge-ölt head commit azonos azzal, amelyre a K3 elfogadás és a bizonyítékok
  vonatkoznak. Ha a head változik (ütközés feloldása), a munkadarab visszamegy az ellenőrzésre.
- **I-0008-3** Egyszerre egy munkadarab landol (sorosítás).
- **I-0008-4** Minden munkatermékre, amelyre kapu-ítélet épül (gyár-javasolt szándék, spec, terv,
  PR), a kapu előtt vonatkozik egy eval- és egy review-ítélet egy, az előállítótól független
  szereplőtől. Akkor is, ha a kapun szabály dönt.

Hol melyik megkötés érvényes:

| Hol | Megkötések |
|---|---|
| K0 | I-0002-5, I-0002-6, I-0008-4 |
| tervezés, K1, K2 | I-0002-1, I-0002-2, I-0002-6, I-0008-4 |
| build | I-0007-3, I-0007-6 |
| ellenőrzés | I-0003-1…4, I-0004-2, I-0004-3, I-0005-1…3 |
| K3 | I-0002-3, I-0002-6, I-0004-1, I-0008-4 |
| landing | I-0008-1…3 |
| mindenhol | I-0002-4, I-0006-1, I-0007-1, I-0007-2, I-0007-4, I-0007-5 |

## Miért

- A közös váz szinte minden vizsgált rendszerben négy lépés: terv → build → ellenőrzés → merge,
  egy „embert kér” mellékállapottal (`topics/folyamat-osszevetes.md`). Mi ehhez a K0-t tesszük
  hozzá.
- A QA és a review egy állomás, mert ugyanazt a PR-t nézik ugyanabban az időben. A függetlenségük a
  sávok között él (0003), nem az állomások sorrendjében.
- A spec és a terv egy állomás, mert ugyanaz a szereplő írja őket egymás után. A K1 és a K2 két
  külön ítélet marad, de egy ülésben is meghozható.
- A K3 a landing előtt van, mert a landing sorosított (I-0008-3). Ha a sorban ember döntene, minden
  munkadarab rá várna. Így a landing tisztán gépi, és az ember a saját tempójában dönt.
- Az I-0008-1…3 a merge sorosítását írja le. A három automatikusan merge-ölő saját kísérletben
  mindhárom megvan valamilyen formában (landing slot, merge gate, sync).

## Mi szólt ellene

- Ha a spec és a terv egy állomás, könnyebb a K1-et és a K2-t „egyben letudni”, és a terv
  átsiklik. Védelem: két külön ítélet, két külön verzióra (I-0002-2).
- Ha a main a K3 és a landing között sokat változik, gyakoribb az ütközés és a visszaküldés az
  ellenőrzésre.
- A publikus rendszerek többsége a merge-et embernél hagyja. Mi alacsony kockázatnál nem (0004).

## Mi változtatná meg

- Ha a tervezés állomás tartósan a leglassabb, és a spec és a terv más szereplőt kíván, akkor
  újra két állomás lesz belőle.
- Ha a landing ütközései miatt sok munkadarab kerül vissza az ellenőrzésre, akkor a build előtti
  ütemezést kell javítani (a fájl-átfedés vizsgálata, ahogy a super-board teszi).
