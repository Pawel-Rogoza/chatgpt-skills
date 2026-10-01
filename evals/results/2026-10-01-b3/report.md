# B3: wynik pilota 0.7.0

Siódmy skill obejmuje zwykłą decyzję powrotową SG pierwszej instancji, administracyjne odwołanie i osobną ocenę wykonania. [Specyfikacja](../../../docs/b3-specification.md), [rubryka rozwojowa](../../return-rubric.md), [manifest przebiegu](run-manifest.json).

## Niezależne porównanie przed poprawką
Dwa syntetyczne przypadki z kluczami przygotowano bez dostępu do implementacji; implementator nie widział ich przed zamrożeniem i wykonaniem. Nowy kontekst uruchomiono osobno dla każdego wariantu, oba przypadki w tym samym kontekście wariantu. Dostęp online był zerowy. Model i ustawienia były dziedziczone jednakowo, ale dokładny snapshot i temperatura nie są udostępnione.
Oceniający znał anonimowe odpowiedzi i własny klucz, bez mapowania. **A = baseline 32/32, B = skill 31/32; bez błędów krytycznych.** Różnica jednego punktu dotyczy braku jawnego warunkowego rachunku daty 26.06 w B3_01. Skill podał poprawną formułę, problem doręczenia pełnomocnikowi i pilną reakcję. Nie stwierdzono materialnej przewagi bezpieczeństwa ani ogólnej wyższości któregokolwiek wariantu. [Ocena z cytatami](assessment-B3.md), [dane](assessment-B3.json).

| Przypadek | Skill, pierwsza wersja | Baseline | Materiał i klucz |
|---|---|---|---|
| B3_01 | [odpowiedź](variant-B-B3_01.md) | [odpowiedź](variant-A-B3_01.md) | [polecenie](inputs/B3_01/user.md), [materiał](inputs/B3_01/materials.md), [klucz](inputs/B3_01/rubric.md) |
| B3_02 | [odpowiedź](variant-B-B3_02.md) | [odpowiedź](variant-A-B3_02.md) | [polecenie](inputs/B3_02/user.md), [materiał](inputs/B3_02/materials.md), [klucz](inputs/B3_02/rubric.md) |

Ślady: [baseline](trace-baseline-B3.json), [skill](trace-skill-B3.json). Po publikacji przypadki są rozwojowe, nie przyszłym holdoutem.

## Wąska poprawka i próby rozwojowe
Dodano jedno zdanie w return-method: przy spornym początku pokazać przydatny warunkowy rachunek niekorzystnego wariantu, wyraźnie odróżniając ochronne założenie od ustalonego terminu. Wynik pierwszej próby pozostaje zachowany; nie przepisano go na ocenę poprawionej instrukcji. Osiem dodatkowych odpowiedzi rozwojowych wykonano z pierwszą zamrożoną instrukcją. Odrębny świeży retest B3_01 dotyczy instrukcji po poprawce i jest próbą rozwojową, nie nowym ukrytym testem.

## Kontrola techniczna i granice odbioru
Check: 53 pliki; build ZIP i quick_validate przeszły. Lokalnie 12 testów przeszło, trzy testy symlinków pominięto w tymczasowym harnessie z powodu uprawnień Windows. Testy repo i CI nie zostały zmienione; pełny Linux CI trzeba zweryfikować w PR. Poprzednie sześć instrukcji zmieniono tylko w wersji metadanych, wspólne polityki i walidator są identyczne. W poprzednim etapie sprawdzono istniejącą apelację i recenzję: [B2](../2026-10-01-b2/report.md).

Status zachowania: porównanie modelowe dwóch przypadków, brak dowodu przewagi, odrębna poprawka i retest. Status zawodowy: bez odbioru adwokata w tej sesji. Routing w hoście, realny research online i nowa instalacja pluginu pozostają otwarte. [Rejestr źródeł](../../../source-policy/source-register.json) odróżnia odczyt fragmentów od kompletnej aktualności prawa. WSA, detencja i sprawa ochronna od początku są poza pilotem.
