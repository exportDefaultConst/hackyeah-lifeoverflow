# 🎯 Life Simulation - ZUS Pension Planning Game

## ✅ Progress Tracker

### Backend
- [x] ✅ 🏗️ Project Structure & Configuration
- [x] ✅ 🗄️ Database Models (SQLAlchemy)
- [x] ✅ 🔐 Authentication (JWT)
- [x] ✅ 🎮 Game Routes & Logic
- [x] ✅ 🤖 AI Event Generator (Claude/LangChain)
- [x] ✅ 👴 Wujek Dobra Rada Advisor
- [x] ✅ 💰 Pension Calculator
- [x] ✅ ⚙️ Utility Functions

### Frontend
- [x] ✅ ⚛️ React Setup & Structure
- [x] ✅ 🎨 Tailwind CSS Configuration
- [x] ✅ 🔑 Login/Registration
- [x] ✅ 🎮 Game Dashboard
- [x] ✅ 👤 Character Avatar System
- [x] ✅ 📊 Stats Panel
- [x] ✅ 🎯 Event Modal
- [x] ✅ 💡 Wujek Advice Component
- [x] ✅ 📈 Results/Pension Screen

### DevOps
- [x] ✅ 🐳 Backend Dockerfile
- [x] ✅ 🐳 Frontend Dockerfile
- [x] ✅ 🐳 Docker Compose

### UI/UX Redesign (v2.0)
- [x] ✅ 🎨 Gaming UI - ciemne tło i gradienty
- [x] ✅ 🖼️ Awatar - obrazki PNG zamiast emoji
- [x] ✅ 📊 Zredukowane statystyki - średnie w grze
- [x] ✅ 📈 Wszystkie statystyki w Results
- [x] ✅ ⚖️ Porady prawne ZUS
- [x] ✅ 🎯 Nowoczesne przyciski i animacje
- [x] ✅ 🎮 Event modal redesign
- [x] ✅ 🔐 Login screen redesign

---

## 🎉 STATUS: UKOŃCZONE! 🎉

Aplikacja została w pełni zaimplementowana zgodnie z wymaganiami:
- ✅ Backend w Flask z SQLAlchemy
- ✅ Frontend w React z Tailwind CSS
- ✅ Integracja Claude AI przez LangChain (tylko Anthropic API)
- ✅ Polski interfejs użytkownika
- ✅ Czyste, komentowane kody z obsługą błędów
- ✅ Minimalistyczne Dockerfiles i docker-compose
- ✅ Gotowe do uruchomienia jedną komendą!

### 🚀 Uruchomienie:
```bash
docker-compose up --build
```

Następnie otwórz http://localhost w przeglądarce!

---

# Cel gry jako narzędzia edukacyjnego
Gra jest projektowana jako narzędzie edukacyjne służące do zwiększania świadomości na temat
planowania życia oraz finansów osobistych. Celem nadrzędnym jest umożliwienie graczom
doświadczenia symulacji całego życia dorosłego człowieka – od młodości, przez karierę zawodową i
życie rodzinne, aż po emeryturę – w bezpiecznym, wirtualnym środowisku. Poprzez interaktywną
rozgrywkę gra ma uczyć podejmowania długoterminowych decyzji oraz pokazywać konsekwencje
różnych wyborów życiowych (np. poziom wykształcenia, styl życia, oszczędzanie na emeryturę) w
różnych obszarach.
Istotnym aspektem edukacyjnym jest zwrócenie uwagi na bezpieczeństwo finansowe na starość. Gra
ma więc służyć jako symulator konsekwencji finansowych, uświadamiając graczom znaczenie
podejmowania zatrudnienia w oparciu o określone formy pracy (np. pełne ubezpieczenie na podstawie
umowy o pracę), dodatkowego oszczędzania i inwestowania długoterminowego na „jesień życia”, a
także decydowania o momencie dekumulacji zgromadzonego kapitału. Dzięki rozgrywce użytkownicy
mogą nauczyć się, jak decyzje podejmowane w młodości (dotyczące edukacji, kariery, nawyków
zdrowotnych czy oszczędzania) wpływają na jakość życia w późniejszych latach.
Podsumowując, celem gry jako narzędzia jest kształtowanie postaw proaktywnych: promowanie
zdrowego trybu życia, równowagi między pracą a życiem osobistym oraz odpowiedzialnego zarządzania
finansami. Ma to być atrakcyjna forma nauki przez zabawę – rodzaj „serious game”, który angażuje
emocjonalnie, a jednocześnie przekazuje praktyczną wiedzę i skłania do refleksji nad własnymi
wyborami.
Cel rozgrywki i scenariusze w grze
W samej grze gracz wciela się w postać, którą prowadzi przez kolejne etapy życia, dążąc do realizacji
określonych celów życiowych. Celem rozgrywki jest zatem takie pokierowanie życiem wirtualnej
postaci, aby osiągnęła ona możliwie wysoki poziom dobrostanu – finansowego, zdrowotnego i
osobistego – szczególnie w wieku emerytalnym. Ostatecznym miernikiem „sukcesu” może być, na
przykład, komfort życia na emeryturze (wysokość zgromadzonych oszczędności, wysokość emerytury,
stan zdrowia i relacje rodzinne w starszym wieku) oraz ogólna satysfakcja życiowa postaci.
Gra będzie oferowała różne tryby i scenariusze rozgrywki, aby zwiększyć regrywalność oraz dostosować
doświadczenie do różnych potrzeb edukacyjnych:
• Tryb swobodny (sandbox) – Gracz przechodzi przez pełen cykl życia postaci bez z góry
narzuconych zadań, samodzielnie wyznaczając sobie cele (np. zgromadzenie określonej kwoty
oszczędności, osiągnięcie określonego szczebla kariery, założenie rodziny itp.). Ten tryb pozwala
eksperymentować z różnymi ścieżkami życiowymi i obserwować ich konsekwencje.
• Scenariusze wyzwań – Zdefiniowane zostaną odrębne scenariusze z konkretnymi celami do
osiągnięcia lub warunkami początkowymi. Przykładowe scenariusze:
o „Bogata emerytura”: startujemy jako młoda osoba, a celem jest przejście na emeryturę
w wieku np. 65 lat z określoną kwotą oszczędności i inwestycji, zapewniającą wysoki
standard życia. Gracz musi strategicznie zarządzać karierą, wydatkami i oszczędzaniem,
aby to osiągnąć.

2

o „Pod górkę”: scenariusz, w którym gracz musi poradzić sobie z serią nieprzewidzianych
trudności (np. recesja i utrata pracy w średnim wieku, poważna choroba w rodzinie,
itp.) i mimo to utrzymać postać na powierzchni – celem jest przetrwanie do emerytury
z pozytywnym wynikiem (np. bez długów, z podstawowym zabezpieczeniem
finansowym).
o „Równowaga życiowa”: celem jest utrzymanie wysokiego poziomu szczęścia lub
satysfakcji życiowej postaci do końca gry. Gracz musi balansować między pracą a
życiem osobistym – np. nie można zaniedbywać zdrowia i rodziny kosztem kariery. Ten
scenariusz punktuje zrównoważony rozwój wszystkich obszarów (zdrowie, relacje,
pasje) oprócz finansów.

• Tryb edukacyjny/story mode – rozgrywka prowadzona przez narrację, gdzie gracz otrzymuje
zadania i pytania kontrolne po drodze. Może być wykorzystywana na warsztatach lub lekcjach
– np. po każdym etapie życia pojawia się podsumowanie z omówieniem, co poszło dobrze lub
źle i jakie byłyby alternatywy. Ten tryb kładzie nacisk na refleksję i omawianie decyzji.
W każdym scenariuszu gra stawia przed graczem wybory dotyczące ścieżki edukacyjnej, ścieżki kariery,
stylu życia i zarządzania finansami. Zadania gracza polegają na podejmowaniu tych decyzji i zarządzaniu
zasobami postaci (czas, pieniądze, punkty zdrowia itp.) tak, by zrealizować cel scenariusza. Różne
scenariusze mogą mieć też różne poziomy trudności – np. start z mniejszymi zasobami, wyższe koszty
życia, częstsze występowanie negatywnych zdarzeń losowych – co pozwoli dostosować grę do odbiorcy
(uczeń, student, osoba dorosła planująca emeryturę itp.) oraz czyni rozgrywkę ciekawszą.
Wizualizacja i interfejs gry
Interfejs gry będzie zaprojektowany tak, aby prezentować graczowi czytelnie wszystkie istotne
informacje o stanie postaci i postępach życia, jednocześnie dbając o atrakcyjność wizualną. Poniżej
przedstawiono kluczowe elementy wizualizacji i pomysły graficzne:
• Pulpit sterowania (dashboard): Główna część interfejsu to pulpit z danymi postaci. Zawiera on
czytelne wskaźniki i wykresy dotyczące najważniejszych zmiennych, takich jak aktualny wiek
postaci, stan zdrowia (np. pasek zdrowia lub procent), poziom zadowolenia/szczęścia, saldo
oszczędności, wysokość zarobków, itp. Pulpit sterowania może przypominać kokpit menedżera
życia – z ikonami reprezentującymi różne obszary (np. praca, zdrowie, rodzina, edukacja,
finanse). Dzięki temu gracz na pierwszy rzut oka widzi kondycję swojej postaci w każdym
aspekcie. Możliwe jest dodanie wykresów liniowych pokazujących historię wybranych
parametrów (np. zmiany stanu konta oszczędnościowego w czasie czy zmianę poziomu zdrowia
wraz z wiekiem). Całość ma być intuicyjna – także dla osób niezaznajomionych z grami, skoro
gra pełni funkcję edukacyjną.
• Oś czasu / postęp życia: U góry ekranu (bądź w innym dobrze widocznym miejscu)
zaplanowano oś czasu reprezentującą upływ lat życia bohatera. Będzie ona podzielona na
etapy odpowiadające fazom życia: Młodość, Wczesna dorosłość, Późna Dorosłość, Wczesna
starość, Późna starość (wraz z osiągnięciem wieku emerytalnego i dalej). Na osi czasu mogą być
zaznaczone kluczowe momenty (np. ukończenie szkoły, przekroczenie 30 lat, 50 lat, osiągnięcie
wieku emerytalnego 60/65 lat – ta wartość również może ulec zmianom jako losowy
komponent, np. decyzje rządu etc.). Bieżący wiek postaci może być oznaczony ruchomym
znacznikiem. Taki „progress bar życia” nie tylko informuje o aktualnym wieku, ale też buduje
zaangażowanie – gracz widzi, ile czasu w grze już minęło i ile jeszcze zostało, co mobilizuje do
myślenia perspektywicznego.

3

• Awatar gracza (postać): Centralnym elementem wizualnym będzie grafika postaci, którą
kieruje gracz. Awatar ma dynamicznie zmieniać się wraz z decyzjami i upływem czasu, co tworzy
emocjonalną więź z graczem:
o Wiek postaci: Postać początkowo jest przedstawiana jako młoda dorosła osoba (~18-
20 lat). W miarę upływu lat awatar starzeje się wizualnie – pojawiają się zmiany
wyglądu odpowiadające dojrzałości (np. inny ubiór, zmiana fryzury). Na starość postać
może być pokazana np. z siwymi włosami i delikatnie pochyloną sylwetką. Jeśli to
pasuje do stylistyki gry, można dodać atrybut typu laska u seniora, jednak ostrożnie i
bez stygmatyzacji – chodzi o subtelne podkreślenie wieku, ale pokazane pozytywnie
(np. uśmiechnięty senior cieszący się życiem, zamiast schorowanego stereotypu).
o Status rodzinny: Jeśli gracz zdecyduje się na założenie rodziny, obok głównego awatara
mogą pojawić się dodatkowe postacie reprezentujące partnera/partnerkę oraz dzieci.
Np. w momencie ślubu interfejs dodaje małą ikonę lub wręcz drugą postać stojącą
obok głównej. Gdy rodzi się dziecko, może pojawić się symboliczna kołyska, a potem
dziecko jako towarzysząca postać (która również rośnie w czasie). Taki wizualny
feedback wzmacnia emocjonalny aspekt decyzji rodzinnych.
o Wydarzenia losowe – wizualizacja: Ważne zdarzenia z życia postaci będą ilustrowane
na awatarze lub w jego otoczeniu. Np. gdy postać ulegnie wypadkowi, może zostać
tymczasowo pokazana z bandażem lub w gipsie, ewentualnie poruszająca się na wózku
inwalidzkim (o ile taki stan trwa dłużej w mechanice gry). Gdy choruje, może pojawić
się ikonka termometru lub chmurka dialogowa sygnalizująca złe samopoczucie. Po
takich zdarzeniach, gdy stan zdrowia wraca do normy, awatar wraca do zwykłego
wyglądu – te zmiany mają charakter tymczasowy, by podkreślić, że np. złamana noga
się wyleczyła. W przypadku najpoważniejszych zdarzeń, jak śmierć bliskiej osoby,
można rozważyć zmianę wyrazu twarzy postaci (smutna mina) lub tło w stonowanych
barwach na pewien czas, co sygnalizuje okres żałoby.
o Styl życia: Awatar może również odzwierciedlać pewne cechy stylu życia gracza.
Przykładowo, jeśli postać przykłada wagę do zdrowia (wysoki wskaźnik zdrowia dzięki
ćwiczeniom, zdrowej diecie), można to pokazać poprzez bardziej wysportowaną
sylwetkę lub strój sportowy. Z kolei osoba przemęczająca się w pracy i zaniedbująca
zdrowie może być zobrazowana jako zgarbiona, z ciemnymi „cieniami” pod oczami. Te
elementy graficzne będą subtelne, ale czytelne – tak aby gracz intuicyjnie widział, w
jakim stanie jest jego postać.

• Projekt graficzny i klimat: Gra będzie utrzymana w przyjaznym stylu graficznym – czytelnym i
atrakcyjnym wizualnie, ale zarazem poważnym na tyle, by oddać realia życia. Może to być
grafika 2D stylizowana na infografiki (ikony, proste postacie, wykresy) lub prosta grafika 3D z
widokiem postaci. Ważne, by kolory i symbole były dobrze przemyślane: np. zielony kolor dla
wysokiego zdrowia, czerwony dla zagrożeń/ryzyk, złoty dla finansów itp. Unikamy zbyt
dziecinnej stylistyki – odbiorcami są młodzież i dorośli – ale również zbyt przytłaczającego
realizmu. Ikonografia i zmieniający się awatar mają w przystępny sposób komunikować stany
gry.
Podsumowując, wizualizacja ma pełnić nie tylko funkcję estetyczną, ale głównie informacyjną i
motywacyjną. Gracz widząc „swoje życie” na ekranie (w formie zmieniającej się postaci i statystyk)
lepiej zrozumie związek przyczynowo-skutkowy decyzji. Dynamiczny awatar angażuje emocje, a

4

czytelny dashboard z danymi – rozum. Połączenie tych elementów zapewni zarówno immersję w
rozgrywkę, jak i spełnienie celów edukacyjnych.
Kluczowe obszary rozgrywki (aspekty życia w grze)
Gra obejmuje szeroki zakres aspektów życia, aby symulacja była kompletna i realistyczna. Poniżej
przedstawiono opisy głównych obszarów, które gracz będzie musiał zarządzać lub brać pod uwagę
podczas rozgrywki:
• Zdrowie: Reprezentuje kondycję fizyczną i psychiczną postaci. Zdrowie początkowo jest
wysokie u młodej osoby, ale z upływem lat naturalnie pogarsza się (mechanika starzenia się).
Gracz może wpływać na zdrowie poprzez wybory stylu życia: np. odpowiednia dieta, aktywność
fizyczna czy unikanie używek będą utrzymywać wysoki poziom zdrowia, podczas gdy
przepracowanie, stres, brak ruchu lub nałogi – obniżą je. Wysoki poziom zdrowia zwiększa
szanse dożycia sędziwego wieku i umożliwia dłuższą pracę zawodową, natomiast niskie zdrowie
może prowadzić do okresów niezdolności do pracy, konieczności kosztownego leczenia, a w
skrajnych przypadkach nawet do przedwczesnej śmierci postaci (co oznacza przedwczesne
zakończenie gry). Zdrowie wpływa także na jakość życia – w grze może to być odzwierciedlone
np. poprzez ograniczenie dostępnych akcji (ciężko chory gracz nie może podjąć dodatkowej
pracy ani aktywnie spędzać czasu). Część zdarzeń losowych z kategorii Ryzyka (choroby,
wypadki) będzie bezpośrednio wpływać na zdrowie.
• Praca i kariera: Ten obszar obejmuje ścieżkę zawodową postaci, wybór profesji oraz przebieg
kariery. Decyzje podjęte we wczesnej fazie (np. poziom wykształcenia, zdobyte kwalifikacje)
determinują, jakie oferty pracy będą dostępne. Gracz może zaczynać od prostych stanowisk
(np. prace dorywcze, staże), a następnie awansować lub zmieniać pracodawców w
poszukiwaniu lepszych zarobków i warunków. Każda praca ma określone parametry:
wynagrodzenie brutto/netto, typ umowy (np. umowa o pracę z pełnymi składkami, umowa
cywilnoprawna, B2B lub praca nierejestrowana – w grze odzwierciedlone tak jak w danych:
różne formy kontraktu w Ofertach pracy), wymagany poziom wykształcenia lub doświadczenia,
a także wpływ na inne aspekty (np. praca wymagająca dużej liczby nadgodzin może negatywnie
wpływać na zdrowie i życie rodzinne). Gracz musi balansować między zarobkami a kosztami
pracy: np. lepiej płatna praca może wymagać przeprowadzki (koszty), może być stresująca lub
niebezpieczna. Kariera wpływa wprost na finanse (dochody) oraz na status społeczny postaci.
Dobre wyniki w pracy mogą prowadzić do podwyżek i awansów, ale też mogą zwiększać ryzyko
przepracowania. W grze przewidziane są także zdarzenia związane z pracą: utrata pracy (np. w
wyniku redukcji etatów lub kryzysu), zmiana branży, a nawet przejście na emeryturę (w którym
to momencie dochód z pracy zanika, a zaczyna się korzystanie z emerytury).
• Edukacja: Wykształcenie postaci jest fundamentem dla jej dalszych możliwości życiowych.
Gracz na starcie wybiera poziom edukacji lub może zdecydować się na dalszą naukę kosztem
czasu i pieniędzy. Dostępne poziomy to np. wykształcenie podstawowe / średnie,
zawodowe/techniczne, wyższe (licencjat/inżynier), czy nawet podyplomowe. W grze będzie to
uproszczone do pewnych slotów edukacji – np. można poświęcić pierwszych kilka lat dorosłego
życia (18–24 lata) na studia, co opóźnia start kariery zawodowej, ale odblokowuje lepsze
stanowiska w przyszłości. Każdy poziom wykształcenia lub zdobyte kwalifikacje (np. kursy
specjalistyczne) odblokowują określone ścieżki kariery i stanowiska pracy (zgodnie z
Słownikiem kompetencji w grze, gdzie różne zawody wymagają określonego wykształcenia).
Edukacja wpływa na dochody w długim terminie – zwykle wyższe kwalifikacje dają wyższe
zarobki. Jednak w krótkim terminie edukacja to inwestycja: studia mogą wymagać opłat

5

(czesnego) i oznaczają brak dochodu przez czas nauki. Gracz musi więc zdecydować czy i kiedy
inwestować w edukację swojej postaci. Możliwe są też ścieżki uzupełniania wykształcenia w
dorosłym życiu (np. studia wieczorowe w trakcie pracy – kosztem czasu wolnego). Ten obszar
uczy planowania: pokazuje, że wysiłek włożony w naukę może bardzo się opłacić finansowo,
ale wymaga poświęceń i nie gwarantuje sukcesu, jeśli np. postać napotka inne trudności.
• Życie rodzinne: Dotyczy relacji osobistych postaci – zawierania związku
małżeńskiego/partnerskiego oraz posiadania dzieci. Gracz może podjąć decyzję o wejściu w
związek (co może nastąpić w różnym wieku) i o potomstwie. Założenie rodziny przynosi
zarówno korzyści, jak i wyzwania. Korzyści mogą obejmować wzrost satysfakcji życiowej
bohatera (w grze może to być ukryty lub jawny wskaźnik szczęścia – zwykle stabilne relacje
rodzinne wpływają pozytywnie na samopoczucie postaci). Rodzina może też stanowić pewne
zabezpieczenie na starość (np. w prawdziwym życiu dzieci często wspierają starszych rodziców,
co gra może symbolicznie uwzględnić jako ewentualny bonus do komfortu życia w starszym
wieku, choć nie należy promować myślenia, że dzieci są „inwestycją” finansową). Z drugiej
strony, posiadanie rodziny to dodatkowe obciążenia finansowe i czasowe: utrzymanie dzieci
wiąże się z kosztami (życie, edukacja dzieci, opieka) i zmniejsza kwotę, jaką postać może
odkładać dla siebie. Dzieci i partner wymagają także poświęcenia czasu – np. gracz mający
rodzinę może mieć mniej czasu na rozwój kariery czy hobby (jeśli w grze zaimplementowany
jest podział czasu). W scenariuszu życiowym mogą wystąpić trudne wydarzenia rodzinne (ujęte
też w ryzykach): rozstanie lub rozwód (dzielimy majątek, spadek szczęścia postaci), śmierć
członka rodziny (trauma dla bohatera, ewentualnie utrata drugiego dochodu jeśli partner
pracował). Obszar życia rodzinnego uczy gracza zarządzania relacjami i pokazuje, że sukces
życiowy to nie tylko kariera i pieniądze, ale także bliscy – i że jedno wpływa na drugie (np. praca
po godzinach może pogorszyć relacje rodzinne).
• Pasje i hobby: Ten obszar reprezentuje czas wolny i aktywności, które postać wykonuje dla
przyjemności lub samorozwoju poza pracą. Gracz może zdecydować, czy i ile czasu postać
poświęca na hobby (np. sport, czytanie, podróże, rozwijanie talentów artystycznych,
angażowanie się społecznie itp.). Pasje wpływają pozytywnie na jakość życia – mogą zwiększać
szczęście/zadowolenie bohatera, obniżać stres oraz nawet poprawiać zdrowie (jeśli hobby jest
np. sportem czy turystyką). W świecie gry hobby może dawać drobne premie: np. regularne
uprawianie sportu dodaje punkty do zdrowia, a hobby artystyczne czy towarzyskie zwiększa
odporność psychiczną na stres. Jednak angażowanie się w pasje wiąże się też z kosztami:
wymagają czasu (który mógłby być przeznaczony na pracę zarobkową lub naukę) i często
pieniędzy (sprzęt sportowy, wycieczki, itp. wydatki). Gracz musi więc znaleźć równowagę –
postać całkowicie skupiona tylko na pracy może szybko wypalić się (spadek zdrowia
psychicznego i szczęścia), z kolei nadmierne folgowanie sobie kosztem pracy może skutkować
kłopotami finansowymi. Pasje/hobby w grze uczą, że well-being i sukces to nie tylko praca, ale
też realizowanie własnych zainteresowań, co przekłada się na długofalowe korzyści (mniej
stresu, lepsze zdrowie).
• Oszczędności emerytalne (ZUS): Jest to obszar finansów związany z państwowym systemem
emerytalnym. Gdy postać pracuje na umowę, która odprowadza składki (np. umowa o pracę,
umowa zlecenie, działalność opodatkowana), część jej dochodu trafia do wirtualnego konta
emerytalnego ZUS. Gra będzie symulować narastanie tych składek przez lata pracy. Na koniec
okresu aktywności zawodowej (osiągnięcie wieku emerytalnego), zgromadzona kwota
zamienia się w emeryturę – miesięczne świadczenie wypłacane postaci do końca życia.
Wysokość emerytury zależy wprost od sumy składek oraz od przewidywanej długości życia (gra

6

może używać tablic średniego dalszego trwania życia, jak to robi ZUS – np. dzielić zgromadzony
kapitał przez liczbę miesięcy, jakie statystycznie zostały do przeżycia). W trakcie gry gracz nie
ma bezpośredniego dostępu do tych pieniędzy – są one „zamrożone” do wieku emerytalnego.
Natomiast kluczowe decyzje to wybór formy zatrudnienia i wysokości zarobków, bo one
wpływają na wysokość odkładanych składek. Np. praca na czarno lub długoletnia przerwa
zawodowa oznacza brak składek, co drastycznie obniży przyszłą emeryturę. Gra zilustruje ten
mechanizm – np. w panelu finansowym będzie widoczna rosnąca kwota na koncie ZUS oraz
szacowana przyszła emerytura. Celem jest uświadomienie graczom, jak ich decyzje (kariera,
przerwy na wychowanie dzieci, wyjazd za granicę bez transferu składek itp.) wpływają na
bezpieczeństwo finansowe w starości. Gracz przekona się, że poleganie wyłącznie na ZUS bywa
ryzykowne – jeśli przez życie zarabiało się mało albo z przerwami, emerytura będzie niska. To
zachęci do myślenia o filarach dodatkowych.
• Prywatne oszczędności i inwestycje: Ten obszar to finanse osobiste, nad którymi gracz ma
bezpośrednią kontrolę przez całą grę. Obejmuje wszelkie formy oszczędzania i inwestowania
poza obowiązkowym ZUS. Gracz decyduje, jak gospodarować swoim budżetem: ile pieniędzy
wydać na bieżące życie, a ile odłożyć lub zainwestować. Do dyspozycji będą różne opcje:
odkładanie oszczędności na nieoprocentowanym koncie (gotówka), lokaty bankowe, fundusze
inwestycyjne, giełda, a nawet polisy oszczędnościowe czy inwestycje w nieruchomości – w
uproszczonej formie dostosowanej do gry. Każda opcja ma inne ryzyko i oczekiwaną stopę
zwrotu (np. gotówka jest najbezpieczniejsza, ale praktycznie nie pomnaża kapitału;
fundusze/akcje mogą dać wyższy zysk, ale z ryzykiem straty; nieruchomości wymagają dużego
wkładu, ale mogą generować dochód z wynajmu). Gracz może wybrać strategię inwestycyjną
dla swojej postaci (np. bezpieczna, zrównoważona, agresywna – tak jak sugerują dane w
Słowniku gry, gdzie te profile inwestycji były wymienione). Celem w tym obszarze jest
zgromadzenie kapitału, z którego postać skorzysta w sytuacjach kryzysowych (poduszka
finansowa na wypadek utraty pracy czy choroby) oraz na starość, uzupełniając ewentualnie
skromną emeryturę z ZUS. W grze prywatne oszczędności mogą być wykorzystywane do dużych
wydatków (np. zakup mieszkania, edukacja dzieci, leczenie) – gracz musi decydować, czy warto
uszczuplić oszczędności na dany cel, czy też zabezpieczyć je na przyszłość. Obszar ten uczy
finansowej przezorności: gracze dowiedzą się, że regularne oszczędzanie nawet małych kwot
oraz ich inwestowanie może przynieść znaczny efekt dzięki długiemu horyzontowi (mechanizm
procentu składanego), a brak oszczędności naraża na poważne problemy w razie nagłych
zdarzeń. Będzie to mocno powiązane z wydarzeniami z kategorii Ryzyka – posiadanie
oszczędności czyni np. utratę pracy mniej dotkliwą.
• Ryzyka życiowe: Ten obszar obejmuje losowe zdarzenia i czynniki ryzyka, które mogą wpłynąć
na losy postaci. Symulacja ma uwzględniać, że życie jest nieprzewidywalne – poza decyzjami
gracza istnieje element przypadku. Wśród ryzyk znajdują się:
o Choroby – Poważne problemy zdrowotne, które mogą dotknąć postać lub jej bliskich.
W grze choroba może powodować czasowe obniżenie wskaźnika zdrowia, wymusić
przerwę w pracy (brak dochodu przez pewien okres) i generować dodatkowe koszty
leczenia. Przykładem zdarzenia może być wykrycie poważnej choroby w średnim
wieku: gracz musi wtedy zapłacić za leczenie z oszczędności lub skorzystać z
ubezpieczenia (o ile wcześniej zainwestował w polisę). Choroba wpływa też na plany –
np. opóźnia przejście na emeryturę lub zmusza do zmiany trybu życia.
o Wypadki – Nagłe zdarzenia losowe, takie jak wypadek samochodowy czy uraz, które
mogą spowodować inwalidztwo czasowe lub trwałe. W grze wypadek skutkuje

7

gwałtownym spadkiem zdrowia postaci; może wymagać rehabilitacji (koszty, czas) i
może skutkować trwałym obniżeniem maksymalnego poziomu zdrowia. Również
możliwa jest czasowa niezdolność do pracy. Gracz musi zarządzić sytuacją kryzysową –
np. korzystając z oszczędności na przetrwanie okresu bez dochodu. Wypadki uczą, jak
ważne jest posiadanie zabezpieczeń (finansowych, ubezpieczeniowych) i dbanie o
bezpieczeństwo.
o Rozstania (rozwód/separacja) – Zdarzenie z obszaru rodzinnego: jeśli postać jest w
związku, istnieje szansa na rozpad tej relacji. W grze może to być spowodowane np.
zbyt niską dbałością o relacje (postać cały czas pracowała i ignorowała rodzinę) albo
całkowicie losowo. Rozstanie niesie konsekwencje: podział majątku (połowa
oszczędności może przypaść partnerowi), ewentualne alimenty na dzieci, spadek
zadowolenia życiowego postaci oraz okres obniżonej produktywności (wpływ
emocjonalny na pracę). Gracz uczy się, że stabilność rodziny nie jest gwarantowana, a
inwestowanie czasu w relacje ma realną wartość.
o Śmierć – Najbardziej drastyczne zdarzenie. Może dotyczyć członka rodziny (np. śmierć
partnera lub nawet dziecka) albo samej postaci gracza. Śmierć bliskiej osoby wpływa
na stan psychiczny bohatera (silny spadek szczęścia, być może okres depresji
przekładający się np. na przerwanie pracy lub konieczność wydania oszczędności na
pochówek i inne sprawy). Jeśli natomiast chodzi o śmierć głównej postaci – to
zdarzenie to kończy rozgrywkę (game over) przed osiągnięciem celów.
Prawdopodobieństwo przedwczesnej śmierci można powiązać z poziomem zdrowia i
czynnikami ryzyka (np. skrajnie zaniedbane zdrowie, brak leczenia choroby, bardzo
podeszły wiek). Śmierć w rodzinie może też mieć aspekt finansowy – np. przy dobrym
planowaniu można było wykupić ubezpieczenie na życie, które wypłaci środki rodzinie
w razie takiego zdarzenia (edukacja w kierunku zabezpieczeń).
o Utrata pracy – Zdarzenie polegające na nagłym zakończeniu stosunku pracy niezależnie
od woli gracza (np. upadek firmy, zwolnienia grupowe, automatyzacja stanowiska).
Skutkuje to utratą dochodu do czasu znalezienia nowej pracy. Gracz będzie musiał
zareagować: ma opcję poszukiwania nowej pracy (co może potrwać kilka
„tur”/miesięcy w grze) oraz ewentualnie musi korzystać z oszczędności lub zasiłku (jeśli
system uwzględnia zasiłek dla bezrobotnych). To wydarzenie podkreśla wagę
dywersyfikacji umiejętności (możliwość przebranżowienia się), posiadania
oszczędności na czarną godzinę oraz rozsądnego zadłużania się (gracz bez oszczędności
może popaść w długi próbując przetrwać bez pracy).
o Trudne warunki pracy – Nie jest to jedno zdarzenie, ale raczej ciągły czynnik ryzyka.
Obejmuje sytuacje takie jak konieczność pracy po godzinach, wysoki stres w pracy,
praca w szkodliwych warunkach (np. fizycznie wyczerpująca albo w niebezpiecznym
środowisku). W grze może to być powiązane z określonymi zawodami lub z decyzją
gracza, by pracować więcej dla większych zarobków. Konsekwencje pojawiają się
stopniowo: pogorszenie zdrowia (np. każda dodatkowa godzina ponad normę obniża
nieco wskaźnik zdrowia lub zwiększa stres), pogorszenie relacji rodzinnych (mniej czasu
w domu) i spadek szczęścia. Gracz powinien zauważyć, że eksploatowanie postaci
ponad miarę przynosi krótkoterminową korzyść finansową, ale długoterminowe
szkody – może doprowadzić do wypalenia zawodowego lub poważnej choroby. Ta
mechanika ma uczyć umiaru i równowagi: czasem lepiej zarobić trochę mniej, ale
zachować zdrowie i relacje.

8

Każdy z powyższych obszarów jest ze sobą powiązany (jak omówiono niżej w sekcji o zależnościach).
Gracz nie może traktować żadnego aspektu w oderwaniu – sukces w grze wymaga holistycznego
podejścia do życia postaci. Dzięki temu gra oddaje złożoność realnego życia, gdzie decyzje w jednej
sferze wpływają na inne.
Zmienne w grze i zależności między nimi
W symulacji zdefiniowanych jest wiele zmiennych, które reprezentują stan postaci i jej otoczenia.
Poniżej przedstawiono listę kluczowych zmiennych oraz opis zależności między nimi:
• Wiek – aktualny wiek postaci (mierzony w latach, postęp w czasie gry). Wiek rośnie w trakcie
rozgrywki, co uruchamia pewne mechanizmy: z wiekiem zmniejsza się maksymalny poziom
zdrowia, zbliżamy się do wieku emerytalnego (po jego osiągnięciu następuje zmiana źródła
dochodu z pracy na emeryturę), dzieci dorastają, itp. Wiek wpływa na dostępne wydarzenia
(np. niektóre choroby pojawiają się dopiero w starości) i modyfikuje inne zmienne (np. wraz z
wiekiem rosną wydatki na zdrowie). Jest to kluczowy, niezależny czynnik postępu gry – czas
płynie nieubłaganie, zmuszając gracza do planowania na przyszłość.
• Stan zdrowia – zmienna reprezentująca zdrowie postaci (np. w skali 0–100 albo jako
procent/sprawność). Zdrowie jest dynamicznie zależne od wieku (im starsza postać, tym
trudniej utrzymać 100% zdrowia), stylu życia (decyzje gracza: dieta, sport, praca po godzinach
– mogą podnosić lub obniżać zdrowie) oraz zdarzeń losowych (choroby, wypadki mogą nagle
obniżyć zdrowie). Wysokie zdrowie zwiększa szanse dożycia końca gry i utrzymania zdolności
do pracy; niskie zdrowie może wywołać kaskadę negatywnych skutków (przerwa w pracy,
wydatki na leczenie, a nawet śmierć postaci). Zależności: Wiek + zły styl życia → spadek
zdrowia; zdrowe nawyki → spowolnienie spadku zdrowia; zdrowie < X → ryzyko zdarzeń (np.
choroby).
• Wykształcenie (poziom edukacji) – zmienna dyskretna określająca najwyższy poziom
ukończonej edukacji (np. 0 – brak, 1 – podstawowe/średnie, 2 – zawodowe, 3 – licencjat, 4 –
magister/inżynier, 5 – doktorat; lub alternatywnie nazwy etapów). Wykształcenie jest wyborem
gracza i może zostać zwiększone poprzez zainwestowanie czasu (lat) i często pieniędzy we
własną edukację. Ta zmienna silnie wpływa na ścieżkę kariery i dochody: wysoki poziom
edukacji odblokowuje stanowiska o wyższym wynagrodzeniu (jak wynika z danych – np.
stanowiska prawnika czy informatyka wymagają wyższego wykształcenia i oferują znacznie
wyższe płace niż prace dla osób bez kwalifikacji). Zależność jest pozytywna: Wykształcenie ↑
→ Dostępne lepsze oferty pracy ↑ → Dochód potencjalny ↑. Jednak edukacja wiąże się z
opóźnieniem wejścia na rynek pracy (koszt alternatywny) i ewentualnym zadłużeniem (np.
kredyt studencki) – te elementy mogą być uproszczone w grze, ale podkreślamy, że edukacja
to inwestycja długoterminowa.
• Doświadczenie zawodowe/poziom kariery – zmienna powiązana z pracą, rośnie wraz z
przepracowanymi latami i osiągnięciami. Doświadczenie zwiększa szanse na awans lub na
znalezienie lepszej pracy. Jest zależne od: Łączna liczba lat pracy, branża, ewentualne szkolenia.
Ta zmienna sprzęga się z wykształceniem: np. ktoś z niższym wykształceniem może dzięki
długiemu doświadczeniu też osiągnąć wysoką pozycję, choć zajmie to więcej czasu.
Doświadczenie i wykształcenie wspólnie determinują poziom zawodowy (w Słowniku gry
opisany jako „poziom zawodowy” potrzebny do danego zawodu). Zależności: Doświadczenie ↑
+ Edukacja ↑ → awans/zmiana pracy → Dochód ↑. Również: Dłuższa przerwa w pracy (np.
urlop wychowawczy) → stagnacja lub spadek doświadczenia względnego (bo
technologia/postęp idą naprzód).

9

• Dochód (wynagrodzenie) – główna zmienna finansowa w okresie pracy, zależna od stanowiska
pracy. Dochód jest funkcją wykształcenia, doświadczenia oraz branży (np. lekarz czy
programista zarabia więcej niż pracownik fizyczny bez kwalifikacji). W grze konkretne wartości
dochodu brutto/netto są przypisane do ofert pracy (jak w arkuszu Oferty pracy – każda oferta
ma podane wynagrodzenie brutto i wyliczone netto). Dochód wpływa na inne zmienne
finansowe: część dochodu → wydatki bieżące, część → składki ZUS, część → potencjalne
oszczędności. Wyższy dochód pozwala na wyższy standard życia (ale to może zwiększać wydatki,
jeśli gracz się na to zdecyduje) oraz na odkładanie większych kwot. Zależności: Dochód ↑ →
(przy stałych wydatkach) Oszczędności ↑, Składka emerytalna ↑ → wyższa emerytura w
przyszłości. Z drugiej strony, prace z wysokim dochodem mogą mieć wysokie wymagania (stres,
kwalifikacje) – więc tu pojawia się związek: Dochód bardzo wysoki ↔ często Trudne warunki
pracy ↑ (co szkodzi zdrowiu i relacjom).
• Budżet / oszczędności prywatne – zmienna reprezentująca aktualny stan posiadanych przez
postać pieniędzy dostępnych „pod ręką” (nie licząc ZUS). Zaczynamy z pewną kwotą (może
minimalną lub zero, w zależności od scenariusza, ewentualnie długi studenckie), a następnie
budżet zmienia się co turę (np. rok): Budżet = Budżet + Dochód netto – Wydatki bieżące –
wydatki wyjątkowe. Jeśli gracz decyduje się inwestować, budżet dzieli się na różne aktywa, ale
łączna wartość netto to nadal ta zmienna (suma gotówki i wartości inwestycji). Budżet jest
powiązany ze wszystkimi decyzjami: wysoki budżet daje możliwość wyboru (np. wcześniejsza
emerytura, opłata za leczenie, inwestycje), zaś niski budżet ogranicza opcje (postać żyje od
wypłaty do wypłaty, jest bardzo podatna na wstrząsy). Zależności: Dochód ↑ → Budżet ↑ (jeśli
wydatki pod kontrolą), Wydarzenia losowe negatywne → nagły spadek Budżetu (koszty),
Inwestycje udane → wzrost Budżetu, Brak oszczędności + utrata pracy → konieczność
zadłużenia się (Budżet ujemny?). Budżet ma też sprzężenie z życiem rodzinnym: Więcej dzieci
→ większe stałe wydatki → presja na Budżet.
• Poziom zadowolenia/szczęścia – opcjonalna zmienna miękka, agregująca satysfakcję życiową
postaci. Na ten poziom wpływ mają czynniki z różnych obszarów: Zdrowie, Relacje rodzinne,
Stres z pracy, Realizacja hobby, ew. cechy osobowości. Np. zdrowa, wypoczęta postać z
kochającą rodziną będzie miała wysoki wskaźnik szczęścia, nawet jeśli nie zarabia ogromnych
pieniędzy; z kolei bardzo bogata postać, ale samotna i schorowana – niski. Ta zmienna może
wpływać na rozgrywkę poprzez motywację postaci: niskie szczęście może zwiększać
prawdopodobieństwo negatywnych zdarzeń (np. wypadek z przemęczenia, rozpad związku),
albo obniżać efektywność w pracy. Wysokie szczęście może dawać drobne premie (np. mniejsza
szansa zachorowania, bo postać ma niższy stres). Zależności: Hobby ↑, Relacje rodzinne dobre,
Zdrowie dobre → Szczęście ↑; Przepracowanie, Samotność, Utrata bliskiego → Szczęście ↓. Ta
zmienna spina jakościowo wszystkie obszary, pokazując, że trzeba dbać o równowagę.
• Relacje społeczne – można traktować jako część szczęścia lub osobno. Chodzi o jakość relacji w
rodzinie i ewentualnie przyjaciół. Zależna od: czas poświęcony rodzinie, wydarzenia (np.
kłótnie, zdrady – to może nie wchodzić w zakres gry, za skomplikowane). Dobre relacje dają
wsparcie (np. może zmniejszać negatywny wpływ stresu, albo w późnym życiu dziecko może
pomóc finansowo – zależność realna: niektórzy liczą na wsparcie dzieci na starość, ale w grze
można to ująć jako drobny bonus do emerytalnego bezpieczeństwa, jeśli mamy dzieci).
• Emerytura (świadczenie) – to zmienna pojawiająca się od momentu zakończenia pracy. Jej
wysokość zależy od składek ZUS zgromadzonych oraz od parametrów zewnętrznych (jak
wspomniane tablice życia – gra może uprościć, ale generalnie: im więcej zgromadzono i im
krócej przewidywane życie, tym wyższa miesięczna emerytura). Zależności: Dochód i lata pracy

10

↑ → składki ↑ → Emerytura ↑. Jednak emerytura może być też zwiększona przez prywatne
filary – np. jeśli gracz zbudował portfel inwestycji, to de facto na emeryturze ma dodatkowy
dochód (z wynajmu mieszkania, z dywidend, czy po prostu żyje z oszczędności – w grze to
będzie symulowane poprzez stopniowe zużywanie prywatnych oszczędności po zaprzestaniu
pracy, chyba że graficznie pokażemy to jako „prywatna emerytura”). Z kolei wcześniejsze
przejście na emeryturę (np. w wieku 60 lat zamiast 65) → mniej lat składkowych i dłuższy okres
pobierania świadczenia → niższa emerytura. Gracz może więc zobaczyć zależność: dłuższa
praca = wyższa emerytura państwowa, ale czy kosztem zdrowia?
• Wydatki stałe i zmienne – choć to nie jedna zmienna, warto wspomnieć: gra będzie śledzić
comiesięczne koszty utrzymania postaci. Wydatki rosną, gdy postać zakłada rodzinę (dzieci),
gdy podnosi standard życia (większe mieszkanie, lepsze jedzenie, rozrywki) albo w wyniku
inflacji (choć inflację można pominąć dla prostoty, ewentualnie zakładać stałe ceny). Zależność
jest taka, że Wydatki rosną wraz z dochodem (skłonność do tzw. inflacji stylu życia), chyba że
gracz świadomie tego unika. Kontrola wydatków jest kluczowa dla oszczędności: Wydatki
mniejsze niż dochody → nadwyżka do oszczędzenia. Zdarzenia losowe mogą generować
wydatki nadzwyczajne (leczenie, naprawy, koszty rozwodu etc.).
Podsumowując zależności między zmiennymi, można je ująć w kilka głównych punktów:
1. Edukacja → Praca/Kariera → Dochód: Wyższa edukacja umożliwia lepszą pracę i zarobki.
Lepsza praca z czasem to wyższe dochody i pozycja zawodowa. Brak inwestycji w edukację
oznacza ograniczone możliwości kariery i niższe dochody długoterminowo.
2. Dochód → Oszczędności (ZUS i prywatne) → Emerytura: Wyższy dochód (szczególnie legalny,
oskładkowany) oznacza większe składki emerytalne oraz potencjalnie większe kwoty, które
można odłożyć prywatnie. To przekłada się na lepsze zabezpieczenie na starość. Niskie dochody
lub przerwy w pracy skutkują niższą emeryturą i koniecznością polegania na skromnych
oszczędnościach albo obniżenia standardu życia.
3. Zdrowie ↔ Praca i Styl życia: Dbałość o zdrowie (odpoczynek, brak przepracowania,
profilaktyka) pozwala pracować dłużej i cieszyć się życiem, natomiast intensywna praca
kosztem zdrowia może krótkoterminowo dać awans lub pieniądze, ale prowadzi do chorób,
które przerwą karierę i generują koszty. Ponadto, stan zdrowia warunkuje długość życia, więc
wpływa pośrednio na to, ile lat postać będzie korzystać z emerytury (w grze można założyć, że
bardzo złe zdrowie może skrócić rozgrywkę).
4. Rodzina → Wydatki i wsparcie emocjonalne: Posiadanie rodziny zwiększa wydatki (co wymaga
większych dochodów lub ograniczenia oszczędności), ale daje korzyści niematerialne (szczęście,
potencjalnie wsparcie w trudnych chwilach). Np. samotna postać może wydawać mniej i więcej
zaoszczędzić, ale może mieć niższy poziom zadowolenia, co np. zwiększa ryzyko wypalenia czy
depresji.
5. Oszczędności prywatne ↔ Ryzyka: Im większa poduszka finansowa i lepsze ubezpieczenia,
tym łagodniej postać przejdzie przez losowe kryzysy. Np. osoba z oszczędnościami poradzi sobie
z utratą pracy (ma za co żyć przez kilka miesięcy), stać ją na leczenie w razie choroby, itd. Osoba
bez oszczędności może wpaść w spiralę problemów: jeden wypadek powoduje długi, te
zwiększają stres, co powoduje kolejne problemy zdrowotne. Gra będzie ilustrować ten efekt
domina.

11

6. Hobby i czas wolny ↔ Praca i szczęście: Poświęcanie czasu na hobby zmniejsza czas na pracę
(więc może wolniej rośnie kariera i dochody), ale zwiększa szczęście i zdrowie. To działa jak
bufor przeciw negatywnym efektom stresu. Całkowite zaniechanie czasu wolnego może
przyspieszyć rozwój kariery, ale zwykle prowadzi do wypalenia (co potem odbija się np. na
zdrowiu i efektywności pracy).
7. Decyzje krótkoterminowe vs długoterminowe: Wiele zależności w grze stawia przeciw sobie
korzyść krótkoterminową a zysk długoterminowy. Np.: wydanie pieniędzy na przyjemności
teraz vs zaoszczędzenie ich na przyszłość; praca nadgodzinami dla premii w tym roku vs ryzyko
pogorszenia zdrowia i relacji; pójście na studia teraz (brak dochodu przez 5 lat) vs od razu praca
(natychmiastowy dochód, ale niższy sufit kariery). Gracz musi balansować te decyzje. Gra
poprzez mechanizmy punktowe i zdarzenia pokaże konsekwencje: często opcja zachęcająca w
krótkim okresie okaże się kosztowna w długim (i odwrotnie, inwestycja i wysiłek teraz opłacą
się później).
Wszystkie te zależności są celowo uwypuklone w projekcie gry, by gracze doświadczalnie zrozumieli
złożoność planowania życia. Symulacja umożliwi obserwowanie skutków decyzji w przyspieszonym
tempie – np. w ciągu kilkudziesięciu minut rozgrywki postać starzeje się o kilkadziesiąt lat – co daje
unikalną perspektywę. Interakcje między zmiennymi mają oddać realizm (na tyle, na ile to możliwe przy
zachowaniu grywalności), dzięki czemu po zakończeniu gry użytkownik może wyciągnąć wnioski
aplikowalne w realnym życiu, np. „jeśli teraz nie zadbam o zdrowie/oszczędności, później będzie za
późno”. Gra, poprzez system zmiennych i zależności, przekazuje więc wiedzę w sposób praktyczny i
angażujący, zamiast teoretycznych wykładów.