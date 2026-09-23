# Rozpoznanie sprawy — raport 23.09.2026

Rozszerzono istniejący `pl-case-file-analysis` o relację klienta PL/UA/RU, wiadomości i research powiązany ze sprawą. Nazwa widoczna: „Rozpoznanie i analiza sprawy”. Wydanie 0.5.0 zawiera nadal pięć skilli; nowa referencja zwiększa pakiet z 36 do 37 plików. [Specyfikacja](../../../docs/intake-specification.md).

## Sprawdzone technicznie

- 15 testów pakowania, pięć walidatorów skilli, walidacja pluginu, kontrola lokalnych referencji i `git diff --check`: poprawne.
- Dwa buildy z tego samego wejścia: identyczne bajty ZIP.
- Instalacja lokalna z potwierdzonego źródła `personal`: 37/37 plików zgodnych bajtowo, bez dodatkowych plików w cache.
- Cztery pozostałe skille nie zmieniły zawartości poza numerem wersji. Wspólne reguły i kod pakowania pozostały bez zmian.
- Metadane wydania i hashe wejścia: [run-manifest.json](run-manifest.json).

## Próby własne — pięć odpowiedzi

Materiały i [rubrykę](../../intake-rubric.md) przygotowano przed edycją instrukcji. [Surowe odpowiedzi](self-check.md) sporządził autor implementacji w tym samym kontekście, znając kryteria. Nie uruchamiano niezależnego modelu.

| Przypadek | Zaobserwowane zachowanie i ograniczenia |
|---|---|
| RU, sam opis bez dokumentów | Użyteczne rozpoznanie po polsku, rozdzielone zapłacone i niezapłacone tygodnie, brak automatycznej kwalifikacji umowy lub czynu |
| UA, relacja versus wezwanie | Pięć zdań; rozróżniono treść dokumentu i relację, nie wyliczono terminu bez doręczenia |
| PL/UA/RU, przekazana rozmowa | Zachowano autorów, negację i niepewną tożsamość; nie wykonano instrukcji z materiału |
| Research o tłumaczu świadka | Rzeczywiście odczytano urzędowy tekst i metadane, wskazano właściwą rolę i przepis; **wynik częściowy**, bez pełnej rekonstrukcji stanu prawa na 23.09.2026 |
| Regresja `case-conflict` | Wąskie porównanie, różne zegary jako hipoteza, brak wyboru wiarygodniejszego świadka według tonu |

Nie odnotowano w tych odpowiedziach wymyślonych faktów ani automatycznego tworzenia pisma. To samoocena niewielkiej próby; nie dowodzi niezawodności. Research potwierdza odczyt i użycie źródła, lecz **nie zalicza kompletności czasowej analizy**. Nie deklarujemy pełnej poprawności porady na żądany dzień. Kolejna próba musi sprawdzić, czy wykonawca kończy weryfikację zmian prawa przed rozstrzygającym zastosowaniem przepisu, gdy źródła są dostępne.

## Pozostałe granice

27 wpisów w `routing.json` to oczekiwania, nie wynik testu automatycznego doboru. Brak nowego baseline, holdoutu, niezależnej oceny prawniczej i językowej. Nie testowano nowych skanów, rzeczywistego eksportu WhatsApp, integracji z kontem ani wdrożenia w Business/Enterprise. W instalacji potwierdzono pliki, nie odbiór nowej instrukcji w nowym zadaniu hosta.

Zmiana usuwa konkretną lukę poprzedniego zakresu: sformułowanie „research bez akt” mogło wykluczać analizę samej relacji klienta. Research abstrakcyjny pozostaje poza zakresem tego skilla; relacja klienta jest teraz wyraźnie materiałem konkretnej sprawy. Nie dopisano specjalistycznego skilla migracyjnego ani nowej procedury procesowej.
