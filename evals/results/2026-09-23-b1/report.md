# B1 — raport z wdrożenia, 23.09.2026

**Implementacja i instalacja lokalna ukończone:** `pl-criminal-detention`, piąty skill pakietu 0.4.0. Zakres: kontrola pierwszego postanowienia o zastosowaniu tymczasowego aresztowania w zwykłej sprawie karnej, argumenty i projekt zażalenia obrony. Przedłużenie, zatrzymanie, detencja administracyjna, wykonanie kary, ENA i ekstradycja pozostają poza pełnym zakresem pilota.

Baza: `2321f147ef5af55a521443ae7a91f498b0c33d27`, otwarty niescalony PR #4, sprawdzony przez GitHub na początku pracy. Zmiany powstały na `codex/legal-ai-b1-detention`. Nie scalano wcześniejszych PR-ów. Zastaną lokalną edycję historycznego raportu A pozostawiono poza zmianami B1.

## Co dodano

- Minimalny skill, referencję metody i warunkową mapę źródeł, metadane UI oraz jawną deklarację ośmiu nowych plików pakietu.
- Osiem fikcyjnych przypadków i osobną [rubrykę](../../detention-rubric.md), przygotowane przed instrukcją B1.
- Siedem nowych pozycji routingu: razem 22. Obejmują odróżnienie kontroli zasadności, recenzji pisma, objaśnienia klientowi i innych rodzajów izolacji.
- [Rejestr źródeł](../../../source-policy/source-register.json) odróżniający dostępność, zakres odczytu, aktualność i warunki użycia.
- [Specyfikację](../../../docs/b1-specification.md), [wydanie i wycofanie](../../../docs/release-0.4.0.md), aktualizację roadmapy i polecenia kontynuacji.

Metoda rozdziela prawdopodobieństwo popełnienia czynu, konkretne ryzyka, potrzebę izolacji, alternatywy i gwarancje procesowe. Późniejsze zdarzenia nie są automatycznie wadą decyzji w chwili wydania. Zażalenie nie staje się wnioskiem o zmianę środka przez samą zmianę nagłówka. Nie wpisano stałych terminów, maksymalnych okresów ani gotowej kwoty poręczenia.

## Sprawdzenia techniczne

15 istniejących testów pakowania przeszło; pięć skilli przeszło `quick_validate.py`, a plugin `validate_plugin.py`. `check` potwierdził 36 plików. Dwukrotny build dał identyczne bajty; hash archiwum i wejść znajduje się w [run-manifest.json](run-manifest.json).

Kod pakowania nie zmienił się. Porównanie czterech wcześniejszych folderów z bazowym commitem wykazało zgodność ich treści poza `metadata.version`, podniesionym do 0.4.0. Wspólna polityka pozostała niezmieniona. To kontrola braku zmiany metody, nie pełny test regresji zachowania.

Sprawdzono lokalny katalog `personal` i jego źródło, zaktualizowano plugin przez CLI do `0.4.0+codex.20260923185426`. Wszystkie 36 plików cache zgadza się ze źródłem; brak dodatkowych plików. Nie wykonano publikacji publicznego pluginu ani wdrożenia Business/Enterprise.

## Źródła — co naprawdę odczytano

23.09.2026 odczytano [metadane ELI](https://api.sejm.gov.pl/eli/acts/DU/2026/490) i wybrane fragmenty [ujednoliconego KPK](https://eli.gov.pl/api/acts/DU/2026/490/text/U/D20260490Lj.pdf): PDF s. 105–114 i 199–200. Data redakcyjna kopii to 17.07.2026. Metadane wykazują późniejsze nowelizacje względem tekstu jednolitego; sam status obwieszczenia nie dowodzi kompletności norm dla daty sprawy. Nie przeprowadzono pełnej rekonstrukcji prawa i przepisów przejściowych ani nie przeczytano całych 357 stron. Hash pobranej kopii zapisano; PDF nie trafił do repozytorium.

Odczytano status i wybrane fragmenty [przewodnika Kancelarii ETPC o art. 5](https://ks.echr.coe.int/documents/d/echr-ks/guide_art_5_eng), oznaczonego 28.02.2026. Jest to niewiążące opracowanie, użyte do mapy zagadnień i źródeł. Nie odczytano orzeczeń przywołanych w przewodniku; nie oznaczamy ich jako zweryfikowanych wyroków i nie kopiujemy ich tez jako samodzielnie sprawdzonych cytatów.

## Próby własne i obserwacje

[Zachowane odpowiedzi](self-check.md) obejmują osiem rzeczywiście wykonanych zadań przez autora w bieżącym kontekście. Autor znał materiały i rubrykę. Nie uruchamiano niezależnych agentów ani innych zadań modelowych; nie były to baseline, holdout ani zaślepione pomiary.

| Przypadek | Obserwacja własna |
|---|---|
| initial | Dwa akapity argumentacji; najem i rodzina nie stały się wykazanym zamieszkaniem; udział tłumacza zachowany |
| specific | Odrzucono fałszywy argument o braku konkretów; sporność autorstwa odróżniono od istnienia zrzutu |
| changed | Późniejsze dokumenty i planowana konfrontacja zachowane; zdrowie rozpoznano jako pilną niewyjaśnioną kwestię |
| extension | Rozpoznano granicę pilota; wskazano historię środka i możliwą kontrolę fragmentu |
| wrong | Rozpoznano detencję administracyjną bez mechanicznego karnego pisma |
| urgent | Nie potwierdzono „do jutra”; podano potrzebne zdarzenia i materiały, bez wysyłki z P3 |
| alternative | Wykryto problem mieszkania u świadka i niepewnego finansowania, bez wymyślonej kwoty |
| clean | Nie wymyślono braku uzasadnienia; kontakt odróżniono od wpływania na treść zeznań |

Nie zaobserwowano we własnej ocenie błędu krytycznego ani istotnego pominięcia wobec jawnej rubryki. Nie przedstawiamy tego jako niezależnego dowodu skuteczności. Przy przeglądzie opis doprecyzowano, aby główne zadanie recenzji gotowego pisma wskazywało skill recenzji; to korekta specyfikacji doboru, nie poprawka potwierdzona pomiarem hosta.

Nie testowano kompletnego projektu z właściwością sądu, finalnym żądaniem i wyliczonym terminem. Próby dotyczyły argumentacji, materiału i granic. Nie oceniano szybkości kontroli adwokata lub kosztu; nie wykazano przewagi względem modelu bez skilla.

## Otwarte kryteria i następny etap

**Routing hosta: niesprawdzony.** Nowy opis może wpływać na wybór pozostałych skilli mimo niezmienionej treści ich instrukcji. Potrzebne są testy jawnego i automatycznego uruchamiania w nowym zadaniu.

Brak dwóch niewidzianych przypadków odbiorczych, porównywalnego baseline/skill, niezależnej recenzji merytorycznej i odbioru adwokata. Nie badano izolacji backendu, obliczania terminów procesowych, reprezentatywnych akt ani firmowego środowiska danych. Własne odpowiedzi nie znoszą tych braków.

| Status | Wynik |
|---|---|
| Technicznie gotowy lokalnie | Tak: walidacja, ZIP, zgodność cache |
| Pilot zachowania | Osiem własnych prób; niezależny odbiór otwarty |
| Dopuszczony do określonego użycia kancelaryjnego | Nie oceniano |

Kolejny etap domenowy: B2 `pl-residence-strategy`, po wybraniu pierwszego rodzaju sprawy pobytowej, następnie B3. Nie rozszerzono tego zlecenia automatycznie na pełne prawo migracyjne lub przedłużenie aresztowania. Przed realnym użyciem B1 potrzebna jest ocena adwokata i weryfikacja źródeł dla konkretnej sprawy.
