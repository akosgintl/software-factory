# 0004 — Alacsony kockázat: mikor fogadhat el szabály ember nélkül

Állapot: 📌 elfogadva · 2026-10-16 · módosítva 2026-10-18 (a gyár saját konfigurációja kemény terület,
E8; ki dönti el; hidegindítás)

## Kérdés

A 0003 szerint alacsony kockázatnál a K3 elfogadást szabály is hozhatja, és a PR ember nélkül
merge-ölhető. Mi az alacsony kockázat?

## Álláspont

Kockázat = mi romolhat el × mennyire látjuk × mennyire vonható vissza.

Egy PR akkor alacsony kockázatú, ha **mind az öt feltétel teljesül**. Ha bármelyik nem, a K3-on
ember dönt.

| # | Feltétel | Mit jelent | Ki dönti el |
|---|---|---|---|
| 1 | **Nincs kemény terület** | a PR a kemény lista egyik elemét sem érinti (lent) | szabály a diffen (útvonal, tartalom) |
| 2 | **Egy reverttel visszavonható** | nincs külső mellékhatás (e-mail, fizetés, harmadik fél), és nincs olyan adatírás, amit a revert nem hoz vissza | Reviewer |
| 3 | **Kicsi hatókör** | nem a közös magot érinti, kevés hívója van (fan-in). **A sorok száma nem számít** | szabály a kód függőségi gráfján |
| 4 | **Teljes bizonyíték** | az I-0003-1…4 teljesül, az e2e zöld, a változott kódot teszt fedi, és a scope-ítélet szerint nincs kéretlen változás (0005) | szabály a QA és a Reviewer ítéletein |
| 5 | **Jó előélet** | a kategória mért átcsúszási aránya a küszöb alatt van, elég mintavételi adat mellett. Új kategóriában, amíg nincs elég adat, a feltétel nem teljesül | szabály a mérőszámon |

**Kemény lista:** pénz; auth és jogosultság; adat (séma, migráció, törlés); személyes adat;
publikus API vagy szerződés; infrastruktúra és titkok; új függőség; a gyár saját konfigurációja
(kapu-konfiguráció, küszöb, kemény lista, a szabályok kódja, skill, ágens-utasítás, munkafolyamat;
E8).

Két szabály:

- **A kockázat csak felfelé módosítható.** Az ágens emelheti, csökkenteni csak ember tudja. A
  Builder nem minősíti a saját munkáját.
- **A kemény listát és a küszöböket csak ember élesíti** (I-0002-4). A tanuló hurok javasolhat
  változtatást.

A szabály által elfogadott PR-okra a 0002 mintavétele vonatkozik (alapból 10%). Ebből jön az 5.
feltétel átcsúszási aránya.

## Megkötések

- **I-0004-1** Szabály szereplőjű K3 elfogadás csak akkor *vonatkozhat* egy PR head commitjára, ha
  mind az öt feltételről van teljesült ítélet a táblázatban megadott szereplőtől.
- **I-0004-2** Csak felfelé: ha egy munkadarabnak több kockázati besorolása van, egy későbbi,
  alacsonyabb besorolást csak ember hozhat.
- **I-0004-3** A kockázati besorolást hozó szereplő független a commitot előállítótól.
- ~~**I-0004-4**~~ A kemény lista változása: beolvadt az I-0002-4-be (2026-10-18).
- ~~**I-0004-5**~~ A mintavétel: mérőszám lett (mintavételi arány, 0002).
- ~~**I-0004-6**~~ A gyár saját konfigurációja: beolvadt az I-0002-4-be és a kemény listába.

## Miért

- Az elfogadó nem a diffet nézi (0002), ezért a sorok száma nem az ő terhét méri. A kockázatot az
  méri, hogy mit érint a változtatás, és mennyire látjuk az eredményét.
- A „csak felfelé” szabály és az emberi kézben tartott kemény lista véd a Goodhart-hatás ellen.
- A gyár saját konfigurációja azért kemény terület, mert különben a gyár a saját kapuit lazíthatná
  (E8).
- Az előélet hiánya nem jó előélet. Új kategóriában ezért az ember dönt.

## Mi szólt ellene

- A sorok száma a hibavalószínűség durva, de olcsó jelzője. Elvetettük, mert a hatókör és a
  bizonyíték jobban mér.
- Egy nagy PR könnyen többet változtat, mint amit az AC-k leírnak. Ezt a bizonyíték nem fedi le.
  Pótlék: a scope-ellenőrzés (`positions/0005-scope-conformance.md`).
- 💭 A hatókör a kód függőségi gráfjából jön, nem a munka gráfjából (0006, 7. pont).
- 💭 A visszavonhatóság a Reviewer ítélete. Ellenőrizni csak azt tudjuk, ki mondta
  (`questions.md`).

## Mi változtatná meg

- Ha a mintavétel azt mutatja, hogy a nagy, de kis hatókörű PR-ok átcsúszási aránya magasabb,
  akkor a méret visszakerül jelzőként.
