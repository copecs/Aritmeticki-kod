# Aritmeticki-kod
Aritmetičko kodiranje je tehnika kompresije podataka sa bogatom istorijom. Njegovi koreni sežu unazad do ključnih doprinosa Claudea Shannona i Davida A. Huffmana. Shannon je postavio temelje varijabilnih dužina kodova za simbole, dok je Huffman 1952. godine razvio praktičan pristup za kodiranje. Ranije, Ransom Horner je u 19. veku stvorio "Hornerovu metodu" za efikasno kodiranje prirodnih brojeva, što se može smatrati pretečom modernih aritmetičkih kodova. Aritmetičko kodiranje nudi visok stepen kompresije, a razvoj moderne računarske tehnologije omogućio je široku primenu ove tehnike u prenosu i skladištenju podataka, od JPEG kompresije slika do kompresije teksta i drugih digitalnih informacija. Nastavak istraživanja i razvoja ovog pristupa obećava efikasniju upotrebu resursa u oblasti komunikacije i skladištenja podataka.

# Primer kako se kodira i dekodira sekvenca 
![ilustrovanje aritmetickog kodovanja](https://github.com/copecs/Aritmeticki-kod/assets/121459386/695f90b2-e74c-4bb3-8d8c-6d36927cc67b)

# Rezultati
Kod uspešno izdvaja simbole iz ulazne rečenice, izračunava njihove verovatnoće i koristi ove verovatnoće da izvrši aritmetičko kodiranje. Zatim dekodira kodiranu poruku kako bi vratila originalni unos. Napomena da aritmetičko kodiranje može naići na probleme sa određenim tipovima ulaza, kao što su simboli koji nisu prisutni u definisanim verovatnoćama ili ekstremno duge rečenice.

Slobodno koristite ovaj projekat kao polaznu tačku za vaše sopstvene eksperimente sa aritmetičkim kodiranjem i kompresijom podataka.

# Slabosti

Aritmetičko kodiranje je moćna tehnika kompresije podataka, ali može biti osetljivo na greške uzrokovane preciznošću brojeva u računarstvu.

Gubitak preciznosti: Kako kodiranje napreduje, intervali postaju sve manji i manji, a brojevi koji ih predstavljaju postaju izuzetno dugi decimalni brojevi. U računarstvu, postoji ograničena preciznost u prikazu decimalnih brojeva, što može dovesti do zaokruživanja i gubitka preciznosti. To može prouzrokovati greške u dekodiranju i gubitak originalnih podataka.

# Test Primeri:
Pokazacemo kako se sam intervala smanjuje u razlicitim test primerima i zasto dolazi do greske:<br />
<strong>Ulaz: "BACA ABAC BACA" </strong><br />
char: B     high: 0.21428571428571425     low: 0     interval: 1<br />
char: A     high: 0.1377551020408163      low: 0.045918367346938764     interval: 0.21428571428571425<br />
char: C     high: 0.12463556851311952     low: 0.10495626822157433     interval: 0.09183673469387754<br />
char: A     high: 0.11760724698042481     low: 0.10917326114119116     interval: 0.019679300291545188<br />
char:       high: 0.11760724698042481     low: 0.11640239186053428     interval: 0.008433985839233646<br />
char: A     high: 0.1171769415804639      low: 0.11666057510051082     interval: 0.0012048551198905327<br />
char: B     high: 0.11677122506050076     low: 0.11666057510051082     interval: 0.0005163664799530815<br />
char: A     high: 0.11673170721764722     low: 0.11668428580622295     interval: 0.0001106499599899391<br />
char: C     high: 0.11672493273030089     low: 0.11671477099928142     interval: 4.742141142427547e-05<br />
char:       high: 0.11672493273030089     low: 0.11672348105444097     interval: 1.0161731019475706e-05<br />
char: B     high: 0.11672379212783952     low: 0.11672348105444097     interval: 1.4516758599231183e-06<br />
char: A     high: 0.11672368103019719     low: 0.11672354771302637     interval: 3.1107339855396265e-07<br />
char: C     high: 0.11672366198488707     low: 0.1167236334169219      interval: 1.333171708167713e-07<br />
char: A     high: 0.11672365178204236     low: 0.11672363953862872     interval: 2.856796517403115e-08<br />
<strong>Izlaz: 0.11672364566033554</strong> <br />
<strong>Test primer se takodje uspesno i dekodira</strong><br /><br /><br />
<strong>Ulaz: "mini delta delta mini delta"<br /></strong>
char: m     high: 0.07407407407407418     low: 0     interval: 1
char: i     high: 0.016460905349794268     low: 0.00548696844993142     interval: 0.07407407407407418<br />
char: n     high: 0.008738505309150041     low: 0.007925621094345386     interval: 0.010973936899862848<br />
char: i     high: 0.00810626203096864      low: 0.007985834739886472     interval: 0.0008128842148046548<br />
char:       high: 0.008039357980367439     low: 0.008021516900207113     interval: 0.00012042729108216813<br />
char: d     high: 0.008031428611407295     low: 0.008029446269167257     interval: 1.7841080160325637e-05<br />
char: e     high: 0.008030767830660618     low: 0.008030547570411722     interval: 1.982342240037724e-06<br />
char: l     high: 0.00803071888393864      low: 0.008030694410577655     interval: 2.202602488957789e-07<br />
char: t     high: 0.00803071616467631      low: 0.008030713445413975     interval: 2.4473360985335924e-08<br />
char: a     high: 0.00803071616467631      low: 0.008030715862536047     interval: 2.7192623344024502e-09<br />
char:       high: 0.008030715996820606     low: 0.008030715952059089     interval: 3.0214026246200287e-10<br />
char: d     high: 0.008030715976926596     low: 0.008030715971953095     interval: 4.4761517409286355e-11<br />
char: e     high: 0.00803071597526876      low: 0.00803071597471615      interval: 4.973500777882833e-12<br />
char: l     high: 0.00803071597514596      low: 0.008030715975084557     interval: 5.526100410602197e-13<br />
char: t     high: 0.008030715975139137     low: 0.008030715975132316     interval: 6.140227215567506e-14<br />
char: a     high: 0.008030715975139137     low: 0.00803071597513838      interval: 6.8209327075408055e-15<br />
char:       high: 0.00803071597513872      low: 0.008030715975138604     interval: 7.563394355258879e-16<br />
char: m     high: 0.008030715975138616     low: 0.008030715975138604     interval: 1.1622647289044608e-16<br />
char: i     high: 0.008030715975138604     low: 0.008030715975138606     interval: 1.214306433183765e-17<br />
char: n     high: 0.008030715975138604     low: 0.008030715975138606     interval: -1.734723475976807e-18<br />
char: i     high: 0.008030715975138604     low: 0.008030715975138606     interval: -1.734723475976807e-18<br />
char:       high: 0.008030715975138604     low: 0.008030715975138606     interval: -1.734723475976807e-18<br />
char: d     high: 0.008030715975138604     low: 0.008030715975138606     interval: -1.734723475976807e-18<br />
char: e     high: 0.008030715975138604     low: 0.008030715975138606     interval: -1.734723475976807e-18<br />
char: l     high: 0.008030715975138604     low: 0.008030715975138606     interval: -1.734723475976807e-18<br />
char: t     high: 0.008030715975138604     low: 0.008030715975138606     interval: -1.734723475976807e-18<br />
char: a     high: 0.008030715975138604     low: 0.008030715975138606     interval: -1.734723475976807e-18<br />
<strong>Izlaz: 0.008030715975138606 </strong> <br />
<strong>Test primer se neuspesno dekodira i izlaz je : mini delta delta me </strong><br /><br /><br />
<strong>Neuspesno dekodiranje desava se zbog toga sto vidimo da se low i high u nekom trenutku stacionariju na nekoj vrednosti
i ne menjaju vrednost to je zato sto interval dodje do najmanje moguce vrednosti za promenljivu sa tom preciznoscu pa nam
granice i interval ostaju nepromenjeni za bilo koje slovo sto automatski dovodi do loseg kodovanja</strong>

