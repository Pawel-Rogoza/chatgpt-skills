# LegalAI 0.10.0, 09.10.2026

Źródłowe wydanie pilota: dziesięć samodzielnych skilli. Nowy pl-wsa-complaint dotyczy zwykłej ostatecznej decyzji powrotowej po administracyjnym odwołaniu: koncepcja lub projekt WSA, osobna ocena wykonania i ochrony. Pozostałe skille zachowują własne zakresy; wszystkie otrzymują wersję 0.10.0 i zgodne kopie wspólnych reguł.

## Zmiany

- WhatsApp: doprecyzowany naturalny krótki styl bez długich myślników; notatka w języku zlecającego, poza tekstem klienta.
- Pracownik: potwierdzenie odbiorcy i nowego kanału przed ujawnieniem informacji; sama znajomość numeru nie jest uprawnieniem.
- WSA: rozpoznanie etapu, dowody doręczenia, ograniczony cel skargi, argument z materiałem i kontrargumentem, status ochrony oddzielony od projektu/złożenia.
- Źródła: zamknięta luka komunikatu startowego CUKR, odrębny komunikat systemu pobytowego, datowana mapa WSA oraz jawne blokady/niepełny odczyt SIS i orzecznictwa.
- Ocena: domknięte przygotowane kontakty, nowe niezależne porównania, regresje oraz 64 prompty doboru z katalogu.

[Raport](../evals/results/2026-10-09-next/report.md) zawiera 47 odpowiedzi i ograniczenia. Nie wykazano zmniejszenia halucynacji ani przewagi bezpieczeństwa nad baseline. Techniczna walidacja obejmuje 89 plików, 15 testów i ZIP z sumą. Zielony wynik nie jest odbiorem zawodowym.

## Wdrożenie i granice

Źródła są przygotowane w [PR #11](https://github.com/Pawel-Rogoza/chatgpt-skills/pull/11); rzeczywisty stan scalenia wynika z GitHub. Instalacji 0.10.0 i automatycznego routingu w hoście nie potwierdzono. [Instrukcja odbioru](host-acceptance-0.10.0.md); [następne wdrożenia](development-roadmap-0.10.0.md).

C1 nie jest kompletną bazą prawa, narzędziem liczącym terminy ani pełnym zakresem migracyjnym. Odbiór adwokata/językowy, pełny projekt na kompletnym materiale, research w próbach i odczyt wskazanych brakujących źródeł pozostają otwarte. Pakiet nie wysyła wiadomości ani pism.

Poprzednia wersja źródłowa: 0.9.0, e8af13af51a8d71419b46f9fc0ee88f10dccf3f1. Cofnięcie wymaga aktualizacji źródła instalacji i potwierdzenia wersji w nowym zadaniu; dokumenty spraw pozostają osobną historią.
