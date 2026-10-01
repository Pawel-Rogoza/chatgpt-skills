# Legal AI PL 0.6.0

B2 dodaje `pl-residence-strategy`: analizę zwykłego pobytu czasowego i pracy dla adwokata. Rozdziela podstawę pobytu, uprawnienie do pracy oraz podróż; porównuje warunki konkretnej decyzji z zatrudnieniem. Nie obejmuje pełnej obsługi ochrony międzynarodowej, szczególnych reżimów UA ani innych rodzajów zezwoleń.

Pakiet zawiera sześć skilli i 45 jawnie zadeklarowanych plików. Dotychczasowe instrukcje zmieniono wyłącznie w metadanych wersji; polityki wspólne i walidator pozostały takie same. Siedem nowych przypadków rozwojowych i osobna rubryka poprzedziły instrukcję. [Wyniki i ograniczenia](../evals/results/2026-10-01-b2/report.md).

Wydanie jest pilotem. Instalacja na docelowym hoście, routing oraz odbiór adwokata wymagają osobnego sprawdzenia. ZIP jest wynikiem istniejącego `scripts/package.py build`; nie opublikowano pluginu dla workspace ani w katalogu publicznym.

Wycofanie: wróć do poprzedniego wydania 0.5.0 i odbuduj pakiet z odpowiadającego mu commita. Nie mieszaj instrukcji i kopii referencji z różnych wydań.
