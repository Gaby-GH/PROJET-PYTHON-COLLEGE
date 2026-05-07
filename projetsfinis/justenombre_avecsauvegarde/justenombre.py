# GROSSE ERREUR A NE PLUS JAMAIS REFAIRE :
# UTILISER LES .WRIT ET .READ ALORS QU ON A IMPORTE JSON
# IL FAUT UTILISER .DUMP ET TOUT LE BASARD
# DU COUP LE SCRIPT DANS LE FICHIER JSON LIS UNE CHAINE DE CARACTER A LA PLACE DE LIRE UNE LISTE VU QU IL EST EN MODE TEXTE ET NON EN MODE JSON


import random
import json
import pathlib
from pathlib import Path

nbr_80 = 80
nombre_80 = 80
partie_01 = 0
chem_sauv_fam = Path(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\justenombre_avecsauvegarde\sauvgare_famille.json")

print("\n\n\nBienvenue au juste nombre. \n Les règles sont simples : trouver le nombre mystère !".upper())
print("Le nombre se situe entre 0 et 1000 !".upper())

user = input("\nPour t'identifier rentre ton numéro correspondant dans user ! : \n\n-Agathe : 1 \n\n-Maman : 2 \n\n-Papa : 3 \n\n-Gabriel : 4 \n\n-Pour faire une partie libre entrez entrez un autre charactère \n\n user : ")
if user.isdigit():
    user = int(user)

    with open(chem_sauv_fam, "r") as fichier_ouvert:
        fichier_lu = fichier_ouvert.read()
        liste_don_user = fichier_lu.split(", ")

        rec_aga = liste_don_user.pop(1)
        rec_aga = int(rec_aga)
        nbr_part_aga = liste_don_user.pop(1)
        nbr_part_aga = int(nbr_part_aga)
        easter_egg_agatr = liste_don_user.pop(1)
        easter_egg_agatr = int(easter_egg_agatr)
        if easter_egg_agatr == 0:
            easter_egg_aga = "Non"
        elif easter_egg_agatr == 1:
            easter_egg_aga = "Oui"

        rec_mam = liste_don_user.pop(1)
        rec_mam = int(rec_mam)
        nbr_part_mam = liste_don_user.pop(1)
        nbr_part_mam = int(nbr_part_mam)
        easter_egg_mamtr = liste_don_user.pop(1)
        easter_egg_mamtr = int(easter_egg_mamtr)
        if easter_egg_mamtr == 0:
            easter_egg_mam = "Non"
        elif easter_egg_mamtr == 1:
            easter_egg_mam = "Oui"

        rec_pap = liste_don_user.pop(1)
        rec_pap = int(rec_pap)
        nbr_part_pap = liste_don_user.pop(1)
        nbr_part_pap = int(nbr_part_pap)
        easter_egg_paptr = liste_don_user.pop(1)
        easter_egg_paptr = int(easter_egg_paptr)
        if easter_egg_paptr == 0:
            easter_egg_pap = "Non"
        elif easter_egg_paptr == 1:
            easter_egg_pap = "Oui"

        rec_gab = liste_don_user.pop(1)
        rec_gab = int(rec_gab)
        nbr_part_gab = liste_don_user.pop(1)
        nbr_part_gab = int(nbr_part_gab)

        nbr_801 = liste_don_user.pop(0)
        nbr_802 = liste_don_user.pop(0)

    if user == 1:
        print("\nBienvenue Agathe !")
        print(
            f"\n-Nombre de partie jouée : {nbr_part_aga} \f-Record : {rec_aga} essais \n-Easter egg d'agathe trouvé : {easter_egg_aga}")

    elif user == 2:

        print("\nBienvenue Maman !")
        print(
            f"\n-Nombre de partie jouée : {nbr_part_mam} \fRecord : {rec_mam} essais \fEaster egg de maman trouvé : {easter_egg_mam}")

    elif user == 3:

        print("\nBienvenue Papa ! (ou devrais-je dire michenté !)")
        print(
            f"\n-Nombre de partie jouée : {nbr_part_pap} \fRecord : {rec_pap} coups \fEaster egg de papa trouvé : {easter_egg_pap}")

    elif user == 4:

        print("\nBienvenue !")
        print(
            f"\n-Nombre de partie jouée : {nbr_part_gab} \fRecord : {rec_gab} coups")

    else:
        partie_01 = 10
        print("\nPartie libre lancée !")
else:
    partie_01 = 10
    print("\nPartie libre lancée !")


jouer = True
while jouer:
    essaie = 1
    nombre_mys = random.randint(1, 1000)
    while True:
        if essaie == 1:
            essaie_01 = input("\nEntrez votre premier nombre ! : ")
            if not essaie_01.isdigit():
                print("\nVous ne pouvez rentrez que des nombres !")
            elif essaie_01.isdigit():
                essaie_01 = int(essaie_01)
                if essaie_01 != nombre_mys:
                    essaie += 1
                    if essaie_01 < nombre_mys:
                        print(
                            f"\nLe nombre mystère est plus grand que {essaie_01} !")
                    if essaie_01 > nombre_mys:
                        print(
                            f"\nLe nombre mystère est plus petit que {essaie_01} !")
                elif essaie_01 == nombre_mys:
                    break
        elif essaie > 1:
            essaie_01 = input("Retenter votre chance ! : ")
            if not essaie_01.isdigit():
                print("\nVous ne pouvez rentrez que des nombres !")
            elif essaie_01.isdigit():
                essaie_01 = int(essaie_01)
                if essaie_01 == nombre_mys:
                    break
                elif essaie_01 != nombre_mys:
                    essaie += 1
                    if essaie_01 < nombre_mys:
                        print(
                            f"\nLe nombre mystère est plus grand que {essaie_01} !")
                        if essaie == 15 and user == 1:
                            print("Même un petit boudin comme toi ferai mieux !")
                            easter_egg_agatr = 1
                        elif essaie == 15 and user == 2:
                            print(
                                "Je savais pas que les gens de l'Assurance Qualité pouvait faire des choses comme ça !")
                            easter_egg_mamtr = 1
                        elif essaie == 15 and user == 3:
                            print(
                                "Non d'un michenté ! Je ne savais pas que c'était possible des faire une telle catastrophe !")
                            easter_egg_paptr = 1
                    elif essaie_01 > nombre_mys:
                        print(
                            f"\nLe nombre mystère est plus petit que {essaie_01} !")
                        if essaie == 15 and user == 1:
                            print("Même un petit boudin comme toi ferai mieux !")
                            easter_egg_agatr = 1
                        elif essaie == 15 and user == 2:
                            print(
                                "Je savais pas que les gens de l'Assurance Qualité pouvait faire des choses comme ça !")
                            easter_egg_mamtr = 1
                        elif essaie == 15 and user == 3:
                            print(
                                "Non d'un michenté ! Je ne savais pas que c'était possible des faire une telle catastrophe !")
                            easter_egg_paptr = 1

    if user == 1:

        nbr_part_aga += 1
        if nbr_part_aga == 1:
            print(f"Petit Boudin a réussi en {essaie} essais !")
            rec_aga = essaie
        else:
            if essaie < rec_aga:
                ancien_aga_rec = rec_aga
                rec_aga = essaie
                print(
                    f"Le petit boudin des flandres a battu son record qui était de {ancien_aga_rec} essais, maintenant il est de {essaie} essais !")
            else:
                print(
                    f"Vous avez réussi en {essaie} essais ! Rejouez pour essayer de battre votre record qui est de {rec_aga} essais !")

    if user == 2:
        nbr_part_mam += 1
        if nbr_part_mam == 1:
            print(f"Mamounnette a réussi en {essaie} essais !")
            rec_mam = essaie
        else:
            if essaie < rec_mam:
                ancien_mam_rec = rec_mam
                rec_mam = essaie
                print(
                    f"Super Mamounette a battu son record qui était de {ancien_mam_rec} essais, maintenant il est de {essaie} essais !")
            else:
                print(
                    f"Vous avez réussi en {essaie} essais ! Rejouez pour essayer de battre votre record qui est de {rec_mam} essais !")

    if user == 3:
        nbr_part_pap += 1
        if nbr_part_pap == 1:
            print(f"\nMichenté a réussi en {essaie} essais !")
            rec_pap = essaie
        else:
            if essaie < rec_pap:
                ancien_pap_rec = rec_pap
                rec_pap = essaie
                print(
                    f"Le michenté Poilu a battu son record qui était de {ancien_pap_rec} essais, maintenant il est de {essaie} essais !")
            else:
                print(
                    f"Vous avez réussi en {essaie} essais ! Rejouez pour essayer de battre votre record qui est de {rec_pap} essais !")

    if user == 4:
        nbr_part_gab += 1
        if nbr_part_gab == 1:
            print(f"\nJean-michel a réussi en {essaie} essais !")
            rec_gab = essaie
        else:
            if essaie < rec_gab:
                ancien_gab_rec = rec_gab
                rec_gab = essaie
                print(
                    f"\nLe michenté Super Poilu a battu son record qui était de {ancien_gab_rec} essais, maintenant il est de {essaie} essais !")
            else:
                print(
                    f"\nVous avez réussi en {essaie} essais ! Rejouez pour essayer de battre votre record qui est de {rec_gab} essais !")

    if partie_01 == 10 and essaie == 1:
        print("\nVous avez réussi du premier coup !!! \nVous avez réussi la chose la plus dur de ce jeu bien joué ! \n Vous avez eu exactement 1 chance sur 1000 de réussir du premier coup !")
    elif partie_01 == 10 and essaie > 1:
        print(
            f"\nVous avez réussi en {essaie} essais ! \nRecommencez pour essayer de le réussir en moins d'essai, voir du premier coup !")

    rejouer = input("""\n\n-Pour rejouer entrez 1

-Pour regarder le classement entrez 2
    
-Pour quitter et sauvegarder entrez autre chose  : """)

    if rejouer == "1":
        essaie = 1
        continue
    elif rejouer == "2" and partie_01 != 10:

        rec_aga2 = rec_aga
        rec_gab2 = rec_gab
        rec_mam2 = rec_mam
        rec_pap2 = rec_pap

        nbr_part_aga2 = nbr_part_aga
        nbr_part_gab2 = nbr_part_gab
        nbr_part_mam2 = nbr_part_mam
        nbr_part_pap2 = nbr_part_pap

        liste_coup = [[rec_aga2, ["Agathe"]], [rec_gab2, ["Gabriel"]], [
            rec_mam2, ["Maman"]], [rec_pap2, ["Papa"]]]
        liste_partie = [[nbr_part_aga2, ["Agathe"]], [nbr_part_gab2, ["Gabriel"]], [
            nbr_part_mam2, ["Maman"]], [nbr_part_pap2, ["Papa"]]]

        liste_coup.sort()
        liste_partie.sort()

        premier_c = liste_coup[0][1][0]
        premier_en_coup = liste_coup[0][0]

        deuxième_c = liste_coup[1][1][0]
        deuxième_en_coup = liste_coup[1][0]

        troisième_c = liste_coup[2][1][0]
        troisième_en_coup = liste_coup[2][0]

        dernier_c = liste_coup[3][1][0]
        dernier_en_coup = liste_coup[3][0]

        premier_p = liste_partie[3][1][0]
        premier_en_partie = liste_partie[3][0]

        deuxième_p = liste_partie[2][1][0]
        deuxième_en_partie = liste_partie[2][0]

        troisième_p = liste_partie[1][1][0]
        troisième_en_partie = liste_partie[1][0]

        dernier_p = liste_partie[0][1][0]
        dernier_en_partie = liste_partie[0][0]

        print(f"""\n\n\nCLASSEMENT DU MOINS DE COUPS POSSIBLE                   CLASSEMENT DU PLUS DE PARTIES
                  
     #1 {premier_c}  COUPS : {premier_en_coup}                                  #1 {premier_p}  PARTIES : {premier_en_partie}

     #2 {deuxième_c}  COUPS : {deuxième_en_coup}                                #2 {deuxième_p}  PARTIES : {deuxième_en_partie}

     #3 {troisième_c}  COUPS : {troisième_en_coup}                              #3 {troisième_p}  PARTIES : {troisième_en_partie}

     #4 {dernier_c}  COUPS : {dernier_en_coup}                                  #4 {dernier_p}  PARTIES : {dernier_en_partie}""")

        rejouer = input("""\n\n-Pour rejouer entrez 1
\n-Pour quitter et sauvegarder entrez autre chose : """)
        if rejouer == "1":
            continue
        else:
            jouer = False

    else:
        jouer = False

with open(chem_sauv_fam, "w") as fichier_ouvert:

    liste_don_user.append(nbr_80)
    liste_don_user.append(rec_aga)
    liste_don_user.append(nbr_part_aga)
    liste_don_user.append(easter_egg_agatr)
    liste_don_user.append(rec_mam)
    liste_don_user.append(nbr_part_mam)
    liste_don_user.append(easter_egg_mamtr)
    liste_don_user.append(rec_pap)
    liste_don_user.append(nbr_part_pap)
    liste_don_user.append(easter_egg_paptr)
    liste_don_user.append(rec_gab)
    liste_don_user.append(nbr_part_gab)
    liste_don_user.append(nombre_80)

    json.dump(liste_don_user, fichier_ouvert)
