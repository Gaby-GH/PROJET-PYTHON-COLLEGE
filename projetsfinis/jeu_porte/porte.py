import random
import time
from pathlib import Path
import json

MENU_ACCEUIL = """ 
                                           Bienvenue au jeu de...
                    
                                               ...la porte !
                    
Les règles sont simples :

Plusieurs portes vont vous être montrées, chacune assignée à un numéro, pour choisir quelle porte vous aller traverser,
il faudra simplement entrez le numéro lui correspondant.
Il y a des bonnes portes et des mauvaises portes, si vous choississez une bonne porte vous serez conduis à la prochaine étape,
avec plus de mauvaises portes, mais si vous choississez une mauvaise porte, vous retournerez au départ et devrez tout recommencer !"""

MENU = """
                            -- MENU --           
                            
- Pour jouer entrez 1
- Pour sortir entrez 2
  _____        _____
 /     \      /     \ 
|   1   |    |   2   |
|       |    |       |
|       |    |       |
|_______|    |_______|

-----------> """

MENU_CHOICE = ["1", "2"]

num_manche = 0

MENU_PORTE = f"""                       
                        
                  _____         _____         _____
                 /     \       /     \       /     \ 
                |   1   |     |   2   |     |   3   |
                |       |     |       |     |       |
                |       |     |       |     |       |
                |_______|     |_______|     |_______|


                  _____         _____         _____
                 /     \       /     \       /     \ 
                |   4   |     |   5   |     |   6   |
                |       |     |       |     |       |
                |       |     |       |     |       |
                |_______|     |_______|     |_______| 


                  _____         _____         _____
                 /     \       /     \       /     \ 
                |   7   |     |   8   |     |   9   |
                |       |     |       |     |       |
                |       |     |       |     |       |
                |_______|     |_______|     |_______| 


                -------> """
MENU_CHOICE_PORTE = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


MENU_MANCHE_SUSPENS = """

                    ................
                    
                    """
MENU_MANCHE_PASS = """

             C'est une des bonnes portes !!! 

"""
MENU_MANCHE_PERDU = f"""


                BOUHHHHHH ! C'est la mauvaise porte !

                (Allez rejoue !!!)
                
                
                """

chemin = Path(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\jeu_porte\porte.json")

INTRO = True
GAME = True

while GAME:
    if INTRO == True:
        print(MENU_ACCEUIL)
        time.sleep(5)
        INTRO = False

    with open(chemin, "r") as fichier_open:
        DONNEES_GAME = json.load(fichier_open)
    user_record = DONNEES_GAME["user record"]

    choice = ""
    while choice not in MENU_CHOICE:
        choice = input(MENU)
        choice = choice.strip(" ")
        if choice not in MENU_CHOICE:
            print("Veuillez choisir une option valide !")

    intro = True
    while choice == "1":
        if intro == True:
            print(f"Votre record est de {user_record} !")
            intro = False
            time.sleep(2)

        porte_choice = ""
        num_manche += 1
        print("Manche")
        print(num_manche)
        time.sleep(2.2)

        while porte_choice not in MENU_CHOICE_PORTE:
            porte_choice = input(MENU_PORTE)
            porte_choice = porte_choice.strip("")
            if porte_choice not in MENU_CHOICE_PORTE:
                print("Veuillez choisir une option valide !")

        mauvaise_porte = random.randint(1, 9)
        mauvaise_porte = str(mauvaise_porte)
        une_des_mauvaises_portes = [mauvaise_porte]

        if num_manche >= 2:
            mauvaise_porte_2 = random.randint(1, 9)
            mauvaise_porte_2 = str(mauvaise_porte_2)
            while mauvaise_porte_2 in une_des_mauvaises_portes:
                mauvaise_porte_2 = random.randint(1, 9)
                mauvaise_porte_2 = str(mauvaise_porte_2)
            une_des_mauvaises_portes.append(mauvaise_porte_2)

        elif num_manche >= 3:
            mauvaise_porte_3 = random.randint(1, 9)
            mauvaise_porte_3 = str(mauvaise_porte_3)
            while mauvaise_porte_3 in une_des_mauvaises_portes:
                mauvaise_porte_3 = random.randint(1, 9)
                mauvaise_porte_3 = str(mauvaise_porte_3)
            une_des_mauvaises_portes.append(mauvaise_porte_3)

        elif num_manche >= 4:
            mauvaise_porte_4 = random.randint(1, 9)
            mauvaise_porte_4 = str(mauvaise_porte_4)
            while mauvaise_porte_4 in une_des_mauvaises_portes:
                mauvaise_porte_4 = random.randint(1, 9)
                mauvaise_porte_4 = str(mauvaise_porte_4)
            une_des_mauvaises_portes.append(mauvaise_porte_4)

        elif num_manche >= 5:
            mauvaise_porte_5 = random.randint(1, 9)
            mauvaise_porte_5 = str(mauvaise_porte_5)
            while mauvaise_porte_5 in une_des_mauvaises_portes:
                mauvaise_porte_5 = random.randint(1, 9)
                mauvaise_porte_5 = str(mauvaise_porte_5)
            une_des_mauvaises_portes.append(mauvaise_porte_5)

        elif num_manche >= 6:
            mauvaise_porte_6 = random.randint(1, 9)
            mauvaise_porte_6 = str(mauvaise_porte_6)
            while mauvaise_porte_6 in une_des_mauvaises_portes:
                mauvaise_porte_6 = random.randint(1, 9)
                mauvaise_porte_6 = str(mauvaise_porte_6)
            une_des_mauvaises_portes.append(mauvaise_porte_6)

        elif num_manche >= 7:
            mauvaise_porte_7 = random.randint(1, 9)
            mauvaise_porte_7 = str(mauvaise_porte_7)
            while mauvaise_porte_7 in une_des_mauvaises_portes:
                mauvaise_porte_7 = random.randint(1, 9)
                mauvaise_porte_7 = str(mauvaise_porte_7)
            une_des_mauvaises_portes.append(mauvaise_porte_7)

        elif num_manche >= 8:
            mauvaise_porte_8 = random.randint(1, 9)
            mauvaise_porte_8 = str(mauvaise_porte_8)
            while mauvaise_porte_8 in une_des_mauvaises_portes:
                mauvaise_porte_8 = random.randint(1, 9)
                mauvaise_porte = str(mauvaise_porte_8)
            une_des_mauvaises_portes.append(mauvaise_porte_8)

        print(MENU_MANCHE_SUSPENS)
        time.sleep(int(num_manche))

        if porte_choice not in une_des_mauvaises_portes:
            print(MENU_MANCHE_PASS)
            time.sleep(2)

        elif porte_choice in une_des_mauvaises_portes:
            if num_manche > user_record:
                ancien_record = user_record
                DONNEES_GAME["user record"] = num_manche
                with open(chemin, "w") as fichier_open:
                    json.dump(DONNEES_GAME, fichier_open, ensure_ascii=False)

                print(
                    f"Vous avez battu le record qui était de {ancien_record}, maintenant il est de {num_manche}")
                time.sleep(5)

            print(MENU_MANCHE_PERDU)
            time.sleep(1)
            print("Vous avez tenu")
            time.sleep(1)
            print(num_manche)
            print("manche !")
            time.sleep(4)
            choice = ""

    if choice == "2":
        GAME = False
