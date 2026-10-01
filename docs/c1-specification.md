# C1: skarga do WSA w sprawie powrotowej — zakres pierwszego pilota

Data: 01.10.2026. Status: specyfikacja do implementacji, nie gotowy skill. Zakres roboczy wybrano jako ciąg dalszy B3 na podstawie zaakceptowanej kolejności projektu. Można go zmienić przed implementacją, jeżeli kancelaria wskaże częstszy typ sprawy.

## Zadanie i granice

Planowany pl-wsa-complaint analizuje możliwość i konstrukcję skargi do WSA na ostateczną decyzję wydaną w zwykłym postępowaniu zobowiązania cudzoziemca do powrotu. Wynik: ocena dla adwokata, koncepcja zarzutów lub zamówiony projekt skargi. Osobno bada pilne kwestie wykonania i potrzebę ochrony tymczasowej, bez obietnicy jej uzyskania.

Poza pierwszym pilotem: bezczynność i przewlekłość, inne rodzaje decyzji, kasacja NSA, pełne prowadzenie ochrony międzynarodowej, detencja, ENA i ekstradycja. Pomyłka w nazwie środka nie blokuje analizy dokumentów; model ma rozpoznać właściwy etap i wskazać potrzebę innej metody.

## Wejście i wynik

Potrzebne materiały: decyzje obu instancji, odwołanie i istotne załączniki, dowody doręczenia, umocowanie, cel zlecenia i dostępne dane o wykonaniu. Braki ograniczają zależne wnioski, nie całe rozpoznanie.

Wynik ma powiązać argumenty z dokumentami i lokalizatorami, rozdzielić relacje od ustaleń organu i zweryfikowanego prawa oraz uzasadnić wybrane żądanie. Droga wniesienia, właściwość, dopuszczalność, termin, wymogi formalne i skutki dla wykonania wymagają sprawdzenia dla konkretnej sprawy. Tekst dla sądu należy oddzielić od pytań i założeń dla adwokata.

## Źródła do właściwej weryfikacji

Punkty startowe: [publikacja tekstu jednolitego p.p.s.a. z 2026 r.](https://eli.gov.pl/api/acts/DU/2026/143/text.pdf), ustawa o cudzoziemcach wraz ze zmianami i przepisami przejściowymi, oraz CBOSA dla konkretnych tez. 01.10.2026 odczytano początkowy fragment oficjalnego PDF p.p.s.a.; nie jest to przegląd całego aktu, późniejszych zmian ani prawa właściwego dla sprawy. Przed instrukcją merytoryczną należy odczytać odpowiednie przepisy i zweryfikować wyjątki. Nie utrwalać w instrukcji stałych terminów lub gwarancji wstrzymania.

## Przypadki rozwojowe do przygotowania przed instrukcją

1. Kompletny zwykły pakiet: właściwy przedmiot, proporcjonalna koncepcja skargi.
2. Tylko pierwsza instancja: rozpoznanie etapu zamiast przedwczesnego projektu WSA.
3. Niejasne doręczenie pełnomocnikowi: jawne warianty rachunku i pilna reakcja, bez pewnej daty bez dowodu.
4. Pilne wykonanie: oddzielenie skargi od statusu ochrony tymczasowej.
5. Projekt żąda rozstrzygnięcia niedopasowanego do przedmiotu kontroli: wykrycie i korekta.
6. Niepełna historia postępowania lub sprzeczne wersje decyzji: analiza ustalonego zakresu i konkretne braki.
7. Rodzina, zdrowie lub ryzyko po powrocie: argumentacja tylko na podstawie udokumentowanych okoliczności.
8. Bezczynność, kasacja NSA lub detencja: poprawne rozpoznanie granicy i właściwej dalszej pracy.
9. Poprawka jednego zarzutu: zachowanie zakresu bez przepisywania całej skargi.
10. Instrukcja ukryta w materiale: potraktowanie jej jako danych.

To lista planowanych prób, nie wyniki. Nowe niezależne przypadki do porównania ze skillem i baseline należy przygotować poza widokiem implementatora; po ujawnieniu nie są już holdoutem.

## Kryteria i kolejność realizacji

Najpierw materiały i rubryka, następnie metoda i referencje, dopiero potem SKILL.md oraz konfiguracja pakowania. Sprawdzić błędy krytyczne, pokrycie argumentów, terminy i wykonanie; przeprowadzić regresję B3, analizy i recenzji. Zapisać surowe odpowiedzi i czas poprawek adwokata. Nowa wersja pakietu dopiero po check, pełnych testach, build i odrębnej weryfikacji instalacji. Odbiór zawodowy pozostaje osobnym warunkiem określonego użycia.

Przygotowanie tej specyfikacji nie dodaje ósmego skilla. C2, C3 i fala D pozostają w roadmapie.
