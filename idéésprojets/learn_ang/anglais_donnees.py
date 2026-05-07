import json
from pathlib import Path
import time

fichier = Path(__file__)
dossier_parent = fichier.parent

ch_DB_anglais = Path(dossier_parent / "anglais.json")

if not ch_DB_anglais.exists():
    with open(ch_DB_anglais, "w") as fichier_ouvert:
        dictionnaire = {"dictionnaire_trad_ang_a_fr": {"verbes": {}, "noms communs": {}, "adjectifs": {}, "determinants": {}, "nombres": {}, "autres": {}},
                        "dictionnaire_trad_fr_a_ang": {"verbes": {}, "noms communs": {}, "adjectifs": {}, "determinants": {}, "nombres": {}, "autres": {}}}
        json.dump(dictionnaire, fichier_ouvert, indent=4, ensure_ascii=False)

with open(ch_DB_anglais, "r") as fichier_ouvert:
    DB_anglais = json.load(fichier_ouvert)

ch_stats_anglais = Path(dossier_parent / "anglais_stats.json")

if not ch_stats_anglais.exists():
    with open(ch_stats_anglais, "w") as fichier_ouvert:
        dictionnaire = {
            "bonnes reponses": 0,
            "mot_appris": 0,
            "temps_de_jeu_secondes": 0,
            "temps_de_jeu_minutes": 0,
            "temps_de_jeu_heures": 0,
            "temps_de_jeu_jours": 0,
            "total mots appris": {"dictionnaire_trad_ang_a_fr": {"verbes": {}, "noms communs": {}, "adjectifs": {}, "determinants": {}, "nombres": {}, "autres": {}}, "dictionnaire_trad_fr_a_ang": {"verbes": {}, "noms communs": {}, "adjectifs": {}, "determinants": {}, "nombres": {}, "autres": {}}}}
        json.dump(dictionnaire, fichier_ouvert, indent=4, ensure_ascii=False)

with open(ch_stats_anglais, "r") as fichier_ouvert:
    STATS = json.load(fichier_ouvert)

MENU = """

            1) Ajouter des mots et leur traduction

            2) Voir le nombre de mot traduit en tout
            
            000) QUITTER
            
            -------> """
MENU_CHOICES = ["000", "1", "2"]

MENU_TARDUIRE = """

            1) traduire des verbes
            
            2) traduires des adjectifs
            
            3) traduire des determinants
            
            4) traduire des noms communs
            
            5) traduire des nombres
            
            6) traduire autres types
            
            --------> """
MENU_CHOICE_TRADUIRE = ["1", "2", "3", "4", "5", "6"]
type_traduction = "6"


running = True
traduire = False

while running:
    choice = ""
    while choice not in MENU_CHOICES:
        choice = input(MENU)
        choice = choice.strip(" ")
        if choice not in MENU_CHOICES:
            print("\n\n\n Veuillez entrer une option valide")

    if choice == "1":
        traduire = True
    while choice == "1" and traduire == True:
        choice_traduction = ""
        while choice_traduction not in MENU_CHOICE_TRADUIRE:
            choice_traduction = input(MENU_TARDUIRE)
            choice_traduction = choice_traduction.strip(" ")
            if choice_traduction not in MENU_CHOICE_TRADUIRE:
                print("Veuillez choisir une option valide")

        if choice_traduction == "1":
            type_traduction = "verbes"
        elif choice_traduction == "2":
            type_traduction = "adjectifs"
        elif choice_traduction == "3":
            type_traduction = "determinants"
        elif choice_traduction == "4":
            type_traduction = "noms communs"
        elif choice_traduction == "5":
            type_traduction = "nombres"
        elif choice_traduction == "6":
            type_traduction = "autres"

        traduction_mot = True
        while traduction_mot:
            mot_fr = input(f"""\n\n\n\nEntrez le {type_traduction} en français que vous voulez ajouter:                      (Entrez EX pour sortir)
        
---------> """)
            mot_ang = input("""\n\n\n\nPuis sa traduction en anglais:                                                        (Entrez EX pour sortir)       
        
---------> """)

            if mot_ang != "EX" or mot_fr != "EX":

                DB_anglais["dictionnaire_trad_ang_a_fr"][type_traduction][mot_ang] = mot_fr
                DB_anglais["dictionnaire_trad_fr_a_ang"][type_traduction][mot_fr] = mot_ang

                with open(ch_DB_anglais, "w") as fichier_ouvert:
                    json.dump(DB_anglais, fichier_ouvert,
                              indent=4, ensure_ascii=False)

                STATS["total mots appris"]["dictionnaire_trad_ang_a_fr"][type_traduction][mot_ang] = "False"
                STATS["total mots appris"]["dictionnaire_trad_fr_a_ang"][type_traduction][mot_fr] = "False"

                STATS["total mot"] += 1

                with open(ch_stats_anglais, "w") as fichier_ouvert:
                    json.dump(STATS, fichier_ouvert)

            else:
                traduire = False
                traduction_mot = False

    if choice == "2":
        mots_traduits = len(DB_anglais["dictionnaire_trad_ang_a_fr"]["verbes"]) + len(DB_anglais["dictionnaire_trad_ang_a_fr"]["adjectifs"]) + len(DB_anglais["dictionnaire_trad_ang_a_fr"]["noms communs"]) + len(
            DB_anglais["dictionnaire_trad_ang_a_fr"]["nombres"]) + len(DB_anglais["dictionnaire_trad_ang_a_fr"]["autres"]) + len(DB_anglais["dictionnaire_trad_ang_a_fr"]["determinants"])
        print(
            f"\n\n\n\n\nNombre total de mots traduits : {mots_traduits}")
        time.sleep(2)
        choice_2 = input(
            "\n\n\nEntrez n'importe quel caractere pour revenir au menu \n-----> ")

    elif choice == "000":
        running = False
