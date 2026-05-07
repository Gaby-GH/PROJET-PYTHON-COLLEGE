import os
import sys
import json

fichier_json_chemin = r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\liste_de_course_sauvegarde\liste_course.json"

if os.path.exists(fichier_json_chemin):
    with open(fichier_json_chemin, "r") as fichier_json_open:
        liste_de_course = json.load(fichier_json_open)
else:
    liste_de_course = []

MENU = """\n\nChoisissez parmi les 5 options suivantes :
1) Ajouter un élément à la liste 
2) Retirer un élément à la liste 
3) Afficher la liste 
4) Vider la liste 
5) Quitter et sauvegarder 
------> Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

APP_liste_course = True

while APP_liste_course:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("\nVeuillez choisir une option valide")
    if user_choice == "1":
        ajout_user = input("\nEntrez lélément que vous voulez ajouter : ")
        liste_de_course.append(ajout_user)
        print(f"\n{ajout_user} a été ajouté à la liste !")
    elif user_choice == "2":
        element_rtr = input("\nEntrez l'élément que vous voulez retirer : ")
        if element_rtr in liste_de_course:
            liste_de_course.remove(element_rtr)
            print(f"{element_rtr} a été retirer de la liste !")
        else:
            print(f"""\nl'élément entrez n'est plus dans la liste.
            Mais si vous pensez que {element_rtr} est dans la liste, 
            alors allez vérifier l'orthographe dans l'option afficher la liste""")
    elif user_choice == "3":
        afficher_liste = "\n".join(liste_de_course)
        print(f"\n{afficher_liste}")
    elif user_choice == "4":
        liste_de_course.clear()
        print("\nLa liste a bien été vidée")
    elif user_choice == "5":
        if os.path.exists(fichier_json_chemin):
            with open(fichier_json_chemin, "w") as fichier_json_open:
                json.dump(liste_de_course, fichier_json_open, indent=4)
                print("\nLa liste a bien été sauvegardée !")
                break
        else:
            break
    print(50*"-")
