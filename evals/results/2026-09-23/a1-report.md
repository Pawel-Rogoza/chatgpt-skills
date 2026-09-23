# A1 — analiza akt

Dodano `pl-case-file-analysis` z referencją pracy na większym pakiecie, warunkowymi modułami czasu/języka i jawnym pakowaniem. Wydanie etapu: 0.2.0. Wspólna polityka pozostaje treściowo w wersji 0.1.0; metadane wszystkich skilli wyrównano do wersji pakietu.

Sześć przypadków rozwojowych i [rubryka](../../case-analysis-rubric.md) powstały przed instrukcją skilla. [Odpowiedzi własne](a1-self-check.md) zawierają faktyczne wykonanie tych zadań przez implementatora. Żaden przypadek nie jest niewidziany ani niezależnie oceniony. Nie było porównywalnego baseline.

Sprawdzono wizualnie syntetyczny jednostronicowy PDF: obraz zachowuje negację, a dostarczona pomocnicza transkrypcja ją pomija. Pusta ekstrakcja tekstu potwierdza, że użyto strony obrazowej. Testuje to porównanie z obrazem w tej próbie; nie jakość silnika OCR.

Sprawdzenia: 15 testów pakowania, `check` (22 pliki), walidatory skilli i manifestu, reprodukowalny build 0.2.0, `git diff --check`. Nowy skill nie jest jeszcze zawodowo odebrany. Potrzebne są dwa niewidziane przypadki od niezależnego oceniającego, ocena adwokata i test docelowego środowiska. **Routing hosta: niesprawdzony.**
