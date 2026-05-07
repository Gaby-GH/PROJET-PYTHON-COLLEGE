import random
from pathlib import Path
import json

dossier_parent = Path(__file__).parent
ch_DB_peche = dossier_parent / "peche.json"

if ch_DB_peche.exists():
    with open(ch_DB_peche, "r") as fichier_ouvert:
        DB_peche = json.load(fichier_ouvert)
else:
    insertion = {"temps de jeu": 0,
                 "nbr de poisson peche": 0, "poisson peche": []}

MENU = r"""





                                                     ______________________
                                                    /                      \
                                                   |                        |
                                                   |  /|       PECHER       |
                                                   |  _|_                   |
                                                    \______________________/
               
                                                     ______________________
                                                    /                      \
                                                   |   __     AMELIORER     |
                                                   |   __|      CANNE       |
                                                   |  |__      A PECHE      |
                                                    \______________________/

                                                     ______________________
                                                    /                      \
                                                   |   __      MES          |
                                                   |   __|    PRISES        |
                                                   |   __|                  |
                                                    \______________________/

                                                     ______________________
                                                    /                      \
                                                   |   __                   |
                                                   |  |  |    QUITTER       |
                                                   |  |__|                  |
                                                    \______________________/
                                                    
                                                    Choix : """
MENU_CHOICE = ["0", "1", "2", "3"]

running = True

while running:
    choice = ""
    while choice not in MENU_CHOICE:
        choice = input(MENU)
        choice = choice.strip()
        if choice not in MENU_CHOICE:
            print(f"{choice} n'est pas une option valide !")

    if choice == "1":
        pass
