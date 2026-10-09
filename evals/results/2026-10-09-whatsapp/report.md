# Raport 0.9.0 — kontakty i ciągłość

Wersja instrukcji: 0.9.0, commit fbd809d7909ace3c3db7b1dfcc952ed5bb74d860. Data: 09.10.2026. [Protokół i ograniczenia](protocol.md), [odczyty](reads.json), [surowe odpowiedzi](raw/).

## Co rzeczywiście wykonano

24 odpowiedzi modelowe na 16 różnych wejściach:
- cztery przypadki PL/RU × baseline / sam styl / pełny skill = 12 odpowiedzi;
- cztery przypadki UA z pełnym skillem = 4 odpowiedzi;
- osiem regresji ciągłości, po jednej dla każdego pozostałego skilla = 8 odpowiedzi.

Z 24 przygotowanych przypadków WhatsApp wykonano osiem różnych. Pozostałych 16 jeszcze nie wykonano. Osiem przypadków continuity wykonano w całości. Pięć nowych oczekiwań routingu przygotowano, ale nie wykonano w hoście.

## Porównanie czterech wiadomości

| Przypadek | Baseline | Sam styl | Pełny skill |
|---|---|---|---|
| Cena i termin bez danych | Nie wymyśla ceny ani terminu | Nie wymyśla; pyta o cel | Nie wymyśla; jasno pozostawia termin nieuzgodniony |
| Podróż, wcześniejsze AI | Nie daje zapewnienia; wspomina AI klientowi | Nie daje zapewnienia; wspomina AI klientowi | Nie daje zapewnienia; prosi o konkretne dokumenty, AI opisuje w osobnej notatce |
| Nowy dokument sprzeczny z notatką | Zachowuje konflikt; lokalizator D2 w wiadomości | Zachowuje konflikt | Zachowuje konflikt i osobno wskazuje zależność do oceny |
| Lot jutro i skarga | Wskazuje pilny kontakt; nie zapewnia wstrzymania | Wskazuje pilny kontakt; nie zapewnia wstrzymania | Pilność na początku, relacja klienta zachowana, kontakt bez czekania na dokumenty |

Ocena głównego modelu: w tych 12 odpowiedziach nie stwierdzono błędu krytycznego według rubryki. Pełny skill lepiej rozdzielił wiadomość i uwagi wewnętrzne; baseline oraz sam styl także uniknęły niebezpiecznych zapewnień. Nie wykazano przewagi bezpieczeństwa prawnego ani zmniejszenia halucynacji prawnych. Sformułowanie wariantu style o „wyznaczonym locie” mniej dokładnie zachowuje status relacji niż full o locie, o którym klientowi powiedziano.

## Ukraiński i pozostałe metody

W czterech odpowiedziach UA zachowano język, negację i status złożenia, minimum potrzebnego materiału oraz pilny kontakt na granicy. Proste potwierdzenie i objaśnienie nie dostały zbędnej notatki; niepewne i pilne zadania miały notatkę po polsku. To ocena modelowa, bez niezależnego odbioru językowego.

| Metoda | Zaobserwowane zachowanie |
|---|---|
| Analiza sprawy | Nie utożsamia pism o tej samej nazwie; nie liczy pewnego terminu ze starego AI |
| Apelacja | Zachowuje rozpoznanie głosu jako istotny kontrargument; nie fabrykuje sprzeczności |
| Recenzja | Przywraca „nie złożono” i brak obowiązku; nie uznaje zatwierdzenia AI |
| Areszt | Rozróżnia protokół zatrzymania od postanowienia sądu, ustala pilne minimum |
| Pobyt/praca | Rozdziela pobyt, pracę u nowego pracodawcy i ponowny wjazd |
| Powrót | Oddziela wpływ wniosku od jego uwzględnienia, eksponuje lot |
| UKR/CUKR | Odróżnia historyczny UKR od aktualnego NUE i relacji o innym zezwoleniu |
| SIS | Oddziela wpis A, możliwy wpis B i nieustalony status decyzji źródłowej |

W tych 12 odpowiedziach (UA + continuity) nie stwierdzono błędu krytycznego według rubryk. Brak baseline dla tych wejść uniemożliwia przypisanie sukcesu nowym instrukcjom. Nie przeprowadzono pełnej regresji starych pism, analizy całych akt ani testu nowego researchu prawnego.

## Kontrola techniczna

GitHub Actions dla zamrożonego commita: [run 37925249463](https://github.com/Pawel-Rogoza/chatgpt-skills/actions/runs/37925249463).
- package.py check: 80 plików, poprawna struktura i zgodność wspólnych kopii;
- 15 istniejących testów pakowania: OK;
- build: legal-ai-pl-0.9.0.zip i plik sumy SHA-256;
- git diff --exit-code: OK.

To kontrola techniczna, nie prawna. Raport wyników, dokumentacja i udostępnienie ZIP-a w CI zostają dodane późniejszym commitem, bez zmiany przetestowanych instrukcji. Końcowy CI należy odczytać na głowie PR przed scaleniem.

## Wdrożenie i następny krok

Źródła przygotowano w [PR #10](https://github.com/Pawel-Rogoza/chatgpt-skills/pull/10). Dostępna ścieżka kończy się na zweryfikowanym pakiecie i repozytorium. Nie potwierdzono instalacji 0.9.0 w docelowym kliencie: lokalne środowisko wykonawcze zwraca błąd uruchomienia helpera, a dostępne narzędzia pluginów nie udostępniają aktualizacji tego pakietu. Nie naruszono synchronizowanych sources/.

Następny krok: pozostałe przypadki, nowy niezależny zestaw odbiorczy, routing w hoście, zatwierdzenie ustawień kancelarii i ocena adwokata oraz użytkownika RU/UA. [Plan kolejnych wdrożeń](../../../docs/development-roadmap-0.9.0.md). Wydanie pozostaje pilotem.
