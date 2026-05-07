import json
import time
from datetime import date, datetime
from pathlib import Path
import random

heure_open = time.time()

chemin_fich_json = Path(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetencours\JDR.json")
with open(chemin_fich_json, "r") as fich_open:
    DONNEES_GAME = json.load(fich_open)

capital_user = DONNEES_GAME["CAPITAL"]["user"]
user_heures_de_jeu = DONNEES_GAME["Temps de jeu"]["heures"]
user_minutes_de_jeu = DONNEES_GAME["Temps de jeu"]["minutes"]

MENU_1 = f"""

                                     __  
                                    /  \ 
                                   | $$ |
                                    \__/
                                     ||
                                     ||
                                     ||
                                     ||
                                   _|  |_ 
                                __|      |__                           
                               |____________|                         
                          |||||             |||||                    
                      ||||                       ||||                 
                   |||       -- Trad' Heure --       |||                   
                |||_____________________________________|||
                |_________________________________________| 
                | |     ___                             | |                          
                | |    |   |    Bureau et affaire       | |__________________________                          
                | |    | 1 |                            | |__________________________\        
                | |____|___|____________________________| |      CAPITAL ACTUEL :     |   
                | |                                     | |                           | 
                |_|_____________________________________|_|  {capital_user} $                       
                | |     ___                             | |___________________________|               
                | |    |   |        QUITTER             | |___________________________\   
                | |    | 4 |                            | | Entrez le numéro de l'étage|
________________|_|____|___|____________________________|_| au-quel vous voulez accéder ---> """

MENU_2 = f"""

                                     __  
                                    /  \ 
                                   | $$ |
                                    \__/
                                     ||
                                     ||
                                     ||
                                     ||
                                   _|  |_ 
                                __|      |__                           
                               |____________|                         
                          |||||             |||||                    
                      ||||                       ||||                 
                   |||       -- Trad' Heure --       |||                   
                |||_____________________________________|||
                |_________________________________________|
                | |     ___                             | | 
                | |    |   |    Bureau et affaire       | |  
                | |    | 1 |                            | |__________________________
                | |____|___|____________________________| |__________________________\ 
                | |                                     | |    -- CAPITAL ACTUEL --   |
                |_|_____________________________________|_|                           |
                | |     ___                             | |  {capital_user} $
                | |    |   |        Employer            | |___________________________|  
                | |    | 2 |                            | |___________________________\ 
                | |____|___|____________________________| |    -- HEURES DE JEU --     |
                | |                                     | |                            | 
                |_|_____________________________________|_|  {user_heures_de_jeu} H
                | |     ___                             | |____________________________|
                | |    |   |        QUITTER             | |____________________________\  
                | |    | 4 |                            | | Entrez le numéro de l'étage |
________________|_|____|___|____________________________|_| au-quel vous voulez accéder ---> """

MENU_3 = f"""

                                     __  
                                    /  \ 
                                   | $$ |
                                    \__/
                                     ||
                                     ||
                                     ||
                                     ||
                                   _|  |_ 
                                __|      |__                           
                               |____________|                         
                          |||||             |||||                    
                      ||||                       ||||                 
                   |||       -- Trad' Heure --       |||                   
                |||_____________________________________|||
                |_________________________________________|
                | |     ___                             | | 
                | |    |   |    Bureau et affaire       | |  
                | |    | 1 |                            | |
                | |____|___|____________________________| |
                | |                                     | |
                |_|_____________________________________|_| 
                | |     ___                             | | 
                | |    |   |        Employer            | |  
                | |    | 2 |                            | |__________________________
                | |____|___|____________________________| |__________________________\ 
                | |                                     | |    -- CAPITAL ACTUEL --   | 
                |_|_____________________________________|_|                           |
                | |     ___                             | |  {capital_user} $
                | |    |   |        Boutique            | |___________________________|  
                | |    | 3 |                            | |___________________________\ 
                | |____|___|____________________________| |    -- HEURES DE JEU --     |                          
                | |                                     | |                            |
                |_|_____________________________________|_|  {user_heures_de_jeu} H 
                | |     ___                             | |____________________________|
                | |    |   |        QUITTER             | |____________________________\  
                | |    | 4 |                            | | Entrez le numéro de l'étage |
________________|_|____|___|____________________________|_| au-quel vous voulez accéder ---> """


MENU_CHOICE_1 = ["1", "4"]
MENU_CHOICE_2 = ["1", "2", "4"]
MENU_CHOICE_3 = ["1", "2", "3", "4"]

MENU = MENU_1
MENU_CHOICE = MENU_CHOICE_1

if DONNEES_GAME["MENU"] == 1:
    MENU = MENU_1
    MENU_CHOICE = MENU_CHOICE_1
elif DONNEES_GAME["MENU"] == 2:
    MENU = MENU_2
    MENU_CHOICE = MENU_CHOICE_2
elif DONNEES_GAME["MENU"] == 3:
    MENU = MENU_3
    MENU_CHOICE = MENU_CHOICE_3


MENU_BUREAU_1 = """

                                                         -- BUREAU --

                                                 ___
                                                / 0 \ 
                                                \___/
                             ____________________|_|______________________
                            /                 __________                  \ 
                           |                 /1| Voir et\                  |
                           |                | gérer mes  |                 |
                           |                | buisness $ |                 |
                           |                 \__________/                  |
                           |                                               |
___________                |                  __________                   |               
           \               |                 /2| Voir   \                  |
     _      |              |                | mes défis  |                 |
    |5|     |              |                | et stats   |                 |            
            |              |                 \__________/                  |
            |               \_____________________________________________/                    
  SORTIR    |                                    | | 
            |                     _______________| |______________________________________________________________
            |                    /       ________| |________                                                     /|        
            |                   /       |___________________|                                                   /||         
            |                  /                                                                               / ||     
            |                 /         _____________________      _________                                  /  ||   
            |                /         ||1|2|3|4|5|6|7|8|9|0||    /    _    \                                /   ||
____________|               /          ||a|z|e|r|t|y|u|i|o|p||   |    /|\    |                              /    ||             
                           /           ||q|s|d|f|g|h|j|k|l|m||   |   | | |   |                             /     || 
                          /            ||w|x|c|v|b|n|?|;|/|!||   |   \___/   |                            /      || 
                         /             |_____________________|    \_________/                            /       ||    
                        /_______________________________________________________________________________/|       ||
                        ||       ||                                                                    |||       ||                                  
                        ||       ||                                                                    |||       ||          
                        ||                                                                             |||                       
                        ||                                                                             |||          
                        ||                                                                             |||           
                        ||                                                                             |||          
                        ||                                                                             |||        ___________________________________    
                        ||                                                                             |||       /          
                        ||                                                                             |||      |Entrez le numéro correspondant
                                                                                                                |à l'action que vous voulez effectuer
                                                                                                                |
                                                                                                                |--------> """

MENU_BUREAU_2 = """

                                                         -- BUREAU --

                                                 ___
                                                / 0 \ 
                                                \___/
                             ____________________|_|______________________
                            /      __________             __________      \ 
                           |      /1| Voir et\           /3| Voir et\      |
                           |     | gérer mes  |         | gérer mes  |     |
                           |     | buisness $ |         | employés   |     |
                           |      \__________/           \__________/      |
                           |                                               |
___________                |       __________                              |               
           \               |      /2| Voir   \                             |
     _      |              |     | mes défis  |                            |
    |5|     |              |     | et stats   |                            |            
            |              |      \__________/                             |
            |               \_____________________________________________/                    
  SORTIR    |                                    | | 
            |                     _______________| |______________________________________________________________
            |                    /       ________| |________                                                     /|        
            |                   /       |___________________|                                                   /||         
            |                  /                                                                               / ||     
            |                 /         _____________________      _________                                  /  ||   
            |                /         ||1|2|3|4|5|6|7|8|9|0||    /    _    \                                /   ||
____________|               /          ||a|z|e|r|t|y|u|i|o|p||   |    /|\    |                              /    ||             
                           /           ||q|s|d|f|g|h|j|k|l|m||   |   | | |   |                             /     || 
                          /            ||w|x|c|v|b|n|?|;|/|!||   |   \___/   |                            /      || 
                         /             |_____________________|    \_________/                            /       ||    
                        /_______________________________________________________________________________/|       ||
                        ||       ||                                                                    |||       ||                                  
                        ||       ||                                                                    |||       ||          
                        ||                                                                             |||                       
                        ||                                                                             |||          
                        ||                                                                             |||           
                        ||                                                                             |||          
                        ||                                                                             |||        ___________________________________    
                        ||                                                                             |||       /          
                        ||                                                                             |||      |Entrez le numéro correspondant
                                                                                                                |à l'action que vous voulez effectuer
                                                                                                                |
                                                                                                                |--------> """

MENU_CHOICE_BUREAU_1 = ["1", "2", "5"]
MENU_CHOICE_BUREAU_2 = ["1", "2", "3", "5"]

MENU_BUREAU = MENU_BUREAU_1
MENU_CHOICE_BUREAU = MENU_CHOICE_BUREAU_1

if DONNEES_GAME["MENU BUREAU"] == 1:
    MENU_BUREAU = MENU_BUREAU_1
    MENU_CHOICE_BUREAU = MENU_CHOICE_BUREAU_1
elif DONNEES_GAME["MENU BUREAU"] == 2:
    MENU_BUREAU = MENU_BUREAU_2
    MENU_CHOICE_BUREAU = MENU_CHOICE_BUREAU_2

MENU_BUISNESS = """

                                            -- BUISNESS --                          

      ________________________________                            ________________________________                 
     /      |                         \                          /      |                         \                                                       
    /       |                  _|_|_   \                        /       |                    /     \ 
   |        |                 _||   \   |                      |   __   |            ___    /       |  
   |   /|   |  CRYPTOMONNAIE  _||___/   |                      |   __|  |  BOURSE   /   \  /        |
   |   _|_  |                  ||   \   |                      |  |__   |          /     \/         |                                  
   |        |                  ||___/   |                      |        |         /                 |              
    \       |                   | |    /                        \       |                          /             
     \______|_________________________/                          \______|_________________________/


    ____________
  / / \         \                 |Choississez le numéro correspondant au 
 | | 3 | BUREAU  |                |domaine dans lequel vous voulez investir
  \_\_/_________/                 |---------> """
MENU_CHOICE_BUISNESS = ["1", "2", "3"]

capital_user = DONNEES_GAME["CAPITAL"]["user"]

VALEUR_bitcoin = DONNEES_GAME["CRYPTOMONNAIE"]["bitcoin"]
VALEUR_ethereum = DONNEES_GAME["CRYPTOMONNAIE"]["ethereum"]
VALEUR_tether = DONNEES_GAME["CRYPTOMONNAIE"]["tether"]
VALEUR_bnb = DONNEES_GAME["CRYPTOMONNAIE"]["bnb"]
VALEUR_xrp = DONNEES_GAME["CRYPTOMONNAIE"]["xrp"]
VALEUR_dogecoin = DONNEES_GAME["CRYPTOMONNAIE"]["dogecoin"]
VALEUR_polygon = DONNEES_GAME["CRYPTOMONNAIE"]["polygon"]
VALEUR_solana = DONNEES_GAME["CRYPTOMONNAIE"]["solana"]
VALEUR_litecoin = DONNEES_GAME["CRYPTOMONNAIE"]["litcoin"]
VALEUR_cosmos = DONNEES_GAME["CRYPTOMONNAIE"]["cosmos"]

det_bitcoin = DONNEES_GAME["CRYPTOMONNAIE_DETENU"]["bitcoin"]
det_ethereum = DONNEES_GAME["CRYPTOMONNAIE_DETENU"]["ethereum"]
det_tether = DONNEES_GAME["CRYPTOMONNAIE_DETENU"]["tether"]
det_bnb = DONNEES_GAME["CRYPTOMONNAIE_DETENU"]["bnb"]
det_xrp = DONNEES_GAME["CRYPTOMONNAIE_DETENU"]["xrp"]
det_dogecoin = DONNEES_GAME["CRYPTOMONNAIE_DETENU"]["dogecoin"]
det_polygon = DONNEES_GAME["CRYPTOMONNAIE_DETENU"]["polygon"]
det_solana = DONNEES_GAME["CRYPTOMONNAIE_DETENU"]["solana"]
det_litecoin = DONNEES_GAME["CRYPTOMONNAIE_DETENU"]["litcoin"]
det_cosmos = DONNEES_GAME["CRYPTOMONNAIE_DETENU"]["cosmos"]

MENU_CRYPTO = f"""




                                            -- CRYPTOMONNAIE --

                                                                                     
 #1  -- LISTE A --

  
 #0 -- Retour au menu buisness --


Entrez le numéro correspondant à la liste que vous voulez séléctionner

--------> """
MENU_CHOICE_CRYPTO_LISTE = ["0", "1"]

MENU_CRYPTO_A = f"""

                                            -- CRYPTOMONNAIE -- 

MON CAPITAL : {capital_user}                                                
                                               
  _____________________________________________________________________________________________________     
 /                                         |          quantité                                         \ 
|          NOM             VALEUR          |          détenue                  bénéfices                |
 \_________________________________________|___________________________________________________________/

                                      -- LISTE A --
                                            
                                            
 #1     Bitcoin         {VALEUR_bitcoin} $               {det_bitcoin}
                                            
 #2     Ethereum        {VALEUR_ethereum} $              {det_ethereum}                  
                                            
 #3     Tether          {VALEUR_tether} $                  {det_tether}

 #4     BNB             {VALEUR_bnb} $                     {det_bnb}

 #5     XRP             {VALEUR_xrp} $                      {det_xrp}
                                                            
 #6     Dogecoin        {VALEUR_dogecoin} $                 {det_dogecoin}       

 #7     Polygon         {VALEUR_polygon} $                   {det_polygon}

 #8     Solana          {VALEUR_solana} $                    {det_solana} 

 #9     Litecoin        {VALEUR_litecoin} $                   {det_litecoin}

 #10    Cosmos          {VALEUR_cosmos} $                     {det_cosmos}               
                                            
                                                                              
Choississez ce que vous voulez faire :                                           
     _______________       _______________       _______________       _______________       _______________         
    /  |            \     /  |            \     /  |Voir autres \     /  | Retour au  \     /  | Retour au  \ 
   | 1 |   Acheter   |   | 2 |   Vendre    |   | 3 |   listes    |   | 4 |menu buisness|   | 5 |  BUREAU     |
    \__|____________/     \__|____________/     \__|____________/     \__|____________/     \__|____________/

-------------> """
MENU_CHOICE_CRYPTO_A = ["1", "2", "3", "4", "5"]

MENU_CRYPTO_ACH_A = f"""

                                            -- CRYPTOMONNAIE -- 

MON CAPITAL : {capital_user}                                                
                                               
                         _________________________________________     
                        /                                         \ 
                       |          NOM             VALEUR           |
                        \_________________________________________/

                                      -- LISTE A --
                                            
                                            
                         #1     Bitcoin         {VALEUR_bitcoin} $  
                                                       
                         #2     Ethereum        {VALEUR_ethereum} $                             
                                            
                         #3     Tether          {VALEUR_tether} $              
 
                         #4     BNB             {VALEUR_bnb} $         
 
                         #5     XRP             {VALEUR_xrp} $                                                                     
 
                         #6     Dogecoin        {VALEUR_dogecoin} $                  

                         #7     Polygon         {VALEUR_polygon} $ 
            
                         #8     Solana          {VALEUR_solana} $   
           
                         #9     Litecoin        {VALEUR_litecoin} $           

                         #10    Cosmos          {VALEUR_cosmos} $

                         #0     Retour au menu de la liste A                         
                                            
Entrez le chiffre correspondant a la cryptomonnaie que vous voulez acheter

-------------> """
MENU_CHOICE_CRYPTO_ACH_A = ["0", "1", "2",
                            "3", "4", "5", "6", "7", "8", "9", "10"]


crypto_ach_val_choice = "§§§§§§"
argent_en_moins = "§§§§§§"
valeur_crypto_ach = "§§§§§§s"
MENU_ACHAT_CRYPTO_REUSSI = f"""

                                -- Achat confirmé ! --

        Vous avez dépensé {argent_en_moins} $ pour acheter et investir dans du {crypto_ach_val_choice} !

        La valeur du {crypto_ach_val_choice} est actuellement de {valeur_crypto_ach} !"""
GAME = True

while GAME:

    # INTRO (
    if DONNEES_GAME["pseudo"] == " ":
        pseudo = input(
            "\nRentre ton nom d'investisseur ! (pourra être modifier plus tard :)\n--------> ")
        DONNEES_GAME["pseudo"] = pseudo
        print("\nBienvenue dans trad'heure !!!")
        time.sleep(2)
        print(f"\n\nBonne chance et travail dûr {pseudo} !")
        time.sleep(1)
        print(f"""\nTéléchargement du jeu :""")

        load_game = True
        baton_load = "|"
        pourcentage_load = 5
        barre_load = baton_load * pourcentage_load
        round_round = 1
        load_boucle = "-"
        round_boucle = 1
        while load_game:

            if round_boucle == 1:
                load_boucle = ""
                round_boucle = 2

            elif round_boucle == 2:
                load_boucle = ""
                round_boucle = 3

            elif round_boucle == 3:
                load_boucle = ""
                round_boucle = 4

            elif round_boucle == 4:
                load_boucle = ""
                round_boucle = 1

            if round_round == 1:
                baton_load = "|"
                pourcentage_load = 5
                barre_load = baton_load * pourcentage_load
            barre_load = baton_load * pourcentage_load
            print(f"{barre_load} {pourcentage_load}%   {load_boucle}")
            pourcentage_load += 1
            barre_load = baton_load * pourcentage_load
            time.sleep(0.09)
            round_round += 1
            if pourcentage_load == 100:
                load_game = False

        with open(chemin_fich_json, "w") as fich_open:
            json.dump(DONNEES_GAME, fich_open, indent=4, ensure_ascii=False)
    pseudo = DONNEES_GAME["pseudo"]
    # INTRO )

    choice = ""
    while choice not in MENU_CHOICE:
        choice = input(MENU)
        choice = choice.strip(" ")
        if choice not in MENU_CHOICE:
            print(f"\n{choice} n'est pas une option valide")
            time.sleep(2)

    choice = choice.strip(" ")

    while choice == "1":
        choice_bureau = ""
        while choice_bureau not in MENU_CHOICE_BUREAU:
            choice_bureau = input(MENU_BUREAU)
            choice_bureau = choice_bureau.strip(" ")
            if choice_bureau not in MENU_CHOICE_BUREAU:
                print(f"{choice_bureau} n'est pas une option valide")
                time.sleep(2)

        choice_bureau = choice_bureau.strip(" ")

        while choice_bureau == "1":
            choice_buisness = ""
            while choice_buisness not in MENU_CHOICE_BUISNESS:
                choice_buisness = input(MENU_BUISNESS)
                choice_buisness = choice_buisness.strip(" ")
                if choice_buisness not in MENU_BUISNESS:
                    print("\nVeuillez choisir une option valide")

            while choice_buisness == "1":
                choice_crypto_liste = ""
                while choice_crypto_liste not in MENU_CHOICE_CRYPTO_LISTE:
                    choice_crypto_liste = input(MENU_CRYPTO)
                    choice_crypto_liste = choice_crypto_liste.strip(" ")
                    if choice_crypto_liste not in MENU_CHOICE_CRYPTO_LISTE:
                        print("\nVeuillez rentrez une option valide")

                while choice_crypto_liste == "1":
                    choice_crypto_liste_A = ""
                    while choice_crypto_liste_A not in MENU_CHOICE_CRYPTO_A:
                        choice_crypto_liste_A = input(MENU_CRYPTO_A)
                        choice_crypto_liste_A = choice_crypto_liste_A.strip(
                            " ")
                        if choice_crypto_liste_A not in MENU_CHOICE_CRYPTO_A:
                            print("\nVeuillez choisir une option valide")
                            time.sleep(3)

                    # ACHETER (

                    while choice_crypto_liste_A == "1":
                        choice_crypto_ach_liste_A = ""
                        while choice_crypto_ach_liste_A not in MENU_CHOICE_CRYPTO_ACH_A:
                            choice_crypto_ach_liste_A = input(
                                MENU_CRYPTO_ACH_A)
                            choice_crypto_ach_liste_A = choice_crypto_ach_liste_A.strip(
                                " ")
                            if choice_crypto_ach_liste_A not in MENU_CHOICE_CRYPTO_ACH_A:
                                print("\nVeuillez séléctionner une option valide")

                        if choice_crypto_ach_liste_A != "0":
                            if choice_crypto_ach_liste_A == "1":
                                crypto_ach = "bitcoin"
                            elif choice_crypto_ach_liste_A == "2":
                                crypto_ach = "Ethereum"
                            elif choice_crypto_ach_liste_A == "3":
                                crypto_ach = "Tether"
                            elif choice_crypto_ach_liste_A == "4":
                                crypto_ach = "BNB"
                            elif choice_crypto_ach_liste_A == "5":
                                crypto_ach = "XRP"
                            elif choice_crypto_ach_liste_A == "6":
                                crypto_ach = "Dogecoin"
                            elif choice_crypto_ach_liste_A == "7":
                                crypto_ach = "Polygon"
                            elif choice_crypto_ach_liste_A == "8":
                                crypto_ach = "Solana"
                            elif choice_crypto_ach_liste_A == "9":
                                crypto_ach = "Litcoin"
                            elif choice_crypto_ach_liste_A == "10":
                                crypto_ach = "Cosmos"
                            MENU_CRYPTO_NOMBRE_ACH_A = f"""

Combien voulez vous acheter de {crypto_ach} ? (Pour retourner au menu des liste de cryptomonnaie entrez 0)

------------> """

                            valeur_crypto_ach = DONNEES_GAME["CRYPTOMONNAIE"][crypto_ach]
                            capital_user = DONNEES_GAME["CAPITAL"]["user"]
                            crypto_ach_val_choice = ""
                            while not crypto_ach_val_choice.isdigit() or int(crypto_ach_val_choice) < 0:
                                crypto_ach_val_choice = input(
                                    MENU_CRYPTO_NOMBRE_ACH_A)
                                crypto_ach_val_choice = crypto_ach_val_choice.strip(
                                    " ")
                                if not crypto_ach_val_choice.isdigit() or int(crypto_ach_val_choice) < 0:
                                    print("Veuillez choisir une option valide")

                            crypto_ach_val_choice = int(crypto_ach_val_choice)
                            if (crypto_ach_val_choice * valeur_crypto_ach) < capital_user and DONNEES_GAME["CRYPTOMONNAIE_DETENU"][crypto_ach] == 0:

                                argent_en_moins = crypto_ach_val_choice * valeur_crypto_ach
                                DONNEES_GAME["CAPITAL"]["user"] -= argent_en_moins
                                capital_user = DONNEES_GAME["CAPITAL"]["user"]

                                crypto_ach = DONNEES_GAME["CRYPTOMONAIE_selec"][choice_crypto_ach_liste_A]

                                DONNEES_GAME["CRYPTOMONNAIE_DETENU"][crypto_ach] += crypto_ach_val_choice

                                crypto_valeur_achat = crypto_ach + "_valeur_achat"
                                DONNEES_GAME["CRYPTOMONNAIE_bénéfice"][crypto_valeur_achat] = valeur_crypto_ach

                                crypto_ach = DONNEES_GAME["CRYPTOMONAIE_selec"][choice_crypto_ach_liste_A]
                                print(MENU_ACHAT_CRYPTO_REUSSI)
                                time.sleep(4)

                            if DONNEES_GAME["CRYPTOMONNAIE_DETENU"][crypto_ach] > 0:
                                print(
                                    "\nVous détenez déja de cette cryptomonnaie !")
                                time.sleep(3)

                            if (crypto_ach_val_choice * valeur_crypto_ach) < capital_user:
                                print(
                                    "\nVous avez les yeux plus gros que le ventre !!! Vous n'avez pas assez d'argent !")
                                time.sleep(3)

                        choice_crypto_liste_A = ""

                    # VENDRE (

                    while choice_crypto_liste_A == "2":
                        None  # faire vendre

                    if choice_crypto_liste_A == "3":
                        choice_crypto_liste = ""

                    if choice_crypto_liste_A == "4":
                        choice_crypto_liste = ""
                        choice_buisness = ""

                    if choice_crypto_liste_A == "5":
                        choice_crypto_liste = ""
                        choice_buisness = ""
                        choice_bureau = ""

                if choice_crypto_liste == "0":
                    choice_buisness = ""

            while choice_buisness == "2":
                None

            if choice_buisness == "3":
                choice_bureau = ""

        while choice_bureau == "2":
            # continuer !!! :)
            None

        while choice_bureau == "3":
            None
            # continuer !!! :)

        if choice_bureau == "5":

            choice = ""

            phrase_exit_bur_1 = "Vous sortez vous décontracter, mais revenez vite vos concurrants vont prendre le dessus sur le marché !"
            phrase_exit_bur_2 = "Vous sortez du bureau ? Allez faire un tour pour embaucher de nouveaux employés ou acheter des choses à la boutique !"
            phrase_exit_bur_3 = "Vous rentrez chez-vous ? Dormez ici il reste un matela à l'acceuil !"
            phrase_exit_bur_4 = "Vous sortez, revenez vite vous manquez déjà au bureau !"
            phrase_exit_bur_5 = "Revenez, cela ne sert à rien de sortir les pizzerias sont toutes fermés aujourd'hui !"
            phrase_exit_bur_secour = "Vous sortez déjà !?!?"
            phrase_exit_bur_choisi = random.randint(1, 6)
            if phrase_exit_bur_choisi == 1:
                phrase_exit_bur_choisi = phrase_exit_bur_1
            elif phrase_exit_bur_choisi == 2:
                phrase_exit_bur_choisi = phrase_exit_bur_2
            elif phrase_exit_bur_choisi == 3:
                phrase_exit_bur_choisi = phrase_exit_bur_3
            elif phrase_exit_bur_choisi == 4:
                phrase_exit_bur_choisi = phrase_exit_bur_4
            elif phrase_exit_bur_choisi == 5:
                phrase_exit_bur_choisi = phrase_exit_bur_5
            elif phrase_exit_bur_choisi != 1 or 2 or 3 or 4 or 5:
                phrase_exit_bur_choisi = phrase_exit_bur_secour

            print(f"\n{phrase_exit_bur_choisi}")
            time.sleep(4)


heure_close = time.time()

time_of_game = heure_close - heure_open

time_of_game /= 60
minute_of_game = round(time_of_game)
DONNEES_GAME["Temps de jeu"]["minutes"] += minute_of_game

time_of_game /= 60
heure_of_game = round(time_of_game, 1)
DONNEES_GAME["Temps de jeu"]["heures"] += heure_of_game

with open(chemin_fich_json, "w") as fich_open:
    json.dump(DONNEES_GAME, fich_open, indent=4, ensure_ascii=False)


# idées de marque américaine à mettre dans bourse
# Technologie Micron
# ServiceNow
# T-Mobile US
# ADP
# Intuit
# Fiserv
# FIS
# Qualcomm
 # Communications de charte
# Texas Instruments
# Broadcom
# IBM
# Pay Pal
 # Netflix
# Nvidia
 # Salesforce
 # Oracle
 # Adobe
 # Comcast
 # Cisco
# Verizon
# AT&T
 # Intel
 # MasterCard
# Visa
# Facebook
# Alphabet
 # Amazone
# Apple
# Microsoft
