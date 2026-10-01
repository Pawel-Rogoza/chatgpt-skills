# B2: wynik pilota 0.6.0

Dodano szósty skill: zwykły pobyt czasowy i praca. [Specyfikacja](../../../docs/b2-specification.md), [rubryka rozwojowa](../../residence-rubric.md), [manifest przebiegu](run-manifest.json).

## Niezależna próba zamrożonej instrukcji
Niezależny autor przygotował dwa syntetyczne przypadki i klucze przed instrukcją. Implementator nie czytał ich do zamrożenia i wykonania. Dwa nowe konteksty agentów wykonały wariant ze skillem i baseline; każdy rozwiązał obydwa przypadki w swoim kontekście. Dostęp do internetu był wyłączony w obu wariantach. Model i ustawienia były dziedziczone tak samo, ale identyfikator snapshotu i temperatura nie są udostępnione.

Oceniający znał wyłącznie anonimowe odpowiedzi A/B i własny klucz, nie mapowanie. **A = skill, B = baseline: oba warianty 32/32**, bez błędów krytycznych. Nie zaobserwowano materialnej przewagi skilla. To wynik dwóch zamkniętych ćwiczeń, nie dowód wyższości lub równoważności modeli ani prawidłowości aktualnego prawa. [Ocena z cytatami](assessment-B2.md) i [dane](assessment-B2.json) używają ośmiu kryteriów 0-2, niezależnych od rubryki rozwojowej.

| Przypadek | Skill | Baseline | Materiał i klucz |
|---|---|---|---|
| B2_01 | [surowa odpowiedź](variant-A-B2_01.md) | [surowa odpowiedź](variant-B-B2_01.md) | [polecenie](inputs/B2_01/user.md), [materiał](inputs/B2_01/materials.md), [klucz](inputs/B2_01/rubric.md) |
| B2_02 | [surowa odpowiedź](variant-A-B2_02.md) | [surowa odpowiedź](variant-B-B2_02.md) | [polecenie](inputs/B2_02/user.md), [materiał](inputs/B2_02/materials.md), [klucz](inputs/B2_02/rubric.md) |

Po publikacji te przypadki stają się rozwojowe i nie wolno przedstawiać ich jako przyszłego holdoutu. Ślady odczytów: [baseline](trace-baseline-B2.json), [skill](trace-skill-B2.json); usunięto lokalne ścieżki wykonania.

## Kontrola techniczna i regresja
Kontrola obejmuje 45 plików, samodzielność referencji, wersje oraz build ZIP; quick_validate skilla przeszedł. Lokalnie 12 testów przeszło, trzy wymagające symlinków pominięto w osobnym tymczasowym harnessie z powodu WinError1314. Pierwotny pełny przebieg miał cztery błędy w tych trzech metodach. Testy repo i CI nie zostały osłabione: Linux powinien wykonać wszystkie 15, wynik trzeba sprawdzić w PR.
Dotychczasowe pięć instrukcji zmieniono wyłącznie w metadanych wersji; wspólne referencje i kod pakowania pozostały bez zmian. Siedem jawnych scenariuszy powstało przed instrukcją. Dodatkowe odpowiedzi rozwojowe oraz próby istniejącej apelacji i recenzji zapisano oddzielnie; nie są holdoutem ani oceną adwokata.

## Granice odbioru
Status techniczny: pakiet zbudowany lokalnie; pełny Linux CI do sprawdzenia. Status zachowania: niezależne porównanie dwóch przypadków bez wykazanej przewagi. Status zawodowy: niedopuszczony przez adwokata w tej sesji. Routing hosta i rzeczywisty research online pozostają otwarte. Odczyt źródeł projektowych odnotowano w [rejestrze](../../../source-policy/source-register.json), bez zapewnienia kompletności prawa na datę sprawy. Nie wykonano instalacji nowego pluginu w ChatGPT lub workspace.
