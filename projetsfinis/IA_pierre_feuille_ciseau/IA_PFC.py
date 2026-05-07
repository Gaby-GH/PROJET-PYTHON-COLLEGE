from pathlib import Path
import random
import json
import time

chemin_json = Path(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\IA_pierre_feuille_ciseau\PFC.json")
with open(chemin_json, "r") as fichier_open:
    DONNEE_PCF = json.load(fichier_open)

MENU = """

                          -- Jeu du --
                           
                  -- Pierre, feuille, ciseau ! --


                
Vous allez jouer contre l'ordinateur, voici l'horthographe à respecter (Les erreurs de majuscules ne sont pas comptées) :

                      Pierre

                      Feuille

                      Ciseau

- Pour commencer une partie entrez 1 !

- Pour regarder les paramètres entrez 2 !

- Pour quitter le jeu entrez 3 !

--------> """
MENU_CHOICE = ["1", "2", "3"]

MENU_GAME = """

Entrez votre choix !

-Rappel écrivez bien dans cette orthographe :

           Pierre  
           Feuille  
           Ciseau  

Si vous n'avez plus besoin du rappel entrez 4

Pour quitter la partie et revenir au menu entrez 5

----------> """
liste_pierre = ["pierre", "piere", "perre", "pieree",
                "pere", "porre", "purre", "p", "pieerre"]
liste_feuille = ["feuille", "feuile", "fuille", "feeuille", "ffeuille", "feuil", "fauille", "fauil", "feuuillle", "feuuille", "euille", "fuille", "feille", "feulle", "feuile", "feuill", "feuille", "cfeuille", "feuilleu", "feuillea", "feuillez", "feuillee", "feuiller", "feuiller", "feuillet", "feuillet", "feuilley", "feuilleu", "feuillei", "feuilleo", "feuillep", "feuilleq", "feuilles", "feuilled",
                 "feuillef", "feuillef", "feuilleg", "feuilleg", "feuilleh", "feuilleh", "feuillej", "feuillek", "feuillel", "feuillel", "feuillem", "feuillew", "feuillex", "feuillec", "feuillev", "feuillev", "feuillev", "feuilleb", "feuillen", "feuille,", "feuilleu;", "feuille;", "feuille:", "feuille!", "feuille1", "feuille2", "feuille3", "feuille4", "feuille5", "feuille6", "feuille7", "feuille8", "feuille9"]
liste_ciseau = [["ciseau", "cisea", "cise", "cis", "ci", "c", "ciseu", "cisaeu", "cisuea", "cisau", "ciseua", "cisseau", "cissau", "sisseau", "sissau", "cciseau", "ciiseau", "cisseau", "ciseeau", "ciseaau", "ciseauu", "ciseaua", "ciseauz", "ciseaue", "ciseaur", "ciseaur", "ciseaut", "ciseaut", "ciseauy", "ciseauu", "ciseaui", "ciseauo", "ciseaup", "ciseauq", "ciseaus", "ciseaud",
                 "ciseauf", "ciseauf", "ciseaug", "ciseaug", "ciseauh", "ciseauh", "ciseauj", "ciseauk", "ciseaul", "ciseaul", "ciseaum", "ciseauw", "ciseaux", "ciseauc", "ciseauv", "ciseauv", "ciseauv", "ciseaub", "ciseaun", "ciseau,", "ciseauu;", "ciseau;", "cisuea", "ciseau:", "ciseau!", "ciseau1", "ciseau2", "ciseau3", "ciseau4", "ciseau5", "ciseau6", "ciseau7", "ciseau8", "ciseau9"]]
MENU_CHOICE_GAME = ["ciseau", "cisea", "cise", "cis", "ci", "c", "ciseu", "cisaeu", "cisuea", "cisau", "ciseua", "cisseau", "cissau", "sisseau", "sissau", "cciseau", "ciiseau", "cisseau", "ciseeau", "ciseaau", "ciseauu", "ciseaua", "ciseauz", "ciseaue", "ciseaur", "ciseaur", "ciseaut", "ciseaut", "ciseauy", "ciseauu", "ciseaui", "ciseauo", "ciseaup", "ciseauq", "ciseaus", "ciseaud",
                    "ciseauf", "ciseauf", "ciseaug", "ciseaug", "ciseauh", "ciseauh", "ciseauj", "ciseauk", "ciseaul", "ciseaul", "ciseaum", "ciseauw", "ciseaux", "ciseauc", "ciseauv", "ciseauv", "ciseauv", "ciseaub", "ciseaun", "ciseau,", "ciseauu;", "ciseau;", "cisuea", "ciseau:", "ciseau!", "ciseau1", "ciseau2", "ciseau3", "ciseau4", "ciseau5", "ciseau6", "ciseau7", "ciseau8", "ciseau9", "pierre", "piere", "perre", "pieree", "pere", "porre", "purre", "p", "pieerre", "feuille", "feuile", "fuille", "feeuille", "ffeuille", "feuil", "fauille", "fauil", "feuuillle", "feuuille", "euille", "fuille", "feille", "feulle", "feuile", "feuill", "feuille", "cfeuille", "feuilleu", "feuillea", "feuillez", "feuillee", "feuiller", "feuiller", "feuillet", "feuillet", "feuilley", "feuilleu", "feuillei", "feuilleo", "feuillep", "feuilleq", "feuilles", "feuilled",
                    "feuillef", "feuillef", "feuilleg", "feuilleg", "feuilleh", "feuilleh", "feuillej", "feuillek", "feuillel", "feuillel", "feuillem", "feuillew", "feuillex", "feuillec", "feuillev", "feuillev", "feuillev", "feuilleb", "feuillen", "feuille,", "feuilleu;", "feuille;", "feuille:", "feuille!", "feuille1", "feuille2", "feuille3", "feuille4", "feuille5", "feuille6", "feuille7", "feuille8", "feuille9", "4", "5"]


nbr_partie_jouées = DONNEE_PCF["Partie_play"]
win_user = DONNEE_PCF["WIN_user"]
win_IA = DONNEE_PCF["WIN_IA"]
MENU_PARAMETRE = f"""

- Parties jouées : {nbr_partie_jouées}

- Parties gagnées par les utilisateurs : {win_user}

- Parties gagnées par l'ordinateur (l'IA de michente) : {win_IA}


Pour revenir au menu entrez 1 :
--------> """
MENU_PARAMETRE_CHOICE = ["1"]

choice_game_user = ""
premiere_partie = 1
game = True

while game:
    choice = ""
    while choice not in MENU_CHOICE:
        choice = input(MENU)
        choice = choice.strip(" ")
        if choice not in MENU_CHOICE:
            print("\nVeuillez selectionner une option valide")
            time.sleep(3)

    if choice == "1":
        game_in_game = True
    while game_in_game:

        if premiere_partie == 1:
            print("\n\nPartie lancée ! \nBonne chance !")
            time.sleep(3)
            premiere_partie += 1

        choice_game = ""
        while choice_game not in MENU_CHOICE_GAME:
            choice_game = input(MENU_GAME)
            choice_game = choice_game.lower()
            choice_game = choice_game.strip(" ")
            if choice_game not in MENU_CHOICE_GAME:
                print("\nVeuillez choisir une option valide !")

        if choice_game != "5" and choice_game != "4":

            if choice_game in liste_pierre:
                choice_game_user = "Pierre"
            elif choice_game in liste_feuille:
                choice_game_user = "Feuille"
            elif choice_game in liste_ciseau:
                choice_game_user = "Ciseau"

            chance_pierre = DONNEE_PCF["Pierre"]
            chance_feuille = DONNEE_PCF["Feuille"]
            chance_ciseau = DONNEE_PCF["Ciseau"]
            ATK = random.randint(1, 300)

            if ATK <= chance_pierre:
                choix_IA = "Pierre"

            elif ATK > chance_pierre and ATK <= chance_feuille:
                choix_IA = "Feuille"

            elif ATK > chance_feuille and ATK <= chance_ciseau:
                choix_IA = "Ciseau"

            time.sleep(0.5)
            print(f"\nL'ordinateur lance {choix_IA} !")
            time.sleep(0.5)

            if choice_game_user == choix_IA:
                print("\nEgalité, personne ne gagne !")
                time.sleep(1)

            elif choice_game_user != choix_IA:

                phrase_loose = f"\nVous perdez, {choice_game_user} perd contre {choix_IA} !"
                phrase_win = f"\nVous gagnez, {choice_game_user} gagne contre {choix_IA} !"

                if choice_game_user == "Pierre":
                    if choix_IA == "Ciseau":
                        DONNEE_PCF["WIN_user"] += 1
                        print(phrase_win)

                        DONNEE_PCF["Feuille"] += 0.5

                    elif choix_IA == "Feuille":
                        DONNEE_PCF["WIN_IA"] += 1
                        print(phrase_loose)

                        DONNEE_PCF["Feuille"] += 0.25
                        DONNEE_PCF["Pierre"] -= 0.25

                elif choice_game_user == "Feuille":
                    if choix_IA == "Pierre":
                        DONNEE_PCF["WIN_user"] += 1
                        print(phrase_win)

                        DONNEE_PCF["Pierre"] -= 0.5
                        DONNEE_PCF["Feuille"] -= 0.5

                    elif choix_IA == "Ciseau":
                        DONNEE_PCF["WIN_IA"] += 1
                        print(phrase_loose)

                        DONNEE_PCF["Pierre"] -= 0.25
                        DONNEE_PCF["Feuille"] -= 0.5

                elif choice_game_user == "Ciseau":
                    if choix_IA == "Pierre":
                        DONNEE_PCF["WIN_IA"] += 1
                        print(phrase_loose)

                        DONNEE_PCF["Pierre"] += 0.5
                        DONNEE_PCF["Feuille"] += 0.25

                    elif choix_IA == "Feuille":
                        DONNEE_PCF["WIN_user"] += 1
                        print(phrase_win)

                        DONNEE_PCF["Pierre"] += 0.5

            DONNEE_PCF["Partie_play"] += 1
            with open(chemin_json, "w") as fichier_open:
                json.dump(DONNEE_PCF, fichier_open,
                          ensure_ascii=False, indent=4)

            time.sleep(1.5)

        if choice_game == "4":
            MENU_GAME = """

Entrez votre choix !

Pour quitter la partie entrez 5

----------> """

        if choice_game == "5":
            game_in_game = False

    if choice == "2":
        nbr_partie_jouées = DONNEE_PCF["Partie_play"]
        win_user = DONNEE_PCF["WIN_user"]
        win_IA = DONNEE_PCF["WIN_IA"]
        MENU_PARAMETRE = f"""

- Parties jouées : {nbr_partie_jouées}

- Parties gagnées par les utilisateurs : {win_user}

- Parties gagnées par l'ordinateur (l'IA de michente) : {win_IA}


Pour revenir au menu entrez 1 :
--------> """

        choice_parametre = ""
        while choice_parametre not in MENU_PARAMETRE_CHOICE:
            choice_parametre = input(MENU_PARAMETRE)
            if choice_parametre not in MENU_PARAMETRE_CHOICE:
                print("Veuillez choisir une option valide")

    if choice == "3":
        print("\nVous quittez le jeu, revenez vite !")
        time.sleep(1)
        print("""

                _________
               /         \       
              |           |      
              |           |      
               \_________/   """)
        time.sleep(1)
        print(""" 
                __________ 
               /         /
              /         /
             /         / 
            /         /
           /_________/ """)
        time.sleep(1)
        print("""
        
                      /
               __    /
              |__|__/_____
                   /__      
                  /__/ """)

        game = False
