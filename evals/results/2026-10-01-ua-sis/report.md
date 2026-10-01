# Pilotaże UKR/CUKR i SIS — 01.10.2026

## Implementacja i research

Wersja 0.8.0: dziewięć skilli. Dodano `pl-ukraine-residence-status` i `pl-sis-alert-review`, doprecyzowano granice B2/B3, uzupełniono rejestr źródeł. Research poprzedził implementację. Raporty [UA](../../../docs/research-ukraine-return-legalisation-2026-10-01.md) i [SIS](../../../docs/research-sis-2026-10-01.md) jawnie rozdzielają ustalenia, zakres odczytu i luki.

## Kontrola techniczna — wykonana

- `scripts/package.py sync`, `check`, `build` — sukces, 68 plików pakietu.
- `python -m unittest discover -s tests` z istniejącego `.venv` — 15/15. Pierwsza próba systemowym Pythonem nie działała z powodu braku PyYAML; użyto istniejącego środowiska repo, bez instalowania zależności do systemu.
- `quick_validate.py` Skill Creator — oba nowe skille poprawne.
- `git diff --check` — sukces.
- Instalacja `legal-ai-pl@personal` przez CLI — 0.8.0, enabled.
- Odczyt `skills/list` lokalnego app-servera, `forceReload` — wszystkie dziewięć enabled, bez błędów; [zapis](skills-discovery.json). Nie uruchamiano turnu modelu przez ten interfejs.
- Porównano bajtowo wszystkie 68 plików źródła i cache — brak rozbieżności.

## Próby zachowania i ograniczenia

Przygotowano sześć przypadków `ua-*` i cztery `sis-*`, rubryki oraz oczekiwania routingu. Zapis discovery nie potwierdza automatycznego wyboru przez model. Niezależna próba dwóch przypadków jest w toku; surowe wyniki zostaną zapisane osobno. Nie deklarujemy wykonania całej dziesiątki, baseline ani odbioru adwokata.

Nie domknięto pełnej rekonstrukcji prawa, właściwych procedur sądowych ani researchu konkretnego ryzyka powrotu. Brak materiałów klientów. C1 WSA pozostaje specyfikacją, a nie zaimplementowanym dziesiątym skillem.
