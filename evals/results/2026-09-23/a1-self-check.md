# A1 — odpowiedzi własne, 23.09.2026

Autor implementacji wykonał sześć zadań `evals/cases/case-*` w bieżącym kontekście, świadomie stosując nowy skill i znając rubrykę. To zapis własnego wykonania, bez niezależnego wykonawcy i bez izolowanego baseline. Model: GPT-6; identyfikator backendu i parametry próbkowania niedostępne. Odczytano skill, wspólne referencje i `analysis-method.md`. Brak researchu prawnego i zewnętrznych działań.

## case-locators — odpowiedź

| Zdarzenie 03.09.2026 | Źródło i status |
|---|---|
| 08:10: Mira zostawiła niebieską torbę na ławce | Relacja Miry, L1, PDF s. 1, k. 78, ak. 1 |
| 08:15: pracownik przeniósł niebieską torbę spod ławki do punktu rzeczy znalezionych | Relacja pracownika w notatce L2, PDF s. 2, k. 81, ak. 1 |
| 08:20: po powrocie Mira nie widziała torby na ławce | Relacja Miry, L1, PDF s. 1, k. 78, ak. 1 |

Daty 4 i 5 września są datami dokumentów. Tożsamość toreb z L1 i L2 nie jest ustalona: wspólny kolor nie wystarcza. Trzeba porównać opis lub identyfikator przedmiotu z rejestrem punktu; relacje dodatkowo różnią się umiejscowieniem torby na/pod ławką.

## case-conflict — odpowiedź

Ada podaje obecność Jana przez około minutę o 18:00 według zegara przy bramie (K1, k. 12, ak. 1). Borys podaje brak kogokolwiek o 18:00 według telefonu (K2, k. 15, ak. 1). Relacje są sprzeczne, jeżeli dotyczą tego samego rzeczywistego momentu i zakresu obserwacji. Synchronizacja zegarów nie została potwierdzona; K2 wprost sygnalizuje niepewność zegara przy bramie. Rozbieżność czasu jest możliwym wyjaśnieniem, nie ustaleniem.

Warto ustalić różnicę wskazań zegarów oraz pozycję i czas obserwacji świadków. Pewny ton Ady wskazany w K3 nie daje samodzielnej podstawy do wyboru jej wersji.

## case-ocr — odpowiedź

Na obrazie `scan.pdf`, s. 1, k. 44, wypowiedź Igi brzmi: „Nie widziałam twarzy tej osoby. Widziałam tylko czerwoną kurtkę”. To relacja świadka, nie identyfikacja osoby. Pomocniczy tekst O1 pomija negację i zmienia sens pierwszego zdania. Podstawą odczytu jest obraz; rozbieżność dotyczy transkrypcji, nie dwóch odrębnych zeznań.

## case-versions — odpowiedź

V2, PDF s. 1, to podpisane 03.09.2026 oświadczenie Anny, które wprost zastępuje V1 z 01.09.2026. Według aktualnego oświadczenia Anna przekazała 300 zł; wcześniejsze 500 zł określiła jako pomyłkę. Nazwy „szkic” i „final” nie zmieniają tej relacji wersji. Nie są to dwie płatności.

Nie ustalono jednak pewnej kwoty przekazania. Druga strona podaje 200 zł (V3, wiadomość z 04.09.2026, ak. 1). Konflikt między twierdzeniami wymaga np. dokumentu płatności; zachowuję historię 500 → 300 zł oraz odrębną relację 200 zł, bez ich sumowania.

## case-missing — odpowiedź

Odczytany zakres obejmuje fragment indeksu M1, dwie strony protokołu M2 (PDF s. 1/k. 50 i PDF s. 2/k. 52) oraz dopisek M3. Ewa relacjonuje otwarte drzwi (k. 50) i brak wiedzy o tym, kto je otworzył (k. 52). Sam ten materiał nie identyfikuje osoby otwierającej.

Nie przekazano k. 51, fotografii z k. 53 ani dalszej części indeksu. Karta 51 może zmienić kontekst relacji, fotografie mogą dokumentować stan miejsca, a pełny indeks pozwoli ustalić zakres dalszych materiałów. Nie wnioskuję, że tych dowodów nie ma w aktach ani że udostępnione fragmenty wyczerpują dowody. Dopisek M3 nie jest upoważnieniem do sięgania po inną sprawę lub zapisu wspólnej pamięci.

## case-clean — odpowiedź

Pakiet obejmuje N1 — potwierdzenie nadania i N2 — potwierdzenie odbioru; oba po jednej stronie PDF, bez numerów kart. Według N1 paczkę P-101 nadaną przez Olę przyjęto do przewozu 10.09.2026 o 09:00. Według N2 Igor odebrał paczkę P-101 11.09.2026 o 12:00. Identyfikator jest zgodny; dokumenty tworzą spójną chronologię nadania i odbioru. Nie określają zawartości paczki.

## Obserwacja i ograniczenia

Własny przegląd odpowiedzi względem rubryki nie wykazał krytycznego błędu. Zachowano lokalizatory, daty zdarzeń, status relacji, konflikt 300/200 zł i ograniczenia pakietu. Odpowiedź dla zwykłego pakietu nie wymagała pytań. Możliwy dodatkowy punkt: odmienna lokalizacja torby na/pod ławką w L1/L2.

PDF rzeczywiście wygenerowano jako stronę z obrazem; pypdf zwrócił pusty tekst. Render Poppler obejrzano w tej sesji i odczytano negację oraz k. 44. Nie uruchomiono osobnego silnika OCR; błędna transkrypcja jest kontrolowanym wejściem testu, nie wynikiem mierzonego OCR. Nie badano trudnych skanów, wielotomowych akt, hostowego routingu ani izolacji backendu. Nie wykazano przewagi względem baseline; wyniki są obciążone znajomością rubryki.
