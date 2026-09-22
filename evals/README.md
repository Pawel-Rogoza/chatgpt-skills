# Testy zachowania

Pakiety w `cases/` są fikcyjne. Nie dodawaj tutaj materiałów klientów. Każdy zawiera rzeczywiste polecenie testowe (`user.md`) i, jeśli potrzebne, surowe materiały (`materials.md`). Kryteria oceny są osobno w [rubric.md](rubric.md); nie przekazuj ich badanemu modelowi.

Przeprowadź próbę w nowym zadaniu, podając polecenie i materiały. W wariancie ze skillem wskaż właściwy skill z tego wydania; w wariancie bazowym nie aktywuj skilli prawnych. Dla obu zachowaj ten sam dostęp do źródeł, ustawienia i model, o ile środowisko pozwala je kontrolować. Po próbie zachowaj surową odpowiedź i informację o odczytanych referencjach. Nie utożsamiaj samooceny modelu z oceną adwokata.

[routing.json](routing.json) opisuje osobny test automatycznego doboru. Jawne wywołanie skilla nie potwierdza poprawnego routingu. Wynik `neither` oznacza, że żaden z tych dwóch skilli nie powinien przejąć zadania.

Wyniki robocze zapisuj do ignorowanego `evals/runs/`. Publikuj wyłącznie wyniki z materiałami syntetycznymi, po sprawdzeniu ich zawartości. Testy techniczne w `tests/` sprawdzają pakowanie i referencje, nie skuteczność prawną. Rozszerzenie do 20 scenariuszy opisano w [recenzji architektury](../legal-ai-review-v0.2-pl.md).
