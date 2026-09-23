# Jawna zawartość pakietu

`config/skill-package.json` jest konfiguracją budowania, poza publikowanym pluginem. `schema_version` ma wartość całkowitą `1`; `skills` jest niepustą listą. Każdy wpis ma dokładnie trzy pola:

- `name`: nazwa folderu i skilla, małe litery/cyfry i pojedyncze myślniki, do 64 znaków;
- `local_files`: jawne ścieżki względem folderu skilla, obowiązkowo `SKILL.md` i `agents/openai.yaml`, plus potrzebne lokalne referencje/zasoby;
- `shared_references`: jawne nazwy plików Markdown z `source-policy/`, kopiowanych do `references/` danego skilla. Lista może być pusta.

Nieznane pola, powtórzone klucze JSON, nazwy skilli, kolizje plików (także różniących się tylko wielkością liter), brak wymaganych wpisów, niekanoniczne ścieżki i symlinki są błędem. Plik nie może być równocześnie katalogiem innego pliku. `check` wymaga dokładnej zgodności faktycznej zawartości pluginu z deklaracją, odrzuca brakujące i dodatkowe pliki oraz rozbieżne kopie. Każda zmiana listy wymaga przeglądu treści nowo dopuszczonych plików.

`sync` najpierw sprawdza konfigurację, odczytuje wszystkie źródła i sprawdza cele, następnie kopiuje wyłącznie zadeklarowane wspólne referencje. Nie edytuje plików lokalnych. Nie jest transakcją odporną na awarię dysku ani jednoczesne zmiany plików przez inny proces. `check` i `build` niczego nie synchronizują.

Zachowano interfejs `sync` / `check` / `build`, kontrolę referencji wewnątrz folderu skilla oraz wersji skilli równej bazowej wersji pluginu (bez sufiksu cache). ZIP ma ustaloną kolejność, daty i uprawnienia wpisów. Identyczne wejście i środowisko kompresji dają identyczne bajty; nie deklarujemy zgodności różnych wersji zlib.

Nie zmieniono manifestu platformy ani katalogu `personal`. Sprawdzona 23.09.2026 [dokumentacja OpenAI](https://developers.openai.com/plugins/build/plugins) nadal wspiera `.codex-plugin/plugin.json` jako format zgodności. Nowa konfiguracja jest wyłącznie mechanizmem repozytorium, nie nowym formatem instalacji OpenAI.
