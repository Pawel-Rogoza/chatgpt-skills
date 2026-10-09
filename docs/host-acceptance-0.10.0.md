# Odbiór w docelowej aplikacji, 0.10.0

Status: przygotowana instrukcja, nie wykonany odbiór. Źródła Git i zielony CI nie dowodzą, że aktywna rozmowa odczytuje nową wersję.

## Odbiór techniczny

1. Pobierz właściwy ZIP pluginu z artefaktu CI ocenionej wersji; rozpakuj zewnętrzny artefakt Actions i sprawdź dołączoną sumę właściwego ZIP-a.
2. Zaktualizuj plugin według obsługi katalogu w swoim kliencie. Nie instaluj równolegle jako pluginu i osobnych skilli.
3. Otwórz nowe zadanie. Potwierdź manifest 0.10.0, dziesięć pozycji, odczyt SKILL.md i samodzielnych referencji, szczególnie WSA i staff-workflow.
4. Na syntetycznym materiale sprawdź rzeczywisty automatyczny dobór z evals/routing.json, w tym zadania bez skilla. Zapisz prompt, rzeczywisty wybór, wersję, brak/skutek i czy trzeba ręcznie wskazać skill. Próba katalogu w raporcie jest jedynie proxy.
5. Sprawdź narzędzia i dostęp do aktualnych źródeł. Test bez źródła musi ujawnić konkretną lukę, nie udawać pełnego researchu.

## Odbiór kancelarii

Uzupełnij prywatnie ustalenia kancelarii: role, zakresy zatwierdzeń, pilny kanał i zastępstwo, dane/uprawnienia, źródła cen i umawiania. Nie używaj formularza z pustymi polami jako polityki.

Adwokat ocenia próbki i błędy według rubryk, właściwe prawo i wyjątki oraz czas potrzebnych poprawek. Osoba kompetentna językowo ocenia RU/UA, w tym zachowanie negacji, warunków i tonu. Zapisuj identyfikator próby, zmianę, powód i czas, bez treści akt w publicznym repo.

Najpierw organizacyjne wiadomości z potwierdzonych danych. Objaśnienia istniejących ustaleń muszą zachowywać zakres zatwierdzenia. Nowe indywidualne decyzje i projekty procesowe wymagają przeglądu adwokata. Bez realnego odbioru nie oznaczaj C1 jako zawodowo zatwierdzonego.

## Powrót do poprzedniej wersji

Źródłowy punkt cofnięcia: 0.9.0, e8af13af51a8d71419b46f9fc0ee88f10dccf3f1. Cofnij źródło instalacji i otwórz nowe zadanie, następnie potwierdź wersję. Nie nadpisuj dokumentów spraw ani nie zmieniaj historii zatwierdzeń.
