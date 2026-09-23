# Legal AI PL 0.4.0 — B1

Dodano piąty skill `pl-criminal-detention`: kontrola pierwszego zastosowania tymczasowego aresztowania w zwykłej sprawie karnej, argumenty i roboczy projekt zażalenia obrony. Pełna obsługa przedłużenia i odrębnych rodzajów pozbawienia wolności pozostaje poza tym wydaniem. [Specyfikacja](b1-specification.md).

Manifest: `0.4.0+codex.20260923185426`; metadane pięciu skilli: `0.4.0`. Cztery dotychczasowe metody i wspólne referencje nie zmieniły treści. Kod pakowania również pozostaje bez zmian.

Archiwum `dist/legal-ai-pl-0.4.0+codex.20260923185426.zip` i suma `.zip.sha256` są wynikiem lokalnego builda, poza Gitem. Dokładny hash zapisano w [manifeście sprawdzeń](../evals/results/2026-09-23-b1/run-manifest.json). Archiwum obejmuje 36 zadeklarowanych plików; nie dołącza materiałów spraw testowych, wyników, źródłowych PDF, dokumentacji repo ani rejestru źródeł.

Sprawdzenia i ograniczenia: [raport B1](../evals/results/2026-09-23-b1/report.md). Zielone kontrole techniczne oraz własne próby autora nie oznaczają zawodowego odbioru, sprawdzonego routingu lub przewagi względem baseline.

## Instalacja i wycofanie

Aktualizacja lokalna używa istniejącego katalogu `personal`, którego źródło sprawdzono jako to repozytorium, i `codex plugin add legal-ai-pl@personal`. Przed taką komendą w innym środowisku sprawdź źródło katalogu; nie nadpisuj innej instalacji o tej samej nazwie. Nowe zadanie służy do potwierdzenia odczytu nowej instrukcji; sama zgodność cache nie dowodzi doboru skilla przez hosta.

Wersja powrotna: `0.3.0+codex.20260923114921`, commit `2321f147ef5af55a521443ae7a91f498b0c33d27`. Zachowaj niezapisane zmiany, wybierz tę wersję w źródle wskazanym przez lokalny katalog, sprawdź i zbuduj stary pakiet, ponownie zainstaluj i porównaj cache. Przy problemie z cache użyj procedury `plugin-creator`. Nie usuwaj lokalnych zmian ani nie zmieniaj dokumentów spraw w ramach rollbacku. Potwierdź wersję w nowym zadaniu.

Nie zmieniono formatu instalacji ani katalogu, nie opublikowano pluginu w katalogu publicznym lub Business/Enterprise. PR B1 jest zależny od PR #4 i nie scala wcześniejszych etapów.
