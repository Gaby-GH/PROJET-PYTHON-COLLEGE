# faire une aplli avec graphique historique et tout sur la course a pied*

from datetime import date, time, datetime
from pathlib import Path
import json
import random

print("\n\n\n\n\n                           G A R M O N                               ")
print("\nBienvenue sur l'application la plus utilisé par les michentés coureur !")

date_ajrd = date.today()

fleche = 15 * "-"
espace = 50 * "-"

MENU = f"""\n\n\n{espace}
Veuillez entrez le chiffre correspondant à l'action

1) Ajouter une course

2) Voir mes courses

3) Changer d'utilisateur

4) Quitter

{fleche}> """

MENU_CHOICE = ["1", "2", "3", "4", "5"]
MOIS_POSSIBLE = ["janvier", "février", "fevrier", "mars", "avril", "mai", "juin",
                 "juillet", "aout", "août", "septembre", "octobre", "novembre", "décembre", "decembre"]
BASE_DE_DONNEE = ["1", "2"]
BASE_DE_DONNEE_DATES = {"01": "janvier",
                        "02": "Février",
                        "03": "Mars",
                        "04": "Avril",
                        "05": "Mai",
                        "06": "Juin",
                        "07": "Juillet",
                        "08": "Âout",
                        "09": "Septembre",
                        "10": "Octobre",
                        "11": "Novembre",
                        "12": "Décembre", }
LISTE_01 = []
LISTE_02 = []

identification = True
run = True

while identification:
    user = input("""\n\nQui se connecte ?

1) Boris

2) Gabriel

utilisateur : """)
    if user not in BASE_DE_DONNEE:
        print("Veuillez entrez une option valide")
    else:
        if user == "1":
            chemin_don_userjson = Path(
                r"C:\Users\boris\pytonJEU\fichierspycréés\projetencours\garmon.json")
        elif user == "2":
            chemin_don_userjson = Path(
                r"C:\Users\boris\pytonJEU\fichierspycréés\projetencours\garmong.json")

        with open(chemin_don_userjson, "r") as fichier_open:
            liste_course = json.load(fichier_open)

        identification = False

while run:
    while identification:
        user = input("""\n\nQui se connecte ?

1) Boris

2) Gabriel

utilisateur : """)
        if user not in BASE_DE_DONNEE:
            print("Veuillez entrez une option valide")
        else:
            if user == "1":
                chemin_don_userjson = Path(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetencours\garmon.json")
            elif user == "2":
                chemin_don_userjson = Path(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetencours\garmong.json")

            with open(chemin_don_userjson, "r") as fichier_open:
                liste_course = json.load(fichier_open)

            identification = False

    choice = ""
    while choice not in MENU_CHOICE:
        choice = input(MENU)
        if choice not in MENU_CHOICE:
            print("\nVeuillez choisir une option valide")

    choice = str(choice)
    choice = choice.strip(" ")

    if choice == "1":
        print("""\n\nEntrez les données correspondante.
                        \nSi vous n'avez pas certaine données ce n'est pas grave elle seront remplacées par des 0""")

        nom_session = input(f"""\n\nLe type de course, ex : fractionné, libre, épreuve etc....  (facultatif)
{fleche}> """)

        date_session = date.today()
        date_session = str(date_session)
        tiret = date_session[4]
        date_session = date_session.split(tiret)
        annee_session = date_session[0]
        mois_session = date_session[1]
        jour_session = date_session[2]

        nbr_km = input(f"""\n\nLe nombre de kilomètre que vous avez parcouru
{fleche}> Km """)

        temps_H = input(f"""\nLe temps que vous avez pris 
\nEn heure :
{fleche}> """)

        temps_M = input(f"""\nEn minute :
{fleche}> """)

        vitesse_max = input(f"""\nVotre vitesse maximale
{fleche}> Km/h """)

        commentaire = input(f"""\nCommentaire ou note particulière, ex : tour en forêt, UTMB etc... (facultatif)
{fleche}> """)

        choice_sauv = input(f"""\n\n\nPour sauvegarder et retourner au menu entrez 1 ou autre chose
{fleche}> """)

        if nbr_km.isdigit() and temps_H.isdigit() and temps_M.isdigit() and int(temps_M) <= 60:
            nbr_km = nbr_km.strip(" ")
            temps_H = temps_H.strip(" ")
            temps_M = temps_M.strip(" ")
            if temps_H == "":
                temps_H = 0
            temps_TM = int(round(int(temps_M) * (100 / 60)))
            temps_TM = temps_TM / 100
            temps_T = int(temps_H) + int(temps_TM)
            vitesse_moy = int(nbr_km) / int(temps_T)

        else:
            vitesse_moy = None
            print("\nDes données ont étés sûrement mal rentré par une erreur de frappe, elles ont été quand même enregistrées, \nvérifiez et modifiez les données si elles sont fausses")

            vitesse_moy = int(nbr_km) / int()

        num_de_course = liste_course["nombre"]
        liste_course["nombre"] = num_de_course + 1
        str_de_course = "course "
        num_de_course = str(num_de_course)
        nom_de_course = str_de_course + num_de_course

        liste_course[nom_de_course] = {}
        liste_course[nom_de_course]["nom session"] = str(
            nom_session)
        liste_course[nom_de_course]["Annee de la session"] = annee_session
        liste_course[nom_de_course]["Mois de la session"] = mois_session
        liste_course[nom_de_course]["Jour de la session"] = jour_session
        liste_course[nom_de_course]["nbr de kilometre"] = nbr_km
        liste_course[nom_de_course]["Temps minute"] = temps_M
        liste_course[nom_de_course]["Temps heure"] = temps_H
        liste_course[nom_de_course]["vitesse maximum"] = vitesse_max
        liste_course[nom_de_course]["commentaire de session"] = commentaire

        with open(chemin_don_userjson, "w") as fichier_json_open:
            json.dump(liste_course, fichier_json_open,
                      indent=4, ensure_ascii=False)
        if user == "1":
            chemin_don_userjson = Path(
                r"C:\Users\boris\pytonJEU\fichierspycréés\projetencours\garmon.json")
        elif user == "2":
            chemin_don_userjson = Path(
                r"C:\Users\boris\pytonJEU\fichierspycréés\projetencours\garmong.json")

        with open(chemin_don_userjson, "r") as fichier_open:
            liste_course = json.load(fichier_open)
            print("\nCourse saugardée !")

    elif choice == "2":

        date_option_2 = date.today()
        date_option_2 = str(date_option_2)
        tiret = date_option_2[4]
        date_option_2 = date_option_2.split(tiret)
        annee_option_2 = date_option_2[0]
        annee_option_2 = int(annee_option_2)
        mois_option_2 = date_option_2[1]
        mois_option_2 = int(mois_option_2)
        jour_option_2 = date_option_2[2]
        jour_option_2 = int(jour_option_2)
        jour_limite = jour_option_2 - 8

        afficher_quand = input(f"""\n\n\n
1) Sur la semaine

2) Sur le mois

3) Sur l'année

4) Depuis le début

Choisissez sur quelle période vous voulez voir vos données
(Pour revenir au menu entrez un autre caractère)
{fleche}> """)

        afficher_quand = str(afficher_quand)
        afficher_quand = afficher_quand.strip(" ")
        if afficher_quand == "1":
            dictionnaire_de_date = {}
            id_date = 1

            session_effect = False

            for date_deu in liste_course:
                if liste_course[str(date_deu)][int("Mois de la session")] == int(mois_option_2) and liste_course[date_deu][int("Jour de la session")] > jour_limite:
                    session_effect = True
                    dateu_jour = liste_course[date_deu]["Jour de la session"]
                    dateu_mois = liste_course[date_deu]["Mois de la session"]
                    dateu_mois = BASE_DE_DONNEE_DATES[dateu_mois]
                    dateu_annee = liste_course[date_deu]["Année de la session"]
                    name_of_course = liste_course[date_deu]["nom session"]
                    name_of_course = str(name_of_course)
                    name_of_course = name_of_course.strip(" ")
                    if name_of_course == "":
                        name_of_course = "// Course non-nommée //"
                    km_parcouru = liste_course[date_deu]["nbr de kilometre"]
                    temps_TTM = liste_course[date_deu]["Temps minute"]
                    temps_TTH = liste_course[date_deu]["Temps heure"]
                    vitesse_max = liste_course[date_deu]["vitesse maximum"]
                    vitesse_moy = liste_course[date_deu]["Temps"]
                    cmmntr = liste_course[date_deu]["commentaire de session"]
                    cmmntr = str(cmmntr)
                    cmmntr = cmmntr.strip(" ")
                    if cmmntr == "":
                        cmmntr = "// Le michenté n'a pas ajouté de commentaire //"

                    print(
                        f"""\n\nCourse n°{id_date}, faite le {dateu_jour} {dateu_mois} {dateu_annee}

                        Nom de la course : {name_of_course}
                        
 -kilomètre parcouru-            -Temps-             -Vitesse moyenne-      -Vitesse maximum-
|                    |  |                       |  |                   |   |                 |
| {km_parcouru} Km   |  |{temps_TTH}H{temps_TTM}|  |{vitesse_moy}Km/H  |   |{vitesse_max}Km/H|
|____________________|  |_______________________|  |___________________|   |_________________|
                                  
                                  
                    COMMENTAIRE :

{cmmntr}
                                  """)
                    id_date += 1

            if session_effect == False:
                print("\n\nLe michenté n'a malheureusement pas couru cette semaine, allez on se bouge le popotin !!! \n(Ou il a oublié de rentrer une de ses courses !)")

            action = input(
                "\nPour revenir au menu entrez un caractère ! \n------> ")
            if action != liste_course:
                continue

        elif afficher_quand == "2":
            dictionnaire_de_date = {}
            id_date = 1
            session_effect = False

            for date_deu in liste_course:
                if liste_course[date_deu]["Mois de la session"] == str(mois_option_2):
                    session_effect = True
                    dateu_jour = liste_course[date_deu]["Jour de la session"]
                    dateu_mois = liste_course[date_deu]["Mois de la session"]
                    dateu_mois = BASE_DE_DONNEE_DATES[dateu_mois]
                    dateu_annee = liste_course[date_deu]["Année de la session"]
                    name_of_course = liste_course[date_deu]["nom session"]
                    name_of_course = str(name_of_course)
                    name_of_course = name_of_course.strip(" ")
                    if name_of_course == "":
                        name_of_course = "// Course non-nommée //"
                    km_parcouru = liste_course[date_deu]["nbr de kilometre"]
                    temps_TTM = liste_course[date_deu]["Temps minute"]
                    temps_TTH = liste_course[date_deu]["Temps heure"]
                    vitesse_max = liste_course[date_deu]["vitesse maximum"]
                    vitesse_moy = liste_course[date_deu]["Temps"]
                    cmmntr = liste_course[date_deu]["commentaire de session"]
                    cmmntr = str(cmmntr)
                    cmmntr = cmmntr.strip(" ")
                    if cmmntr == "":
                        cmmntr = "// Le michenté n'a pas ajouté de commentaire //"

                    print(
                        f"""\n\nCourse n°{id_date}, faite le {dateu_jour} {dateu_mois} {dateu_annee}

                        Nom de la course : {name_of_course}
                        
 -kilomètre parcouru-           -Temps-             -Vitesse moyenne-      -Vitesse maximum-
|                    |  |                       |  |                  |   |                 |
| {km_parcouru} Km   |  |{temps_TTH}H{temps_TTM}|  |{vitesse_moy}Km/H |   |{vitesse_max}Km/H|
|____________________|  |_______________________|  |__________________|   |_________________|
                                  
                                  
                COMMENTAIRE :

{cmmntr}
                                  """)
                    id_date += 1

            if session_effect == False:
                print("\n\nLe michenté n'a malheureusement pas couru ce mois-ci, allez on se bouge le popotin !!! \n(Ou il a oublié de rentrer une de ses courses !)")

            action = input(
                "\nPour revenir au menu entrez un caractère ! \n------> ")
            if action != liste_course:
                continue

        elif afficher_quand == "3":
            dictionnaire_de_date = {}
            id_date = 1
            session_effect = False

            for date_deu in liste_course:
                for ddateu in date_deu:

                    if liste_course[date_deu]["Annee de la session"] == str(annee_option_2):
                        session_effect = True
                        dateu_jour = liste_course[date_deu]["Jour de la session"]
                        dateu_mois = liste_course[date_deu]["Mois de la session"]
                        dateu_mois = BASE_DE_DONNEE_DATES[dateu_mois]
                        dateu_annee = liste_course[date_deu]["Année de la session"]
                        name_of_course = liste_course[date_deu]["nom session"]
                        name_of_course = str(name_of_course)
                        name_of_course = name_of_course.strip(" ")
                        if name_of_course == "":
                            name_of_course = "// Course non-nommée //"
                        km_parcouru = liste_course[date_deu]["nbr de kilometre"]
                        temps_TTM = liste_course[date_deu]["Temps minute"]
                        temps_TTH = liste_course[date_deu]["Temps heure"]
                        vitesse_max = liste_course[date_deu]["vitesse maximum"]
                        vitesse_moy = liste_course[date_deu]["Temps"]
                        cmmntr = liste_course[date_deu]["commentaire de session"]
                        cmmntr = str(cmmntr)
                        cmmntr = cmmntr.strip(" ")
                        if cmmntr == "":
                            cmmntr = "// Le michenté n'a pas ajouté de commentaire //"

                    print(
                        f"""\n\nCourse n°{id_date}, faite le {dateu_jour} {dateu_mois} {dateu_annee}

                        Nom de la course : {name_of_course}
                        
 -kilomètre parcouru-           -Temps-             -Vitesse moyenne-      -Vitesse maximum-
|                    |  |                       |  |                  |   |                 |
| {km_parcouru} Km   |  |{temps_TTH}H{temps_TTM}|  |{vitesse_moy}Km/H |   |{vitesse_max}Km/H|
|____________________|  |_______________________|  |__________________|   |_________________|
                                  
                                  
                    COMMENTAIRE :

{cmmntr}
                                  """)
                    id_date += 1

            if session_effect == False:
                print("\n\nLe michenté n'a malheureusement pas couru cette année-là, le reveillon à dû être dur, allez on se bouge le popotin !!! \n(Ou il a oublié de rentrer une de ses courses !)")

            action = input(
                "\nPour revenir au menu entrez un caractère ! \n------> ")
            if action != liste_course:
                continue

        elif afficher_quand == "4":
            dictionnaire_de_date = {}
            id_date = 1
            session_effect = False

            for date_deu in liste_course:

                session_effect = True
                dateu_jour = liste_course[date_deu]["Jour de la session"]
                dateu_mois = liste_course[date_deu]["Mois de la session"]
                dateu_mois = BASE_DE_DONNEE_DATES[dateu_mois]
                dateu_annee = liste_course[date_deu]["Année de la session"]
                name_of_course = liste_course[date_deu]["nom session"]
                name_of_course = str(name_of_course)
                name_of_course = name_of_course.strip(" ")
                if name_of_course == "":
                    name_of_course = "// Course non-nommée //"
                km_parcouru = liste_course[date_deu]["nbr de kilometre"]
                temps_TTM = liste_course[date_deu]["Temps minute"]
                temps_TTH = liste_course[date_deu]["Temps heure"]
                vitesse_max = liste_course[date_deu]["vitesse maximum"]
                vitesse_moy = liste_course[date_deu]["Temps"]
                cmmntr = liste_course[date_deu]["commentaire de session"]
                cmmntr = str(cmmntr)
                cmmntr = cmmntr.strip(" ")
                if cmmntr == "":
                    cmmntr = "// Le michenté n'a pas ajouté de commentaire //"

                print(
                    f"""\n\nCourse n°{id_date}, faite le {dateu_jour} {dateu_mois} {dateu_annee}

                    Nom de la course : {name_of_course}
                    
 -kilomètre parcouru-           -Temps-             -Vitesse moyenne-      -Vitesse maximum-
|                    |  |                       |  |                  |   |                 |
| {km_parcouru} Km   |  |{temps_TTH}H{temps_TTM}|  |{vitesse_moy}Km/H |   |{vitesse_max}Km/H|
|____________________|  |_______________________|  |__________________|   |_________________|
                                  
                                  
                    COMMENTAIRE :

{cmmntr}
                                  """)
                id_date += 1

            action = input(
                "\nPour revenir au menu entrez un caractère ! \n------> ")
            if action != liste_course:
                continue

    elif choice == "3":
        identification = True

    elif choice == "4":
        run = False


# DEMANDER JUSTE TEMPS ET NBR KILOMETRE PUIS DIVISER TEMPS PAR KILOMETRE COMME CA PAS BESOIN DE DEMANDER ET EN PLUS DONNEER DE TEMPS EN +
