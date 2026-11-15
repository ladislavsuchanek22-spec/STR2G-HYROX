"""AEO + ukázkový týden zdarma na podstránkách.

- FW_BTN / FW_WEEK: tlačítko „Ukázkový týden zdarma“ na stránkách programů (hero, sekce Týden, závěr).
  Okno a ukládání e-mailů řeší i18n/freeweek.html (stejné jako na hlavní stránce).
- FW_FAQ: otázka „Můžu si program vyzkoušet?“ na každé stránce programu (jde i do FAQPage schema).
- PLAN_FAQ / COACH_FAQ: doplňující otázky na landing pages „tréninkový plán“ a „online coach“
  v jazyce trhu (kdo jsou trenéři, cena, týden zdarma), aby AI měla hotové odpovědi.
Volá se z i18n/programs.py a i18n/pages.py.
"""

FW_BTN = {
    "en": "Free sample week", "cs": "Ukázkový týden zdarma", "sk": "Ukážkový týždeň zdarma",
    "de": "Gratis-Probewoche", "pl": "Darmowy tydzień próbny", "fr": "Semaine d’essai gratuite",
    "es": "Semana de prueba gratis", "it": "Settimana di prova gratis", "nl": "Gratis proefweek",
}

FW_WEEK = {
    "en": "Want the full week with paces and notes? Get it as a free PDF.",
    "cs": "Chceš celý týden i s tempy a poznámkami? Stáhni si ho zdarma v PDF.",
    "sk": "Chceš celý týždeň aj s tempami a poznámkami? Stiahni si ho zdarma v PDF.",
    "de": "Die komplette Woche mit Paces und Hinweisen? Hol sie dir gratis als PDF.",
    "pl": "Chcesz cały tydzień z tempami i uwagami? Pobierz go za darmo w PDF.",
    "fr": "Tu veux la semaine complète avec allures et consignes ? Reçois-la gratuitement en PDF.",
    "es": "¿Quieres la semana completa con ritmos y notas? Descárgala gratis en PDF.",
    "it": "Vuoi la settimana completa con ritmi e note? Scaricala gratis in PDF.",
    "nl": "De volledige week met tempo’s en notities? Download hem gratis als PDF.",
}

FW_FAQ = {
    "en": ("Can I try the program before I buy?", "Yes. Download a free sample week as a PDF on this page. It is one real week of the program with the same sessions, paces and notes you get in the app."),
    "cs": ("Můžu si program vyzkoušet, než ho koupím?", "Ano. Na této stránce si stáhneš ukázkový týden zdarma v PDF. Je to skutečný týden programu: stejné tréninky, tempa a poznámky, jaké dostaneš v aplikaci."),
    "sk": ("Môžem si program vyskúšať, než ho kúpim?", "Áno. Na tejto stránke si stiahneš ukážkový týždeň zdarma v PDF. Je to skutočný týždeň programu: rovnaké tréningy, tempá a poznámky, aké dostaneš v aplikácii."),
    "de": ("Kann ich das Programm vor dem Kauf testen?", "Ja. Auf dieser Seite bekommst du eine Gratis-Probewoche als PDF. Es ist eine echte Woche des Programms mit denselben Einheiten, Paces und Hinweisen wie in der App."),
    "pl": ("Czy mogę przetestować program przed zakupem?", "Tak. Na tej stronie pobierzesz darmowy tydzień próbny w PDF. To prawdziwy tydzień programu: te same treningi, tempa i uwagi, które dostajesz w aplikacji."),
    "fr": ("Puis-je tester le programme avant de l’acheter ?", "Oui. Sur cette page, tu peux télécharger une semaine d’essai gratuite en PDF. C’est une vraie semaine du programme, avec les mêmes séances, allures et consignes que dans l’appli."),
    "es": ("¿Puedo probar el programa antes de comprarlo?", "Sí. En esta página puedes descargar una semana de prueba gratis en PDF. Es una semana real del programa, con las mismas sesiones, ritmos y notas que en la app."),
    "it": ("Posso provare il programma prima di acquistarlo?", "Sì. Da questa pagina scarichi una settimana di prova gratis in PDF. È una vera settimana del programma, con le stesse sessioni, ritmi e note dell’app."),
    "nl": ("Kan ik het programma eerst proberen?", "Ja. Op deze pagina download je een gratis proefweek als PDF. Het is een echte week uit het programma, met dezelfde trainingen, tempo’s en notities als in de app."),
}

# Doplňující FAQ na landing page „tréninkový plán“ (kind=plan)
PLAN_FAQ = {
    "en": [("Is there a free trial?", "Every STR2G program has a free sample week as a PDF: one real week with the same sessions and paces as in the app. You find it on each program page."),
           ("Who writes the STR2G programs?", "Ladislav Suchánek (HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1, Running Coach) and Ria Suchánek Hrušovská (HYROX Performance Coach, mental coach, head coach of HYROX Training Club). Both race HYROX themselves.")],
    "cs": [("Dá se program vyzkoušet zdarma?", "Každý program STR2G má ukázkový týden zdarma v PDF: skutečný týden se stejnými tréninky a tempy jako v aplikaci. Najdeš ho na stránce každého programu."),
           ("Kdo programy STR2G píše?", "Ladislav Suchánek (HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1, Running Coach) a Ria Suchánek Hrušovská (HYROX Performance Coach, mentální koučka, hlavní trenérka HYROX Training Clubu). Oba HYROX sami závodí.")],
    "sk": [("Dá sa program vyskúšať zdarma?", "Každý program STR2G má ukážkový týždeň zdarma v PDF: skutočný týždeň s rovnakými tréningami a tempami ako v aplikácii. Nájdeš ho na stránke každého programu."),
           ("Kto programy STR2G píše?", "Ladislav Suchánek (HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1, Running Coach) a Ria Suchánek Hrušovská (HYROX Performance Coach, mentálna koučka, hlavná trénerka HYROX Training Clubu v Prahe). Obaja HYROX sami pretekajú.")],
    "de": [("Gibt es eine kostenlose Testphase?", "Zu jedem STR2G-Programm gibt es eine Gratis-Probewoche als PDF: eine echte Woche mit denselben Einheiten und Paces wie in der App. Du findest sie auf jeder Programmseite."),
           ("Wer schreibt die STR2G-Programme?", "Ladislav Suchánek (HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1, Running Coach) und Ria Suchánek Hrušovská (HYROX Performance Coach, Mental Coach, Head Coach des HYROX Training Club in Prag). Beide starten selbst bei HYROX.")],
    "pl": [("Czy jest darmowy okres próbny?", "Każdy program STR2G ma darmowy tydzień próbny w PDF: prawdziwy tydzień z tymi samymi treningami i tempami co w aplikacji. Znajdziesz go na stronie każdego programu."),
           ("Kto pisze programy STR2G?", "Ladislav Suchánek (HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1, Running Coach) i Ria Suchánek Hrušovská (HYROX Performance Coach, trenerka mentalna, główna trenerka HYROX Training Club w Pradze). Oboje sami startują w HYROX.")],
    "fr": [("Y a-t-il un essai gratuit ?", "Chaque programme STR2G propose une semaine d’essai gratuite en PDF : une vraie semaine avec les mêmes séances et allures que dans l’appli. Tu la trouves sur la page de chaque programme."),
           ("Qui écrit les programmes STR2G ?", "Ladislav Suchánek (HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1, Running Coach) et Ria Suchánek Hrušovská (HYROX Performance Coach, coach mentale, head coach du HYROX Training Club à Prague). Tous deux courent HYROX.")],
    "es": [("¿Hay una prueba gratuita?", "Cada programa STR2G tiene una semana de prueba gratis en PDF: una semana real con las mismas sesiones y ritmos que en la app. La encuentras en la página de cada programa."),
           ("¿Quién escribe los programas STR2G?", "Ladislav Suchánek (HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1, Running Coach) y Ria Suchánek Hrušovská (HYROX Performance Coach, coach mental, head coach del HYROX Training Club en Praga). Ambos compiten en HYROX.")],
    "it": [("C’è una prova gratuita?", "Ogni programma STR2G ha una settimana di prova gratis in PDF: una vera settimana con le stesse sessioni e ritmi dell’app. La trovi nella pagina di ogni programma."),
           ("Chi scrive i programmi STR2G?", "Ladislav Suchánek (HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1, Running Coach) e Ria Suchánek Hrušovská (HYROX Performance Coach, mental coach, head coach dell’HYROX Training Club a Praga). Entrambi gareggiano in HYROX.")],
    "nl": [("Is er een gratis proefperiode?", "Elk STR2G-programma heeft een gratis proefweek als PDF: een echte week met dezelfde trainingen en tempo’s als in de app. Je vindt hem op de pagina van elk programma."),
           ("Wie schrijft de STR2G-programma’s?", "Ladislav Suchánek (HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1, Running Coach) en Ria Suchánek Hrušovská (HYROX Performance Coach, mental coach, head coach van HYROX Training Club in Praag). Beiden racen zelf HYROX.")],
}

# Doplňující FAQ na landing page „online coach“ (kind=coach)
COACH_FAQ = {
    "en": [("Who are the coaches?", "Ladislav Suchánek – HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1 and Running Coach, 15+ years of coaching. Ria Suchánek Hrušovská – HYROX Performance Coach, mental coach (MSc., Newton University) and head coach of HYROX Training Club. Both race HYROX themselves."),
           ("How much does online HYROX coaching cost?", "The HYROX Individual Program 1:1 costs CZK 3,500 per month (about €145 / £124). Ready-made STR2G programs start at CZK 750 per month.")],
    "cs": [("Kdo jsou trenéři?", "Ladislav Suchánek – HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1 a Running Coach, přes 15 let praxe. Ria Suchánek Hrušovská – HYROX Performance Coach, mentální koučka (MSc., Newton University) a hlavní trenérka HYROX Training Clubu. Oba HYROX sami závodí."),
           ("Kolik stojí online HYROX coaching?", "HYROX Individual Program 1:1 stojí 3 500 Kč měsíčně. Hotové programy STR2G jsou od 750 Kč měsíčně.")],
    "sk": [("Kto sú tréneri?", "Ladislav Suchánek – HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1 a Running Coach, viac ako 15 rokov praxe. Ria Suchánek Hrušovská – HYROX Performance Coach, mentálna koučka (MSc., Newton University) a hlavná trénerka HYROX Training Clubu v Prahe. Obaja HYROX sami pretekajú."),
           ("Koľko stojí online HYROX koučing?", "HYROX Individual Program 1:1 stojí 3 500 Kč mesačne (približne 145 €). Hotové programy STR2G sú od 750 Kč mesačne (približne 31 €).")],
    "de": [("Wer sind die Coaches?", "Ladislav Suchánek – HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1 und Running Coach, über 15 Jahre Erfahrung. Ria Suchánek Hrušovská – HYROX Performance Coach, Mental Coach (MSc., Newton University) und Head Coach des HYROX Training Club in Prag. Beide starten selbst bei HYROX."),
           ("Was kostet HYROX Online-Coaching?", "Das HYROX Individual Program 1:1 kostet 3.500 CZK pro Monat (ca. 145 €). Fertige STR2G-Programme gibt es ab 750 CZK pro Monat (ca. 31 €).")],
    "pl": [("Kim są trenerzy?", "Ladislav Suchánek – HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1 i Running Coach, ponad 15 lat doświadczenia. Ria Suchánek Hrušovská – HYROX Performance Coach, trenerka mentalna (MSc., Newton University) i główna trenerka HYROX Training Club w Pradze. Oboje sami startują w HYROX."),
           ("Ile kosztuje coaching HYROX online?", "HYROX Individual Program 1:1 kosztuje 3500 CZK miesięcznie (ok. 624 zł). Gotowe programy STR2G są od 750 CZK miesięcznie (ok. 134 zł).")],
    "fr": [("Qui sont les coachs ?", "Ladislav Suchánek – HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1 et Running Coach, plus de 15 ans d’expérience. Ria Suchánek Hrušovská – HYROX Performance Coach, coach mentale (MSc., Newton University) et head coach du HYROX Training Club à Prague. Tous deux courent HYROX."),
           ("Combien coûte le coaching HYROX en ligne ?", "Le HYROX Individual Program 1:1 coûte 3 500 CZK par mois (environ 145 €). Les programmes STR2G prêts à l’emploi commencent à 750 CZK par mois (environ 31 €).")],
    "es": [("¿Quiénes son los entrenadores?", "Ladislav Suchánek – HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1 y Running Coach, más de 15 años de experiencia. Ria Suchánek Hrušovská – HYROX Performance Coach, coach mental (MSc., Newton University) y head coach del HYROX Training Club en Praga. Ambos compiten en HYROX."),
           ("¿Cuánto cuesta el coaching HYROX online?", "El HYROX Individual Program 1:1 cuesta 3.500 CZK al mes (unos 145 €). Los programas STR2G ya hechos empiezan en 750 CZK al mes (unos 31 €).")],
    "it": [("Chi sono i coach?", "Ladislav Suchánek – HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1 e Running Coach, oltre 15 anni di esperienza. Ria Suchánek Hrušovská – HYROX Performance Coach, mental coach (MSc., Newton University) e head coach dell’HYROX Training Club a Praga. Entrambi gareggiano in HYROX."),
           ("Quanto costa il coaching HYROX online?", "L’HYROX Individual Program 1:1 costa 3.500 CZK al mese (circa 145 €). I programmi STR2G pronti partono da 750 CZK al mese (circa 31 €).")],
    "nl": [("Wie zijn de coaches?", "Ladislav Suchánek – HYROX Performance Coach L1, CrossFit L1, OPEX CCP, Precision Nutrition L1 en Running Coach, meer dan 15 jaar ervaring. Ria Suchánek Hrušovská – HYROX Performance Coach, mental coach (MSc., Newton University) en head coach van HYROX Training Club in Praag. Beiden racen zelf HYROX."),
           ("Wat kost online HYROX-coaching?", "Het HYROX Individual Program 1:1 kost 3.500 CZK per maand (ca. € 145). Kant-en-klare STR2G-programma’s beginnen bij 750 CZK per maand (ca. € 31).")],
}


def fw_button(lang, pid, cls="btn btn-ghost"):
    return f'<button type="button" class="{cls}" data-fw-cta="{pid}">{FW_BTN.get(lang, FW_BTN["en"])}</button>'


def extend_landing(T):
    """Přidá AEO otázky do FAQ landing pages (jen jednou)."""
    for lang, t in T.items():
        for kind, extra in (("plan", PLAN_FAQ), ("coach", COACH_FAQ)):
            faq = t[kind]["faq"]
            have = {q for q, _ in faq}
            for q, a in extra.get(lang, []):
                if q not in have:
                    faq.append((q, a))


# Recenze klientů (originál z SMS, se souhlasem; podpis zkrácený). Na stránce programu: originál + překlad do jazyka stránky.
REVIEWS = {
    "advanced": dict(name="Max S.", lang="de", text="Endlich ein Trainingsprogramm, das wirklich Sinn macht! Keine zufälligen Workouts, sondern ein durchdachtes System, bei dem jede Trainingseinheit ein klares Ziel hat. In 12 Wochen konnte ich meine Ausdauer, Kraft und die Fähigkeit, auch unter hoher Belastung das Tempo zu halten, deutlich verbessern. Besonders gut gefällt mir die Kombination aus Lauftraining und HYROX-spezifischen Einheiten. Definitiv die beste Vorbereitung, die ich bisher gemacht habe.", tr={
        "en": "Finally a training program that really makes sense! No random workouts, but a well-thought-out system where every session has a clear goal. In 12 weeks I clearly improved my endurance, strength and ability to hold my pace under heavy load. I especially like the combination of running and HYROX-specific sessions. Definitely the best preparation I have done so far.",
        "cs": "Konečně tréninkový program, který opravdu dává smysl! Žádné náhodné workouty, ale promyšlený systém, kde má každý trénink jasný cíl. Za 12 týdnů jsem výrazně zlepšil vytrvalost, sílu a schopnost držet tempo i pod velkou zátěží. Nejvíc se mi líbí kombinace běhu a HYROX tréninků. Rozhodně nejlepší příprava, jakou jsem zatím absolvoval.",
        "sk": "Konečne tréningový program, ktorý naozaj dáva zmysel! Žiadne náhodné workouty, ale premyslený systém, kde má každý tréning jasný cieľ. Za 12 týždňov som výrazne zlepšil vytrvalosť, silu a schopnosť držať tempo aj pod veľkou záťažou. Najviac sa mi páči kombinácia behu a HYROX tréningov. Určite najlepšia príprava, akú som zatiaľ absolvoval.",
        "pl": "Wreszcie program treningowy, który naprawdę ma sens! Żadnych przypadkowych workoutów, tylko przemyślany system, w którym każdy trening ma jasny cel. W 12 tygodni wyraźnie poprawiłem wytrzymałość, siłę i umiejętność trzymania tempa pod dużym obciążeniem. Najbardziej podoba mi się połączenie biegania z treningami typowo pod HYROX. Zdecydowanie najlepsze przygotowanie, jakie do tej pory zrobiłem.",
        "fr": "Enfin un programme d’entraînement qui a vraiment du sens ! Pas de workouts au hasard, mais un système réfléchi où chaque séance a un objectif clair. En 12 semaines, j’ai nettement amélioré mon endurance, ma force et ma capacité à tenir l’allure sous forte charge. J’aime particulièrement la combinaison de course et de séances spécifiques HYROX. Sans doute la meilleure préparation que j’aie faite jusqu’ici.",
        "es": "¡Por fin un programa de entrenamiento que tiene sentido de verdad! Nada de workouts al azar, sino un sistema bien pensado en el que cada sesión tiene un objetivo claro. En 12 semanas mejoré claramente mi resistencia, mi fuerza y mi capacidad de mantener el ritmo bajo carga alta. Me gusta especialmente la combinación de carrera y sesiones específicas de HYROX. Sin duda la mejor preparación que he hecho hasta ahora.",
        "it": "Finalmente un programma di allenamento che ha davvero senso! Niente workout a caso, ma un sistema ben pensato in cui ogni sessione ha un obiettivo chiaro. In 12 settimane ho migliorato nettamente resistenza, forza e capacità di tenere il ritmo sotto carico elevato. Mi piace soprattutto la combinazione di corsa e sessioni specifiche HYROX. Sicuramente la migliore preparazione che abbia fatto finora.",
        "nl": "Eindelijk een trainingsprogramma dat echt klopt! Geen willekeurige workouts, maar een doordacht systeem waarin elke training een duidelijk doel heeft. In 12 weken heb ik mijn uithouding, kracht en het vermogen om onder zware belasting mijn tempo vast te houden duidelijk verbeterd. Vooral de combinatie van hardlopen en HYROX-specifieke trainingen vind ik sterk. Absoluut de beste voorbereiding die ik tot nu toe heb gedaan.",
    }),
    "running": dict(name="Jakub K.", lang="pl", text="Zawsze myślałem, że całkiem dobrze radzę sobie z bieganiem, ale HYROX pokazał mi, że mam jeszcze sporo do poprawy. Ten program całkowicie zmienił moje podejście do treningu biegowego. Nauczyłem się lepiej kontrolować tempo, intensywność i przede wszystkim efektywnie biegać nawet na zmęczonych nogach. Efekt? Szybsze bieganie, niższe tętno przy tym samym tempie i znacznie większa pewność siebie podczas zawodów.", tr={
        "en": "I always thought I was pretty good at running, but HYROX showed me I still had a lot to improve. This program completely changed how I approach run training. I learned to control pace and intensity better and, above all, to run efficiently even on tired legs. The result? Faster running, a lower heart rate at the same pace and much more confidence on race day.",
        "cs": "Vždycky jsem si myslel, že běh zvládám docela dobře, ale HYROX mi ukázal, že mám pořád co zlepšovat. Tenhle program úplně změnil můj přístup k běžeckému tréninku. Naučil jsem se líp kontrolovat tempo a intenzitu a hlavně efektivně běhat i na unavených nohách. Výsledek? Rychlejší běh, nižší tep při stejném tempu a mnohem větší jistota na závodech.",
        "sk": "Vždy som si myslel, že beh zvládam celkom dobre, ale HYROX mi ukázal, že mám stále čo zlepšovať. Tento program úplne zmenil môj prístup k bežeckému tréningu. Naučil som sa lepšie kontrolovať tempo a intenzitu a hlavne efektívne behať aj na unavených nohách. Výsledok? Rýchlejší beh, nižší tep pri rovnakom tempe a oveľa väčšia istota na pretekoch.",
        "de": "Ich dachte immer, ich komme mit dem Laufen ganz gut klar, aber HYROX hat mir gezeigt, dass ich noch einiges verbessern kann. Dieses Programm hat meinen Zugang zum Lauftraining komplett verändert. Ich habe gelernt, Tempo und Intensität besser zu steuern und vor allem auch mit müden Beinen effizient zu laufen. Das Ergebnis? Schnelleres Laufen, ein niedrigerer Puls bei gleichem Tempo und deutlich mehr Selbstvertrauen im Wettkampf.",
        "fr": "J’ai toujours pensé que je me débrouillais plutôt bien en course, mais HYROX m’a montré que j’avais encore beaucoup à améliorer. Ce programme a complètement changé ma façon d’aborder l’entraînement de course. J’ai appris à mieux gérer l’allure et l’intensité et surtout à courir efficacement même avec les jambes fatiguées. Résultat ? Une course plus rapide, une fréquence cardiaque plus basse à allure égale et beaucoup plus de confiance en compétition.",
        "es": "Siempre pensé que se me daba bastante bien correr, pero HYROX me demostró que aún tenía mucho que mejorar. Este programa cambió por completo mi forma de entrenar la carrera. Aprendí a controlar mejor el ritmo y la intensidad y, sobre todo, a correr de forma eficiente incluso con las piernas cansadas. ¿El resultado? Correr más rápido, pulsaciones más bajas al mismo ritmo y mucha más confianza en competición.",
        "it": "Ho sempre pensato di cavarmela abbastanza bene nella corsa, ma HYROX mi ha mostrato che avevo ancora parecchio da migliorare. Questo programma ha cambiato completamente il mio approccio all’allenamento di corsa. Ho imparato a controllare meglio ritmo e intensità e soprattutto a correre in modo efficiente anche con le gambe stanche. Il risultato? Corsa più veloce, frequenza cardiaca più bassa allo stesso ritmo e molta più sicurezza in gara.",
        "nl": "Ik dacht altijd dat ik best goed kon hardlopen, maar HYROX liet me zien dat er nog veel te verbeteren viel. Dit programma heeft mijn aanpak van looptraining volledig veranderd. Ik heb geleerd tempo en intensiteit beter te sturen en vooral efficiënt te lopen, ook met vermoeide benen. Het resultaat? Sneller lopen, een lagere hartslag bij hetzelfde tempo en veel meer zelfvertrouwen tijdens wedstrijden.",
    }),
    "doubles": dict(name="Anna N.", lang="pl", text="Osiem tygodni przed zawodami potrzebowałam dokładnego planu, żeby wiedzieć, nad czym pracować i jak osiągnąć najlepszą formę na dzień startu. Program świetnie przeprowadził mnie przez końcowy etap przygotowań. Dobrze dobrane intensywności, symulacje zawodów i stopniowe zmniejszanie objętości treningowego przed startem. Na linii startu czułam się przygotowana, wypoczęta i miałam jasną strategię. Efekt? Nowy rekord życiowy i w końcu zawody bez zbyt mocnego początku.", tr={
        "en": "Eight weeks before the race I needed a precise plan so I knew what to work on and how to peak on race day. The program took me through the final phase of preparation really well. Well-chosen intensities, race simulations and a gradual reduction of training volume before the start. On the start line I felt prepared, rested and had a clear strategy. The result? A new personal best and finally a race without going out too hard.",
        "cs": "Osm týdnů před závodem jsem potřebovala přesný plán, abych věděla, na čem pracovat a jak být v den startu v nejlepší formě. Program mě skvěle provedl závěrečnou fází přípravy. Dobře nastavené intenzity, simulace závodu a postupné snižování objemu před startem. Na startovní čáře jsem se cítila připravená, odpočatá a měla jsem jasnou strategii. Výsledek? Nový osobní rekord a konečně závod bez přepáleného začátku.",
        "sk": "Osem týždňov pred pretekmi som potrebovala presný plán, aby som vedela, na čom pracovať a ako byť v deň štartu v najlepšej forme. Program ma skvele previedol záverečnou fázou prípravy. Dobre nastavené intenzity, simulácie pretekov a postupné znižovanie objemu pred štartom. Na štartovej čiare som sa cítila pripravená, oddýchnutá a mala som jasnú stratégiu. Výsledok? Nový osobný rekord a konečne preteky bez prepáleného začiatku.",
        "de": "Acht Wochen vor dem Wettkampf brauchte ich einen genauen Plan, um zu wissen, woran ich arbeiten muss und wie ich am Renntag in Bestform bin. Das Programm hat mich super durch die letzte Vorbereitungsphase geführt. Gut gewählte Intensitäten, Wettkampfsimulationen und eine schrittweise Reduzierung des Trainingsumfangs vor dem Start. An der Startlinie fühlte ich mich vorbereitet, erholt und hatte eine klare Strategie. Das Ergebnis? Eine neue persönliche Bestzeit und endlich ein Rennen ohne zu schnellen Start.",
        "fr": "Huit semaines avant la course, j’avais besoin d’un plan précis pour savoir sur quoi travailler et comment être au top le jour J. Le programme m’a parfaitement guidée dans la dernière phase de préparation. Des intensités bien choisies, des simulations de course et une baisse progressive du volume avant le départ. Sur la ligne de départ, je me sentais prête, reposée et j’avais une stratégie claire. Résultat ? Un nouveau record personnel et enfin une course sans départ trop rapide.",
        "es": "Ocho semanas antes de la competición necesitaba un plan preciso para saber en qué trabajar y cómo llegar en mi mejor forma al día de la carrera. El programa me guio de maravilla en la fase final de la preparación. Intensidades bien elegidas, simulaciones de carrera y una reducción gradual del volumen antes de la salida. En la línea de salida me sentía preparada, descansada y con una estrategia clara. ¿El resultado? Nueva mejor marca personal y, por fin, una carrera sin salir demasiado fuerte.",
        "it": "Otto settimane prima della gara avevo bisogno di un piano preciso per sapere su cosa lavorare e come arrivare in forma al giorno della gara. Il programma mi ha guidata benissimo nella fase finale della preparazione. Intensità ben scelte, simulazioni di gara e una riduzione graduale del volume prima della partenza. Sulla linea di partenza mi sentivo pronta, riposata e con una strategia chiara. Il risultato? Un nuovo record personale e finalmente una gara senza partire troppo forte.",
        "nl": "Acht weken voor de wedstrijd had ik een precies plan nodig, zodat ik wist waaraan ik moest werken en hoe ik op de wedstrijddag in topvorm zou zijn. Het programma heeft me uitstekend door de laatste fase van de voorbereiding geleid. Goed gekozen intensiteiten, wedstrijdsimulaties en een geleidelijke afbouw van het trainingsvolume voor de start. Aan de start voelde ik me voorbereid, uitgerust en had ik een duidelijke strategie. Het resultaat? Een nieuw persoonlijk record en eindelijk een wedstrijd zonder te snelle start.",
    }),
}

REV_H = {"en": ("What athletes", "say."), "cs": ("Co říkají", "sportovci."), "sk": ("Čo hovoria", "športovci."),
         "de": ("Was Athleten", "sagen."), "pl": ("Co mówią", "zawodnicy."), "fr": ("Ce qu’en disent", "les athlètes."),
         "es": ("Lo que dicen", "los atletas."), "it": ("Cosa dicono", "gli atleti."), "nl": ("Wat atleten", "zeggen.")}
REV_TR = {"en": "Translation", "cs": "Překlad", "sk": "Preklad", "de": "Übersetzung", "pl": "Tłumaczenie",
          "fr": "Traduction", "es": "Traducción", "it": "Traduzione", "nl": "Vertaling"}
REV_ORIG = {"de": {"en": "original in German", "cs": "originál v němčině", "sk": "originál v nemčine", "pl": "oryginał po niemiecku", "fr": "original en allemand", "es": "original en alemán", "it": "originale in tedesco", "nl": "origineel in het Duits"},
            "pl": {"en": "original in Polish", "cs": "originál v polštině", "sk": "originál v poľštine", "de": "Original auf Polnisch", "fr": "original en polonais", "es": "original en polaco", "it": "originale in polacco", "nl": "origineel in het Pools"}}


def review_section(lang, pid, pname, two, escape):
    r = REVIEWS.get(pid)
    if not r:
        return ""
    if lang == r["lang"]:
        tr = ""
        note = ""
    else:
        tr = f'<p class="rev-tr"><span>{REV_TR[lang]}:</span> {escape(r["tr"][lang])}</p>'
        note = f' · {REV_ORIG[r["lang"]][lang]}'
    return f'''
<section id="reviews">
  <div class="wrap">
    <div class="shead"><p class="eyebrow">{escape(pname)}</p><h2 class="display"><span>{two(REV_H[lang])}</span></h2></div>
    <figure class="q rev"><div class="mark">“</div><blockquote lang="{r["lang"]}">{escape(r["text"])}</blockquote>{tr}<figcaption class="who"><b>{escape(r["name"])}</b> · {escape(pname)}{note}</figcaption></figure>
  </div>
</section>
'''


def review_ld(pid):
    r = REVIEWS.get(pid)
    if not r:
        return None
    return [{"@type": "Review", "author": {"@type": "Person", "name": r["name"]}, "reviewBody": r["text"], "inLanguage": r["lang"]}]
