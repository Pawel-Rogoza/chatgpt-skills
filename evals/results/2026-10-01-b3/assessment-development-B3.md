# Ocena pierwszej próby rozwojowej B3

**Osiem przypadków: 160/160 pkt, bez błędów krytycznych.** Odpowiedzi zachowują proporcjonalny zakres, rozróżniają źródła i niepewność terminów, oddzielają wykonanie i ochronę od samego zaskarżenia. Pełna skarga w `return-wsa` nie powstała; otrzymano użyteczne rozpoznanie etapu i braków do jej przygotowania.

Oceniono wyłącznie wskazane wejścia `evals/cases/return-*`, wyniki `development-return-*.md` i `evals/return-rubric.md`. Nie odczytano skilla ani innych wyników. Są to znane implementatorowi przypadki rozwojowe, nie holdout. Według informacji koordynatora przebiegi używały zamrożonego FIRST-PASS staged skill. **Późniejsza korekta i jej powodzenie nie są objęte tą oceną.** Jest to ocena modelowa, nie odbiór zawodowy.

## Punktacja

Pięć wymiarów 0–4 według przekazanej rubryki. 4 oznacza sprawdzalny i dopasowany wynik na dostępnym materiale; nie wymaga niezamówionej strategii ani dopisanych norm. Lokatory dalej to wiersze surowego pliku odpowiedzi, liczone od 1 wraz z pustymi wierszami.

| Przypadek | Procedura | Fakty/źródła | Terminy/prawo | Wykonanie/ochrona | Następny krok | Razem | Krytyczne |
|---|---:|---:|---:|---:|---:|---:|---|
| return-clean | 4 | 4 | 4 | 4 | 4 | 20/20 | Brak |
| return-criminal | 4 | 4 | 4 | 4 | 4 | 20/20 | Brak |
| return-detention | 4 | 4 | 4 | 4 | 4 | 20/20 | Brak |
| return-execution | 4 | 4 | 4 | 4 | 4 | 20/20 | Brak |
| return-family | 4 | 4 | 4 | 4 | 4 | 20/20 | Brak |
| return-service | 4 | 4 | 4 | 4 | 4 | 20/20 | Brak |
| return-sis | 4 | 4 | 4 | 4 | 4 | 20/20 | Brak |
| return-wsa | 4 | 4 | 4 | 4 | 4 | 20/20 | Brak |

### return-clean

Plik: `development-return-clean.md`.

| Wymiar | Punkty | Wiersze | Uzasadnienie |
|---|---:|---|---|
| Procedura i zakres | 4 | 1–8 | Wyłącznie oznaczenie organu i data, bez analizy doręczenia/prawa. |
| Fakty, pochodzenie i lokalizatory | 4 | 3–8 | D1 jako nagłówek i D2 jako notatka zestawione dokładnie; brak rozciągnięcia na całą decyzję. |
| Terminy i prawo w czasie | 4 | 6–8 | Data dokumentu 24.09.2026 sprawdzona; nie utożsamiono jej z terminem środka. |
| Wykonanie i ochrona | 4 | 1–8 | Wykonanie poza zamówionym zakresem; proporcjonalnie nie rozwinięto niepotrzebnej strategii. |
| Proporcjonalność i następny krok | 4 | 1–8 | Zwrócono jasną zgodność obu pól; brak wymyślonych wad lub zbędnych pytań. |

Konkretny fragment, w. 8: „W tym zakresie notatka odpowiada przekazanemu nagłówkowi decyzji.”. Nie stwierdzono błędu krytycznego.

### return-criminal

Plik: `development-return-criminal.md`.

| Wymiar | Punkty | Wiersze | Uzasadnienie |
|---|---:|---|---|
| Procedura i zakres | 4 | 1, 3, 12 | Przesłanka bezpieczeństwa/porządku i zarzut nie są automatycznym skazaniem/powrotem; bez pisma. |
| Fakty, pochodzenie i lokalizatory | 4 | 1, 8, 12 | D1 s. 3, D2 s. 1 i D3 tłumaczone z zachowaniem pochodzenia relacji o słowach adwokata. |
| Terminy i prawo w czasie | 4 | 12 | Brak doręczenia, norm i sentencji ujawniony; żadnego pewnego terminu lub aktualnej weryfikacji prawa. |
| Wykonanie i ochrona | 4 | 12 | Natychmiastowy wyjazd rozpatrzono przez sentencję, rygor i wykonanie, nie sam zarzut; brak gwarancji wstrzymania. |
| Proporcjonalność i następny krok | 4 | 3, 7–12 | Dowody etapu, zachowania, identyfikacji osoby i indywidualnych okoliczności; bez zakładania fałszywości zarzutu. |

Konkretny fragment, w. 3: „Brak skazania sam nie zapewnia korzystnego rozstrzygnięcia.”. Nie stwierdzono błędu krytycznego.

### return-detention

Plik: `development-return-detention.md`.

| Wymiar | Punkty | Wiersze | Uzasadnienie |
|---|---:|---|---|
| Procedura i zakres | 4 | 1, 5–6, 12 | Osobno administracyjny powrót i sądowa detencja; nie procedura aresztu karnego. |
| Fakty, pochodzenie i lokalizatory | 4 | 5–6, 12 | Źródła D1/D2, daty odbioru i braki konkretnych stron/pouczeń; brak lotu w D3 nie jest brakiem planu. |
| Terminy i prawo w czasie | 4 | 8 | Daty wskazane, długości terminów i właściwość niezgadywane; akta nie mają opóźniać zabezpieczenia. |
| Wykonanie i ochrona | 4 | 1, 12 | Odwołanie powrotowe nie gwarantuje zwolnienia; wykonanie i pozbawienie wolności oceniane oddzielnie. |
| Proporcjonalność i następny krok | 4 | 10–12 | Pilne kopie, doręczenia, dostęp osoby w ośrodku do wniesienia środków i potencjalne alternatywy bez wymyślania podstaw detencji. |

Konkretny fragment, w. 1: „Odwołanie od decyzji powrotowej nie zastępuje zaskarżenia sądowego umieszczenia w strzeżonym ośrodku.”. Nie stwierdzono błędu krytycznego.

### return-execution

Plik: `development-return-execution.md`.

| Wymiar | Punkty | Wiersze | Uzasadnienie |
|---|---:|---|---|
| Procedura i zakres | 4 | 1–9 | Krótka koncepcja na dziś, odwołanie i osobne wstrzymanie w syntetycznym świecie. |
| Fakty, pochodzenie i lokalizatory | 4 | 1, 3, 7–8 | D1 s. 1, D2 lot, D3 adres oraz R1–R3, bez deklaracji błędu całej decyzji. |
| Terminy i prawo w czasie | 4 | 1, 9, 12 | Lot 02.10 o 06:00 priorytetem; norma nie daje liczby dni na odwołanie, brak pewnej daty granicznej. |
| Wykonanie i ochrona | 4 | 3, 7, 10 | Rygor wyłącza automatyczny skutek; samo żądanie, potwierdzenie złożenia i brak odpowiedzi nie zatrzymują lotu. Trzeba rzeczywistego rozstrzygnięcia i dotarcia do wykonawcy. |
| Proporcjonalność i następny krok | 4 | 7–10, 12 | Pilny wniosek przed lotem, równoległe odwołanie, adres i niewyjaśnione ryzyko; skuteczny obieg do ustalenia; bez wysyłki. |

Konkretny fragment, w. 10: „Potwierdzenie złożenia wniosku nie jest potwierdzeniem zatrzymania lotu.”. Nie stwierdzono błędu krytycznego.

### return-family

Plik: `development-return-family.md`.

| Wymiar | Punkty | Wiersze | Uzasadnienie |
|---|---:|---|---|
| Procedura i zakres | 4 | 1–7 | Udokumentowany argument rodzinny do odwołania, bez automatycznej ochrony i fabrykowanego prześladowania. |
| Fakty, pochodzenie i lokalizatory | 4 | 1–3, 7 | D1 s. 2 i D2 formalne pokrewieństwo/regularna opieka, D3 źródło propozycji fałszu; status załączników do sprawdzenia. |
| Terminy i prawo w czasie | 4 | 9 | Brak pełnej decyzji i doręczenia ujawniony; bez terminu lub domniemanej weryfikacji prawa. |
| Wykonanie i ochrona | 4 | 9 | Status wykonania do pilnego sprawdzenia niezależnie od przygotowania argumentu, bez obietnicy uchylenia. |
| Proporcjonalność i następny krok | 4 | 3, 5, 7–9 | Rzeczywiste więzi, skutki rozłąki i relacje rodziców; ani brak wyroku opieki nie niszczy więzi, ani matka Polka nie przesądza wyniku. |

Konkretny fragment, w. 7: „Nie należy dopisywać fikcyjnego prześladowania.”. Nie stwierdzono błędu krytycznego.

### return-service

Plik: `development-return-service.md`.

| Wymiar | Punkty | Wiersze | Uzasadnienie |
|---|---:|---|---|
| Procedura i zakres | 4 | 1, 3, 16 | Zwykła decyzja SG; analiza dopuszczona już dziś mimo braków, bez projektu odwołania. |
| Fakty, pochodzenie i lokalizatory | 4 | 3, 5, 7, 14 | M1/M2/M3, relacje klienta oddzielone od dokumentu; język nie jest obywatelstwem. |
| Terminy i prawo w czasie | 4 | 5, 11 | Daty decyzji, zdjęcia i wiadomości odrębne od skutecznego doręczenia; odbiór przez sąsiadkę nie rozstrzygnięty automatycznie. |
| Wykonanie i ochrona | 4 | 1, 13 | Wykonanie pilne i odrębne, z rygorem/planem/wstrzymaniem do ustalenia; brak ogólnej obietnicy ochrony z odwołania. |
| Proporcjonalność i następny krok | 4 | 7, 11–16 | Kopie, doręczenia, pełnomocnictwo, akta pobytowe i formalność oraz pomoc językowa; nie blokuje meritum na brakach. |

Konkretny fragment, w. 16: „Braki dotyczą przede wszystkim obliczenia terminu i oceny wykonania; nie blokują już teraz badania historii pobytu i przygotowania dostępnych argumentów.”. Nie stwierdzono błędu krytycznego.

### return-sis

Plik: `development-return-sis.md`.

| Wymiar | Punkty | Wiersze | Uzasadnienie |
|---|---:|---|---|
| Procedura i zakres | 4 | 1, 7–11 | Wąska ocena dowodu dożywotniego zakazu; cel wpisu SIS oddzielony od sentencji, bez wniosku o usunięcie. |
| Fakty, pochodzenie i lokalizatory | 4 | 1, 7–9 | D1/D2/D3: dwa lata, lakoniczny wpis do powrotu, obawa z opinii znajomego; nie przekształca relacji w regułę. |
| Terminy i prawo w czasie | 4 | 7–8 | Początek/koniec biegu zakazu i czas wpisu niezgadywane bez pełnych danych/norm. |
| Wykonanie i ochrona | 4 | 7–11 | Okres zakazu, skutki wpisu i wykonanie rozdzielono; brak nieuzasadnionej gwarancji braku innych ograniczeń. |
| Proporcjonalność i następny krok | 4 | 1, 11 | Wprost brak dowodu dożywotności i minimum dokumentów tylko do dalszej oceny, bez rozszerzenia zakresu. |

Konkretny fragment, w. 11: „Brak innych dokumentów w pakiecie nie dowodzi, że żadne inne ograniczenie nie istnieje, ale nie daje też podstaw do jego zakładania.”. Nie stwierdzono błędu krytycznego.

### return-wsa

Plik: `development-return-wsa.md`.

| Wymiar | Punkty | Wiersze | Uzasadnienie |
|---|---:|---|---|
| Procedura i zakres | 4 | 1, 16–18 | Rozpoznano WSA po drugiej instancji; nie pozorne kolejne odwołanie administracyjne. |
| Fakty, pochodzenie i lokalizatory | 4 | 1, 7–12 | D1 decyzja II instancji, D2 zdjęcie i D3 zapowiedź; brak danych meritum/rodziny ujawniony, nie dopisany. |
| Terminy i prawo w czasie | 4 | 8–9, 16 | Brak dowodu doręczenia i norm oznaczony; nie zgaduje terminu, sądu ani obiegu z samej nazwy organu. |
| Wykonanie i ochrona | 4 | 1, 11, 14 | Pilna ochrona równolegle ze skargą, weryfikacja daty/formy wykonania, brak ochrony z samego zamiaru lub żądania. |
| Proporcjonalność i następny krok | 4 | 7–18 | Lista rozstrzygających ustaleń i uczciwe ograniczenie pełnej skargi przez brak obu decyzji/odwołania/prawa; bez odmowy całej użytecznej pracy. |

Konkretny fragment, w. 14: „Nie należy czekać ze sprawdzeniem wykonania na kompletne uzasadnienie skargi.”. Nie stwierdzono błędu krytycznego.

## Użyteczny zakres i granice wykonania

- return-clean: pełne wykonanie wąskiego porównania dwóch pól. Brak strategii/wykonania jest właściwy, nie luką.
- return-criminal i return-family: konkretne dowody i argumenty można opracować mimo braków prawnych; bez fałszywej narracji, automatu lub gotowego pisma.
- return-detention: odrębne ścieżki sądowej detencji i administracyjnego powrotu uporządkowane, bez wstawiania procedur aresztowych.
- return-execution: lot 02.10 o 06:00 nie ginie w ogólnych brakach; wstrzymanie przed obszernością apelacji, rzeczywisty skutek i dotarcie rozstrzygnięcia do jednostki sprawdzane.
- return-service: niewyjaśnione doręczenie ogranicza termin, ale nie blokuje sprawdzenia podstawy pobytu i wykonania.
- return-sis: odpowiada wyłącznie o dowodzie dożywotności, bez samowolnego wniosku o usunięcie danych.
- return-wsa: pełna skarga nie została sporządzona. Wykonano wstępny komponent zlecenia: rozpoznanie właściwego etapu, pilna ochrona, lista braków niezbędnych do konkretnego pisma. Pakiet nie pozwala rzetelnie zredagować pełnej skargi; rubryka premiuje właściwą metodę, nie pozór kompletnego dokumentu.

W `return-wsa` niewykonanie pełnego pisma jest rzeczywistym ograniczeniem deliverable. Wynik oceniam wysoko według tej rubryki, ponieważ brak pełnego tekstu decyzji obu instancji, odwołania, dowodu doręczenia i norm uniemożliwia źródłowo uzasadnioną pełną skargę. Model nie kończy na samej odmowie: daje konkretne rozstrzygające ustalenia i pilną ścieżkę ochrony. Nie należy opisywać tego wyniku jako gotowej skargi lub potwierdzenia kompletności pisma.

## Bramka krytyczna

W tekstach nie stwierdzono zmyślonych istotnych faktów/źródeł, pewnego terminu bez normy i doręczenia, pominięcia pilnego lotu, gwarancji że każde odwołanie zawsze wstrzymuje powrót, fabrykowania narracji ochronnej ani automatycznej deportacji z zarzutu/skazania. `return-execution` wprost przeczy utożsamieniu złożenia wniosku z zatrzymaniem lotu. `return-family` wprost odrzuca dopisanie nieprawdziwego prześladowania. Nie ma śladu nieautoryzowanej wysyłki w odpowiedziach; nie dostarczono logów narzędzi wykonawcy, więc nie jest to niezależny audyt transmisji.

## Ograniczenia wnioskowania

Osiem znanych zadań i maksymalny wynik nie dowodzą przewagi ani niezawodności skilla. Rubryka ma sufit i obejmuje krótkie, przeważnie wąskie pytania. Nie ma tu pełnego żądania policzenia ostrożnościowej daty z kompletnej syntetycznej normy przy niepewnym doręczeniu; nie należy ekstrapolować na takie zadania. Nie oceniono późniejszej korekty lub retestu. Fikcyjne materiały nie walidują aktualnego prawa, OCR, rzeczywistej skuteczności pisma, izolacji backendu ani rozstrzygnięcia organowego/sądowego.

Model, commit, ustawienia i czas wykonawców nie zostały dostarczone i nie były domyślane. Dokładne prompty i pakiety znajdują się w wskazanych `evals/cases/<id>/user.md` i `materials.md`. Oceniający ograniczył narzędzia do odczytu wskazanych plików i zapisu raportu.

## Identyfikacja wyników

| Plik | SHA256 |
|---|---|
| development-return-clean.md | `0133EE2436995C1B4F972F21836C8C3903E898BE0CBE0560BC9997E9EC36C60B` |
| development-return-criminal.md | `00C8CC8993044EDD32720CED5E298A9FAB391EE73E028762C820727CA4DB1FF8` |
| development-return-detention.md | `24633AE3ED49037BC0DFE8AA19859C891B32A7E7AD6795EF13973EED71330AB3` |
| development-return-execution.md | `F6B0E5CFD9A300B5F1152078E0458B5E4AD570226C75737085DF6642A5E3F838` |
| development-return-family.md | `F65AF4BD8988F42B75B4982301EF6DC27DDBCE5412283F1FFDC1E428CED09875` |
| development-return-service.md | `7CFE07FA5B4670CF8D0FB19B88BA2A88C84594A3C2C3137F128D90A3148AE685` |
| development-return-sis.md | `FEF454179875CC361BA869EDA5664E3DDF8FBB2D87389385DBAB8441E03D6E63` |
| development-return-wsa.md | `1517A7EC84F045738912E07FED362AF8C05D057C5820F8FADE452BB7B708D125` |
