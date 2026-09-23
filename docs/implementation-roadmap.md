# Plan kolejnych wdrożeń Legal AI PL

**Data:** 22.09.2026  
**Przeznaczenie:** plan wykonawczy dla innego modelu i osoby prowadzącej projekt.  
**Status (aktualizacja 23.09.2026):** A0–A2 zaimplementowane i zainstalowane lokalnie w wydaniu 0.3.0. Próby zachowania w tej fali są własne, nie niezależne; routing hosta, holdout, baseline i odbiór zawodowy pozostają otwarte. B1 ma implementację wąskiego pilota kontroli pierwszego zastosowania aresztowania (0.4.0); B2–B3 i C–D nie są zaimplementowane. [Raport](../evals/results/2026-09-23/report.md).
**Polecenie startowe:** [next-model-prompt.md](next-model-prompt.md).

### Stan realizacji fali A — 23.09.2026

- A0: jawna konfiguracja i 15 testów pakowania; [PR #2](https://github.com/Pawel-Rogoza/chatgpt-skills/pull/2), baza PR #1.
- A1: analiza akt, sześć przypadków i syntetyczny PDF; [PR #3](https://github.com/Pawel-Rogoza/chatgpt-skills/pull/3), baza PR #2.
- A2: objaśnienia PL/UA/RU, siedem przypadków, pełny build i instalacja lokalna; [PR #4](https://github.com/Pawel-Rogoza/chatgpt-skills/pull/4), baza PR #3.
- Technicznie sprawdzono 28 plików źródłowych i ich zgodność z cache. Nie wykonano wdrożenia Business/Enterprise.
- Niezależne próby i odbiór fali A pozostają do wykonania; nie należy ponownie tworzyć A0–A2 od zera. B1 wdrożono następnie w zakresie pierwszego zastosowania aresztowania; kolejnym zadaniem domenowym jest B2 po wyborze typu sprawy pobytowej.

### Stan realizacji B1 — 23.09.2026

- [PR #5](https://github.com/Pawel-Rogoza/chatgpt-skills/pull/5), zależny od #4: `pl-criminal-detention`, pierwsze zastosowanie aresztowania; osiem rozwojowych przypadków, jawne granice przedłużenia i innych procedur.
- Pakiet 0.4.0: pięć skilli i 36 plików; [raport B1](../evals/results/2026-09-23-b1/report.md), [specyfikacja](b1-specification.md), [rejestr źródeł](../source-policy/source-register.json).
- Niezależne próby, routing i zawodowy odbiór pozostają otwarte. Rejestr nie jest potwierdzeniem kompletnego aktualnego prawa.

### Rozszerzenie A1 — rozpoznanie z wiadomości, 23.09.2026

Na prośbę użytkownika przed dalszym B2 rozszerzono istniejący `pl-case-file-analysis` o opis klienta PL/UA/RU, wklejoną korespondencję, dokumenty i research powiązany ze sprawą. To samodzielna analiza dla zlecającego, także bez formalnych akt i bez tworzenia pisma. Nie dodano szóstego, nakładającego się skilla. Wydanie 0.5.0: pięć skilli, 37 plików; [specyfikacja](intake-specification.md), [raport](../evals/results/2026-09-23-intake/report.md). Próby własne i kontrola techniczna nie zastępują niezależnego odbioru.

Poniższy plan zachowuje specyfikację i historyczną bazę z 22.09.2026.

## 1. Punkt startowy — nie pomiń tego

Repozytorium: [Pawel-Rogoza/chatgpt-skills](https://github.com/Pawel-Rogoza/chatgpt-skills).

Na dzień sporządzenia planu [PR #1](https://github.com/Pawel-Rogoza/chatgpt-skills/pull/1) jest otwarty, niescalony. Implementacja znajduje się na `codex/legal-ai-pilot`, w commicie `5ae435e08a9060a9539b5bd13365f54cd4eb41e6`. Plan jest późniejszym dodatkiem dokumentacyjnym do tej gałęzi. **Nie rozpoczynaj implementacji od starego `main`, jeżeli PR nadal nie jest scalony.** Sprawdź rzeczywisty stan GitHuba przed pracą.

Istnieją:

- `pl-criminal-appeal` i `pl-legal-document-review`, z referencjami wewnątrz samodzielnych folderów;
- wspólne źródło instrukcji w `source-policy/` i synchronizowane kopie;
- plugin `legal-ai-pl`, katalog `.agents/plugins/marketplace.json` o identyfikatorze `personal`;
- walidator/pakowanie w `scripts/package.py`, siedem testów technicznych i CI;
- dwa pakiety testowe z materiałami, scenariusz korekty językowej, lista testów routingu;
- cztery zapisane przebiegi prób, w tym jeden baseline, oraz [raport](../evals/results/2026-09-22/report.md).

W poprzednim etapie plugin zainstalowano lokalnie w środowisku autora, w wersji `0.1.0+codex.20260922204005`. **Nowe środowisko nie dziedziczy tej instalacji.** Nie ma potwierdzonego wdrożenia w docelowym Business/Enterprise.

Nie wykazano przewagi jakościowej nad modelem bez skilla. Nie wykonano oceny adwokata na reprezentatywnych sprawach, testów hostowego routingu, OCR, rzeczywistego researchu ani izolacji backendu. Żaden z tych braków nie może zostać oznaczony jako rozwiązany samym dodaniem instrukcji.

Przeczytaj przed pracą: [README](../README.md), [architekturę v0.2](../legal-ai-architecture-v0.2-pl.md), istniejące skille, politykę źródeł, kod pakowania i raport prób. Nie czytaj rubryk, jeśli Twoim zadaniem jest niezależne wykonanie testu; to materiały dla implementatora i oceniającego.

## 2. Kolejność i granice projektu

Rekomenduję trzy fale. Numeracja wskazuje zależności i kolejność, nie zobowiązanie do zbudowania wszystkiego naraz. Każdy nowy skill trafia najpierw do pilotażu. Pełna baza orzeczeń nie jest warunkiem rozpoczęcia.

| Zadanie | Wynik | Zależność | Kiedy uznać etap za użyteczny |
|---|---|---|---|
| A0 | Pakowanie gotowe na kolejne skille, komplet testów istniejących | Obecny pilot | Trzeci skill można dodać bez osłabienia listy dozwolonych plików |
| A1 | `pl-case-file-analysis` | A0 | Adwokat dostaje sprawdzalną mapę akt, faktów i luk |
| A2 | `pl-client-explanation` | A0; może korzystać z wyniku A1 | Klient otrzymuje wierne, zrozumiałe objaśnienie PL/UA/RU |
| B1 | `pl-criminal-detention` | A1 i metoda terminów | Powstaje użyteczna analiza konkretnego środka izolacyjnego i projektu reakcji |
| B2 | `pl-residence-strategy` | A1, A2 i źródła czasowe | Rozpoznano sytuację pobytową, warianty i potrzebne dokumenty |
| B3 | `pl-return-defense` | B2 i procedura administracyjna | Osobno oceniono zaskarżenie, wykonanie i pilne potrzeby ochrony |
| C1 | `pl-wsa-complaint` | Dojrzałe źródła i rozpoznanie procedury | Powstaje projekt skargi dopasowany do konkretnego przedmiotu kontroli |
| C2 | `pl-criminal-enforcement` | A1 i źródła czasowe | Wybrano właściwą ścieżkę dla konkretnej sprawy wykonawczej |
| C3 | `pl-evidence-motion` — warunkowo | A1; udokumentowane powtarzalne potrzeby | Osobny skill daje korzyść ponad referencję w istniejącym workflow |
| D | Kasacje, ENA/ekstradycja, INTERPOL, szczególne postępowania | Osobna decyzja i testy dziedzinowe | Nie traktujemy krótkiej referencji jako kompletnej obsługi |

**Domyślny zakres pierwszego zlecenia dla kolejnego modelu: A0–A2.** Potem można zlecić osobno B1, B2 i B3 według częstości spraw kancelarii. Jeżeli dominują sprawy powrotowe, B2–B3 można przesunąć przed B1; pozostają ich zależności i kryteria odbioru.

Nie twórz na tym etapie mega-skilli `pl-criminal-case`, `pl-foreigners` ani ogólnego `pl-write-any-legal-document`. Nie każdy rodzaj pisma wymaga osobnego skilla. Granicę wyznacza odrębne zadanie, potrzebna metoda i wyniki testów uruchamiania.

## 3. A0 — najpierw przygotuj istniejący pakiet

### A0.1. Rozszerzalna, jawna lista zawartości

Obecny `scripts/package.py` ma na sztywno `SKILLS`, `SHARED` i `SPECIFIC`. Zakłada też jedną referencję specyficzną na skill oraz jednakowy zestaw wspólnych referencji. Dodanie samego `SKILL.md` nie wystarczy — build odrzuci nowe pliki.

Przenieś tę deklarację do małego pliku danych, np. `config/skill-package.json`, poza katalogiem publikowanego pluginu. Opisz dla każdego skilla pliki lokalne i potrzebne wspólne referencje. **Zachowaj dokładną listę dozwolonych plików.** Nie zastępuj jej pakowaniem wszystkiego znalezionego rekursywnie. Nie buduj systemu pluginów dla walidatora.

Wymagania:

- pakiet samodzielnego skilla nie odwołuje się poza własny folder;
- brakujące, zduplikowane i nieznane wpisy konfiguracji powodują błąd;
- symlinki i ścieżki wychodzące poza dozwolony katalog są odrzucane;
- rozbieżne wspólne kopie blokują build; `check` nie naprawia ich sam;
- każdy zadeklarowany plik jest faktycznie dołączony, a każdy dołączony — zadeklarowany;
- porównanie wersji uwzględnia istniejący sufiks cache; nie zmienia po cichu wersji merytorycznej;
- dodanie skilla z dwiema referencjami specyficznymi i innym zestawem wspólnych plików ma test;
- identyczne wejście daje identyczne archiwum.

Przenieś istniejące testy i rozszerz je o rzeczywiste granice konfiguracji. Zmiana formatu nie jest okazją do osłabienia kontroli prywatnych plików.

### A0.2. Domknięcie znanych luk testów

Uruchom istniejący `style-only` i testy z `evals/routing.json`, o ile host umożliwia obserwację wyboru skilla. Gdy nie umożliwia, wykonaj test zachowania przy jawnym wywołaniu i zapisz **routing hosta: niesprawdzony**. Nie uznawaj zgodnej odpowiedzi za dowód automatycznego uruchomienia właściwego skilla.

Dodaj minimum dwie nowe próby poza dotychczasowymi przykładami: poprawne pismo bez pułapek oraz poprawkę fragmentu bez zmiany sensu i bez pełnego audytu. Sprawdź zachowanie argumentu alternatywnego, brak zbędnej eskalacji i oddzielenie notatki wewnętrznej od tekstu pisma.

### A0.3. Dwa punkty do odnotowania, bez przebudowy na zapas

Identyfikator katalogu `personal` może kolidować z inną instalacją. W nowym środowisku sprawdź katalogi; nie nadpisuj istniejącego źródła. Ewentualną zmianę nazwy zaplanuj jako jawną migrację z aktualizacją dokumentacji i sprawdzeniem instalacji, a nie uboczny skutek dodania skilla.

Obecny walidator wymaga wersji każdego skilla równej bazowej wersji pakietu. Na kolejną falę zachowaj ten prosty model i zaktualizuj wszystkie metadane; nie wprowadzaj niezależnego wersjonowania bez potrzeby. Numer kolejnej wolnej wersji ustal z repozytorium, nie zakładaj, że w chwili wykonania nadal będzie to `0.2.0`.

## 4. A1 — specyfikacja `pl-case-file-analysis`

**Zadanie:** analiza konkretnego pakietu akt: co jest dostępne, co wynika z dokumentów, gdzie są sprzeczności i jakie zagadnienia wymagają dalszej pracy. To samodzielny produkt, który wspiera późniejsze pisma.

**Uruchamiaj przy:** „przeanalizuj akta”, „zrób chronologię”, „porównaj zeznania”, „wskaż luki dowodowe”, „ustal, co wynika z materiału”.

**Nie przejmuj:** prostego streszczenia jednego dokumentu, tłumaczenia, researchu prawa bez akt ani pisania całej apelacji. Dostosuj zadanie, jeżeli użytkownik potrzebuje tylko jednego porównania.

**Wejście:** pakiet dokumentów lub fragmentów, cel analizy i znana rola klienta. Brak roli nie blokuje neutralnego uporządkowania materiału, ale ogranicza rekomendację strategii.

**Wynik:** proporcjonalny do celu manifest/zakres, chronologia, mapa istotnych twierdzeń i źródeł, sprzeczności, braki oraz następne zagadnienia. Nie narzucaj pięciu tabel do każdej odpowiedzi. Każdy istotny fakt ma lokalizator i status: relacja, twierdzenie strony, treść dokumentu, ustalenie sądu lub własny wniosek.

**Referencje:** istniejące `case-record.md`, `source-policy.md`; nowe wskazówki pracy na dużym pakiecie i porównania dowodów tylko wtedy, gdy wnoszą odrębne decyzje. `temporal-law.md` i `foreign-national.md` warunkowo. Nie kopiuj instrukcji obsługi każdej biblioteki PDF do skilla prawnego; wykorzystuj dostępne narzędzia dokumentowe.

**Ważne zachowania:** odróżniaj stronę pliku od karty akt; błędny OCR od sporu dowodowego; brak w przekazanym pakiecie od braku w aktach; kolejną wersję od odrębnego dokumentu. Rozpoznaj istotne pytania prawne, ale nie udawaj przeprowadzonego researchu. Nie ustanawiaj domyślnej wiarygodności dokumentów strony kancelarii.

**Minimalne przypadki do przygotowania:**

| Przypadek | Oczekiwane rozróżnienie |
|---|---|
| Różne numery strony PDF i karty | Odwołanie trafia do rzeczywistego fragmentu |
| Dwa sprzeczne zeznania | Sprzeczność opisana bez dowolnego rozstrzygnięcia wiarygodności |
| Zmiana negacji przez OCR | Kontrola obrazu albo oznaczona niepewność |
| Stara i poprawiona wersja dokumentu | Rozpoznanie wersji, brak mieszania danych |
| Brak strony i niepełny indeks akt | Uczciwy zakres analizy, kontynuacja niezależnej pracy |
| Zwykły kompletny pakiet | Zwięzła użyteczna analiza bez wymyślonych problemów |

Co najmniej jeden test powinien zawierać rzeczywisty syntetyczny plik PDF/obraz, nie tylko tekst opisujący „błąd OCR”. Jeżeli środowisko nie pozwala go odczytać, odnotuj ograniczenie i nie twierdź, że przetestowano OCR. Nie ma potrzeby pisać własnego silnika OCR.

**Odbiór pilota:** adwokat/oceniający może odnaleźć wszystkie kluczowe twierdzenia w pakiecie; model nie wymyśla brakującego dokumentu ani nie deklaruje pełnego przeglądu przy pracy na fragmentach. Zapisz również istotne pominięcia, nie tylko poprawność przytoczonych faktów.

## 5. A2 — specyfikacja `pl-client-explanation`

**Zadanie:** zamiana pisma, decyzji lub zatwierdzonej analizy w wierne i zrozumiałe objaśnienie dla klienta w PL, UA albo RU; przygotowanie projektu wiadomości i listy potrzebnych czynności/dokumentów.

**Uruchamiaj przy:** „wyjaśnij klientowi”, „przygotuj wiadomość po ukraińsku”, „opisz prostym rosyjskim, co wynika z tej decyzji”.

**Nie przejmuj:** każdego tłumaczenia, pełnej analizy migracyjnej, pisania pisma procesowego ani wysyłki. „Przetłumacz zdanie” pozostaje zwykłym zadaniem językowym.

**Wejście:** dokument lub analiza źródłowa, oczekiwany język i cel. Język preferowany, obywatelstwo i pisownia dokumentowa są osobnymi informacjami. Jeżeli klient nie wskazał języka, użyj informacji z kontekstu albo krótko ustal preferencję; nie wyprowadzaj jej z nazwiska.

**Wynik:** gotowy projekt objaśnienia, w razie potrzeby krótkie działania do wykonania i terminy z jawną podstawą. Zastrzeżenia dla adwokata są oddzielne. Nie dodawaj dwujęzycznej wersji automatycznie, jeśli użytkownik chce tylko jeden język.

**Granice:** wyjaśnienie źródła nie wymaga za każdym razem nowego pełnego researchu. Jeżeli jednak model ma dopisać aktualną rekomendację, ustalić skutki lub konkretny termin, musi sprawdzić podstawę albo pozostawić informację warunkową. Nie powiela bezkrytycznie widocznego błędu zatwierdzonej notatki. Nie obiecuje wyniku ani nie poświadcza tłumaczenia.

**Minimalne testy:** po dwa przypadki PL/UA/RU, łącznie co najmniej sześć: negacja, osoba wykonująca czynność, niejednoznaczny termin językowy, brak daty doręczenia, klient ukraiński preferujący RU, proste objaśnienie bez pułapki. Dodaj osobny test braku upoważnienia do wysłania wiadomości. Poproś kompetentną osobę o ocenę językową materiałów przeznaczonych do realnego użycia; samo tłumaczenie zwrotne przez model nie potwierdza jakości.

**Odbiór pilota:** zachowany sens, brak nowej pewnej tezy lub terminu bez podstawy, jasny następny krok, brak stereotypowego utożsamienia języka z obywatelstwem, brak wykonanej wysyłki.

## 6. B1 — specyfikacja `pl-criminal-detention`

**Zadanie:** analiza konkretnej sytuacji tymczasowego aresztowania w sprawie karnej, przygotowanie argumentów i właściwego projektu reakcji. Pierwsze wydanie ogranicz do jednego jasno opisanego workflow, np. kontroli postanowienia o zastosowaniu albo przedłużeniu aresztu; pozostałe warianty dodawaj po testach.

**Wejście:** postanowienie i uzasadnienie, etap, historia środka, znane daty, materiały przywołane przez sąd, cel obrony. Nie zakładaj, że użyte przez klienta słowo „areszt” oznacza konkretny środek.

**Wynik:** analiza podstaw i ich oparcia w aktach, argumenty i alternatywy, projekt w zleconym zakresie, pilne braki. Badaj aktualność przyczyn, indywidualne okoliczności i argumenty przeciwne; nie stosuj szablonu gwarantującego uchylenie.

**Granica:** zatrzymanie, wykonanie kary i detencja administracyjna cudzoziemca nie są automatycznie tym samym zadaniem. W razie innej procedury rozpoznaj potrzebę zmiany metody. Nie wpisuj do skilla stałych terminów ani uniwersalnej maksymalnej długości środka.

**Testy:** zastosowanie i przedłużenie; ogólne versus indywidualne uzasadnienie; zmienione okoliczności; błędnie nazwany środek; pilna sprawa z nieznanym doręczeniem; właściwa alternatywa; argument obrony podważony aktami. Istotne aktualne twierdzenia prawne wymagają sprawdzonych źródeł i daty.

**Odbiór:** właściwe rozpoznanie środka/procedury, brak wymyślonego terminu, argumenty odpowiadające rzeczywistym podstawom decyzji i materiałowi. Ocena adwokata przed użyciem w realnej sprawie.

## 7. B2 — specyfikacja `pl-residence-strategy`

**Zadanie:** analiza sytuacji pobytowej cudzoziemca i możliwych ścieżek działania, z mapą dokumentów, dat, przesłanek oraz niewyjaśnionych kwestii. Pierwszy zakres: wybrany, reprezentatywny dla kancelarii typ legalizacji pobytu; nie cały system migracyjny.

**Wejście:** obywatelstwo/obywatelstwa, dokumenty i decyzje, podstawa i chronologia pobytu, cel klienta, istotne okoliczności rodzinne/zawodowe, inne postępowania w niezbędnym zakresie. Nie zbieraj pełnego wywiadu, jeżeli pytanie dotyczy jednej wąskiej kwestii.

**Wynik:** ustalona sytuacja i luki, warianty z przesłankami, źródła właściwe dla dat, lista potrzebnych dokumentów i następny krok. Nie zamieniaj brakującego dokumentu w stwierdzenie nielegalności pobytu.

**Referencje:** status i daty, dokumenty tożsamości, styk karny–pobytowy, odróżnienie praktyki urzędu od prawa. Konkretne zasady dotyczące obywateli Ukrainy wymagają sprawdzenia w chwili zadania; nie utrwalaj ich w skillu jako bezterminowych reguł.

**Testy:** obywatel Ukrainy komunikujący się w RU; różne podstawy pobytu; przekroczenie daty zmiany prawa; dokument niepotwierdzający tezy klienta; praktyka lokalnego urzędu; równoległa sprawa karna; brak danych bez nadmiernego wywiadu.

**Odbiór:** warianty zależą od udokumentowanych przesłanek, stan prawny i podstawa zastosowania są jawne, brak automatycznego zrównania obywatelstwa ze statusem ochronnym. Pełne sprawy ochrony międzynarodowej pozostają poza pierwszym zakresem.

## 8. B3 — specyfikacja `pl-return-defense`

**Zadanie:** analiza konkretnej decyzji lub etapu sprawy zobowiązania do powrotu oraz przygotowanie właściwej reakcji w granicach zlecenia. Pierwsze wydanie ogranicz do oznaczonego stadium administracyjnego; etap WSA ma osobną metodę.

**Wejście:** decyzja, pouczenie, dowód/okoliczności doręczenia, etap i znane czynności, dane o wykonaniu, istotne dokumenty rodzinne, zdrowotne i ochronne tylko w potrzebnym zakresie.

**Wynik:** oddzielna ocena środka zaskarżenia, ryzyka i skutków wykonania, potrzeby ochrony tymczasowej oraz argumentów merytorycznych; projekt i notatka z pilnymi decyzjami dla adwokata.

**Granice:** powrót, ENA, ekstradycja i publiczna informacja INTERPOL to różne mechanizmy. Nie zakładaj automatycznego wstrzymania wykonania ani nie twórz gotowej historii ryzyka prześladowania. Braki nie uzasadniają zmyślania faktów; prawdziwe okoliczności należy rozpoznać i udokumentować.

**Testy:** mylące pouczenie; niejasne doręczenie; złożony środek bez ustalonego skutku dla wykonania; równoległa sprawa karna; istotne okoliczności rodzinne; informacja o ryzyku powrotu; błędne utożsamienie z ekstradycją. Co najmniej jeden test ma wymuszać szybkie wskazanie pilnego problemu przed długim researchem.

**Odbiór:** konkretna procedura i właściwe źródła, rozdzielenie zaskarżenia i wykonania, wskazanie pilnych zależności, brak pozornej pewności. Pilotaż wyłącznie z przeglądem adwokata.

## 9. Fala C i zakres odłożony

### C1. `pl-wsa-complaint`

Przygotowanie skargi do WSA w wybranym typie sprawy: przedmiot kontroli, droga do sądu, legitymacja, doręczenie, żądanie, zarzuty i uzasadnienie. Osobno rozpoznawaj, czy chodzi o decyzję, bezczynność lub inny przedmiot; zacznij od jednego wariantu. Nie przenoś mechanicznie apelacji karnej. Skarga kasacyjna do NSA jest poza zakresem. Testy: błędny środek, niepełna historia postępowania, niewłaściwy przedmiot, niespójne żądanie, wątek cudzoziemski, wniosek o ochronę tymczasową zależny od odrębnych przesłanek.

### C2. `pl-criminal-enforcement`

Rozpoznanie konkretnego zadania wykonawczego i projekt właściwego wniosku. Nie otwieraj naraz wszystkich zagadnień KKW; wybierz z kancelarią pierwszy powtarzalny typ sprawy. Oddziel diagnozę właściwego środka od oceny przesłanek. Testy: błędnie nazwany wniosek, nieznany status wykonania, aktualność dokumentacji, sprzeczne dane i skutki dla cudzoziemca. Brak wybranego typu sprawy nie blokuje pracy nad falą A/B; blokuje jedynie finalizację zakresu tego skilla.

### C3. `pl-evidence-motion` — tylko po potwierdzeniu potrzeby

Projekt wniosku dowodowego: fakt wymagający wykazania, dowód, związek z celem, etap, możliwe przeszkody i warianty. Nie jest osobną bazą prawa. Wydziel, jeśli samodzielne zlecenia i testy uzasadniają odrębny trigger; inaczej pozostaw metodę jako referencję. Testy powinny odróżniać fakt od środka dowodowego i eliminować ogólne wnioski niemające znaczenia dla sprawy.

### D. Dopiero po osobnej specyfikacji

Kasacja karna, kasacja do NSA, ENA/ekstradycja, obsługa zagadnień INTERPOL, ochrona międzynarodowa i detencja administracyjna cudzoziemców. Wymagają odrębnych źródeł, granic i testów; nie są wariantami jednej „apelacji”. Ogólny skill odwołania administracyjnego dodawaj tylko, jeśli workflow B2/B3 rzeczywiście wymaga samodzielnego zastosowania między domenami.

## 10. Prace wspólne — co równolegle, a co później

| Obszar | Teraz / przed falą B | Później, po wykazaniu potrzeby |
|---|---|---|
| Źródła | Mały rejestr: URL, rodzaj, zakres, warunki użycia, data/status sprawdzenia, znane luki | Automatyczne adaptery najczęściej używanych źródeł |
| Prawo w czasie | Procedura, testy, zapisy wersji i podstawy zastosowania | Wąski resolver dobrze określonych zagadnień |
| Akta | Lokalizatory, zakres odczytu, test syntetycznego PDF | Własny pipeline OCR tylko przy wykazanej luce |
| Orzecznictwo | Research na zadanie, cache sprawdzonych materiałów w dopuszczonym miejscu | Mały benchmark indeksu; potem ewentualnie SAOS i VPS |
| Wiedza kancelarii | Schemat i kilka uogólnionych notatek zatwierdzonych poza publicznym repo | Większa baza i sygnały ponownego przeglądu |
| Dane i workspace | Reguły danych, role, retencja, próbna instalacja na docelowym koncie | Integracje z systemami kancelarii |

Nie oznaczaj źródła jako sprawdzonego tylko dlatego, że jego adres jest w rejestrze. Nie dodawaj ogólnego `pl-legal-research` jako obowiązkowej zależności wszystkich skilli: wspólna polityka i dostępne narzędzia wystarczą, dopóki testy nie wykażą odrębnej potrzeby.

Metadane źródeł powinny rozróżniać sprawdzoną dostępność, pełny tekst, zakres prawny, aktualność i warunki wykorzystania. W pierwszej wersji wystarczy JSON/YAML i ręczny przegląd. Bez masowego pobierania korpusu, kupowania API lub uruchamiania usług w ramach samego zlecenia A0–A2.

## 11. Standard realizacji jednego skilla

Każdy pakiet prac obejmuje:

1. Krótką specyfikację: zadanie, trigger, wyłączenia, wejście, wynik, ryzyka i źródła.
2. Materiały testowe oraz osobną rubrykę przed strojeniem instrukcji. Do pilota startowo 4 przypadki rozwojowe i 2 niewidziane przez implementatora przypadki odbiorcze. Dla A2 zachowaj dodatkowo pokrycie wszystkich trzech języków.
3. Minimalny `SKILL.md`, tylko potrzebne referencje i metadane UI. Nazwa folderu odpowiada `name`.
4. Konfigurację pakowania, referencje, dokumentację i aktualizację listy triggerów.
5. Próby baseline/skill z tym samym materiałem, wersją modelu i narzędziami, o ile da się je kontrolować.
6. Poprawki wywołane obserwowanymi błędami oraz ponowny test zmienionego zachowania.
7. Commit, mały PR, wyniki CI, raport testów i instrukcję instalacji/wycofania.

Liczby testów są proponowanym minimum organizacyjnym, nie dowodem niezawodności. Niewidziane przypadki powinien przygotować odrębny evaluator lub adwokat i przechować poza materiałem dostępnym implementatorowi do czasu odbioru. Jeśli autor widział klucz, nazwij test rozwojowym — nie „holdout”. Nie obiecuj zaślepienia na podstawie samej innej nazwy katalogu.

Jeśli środowisko dopuszcza niezależne próby, wykonawcy zadania daj tylko skill, surowe materiały i polecenie, bez sugerowania błędu i oczekiwanego rozwiązania. Gdy taki podział nie jest dostępny, zapisz ograniczenie i nie udawaj niezależności. Osoba oceniająca może uznać poprawny argument spoza klucza.

### Trzy osobne statusy ukończenia

| Status | Warunek |
|---|---|
| Technicznie gotowy | Struktura, linki, synchronizacja, pakowanie, testy i instalowalność sprawdzone |
| Pilot zachowania | Wykonane zadania z surowymi wynikami i oceną; brak nierozwiązanych błędów krytycznych w badanej próbie |
| Dopuszczony do określonego użycia kancelaryjnego | Ocena adwokata, właściwe warunki danych i test docelowego środowiska |

Brak dostępnego adwokata nie blokuje przygotowania skilla i prób syntetycznych. Blokuje jedynie twierdzenie, że skill przeszedł zawodowy odbiór. Nie kończ samej implementacji ogólnym „potrzebuję eksperta”; przygotuj kompletny materiał do jego oceny.

### Bramka jakości

Zero zaobserwowanych: wymyślonych kluczowych faktów/cytatów, stanowczych terminów bez podstaw, wykonanych instrukcji z dokumentu, ujawnień między sprawami lub działań bez upoważnienia. Zachowane krytyczne zagadnienia i sensowne alternatywy. Brak istotnej regresji istniejących skilli.

Mierz odrębnie: trafność, pokrycie istotnych problemów, czas poprawek adwokata, zbędne pytania i wywołania narzędzi. Progi pilotażu z architektury są punktem startowym, nie wynikami pomiaru. Jeżeli baseline radzi sobie równie dobrze, pokaż to i oceń, czy skill daje powtarzalność lub oszczędność — nie dokładaj instrukcji tylko po to, by zwiększyć objętość.

## 12. Git, wydania i instalacja

Przed zmianami odczytaj stan repo i ewentualne `AGENTS.md`. Nie nadpisuj cudzych zmian. Preferuj `codex/…` dla nowych gałęzi.

- Jeżeli PR #1 jest scalony: pobierz aktualny `main` i rozpocznij z niego.
- Jeżeli PR #1 jest nadal otwarty: pracuj od aktualnej gałęzi pilota lub utwórz gałąź potomną i PR zależny, jawnie opisując bazę. Nie wykonuj merge tylko dlatego, że potrzebujesz kodu.
- Jeden PR powinien odpowiadać jednemu sprawdzalnemu etapowi: A0, A1, A2; ewentualnie A0+A1, jeśli rozdzielenie uniemożliwia test konfiguracji z trzecim skillem.
- Nie publikuj automatycznie pluginu w katalogu publicznym ani w całym workspace. Wdrożenie lokalne, publikacja zespołowa i udostępnienie repo to odrębne działania.

Wydanie obejmuje jawny numer wersji, build, sumę kontrolną, raport oraz znaną wersję do wycofania. Po zmianie wspólnej referencji uruchom próby istniejących skilli, których zachowanie może się zmienić. Aktualizacja źródeł nie jest dowodem aktualizacji zainstalowanego cache.

Użyj aktualnych instrukcji `skill-creator` oraz — gdy zmieniasz pakowanie/instalację — `plugin-creator`. Sprawdź bieżącą dokumentację platformy przed zmianą formatu lub procedury instalacji. Nie kopiuj prywatnych ścieżek ze starego środowiska do repozytorium.

Komendy kontrolne obecnego projektu:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/package.py sync
.venv/bin/python scripts/package.py check
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/package.py build
git diff --check
```

Po A0 zachowaj te interfejsy komend, o ile nie ma konkretnego powodu do migracji. Nie uruchamiaj `sync` jako sposobu ukrycia regresji: najpierw sprawdź, które pliki zostaną zastąpione i że edytowano źródło kanoniczne.

## 13. Co wymaga informacji z kancelarii

Do rozpoczęcia A0–A2 wystarczają materiały syntetyczne. Zbieraj równolegle, bez blokowania niezależnych prac:

- dwa najczęstsze typy spraw i pism oraz typowy rozmiar/jakość akt;
- preferowany układ pisma i przykłady po bezpiecznym przygotowaniu;
- osobę oceniającą prawniczo i językowo oraz akceptowane użycia pilota;
- docelowy workspace, role i zasady danych;
- dla B1 pierwszy workflow aresztowy, dla B2 pierwszy typ sprawy pobytowej, dla C2 pierwszy typ sprawy wykonawczej.

Nie pytaj o całą listę przed wykonaniem pierwszego kroku. Brak odpowiedzi nie oznacza zgody na nowe przetwarzanie danych ani publikację. Użyj syntetycznych przykładów i jasno opisz założenia.

## 14. Warunek zakończenia pierwszego zlecenia A0–A2

Inny model ma pozostawić: rozszerzalne pakowanie z zachowanymi ograniczeniami; dwa nowe skille; potrzebne referencje; materiały i wyniki testów; sprawdzenie regresji dwóch istniejących skilli; zbudowany pakiet; aktualną dokumentację; commit/PR i raport faktycznego stanu instalacji.

Ma osobno wymienić: co sprawdzono, co poprawiono, czego nie sprawdzono, czy zaobserwowano poprawę względem baseline oraz co wymaga oceny kancelarii. Nie powinien wdrażać od razu B–D ani uznawać wygenerowanych instrukcji za udowodnioną poprawę jakości.
