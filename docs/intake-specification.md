# A1 — rozpoznanie i analiza sprawy z wiadomości klienta

Wydanie 0.5.0 rozszerza `pl-case-file-analysis`. Użytkownik może wkleić nieuporządkowany opis PL/UA/RU, np. z WhatsAppa, dodać dokumenty i poprosić o research oraz wyjaśnienie sprawy adwokatowi. Formalne akta nie są warunkiem użycia. Nazwa widoczna: „Rozpoznanie i analiza sprawy”.

Wynik odpowiada celowi: sedno i etap sprawy, relacja versus dokumenty, ustalenia i wątpliwości, sprawdzone źródła prawa, warianty zależne od braków, konkretna pilność i następny krok. Krótkie pytanie może dostać krótki opis. Analiza nie generuje automatycznie pisma ani wiadomości do klienta. Dotychczasowa chronologia i porównywanie akt pozostają dostępne.

Metoda kontroluje cytowane i przekazane wypowiedzi, negacje, wieloznaczne terminy, daty względne, tożsamość osób i potoczne kwalifikacje klienta. Research wymaga odczytu źródeł oraz zastosowania ich do właściwej roli, daty i procedury; nie jest samą listą przyszłych pytań. Brak dostępu ogranicza zależny wniosek, nie całą analizę. Nie dodano integracji WhatsApp ani bazy prawa.

Granice: sama translacja i proste streszczenie nie uruchamiają pełnej analizy; abstrakcyjny research bez konkretnej sprawy nie jest osobnym skillem tego pakietu. `pl-client-explanation` przygotowuje przekaz dla klienta. Szczegółowa strategia migracyjna lub pismo procesowe nie zostają wdrożone przez samo rozszerzenie intake. Nie zmieniono wspólnych zasad ani metod pozostałych czterech skilli.

Walidacja: cztery fikcyjne przypadki i osobna [rubryka](../evals/intake-rubric.md), pięć nowych oczekiwań routingu, kontrola techniczna pakietu i porównanie instalacji. [Raport](../evals/results/2026-09-23-intake/report.md) rozróżnia własne odpowiedzi autora od niezależnego badania i odbioru zawodowego.
