# Dalsze prace po wdrożeniu 0.8.0

Data planu: 01.10.2026. Wdrożenie oznacza scalenie kodu pilota do `main` i lokalną instalację; nie jest zawodowym odbiorem odpowiedzi. Pakiet zawiera dziewięć skilli, w tym UKR/CUKR i SIS. Wyniki: [raport 0.8.0](../evals/results/2026-10-01-ua-sis/report.md). Dwie niezależne próby wykonano; pełne testy pozostają otwarte.

## Kolejność i kryteria ukończenia

| Priorytet | Zadanie | Konkretny wynik | Kryterium ukończenia |
|---|---|---|---|
| 1 | Domknąć research UKR/CUKR i SIS | Uzupełniony rejestr z datą, zakresem odczytu i lukami | Odczyt komunikatu startowego CUKR; właściwe wersje rozporządzeń SIS i polskiej ustawy SIS/VIS; aktualna instrukcja wojskowego warunku UE lub wyraźnie udokumentowany brak; rozpoznany tryb naprawy wpisu UKR/NUE. Bez pozornych potwierdzeń aktualności |
| 2 | Pełne próby nowych pilotów | Surowe odpowiedzi dla sześciu `ua-*` i czterech `sis-*`, oceny, poprawki i regresja | Każdy przypadek w osobnym kontekście; wąskie poprawki po wykazanych błędach. Dotychczasowe dwie próby zachować jako wynik rozwojowy, nie holdout |
| 3 | Baseline i nowe przypadki | Porównanie ze skillem i bez niego, na nowych materiałach | Ten sam model, narzędzia i dane obu wariantów; przygotowanie holdoutu poza widokiem autora; brak błędów krytycznych, jawna ocena przydatności i czasu poprawek |
| 4 | Routing i regresja dziewięciu skilli | Wyniki `evals/routing.json` oraz przypadków na styku analizy, pobytu, powrotu, UKR/CUKR i SIS | Sprawdzić automatyczny wybór bez jawnego wywołania, brak przejmowania tłumaczenia/niepowiązanych zadań, poprawny zakres przy wielu wątkach. Discovery jest osobnym sprawdzeniem |
| 5 | Odbiór adwokata i języka | Lista uwag, decyzja o zakresie użycia i potrzebnych poprawkach | Przegląd prawny odpowiedzi i projektów, terminów, środków i wykonania; kontrola PL/UA/RU przy objaśnieniach. Modelowa samoocena nie zamyka tego etapu |
| 6 | C1: WSA w sprawie powrotowej | Dziesiąty, wąski skill według [specyfikacji](c1-specification.md) | Najpierw research p.p.s.a., przepisów szczególnych i właściwego orzecznictwa, potem przypadki/rubryka, metoda i instrukcja; osobna ocena skargi i ochrony przed wykonaniem; regresja B3/SIS/UKR |
| 7 | Wydanie kolejnej wersji | Archiwum, suma kontrolna, raport i instalacja zweryfikowanej wersji | Check, 15 testów pakowania, build, zgodność cache, discovery bez błędów oraz raport prób. Wersja 0.8.1 dla poprawek albo 0.9.0 przy dodaniu C1 |

## Po C1

Kolejne kandydatury do osobnego researchu i zawężenia: detencja administracyjna cudzoziemców, kontrola odmowy/cofnięcia pobytu, kompleksowa ochrona międzynarodowa. Każdy zakres ma własne środki i testy; nie rozszerzać go przez pojedynczy akapit w skillu powrotowym. Najpierw ocenić częstotliwość zleceń i luki istniejących skilli, następnie wybrać jeden pilot.

## Zasady wykonania

Pracować na gałęziach `codex/`, publikować konkretną zmianę w PR i zachowywać surowe wyniki na materiałach fikcyjnych. Nie dodawać akt klientów. Stan prawny weryfikować na datę sprawy, a datowany research zachować jako punkt wyjścia. Luki źródłowe nie blokują niezależnej analizy materiałów, ale ograniczają zależny wniosek prawny. Potwierdzenie danych SIS nie zastępuje kontroli decyzji lub pilnego środka.

Plan ustala zależności i kolejność, bez obietnicy terminu odbioru adwokata lub dostępu do zewnętrznych źródeł. Nie tworzy automatycznych zadań ani harmonogramu powiadomień.
