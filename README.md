# ChatGPT Skills — Legal AI PL

Projekt skilli dla pracy adwokackiej w Polsce: analiza akt, apelacje karne oraz recenzja pism, z uwzględnieniem sytuacji cudzoziemców i języków PL/UA/RU.

Punktem wyjścia jest [architektura v0.2](legal-ai-architecture-v0.2-pl.md) oraz [recenzja z planem oceny](legal-ai-review-v0.2-pl.md).

Dalsze prace: [plan wdrożenia kolejnych skilli](docs/implementation-roadmap.md) oraz [gotowe polecenie dla następnego modelu](docs/next-model-prompt.md). Pierwsza kolejna fala obejmuje rozszerzenie pakowania, analizę akt i objaśnienia dla klienta PL/UA/RU.

Repozytorium przechowuje metodę, dokumentację i fikcyjne materiały testowe. Nie należy dodawać tu akt klientów, danych dostępowych ani poufnych notatek kancelarii. `.gitignore` jest pomocą organizacyjną, nie kontrolą dostępu.

## Pakiet 0.1.0 — kontrolowany pilotaż

| Skill | Zadanie |
|---|---|
| [pl-criminal-appeal](plugins/legal-ai-pl/skills/pl-criminal-appeal/SKILL.md) | Koncepcja, zarzuty, żądania i projekt apelacji karnej |
| [pl-legal-document-review](plugins/legal-ai-pl/skills/pl-legal-document-review/SKILL.md) | Recenzja istniejącego pisma, kontrola argumentów, faktów i cytatów |

Wyniki wymagają przeglądu adwokata. Pakiet nie zawiera bazy prawa, OCR, klienta SAOS ani narzędzi obliczających terminy. Korzysta z narzędzi dostępnych w danym środowisku i ma wskazać brak możliwości sprawdzenia źródła. Nie egzekwuje izolacji spraw, nie podpisuje, nie wysyła ani nie składa pism.

Każdy skill jest samodzielnym folderem z `SKILL.md` i referencjami. Wspólne reguły utrzymujemy w `source-policy/`; skrypt kopiuje je do pakietu, a kontrola blokuje rozbieżne kopie. Odwołania skilla nie wychodzą poza jego folder. Nie jest wymagany drugi skill ani prywatna ścieżka na komputerze autora.

## Instalacja w lokalnym Codex

Po sklonowaniu repozytorium i wybraniu wersji przeznaczonej do testu, w katalogu repo:

```sh
codex plugin marketplace add .
codex plugin add legal-ai-pl@personal
```

`personal` to identyfikator katalogu zapisany w `.agents/plugins/marketplace.json` tego repozytorium, nie polecenie udostępnienia publicznego. Jeśli masz już inne źródło o tej nazwie, sprawdź `codex plugin marketplace list` i nie zastępuj go bez rozstrzygnięcia konfliktu. Następnie otwórz nowe zadanie; w razie braku pozycji odśwież aplikację. Instalator może kwalifikować nazwę katalogu — użyj identyfikatora zwróconego przez CLI.

W selektorze wybierz „Apelacja karna” albo „Recenzja pisma prawnego”. Nazwa skilla może otrzymać prefiks pluginu. Samo skopiowanie plików do repozytorium nie potwierdza instalacji w ChatGPT Business/Enterprise.

Alternatywnie możesz skopiować **cały folder wybranego skilla**, łącznie z `references/` i `agents/`, do obsługiwanej lokalizacji skilli w swoim środowisku. Nie instaluj równolegle tej samej wersji jako osobnego skilla i pluginu, bo może to dać duplikaty.

## ChatGPT Business / Enterprise

Pakiet używa wspieranego manifestu `.codex-plugin/plugin.json`. Administrator docelowego workspace powinien użyć dostępnej w nim ścieżki importu/dystrybucji pluginów, wskazując katalog `plugins/legal-ai-pl` lub zbudowane archiwum, jeśli interfejs obsługuje import pliku. Dostępność zależy od produktu, uprawnień i konfiguracji. Nie zakładaj, że rejestracja lokalnego katalogu wdraża plugin całemu zespołowi.

Potwierdź w docelowym workspace: widoczność obu skilli, odczyt ich referencji, uprawnienia do plików, narzędzia researchu i właściwą wersję. Przed aktami klientów ustal zasady danych i przetestuj granice dostępu. Źródła: [OpenAI — skille](https://learn.chatgpt.com/docs/build-skills), [pakowanie i dystrybucja](https://developers.openai.com/plugins/build/plugins).

## Przykłady

- „Przygotuj roboczą koncepcję apelacji na korzyść oskarżonego. Wskaż zależności argumentów od akt; brakujące dane oznacz osobno”.
- „Sprawdź ten projekt: zgodność zarzutów z uzasadnieniem i żądaniem oraz poprawność cytatów. Popraw wykryte błędy”.
- „Oceń tylko ten pomysł na zarzut. Nie przygotowuj całej apelacji”.

Do prób bez danych klientów użyj [pakietów syntetycznych](evals/README.md).

[Raport pierwszych prób](evals/results/2026-09-22/report.md) zawiera surowe odpowiedzi, porównanie z baseline i zaobserwowaną poprawkę. Nie wykazuje jeszcze przewagi skilli ani gotowości produkcyjnej.

## Rozwój i kontrola pakietu

Python 3.9+:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/package.py check
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/package.py build
```

Zawartość każdego skilla deklaruje `config/skill-package.json`; szczegóły i ograniczenia: [konfiguracja pakowania](docs/package-configuration.md). Nowy plik nie trafia do archiwum automatycznie.

Po zmianie wspólnych reguł uruchom `scripts/package.py sync`, a potem ponownie `check`. Nie poprawiaj ich kopii w folderach skilli. Po zmianie wersji zaktualizuj manifest i `metadata.version` obu skilli. `build` nie naprawia niezgodności po cichu.

Archiwum i suma SHA-256 trafiają do `dist/`, poza Gitem. Wersja manifestu może mieć sufiks `+codex.…` do odświeżenia lokalnego cache; wersja merytoryczna skilli pozostaje `0.1.0`. ZIP obejmuje wyłącznie jawnie wymienione pliki pluginu, bez dokumentacji projektu, testów, logów i danych spraw. Testy sprawdzają również odrzucenie dodatkowych plików, symlinków, brakujących referencji i niezgodności kopii. Nie zastępuje to kontroli treści dołączanych plików.

GitHub Actions wykonuje tę samą kontrolę i budowanie pakietu, bez wywołań modeli, kluczy API i automatycznej publikacji. Wynik zielony oznacza poprawność techniczną pakietu, nie przydatność prawną.

## Aktualizacje i cofnięcie

Zachowaj znaną wersję źródłową i surowe wyniki testów. Po zmianie pluginu odśwież/reinstaluj go zgodnie z obsługą katalogu w używanym kliencie i rozpocznij nowe zadanie. Zweryfikuj zainstalowany manifest; aktywna rozmowa może nadal zawierać wcześniejsze instrukcje.

Cofnięcie polega na przywróceniu ocenionej wersji i ponownej instalacji, nie nadpisywaniu dokumentów spraw. Repozytorium nie nadaje licencji na materiały osób trzecich ani praw do importu akt do usług zewnętrznych.
