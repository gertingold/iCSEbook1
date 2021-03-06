Równanie  logistyczne
+++++++++++++++++++++



Trochę historii
===============


W latach siedemdziesiątych XX wieku, na Uniwersytecie w Oxford,
australijski uczony Robert May zajmował się teoretycznymi aspektami
dynamiki populacyjnej. Swoje prace podsumował w artykule, który ukazał
się w *Nature* pod prowokującym tytułem "Proste modele matematyczne z
bardzo skomplikowaną dynamiką" x[may76]_. Artykuł ten po latach stał
się jedną z najczęściej cytowanych prac z teoretycznej ekologii.  Co
wzbudziło tak wielkie zainteresowanie w tej pracy?

May zajmował się zastosowaniem matematyki w ilościowym opisie zjawisk
ekologicznych. Klasycznym zadaniem w tej dziedzinie jest obliczenie wielkości 
populacji pewnego gatunku w czasie, znając jej stan liczebny w chwili
początkowej. Najprostszym, z punktu widzenia modelowania
matematycznego, rodzajem ekosystemów wydawały się takie w których
życie jednego pokolenia populacji trwa jeden sezon. Dobrym przykładem
jest populacja owadów, które w ciągu jednego sezonu przechodzą pełną
metamorfozę np. motyle. Czas jest w naturalny sposób podzielony na
dyskretne okresy, odpowiadające cyklom życia populacji. Równania
opisujące taki ekosystem mają więc formę dyskretnych układów
iterowanych w których bieżąca liczebność osobników danego gatunku w
ekosystemie jest funkcją liczebności w poprzednim okresie.

Robert May zajmował się między innymi właśnie taką dynamiką. Badając
układy iteracyjne, uprościł ekosystem do jednego gatunku w którym
populacja była funkcją kwadratową populacji w roku poprzednim. Skąd
taki model?  Najprostszym równaniem dyskretnym opisującym ewolucję
populacji jest model liniowy:

.. math::
   :label: Ni

   N_{i+1} = \alpha \; N_{i},

gdzie :math:`N_i` to liczebność w i-tym sezonie. Łatwo się przekonać,
że takie równanie może prowadzić to trzech scenariuszy. Jeżeli
:math:`\alpha>1` to populacja będzie nieograniczenie rosnąć, jeżeli
:math:`\alpha<1` to zaniknie oraz dla :math:`\alpha=1` ewolucja nie
będzie zmieniać stanu liczebnego populacji. Najprostszym rozwinięciem
tego modelu jest wprowadzenie zależności stałej :math:`\alpha` od
wielkości populacji. Wyobraźmy sobie populacje szkodników w zamkniętym
ekosystemie. Szkodniki zjadają zboże, którego jest dokładnie taka sama
ilość co roku. Jeżeli owadów jest mało w porównaniu do ilości
pożywienia, to mogą rozmnażać się z pełną siła rozrodczą - na przykład
w następnym sezonie będzie ich cztery razy więcej niż w
poprzednim. Jednak w miarę wzrostu liczebności szkodników, pożywienia
nie będzie wystarczać i siła rozrodcza będzie maleć. W krytycznym
przypadku można sobie wyobrazić ze owady zjadają latem całe zboże po
czym wszystkie osobniki umierają z głodu przed osiągnięciem zdolności
rozrodczej. Załóżmy więc, że nasza stała rozrodu będzie liniową
funkcją populacji:

.. math::
   :label: alpha

   \alpha = \alpha( N_{i} ) = A - B N_{i},

gdzie :math:`A` to stała wzrostu populacji w warunkach dostatku
pożywienia a :math:`B` jest stałą, która określa jak szybko brak
pożywienia będzie zmniejszał siłę rozrodczą. W szczególności jeśli
:math:`N_i=A/B` to pożywienia jest na tyle mało, że żaden osobnik nie
przeżywa sezonu żerowania.


Równanie :eq:`Ni` ze stałą :eq:`alpha`, można przeskalować do postaci
matematycznie równoważnej, zależnej tylko od jednego
parametru. Równanie takie obecnie jest znane pod nazwą odwzorowania
logistycznego:

.. math::
   :label: logistic

   x_{i+1} = a x_{i} (1 - x_{i}),

gdzie :math:`a<=4` jest pewną dodatnią stałą a :math:`x_i\in(0,1)`
jest proporcjonalne do liczebności populacji w i-tym sezonie. 

.. note:: 

   Jeśli populacja ma liczebność równą jeden, to nie dożywa do
   następnego pokoleniu. Tak samo było by w przypadku gdy jest większa
   od jednego, dlatego wystarczy się ograniczyć do
   :math:`x_i\in(0,1)`. Z tego samego powodu nie rozważamy parametru
   :math:`a>4` - bowiem :math:`a<=4` odwzorowanie logistyczne
   przeprowadza zawsze odcinek (0,1) w odcinek (0,1).


Mogło by się wydawać, że tak prosty model będzie dawał proste
wyniki. Spróbujmy sami!

Rozważmy model :eq:`logistic` dla parametru :math:`a=0.5`, startując z
liczebności :math:`x=0.45`. Kolejne wartości populacji można otrzymać
stosując przekształcenie kwadratowe :eq:`logistic` do wartości z
poprzedniego sezonu, na przykład za pomocą poniższego programu:

.. sagecellserver::

   a = 0.5 
   x = 0.45
   for i in range(10):
       x = a*x*(1-x)
       print x

Wykonując ten przykład otrzymujemy kolejne wartości populacji, które wraz z
upływem czasu dążą do zera. Eksperymentując z powyższym kodem łatwo
też jest się przekonać, że niezależnie od wartości z której
startujemy, zawsze populacja ginie. 

Możemy sobie też ułatwić zadanie, wykorzystując w Sage narzędzie do
szybkiego prototypowania elementów interaktywnych - dekorator
:code:`@interact`. Ponadto, zamiast wypisywać wartości liczbowe
przedstawmy je graficzne rysując wykres liczebności populacji od
czasu.

.. sagecellserver::
   :linked: false

   @interact
   def myf(x = slider(0.0,1.0,0.01,default=0.4),a=slider(0,4,0.01,default=0.5)):
       pkts = []
       for i in range(25):
           pkts.append( (i,x) )
           x = a*x*(1-x)
       point(pkts,figsize=(7,3),ymin=0,ymax=1).show()

W powyższym kodzie, elementy :code:`slider` pozwalają nam na wykonanie
funkcji :code:`myf` dla wybranych interaktywnie wartości :math:`x` i
:math:`a`. 

Zwiększmy teraz parametr :math:`a` do dowolnej wartości z przedziału
:math:`a\in(1,3)`.  Okazuje się, że wtedy ciąg :math:`x_i` dąży do
pewnej wielkości - tym razem jednak nie jest to zero. Interpretując w
kategoriach ekologii, możemy powiedzieć, że wielkość populacji ustala
się na pewnym poziomie, który nie zmienia się z sezonu na
sezon. Podobnie jak poprzednim razem, ta wartość graniczna nie zależy
od punktu startowego. Czyli niezależnie od tego czy populacja
wystartuje bardzo małą liczebnością czy dużą, po kilku pokoleniach i
tak będzie taka sama. W takim przypadku mamy efekt dążenia ekosystemu
do stabilizacji - populacja dostosowuje swoją liczebność do możliwości
wyżywienia się.

Taki efekt był oczekiwany przez badaczy i równanie logistyczne
:eq:`logistic` nie przyciągnęło by szczególnej uwagi gdyby nie
pewna niespodzianka. Okazało się bowiem, że dla pewnych wartości
parametru :math:`a` model nie zachowuje się w przewidywalny
sposób. Pojawiają się nie tylko stany okresowe, ale i stany w których
populacja z roku na rok zmienia się w chaotyczny sposób i występuje
czułość na warunki początkowe - wszystkie cechy, które są
charakterystyczne dla chaosu deterministycznego.

Zbadajmy to! Na początek ustalmy wartość parametru na :math:`a = 3.2`
i przyjrzyjmy się ewolucji. Zaskoczeniem może być fakt, że tym razem
populacja nie osiąga jednej wartości, ale dwie, które występują
kolejno po sobie co drugi sezon.  Przyjrzyjmy się bliżej temu
zjawisku. Po pierwsze jeżeli ciąg kolejnych wartości :math:`x_i` dąży
do pewnej granicy, to możemy napisać dokładny warunek na jej wartość
:math:`x_g`. Musi bowiem zachodzić :math:`x_g=f(x_g)`. Jeżeli taki
punkt istnieje dla pewnej funkcji :math:`f`, to mówimy, że jest to
punkt stały odwzorowania. Możemy więc dokładnie wyznaczyć wartość
punktów stałych odwzorowania logistycznego w zależności od parametru
:math:`a`. Prosty rachunek pokazuje, że mamy dwa rozwiązania:
:math:`x_g = 0` oraz :math:`x_g=1-\frac{1}{a}`. O ile :math:`x_g = 0`
jest punktem stałym dla dowolnej wartości parametru, to pamiętając, że
sens mają tylko wartości :math:`x_i\in(0,1)`, drugi punkt stały
istnieje dla wartości :math:`a\in(1,4)`. Możemy narysować więc wykres
punktów stałych od parametru:

.. sagecellserver::

   var('a')
   plot(0,(a,0,1),thickness=2)+\
    plot(1-1/a,(a,1,4),thickness=2)+\
    plot(0,(a,1,4),thickness=2,color='red',figsize=(7,3))


Jeżeli mamy równanie zależne od parametru i ilość rozwiązań zmienia się
wraz z tymże parametrem to mówimy, że następuje bifurkacja. W punkcie
:math:`a=1` następuje właśnie bifurkacja i układ zamiast jednego
rozwiązania ma dwa. Jednak zauważmy jeszcze jedno ciekawe zjawisko. Z
dowolnego warunku początkowego dla :math:`a<1` zawsze otrzymywaliśmy
malejący ciąg populacji, który wydawał się być przyciągany do jedynego
w tym obszarze punktu stałego - do zera. Taki punkt, do którego układ
jest przyciągany zwany jest też atraktorem układu. Dla :math:`a>1`
mamy dwa punkty stałe. Okazuje się, że w tym obszarze startując z
dowolnego punktu z wyjątkiem :math:`x=0` zawsze będziemy dążyć do
drugiego rozwiązania, który jest atraktorem!  Oznacza to, że jeżeli
rozwiązanie :math:`x=0` zaburzymy dowolnie małą liczbą
np. :math:`x=0.0001` to i tak po kilkunastu iteracjach populacja
będzie dążyła do :math:`x_g=1-\frac{1}{a}` (Poeksperymentujmy!).
Stabilny dla :math:`a<1` punkt stały :math:`x=0` staje się niestabilny
dla :math:`a>1`.

Wróćmy więc do naszej sytuacji, w której mamy :math:`a = 3.2`. Według
poprzednich wyliczeń dalej powinniśmy mieć punkt stały
:math:`x_g=1-\frac{1}{a}`! I mamy, sprawdźmy:

.. sagecellserver::

   a=3.2
   x=1-1/a
   print "Wartosc poczatkowa x=",x
   pkts = []
   for i in range(125):
       pkts.append( (i,x) )
       x = a*x*(1-x)
   point(pkts,figsize=(7,3),ymin=0,ymax=1).show()

Dodajmy jednak do wartości początkowej pewną małą liczbę np. niech
:code:`x=x+1e-6`. Zobaczmy co się stanie? Okazuje się, że we
wcześniejszym punkcie (jak się okaże :math:`a=3`) nastąpiła kolejna
bifurkacja w wyniku której rozwiązanie :math:`x_g=1-\frac{1}{a}`
utraciło stabilność na rzecz oscylacji. Ponieważ oscylacje te są w
pomiędzy dwoma wartościami, to mówimy, że dla :math:`a=3.2` układ ma
punkt okresowy z okresem 2. Właściwie to możemy tylko przypuszczać, że
tak jest bo wynika to tylko z zabaw podczas których liczba iteracji
była skończona. Możemy jednak w tym przypadku pokazać to
dokładnie. Jeżeli populacja co drugi sezon przechodzi w tą samą to
możemy rozważyć odwzorowanie :math:`g(x)=f(f(x))`, które przeprowadza
układ o dwa sezony do przodu. W taki przypadku powinniśmy punkt stały
dla :math:`g` odpowiada punktowi okresowemu o okresie 2 dla
:math:`f`. Zastosujmy tą chytrą sztuczkę, tym razem z pomocą Sage:

.. sagecellserver::

   var('a x')
   f(x) = a*x*(1-x)
   show( expand( f(f(x))==x) ) 
   s = solve(f(f(x))==x,x)
   show(s)

Dobrze, że możemy wyręczyć się systemem algebry komputerowej, bo
niestety równanie :math:`f(f(x))=x` jest równaniem czwartego stopnia!
Sage na szczęście "potrafi" rozwiązywać analitycznie równania czwartego
stopnia i otrzymujemy rozwiązania. Od razu widzimy wśród pierwiastków
punkty stałe odwzorowania :math:`f`, co jest zrozumiałe, bo jeśli
zachodzi :math:`f(x)=x` to tym bardziej :math:`f(f(x))=x`. Narysujmy
zatem nasz wynik.
 

.. sagecellserver::

   var('x a')
   f(x)=a*x*(1-x)
   s = solve(x==f(f(x)),x)
   show(s)

   plot(s[3].rhs(),(a,0,1),thickness=2)+\
    plot(s[2].rhs(),(a,1,3),thickness=2)+\
    plot(s[3].rhs(),(a,1,4),thickness=2,color='red',figsize=(7,3))+\
    plot(s[0].rhs(),(a,3,4),thickness=2)+\
    plot(s[1].rhs(),(a,3,4),thickness=2)+\
    plot(s[2].rhs(),(a,3,4),thickness=2,ymin=0,ymax=1,color='red')


Wykres ten, zwany diagramem bifurkacyjnym, nie jest do końca
kompletny - skoro pojawiły się dwie bifurkacje to nie ma powodu, żeby
zakładać, że więcej się nie pojawi! W dalszej analizie pojawia się
jednak zasadniczy problem. Otóż nie możemy badać analitycznie punktów
stałych dalszych złożeń odwzorowania :math:`f(f(f(x)))=x`, bo w
poprzednim przypadku wyczerpaliśmy możliwość dokładnego znajdywania
miejsc zerowych wielomianów. Zgodnie z `Teoria Galois
<http://pl.wikipedia.org/wiki/Teoria_Galois>`_ wzory analityczne na
pierwiastki wielomianu kończą się w przypadku ogólnym na stopniu
cztery. Oczywiście można zastosować metody przybliżone, lub metodę
graficzną. Jednak okazuje się, że całkiem niezłym sposobem na poznanie
struktury cykli układu jest po prostu jego symulacja na tyle długa by
układ zdążył dojść wystarczająco blisko do atraktora. Zanim użyjemy
tego sposobu, zapoznajmy się z metodą graficzną - jak mawiano,
ilustracja jest warta tysiąca słów. Zapraszamy do lektury części II!
