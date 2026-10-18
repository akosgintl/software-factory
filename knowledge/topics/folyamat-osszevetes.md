# A folyamat összevetése: hány lépés, kinél

🔍 2026-10-18. A négy saját kísérlet kódja és 11 publikus rendszer dokumentációja alapján. A
források a `sources.md` fájlban vannak; ahol a kutatás csak másodlagos forrást talált, ott
`[ellenőrizendő]` jelölés áll. Ebből lett a négy állomás: `positions/0008-negy-allomas.md`.

## Saját kísérletek

| Gyár | Állomások (fő út) | Mellékállapot | Emberi kapu | Újramunka-korlát | Merge |
|---|---|---|---|---|---|
| super-board (`origin/super-board`) | Backlog → Ready → Building → QA → Review → Done (6) | Blocked | ember teszi Backlogból Ready-be; merge policy (pénz, auth, séma, 400 sor felett) | 2, azonos root-cause hash esetén | merge gate: zár, a reviewed SHA-hoz kötve, CI az aktuális bázison |
| fable-factory | spec → build → review → sync → approve → merged (6) | needs-human | approver ESCALATE esetén | 2 review-kör | helyi `merge --no-ff`, egyesével, sync előtte |
| opus-factory | spec → build → review → approve (landing slot) → merged (5) | needs-human | approver ESCALATE esetén, kockázatos kategóriánál akkor is, ha a review zöld | 1 javítás | landing slot: egyszerre egy job szinkronizál és merge-öl |
| warpdotdev-factory | triage → spec (csak kétértelmű vagy nagy munkánál) → implement → review → draft PR (4 + emberi merge) | nincs rögzítve | spec jóváhagyás; a merge mindig ember | nincs rögzítve: a foreman addig küldi vissza a review egyértelmű leleteit, amíg tiszta | mindig ember, a gyár soha nem merge-öl |

## Publikus rendszerek

| Rendszer | Lépések | Spec / terv kapu |
|---|---|---|
| Warp Factories (korábban Oz) | Triage → Planning → Building → Reviewing (4) + átadás embernek | spec jóváhagyás alapból; a merge-et soha nem végzi |
| Factory Missions | Requirements → Validation contract → Decomposition → Shared state → Execution → Milestone validation → Rework (7) | terv jóváhagyás |
| Factory Spec Mode | leírás → kutatás és terv → jóváhagyás → implementálás (4) | spec jóváhagyás, autonómia-szint választással |
| GitHub Spec Kit | specify → plan → tasks → implement (4 mag, opcionálisakkal 9) | review minden lépés után |
| Kiro | Requirements → Design → Tasks → implement (4) | jóváhagyás fázisok között |
| BMAD | Clarify → Plan → Build and verify → Learn and adjust (4) | terv jóváhagyás csak jelzett kockázatnál |
| Jules | terv → jóváhagyás → végrehajtás → publikálás (4) | terv jóváhagyás, időzítővel automatikus |
| Copilot, Codex, Devin | feladat → implementálás → önellenőrzés → PR → emberi review (kb. 5) | nincs dokumentált terv-kapu (Devin: csak bizonytalanságnál) |
| StrongDM | nincs rögzített sor; gráf-pipeline (Attractor), amely konvergenciáig hurkol | nincs emberi kód-review, szabály szerint |

## Ami szinte mindenkinél közös

- A váz négy lépés: **terv → build → ellenőrzés → merge**, plusz egy „embert kér” mellékállapot,
  és egy újramunka-hurok az ellenőrzésből a buildbe.
- Izolált környezet vagy branch munkadarabonként, a kimenet PR.
- Az ellenőrzést egy másik ágens végzi (reviewer, kritikus).
- A merge sorosítása (landing slot, merge gate, sync) a három automatikusan merge-ölő saját
  kísérletben megvan. A warp-kísérletben az ember merge-öl.

## Ami eltér, és mit tanulunk belőle

- 🔍 **A bizonyíték előre rögzítve.** A Factory Missions „validation contract”-ja a feature-ök előtt
  rögzíti, milyen bizonyíték kell (például képernyőkép és HTTP 200), hogy a terv utólag ne írhassa
  át, mi a „helyes”. Ez a 0003 közeli rokona (`questions.md`).
- 💭 **Rejtett forgatókönyvek.** A StrongDM a teszt-forgatókönyveket a kódon kívül tartja, a
  builder nem látja őket. Ez erősítené a bizonyíték függetlenségét (0003, `questions.md`).
- 💭 **Azonos hiba számlálása.** A super-board nem a köröket számolja, hanem az azonos okú hibát
  (root-cause hash). Ha más a hiba, a számláló újraindul. Jobb mérce lehet, mint a 0007 sima
  újramunka-korlátja (`questions.md`).
- 🔍 **Utólagos, mintavételes eval.** A warp-kísérlet két scorere (task-compliance, review-quality)
  LLM bírálóval, a futások 25%-án pontozza az implementert és a reviewert. A task-compliance azt
  kérdezi, amit a 0005: megcsinálta-e, amit kértek, és csak azt. Nálunk ez a kapu előtt, minden
  PR-on fut (I-0008-4), nem utólag. A `selfImprovement: true` jelentése `[ellenőrizendő]`
  (`questions.md`).
- 🔍 **A merge.** A publikus rendszerek többsége és a warp-kísérlet a merge-et embernél hagyja. A
  másik három saját kísérlet és a 0004 alacsony kockázatnál automatikusan merge-öl. Ebben
  agresszívebbek vagyunk.
- 🔍 **A K0.** A super-board-ban megvan (az ember teszi Ready-be, ez egyben a K1). A többinél
  rejtett: az ember adja a feladatot.
