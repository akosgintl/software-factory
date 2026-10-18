# 0008 — A gyár folyamata: négy állomás

Állapot: 📌 elfogadva · 2026-10-18 · módosítva 2026-10-18 (független ellenőrzés minden kapu előtt)

## Kérdés

Milyen állomásokon megy végig a munka? Az első vázlat kilenc állomást tartalmazott (befogadás,
spec, terv, ütemezés, build, QA, review, landing, utókövetés). Ez túl sok.

## Álláspont

Négy állomás, egy mellékállapot, négy kapu (KISS):

Ábra (sávok, állomások, kapuk): [`abrak/gyar-folyamat.html`](../abrak/gyar-folyamat.html), élő
változat: https://claude.ai/artifact/QfdY4btjwQMcAwXPBguZ2H

```
backlog ─[K0]─▶ tervezés ─[K1, K2]─▶ build ⇄ ellenőrzés ─▶ landing ─[K3]─▶ kész
                       bármelyik állomásból ──▶ elakadt ──[ember]──▶ vissza
```

| Állomás | Mit használ | Mit állít elő | Sáv | Utána |
|---|---|---|---|---|
| **tervezés** | a K0-n kiválasztott szándékot | spec (felhasználói szintű AC, kockázat, mi nincs benne) és terv (felbontás munkadarabokra, függőségek); utána eval és review | Planner, majd Reviewer | K1 a specre, K2 a tervre |
| **build** | egy Ready munkadarabot és az AC-it; újramunkánál az ellenőrzés leleteit | commit, PR, beszámoló | Builder | ellenőrzés |
| **ellenőrzés** | a PR head commitját, a munkadarab AC-it | QA: bizonyíték AC-nként, preview környezetben. Reviewer: scope-ítélet, review-leletek, kockázati besorolás | QA és Reviewer, párhuzamosan, egymástól függetlenül | átment: landing. Nem ment át: vissza a buildbe (újramunka) |
| **landing** | az ellenőrzött PR-t és az aktuális main-t | frissítés a main-re, CI az összevont állapoton, elfogadás (K3), merge | szabály (merge gate), ember a 0004 szerint | kész |

**Független ellenőrzés minden kapu előtt.** Egy emberi kapu kikapcsolása nem kapcsolja ki az
ellenőrzést. Minden kapu előtt egy, az előállítótól független szereplő eval-t (gépi
kiértékelés) és review-t végez. Az ember e fölé kerül, nem helyette van.

| Kapu | Mit ellenőriznek előtte | Ki |
|---|---|---|
| K0 | gyár-javasolt szándéknál: van-e mögötte adat, nem duplikátum-e, ütközik-e mással | Reviewer |
| K1, K2 | szándék → spec: minden elemhez van AC, és nincs kéretlen AC; spec AC → munkadarab AC: a felbontás lefed mindent (visszavezethetőség, gap elemzés); minden AC-hez megadható bizonyíték; a kockázati besorolás | Reviewer, előbb a szándékot olvassa, csak utána a Planner indoklását |
| K3 | bizonyíték AC-nként; scope-ellenőrzés; CI az összevont állapoton | QA, Reviewer, merge gate |

Bármelyik állomás-futás zárulhat **elakadással** (0007). Ekkor a munkadarab az *elakadt*
mellékállapotba kerül, és emberi ítéletig ott marad.

Ami nem állomás:

- **backlog**: a K0 előtti szándékok nézete. Ott nem dolgozik senki.
- **ütemezés**: a vezérlés dolga. A Ready nézet: a munkadarab indítható.
- **utókövetés**: a kész után, a tanuló hurok része (mintavétel, átcsúszott hibák).

Új invariánsok:

- **I-0008-1** Merge csak akkor történhet, ha a CI az összevont állapoton (a PR és az aktuális
  main) zöld.
- **I-0008-2** A K3 elfogadás és a bizonyíték ugyanarra a head SHA-ra vonatkozik, amelyet
  merge-ölünk. Ha a landing közben a head változik (ütközés feloldása), a munkadarab visszamegy az
  ellenőrzésre.
- **I-0008-3** Egyszerre egy munkadarab landol (sorosítás).
- **I-0008-4** Minden munkatermékre, amelyre kapu-ítélet épül (gyár-javasolt szándék, spec, terv,
  PR), a kapu előtt vonatkozik egy eval- és egy review-ítélet egy olyan szereplőtől, amely nem
  azonos az előállítóval. Akkor is, ha a kapun ember dönt, ha szabály dönt, és akkor is, ha a
  kapu ki van kapcsolva.

A többi állomásra a meglévő invariánsok vonatkoznak: tervezés: I-0002-1, -2, -5; build:
I-0007-3; ellenőrzés: I-0003-1…4, I-0004-3, I-0005-1…3; landing: I-0002-3, I-0004-1.

## Miért

- A közös váz szinte minden vizsgált rendszerben négy lépés: terv → build → ellenőrzés → merge,
  egy „embert kér” mellékállapottal (`topics/folyamat-osszevetes.md`). Mi ehhez a K0-t tesszük
  hozzá.
- A QA és a review egy állomás, mert ugyanazt a PR-t nézik ugyanabban az időben. A függetlenségük a
  sávok között él (0003), nem az állomások sorrendjében.
- A spec és a terv egy állomás, mert ugyanaz a szereplő írja őket egymás után. A K1 és a K2 két
  külön ítélet marad, de egy ülésben is meghozható.
- Az I-0008-1…3 a merge sorosítását írja le. Mindhárom saját kísérletben megvan valamilyen
  formában (landing slot, merge gate, sync).

## Mi szólt ellene

- Ha a spec és a terv egy állomás, könnyebb a K1-et és a K2-t „egyben letudni”, és a terv
  átsiklik. Védelem: két külön ítélet, két külön verzióval (I-0002-2).
- A publikus rendszerek többsége a merge-et embernél hagyja. Mi alacsony kockázatnál nem (0004).

## Mi változtatná meg

- Ha a tervezés állomás tartósan a leglassabb, és a spec és a terv más szereplőt kíván, akkor
  újra két állomás lesz belőle.
- Ha a landing ütközései miatt sok munkadarab kerül vissza az ellenőrzésre, akkor a sorosítás
  helyett a build előtti ütemezést kell javítani (fájl-átfedés vizsgálata, ahogy a super-board
  pre-flight teszi).
