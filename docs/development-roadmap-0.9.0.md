# Kolejne wdrożenia po 0.9.0

Stan: 09.10.2026. 0.9.0 rozszerza istniejące dziewięć skilli i zachowuje status pilota. To metoda pracy ChatGPT, bez osobnej aplikacji lub automatycznej obsługi WhatsAppa. Szczegóły celu: [plan komunikacji](whatsapp-development-plan-2026-10-09.md).

| Kolejność | Zakres | Warunek zakończenia |
|---|---|---|
| 0.9.1: ocena i kalibracja | Wykonać pozostałe przypadki kontaktów, baseline/style/full, niezależny nowy zestaw i przegląd istniejących prób | Surowe wyniki, jawne błędy krytyczne, ocena adwokata i osoby kompetentnej w RU/UA; bez twierdzenia o przewadze na małej próbie |
| Pilot kancelarii | Wypełnić prywatne ustalenia kancelarii, przetestować projekty na zadaniach dopuszczonych przez kancelarię | Znany nadawca, procedura eskalacji, kontrola danych, potwierdzona wersja w docelowym środowisku, rejestr poprawek bez akt w repo |
| Routing i regresje | Sprawdzić w hoście automatyczny wybór wszystkich 9 skilli i zadania bez skilla; próbki starych apelacji i pism | Wyniki rzeczywistego doboru, brak narzucania stylu WhatsApp analizom i pismom |
| Źródła migracyjne | Ponowny datowany research UKR/CUKR, SIS, pobytu/pracy i wykonania powrotu | Weryfikacja wersji, wejścia w życie i zakresu; nowe niezależne przypadki, jawne luki |
| C1: WSA | Osobny wąski pilot skargi w sprawie powrotowej według istniejącej specyfikacji | Rozdzielenie skargi, wykonania i ochrony; baseline, kontrprzypadki, odbiór zawodowy |
| Areszt i kolejne zakresy | Dopiero potem przedłużenie aresztowania i odrębna detencja administracyjna | Specyfikacja procedury i niezależne testy; nie rozszerzać pilota samą nazwą |

Nie wprowadzaj kolejnych skilli tylko po to, by rozdzielić ton wiadomości. Wspólną metodę utrzymuj w source-policy, a kopie synchronizuj. Ustal priorytet według rzeczywistych poprawek pracowników i adwokata, nie liczby funkcji.

## Bramka następnego wydania

Każda zmiana: konkretne zadanie, ograniczony diff, zamrożona wersja, świeża próba bez ujawniania oczekiwanej odpowiedzi, odpowiednie kontrole pakietu, opis pozostałych braków. Nie twórz zawodowego zatwierdzenia na podstawie oceny modelowej. Nie zmieniaj odczytanych relacji klienta w fakty.

## Cofnięcie i instalacja

Znana wcześniejsza wersja: main przed tą zmianą, commit 848b451bb421235e6a4e09868b8fcee087984dc3, pakiet 0.8.0. Powrót do niej wymaga aktualizacji źródła instalacji i nowej rozmowy; nie zmienia dokumentów spraw. Nowa wersja źródeł nie potwierdza automatycznie aktualizacji już zainstalowanego pluginu.
