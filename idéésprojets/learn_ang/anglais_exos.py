from pathlib import Path
import json
import random
import time

file_path = Path(__file__)
dossier_parent = file_path.parent
ch_DB_anglais = dossier_parent / "anglais.json"

with open(ch_DB_anglais, "r") as fichier_ouvert:
    DB_anglais: dict = json.load(fichier_ouvert)

ch_stats_anglais = dossier_parent / "anglais_stats.json"
with open(ch_stats_anglais, "r") as fichier_ouvert:
    STATS = json.load(fichier_ouvert)


MENU = """\n\n\n\n                      -- TRIOLINGO --


            1) Entrainement avec des mots au hasard
            
            2) Entrainement verbes
            
            3) Entrainement noms communs
            
            4) Entrainement adjectifs
            
            5) Entrainement nombres

            6) Entrainement determinants
            
            7) Entrainement autres

            8) Voir les stats

            9) Entrainement mot non appris

            0) QUITTER 
            
            ----------> """

MENU_CHOICE = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

LISTE_BAD_CHOICE = ["dictionnaire_trad_ang_a_fr",
                    "dictionnaire_trad_fr_a_ang", "verbes"]

# compteur de bonnes reponse pour les stats
bonnes_reponse = 0

start_of_learn = time.time()

categorie_mot = ""
mot_reponse = ""
mot_question = ""
verbe_question = ""
verbe_reponse = ""
noms_communs_reponse = ""
noms_communs_question = ""
adjectifs_reponse = ""
adjectifs_question = ""
nombres_reponse = ""
nombres_question = ""
determinants_reponse = ""
determinants_question = ""
autres_reponse = ""
autres_question = ""
langue_a_traduire = ""
liste_mot_reponse = ""

entrainement_hasard = False

running = True

while running:
    # Mise à jour des stats
    with open(ch_stats_anglais, "w") as fichier_ouvert:
        json.dump(STATS, fichier_ouvert, indent=4, ensure_ascii=False)

    # MENU AND CHOICE
    choice = ""
    while choice not in MENU_CHOICE:
        choice = input(MENU)
        choice = choice.strip(" ")
        if choice not in MENU_CHOICE:
            print("Le michente est prié de prendre une bonne option !")

    if choice == "1":
        entrainement_hasard = True
        while entrainement_hasard == True:
            # choisir au hasard si on veut traduire en angalais ou en français
            francais_ou_anglais = random.randint(1, 2)

            if francais_ou_anglais == 1:
                langue_a_traduire = "dictionnaire_trad_ang_a_fr"
            else:
                langue_a_traduire = "dictionnaire_trad_fr_a_ang"

            quelle_categorie_mot = random.randint(1, 100)
            if quelle_categorie_mot > 0 and quelle_categorie_mot < 26:
                categorie_mot = "noms communs"
            elif quelle_categorie_mot > 25 and quelle_categorie_mot < 51:
                categorie_mot = "verbes"
            elif quelle_categorie_mot > 50 and quelle_categorie_mot < 76:
                categorie_mot = "adjectifs"
            elif quelle_categorie_mot > 75 and quelle_categorie_mot < 91:
                categorie_mot = "autres"
            elif quelle_categorie_mot > 90 and quelle_categorie_mot < 86:
                categorie_mot = "determinants"
            else:
                categorie_mot = "nombres"

            # Prendre un mot au hasard dans le dictionnaire choisi au hasard
            dictionnaire_mot_possible = DB_anglais[langue_a_traduire][categorie_mot]
            dictionnaire_mot_possible = list(dictionnaire_mot_possible.items())
            random.shuffle(dictionnaire_mot_possible)
            dictionnaire_mot_possible = dict(dictionnaire_mot_possible)

            for mot in dictionnaire_mot_possible.keys():
                mot_question = mot
                mot_reponse = dictionnaire_mot_possible[mot]
                break
            liste_mot_reponse = []
            liste_mot_reponse.append(mot_reponse)

            traduction = input(f"""                                   (Pour quitter entre EX)

            Traduis le mot {mot_question}                                     
            
            --------> """)
            traduction = traduction.strip(" ")

            if traduction.lower() in liste_mot_reponse:
                print(f"\n\nBravo c'est la bonne réponse !")
                STATS["bonnes reponses"] += 1
                appris_ou_pas = STATS["total mots appris"][langue_a_traduire][categorie_mot][mot_question]
                if appris_ou_pas == "False":
                    STATS["total mots appris"][langue_a_traduire][categorie_mot][mot_question] = "True"
                    STATS["mot_appris"] += 1
                time.sleep(1)
            elif traduction not in liste_mot_reponse and traduction != "EX":
                print(
                    f"""\n\nDommage ! {traduction} n'est pas la bonne traduction du mot {mot_question}.
Voici la ou les bonne(s) traduction(s) possible(s) du mot {mot_question} :""")
                for reponse_possible in liste_mot_reponse:
                    print(f"-{reponse_possible}")
                time.sleep(3)

            else:
                entrainement_hasard = False

    elif choice == "2":
        entrainement_verbe = True
        while entrainement_verbe:
            # choisir au hasard si on veut traduire en angalais ou en français
            francais_ou_anglais = random.randint(1, 2)

            if francais_ou_anglais == 1:
                langue_a_traduire = "dictionnaire_trad_ang_a_fr"
            else:
                langue_a_traduire = "dictionnaire_trad_fr_a_ang"

            dictionnaire_verbe_possible = DB_anglais[langue_a_traduire]["verbes"]
            dictionnaire_verbe_possible = list(
                dictionnaire_verbe_possible.items())
            random.shuffle(dictionnaire_verbe_possible)
            dictionnaire_verbe_possible = dict(dictionnaire_verbe_possible)

            for mot in dictionnaire_verbe_possible.keys():
                verbe_question = mot
                verbe_reponse = DB_anglais[langue_a_traduire]["verbes"][mot]
                break

            liste_verbe_reponse = []
            liste_verbe_reponse.append(verbe_reponse)

            traduction_verbe = input(f"""                                     (Entre michente si tu veux revenir au menu !)
            
            Traduis le verbe {verbe_question}
            
            ------------> """)

            if traduction_verbe.lower() in liste_verbe_reponse:
                print("\n\nBravo c'est la bonne réponse !")
                STATS["bonnes reponses"] += 1
                appris_ou_pas = STATS["total mots appris"][langue_a_traduire]["verbes"][verbe_question]
                if appris_ou_pas == "False":
                    STATS["total mots appris"][langue_a_traduire]["verbes"][verbe_question] = "True"
                STATS["mot_appris"] += 1
                time.sleep(1)

            elif traduction_verbe not in liste_verbe_reponse and traduction_verbe != "michente":
                print(f"""\n\nDommage ! {traduction_verbe} n'est pas la bonne traduction du verbe {verbe_question}.
Voici la ou les bonne(s) réponse(s) possible(s): """)
                for reponse_possible_verbe in liste_verbe_reponse:
                    print(f"-{reponse_possible_verbe}")
                    time.sleep(3)

            else:
                entrainement_verbe = False

    elif choice == "3":
        entrainement_noms_communs = True
        while entrainement_noms_communs:
            # choisir au hasard si on veut traduire en angalais ou en français
            francais_ou_anglais = random.randint(1, 2)

            if francais_ou_anglais == 1:
                langue_a_traduire = "dictionnaire_trad_ang_a_fr"
            else:
                langue_a_traduire = "dictionnaire_trad_fr_a_ang"

            dictionnaire_noms_communs_possible = DB_anglais[langue_a_traduire]["noms communs"]
            dictionnaire_noms_communs_possible = list(
                dictionnaire_noms_communs_possible.items())
            random.shuffle(dictionnaire_noms_communs_possible)
            dictionnaire_noms_communs_possible = dict(
                dictionnaire_noms_communs_possible)

            for mot in dictionnaire_noms_communs_possible.keys():
                noms_communs_question = mot
                noms_communs_reponse = DB_anglais[langue_a_traduire]["noms communs"][mot]
                break

            liste_noms_communs_reponse = []
            liste_noms_communs_reponse.append(noms_communs_reponse)

            traduction_noms_communs = input(f"""                                     (Entre michente si tu veux revenir au menu !)
            
            Traduis le noms communs {noms_communs_question}
            
            ------------> """)

            if traduction_noms_communs.lower() in liste_noms_communs_reponse:
                print("\n\nBravo c'est la bonne réponse !")
                STATS["bonnes reponses"] += 1
                appris_ou_pas = STATS["total mots appris"][langue_a_traduire]["noms communs"][noms_communs_question]
                if appris_ou_pas == "False":
                    STATS["total mots appris"][langue_a_traduire]["noms communs"][noms_communs_question] = "True"
                STATS["mot_appris"] += 1
                time.sleep(1)

            elif traduction_noms_communs not in liste_noms_communs_reponse and traduction_noms_communs != "michente":
                print(f"""\n\nDommage ! {traduction_noms_communs} n'est pas la bonne traduction du mot {noms_communs_question}.
Voici la ou les bonne(s) réponse(s) possible(s): """)
                for reponse_possible_noms_communs in liste_noms_communs_reponse:
                    print(f"-{reponse_possible_noms_communs}")
                    time.sleep(3)

            else:
                entrainement_noms_communs = False

    elif choice == "4":
        entrainement_adjectifs = True
        while entrainement_adjectifs:
            # choisir au hasard si on veut traduire en angalais ou en français
            francais_ou_anglais = random.randint(1, 2)

            if francais_ou_anglais == 1:
                langue_a_traduire = "dictionnaire_trad_ang_a_fr"
            else:
                langue_a_traduire = "dictionnaire_trad_fr_a_ang"

            dictionnaire_adjectifs_possible = DB_anglais[langue_a_traduire]["adjectifs"]
            dictionnaire_adjectifs_possible = list(
                dictionnaire_adjectifs_possible.items())
            random.shuffle(dictionnaire_adjectifs_possible)
            dictionnaire_adjectifs_possible = dict(
                dictionnaire_adjectifs_possible)

            for mot in dictionnaire_adjectifs_possible.keys():
                adjectifs_question = mot
                adjectifs_reponse = DB_anglais[langue_a_traduire]["adjectifs"][mot]
                break

            liste_adjectifs_reponse = []
            liste_adjectifs_reponse.append(adjectifs_reponse)

            traduction_adjectifs = input(f"""                                     (Entre michente si tu veux revenir au menu !)
            
            Traduis le adjectifs {adjectifs_question}
            
            ------------> """)

            if traduction_adjectifs.lower() in liste_adjectifs_reponse:
                print("\n\nBravo c'est la bonne réponse !")
                STATS["bonnes reponses"] += 1
                appris_ou_pas = STATS["total mots appris"][langue_a_traduire]["adjectifs"][adjectifs_question]
                if appris_ou_pas == "False":
                    STATS["total mots appris"][langue_a_traduire]["adjectifs"][adjectifs_question] = "True"
                STATS["mot_appris"] += 1
                time.sleep(1)

            elif traduction_adjectifs not in liste_adjectifs_reponse and traduction_adjectifs != "michente":
                print(f"""\n\nDommage ! {traduction_adjectifs} n'est pas la bonne traduction du adjectifs {adjectifs_question}.
Voici la ou les bonne(s) réponse(s) possible(s): """)
                for reponse_possible_adjectifs in liste_adjectifs_reponse:
                    print(f"-{reponse_possible_adjectifs}")
                    time.sleep(3)

            else:
                entrainement_adjectifs = False

    elif choice == "5":
        entrainement_nombres = True
        while entrainement_nombres:
            # choisir au hasard si on veut traduire en angalais ou en français
            francais_ou_anglais = random.randint(1, 2)

            if francais_ou_anglais == 1:
                langue_a_traduire = "dictionnaire_trad_ang_a_fr"
            else:
                langue_a_traduire = "dictionnaire_trad_fr_a_ang"

            dictionnaire_nombres_possible = DB_anglais[langue_a_traduire]["nombres"]
            dictionnaire_nombres_possible = list(
                dictionnaire_nombres_possible.items())
            random.shuffle(dictionnaire_nombres_possible)
            dictionnaire_nombres_possible = dict(dictionnaire_nombres_possible)

            for mot in dictionnaire_nombres_possible.keys():
                nombres_question = mot
                nombres_reponse = DB_anglais[langue_a_traduire]["nombres"][mot]
                break

            liste_nombres_reponse = []
            liste_nombres_reponse.append(nombres_reponse)

            traduction_nombres = input(f"""                                     (Entre michente si tu veux revenir au menu !)
            
            Traduis le nombres {nombres_question}
            
            ------------> """)

            if traduction_nombres.lower() in liste_nombres_reponse:
                print("\n\nBravo c'est la bonne réponse !")
                STATS["bonnes reponses"] += 1
                appris_ou_pas = STATS["total mots appris"][langue_a_traduire]["nombres"][nombres_question]
                if appris_ou_pas == "False":
                    STATS["total mots appris"][langue_a_traduire]["nombres"][nombres_question] = "True"
                STATS["mot_appris"] += 1
                time.sleep(1)

            elif traduction_nombres not in liste_nombres_reponse and traduction_nombres != "michente":
                print(f"""\n\nDommage ! {traduction_nombres} n'est pas la bonne traduction du nombres {nombres_question}.
Voici la ou les bonne(s) réponse(s) possible(s): """)
                for reponse_possible_nombres in liste_nombres_reponse:
                    print(f"-{reponse_possible_nombres}")
                    time.sleep(3)

            else:
                entrainement_nombres = False

    elif choice == "6":
        entrainement_determinants = True
        while entrainement_determinants:
            # choisir au hasard si on veut traduire en angalais ou en français
            francais_ou_anglais = random.randint(1, 2)

            if francais_ou_anglais == 1:
                langue_a_traduire = "dictionnaire_trad_ang_a_fr"
            else:
                langue_a_traduire = "dictionnaire_trad_fr_a_ang"

            dictionnaire_determinants_possible = DB_anglais[langue_a_traduire]["determinants"]
            dictionnaire_determinants_possible = list(
                dictionnaire_determinants_possible.items())
            random.shuffle(dictionnaire_determinants_possible)
            dictionnaire_determinants_possible = dict(
                dictionnaire_determinants_possible)

            for mot in dictionnaire_determinants_possible.keys():
                determinants_question = mot
                determinants_reponse = DB_anglais[langue_a_traduire]["determinants"][mot]
                break

            liste_determinants_reponse = []
            liste_determinants_reponse.append(determinants_reponse)

            traduction_determinants = input(f"""                                     (Entre michente si tu veux revenir au menu !)
            
            Traduis le determinants {determinants_question}
            
            ------------> """)

            if traduction_determinants.lower() in liste_determinants_reponse:
                print("\n\nBravo c'est la bonne réponse !")
                STATS["bonnes reponses"] += 1
                appris_ou_pas = STATS["total mots appris"][langue_a_traduire]["determinants"][determinants_question]
                if appris_ou_pas == "False":
                    STATS["total mots appris"][langue_a_traduire]["determinants"][determinants_question] = "True"
                STATS["mot_appris"] += 1
                time.sleep(1)

            elif traduction_determinants not in liste_determinants_reponse and traduction_determinants != "michente":
                print(f"""\n\nDommage ! {traduction_determinants} n'est pas la bonne traduction du determinants {determinants_question}.
Voici la ou les bonne(s) réponse(s) possible(s): """)
                for reponse_possible_determinants in liste_determinants_reponse:
                    print(f"-{reponse_possible_determinants}")
                    time.sleep(3)

            else:
                entrainement_determinants = False

    elif choice == "7":
        entrainement_autres = True
        while entrainement_autres:
            # choisir au hasard si on veut traduire en angalais ou en français
            francais_ou_anglais = random.randint(1, 2)

            if francais_ou_anglais == 1:
                langue_a_traduire = "dictionnaire_trad_ang_a_fr"
            else:
                langue_a_traduire = "dictionnaire_trad_fr_a_ang"

            dictionnaire_autres_possible = DB_anglais[langue_a_traduire]["autres"]
            dictionnaire_autres_possible = list(
                dictionnaire_autres_possible.items())
            random.shuffle(dictionnaire_autres_possible)
            dictionnaire_autres_possible = dict(dictionnaire_autres_possible)

            for mot in dictionnaire_autres_possible.keys():
                autres_question = mot
                autres_reponse = DB_anglais[langue_a_traduire]["autres"][mot]
                break

            liste_autres_reponse = []
            liste_autres_reponse.append(autres_reponse)

            traduction_autres = input(f"""                                     (Entre michente si tu veux revenir au menu !)
            
            Traduis le autres {autres_question}
            
            ------------> """)

            if traduction_autres.lower() in liste_autres_reponse:
                print("\n\nBravo c'est la bonne réponse !")
                STATS["bonnes reponses"] += 1
                appris_ou_pas = STATS["total mots appris"][langue_a_traduire]["autres"][autres_question]
                if appris_ou_pas == "False":
                    STATS["total mots appris"][langue_a_traduire]["autres"][autres_question] = "True"
                STATS["mot_appris"] += 1
                time.sleep(1)

            elif traduction_autres not in liste_autres_reponse and traduction_autres != "michente":
                print(f"""\n\nDommage ! {traduction_autres} n'est pas la bonne traduction du autres {autres_question}.
Voici la ou les bonne(s) réponse(s) possible(s): """)
                for reponse_possible_autres in liste_autres_reponse:
                    print(f"-{reponse_possible_autres}")
                    time.sleep(3)

            else:
                entrainement_autres = False

    elif choice == "8":
        menu_stats = True
        while menu_stats:
            nbr_bonnes_reponses = STATS["bonnes reponses"]
            nbr_mot_appris = STATS["mot_appris"] / 2
            nbr_mot_appris = int(nbr_mot_appris)
            total_mot_a_apprendre = STATS["total mot"] / 2
            total_mot_a_apprendre = int(total_mot_a_apprendre)
            nbr_minute_to_learn = STATS["temps_de_jeu_minutes"]
            nbr_heure_to_learn = STATS["temps_de_jeu_heures"]

            decimale = 0
            str_nbr_heure_to_play = str(nbr_heure_to_learn)
            for i in str_nbr_heure_to_play:
                decimale += 1
                if i == ".":
                    nbr_minute_to_learn = str_nbr_heure_to_play[decimale] + str(
                        str_nbr_heure_to_play[decimale + 1])
                    nbr_minute_to_learn = (int(nbr_minute_to_learn) * 60) / 100
                    nbr_minute_to_learn = int(nbr_minute_to_learn)

            print(f"""\n\n\n\n              STATISTIQUES
            

            NOMBRE DE BONNES REPONSE : {nbr_bonnes_reponses}

            NOMBRE DE MOTS APPRIS : {nbr_mot_appris} sur {total_mot_a_apprendre}

            TEMPS D'APPRENTISSAGE : {int(nbr_heure_to_learn)} h {nbr_minute_to_learn}      
            """)

            choice_stats = input(
                "\n\n\n\nPour revenir au menu entrez 'michente' \n---------> ")

            if choice_stats == "michente":
                menu_stats = False

    elif choice == "9":
        menu_pas_appris = True
        while menu_pas_appris:
            trouver_mot_pas_appris = True
            while trouver_mot_pas_appris:
                # choisir au hasard si on veut traduire en angalais ou en français
                francais_ou_anglais = random.randint(1, 2)

                if francais_ou_anglais == 1:
                    langue_a_traduire = "dictionnaire_trad_ang_a_fr"
                else:
                    langue_a_traduire = "dictionnaire_trad_fr_a_ang"

                quelle_categorie_mot = random.randint(1, 100)
                if quelle_categorie_mot > 0 and quelle_categorie_mot < 26:
                    categorie_mot = "noms communs"
                elif quelle_categorie_mot > 25 and quelle_categorie_mot < 51:
                    categorie_mot = "verbes"
                elif quelle_categorie_mot > 50 and quelle_categorie_mot < 76:
                    categorie_mot = "adjectifs"
                elif quelle_categorie_mot > 75 and quelle_categorie_mot < 91:
                    categorie_mot = "autres"
                elif quelle_categorie_mot > 90 and quelle_categorie_mot < 86:
                    categorie_mot = "determinants"
                else:
                    categorie_mot = "nombres"

                # Prendre un mot au hasard dans le dictionnaire choisi au hasard
                dictionnaire_mot_possible = DB_anglais[langue_a_traduire][categorie_mot]
                dictionnaire_mot_possible = list(
                    dictionnaire_mot_possible.items())
                random.shuffle(dictionnaire_mot_possible)
                dictionnaire_mot_possible = dict(dictionnaire_mot_possible)

                for mot in dictionnaire_mot_possible.keys():
                    mot_question = mot
                    mot_reponse = dictionnaire_mot_possible[mot]
                    break
                liste_mot_reponse = []
                liste_mot_reponse.append(mot_reponse)

                if STATS["total mots appris"][langue_a_traduire][categorie_mot][mot_question] == "False":
                    trouver_mot_pas_appris = False

            traduction = input(f"""                                   (Pour quitter entre EX)

            Traduis le mot {mot_question}                                     
            
            --------> """)
            traduction = traduction.strip(" ")

            if traduction.lower() in liste_mot_reponse:
                print(f"\n\nBravo c'est la bonne réponse !")
                STATS["bonnes reponses"] += 1
                appris_ou_pas = STATS["total mots appris"][langue_a_traduire][categorie_mot][mot_question]
                if appris_ou_pas == "False":
                    STATS["total mots appris"][langue_a_traduire][categorie_mot][mot_question] = "True"
                    STATS["mot_appris"] += 1
                time.sleep(1)
            elif traduction not in liste_mot_reponse and traduction != "EX":
                print(
                    f"""\n\nDommage ! {traduction} n'est pas la bonne traduction du mot {mot_question}.
Voici la ou les bonne(s) traduction(s) possible(s) du mot {mot_question} :""")
                for reponse_possible in liste_mot_reponse:
                    print(f"-{reponse_possible}")
                time.sleep(3)

            else:
                menu_pas_appris = False
                trouver_mot_pas_appris = False
                entrainement_hasard = False

    elif choice == "0":
        running = False

end_of_learn = time.time()

temps_de_jeu_secondes = end_of_learn - start_of_learn
temps_de_jeu_minutes = temps_de_jeu_secondes / 60
temps_de_jeu_heures = temps_de_jeu_minutes / 60
temps_de_jeu_jour = temps_de_jeu_heures / 24

STATS["temps_de_jeu_secondes"] += temps_de_jeu_secondes
STATS["temps_de_jeu_minutes"] += temps_de_jeu_minutes
STATS["temps_de_jeu_heures"] += temps_de_jeu_heures
STATS["temps_de_jeu_jours"] += temps_de_jeu_jour

with open(ch_stats_anglais, "w") as fichier_ouvert:
    json.dump(STATS, fichier_ouvert, indent=4, ensure_ascii=False)
