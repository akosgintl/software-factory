# Fogalmi modell

📌 Elfogadva 2026-10-18 (0. kör). A fogalomtár (`glossary.md`) ábécérendben sorolja a szavakat,
ez a jegyzet a viszonyukat mutatja: mi micsoda, hány az egyhez, ki mit csinál vele.

📌 A modell típusos gráf (`positions/0006-grafmodell.md`): a csomópontok munkatermékek,
tevékenységek és szereplők, az élek típusosak, a kardinalitás élmegkötés. Az alábbi lánc a
*származik* élek nézete, nem maga a modell.

## 1. Munkatermékek: ami végigmegy a soron

```
szándék ─1:1─ spec ─1:1─ terv ─1:N─ kártya ─1:1─ PR ─1:N─ bizonyíték
```

| Fogalom | Ki hozza létre | Mi van benne |
|---|---|---|
| szándék | ember | mit akar elérni és miért, a saját szavaival |
| spec | ágens, ember hagyja jóvá (K1) | probléma, felhasználói szintű AC, kockázat, és mi *nincs* benne |
| terv | ágens, ember hagyja jóvá (K2) | megközelítés, felbontás kártyákra, függőségek |
| kártya | a terv terméke | a gyártás egysége: saját, technikai AC, egy branch, egy PR |
| PR | Build | a változtatás |
| bizonyíték | QA, függetlenül a Buildtől | AC-nként, a commithoz kötve (0003) |

- 📌 **A felbontás egyetlen helye a terv.** Kártya csak a tervből jön. Ezért a K2 erősebb kapu,
  mint korábban gondoltuk (0002).
- 💭 A „kártya” munkanév. Jobb magyar szót keresünk.
- 💭 A szándék : spec arány egyelőre 1:1. Hogy nagy szándéknál 1:N kell-e, az nyitott kérdés
  (`questions.md`).

## 2. Szereplők: aki dolgozik

- **ember**: szándékot ad, kapunál dönt, mintát néz. Később érdemes lehet szétválasztani a szerepeit
  (megrendelő, jóváhagyó).
- **ágens**: munkavégző. Modell, eszközök és utasítás egy szerephez.
- **skill**: újrahasznosítható eljárás vagy tudás, amit az ágens betölt.
- **workflow**: az állomások és a kapuk sorrendje. Determinisztikus vezérlés, nem ágens.

## 3. Állomás és sáv

- **állomás**: egy lépés a soron (spec, terv, build, QA, review, landing). *Mit* csinálunk. Az
  állomások sorrendjét a folyamat (workflow) adja.
- **sáv (lane)**: szerepkör. *Ki* csinálja. Egy sávban több állomás lehet. Egy állomás egy
  sávhoz tartozik.
- 💭 A sáv nem csak vizualizáció. A függetlenségi szabályok sávok között élnek: a Builder nem
  minősíti a saját munkáját (0004), a bizonyítékot másik sáv állítja elő (0003).
- 💭 Az ember is sáv: az ő állomásai a kapuk.

## 4. Döntési pontok: ahol a munka megáll

- **kapu**: döntési pont. Dönthet ember vagy szabály (például merge policy).
- **jóváhagyás**: döntés, *mielőtt* a munka elindul. K1 (spec), K2 (terv).
- **elfogadás**: döntés az *eredményről*. K3.
- **kockázat**, **kategória**: ezek alapján kapcsoljuk a kapukat (0004).
