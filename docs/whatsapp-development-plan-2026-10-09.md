# LegalAI: plan rozwoju do obsługi wiadomości klientów
Data: 9 października 2026
Status: specyfikacja i plan do wdrożenia, bez zmian w pluginie.
Punkt wyjścia: legal-ai-pl 0.8.0, dziewięć skilli, main 848b451bb421235e6a4e09868b8fcee087984dc3.

## 1. Cel i zakres
LegalAI jest pluginem przygotowującym ChatGPT do pracy kancelarii. ChatGPT pozostaje asystentem; plan nie zakłada budowania oddzielnej aplikacji ani bota. Codzienny przebieg: pracownik wkleja wiadomość z WhatsAppa, dodaje potrzebny fragment rozmowy lub dokument, otrzymuje projekt odpowiedzi i wysyła go ręcznie po sprawdzeniu.

Główni użytkownicy to adwokat oraz pracownicy kancelarii bez wykształcenia prawniczego. Klienci często są obywatelami Ukrainy komunikującymi się po rosyjsku; pojawiają się również wiadomości po polsku i ukraińsku. Język wyniku ma wynikać ze zlecenia i rozmowy, niezależnie od obywatelstwa.

Cele:
- krótkie, rzeczowe i naturalne wiadomości;
- ograniczenie dopisywania faktów, błędnych założeń i niezweryfikowanych skutków prawnych;
- wierne przenoszenie znaczenia między językami;
- ograniczenie liczby pytań i poprawek pracownika;
- rozpoznanie pilności i nowych decyzji prawnych wymagających adwokata;
- ciągłość pracy nad konkretną sprawą.

Miarą powodzenia jest użyteczność odpowiedzi oraz czas potrzebny na jej poprawienie. Samo brzmienie profesjonalne lub zaliczenie testów pakowania nie dowodzi jakości.

## 2. Architektura skilli
Pierwszą zmianą jest rozwój istniejących skilli, bez tworzenia oddzielnego skilla wyłącznie do tonu.

| Element | Rola po zmianie |
| --- | --- |
| pl-client-explanation | Główny skill odpowiadania klientom: WhatsApp, objaśnienie dokumentu, prośba o materiały, komunikacja organizacyjna i przekazanie ustaleń kancelarii. |
| pl-case-file-analysis | Rozpoznanie niejasnej relacji, dokumentów i sprzeczności; analiza wewnętrzna po polsku na potrzeby pracownika lub adwokata. |
| Skille specjalistyczne | Analiza prawna potrzebna do odpowiedzi, tylko gdy pytanie wymaga ich metody; nie pełna strategia do każdej wiadomości. |
| pl-legal-document-review | Kontrola istniejącego pisma na wyraźne zlecenie. Nie przejmuje prostej korespondencji. |
| pl-criminal-appeal i pozostałe skille pisemne | Przygotowanie żądanego pisma lub argumentacji w odrębnym zadaniu. |

Styl WhatsAppa umieścić w lokalnej referencji pl-client-explanation. Nie dodawać go do wszystkich skilli: apelacja, wewnętrzna analiza i wiadomość klientowi mają inne potrzeby. Wspólne reguły źródeł i faktów utrzymywać w source-policy i synchronizować istniejącym mechanizmem.

Nie zakładać obowiązkowego odczytu wszystkich dziewięciu skilli. Zachować samodzielność folderów: istotne zasady komunikacji i weryfikacji muszą być dostępne w skillu, który ich potrzebuje. Nazwa innego skilla nie zastępuje odczytu jego metody.

Osobny skill pierwszego kontaktu rozważyć dopiero wtedy, gdy próby wykażą, że poszerzony pl-client-explanation myli rozpoznanie nowej sprawy z objaśnianiem istniejących ustaleń.

## 3. Specyfikacja komunikacji na WhatsApp
Domyślna odpowiedź ma być gotowym tekstem do wklejenia, bez wprowadzenia „Oto propozycja odpowiedzi”. Długość dopasować do treści:
- potwierdzenie lub organizacja: zwykle 1–3 zdania;
- typowa odpowiedź: zwykle 2–5 zdań, orientacyjnie 35–90 słów;
- kilka istotnych wątków: krótkie akapity lub najwyżej kilka punktów;
- dłuższe objaśnienie: gdy użytkownik go zamówi lub skrót zniekształci ważny sens.

To cele redakcyjne, nie sztywny limit. Nie usuwać informacji o pilności, niepewności, wykonaniu decyzji lub koniecznej czynności tylko dla zachowania liczby słów. Długość oryginału nie przesądza długości odpowiedzi: długa relacja klienta może wymagać jednej krótkiej prośby o dokument.

Ton:
- rzeczowy, spokojny, naturalny, uprzejmy;
- zwykłe słownictwo i konkretne czasowniki;
- bez kancelaryjnych formuł typu „niniejszym informujemy”, „w związku z powyższym”;
- bez żartów, emotikonów, przesadnej empatii, obietnic sukcesu i presji sprzedażowej;
- bez powtarzania całej historii klienta;
- bez nagłówków, tabel, rozbudowanego Markdown i cytowania przepisów w zwykłej wiadomości;
- bez powitania i podpisu w każdej kolejnej wypowiedzi;
- bez pauzy em dash;
- nie narzucać „ja” lub „my”: dopasować do rzeczywistego nadawcy i ustalonego stylu kancelarii;
- nie podpisywać wypowiedzi tytułem adwokata, jeżeli autorem jest pracownik;
- nie dodawać tłumaczenia polskiego do rosyjskiej odpowiedzi, chyba że zostało zamówione.

Domyślna konstrukcja: odpowiedź na pytanie, jedno potrzebne objaśnienie, następny krok. Nie stosować wszystkich trzech elementów mechanicznie. Pytać zwykle o 1–3 informacje, które faktycznie zmieniają dalsze działanie.

### Przykłady stylu
Przykłady są syntetyczne; nie stanowią zatwierdzonych odpowiedzi do konkretnej sprawy.

Prośba o pismo, RU:
„Пришлите, пожалуйста, все страницы полученного письма, включая страницу с разъяснениями. Уточните, когда и как вы его получили.”

Brak załącznika, PL:
„Nie widzę załącznika. Prześlij proszę zdjęcie dokumentu jeszcze raz, tak żeby było widać całą stronę.”

Potwierdzenie w trwającej rozmowie, RU, wyłącznie gdy pliki rzeczywiście są dostępne:
„Документы получили, спасибо. Если потребуется что-то ещё, сообщим.”

Preferować konkretną prośbę zamiast „W celu dokonania kompleksowej analizy przedstawionego stanu faktycznego uprzejmie prosimy o dostarczenie pełnej dokumentacji”. Przykłady nie są szablonami do wklejania niezależnie od kontekstu.

## 4. Rozpoznanie wiadomości i podstawa odpowiedzi
Przed redagowaniem ustalić z dostępnego kontekstu:
1. Czy to nowa sprawa, kontynuacja czy wyłącznie kwestia organizacyjna?
2. Czego klient chce teraz: wyjaśnienia, terminu konsultacji, informacji o stanie sprawy czy decyzji prawnej?
3. Co pochodzi z relacji, co z dokumentu, co jest zatwierdzonym ustaleniem adwokata?
4. Czy wiadomość ujawnia pilność, nowy dokument, zmianę faktów lub możliwy termin?
5. Jakie minimum trzeba ustalić przed odpowiedzią?

Pierwszeństwo mają materiały i decyzje z bieżącej sprawy, aktualne zasady organizacyjne kancelarii oraz sprawdzone źródła właściwe dla zagadnienia. To różne rodzaje podstaw: zatwierdzona notatka nie zastępuje normy prawnej, a dokument klienta nie dowodzi automatycznie prawdziwości opisanego zdarzenia.

Nie wnioskować, że „adwokat sprawdził” tylko dlatego, że wcześniejszy tekst AI znalazł się w rozmowie. Decyzja zatwierdzona musi mieć jawne pochodzenie. Widoczny konflikt notatki z dokumentem zgłosić poza wiadomością klientowi; przygotować niezależną część odpowiedzi.

## 5. Ograniczanie halucynacji
Zastosować następujące kontrole do istotnych zdań:
- Fakty: każde twierdzenie o sprawie ma oparcie w wiadomości, dokumencie albo jawnej decyzji kancelarii.
- Status: nie zamieniać podejrzenia, planu lub projektu w zdarzenie dokonane.
- Prawo: nowy rozstrzygający wniosek wymaga właściwego przepisu, jego wersji i zastosowania do znanych faktów.
- Terminy: potrzebna jest norma, czynność, zdarzenie początkowe i dowód tego zdarzenia. Gdy ich brakuje, nie tworzyć pewnej daty.
- Źródła: odczytać odpowiedni tekst, a nie tylko wynik wyszukiwania. Sprawdzić kontekst cytatu oraz wyjątki istotne dla pytania.
- Język: zachować negacje, wykonawcę czynności, role i stopień pewności.
- Działania: nie sugerować, że wiadomość wysłano, pismo złożono lub kancelaria przyjęła sprawę, jeśli brak potwierdzenia.

Podczas researchu nie wyszukiwać nazwisk, numerów dokumentów i zbędnych szczegółów klienta. Korzystać z opisu problemu prawnego.

Nie wykonywać pełnego researchu przy potwierdzeniu dokumentów lub uzgadnianiu konsultacji. Jeżeli prośba wymaga aktualnej rekomendacji prawnej, wykonać potrzebną weryfikację dostępnymi narzędziami. Przy braku źródła ograniczyć zależny wniosek, ale kontynuować użyteczną pracę.

Sam przepis, cytat, link ani wysoka deklarowana pewność modelu nie stanowią zatwierdzenia porady. Skill ogranicza niektóre błędy, lecz nie egzekwuje technicznie poprawności ani zakresu uprawnień.

## 6. Tryb pracownika i tryb adwokata
Przyjąć podział jako wewnętrzną politykę kancelarii zatwierdzaną przez adwokata, a nie uniwersalną kwalifikację prawną wszystkich czynności personelu.

| Sytuacja | Tryb pracownika |
| --- | --- |
| Organizacja, potwierdzenie, zebranie dokumentów | Przygotować odpowiedź na podstawie aktualnych ustaleń. |
| Przekazanie decyzji adwokata w tej samej sprawie | Wiernie objaśnić, bez dopisywania nowej strategii. |
| Ogólne objaśnienie procedury | Korzystać z zatwierdzonego, aktualnego materiału w jego warunkach zastosowania. |
| Niejasna relacja lub brak kluczowego dokumentu | Przygotować krótką odpowiedź i potrzebne pytania; wskazać brak wewnętrznie, jeśli istotny. |
| Nowa indywidualna decyzja: zaskarżenie, wyjazd, zachowanie na przesłuchaniu, termin, ryzyko wykonania | Opracować propozycję dla adwokata; nie przedstawiać jej jako zatwierdzonej rady kancelarii. |
| Zatrzymanie, planowany powrót, czynność w bliskim terminie | Wskazać pilność na początku, zebrać minimum i przygotować przekazanie; nie uzależniać reakcji od pełnych akt lub płatności. |

Pracownik nie powinien być jedyną osobą sprawdzającą nową ocenę prawną wygenerowaną przez AI. Samo ręczne kliknięcie „wyślij” nie jest merytorycznym odbiorem. Jeżeli użytkownik poprosi o sam tekst, ważny problem wymagający adwokata nadal trzeba krótko zaznaczyć poza projektem.

W trybie adwokata model może przygotować pełniejszą roboczą ocenę z materiałami, podstawami i kontrargumentami. Odbiór należy do adwokata. Nie wymagać ponownego zatwierdzania każdej organizacyjnej wiadomości.

## 7. Języki PL/RU/UA i odczyt dokumentów
- Odpowiedzieć w języku wskazanym przez użytkownika; w braku wskazania korzystać z języka rozmowy klienta.
- Wewnętrzne wyjaśnienie dla polskojęzycznego pracownika podawać po polsku, jeśli jest potrzebne.
- Rosyjski nie oznacza obywatelstwa rosyjskiego; obywatelstwo UA nie narzuca języka ukraińskiego.
- Zachować pisownię nazw z dokumentu. Nie utożsamiać osób przez podobną transliterację.
- Wyrazy potoczne traktować początkowo jako określenia klienta: „deportacja”, „areszt”, „oszustwo”.
- Odróżniać role: świadek, podejrzany, oskarżony, skazany, pokrzywdzony.
- Rozróżniać: złożenie/uwzględnienie wniosku, wezwanie/decyzję, wydanie/doręczenie, możliwość/obowiązek/zakaz.
- Przy nieczytelnym skanie sprawdzić obraz istotnej daty, negacji lub nazwiska. Poprosić o lepsze zdjęcie tylko potrzebnej strony.
- Nie tłumaczyć całego dokumentu, gdy pytanie dotyczy jednego skutku.

Stworzyć niewielki glosariusz pojęć z kontekstem i przykładami; nie słownik mechanicznych zamienników. Kontrolę przykładów RU/UA powinna wykonać osoba kompetentna językowo i prawnie.

## 8. Format wyniku bez nadmiernego raportowania
Domyślnie zwracać sam projekt wiadomości.
Gdy występuje istotny brak, nowa decyzja prawna albo pilność, dodać krótką notatkę dla kancelarii, wyraźnie oddzieloną od tekstu do skopiowania. Zwykle wystarczy 1–3 punkty zawierające konkretny problem i potrzebny krok.

Nie dopisywać do każdej odpowiedzi czterech sekcji, tabeli dowodowej, procentu pewności ani ogólnego „wymaga konsultacji z adwokatem”. Notatka powinna wyjaśniać konkretną zależność, a nie powtarzać disclaimer.

Na żądanie pracownika dodać krótkie wyjaśnienie po polsku. Na żądanie adwokata podać pełną podstawę analizy. Zachować możliwość szczegółowej odpowiedzi, gdy użytkownik wyraźnie jej potrzebuje.

## 9. Zasady kancelarii i ciągłość sprawy
Dodać lekki, oddzielny dokument konfiguracyjny do użytku w danym środowisku:
- aktualny cennik z zakresem usługi i datą zatwierdzenia;
- języki i kanały konsultacji;
- zasady płatności i materiałów przed spotkaniem;
- sposób rezerwacji i potwierdzania;
- reguły nadawcy, podpisu i komunikacji o czasie odpowiedzi;
- zakres usług oraz sytuacje wymagające decyzji adwokata.

Nie wpisywać historycznych stawek, terminów, kont bankowych lub dostępności z pamięci rozmów jako obecnego faktu. Gdy brak aktualnej informacji, użyć oznaczonego miejsca do uzupełnienia lub krótkiego pytania. Nigdy nie wymyślać wolnego terminu.

W późniejszym etapie wprowadzić kartę sprawy:
- identyfikator sprawy i minimalne dane;
- źródła, wersje i rzeczywiście odczytany zakres;
- ustalone fakty oraz relacje nieweryfikowane;
- zatwierdzone decyzje adwokata;
- otwarte pytania i ważne zdarzenia;
- projekty oraz jawnie potwierdzone wysłane wiadomości.

Karta jest dokumentem roboczym, nie gwarancją trwałej pamięci ChatGPT. W nowej rozmowie udostępnić aktualną kartę i potrzebne materiały. Dane spraw przechowywać osobno od publicznego repozytorium. Skill nie gwarantuje technicznej izolacji spraw ani automatycznej synchronizacji. Nowy fakt może wymagać ponownej oceny wcześniejszej decyzji.

## 10. Plan wdrożenia
| Etap | Konkretny wynik | Warunek ukończenia |
| --- | --- | --- |
| A. Styl WhatsApp | Rozszerzony pl-client-explanation, lokalna referencja stylu i przykłady PL/RU. | Krótkie, naturalne projekty bez pomijania ważnego sensu; proste pytania nie uruchamiają dużego raportu. |
| B. Pierwszy kontakt | Poszerzony opis uruchamiania i metoda pl-case-file-analysis; jawne granice trybu pracownika. | Relacja nie staje się faktem; właściwe minimum pytań; rozpoznanie pilności. |
| C. Kontrola znaczenia i źródeł | Glosariusz, poprawki meaning-check, reguły nowych twierdzeń prawnych i rozdzielenia notatki. | Zachowane negacje, role i modalność; źródła faktycznie odczytane w zadaniach prawnych. |
| D. Zasady kancelarii | Aktualny, zatwierdzony dokument organizacyjny, oddzielony od metody ogólnej. | Brak dopisywania cen, dostępności i przyjęcia sprawy. |
| E. Ocena porównawcza | Odpowiedzi z trzech wariantów, oceny adwokata i języka, czas poprawek. | Jawnie oceniona korzyść i brak nierozwiązanych błędów krytycznych w przyjętym zestawie. |
| F. Ciągłość | Format karty sprawy i sposób jej aktualizacji. | Zmiana faktu lub dokumentu nie utrwala starej odpowiedzi; zakres pamięci jest jawny. |
| G. Wydanie | Pakiet, check, istniejące testy techniczne, build i zweryfikowana instalacja. | Zgodne referencje i wersje, poprawne wykrywanie oraz osobno sprawdzony wybór skilli. |

Proponowana pierwsza wersja: 0.8.1, jeżeli zmiany pozostają poprawkami istniejących skilli. Przy dodaniu nowego skilla lub większym rozszerzeniu zakresu rozważyć 0.9.0. Numer wersji ustalić według finalnej zmiany; tabela jest planem, nie deklaracją wykonania.

Najpierw etapy A–D i ich ocena. Kartę sprawy rozwijać po sprawdzeniu podstawowej korespondencji. Rozszerzenia kolejnych dziedzin prawnych odsunąć, jeżeli nie wynikają z najczęstszych kontaktów kancelarii.

## 11. Ocena jakości
Przygotować 24 scenariusze:
- 6 organizacyjnych i potwierdzających;
- 6 rozpoznających niejasny opis, dokument lub sprzeczność;
- 6 objaśniających zatwierdzony plan albo pojęcie;
- 6 pilnych lub wymagających nowej indywidualnej oceny.

Połowę scenariuszy przygotować po rosyjsku, osiem po polsku, cztery po ukraińsku lub z mieszanym materiałem. To początkowa propozycja; proporcje dopasować do rzeczywistego ruchu.

Uwzględnić: nieczytelną datę, „wczoraj” bez daty wiadomości, negację RU, brak załącznika, potoczną nazwę procedury, nowy dokument sprzeczny z notatką, żądanie gwarancji, pytanie o termin, przesłuchanie jutro, kilka spraw jednej osoby i instrukcję do AI umieszczoną w materiale klienta. Dodać przypadki, gdzie właściwa odpowiedź ma tylko jedno zdanie.

Porównać:
1. ten sam model bez skilli prawnych;
2. ten sam model z krótką instrukcją stylu;
3. ten sam model z poprawionym LegalAI.

Zapewnić te same dane, narzędzia i polecenie. Każde zadanie i wariant wykonywać w osobnym kontekście; zachować wersję modelu i ustawienia, jeśli dostępne. Nie przekazywać rubryki ani oczekiwanej odpowiedzi wykonawcy. Rozdzielić zestaw rozwojowy od nowych przypadków odbiorczych. Nie przedstawiać samooceny autora jako niezależnej oceny adwokata.

Mierzyć:
- wierność faktom i brak dopisków;
- zachowanie znaczenia w języku klienta;
- trafność następnego kroku i rozpoznania pilności;
- zasadność pytań i uwag wewnętrznych;
- naturalność i długość;
- poprawność podstaw nowych wniosków prawnych;
- czas poprawek oraz liczbę odpowiedzi gotowych po kontroli;
- niepotrzebny research, koszt i opóźnienie, jeśli da się je zmierzyć.

Błędy krytyczne: pewny termin bez podstawy, nieuzasadnione zapewnienie o legalności wyjazdu lub wstrzymaniu wykonania, zmiana negacji/roli, wymyślony stan sprawy, deklaracja zatwierdzenia bez dowodu albo pominięcie konkretnej pilności. Po błędzie wprowadzić wąską poprawkę i sprawdzić nowy przypadek o podobnym mechanizmie. Brak błędów w zestawie nie gwarantuje ich braku w przyszłości.

## 12. Konkretne zmiany w repozytorium
Planowane pliki:
- plugins/legal-ai-pl/skills/pl-client-explanation/SKILL.md: rozszerzyć uruchamianie na krótkie odpowiedzi i komunikację organizacyjną; dodać domyślny format i tryb pracownika.
- plugins/legal-ai-pl/skills/pl-client-explanation/references/whatsapp-style.md: styl, długość, struktura i przykłady.
- plugins/legal-ai-pl/skills/pl-client-explanation/references/meaning-check.md: rozróżnienia językowe, kontrola pewności i zatwierdzonego planu.
- plugins/legal-ai-pl/skills/pl-client-explanation/references/client-contact-method.md: wybór podstawy, minimum pytań i przekazanie nowej decyzji adwokatowi.
- plugins/legal-ai-pl/skills/pl-case-file-analysis/SKILL.md oraz references/intake-and-research.md: rozpoznanie dla pracownika i proporcjonalność.
- agents/openai.yaml obu skilli: nazwy i przykładowe polecenia zgodne ze zmienionym zakresem.
- config/skill-package.json: jawnie zadeklarować nowe referencje.
- evals/: przypadki komunikacji, rubryka, oczekiwania routingu i raporty.
- dokumentacja wydania oraz metadane wszystkich skilli: zgodność wersji według istniejącego walidatora.

Przykłady do repo powinny być syntetyczne. Rzeczywiste rozmowy, nawet po usunięciu nazwiska, mogą zawierać identyfikujące szczegóły. Wykorzystywać je tylko w odpowiednim prywatnym procesie i po ograniczeniu danych. Regułę przenosić do skilla na poziomie ogólnego mechanizmu błędu, bez treści sprawy.

Nie dodawać testów, które jedynie sprawdzają obecność słowa w instrukcji. Zachować istniejące testy pakowania i dodać tylko uzasadnione kontrole struktury. Zachowanie oceniać na odpowiedziach modelu.

## 13. Polecenie dla następnego wykonawcy
Pracuj w repozytorium Pawel-Rogoza/chatgpt-skills na aktualnej wersji main. Wdróż etapy A–D tego planu jako rozwój ChatGPT przez plugin LegalAI. Zacznij od istniejących pl-client-explanation i pl-case-file-analysis. Nie buduj aplikacji ani integracji WhatsApp. Zachowaj dziewięć skilli, ich samodzielne referencje i istniejący mechanizm pakowania.

Opracuj krótką komunikację WhatsApp PL/RU/UA, tryb pracownika kancelarii, rozdzielenie materiału klienta od ustaleń oraz konkretne kontrole nowych twierdzeń prawnych. Domyślnie oddawaj sam projekt wiadomości; notatkę dodawaj przy realnej zależności. Nie usuwaj swobody adwokata ani możliwości głębszej analizy na zlecenie.

Przygotuj syntetyczne przypadki i rubrykę przed oceną odpowiedzi. Zachowaj wyniki z rozróżnieniem prób technicznych, modelowych i zawodowego odbioru. Nie twierdź, że porównanie wykonano lub że wykazano przewagę, jeśli brak zapisanych odpowiedzi i ocen. Uruchom istniejące wymagane check, testy i build po zmianach. Udokumentuj zakres i ograniczenia; nie instaluj ani nie publikuj pod innym zakresem niż wynika ze zlecenia.

## 14. Źródła i ograniczenia
Repozytorium i metoda:
- https://github.com/Pawel-Rogoza/chatgpt-skills
- https://github.com/Pawel-Rogoza/chatgpt-skills/blob/848b451bb421235e6a4e09868b8fcee087984dc3/plugins/legal-ai-pl/skills/pl-client-explanation/SKILL.md
- https://github.com/Pawel-Rogoza/chatgpt-skills/blob/848b451bb421235e6a4e09868b8fcee087984dc3/docs/next-steps-0.8.0.md
- https://github.com/Pawel-Rogoza/chatgpt-skills/blob/848b451bb421235e6a4e09868b8fcee087984dc3/evals/results/2026-10-01-b2/report.md
- https://github.com/Pawel-Rogoza/chatgpt-skills/blob/848b451bb421235e6a4e09868b8fcee087984dc3/evals/results/2026-10-01-b3/report.md

Kontekst zawodowy, odczytany w tej rozmowie:
- Kodeks Etyki Adwokackiej, tekst jednolity z 23.06.2026, §19 i §23e:
https://www.adwokatura.pl/admin/wgrane_pliki/file-zal-do-uchwaly-prezydium-nra-nr-1742026kodeksetykiadwokackiejtekst-jednolity-44572.pdf

Plan stanowi propozycję organizacji pracy i rozwoju instrukcji. Nie jest pełnym audytem zasad przetwarzania danych ani prawnym zatwierdzeniem konkretnej usługi lub dostawcy. Ochronę tajemnicy i odpowiednie środowisko należy ustalić dla faktycznego sposobu korzystania. Instrukcje nie zastąpią technicznej ochrony danych ani oceny adwokata.

Nie wdrożono tu zmian, nie wykonano nowych prób modelowych i nie potwierdzono instalacji. Istniejące raporty repo nie wykazują ogólnej przewagi skilli; dlatego porównanie jakości korespondencji jest częścią planu.
