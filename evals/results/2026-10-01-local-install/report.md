# Domknięcie i instalacja lokalna 0.7.0 — 01.10.2026

B3 (#8) scalono przez Git do B2, następnie B2 (#7) do main. GitHub potwierdził oba PR-y jako merged. Zachowano pełną historię, bez squash i force-push. Powód użycia Git: PR-y były draftami, a dostępny connector nie udostępnia zmiany tego statusu; próba merge API została odrzucona. Nie zmieniano reguł ochrony gałęzi.

## Wykonane sprawdzenia

- Wszystkie 15 testów pakowania przeszło w lokalnym Linux, włącznie z testami symlinków.
- Check: 53 pliki; build ZIP 0.7.0 przeszedł.
- Zarejestrowano lokalny marketplace personal, wcześniej nieobecny; zainstalowano legal-ai-pl@personal 0.7.0. CLI potwierdza installed=true i enabled=true.
- Wszystkie 53 pliki zainstalowanego cache są bajtowo zgodne ze źródłem pluginu.
- Nowy proces lokalnego Codex app-server, przez initialize i skills/list z forceReload, wykrył siedem skilli jako enabled=true, bez błędów pluginu. Znormalizowany wynik: [skills-discovery.json](skills-discovery.json); ścieżki prywatne zastąpiono odpowiednikami w repo.
- Obie kontrole GitHub CI na źródłowym head B3 ef58ed5 miały status success przed scaleniem. Status CI nowego main należy sprawdzić osobno.

## Granice wyniku

Discovery nie dowodzi automatycznego wyboru skilla przez model, poprawności odpowiedzi prawnej ani odświeżenia już otwartej rozmowy w aplikacji. Nie wykonano nowych prób zachowania, realnego researchu sprawy, odbioru zawodowego, testu izolacji spraw ani wdrożenia zespołowego. Raporty B2/B3 zachowują wcześniejsze wyniki porównania z baseline i brak wykazanej przewagi.

## Następne zadania

Nowe próby na niewykorzystanych przypadkach i porównanie ze skillem/bez skilla, sprawdzenie routingu w nowej rozmowie, odbiór adwokata i UA/RU. Następny zakres domenowy opisuje [specyfikacja C1](../../../docs/c1-specification.md).

ZIP SHA-256: `cb31d5623af26d367f8732dee515ce7e9978348a85432f09767c21728c9b4f94`.
