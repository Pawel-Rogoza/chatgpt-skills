# Testy zachowania

Pakiety w `cases/` są fikcyjne. Nie dodawaj tutaj materiałów klientów. Każdy zawiera rzeczywiste polecenie testowe (`user.md`) i, jeśli potrzebne, surowe materiały (`materials.md`). Kryteria oceny są osobno w [rubric.md](rubric.md); nie przekazuj ich badanemu modelowi.

Przeprowadź próbę w nowym zadaniu, podając polecenie i materiały. W wariancie ze skillem wskaż właściwy skill z tego wydania; w wariancie bazowym nie aktywuj skilli prawnych. Dla obu zachowaj ten sam dostęp do źródeł, ustawienia i model, o ile środowisko pozwala je kontrolować. Po próbie zachowaj surową odpowiedź i informację o odczytanych referencjach. Nie utożsamiaj samooceny modelu z oceną adwokata.

[routing.json](routing.json) opisuje osobny test automatycznego doboru. Jawne wywołanie skilla nie potwierdza poprawnego routingu. Wynik `neither` oznacza, że żaden z pakietowych skilli nie powinien przejąć zadania.

Wyniki robocze zapisuj do ignorowanego `evals/runs/`. Publikuj wyłącznie wyniki z materiałami syntetycznymi, po sprawdzeniu ich zawartości. Testy techniczne w `tests/` sprawdzają pakowanie i referencje, nie skuteczność prawną. Rozszerzenie do 20 scenariuszy opisano w [recenzji architektury](../legal-ai-review-v0.2-pl.md).

Przypadki `case-*` i [rubryka analizy akt](case-analysis-rubric.md) rozszerzają pilot o A1. `case-ocr/scan.pdf` jest rzeczywistym syntetycznym dokumentem obrazowym; trzeba go przekazać obok `user.md` i `materials.md`. Nie zastępuj odczytu obrazu samą deklaracją testera.

Przypadki `client-*` i [rubryka objaśnień](client-explanation-rubric.md) obejmują po dwa zadania PL/UA/RU oraz granicę wysyłki. [Raport 23.09](results/2026-09-23/report.md) zawiera 18 własnych odpowiedzi autora, wyraźnie oddzielonych od niezależnych prób 22.09. Nie używaj ich jako baseline ani ukrytego zestawu odbiorczego.

B1: osiem katalogów `detention-*`, [rubryka](detention-rubric.md) i [raport](results/2026-09-23-b1/report.md). Przedłużenie i detencja administracyjna testują granicę zakresu; nie są dowodem pełnej obsługi tych procedur. Nowe wpisy routingu są specyfikacją oczekiwań, nie wykonanym testem hosta.
