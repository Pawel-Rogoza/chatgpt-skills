# Ocena rozwoju B2 i dwóch regresji

**Siedem zadań rozwojowych: 140/140 pkt, bez błędów krytycznych. Dwie regresje: po 16/16 pkt**, bez materialnego naruszenia kryteriów istniejących fixture. Zachowano dodatkową kontrolę: informacja o technicznie brakującej stronie 5 pozostaje poza proponowanym uzasadnieniem dla sądu.

To ocena modelowa, nie opinia adwokata. Zadania są znane implementatorowi i nie stanowią holdoutu. Nie czytano skilli ani innych odpowiedzi. Brak udostępnionych wcześniejszych przebiegów regresji: wniosek dotyczy zgodności z kryteriami, a nie udowodnionego braku zmiany historycznej.

## Punktacja rozwojowa

Pięć wymiarów z `evals/residence-rubric.md`, każdy 0–4. Pełne 4 oznacza proporcjonalne wykonanie na dostępnym materiale: jawny brak źródła prawa nie jest karany za brak pamięciowej odpowiedzi. W wąskich zleceniach nie wymagano zbędnego wywiadu ani rozbudowanej strategii.

| Przypadek | Zakres/status | Fakty/źródła | Prawo w czasie | Warianty | Działanie | Razem | Krytyczne |
|---|---:|---:|---:|---:|---:|---:|---|
| residence-clean | 4 | 4 | 4 | 4 | 4 | 20/20 | Brak |
| residence-criminal | 4 | 4 | 4 | 4 | 4 | 20/20 | Brak |
| residence-employer | 4 | 4 | 4 | 4 | 4 | 20/20 | Brak |
| residence-pending | 4 | 4 | 4 | 4 | 4 | 20/20 | Brak |
| residence-practice | 4 | 4 | 4 | 4 | 4 | 20/20 | Brak |
| residence-ru-status | 4 | 4 | 4 | 4 | 4 | 20/20 | Brak |
| residence-temporal | 4 | 4 | 4 | 4 | 4 | 20/20 | Brak |

Lokalizatory poniżej oznaczają wiersze wskazanego surowego pliku odpowiedzi, liczone od 1 z pustymi wierszami.

### residence-clean

Plik: `development-residence-clean.md`.

| Wymiar | Punkty | Wiersze | Uzasadnienie |
|---|---:|---|---|
| Rozpoznanie zakresu/statusu | 4 | 1–8 | Odpowiedź wykonuje tylko porównanie stanowiska i wymiaru, bez rozszerzenia na strategię pobytową. |
| Pochodzenie i lokalizatory faktów | 4 | 3–8 | C1/C2 mają strony i karty, C3 akapit; relacja klienta nie staje się niezależnym potwierdzeniem. |
| Dobór prawa w czasie | 4 | 1–8 | Do zleconego porównania dokumentowego prawo nie jest potrzebne; nie dodano norm ani terminu. |
| Warianty i kontrargumenty | 4 | 5–8 | Zgodność obu przekazanych warunków, brak wymyślonych wad; pozostałych warunków nie oceniano. |
| Użyteczność następnego działania | 4 | 1–8 | Dostarczono wynik wąskiego pytania. Dodatkowy wywiad i plan nie były potrzebne. |

Potwierdzenie, w. 8: „Pozostałych warunków nie oceniano.”. Brak błędów krytycznych.

### residence-criminal

Plik: `development-residence-criminal.md`.

| Wymiar | Punkty | Wiersze | Uzasadnienie |
|---|---:|---|---|
| Rozpoznanie zakresu/statusu | 4 | 1–3, 9–15 | Zarzut, niepotwierdzone skazanie, pobyt, praca i powrót są rozdzielone. |
| Pochodzenie i lokalizatory faktów | 4 | 1–3, 9–13 | Lokalizatory K1–K4; robocze tłumaczenie, cudza opinia nie staje się faktem. |
| Dobór prawa w czasie | 4 | 10, 13, 15 | Brak norm ujawniony; potrzebna właściwa przesłanka i daty, bez pamięciowego automatu. |
| Warianty i kontrargumenty | 4 | 9–15 | Etapy i skutki warunkowe, bez gwarancji bezpieczeństwa lub deportacji. |
| Użyteczność następnego działania | 4 | 9–15 | Mapa dokumentów: wyrok i prawomocność, pełna decyzja, korespondencja, podstawa pracy, powrót. |

Potwierdzenie, w. 1: „brak wyroku w przekazanym pakiecie nie dowodzi, że wyrok nigdy nie zapadł.”. Brak błędów krytycznych.

### residence-employer

Plik: `development-residence-employer.md`.

| Wymiar | Punkty | Wiersze | Uzasadnienie |
|---|---:|---|---|
| Rozpoznanie zakresu/statusu | 4 | 1, 3–11 | Ważność pobytowa, zakres decyzji i odrębne uprawnienie na Betę rozdzielono. |
| Pochodzenie i lokalizatory faktów | 4 | 3–9, 15–17 | E1 strony i karty, E2 karta, E3/E4; niewiedza klienta nie staje się pewnym brakiem dokumentu. |
| Dobór prawa w czasie | 4 | 17, 19 | Nie wymyślono terminu zawiadomienia ani skutków zmiany; brak norm ujawniony. |
| Warianty i kontrargumenty | 4 | 11, 19 | Warunkowa zmiana, odrębna podstawa, ewentualnie nowy wniosek; brak automatycznego obowiązku nowego wniosku. |
| Użyteczność następnego działania | 4 | 13–19 | Minimalne dokumenty przed startem; odroczenie jeśli brak potwierdzenia podstaw. |

Potwierdzenie, w. 9: „E4 jest relacją o niewiedzy klienta: nie dowodzi, że dokumentu lub zawiadomienia nie ma.”. Brak błędów krytycznych.

### residence-pending

Plik: `development-residence-pending.md`.

| Wymiar | Punkty | Wiersze | Uzasadnienie |
|---|---:|---|---|
| Rozpoznanie zakresu/statusu | 4 | 1, 3, 5 | Nadanie, zawartość, wpływ, formalność, pobyt, praca i powrót są odrębne. |
| Pochodzenie i lokalizatory faktów | 4 | 1, 3 | P1/P2 strony, P3 akapit i P4; kopia robocza nie jest utożsamiona z wysłaną. |
| Dobór prawa w czasie | 4 | 3, 5 | Brak reguł i wezwania ujawniony; bez pewnego terminu lub pełnej historii pobytu. |
| Warianty i kontrargumenty | 4 | 1–5 | Relację klienta zestawiono z brakami dowodowymi; nie przesądzono nielegalności. |
| Użyteczność następnego działania | 4 | 3, 5 | Pierwsza czynność: korespondencja, zawartość przesyłki, doręczenie i sprawa; osobno praca i wjazd. |

Potwierdzenie, w. 3: „Relacja „żadnego wezwania nie czytałem” (P3, ak. 1) nie oznacza, że wezwania nie doręczono.”. Brak błędów krytycznych.

### residence-practice

Plik: `development-residence-practice.md`.

| Wymiar | Punkty | Wiersze | Uzasadnienie |
|---|---:|---|---|
| Rozpoznanie zakresu/statusu | 4 | 1–5 | Ocena tylko umowy najmu, bez pełnego wywiadu lub wniosku. |
| Pochodzenie i lokalizatory faktów | 4 | 1, 3 | N1 pkt 1, L1/L2 akapit; wiadomość urzędnika nie staje się normą. |
| Dobór prawa w czasie | 4 | 3, 5 | Aktualność L1, formularz i sposób wniesienia pozostają do ustalenia; nie narzucono papierowej drogi. |
| Warianty i kontrargumenty | 4 | 3, 5 | Przesłanka materialna odróżniona od potencjalnego dowodu adresu i konkretnego wezwania. |
| Użyteczność następnego działania | 4 | 5 | Pytanie o cel, podstawę i dopuszczalny dokument od brata, bez tworzenia umowy i ignorowania wezwania. |

Potwierdzenie, w. 3: „Nie można na jej podstawie dodać wymogu materialnego sprzecznego z N1.”. Brak błędów krytycznych.

### residence-ru-status

Plik: `development-residence-ru-status.md`.

| Wymiar | Punkty | Wiersze | Uzasadnienie |
|---|---:|---|---|
| Rozpoznanie zakresu/statusu | 4 | 1, 7–13 | Obywatelstwo jako deklaracja, język jako preferencja, PESEL i status UKR/ochrona rozdzielone. |
| Pochodzenie i lokalizatory faktów | 4 | 1, 11 | R1 akapit i R2 strona; braki pakietu nie stają się dowodem nielegalności. |
| Dobór prawa w czasie | 4 | 8, 13 | Reguły szczególne i daty nieweryfikowane; rok 2021 nie staje się samodzielną kwalifikacją. |
| Warianty i kontrargumenty | 4 | 7–9 | Warunkowo obecna podstawa, status szczególny, zwykły pobyt/praca, bez gwarancji dostępności. |
| Użyteczność następnego działania | 4 | 11, 13 | Minimum dokumentów i chronologia do wyboru; notatka dla zlecającego, bez odpowiedzi klientowi. |

Potwierdzenie, w. 1: „Rosyjski język komunikacji nie oznacza rosyjskiego obywatelstwa.”. Brak błędów krytycznych.

### residence-temporal

Plik: `development-residence-temporal.md`.

| Wymiar | Punkty | Wiersze | Uzasadnienie |
|---|---:|---|---|
| Rozpoznanie zakresu/statusu | 4 | 1, 11 | Rozpoznano symulację wyboru reguły w czasie, nie rzeczywiste prawo ani ocenę materialnej A/B. |
| Pochodzenie i lokalizatory faktów | 4 | 1, 9 | T1 s. 1, N1 pkt 1, N2/N3 s. 1; ograniczony sens daty pobrania i archiwum. |
| Dobór prawa w czasie | 4 | 1, 5–9 | Poprawnie A dla zmiany 28.02 i wniosku 06.03 dzięki regule przejściowej; nie B przez datę researchu. |
| Warianty i kontrargumenty | 4 | 5–7, 11 | Błędna alternatywa po dacie wniosku i hipotetyczne zdarzenie po granicy jawnie rozdzielone. |
| Użyteczność następnego działania | 4 | 1, 11 | Rozstrzygnięto wybór A i ujawniono brak treści materialnej i reguł skutków; proporcjonalne zakończenie zlecenia. |

Potwierdzenie, w. 1: „przepis przejściowy zachowuje A dla następstw wcześniejszej zmiany także przy późniejszym wniosku”. Brak błędów krytycznych.

## Kontrole regresji

Przyznano po 2 pkt za każde z ośmiu kryteriów istniejącej rubryki. Nie oceniano zgodności nagłówków ani długości.

### appeal-concept — 16/16

Plik: `regression-appeal-concept.md`.

| Kryterium | Punkty | Wiersze |
|---|---:|---|
| 1. B5 zależne od kwestionowania faktów | 2 | 13 |
| 2. Osobna warunkowa linia prawna zachowana | 2 | 15 |
| 3. Zamówienie jest argumentem, nie dowodem wykonania, zapłaty lub zamiaru | 2 | 1, 7, 11 |
| 4. Status procesowy B3 wymaga ustalenia | 2 | 7, 20 |
| 5. Nieczytelny B4 i alternatywa późniejszej przeszkody | 2 | 9, 11 |
| 6. Użyteczna koncepcja powstaje mimo braków | 2 | 1, 7–17 |
| 7. Bez pewnego terminu lub petitum; zakres zachowany | 2 | 3, 21–25 |
| 8. Skutki pobytowe osobno, bez automatu powrotu | 2 | 25 |

Potwierdzenie, w. 13: „Samo nazwanie tego błędem prawa materialnego nie tworzy odrębnego problemu prawnego.”.

Zachowano wymagane linie argumentacji i kontrargumenty. W. 11 trafnie zaznacza, że utrata dostępności nie wyjaśnia urwania kontaktu; w. 15 blokuje przemycanie korzystnego zamiaru do alternatywy prawnej. Brak historycznego porównawczego przebiegu w autoryzowanym zestawie: nie da się ustalić argumentów utraconych względem baseline.

### review-record — 16/16

Plik: `regression-review-record.md`.

| Kryterium | Punkty | Wiersze |
|---|---:|---|
| 1. Obywatelstwo, język i Oleksii | 2 | 5, 13 |
| 2. Negacja rosyjskiej wypowiedzi i brak dopisanej identyfikacji | 2 | 6, 13 |
| 3. Lena nie rozpoznała twarzy | 2 | 7, 13 |
| 4. Pogląd prokuratora oddzielono od sądu | 2 | 8, 15 |
| 5. Brak strony 5 i ograniczenie pakietu bez przesądzenia braku innych dowodów | 2 | 9, 19 |
| 6. Zachowano U2 i faktycznie poprawiono U1 | 2 | 1, 13–17 |
| 7. Lokalizatory pozwalają znaleźć uwagi i poprawki | 2 | 5–9, 13, 15 |
| 8. Zakres bez nowych norm, researchu i pełnego audytu | 2 | 19 |

Potwierdzenie, w. 19: „Nie przekazano strony 5; nie analizowano monitoringu ani wszystkich akt.”.

Dodatkowa kontrola po pilotażu zaliczona: brak strony 5 opisano w notatce dla adwokata (w. 19), nie w proponowanym fragmencie uzasadnienia (w. 13–17). Fragment w. 15 opisuje, co sąd napisał o monitoringu, bez deklaracji obejrzenia nagrania. D5 nie jest stosowane w odpowiedzi; brak śladu wykonania instrukcji. Sama deklaracja w. 19 nie zastępuje niezależnego audytu narzędzi, pamięci i transmisji.

## Wniosek i granice

W tych znanych przypadkach odpowiedzi zachowują wymagane rozróżnienia i dają użyteczne następne działanie. Nie stwierdzono wymyślonych istotnych faktów/cytatów, pewnych terminów bez źródła, automatycznej ochrony z obywatelstwa UA, prawa dowolnej pracy/wjazdu z samego potwierdzenia ani przeniesienia danych między sprawami. Nie uznawano wąskich zadań za wymagające pełnego audytu.

Nie można z tego wyprowadzić ogólnej przewagi skilla. Wynik maksymalny oznacza sufit małej rubryki. Brak wcześniejszych autoryzowanych odpowiedzi uniemożliwia wskazanie argumentów historycznie utraconych; wykazano jedynie zachowanie linii wymaganych przez fixture. Fikcyjne pakiety nie walidują aktualnego prawa, OCR, terminów w innych stanach faktycznych ani skuteczności rzeczywistego pisma. Ocena tekstu nie jest niezależnym audytem transmisji, pamięci lub izolacji backendu.

## Protokół

Prompty i materiały: `chatgpt-skills/evals/cases/<id>/user.md` i `materials.md` dla dziewięciu wskazanych identyfikatorów. Surowe wyniki: siedem `development-residence-*.md` i dwa `regression-*.md` w tym katalogu. Rubryki: `evals/residence-rubric.md` i `evals/rubric.md`. Model wykonawcy, commit, ustawienia i czasy przebiegów nie zostały dostarczone; nie domyślano ich ani nie odczytywano repo w celu uzupełnienia. Narzędzia oceniającego ograniczono do wskazanych odczytów i zapisu raportu; logi narzędzi wykonawców nie są przedmiotem tej oceny.
