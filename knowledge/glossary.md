# Fogalomtár

Közös szókincs. Ábécérendben. Ha egy fogalom jelentése vitatott, a hozzá tartozó topic jegyzetre
mutatunk.

| Fogalom | Jelentés | Bővebben |
|---|---|---|
| AC (acceptance criteria) | elfogadási feltételek; gép által ellenőrizhető állítások arról, mikor kész egy kártya | |
| AI-natív szoftvergyár | olyan gyár, amelynek a folyamatát az ágensekre tervezték; az ember a hurok fölött áll | `topics/ai-nativ-vs-ai-tamogatott.md` |
| AI-támogatott szoftvergyár | meglévő, emberközpontú folyamat, amelyben az AI eszköz; az ember a hurokban áll | `topics/ai-nativ-vs-ai-tamogatott.md` |
| ágens (agent) | önállóan több lépést végrehajtó modell, eszközökkel és célokkal | |
| bizonyíték (evidence) | a PR-hoz csatolt, emberi szemmel gyorsan ellenőrizhető igazolás: képernyőkép a futásról, e2e eredmény, AC-nként | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| dark factory | „sötét gyár”: autonóm termelés, amelyben ember nem ír és nem néz át kódot; a gyárvilág lights-out manufacturing fogalmából | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| e2e (end-to-end) teszt | a futó rendszer tesztje a felhasználó oldaláról, böngészőn vagy API-n át, az összes rétegen keresztül | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| human in the loop | az ember minden lépésnél jóváhagy | |
| human on the loop | az ember felügyel, és csak kivételnél vagy kapunál lép be | |
| escape rate | a kapun átjutott, később megtalált hibák aránya; a kapu és a bizalom mérőszáma | `topics/alacsony-kockazat.md` |
| flaky teszt | ugyanazon a kódon néha átmegy, néha elbukik | |
| intent (szándék) | az ember által megfogalmazott cél egy változtatásra; a gyár bemenete | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| lane | egy szerepkör sávja a folyamatban (Build, QA, Review); saját ágens, saját szabályok | `experiments.md` |
| merge kapu (merge gate) | szabályalapú döntési pont: automatikus merge, vagy emberi jóváhagyás kockázat szerint | `experiments.md` |
| szoftvergyár (software factory) | rendszer, amely emberi szándékból (intent) ágensekkel, skillekkel és workflow-kkal PR-t állít elő; az ember dönt és validál, a gyár javasol, végrehajt és tanul | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| tanuló hurok (learning loop) | a gyár elemzi az eredményeit és a hatékonyságát, és változtatást javasol a saját működésére; az ember dönt róla | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| worktree izoláció | minden munkaegység saját git worktree-ben és branchen fut, hogy a párhuzamos munka ne ütközzön | `experiments.md` |
