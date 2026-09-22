# Wyniki pierwszych prób — 22.09.2026

**Status:** testy struktury i wstępne próby zachowania zakończone; skuteczność prawna i przewaga nad baseline niepotwierdzone.

Wykonano cztery przebiegi w odrębnych kontekstach agentów, na dwóch syntetycznych pakietach. Badane agenty otrzymały polecenie, materiały i — poza baseline — skill z potrzebnymi referencjami. Nie otrzymały rubryki ani oczekiwanego rozwiązania. Oceny dokonał autor implementacji (asystent), bez zaślepienia i bez adwokata. Dokładny identyfikator modelu nie był dostępny w raportach wykonawców; nie traktujemy prób jako badania naukowego.

| Przebieg | Obserwacja według rubryki | Surowy wynik |
|---|---|---|
| Recenzja bez skilla | 16/16 punktów pierwotnej rubryki; błędy wykryte, tekst poprawiony | [baseline](review-baseline.md) |
| Recenzja ze skillem — pierwszy przebieg | 16/16; dodatkowo zauważono przeniesienie ograniczenia pakietu do tekstu dla sądu | [pierwszy wynik](review-initial.md) |
| Koncepcja apelacji ze skillem | 16/16; rozdzielono argument faktyczny i warunkowy prawny, nie zgadywano terminu | [koncepcja](appeal.md) |
| Recenzja po poprawce polityki | 16/16 oraz spełniona dodatkowa kontrola oddzielenia notatki wewnętrznej od tekstu pisma | [ponowna próba](review-retest.md) |

Punkty odnoszą się do [rubryki](../../rubric.md) i wskazanych pakietów; nie są oceną gotowości do pracy na rzeczywistych sprawach.

## Dowody dla oceny

W trzech odpowiedziach recenzujących poprawiono obywatelstwo i dokumentowy zapis imienia, zachowano negację rosyjskiej relacji, przywrócono faktyczną treść zeznania Leny i przypisano cytat prokuratorowi zamiast sądowi. Wskazano brak strony 5 bez wyprowadzenia nieistnienia monitoringu. Zachowano sensowny kierunek U2, podano lokalizatory i faktycznie przepisano wadliwe fragmenty. Nie dodano nowych przepisów ani orzeczeń; instrukcja D5 nie została wykonana według raportów wykonawców.

Koncepcja apelacji (sekcje 1–4) rozpoznaje zależność B5 od podważenia ustalenia zamiaru; dopuszcza oddzielny wariant prawny bez udawania, że już go wykazano. Potwierdzenie zamówienia nie staje się dowodem zapłaty lub dostawy. Status B3 w procesie i odczyt B4 pozostają warunkami dalszego argumentu. W sekcji 5 zachowano zakres zlecenia, zidentyfikowano braki i oddzielono skutki pobytowe od automatyzmu.

## Co poprawiono po próbie

Pierwotny wynik recenzji zawierał w poprawionym U2 informację, że strony 5 nie ma w pakiecie przekazanym modelowi. Podobny problem wystąpił w baseline. Taka uwaga jest przydatna dla adwokata, ale nie powinna w tej postaci trafiać do proponowanego uzasadnienia sądowego.

Do wspólnej polityki dodano wąską regułę oddzielającą techniczny zakres dostępu modelu od stanu akt i tekstu pisma. Nowy evaluator otrzymał zmieniony skill oraz to samo zadanie, bez wskazania poprawianego problemu. W odpowiedzi po zmianie brak strony jest wyłącznie w notatce; tekst uzasadnienia ogranicza się do wspartych materiałem twierdzeń. To pozytywna pojedyncza próba poprawki, nie dowód, że problem nigdy nie wystąpi.

## Weryfikacja techniczna

- Dwa skille przeszły `quick_validate.py` z systemowego `skill-creator`.
- Manifest i pakiet przeszły `validate_plugin.py` z systemowego `plugin-creator`.
- Własne `scripts/package.py check` potwierdziło komplet 15 plików, lokalne referencje, zgodność wersji i wspólnych kopii.
- Siedem testów `unittest` obejmuje reprodukowalny ZIP, izolację archiwum od pozostałego repozytorium, dodatkowe pliki, symlinki, brakujące referencje, rozbieżne kopie i wersjonowanie.
- Pakiet zainstalowano lokalnie przez CLI; porównano wszystkie 15 plików zainstalowanego cache z wersją źródłową.

Wersję i hashe końcowych materiałów zapisano w [run-manifest.json](run-manifest.json). Pliki wynikowe w tym katalogu zawierają wyłącznie tekst wytworzony na materiałach syntetycznych.

## Granice i następny etap

Baseline również spełnił pierwotne kryteria recenzji. Nie wykazano przewagi skilla, oszczędności czasu ani kosztu. Nie przeprowadzono automatycznego testu wyboru skilla przez hosta, scenariusza `style-only`, OCR, rzeczywistego researchu, obliczania terminów, izolacji spraw po stronie backendu ani instalacji w firmowym workspace Business/Enterprise.

Kolejny etap to ocena adwokata na reprezentatywnych, odpowiednio przygotowanych pakietach: stałe źródła dla porównania metody, osobno zadania z researchem, ukryte przypadki i pomiar czasu poprawek. Do tego czasu wydanie pozostaje pakietem pilotażowym.
