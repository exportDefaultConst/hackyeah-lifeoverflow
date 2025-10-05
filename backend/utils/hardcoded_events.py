"""
Hardcoded events - predefiniowane wydarzenia życiowe
"""

# Porady emerytalne ZUS - pokazywane losowo
PENSION_TIPS = [
    {
        'title': '💼 Wiek emerytalny',
        'text': 'Kobiety: 60 lat, Mężczyźni: 65 lat (wymaga min. 20/25 lat składek). Im dłużej pracujesz, tym wyższa emerytura!'
    },
    {
        'title': '💰 Składka emerytalna',
        'text': '19,52% wynagrodzenia brutto trafia na Twoje indywidualne konto w ZUS. To Twoja przyszła emerytura!'
    },
    {
        'title': '� Rodzaje umów a ZUS',
        'text': 'UoP = 100% składek (19.52%). Zlecenie = ~50% składek. B2B = minimalne składki! Wybór umowy wpływa na emeryturę!'
    },
    {
        'title': '�📈 Kapitał początkowy',
        'text': 'Składki sprzed 1999 r. są przeliczane i doliczane do kapitału. Nie tracisz tego co już zapłaciłeś!'
    },
    {
        'title': '⏱️ Dalsze zatrudnienie',
        'text': 'Możesz pracować po osiągnięciu wieku emerytalnego i zwiększać kapitał. Każdy miesiąc pracy to wyższa emerytura!'
    },
    {
        'title': '⚠️ Wzór na emeryturę',
        'text': 'Emerytura = kapitał ÷ średnie dalsze trwanie życia. Im dłużej odkładasz emeryturę, tym wyższa będzie!'
    },
    {
        'title': '🏢 Umowa o pracę (UoP)',
        'text': 'Umowa o pracę daje NAJWYŻSZE składki ZUS (pełne 19.52%). Pracodawca automatycznie odprowadza za Ciebie!'
    },
    {
        'title': '💡 Dodatkowe oszczędzanie',
        'text': 'PPK i IKE to dodatkowe sposoby oszczędzania na emeryturę z korzyściami podatkowymi. Warto rozważyć!'
    },
    {
        'title': '⚡ B2B i ZUS',
        'text': 'Działalność gospodarcza (B2B) pozwala płacić MINIMALNE składki ZUS. Większe zarobki teraz, ale niższa emerytura!'
    }
]

# Wydarzenia stałe - dostępne codziennie
DAILY_EVENTS = {
    'meet_friends': {
        'event_name': '👥 Spotkanie ze znajomymi',
        'description': 'Możesz spotkać się ze znajomymi. To poprawi Twoje samopoczucie, ale stracisz trochę czasu i pieniędzy.',
        'choices': [
            {
                'text': 'Spotkaj się (2h, 150 zł)',
                'impacts': {
                    'happiness': 1,
                    'social_connections': 1,
                    'emotional_wellbeing': 1,
                    'savings': -150,
                    'free_time': -1,
                    'stress_level': -1
                },
                'tip': '💡 Relacje społeczne są ważne dla zdrowia psychicznego i jakości życia!'
            },
            {
                'text': 'Zostań w domu',
                'impacts': {
                    'savings': 50,
                    'free_time': 1
                },
                'tip': '💡 Oszczędzanie to dobrze, ale nie zapominaj o relacjach!'
            }
        ]
    },
    'go_out_eat': {
        'event_name': '🍽️ Wyjście do restauracji',
        'description': 'Możesz pójść na kolację do restauracji. Dobry posiłek i miła atmosfera poprawią nastrój.',
        'choices': [
            {
                'text': 'Droga restauracja (300 zł)',
                'impacts': {
                    'happiness': 2,
                    'emotional_wellbeing': 1,
                    'savings': -300,
                    'free_time': -2
                },
                'tip': '💡 Pozwalaj sobie czasem na przyjemności, ale pamiętaj o budżecie!'
            },
            {
                'text': 'Tania knajpka (80 zł)',
                'impacts': {
                    'happiness': 1,
                    'savings': -80,
                    'free_time': -1
                },
                'tip': '💡 Można dobrze się bawić nie wydając fortuny!'
            },
            {
                'text': 'Gotuj w domu',
                'impacts': {
                    'savings': 30,
                    'health': 1
                },
                'tip': '💡 Gotowanie w domu jest zdrowsze i tańsze!'
            }
        ]
    },
    'exercise': {
        'event_name': '🏃 Aktywność fizyczna',
        'description': 'Możesz poświęcić czas na sport. To poprawi Twoje zdrowie.',
        'choices': [
            {
                'text': 'Siłownia (50 zł)',
                'impacts': {
                    'health': 1,
                    'physical_health': 1,
                    'stress_level': -1,
                    'savings': -50,
                    'free_time': -2
                },
                'tip': '💡 Regularna aktywność fizyczna zwiększa długość życia!'
            },
            {
                'text': 'Pobiegaj w parku (0 zł)',
                'impacts': {
                    'health': 1,
                    'stress_level': -1,
                    'free_time': -1
                },
                'tip': '💡 Sport nie musi być drogi!'
            }
        ]
    },
    'hobby_time': {
        'event_name': '🎨 Hobby',
        'description': 'Możesz poświęcić czas na swoje hobby. Relaks i przyjemność.',
        'choices': [
            {
                'text': 'Poświęć czas (2h)',
                'impacts': {
                    'happiness': 1,
                    'stress_level': -2,
                    'free_time': -2,
                    'life_purpose': 1
                },
                'tip': '💡 Hobby pomaga w redukcji stresu i poprawia jakość życia!'
            },
            {
                'text': 'Nie mam czasu',
                'impacts': {
                    'stress_level': 1
                },
                'tip': '💡 Każdy potrzebuje czasu dla siebie!'
            }
        ]
    },
    'volunteer_work': {
        'event_name': '🤝 Wolontariat',
        'description': 'Możesz pomóc w lokalnej organizacji charytatywnej.',
        'choices': [
            {
                'text': 'Pomagaj (4h)',
                'impacts': {
                    'happiness': 2,
                    'life_purpose': 2,
                    'community_involvement': 2,
                    'social_connections': 1,
                    'free_time': -3
                },
                'tip': '💡 Pomaganie innym daje poczucie sensu życia!'
            },
            {
                'text': 'Nie dzisiaj',
                'impacts': {},
                'tip': '💡 Wolontariat to świetny sposób na poznanie ludzi!'
            }
        ]
    },
    'gaming_session': {
        'event_name': '🎮 Gry komputerowe',
        'description': 'Możesz zagrać w gry. Relaks, ale zabiera czas.',
        'choices': [
            {
                'text': 'Zagraj (3h)',
                'impacts': {
                    'happiness': 1,
                    'stress_level': -1,
                    'free_time': -3,
                    'social_connections': -1
                },
                'tip': '💡 Gry to dobry relaks, ale w umiarkowanych ilościach!'
            },
            {
                'text': 'Rób coś produktywnego',
                'impacts': {
                    'personal_growth': 1
                },
                'tip': '💡 Czasem lepiej wykorzystać czas na rozwój!'
            }
        ]
    },
    'side_hustle': {
        'event_name': '💼 Dorabianie',
        'description': 'Możesz dorobić na boku - dodatkowa praca wieczorami lub w weekendy.',
        'choices': [
            {
                'text': 'Dorabiaj (800 zł, -wolny czas)',
                'impacts': {
                    'savings': 800,
                    'free_time': -3,
                    'stress_level': 2,
                    'mental_health': -1,
                    'work_life_balance': -2,
                    'health': -1
                },
                'tip': '💡 Dorabianie zwiększa dochody, ale odbiera czas i energię!'
            },
            {
                'text': 'Odpuść sobie',
                'impacts': {
                    'free_time': 1,
                    'stress_level': -1
                },
                'tip': '💡 Czasem odpoczynek jest cenniejszy niż dodatkowe pieniądze!'
            }
        ]
    },
    'job_search': {
        'event_name': '🔍 Aktywne poszukiwanie pracy',
        'description': 'Możesz aktywnie szukać pracy - wysyłanie CV, rozmowy kwalifikacyjne, networking.',
        'choices': [
            {
                'text': 'Szukaj intensywnie',
                'impacts': {
                    'mental_health': -2,
                    'stress_level': 3,
                    'free_time': -3,
                    'self_esteem': -1,
                    'savings': -200,  # Koszty dojazdu na rozmowy
                    'actively_job_searching': True  # Flaga - zwiększona szansa na pracę
                },
                'consequence': 'Zwiększasz szanse na ofertę pracy w następnym wydarzeniu!',
                'tip': '💡 Aktywne poszukiwanie pracy to stres, ale zwiększa szanse na znalezienie zatrudnienia!'
            },
            {
                'text': 'Zaczekaj na lepszy moment',
                'impacts': {
                    'stress_level': 1,
                    'actively_job_searching': False
                },
                'tip': '💡 Brak aktywności nie pomoże znaleźć pracy!'
            }
        ]
    },
    'online_course': {
        'event_name': '💻 Kurs online',
        'description': 'Możesz zapisać się na kurs online aby podnieść swoje kwalifikacje.',
        'choices': [
            {
                'text': 'Zapisz się (400 zł, wymaga czasu)',
                'impacts': {
                    'savings': -400,
                    'personal_growth': 2,
                    'career_satisfaction': 1,
                    'free_time': -2,
                    'self_esteem': 1
                },
                'tip': '💡 Inwestycja w rozwój to inwestycja w przyszłość!'
            },
            {
                'text': 'Za drogie',
                'impacts': {
                    'savings': 50
                },
                'tip': '💡 Bez rozwoju trudniej znaleźć lepszą pracę!'
            }
        ]
    },
    'freelance_gig': {
        'event_name': '🖥️ Zlecenie freelance',
        'description': 'Dostałeś propozycję jednorazowego zlecenia freelance. Można zarobić, ale wymaga czasu.',
        'choices': [
            {
                'text': 'Przyjmij (1200 zł, wieczory)',
                'impacts': {
                    'savings': 1200,
                    'free_time': -4,
                    'stress_level': 2,
                    'work_life_balance': -1,
                    'personal_growth': 1
                },
                'tip': '💡 Freelance to dobry sposób na dodatkowy zarobek!'
            },
            {
                'text': 'Odmów - potrzebuję odpoczynku',
                'impacts': {
                    'stress_level': -1,
                    'mental_health': 1
                },
                'tip': '💡 Dbanie o siebie to priorytet!'
            }
        ]
    },
    'meditation_yoga': {
        'event_name': '🧘 Medytacja/Joga',
        'description': 'Możesz zacząć praktykować medytację lub jogę. Dobry sposób na redukcję stresu.',
        'choices': [
            {
                'text': 'Zapisz się na zajęcia (250 zł/mies)',
                'impacts': {
                    'savings': -250,
                    'mental_health': 2,
                    'stress_level': -3,
                    'emotional_wellbeing': 2,
                    'health': 1,
                    'free_time': -2
                },
                'tip': '💡 Regularna praktyka mindfulness znacząco obniża stres!'
            },
            {
                'text': 'Praktykuj sam w domu (YT)',
                'impacts': {
                    'mental_health': 1,
                    'stress_level': -1,
                    'free_time': -1
                },
                'tip': '💡 Nawet 10 minut dziennie robi różnicę!'
            },
            {
                'text': 'Nie dla mnie',
                'impacts': {},
                'tip': '💡 Każdy sposób na stres jest dobry - znajdź swój!'
            }
        ]
    },
    'books_reading': {
        'event_name': '📚 Czytanie książek',
        'description': 'Możesz poświęcić czas na czytanie. Rozwój osobisty i relaks.',
        'choices': [
            {
                'text': 'Kup i czytaj (100 zł)',
                'impacts': {
                    'savings': -100,
                    'personal_growth': 2,
                    'stress_level': -2,
                    'life_purpose': 1,
                    'free_time': -2
                },
                'tip': '💡 Czytanie rozwija umysł i pomaga w karierze!'
            },
            {
                'text': 'Biblioteka (0 zł)',
                'impacts': {
                    'personal_growth': 1,
                    'stress_level': -1,
                    'free_time': -1
                },
                'tip': '💡 Biblioteka to skarb - korzystaj!'
            },
            {
                'text': 'Nie mam czasu',
                'impacts': {
                    'stress_level': 1
                },
                'tip': '💡 15 minut dziennie to 90 godzin rocznie!'
            }
        ]
    },
    'networking_event': {
        'event_name': '🤝 Event networkingowy',
        'description': 'Możesz pójść na wydarzenie networkingowe. Poznasz ludzi z branży.',
        'choices': [
            {
                'text': 'Weź udział (150 zł)',
                'impacts': {
                    'savings': -150,
                    'social_connections': 2,
                    'career_satisfaction': 1,
                    'self_esteem': 1,
                    'free_time': -2
                },
                'tip': '💡 Networking to klucz do nowych możliwości zawodowych!'
            },
            {
                'text': 'Zostań w domu',
                'impacts': {
                    'social_connections': -1
                },
                'tip': '💡 "Znajomości" to często ważniejsze niż CV!'
            }
        ]
    },
    'declutter_sell': {
        'event_name': '🏷️ Sprzedaż rzeczy',
        'description': 'Możesz posprzątać i sprzedać niepotrzebne rzeczy na OLX/Vinted.',
        'choices': [
            {
                'text': 'Uporządkuj i sprzedaj (300 zł)',
                'impacts': {
                    'savings': 300,
                    'mental_health': 1,
                    'stress_level': -1,
                    'happiness': 1,
                    'free_time': -2
                },
                'tip': '💡 Minimalizm i dodatkowa gotówka - win-win!'
            },
            {
                'text': 'Zostaw jak jest',
                'impacts': {},
                'tip': '💡 Nieużywane rzeczy to zamrożone pieniądze!'
            }
        ]
    }
}
EDUCATION_EVENTS = {
    'technical_school': {
        'event_key': 'technical_school',
        'requires': ['podstawowe'],
        'excludes': ['zawodowe'],
        'age_range': (16, 30),
        'show_once': True,  # Pokazuj tylko raz
        'event_name': '🔧 Szkoła zawodowa',
        'description': 'Możesz zdobyć wykształcenie zawodowe. To 3 lata nauki.',
        'choices': [
            {
                'text': 'Zapisz się (3 lata, 8000 zł)',
                'impacts': {
                    'education_level': 'zawodowe',
                    'student': True,
                    'savings': -8000,
                    'personal_growth': 2,
                    'monthly_costs': 500  # Koszty nauki
                },
                'add_to_completed': 'zawodowe',
                'skip_years': 2,  # Pomiń 2 lata
                'tip': '💡 Wykształcenie zawodowe daje konkretne umiejętności!'
            },
            {
                'text': 'Nie, wolę pracować',
                'impacts': {'student': False},
                'tip': '💡 Bez wykształcenia trudniej znaleźć dobrą pracę.'
            }
        ]
    },
    'university': {
        'event_key': 'university',
        'requires': ['średnie', 'zawodowe'],
        'excludes': ['wyższe'],
        'age_range': (18, 35),
        'show_once': True,  # Pokazuj tylko raz
        'event_name': '🎓 Studia wyższe',
        'description': 'Możesz pójść na studia. To 5 lat i duże koszty.',
        'choices': [
            {
                'text': 'Studia (5 lat, 20000 zł)',
                'impacts': {
                    'education_level': 'wyższe',
                    'student': True,
                    'savings': -20000,
                    'personal_growth': 3,
                    'free_time': -3,
                    'monthly_costs': 800  # Koszty akademika, materiałów
                },
                'add_to_completed': 'wyższe',
                'skip_years': 5,  # Pomiń 5 lat
                'tip': '💡 Studia zwiększają szanse na lepszą pracę o 50%!'
            },
            {
                'text': 'Nie chcę studiować',
                'impacts': {'student': False},
                'tip': '💡 Bez studiów możesz mieć trudniej.'
            }
        ]
    }
}
JOB_EVENTS = {
    'first_job': {
        'event_key': 'first_job',
        'requires_no_job': True,
        'age_range': (18, 30),
        'show_once': True,  # Pokazuj tylko raz
        'higher_chance_when_unemployed': True,  # Większa szansa gdy bezrobotny
        'event_name': '💼 Pierwsza praca',
        'description': 'Dostałeś ofertę pracy! Wybierz rodzaj umowy.',
        'choices': [
            {
                'text': 'Umowa o pracę (4500 zł/mc)',
                'impacts': {
                    'type_employment': 'UoP',
                    'work': 'pracownik',
                    'income': 4500,
                    'has_job': True,
                    'financial_security': 3,
                    'free_time': -3
                },
                'tip': '💡 UoP daje stabilność i PEŁNE składki ZUS (19.52%)! Najlepsza emerytura.'
            },
            {
                'text': 'Zlecenie (4000 zł/mc)',
                'impacts': {
                    'type_employment': 'zlecenie',
                    'work': 'zleceniobiorca',
                    'income': 4000,
                    'has_job': True,
                    'free_time': -2
                },
                'tip': '💡 Zlecenie = elastyczność, ale NIŻSZE składki ZUS (50%). Niższa emerytura!'
            },
            {
                'text': 'B2B (6000 zł/mc, start 5000 zł)',
                'impacts': {
                    'type_employment': 'B2B',
                    'work': 'przedsiębiorca',
                    'income': 6000,
                    'has_job': True,
                    'savings': -5000,
                    'stress_level': 2,
                    'free_time': -4
                },
                'tip': '💡 B2B może być dochodowe, ale ZUS MINIMALNY lub opcjonalny. Zadbaj o emeryturę sam!'
            }
        ]
    },
    'job_offer': {
        'event_key': 'job_offer',
        'requires_no_job': True,
        'age_range': (20, 65),
        'higher_chance_when_unemployed': True,  # Większa szansa gdy bezrobotny
        'event_name': '💼 Oferta pracy',
        'description': 'Podczas aktywnego poszukiwania dostałeś ofertę pracy! Osoby bez pracy mają większe szanse na znalezienie zatrudnienia.',
        'choices': [
            {
                'text': 'Umowa o pracę (5000 zł/mc)',
                'impacts': {
                    'type_employment': 'UoP',
                    'work': 'pracownik',
                    'income': 5000,
                    'has_job': True,
                    'financial_security': 3,
                    'stress_level': -2,
                    'free_time': -3
                },
                'tip': '💡 Aktywne poszukiwanie się opłaciło! UoP = PEŁNE składki ZUS na emeryturę!'
            },
            {
                'text': 'Zlecenie (4500 zł/mc)',
                'impacts': {
                    'type_employment': 'zlecenie',
                    'work': 'zleceniobiorca',
                    'income': 4500,
                    'has_job': True,
                    'stress_level': -1,
                    'free_time': -2
                },
                'tip': '💡 Zlecenie to dobry start! Ale pamiętaj - POŁOWA składek ZUS vs UoP.'
            },
            {
                'text': 'B2B (7000 zł/mc, start 3000 zł)',
                'impacts': {
                    'type_employment': 'B2B',
                    'work': 'przedsiębiorca',
                    'income': 7000,
                    'has_job': True,
                    'savings': -3000,
                    'stress_level': 1,
                    'free_time': -4
                },
                'tip': '💡 B2B = wyższe zarobki, ale MINIMALNE składki ZUS! Musisz sam dbać o emeryturę!'
            },
            {
                'text': 'Odrzuć ofertę',
                'impacts': {
                    'stress_level': 1
                },
                'tip': '💡 Czasem warto poczekać na lepszą ofertę.'
            }
        ]
    },
    'promotion': {
        'requires_job': True,
        'age_range': (25, 60),
        'event_name': '📈 Awans',
        'description': 'Szef proponuje awans. Więcej odpowiedzialności.',
        'choices': [
            {
                'text': 'Przyjmij (+3000 zł/mc)',
                'impacts': {
                    'income': 3000,
                    'career_satisfaction': 3,
                    'stress_level': 2,
                    'free_time': -1
                },
                'tip': '💡 Awans = wyższe zarobki = wyższa emerytura!'
            },
            {
                'text': 'Odmów',
                'impacts': {
                    'career_satisfaction': -2
                },
                'tip': '💡 Czasem work-life balance jest ważniejszy.'
            }
        ]
    },
    'raise_request': {
        'requires_job': True,
        'age_range': (25, 60),
        'event_name': '💰 Prośba o podwyżkę',
        'description': 'Pracujesz tu już rok. Możesz poprosić o podwyżkę.',
        'choices': [
            {
                'text': 'Poproś o podwyżkę',
                'impacts': {
                    'income': 800,
                    'self_esteem': 2,
                    'stress_level': 1
                },
                'tip': '💡 Nie proś, nie dostaniesz! Szef doceni inicjatywę.'
            },
            {
                'text': 'Czekaj na awans',
                'impacts': {
                    'career_satisfaction': -1
                },
                'tip': '💡 Pasywne czekanie rzadko się opłaca.'
            }
        ]
    },
    'burnout_warning': {
        'requires_job': True,
        'age_range': (25, 55),
        'event_name': '😰 Wypalenie zawodowe',
        'description': 'Czujesz się wyczerpany pracą. Stres rośnie.',
        'choices': [
            {
                'text': 'Weź urlop (2000 zł koszt)',
                'impacts': {
                    'savings': -2000,
                    'stress_level': -3,
                    'mental_health': 2,
                    'happiness': 2
                },
                'tip': '💡 Zdrowie psychiczne jest ważniejsze niż pieniądze!'
            },
            {
                'text': 'Zmień pracę',
                'impacts': {
                    'work': 'bezrobotny',
                    'has_job': False,
                    'income': -999999,
                    'stress_level': -2,
                    'mental_health': 1
                },
                'tip': '💡 Czasem trzeba odejść dla własnego zdrowia.'
            },
            {
                'text': 'Wytrzymaj',
                'impacts': {
                    'mental_health': -2,
                    'stress_level': 3,
                    'happiness': -2
                },
                'tip': '💡 Ignorowanie wypalenia może prowadzić do depresji!'
            }
        ]
    },
    'skill_training': {
        'requires_job': True,
        'age_range': (22, 55),
        'event_name': '📚 Szkolenie zawodowe',
        'description': 'Firma oferuje płatne szkolenie. Nowe umiejętności!',
        'choices': [
            {
                'text': 'Weź udział (0 zł, płaci firma)',
                'impacts': {
                    'personal_growth': 2,
                    'career_satisfaction': 2,
                    'income': 500,
                    'free_time': -2
                },
                'tip': '💡 Rozwój kompetencji zwiększa wartość na rynku pracy!'
            },
            {
                'text': 'Odmów',
                'impacts': {
                    'career_satisfaction': -1
                },
                'tip': '💡 Odmawianie rozwoju ogranicza karierę.'
            }
        ]
    },
    'remote_work_offer': {
        'requires_job': True,
        'age_range': (25, 60),
        'event_name': '🏠 Praca zdalna',
        'description': 'Firma pozwala na pracę zdalną. Więcej elastyczności!',
        'choices': [
            {
                'text': 'Pracuj zdalnie',
                'impacts': {
                    'work_life_balance': 3,
                    'stress_level': -2,
                    'free_time': 2,
                    'happiness': 2,
                    'savings': 300
                },
                'tip': '💡 Praca zdalna oszczędza czas i koszty dojazdu!'
            },
            {
                'text': 'Wolisz biuro',
                'impacts': {
                    'social_connections': 1
                },
                'tip': '💡 Biuro ma swoje plusy - kontakty społeczne!'
            }
        ]
    }
}
HOUSING_EVENTS = {
    'need_apartment': {
        'event_key': 'need_apartment',
        'requires_no_apartment': True,
        'mandatory_if_working': True,
        'age_range': (20, 40),
        'show_once': True,  # Pokazuj tylko raz
        'event_name': '🏠 Potrzebujesz mieszkania',
        'description': 'Nie możesz już mieszkać z rodzicami. Musisz znaleźć mieszkanie.',
        'choices': [
            {
                'text': 'Wynajmij kawalerkę (2200 zł/mc)',
                'impacts': {
                    'has_apartment': True,
                    'monthly_costs': 2200,
                    'happiness': 2,
                    'savings': -5000
                },
                'tip': '💡 Własne mieszkanie = swoboda, ale koszty!'
            },
            {
                'text': 'Wynajmij pokój (1200 zł/mc)',
                'impacts': {
                    'has_apartment': True,
                    'monthly_costs': 1200,
                    'happiness': 1,
                    'savings': -1500
                },
                'tip': '💡 Pokój to tańsza opcja.'
            },
            {
                'text': 'Mieszkaj z rodzicami (200 zł/mc)',
                'impacts': {
                    'monthly_costs': 200,
                    'self_esteem': -1
                },
                'tip': '💡 Oszczędzasz, ale ograniczasz niezależność.'
            }
        ]
    },
    'rent_increase': {
        'requires_apartment': True,
        'age_range': (20, 70),
        'event_name': '📈 Podwyżka czynszu',
        'description': 'Właściciel podnosi czynsz o 300 zł.',
        'choices': [
            {
                'text': 'Akceptuj podwyżkę',
                'impacts': {
                    'monthly_costs': 300,
                    'stress_level': 2
                },
                'tip': '💡 Czynsze rosną szybciej niż płace!'
            },
            {
                'text': 'Szukaj tańszego (przeprowadzka 2000 zł)',
                'impacts': {
                    'savings': -2000,
                    'monthly_costs': -200,
                    'stress_level': 3
                },
                'tip': '💡 Przeprowadzka to stres, ale czasem się opłaca.'
            }
        ]
    },
    'buy_apartment': {
        'requires_apartment': True,
        'requires_savings': 50000,
        'age_range': (28, 50),
        'event_name': '🏡 Kupno mieszkania',
        'description': 'Możesz kupić mieszkanie na kredyt. Wkład 50000 zł.',
        'choices': [
            {
                'text': 'Kup (rata 2500 zł/mc, 25 lat)',
                'impacts': {
                    'savings': -50000,
                    'monthly_costs': 1000,
                    'financial_security': 3,
                    'happiness': 3
                },
                'tip': '💡 Własne mieszkanie to inwestycja!'
            },
            {
                'text': 'Dalej wynajmuj',
                'impacts': {
                    'savings': 5000
                },
                'tip': '💡 Wynajem daje elastyczność.'
            }
        ]
    }
}
COST_EVENTS = {}
RANDOM_LIFE_EVENTS = {
    'health_crisis': {
        'age_range': (30, 70),
        'event_name': '🏥 Problemy ze zdrowiem',
        'description': 'Odczuwasz problemy zdrowotne. Lekarz zaleca leczenie.',
        'choices': [
            {
                'text': 'Prywatnie (8000 zł)',
                'impacts': {
                    'savings': -8000,
                    'health': 3,
                    'stress_level': -2
                },
                'tip': '💡 Zdrowie najważniejsze!'
            },
            {
                'text': 'NFZ (500 zł, czekasz)',
                'impacts': {
                    'savings': -500,
                    'health': 2,
                    'stress_level': 2
                },
                'tip': '💡 NFZ tańsze, ale dłużej czekasz.'
            }
        ]
    },
    'job_loss': {
        'requires_job': True,
        'age_range': (25, 65),
        'event_name': '😢 Utrata pracy',
        'description': 'Firma zwalnia. Jesteś na liście.',
        'choices': [
            {
                'text': 'Szukaj nowej pracy',
                'impacts': {
                    'work': 'bezrobotny',
                    'has_job': False,
                    'income': -999999,
                    'stress_level': 4,
                    'mental_health': -2
                },
                'tip': '💡 Bezrobocie trudne, ale szukaj aktywnie!'
            }
        ]
    },
    'car_accident': {
        'age_range': (20, 70),
        'event_name': '🚗 Wypadek samochodowy',
        'description': 'Miałeś wypadek. Na szczęście nic poważnego.',
        'choices': [
            {
                'text': 'Napraw auto (5000 zł)',
                'impacts': {
                    'savings': -5000,
                    'stress_level': 2
                },
                'tip': '💡 Ubezpieczenie AC się przydaje!'
            },
            {
                'text': 'Jeździj komunikacją',
                'impacts': {
                    'monthly_costs': 200,
                    'free_time': -1
                },
                'tip': '💡 Komunikacja miejska to oszczędność!'
            }
        ]
    },
    'inheritance': {
        'age_range': (30, 60),
        'event_name': '💰 Spadek',
        'description': 'Krewny zostawił Ci spadek. Nieoczekiwana kasa!',
        'choices': [
            {
                'text': 'Przyjmij spadek (30000 zł)',
                'impacts': {
                    'savings': 30000,
                    'happiness': 2
                },
                'tip': '💡 Mądre wykorzystanie spadku może zmienić życie!'
            }
        ]
    },
    'lottery_win': {
        'age_range': (18, 70),
        'event_name': '🎰 Wygrana na loterii',
        'description': 'Wygrałeś 10000 zł! Szczęściarz!',
        'choices': [
            {
                'text': 'Odbierz wygraną',
                'impacts': {
                    'savings': 10000,
                    'happiness': 3
                },
                'tip': '💡 Szczęście sprzyja mądrym - zainwestuj mądrze!'
            }
        ]
    },
    'theft': {
        'age_range': (18, 70),
        'event_name': '🔒 Kradzież',
        'description': 'Okradziono Cię. Strata 3000 zł.',
        'choices': [
            {
                'text': 'Zgłoś policji',
                'impacts': {
                    'savings': -3000,
                    'stress_level': 3,
                    'happiness': -2
                },
                'tip': '💡 Zawsze zgłaszaj przestępstwa!'
            }
        ]
    },
    'friend_help': {
        'age_range': (20, 60),
        'event_name': '🤝 Przyjaciel prosi o pomoc',
        'description': 'Przyjaciel prosi o pożyczkę 2000 zł.',
        'choices': [
            {
                'text': 'Pożycz (2000 zł)',
                'impacts': {
                    'savings': -2000,
                    'social_connections': 2,
                    'happiness': 1
                },
                'tip': '💡 Prawdziwi przyjaciele pomagają sobie!'
            },
            {
                'text': 'Odmów',
                'impacts': {
                    'social_connections': -2,
                    'stress_level': 1
                },
                'tip': '💡 Czasem trzeba powiedzieć nie.'
            }
        ]
    },
    'apartment_flood': {
        'requires_apartment': True,
        'age_range': (20, 70),
        'event_name': '💧 Zalanie mieszkania',
        'description': 'Sąsiad zalał Ci mieszkanie. Remont!',
        'choices': [
            {
                'text': 'Zrób remont (8000 zł)',
                'impacts': {
                    'savings': -8000,
                    'stress_level': 3,
                    'happiness': -2
                },
                'tip': '💡 Ubezpieczenie mieszkania jest ważne!'
            }
        ]
    },
    'relationship_start': {
        'age_range': (18, 50),
        'event_name': '❤️ Nowy związek',
        'description': 'Poznałeś kogoś wyjątkowego. To może być to!',
        'choices': [
            {
                'text': 'Zacznij związek',
                'impacts': {
                    'happiness': 3,
                    'emotional_wellbeing': 3,
                    'relationship_quality': 5,
                    'monthly_costs': 500,
                    'social_connections': 2
                },
                'tip': '💡 Zdrowy związek poprawia jakość życia!'
            },
            {
                'text': 'Nie jesteś gotowy',
                'impacts': {
                    'happiness': -1
                },
                'tip': '💡 Nie spiesz się. Związek wymaga gotowości.'
            }
        ]
    },
    'breakup': {
        'age_range': (18, 60),
        'event_name': '💔 Rozstanie',
        'description': 'Związek się nie układa. Czas kończyć.',
        'choices': [
            {
                'text': 'Zerwij związek',
                'impacts': {
                    'happiness': -3,
                    'emotional_wellbeing': -3,
                    'relationship_quality': -5,
                    'stress_level': 4,
                    'mental_health': -2,
                    'monthly_costs': -500
                },
                'tip': '💡 Rozstanie boli, ale czasem jest konieczne.'
            },
            {
                'text': 'Spróbuj naprawić',
                'impacts': {
                    'savings': -2000,
                    'relationship_quality': 1,
                    'stress_level': 2
                },
                'tip': '💡 Terapia par może pomóc!'
            }
        ]
    },
    'pet_adoption': {
        'age_range': (20, 60),
        'event_name': '🐕 Adopcja zwierzaka',
        'description': 'Myślisz o adopcji psa lub kota.',
        'choices': [
            {
                'text': 'Adoptuj (500 zł start, 300 zł/mc)',
                'impacts': {
                    'savings': -500,
                    'monthly_costs': 300,
                    'happiness': 3,
                    'emotional_wellbeing': 2,
                    'stress_level': -1
                },
                'tip': '💡 Zwierzęta poprawiają zdrowie psychiczne!'
            },
            {
                'text': 'Nie teraz',
                'impacts': {},
                'tip': '💡 Zwierzę to odpowiedzialność na 10-15 lat!'
            }
        ]
    }
}


def get_random_pension_tip():
    """Zwraca losową poradę emerytalną"""
    import random
    return random.choice(PENSION_TIPS)


def get_daily_events():
    """Zwraca losowe wydarzenie codzienne"""
    import random
    return random.choice(list(DAILY_EVENTS.values()))


def check_event_requirements(event_data, session):
    """Sprawdza czy wydarzenie spełnia wymagania"""
    import logging
    logger = logging.getLogger(__name__)
    
    event_key = event_data.get('event_key', 'unknown')
    
    if 'age_range' in event_data:
        age_min, age_max = event_data['age_range']
        if not (age_min <= session.age <= age_max):
            logger.info(f"  {event_key}: FAILED age check (age={session.age}, range={age_min}-{age_max})")
            return False
    
    completed_events = session.completed_events or []

    # Blokuj wydarzenia edukacyjne po pierwszym przedstawieniu
    if event_data.get('event_key') in EDUCATION_EVENTS and 'education_intro' in completed_events:
        logger.info(f"  {event_key}: FAILED education_intro already completed")
        return False

    # Sprawdź czy wydarzenie może wystąpić tylko raz
    if event_data.get('show_once'):
        event_key_check = event_data.get('event_key', '')
        if event_key_check in completed_events:
            logger.info(f"  {event_key}: FAILED show_once check")
            return False
    
    if event_data.get('requires_no_job') and session.has_job:
        logger.info(f"  {event_key}: FAILED requires_no_job (has_job={session.has_job})")
        return False
    
    if event_data.get('requires_job') and not session.has_job:
        logger.info(f"  {event_key}: FAILED requires_job (has_job={session.has_job})")
        return False
    
    if event_data.get('requires_apartment') and not session.has_apartment:
        logger.info(f"  {event_key}: FAILED requires_apartment")
        return False
    
    if event_data.get('requires_no_apartment') and session.has_apartment:
        logger.info(f"  {event_key}: FAILED requires_no_apartment")
        return False
    
    if 'requires' in event_data:
        completed = session.completed_education or []
        if not any(edu in completed for edu in event_data['requires']):
            logger.info(f"  {event_key}: FAILED requires check (needs {event_data['requires']}, has {completed})")
            return False
    
    if 'excludes' in event_data:
        completed = session.completed_education or []
        if any(edu in completed for edu in event_data['excludes']):
            logger.info(f"  {event_key}: FAILED excludes check (excludes {event_data['excludes']}, has {completed})")
            return False
    
    logger.info(f"  {event_key}: PASSED all checks")
    return True


def get_mandatory_events(session):
    """Zwraca obowiązkowe wydarzenia"""
    mandatory = []
    
    # Mieszkanie obowiązkowe jeśli ma >23 lata i pracuje
    if session.age > 23 and session.has_job and not session.has_apartment:
        if check_event_requirements(HOUSING_EVENTS['need_apartment'], session):
            mandatory.append(HOUSING_EVENTS['need_apartment'])
    
    return mandatory


def get_available_events(session):
    """Zwraca wszystkie dostępne wydarzenia z kluczami"""
    available = []
    
    for event_key, event_data in EDUCATION_EVENTS.items():
        event_data['event_key'] = event_key  # Dodaj klucz do danych
        if check_event_requirements(event_data, session):
            available.append(event_data)
    
    for event_key, event_data in JOB_EVENTS.items():
        event_data['event_key'] = event_key
        if check_event_requirements(event_data, session):
            available.append(event_data)
    
    for event_key, event_data in HOUSING_EVENTS.items():
        event_data['event_key'] = event_key
        if not event_data.get('mandatory_if_working'):
            if check_event_requirements(event_data, session):
                available.append(event_data)
    
    for event_key, event_data in RANDOM_LIFE_EVENTS.items():
        event_data['event_key'] = event_key
        if check_event_requirements(event_data, session):
            available.append(event_data)
    
    return available


def get_event_for_session(session):
    """
    Zwraca odpowiednie wydarzenie.
    Priorytet: pierwsze wydarzenie (edukacja) > obowiązkowe > oferty pracy dla bezrobotnych (80% lub 95% jeśli aktywnie szuka) > życiowe (60%) > codzienne (30%) > brak (10%)
    """
    import random
    
    # SPECJALNE: Jeśli to pierwsza gra (brak completed_events), zawsze pokaż wybór szkoły
    completed = session.completed_events or []
    if len(completed) == 0 and session.age <= 20:
        # Sprawdź czy są dostępne wydarzenia edukacyjne
        for event_key, event_data in EDUCATION_EVENTS.items():
            event_data['event_key'] = event_key
            if check_event_requirements(event_data, session):
                return event_data
    
    # Najpierw obowiązkowe
    mandatory = get_mandatory_events(session)
    if mandatory:
        event = mandatory[0]
        if 'event_key' not in event:
            event['event_key'] = 'need_apartment'
        return event
    
    # NOWE: Jeśli nie ma pracy, zwiększona szansa na wydarzenie związane z pracą
    # BONUS: Jeśli aktywnie szuka pracy (actively_job_searching = True), szansa wzrasta do 95%!
    if not session.has_job:
        job_events_available = []
        for event_key, event_data in JOB_EVENTS.items():
            event_data['event_key'] = event_key
            if event_data.get('higher_chance_when_unemployed') and check_event_requirements(event_data, session):
                job_events_available.append(event_data)
        
        # Zwiększona szansa jeśli aktywnie szuka pracy
        job_chance = 0.95 if getattr(session, 'actively_job_searching', False) else 0.80
        
        if job_events_available and random.random() < job_chance:
            # Reset flagi po wykorzystaniu
            if getattr(session, 'actively_job_searching', False):
                session.actively_job_searching = False
            return random.choice(job_events_available)
    
    # 10% szans na brak wydarzenia (szybsze tempo gry)
    if random.random() < 0.1:
        return None
    
    # Potem życiowe lub codzienne
    available = get_available_events(session)
    if available and random.random() < 0.6:  # 60% na życiowe
        return random.choice(available)
    
    # Codzienne
    return get_daily_events()
