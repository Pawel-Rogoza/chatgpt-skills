# Legal AI PL 0.7.0

B3 dodaje siódmy skill, pl-return-defense: analizę zwykłej decyzji powrotowej SG pierwszej instancji i administracyjnego odwołania. Odrębnie bada wykonanie i pilną potrzebę ochrony. Projekt pisma powstaje tylko na takie zlecenie. To pilot, bez pełnej obsługi WSA, detencji, ENA i postępowania ochronnego od początku.

Pakiet zawiera 53 jawnie zadeklarowane pliki, siedem samodzielnych skilli. Dotychczasowe instrukcje zmieniono wyłącznie w metadanych wersji; wspólne polityki i kod walidatora pozostały bez zmian. Osiem rozwojowych przypadków i rubryka poprzedziły instrukcję. [Wyniki i ograniczenia](../evals/results/2026-10-01-b3/report.md).

Zbudowano ZIP istniejącym scripts/package.py build, bez zmiany formatu lub procedury instalacji. Nie wykonano nowej instalacji ani dystrybucji dla workspace. Odbiór zawodowy, routing hosta i rzeczywisty research w konkretnej sprawie pozostają do sprawdzenia.
Wycofanie: wróć do wydania 0.6.0 i zbuduj pakiet z właściwego commita; w celu wycofania obu nowych skilli wybierz 0.5.0. Nie mieszaj folderów i referencji z różnych wydań.

## Domknięcie 01.10.2026

B2 i B3 scalono do main. Zbudowano paczkę 0.7.0, wszystkie 15 testów przeszło lokalnie w Linux. Plugin zainstalowano i włączono w lokalnym Codex; host wykrywa siedem skilli bez błędów. [Raport instalacji](../evals/results/2026-10-01-local-install/report.md) zawiera SHA-256 paczki i granice sprawdzenia. Starszy akapit o braku instalacji opisuje pierwotny etap B3.
