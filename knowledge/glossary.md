# Fogalomtár

Közös szókincs. Ábécérendben. Ha egy fogalom jelentése vitatott, a hozzá tartozó topic jegyzetre
mutatunk.

| Fogalom | Jelentés | Bővebben |
|---|---|---|
| AC (acceptance criteria) | elfogadási feltételek; gép által ellenőrizhető állítások arról, mikor kész egy kártya | |
| AI-natív szoftvergyár | olyan gyár, amelynek a folyamatát az ágensekre tervezték; az ember a hurok fölött áll | `topics/ai-nativ-vs-ai-tamogatott.md` |
| AI-támogatott szoftvergyár | meglévő, emberközpontú folyamat, amelyben az AI eszköz; az ember a hurokban áll | `topics/ai-nativ-vs-ai-tamogatott.md` |
| ágens (agent) | önállóan több lépést végrehajtó modell, eszközökkel és célokkal | |
| állomás | egy lépés a soron (spec, terv, build, QA, review, landing); a sorrendet a folyamat adja | `topics/fogalmi-modell.md` |
| bizonyíték (evidence) | a PR-hoz csatolt, emberi szemmel gyorsan ellenőrizhető igazolás: képernyőkép a futásról, e2e eredmény, AC-nként | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| dark factory | „sötét gyár”: autonóm termelés, amelyben ember nem ír és nem néz át kódot; a gyárvilág lights-out manufacturing fogalmából | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| e2e (end-to-end) teszt | a futó rendszer tesztje a felhasználó oldaláról, böngészőn vagy API-n át, az összes rétegen keresztül | `positions/0003-a-veg-a-pr-bizonyitekkal.md` |
| elfogadás | döntés az eredményről (K3); vö. jóváhagyás | `topics/fogalmi-modell.md` |
| human in the loop | az ember minden lépésnél jóváhagy | |
| human on the loop | az ember felügyel, és csak kivételnél vagy kapunál lép be | |
| escape rate | a kapun átjutott, később megtalált hibák aránya; a kapu és a bizalom mérőszáma | `topics/alacsony-kockazat.md` |
| flaky teszt | ugyanazon a kódon néha átmegy, néha elbukik | |
| intent | lásd: szándék | |
| invariáns | a gyár gráfján gépi úton ellenőrizhető szabály; a döntéseink egyik célformája | `positions/0006-grafmodell.md` |
| ítélet | a gyár gráfjának csomópontja: egy szereplő (ember, ágens vagy szabály) döntése egy munkatermék adott verziójáról; az invariánsok mondják meg, melyiket ki hozhatja | `positions/0006-grafmodell.md` |
| jóváhagyás | döntés, mielőtt a munka elindul (K1 spec, K2 terv); vö. elfogadás | `topics/fogalmi-modell.md` |
| kapu | döntési pont, ahol a munka megáll; dönthet ember vagy szabály | `topics/fogalmi-modell.md` |
| lane | lásd: sáv | |
| munkatermék (work product, artifact) | a gyár gráfjának csomópont-típusa: szándék, spec, AC, terv, munkadarab, commit, bizonyíték, döntés | `positions/0006-grafmodell.md` |
| merge kapu (merge gate) | szabályalapú döntési pont: automatikus merge, vagy emberi jóváhagyás kockázat szerint | `experiments.md` |
| sáv (lane) | szerepkör: ki végzi az állomást (Build, QA, Review, ember); egy sávban több állomás lehet; a függetlenségi szabályok sávok között élnek | `topics/fogalmi-modell.md` |
| scope conformance | annak ellenőrzése, hogy a diff minden része visszavezethető egy AC-re | `positions/0005-scope-conformance.md` |
| scope drift | a diff olyat változtat, amit a kártya AC-i nem kértek | `positions/0005-scope-conformance.md` |
| szándék (intent) | az ember által megfogalmazott cél egy változtatásra; a gyár bemenete. Egy szándékból több kártya és több PR lehet (1:N). Nem „igény”, mert az igényfelmérés a spec felé húz | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| szoftvergyár (software factory) | rendszer, amely emberi szándékból (intent) ágensekkel, skillekkel és workflow-kkal PR-t állít elő; az ember dönt és validál, a gyár javasol, végrehajt és tanul | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| tanuló hurok (learning loop) | a gyár elemzi az eredményeit és a hatékonyságát, és változtatást javasol a saját működésére; az ember dönt róla | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` |
| worktree izoláció | minden munkaegység saját git worktree-ben és branchen fut, hogy a párhuzamos munka ne ütközzön | `experiments.md` |
