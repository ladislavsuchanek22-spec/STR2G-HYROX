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
