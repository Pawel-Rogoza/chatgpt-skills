# Kolejne wdrożenia po 0.10.0

Stan 09.10.2026. Pakiet ma dziesięć samodzielnych skilli. Obecne wdrożenie obejmuje domknięcie 24 przygotowanych prób kontaktów, nowy niezależny zestaw, poprawki redakcyjne, ponowny ograniczony research oraz pilota C1. Wyniki i braki: [raport](../evals/results/2026-10-09-next/report.md).

| Priorytet | Następny pakiet | Wynik i warunek zakończenia |
|---|---|---|
| P0 | Odbiór 0.10.0 w aplikacji i kancelarii | Potwierdzenie wersji/dziesięciu skilli/referencji; rzeczywisty routing; prywatne zasady i zastępstwo; adwokat i kompetentna osoba RU/UA oceniają próbki oraz czas poprawek. Instrukcja host-acceptance-0.10.0.md. Nie udawać tego odbioru oceną modelową. |
| P1 | 0.10.1: kalibracja na błędach użytkowników | Zebrać zminimalizowane kategorie poprawek z pracy kancelarii, bez akt w repo. Porównać czas i istotne błędy baseline/style/full na nowym niezależnym zestawie. Rozdzielić wiadomość od notatki także w interfejsie kopiowania. |
| P1 | Dokończenie źródeł i C1 | Uzyskać odczyt konsolidacji SIS, pełnych uzasadnień CBOSA i właściwych wyjątków/zmian. Sprawdzić z adwokatem pełny syntetyczny projekt WSA, dobór żądania, terminy i ochronę; wykonać zewnętrzny research w testach, nie tylko zamknięte założenia. |
| P2 | C2: przedłużenie aresztowania karnego | Osobna specyfikacja, wejścia/rubryka przed instrukcją, podstawy i dynamika kolejnych postanowień, niezależne baseline/full, regresja pierwszego zastosowania. Nie rozszerzać dotychczasowego B1 samą nazwą. |
| P2 | C3: detencja administracyjna | Osobny reżim: umieszczenie/przedłużenie w ośrodku, indywidualne przesłanki i alternatywy, terminy/właściwy sąd, aktualne źródła i odbiór zawodowy. Nie przenosić mechanicznie reguł aresztu karnego. |
| P3 | Kolejne pisma według realnej potrzeby | Kasacja NSA, bezczynność, dalsze sprawy pobytowe lub karne dopiero po określeniu częstych zadań i jakości poprzednich metod. Żadna pozycja nie jest już wdrożona przez samą obecność w planie. |

## Warunki wydania

Zamroź instrukcje i wejścia przed próbą; oczekiwania pozostają poza kontekstem modelu. Zachowaj surowe teksty i ślady. Najpierw usuń błędy krytyczne, potem popraw ergonomię. Check, odpowiednie testy, build i kontrola diffu muszą dotyczyć końcowej głowy zmian; później oddzielnie weryfikuj zainstalowaną wersję. Dla zmiany merytorycznej wymagany jest adekwatny przegląd źródła i nowy kontrprzypadek.

Mała próba bez błędów nie wykazuje redukcji halucynacji. Priorytetem jest czas użytecznej pracy pracownika/adwokata przy zachowaniu granic źródeł i zatwierdzeń. Nie tworzyć osobnej aplikacji ani bota WhatsApp, jeśli praca w ChatGPT spełnia cel.

Poprzedni punkt źródłowy do cofnięcia: 0.9.0, e8af13af51a8d71419b46f9fc0ee88f10dccf3f1. Cofnięcie i instalacja nie zmieniają dokumentów spraw.
