# Legal AI PL 0.3.0 — fala A

## Zakres

A0 przygotowuje jawną konfigurację pakowania. A1 dodaje analizę akt (pośrednie wydanie 0.2.0). A2 dodaje objaśnienia dla klienta PL/UA/RU. Wszystkie cztery skille mają `metadata.version: "0.3.0"`. Wspólne referencje pozostały bez zmiany treści; numer 0.1.0 w nagłówku wspólnej polityki oznacza jej niezmienioną rewizję, nie wersję pluginu.

Końcowy manifest: `0.3.0+codex.20260923114921`. Archiwum: `dist/legal-ai-pl-0.3.0+codex.20260923114921.zip`, suma w pliku `.zip.sha256` obok niego i w [manifeście sprawdzeń](../evals/results/2026-09-23/run-manifest.json). ZIP nie zawiera testów, PDF, wyników, dokumentacji projektu ani konfiguracji budowania. Nie opublikowano GitHub Release ani pluginu w publicznym katalogu.

## Stan sprawdzeń

15 testów pakowania, cztery walidatory skilli, walidator manifestu, 28 zadeklarowanych plików, identyczny powtórny build oraz porównanie 28/28 plików lokalnej instalacji z repozytorium. Szczegóły i ograniczenia prób: [raport](../evals/results/2026-09-23/report.md).

Baza do cofnięcia: commit `aa0793263e8e936f0a08d7b49c9a6c9f96658163`, plugin `0.1.0+codex.20260922204005` — poprzedni kontrolowany pilot, także bez zawodowego odbioru. PR-y są zależne; nie scalono automatycznie żadnego z nich.

## Instalacja i wycofanie

23.09.2026 sprawdzono, że zarejestrowany lokalny katalog `personal` wskazuje to repozytorium. Następnie wykonano `codex plugin add legal-ai-pl@personal` i porównano zainstalowane pliki z wydaniem. W nowym środowisku najpierw sprawdź źródło przez `codex plugin marketplace list` i `codex plugin list`; sama nazwa `personal` nie gwarantuje tego samego katalogu. Nie nadpisuj innego katalogu o tej nazwie.

Użyj nowego zadania do prób wszystkich czterech skilli. Sprawdzenie obecności w cache nie jest dowodem automatycznego wyboru przez hosta. Nie wykonano instalacji w firmowym Business/Enterprise ani publikacji zespołowej.

Aby cofnąć wersję, zachowaj lokalne zmiany i wybierz znany commit na źródle wskazywanym przez katalog instalacji. Zbuduj i sprawdź stary pakiet, ponownie zainstaluj z tego samego potwierdzonego źródła i porównaj cache. Jeżeli klient utrzymuje starą kopię, użyj procedury odświeżenia lokalnego pluginu/cache z `plugin-creator`. Nie stosuj resetu usuwającego niezapisane zmiany ani nie edytuj dokumentów spraw. Po cofnięciu rozpocznij nowe zadanie i potwierdź odczytaną wersję.

Format `.codex-plugin/plugin.json` zachowano jako nadal wspierany format zgodności, zgodnie z [dokumentacją OpenAI sprawdzoną 23.09.2026](https://developers.openai.com/plugins/build/plugins). Nie zmieniono katalogu ani procedury dystrybucji całemu workspace.
