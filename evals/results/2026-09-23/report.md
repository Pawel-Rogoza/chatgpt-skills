# Fala A0–A2 — raport z 23.09.2026

**Wynik:** implementacja i instalacja lokalna ukończone. Pakiet 0.3.0 ma cztery skille. Kontrole techniczne przeszły; etap niezależnej oceny zachowania i dopuszczenia kancelaryjnego pozostaje otwarty.

## Dostarczone zmiany

| Etap | Wynik | Historia |
|---|---|---|
| A0 | Jawna konfiguracja każdego pliku, kontrola źródeł i ścieżek, 15 testów | [PR #2](https://github.com/Pawel-Rogoza/chatgpt-skills/pull/2), baza PR #1 |
| A1 | Analiza akt: lokalizatory, status twierdzeń, chronologia, konflikty i wersje | [PR #3](https://github.com/Pawel-Rogoza/chatgpt-skills/pull/3), baza PR #2 |
| A2 | Objaśnienia klientowi PL/UA/RU, kontrola sensu, granica projektu/wysyłki | [PR #4](https://github.com/Pawel-Rogoza/chatgpt-skills/pull/4), baza PR #3 |

Baza pilota `aa07932` sprawdzona przez plugin GitHub: PR #1 nadal otwarty. Nie scalano PR-ów. A0 zachował wydanie 0.1.0; A1 użył 0.2.0; końcowe A2 używa 0.3.0 z sufiksem cache. [Wydanie i wycofanie](../../../docs/release-0.3.0.md).

## Co rzeczywiście sprawdzono

- 15 testów `unittest`: wcześniejsze granice plus konfiguracja, brak/duplikaty/nieznane wpisy, kolizje ścieżek, trzeci skill o innym zestawie referencji, symlinki i preflight źródeł przed synchronizacją.
- `check`: 28 jawnie zadeklarowanych plików; kopie zgodne ze źródłami, referencje wewnątrz folderów, wspólna wersja metadanych.
- Cztery `quick_validate.py` i `validate_plugin.py` zakończone powodzeniem.
- Ponowny build dał identyczne bajty ZIP w tym środowisku. Wygenerowano sumę SHA-256.
- Porównanie z bazą wykazało, że obie wcześniejsze metody i referencje są identyczne poza numerem wersji w metadanych.
- Istniejący lokalny katalog `personal` wskazywał repozytorium; instalację odświeżono przez CLI. Zainstalowany cache `0.3.0+codex.20260923114921` ma dokładnie 28 plików i wszystkie są identyczne ze źródłem.
- Faktyczny syntetyczny PDF wyrenderowano Popplerem i obejrzano. Obraz zawiera negację, którą pominięto w kontrolowanej transkrypcji pomocniczej. Ekstrakcja pypdf zwróciła pusty tekst. Nie uruchomiono silnika OCR.

CI GitHub Actions zakończyło się powodzeniem dla trzech etapów: [A0](https://github.com/Pawel-Rogoza/chatgpt-skills/actions/runs/35847016710), [A1](https://github.com/Pawel-Rogoza/chatgpt-skills/actions/runs/35856368401), [A2](https://github.com/Pawel-Rogoza/chatgpt-skills/actions/runs/35857126958). Są to kontrole techniczne, bez wywołań modeli.

## Próby zachowania — jawnie ograniczone

W tej sesji nie uruchamiano niezależnych agentów ani nowych zadań modelowych. Autor wykonał zadania w bieżącym kontekście po poznaniu materiałów i rubryk. To **18 własnych odpowiedzi rozwojowych**, a nie 18 niezależnych pomiarów skuteczności. Nie kontrolowano osobno parametrów generacji, nie mierzono czasu poprawek adwokata. Wyniki zapisano bez przypisywania ich innemu wykonawcy.

| Zestaw | Liczba | Odpowiedzi i ocena |
|---|---:|---|
| Korekta, poprawny fragment i wąska poprawka | 3 | [A0](a0-self-check.md) |
| Analiza akt, w tym rzeczywisty obraz PDF | 6 | [A1](a1-self-check.md) |
| PL/UA/RU i brak upoważnienia do wysyłki | 7 | [A2](a2-self-check.md) |
| Recenzja i koncepcja apelacji z wcześniejszego pilota | 2 | [Regresja](regression-self-check.md) |

Własna ocena nie wykazała błędu krytycznego w tych odpowiedziach: zachowano negacje, role, warianty, lokalizatory i rozdział tekstu dla odbiorcy od uwag wewnętrznych. Nie wykonano poleceń wysyłki/pamięci z dokumentów. Przypadki bez pułapek nie doprowadziły do wymyślenia wad. Nie dopisywano dat końcowych ani przepisów.

Nie było błędu behawioralnego, który uzasadniałby kolejną zmianę instrukcji po tej własnej próbie. Nie przeprowadzano pozornego retestu ani nie przyznawano punktów sugerujących zawodowy odbiór. Najważniejsze poprawki w tej fali dotyczą mechanizmu pakowania oraz nowych, zakresowo odrębnych metod.

## Czego nie sprawdzono

**Routing hosta: niesprawdzony.** Lista triggerów ma 15 pozycji; jej statyczny przegląd i świadome zastosowanie instrukcji nie dowodzą automatycznego wyboru. Rozszerzenie katalogu może zmienić wybór istniejących skilli.

Nie przeprowadzono izolowanego, porównywalnego baseline/skill ani dwóch niewidzianych przypadków dla każdego nowego skilla. Wszystkie nowe przypadki są znane implementatorowi. Starego baseline z 22.09 nie porównuje się liczbowo z wynikami tej sesji. **Nie wykazano przewagi jakościowej, oszczędności czasu ani kosztu.**

Nie wykonano odbioru adwokata lub niezależnej kontroli językowej PL/UA/RU, rzeczywistego researchu prawa, obliczania procesowych terminów, testu dużych akt/słabych skanów, technicznej izolacji spraw ani wdrożenia Business/Enterprise. Samo niewykonanie instrukcji z syntetycznego dokumentu nie potwierdza zabezpieczenia backendu.

## Statusy i kolejny krok

| Status | Ocena |
|---|---|
| Technicznie gotowy lokalnie | Tak: walidacja, ZIP i zgodność instalacji |
| Pilot zachowania | Własne próby wykonane; niezależny odbiór otwarty |
| Dopuszczony do użycia kancelaryjnego | Nie oceniano |

Do odbioru przygotować dwa niewidziane przypadki A1 i A2 poza tym publicznym repo, wykonać kontrolowane baseline/skill i routing w nowym zadaniu oraz przekazać objaśnienia kompetentnej osobie językowej. Dla realnych danych potwierdzić środowisko, role i zasady przetwarzania.

Następne zadanie domenowe z roadmapy to **B1 — pl-criminal-detention**, po wyborze pierwszego workflow, np. kontroli postanowienia o zastosowaniu albo przedłużeniu tymczasowego aresztowania. Nie rozpoczęto B–D w ramach tego zlecenia.
