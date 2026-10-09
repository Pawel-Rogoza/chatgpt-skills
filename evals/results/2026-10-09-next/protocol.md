# Protokół i ograniczenia

Data 09.10.2026. Wszystkie wejścia syntetyczne, bez danych klientów. Wyniki zachowano bez poprawiania odpowiedzi modelu. Pojedyncze odpowiedzi lub pary są w plikach wynikowych; wynik recenzji i doboru jest zapisany jako JSON.

## Wersje i konteksty

- Pozostałe kontakty i niezależne porównanie: instrukcje 0.9.0, e8af13af51a8d71419b46f9fc0ee88f10dccf3f1. Nowe wejścia contact-holdout-h01–h04 utrwalono w d51ad908f216fc788fee1167ec46e43bf8d3b952 przed poprawkami instrukcji; autor bez dostępu do repo/skilli. Każdy z 16 pozostałych kontaktów miał świeży kontekst. Porównanie: trzy świeże konteksty baseline/style/full, po cztery wejścia w każdym; brak pełnej izolacji między czterema zadaniami jednej grupy.
- C1: dziesięć wejść i rubrykę utrwalono przed instrukcją. Dwa niezależne wejścia wsa-h01/h02 przygotował nowy autor bez repo/skilli; utrwalono w f191761080f073e1d6c9b6dd737b973c079b6a5a. Dziesięć rozwojowych: pięć świeżych kontekstów, po dwa odrębne zadania. Niezależne porównanie: cztery oddzielne świeże konteksty, jeden input na każdy baseline/full.
- Instrukcje 0.10.0: 85808f02ac6fe34c6c781d1db2d801df3f1be1d9. Na tym ref wykonano C1, dwa powtórzenia mobilne i trzy osobne regresje. Późniejsze commity wyników/dokumentacji nie zmieniają instrukcji.
- Dobór: jeden świeży kontekst, katalog opisów oraz 64 prompty bez expected, evals/routing-input-0.10.0.json na c5fd9217144214cca79ec68f9f46c792b3a90c95. Oceniający zna expected z evals/routing.json; badany go nie odczytał. To proxy, nie narzędzie automatycznego routingu hosta.

Badane konteksty nie dostały rubryki ani wzorca odpowiedzi. Narzędzia do pobrania: github_fetch_file, wyjątkowo github_fetch dla przypiętych raw URL. Brak researchu w zadaniach z zamkniętymi założeniami; takie zadania nie potwierdzają aktualnego prawa. Jawne wskazanie skilla testuje metodę, nie wybór skilla.

Ślady C1, regresji 0.10.0 i katalogu zapisano z odpowiedziami. Dla kontaktów 0.9.0 i czterech porównań zachowano surowe teksty i ten skrócony zapis wersji/kontekstów, bez pełnego eksportu telemetrycznego każdego wywołania. Nie opisuj go jako kompletnego trace.

Model i parametry dziedziczone ze środowiska; dokładny identyfikator backendu, seed, temperatura i powtarzalność nie są kontrolowane. Narzędzia odczytu miały podobny dostęp, lecz różna liczba instrukcji wpływa na kontekst. Nie prowadzono ślepej oceny przez niezależnego adwokata ani użytkownika RU/UA. Ocena głównego modelu może mieć stronniczość. Nie zmierzono czasu poprawek człowieka. Po ujawnieniu nowe wejścia stają się regresją, nie kolejnym holdoutem.

Zapis bloba po wygenerowaniu odpowiedzi służył wyłącznie utrwaleniu niezmienionego wyniku; nie był działaniem w sprawie klienta. Nie wysłano komunikatów, nie złożono pism ani nie wykonano technicznej aktualizacji pluginu w hoście.
