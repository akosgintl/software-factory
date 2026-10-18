# Megkötések és ítéletek a 0002–0005 állásponton

🔍 2026-10-18. A 0006 első próbája: végigmegyünk a 0002–0005 állásponton, és mindegyikből kiírjuk,
mi megkötés, mi ítélet, és mi az, ami egyik formába sem fér bele.

📌 Mi a megkötés, milyen fajtái vannak, és mi történik, ha sérül:
`positions/0006-grafmodell.md` 4., 4a–4c. pont.

## Típusok (első változat)

💭 Csomópontok:

| Csoport | Típus | Megjegyzés |
|---|---|---|
| munkatermék | szándék, spec, AC, terv, munkadarab, commit, diffrész, PR, bizonyíték, beszámoló | a diffrész a commit egy darabja (hunk); a beszámoló a Builder saját leírása |
| munkatermék | ítélet | kiválasztás, jóváhagyás, elfogadás, elutasítás, kockázati besorolás, hatókör-ítélet, mintavételi ítélet |
| munkatermék | konfiguráció | kemény kategóriák listája, küszöbök, kapuk be- és kikapcsolása kategóriánként |
| munkatermék | átcsúszott hiba | egy kapun átjutott, később talált hiba |
| tevékenység | állomás-futás | attribútum: állomás, sáv, kezdet, vég |
| szereplő | ember, ágens, szabály | a szabály determinisztikus kód (például merge policy) |

💭 Élek:

| Él | Honnan → hová | Jelentés |
|---|---|---|
| *származik* | spec → szándék, terv → spec, munkadarab → terv, munkadarab → munkadarab | ebből jött létre |
| *része* | AC → spec, AC → munkadarab, diffrész → commit | |
| *új verziója* | munkatermék → munkatermék | a spec, a terv vagy a head változott |
| *teljesít* | diffrész → AC | ezért a darabért van ez a változás |
| *igazol* | bizonyíték → AC | |
| *vonatkozik* | ítélet → munkatermék egy verziója | miről szól az ítélet |
| *függ* | munkadarab → munkadarab | |
| *okozta* | átcsúszott hiba → commit | |
| *átengedte* | átcsúszott hiba → ítélet | melyik kapun jutott át |
| *előállította* | munkatermék → állomás-futás | |
| *használta* | állomás-futás → munkatermék | időbélyeggel |
| *végezte* | állomás-futás → szereplő | |

## 0002 — Emberi kapuk és bizalom

**Megkötések**

- **I-0002-1** Ha egy kategóriában a K1 be van kapcsolva, akkor minden munkadarabtól a *származik*
  élek egy olyan spechez vezetnek, amelyre ember jóváhagyó ítélete *vonatkozik*. A K2-re ugyanez a
  tervvel.
- **I-0002-2** A jóváhagyás egy verzióra vonatkozik. Ha a specnek vagy a tervnek *új verziója* van,
  a régi jóváhagyás nem érvényes rá.
- **I-0002-3** Minden merge-ölt PR-ra vonatkozik egy elfogadás. Hogy ki hozhatja, azt a 0004 mondja
  meg.
- **I-0002-4** A kapu-konfiguráció minden változására vonatkozik egy ember ítélete.
- **I-0002-5** Spec csak olyan szándékra készülhet, amelyre ember kiválasztó ítélete (K0)
  vonatkozik. A K0 nem kapcsolható ki.

**Ítéletek:** K0 (ember, mindig), K1 (ember), K2 (ember), K3 (ember vagy szabály), egy kapu ki- vagy bekapcsolása
(ember, a tanuló hurok javaslata alapján).

**Ami nem fér bele:** „a bizalmat mérjük”. Ez se nem megkötés, se nem ítélet, hanem
**lekérdezés** a gráfon: az átcsúszott hibák aránya kapunként és kategóriánként.

## 0003 — A vég a PR, bizonyítékkal

**Megkötések**

- **I-0003-1** A munkadarab minden AC-jére *igazol* legalább egy bizonyíték.
- **I-0003-2** A bizonyítékot előállító futás *használta* a PR aktuális head commitját. Ha a head
  változik, a bizonyíték elavul.
- **I-0003-3** A bizonyítékot előállító futás sávja más, mint a commitot előállító futásé.
- **I-0003-4** A bizonyítékok között van e2e eredmény és képernyőkép, és a futás
  preview környezetben készült.

**Ítéletek:** K3, a bizonyíték alapján, a szándékhoz és az AC-hez képest.

**Ami nem fér bele:**
- 💭 A környezet nincs a típuslistán. Az I-0003-4 csak attribútumként ellenőrizhető, amit a
  QA-ágens maga állít. Ez gyenge pont.
- 💭 „A diffet csak kockázat szerint nézi.” A gráf rögzítheti, hogy az elfogadó *használta* a
  diffet. Azt nem tudja, hogy tényleg meg is nézte.

## 0004 — Alacsony kockázat

**Megkötések**

- **I-0004-1** Szabály szereplőjű elfogadás csak akkor vonatkozhat egy PR-ra, ha mind az öt
  feltétel igaz:
  1. a kockázati besorolás szerint nem érint kemény kategóriát,
  2. a besorolás szerint egy reverttel visszavonható,
  3. a hatókör kicsi (lásd alább),
  4. az I-0003-1…4 teljesül, a lefedettség elég, és van „nincs kéretlen változás” ítélet (0005),
  5. a kategória átcsúszási aránya a küszöb alatt van.
- **I-0004-2** Csak felfelé: ha egy munkadarabnak több kockázati besorolása van, egy későbbi,
  alacsonyabb besorolást csak ember hozhat.
- **I-0004-3** A munkadarabra vonatkozó kockázati besorolást nem hozhatja az a szereplő, amelyik a
  commitot előállította.
- **I-0004-4** A kemény kategóriák listájának minden változására ember ítélete vonatkozik.
- ~~**I-0004-5**~~ Átsorolva mérőszámnak (2026-10-18): **mintavételi arány** = a szabály által
  elfogadott PR-ok közül hánynak van utólagos emberi mintavételi ítélete, időablakra. Ha 10% alá
  esik, a gyár riaszt. Az azonosító nem kerül újra kiosztásra.
- **I-0004-6** A gyár saját szabályait vagy működését változtató PR (konfiguráció, küszöb, kemény
  lista, skill, ágens-utasítás, munkafolyamat) kemény kategória: elfogadó ítéletét csak ember hozhatja.
  Ennek a gyár által előállított változata javaslat marad, amíg ember jóvá nem hagyja (E8).

**Ítéletek:** kockázati besorolás (ágens vagy szabály), emberi elfogadás a nem alacsony
kockázatnál, mintavételi ítélet, a küszöbök és a lista módosítása.

**Ami nem fér bele:**
- 💭 A hatókör (fan-in, közös mag) nem a munka gráfjából jön, hanem a **kód függőségi gráfjából**.
  Ez egy második gráf.
- 💭 A visszavonhatóság ágens ítélete. Ellenőrizni nem tudjuk, csak azt, hogy ki mondta.
- 🔍 Az I-0004-5 statisztikai volt, időablakra; egy pillanatra nem dönthető el. Ezért mérőszám
  lett küszöbbel (0006, 4a).

## 0005 — Scope-ellenőrzés

**Megkötések**

- **I-0005-1** A PR minden diffrészéből *teljesít* él vezet a munkadarab egy AC-jéhez.
- **I-0005-2** A hatókör-ítéletet hozó futás szereplője más, mint a commitot előállítóé.
- **I-0005-3** A hatókör-ítéletet hozó futás előbb *használta* az AC-ket és a diffet, és csak utána
  a Builder beszámolóját (az időbélyegek sorrendje).
- **I-0005-4** Ha egy munkadarab egy másik munkadarabból *származik* (a review közben jött létre),
  akkor a Ready állapothoz emberi K1 jóváhagyás kell rá.

**Ítéletek:** hatókör-ítélet (ágens), az, hogy a talált kéretlen változás kikerül vagy új munkadarab lesz
(ágens), refaktor-kör indítása (ember).

**Ami nem fér bele:**
- 💭 „Ready állapot”: a gráfban nincs állapot. A Ready **levezetett nézet**: a munkadarabhoz
  érvényes jóváhagyások tartoznak, és a függőségei készen vannak.
- 💭 Az erózió mérése (a refaktor-munkadarabok száma és kora) megint lekérdezés.

## Amit a próba kimutatott

1. **Két forma kevés, három kell.** Megkötés, ítélet és **mérőszám** (lekérdezés a gráfon). A
   küszöbök konfigurációként, emberi ítélettel változnak.
2. **Ítéletet nem csak ember hoz.** Ágens (hatókör, kockázat, visszavonhatóság) és szabály (merge
   policy) is. A megkötések azt mondják meg, *melyik* ítéletet ki hozhatja.
3. **A gráf időbeli, és csak bővülhet.** Verziók, SHA-kötés, olvasási sorrend, „csak felfelé”:
   ezek mind az időre vonatkoznak. Ezért semmi nem íródik felül, minden új csomópont vagy él lesz.
4. **Az állapot nézet, nem tárolt adat.** Backlog, Ready, Done: a gráfból levezethető.
5. **Két gráf van:** a munka gráfja és a kód függőségi gráfja. A 0004 hatókör-feltétele a kettőt
   köti össze.
6. **Gyenge pont: az ágens saját állítása.** A preview környezet és a visszavonhatóság csak annyira
   megbízható, amennyire a szereplő, aki állítja. A megkötés csak azt garantálja, hogy *ki*
   állította.
