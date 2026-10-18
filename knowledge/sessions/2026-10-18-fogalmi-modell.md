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
- 🔍 [`topics/invariansok.md`](../topics/invariansok.md): a típusok első változata és a 0002–0005
  invariánsai.
- Fogalomtár: szándék, állomás, sáv, kapu, jóváhagyás, elfogadás, munkatermék, invariáns, ítélet.
  Forrás: W3C PROV-DM.

## Nyitva maradt

- A „kártya” magyar neve.
- Nagy szándéknál a szándék : spec arány 1:N legyen?
- Mitől lesz egy ágens saját állítása ellenőrizhető?
- A folyamat kibontása: kivételkezelés (andon), a K1 kettéválása, utókövetés.
