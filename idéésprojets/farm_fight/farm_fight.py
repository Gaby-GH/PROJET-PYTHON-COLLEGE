import random
from pathlib import Path
import time
import json
a = 1


dossier_parent = Path(__file__).parent
ch_farm_fight_json = dossier_parent / "farm_fight.json"


if not ch_farm_fight_json.exists():
    with open(ch_farm_fight_json, "w") as fichier_ouvert:
        inseration = {"Temps de jeu": 0, "Nombre de kill": 0}
        json.dump(inseration, fichier_ouvert, indent=4, ensure_ascii=False)
else:
    with open(ch_farm_fight_json, "r") as fichier_ouvert:
        DB_JEU = json.load(fichier_ouvert)


debut_jeu = time.time()

MENU = fr"""



                                                     ______________________
                                                    /                      \
                                                   |                        |
                                                   |  /|       AVENTURE     |
                                                   |  _|_                   |
                                                    \______________________/
               
                                                     ______________________
                                                    /                      \
                                                   |   __     PERSONNAGE    |
                                                   |   __|        &         |
                                                   |  |__    AMELIORATION   |
                                                    \______________________/

                                                     ______________________
                                                    /                      \
                                                   |   __     DONNEES       |
                                                   |   __|       &          |
                                                   |   __|   PARAMETRES     |
                                                    \______________________/

                                                     ______________________
                                                    /                      \
                                                   |   __                   |
                                                   |  | /|    QUITTER       |
                                                   |  |/_|                  |
                                                    \______________________/


                                                    Choice : """
MENU_CHOICE = ["0", "1", "2", "3"]


def intro_aventure():
    print(f"\n\n\n Bienvenue dans l'aventure !")
    time.sleep(2)
    temps_de_jeu_total = DB_JEU["Temps de jeu"]
    minute_jeu_total = temps_de_jeu_total / 60
    heure_jeu_total = minute_jeu_total / 60
    temps_de_jeu_total_phrase = f"{heure_jeu_total} H"
    nbr_total_kill = DB_JEU["Nombre de kill"]
    print(
        f"\n\n\nVous avez {temps_de_jeu_total_phrase} de jeu et un nombre total de kill de {nbr_total_kill} !\nBonne chance !")
    time.sleep(2)


MENU_AVENTURE = """


                                                   MAP 

                         ___________________________________________________________
                        |                                                           |
                        |                                                           |
                        |                                                           |
                        |                                                           |
                        |                                                           |
                        |                                                           |
                        |                                                           |
                        |                                                           |
                        |                                                           |
                        |                                                           |
                        |                                                           |
                        |                                                           |
                        |                                                           |
                        |                                                           |
                        |___________________________________________________________|










"""

running = True

while running:

    choice = ""
    while choice not in MENU_CHOICE:

        choice = input(MENU)
        choice = choice.strip(" ")

        if choice not in MENU_CHOICE:
            print(f"{choice} n'est pas une option valable")

    if choice == "1":
        intro_aventure()

    elif choice == "2":
        pass

    elif choice == "3":
        pass

    elif choice == "0":
        running = False


fin_jeu = time.time()
temps_de_jeu = fin_jeu - debut_jeu
