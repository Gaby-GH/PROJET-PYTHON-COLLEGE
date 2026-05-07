import matplotlib.pyplot as plt
from pathlib import Path
import json
import time
import random
import os
print("tu peux parler avec moi")
prénom = input("entre ton prénom : ")
age = input("Puis ton age : ")
age = int(age)
if age > 60:
    print("vous ne pouvez pas être un dinosaure")
année_naissance = 2022 - int(age)
phrase = f"salut {prénom} je sais que tu es nés en {année_naissance} !"
if age < 60:
    print(phrase)

print("projet calculatrice d'addition")
print("les 2 nombre que vous allez écrire s'additionneront")
nombre_1 = input("entez un nombre : ")
nombre_2 = input("puis un deuxième : ")
résultat = int(nombre_1) + int(nombre_2)
résultat_1 = f"donc l'addition de {nombre_1} par {nombre_2} est égale à {résultat}"
print(résultat_1)

aage = input("entrez votre âge : ")
aage = int(aage)
if aage >= 18:
    print("vous êtes majeur")
if aage < 18:
    print("vous êtes mineur")

code = input("entrer le code secret : ")
code = int(code)
if code == 27:
    print("vous êtes trop fort !")
else:
    print("ce n'est pas le code secret")

année = input("entrer votre année de naissance : ")
année = int(année)
mot_de_passe = input("entrer ensuite votre mot de passe : ")
mot_de_passe = int(mot_de_passe)
nom_utilisateur = input("puis votre nom d'utilisateur : ")
if année < 2004 and mot_de_passe == 27 and nom_utilisateur == "gab":
    print("bien joué michente")
else:
    print("Accès refuser")

    import random
nombre_aléatoire = random.randint(0, 30)
print(nombre_aléatoire)
if nombre_aléatoire == 27:
    print("vous avez debloquer le brawler gabriel !!!")

chemin = "/Users/boris/OneDrive/Bureau/pytonJEU"
dossier_chocolat = os.path.join(chemin, "dossier chocolat")
print(dossier_chocolat)
os.makedirs(dossier_chocolat)

# j'ai enfin réussi à trouver comment on met des notes !!!
numéro_dès = random.randint(1, 6)
print(numéro_dès)

print("cookies")
print("\u2764")
print(r"gaby\b pipinou")
print("croquette\vsaumonophobe")
a = 5
b = 10
"bonjour bienvenue chez oim"
bonjour = "bonjour bienvenue chez oim"
nombre = input("entrez un nombre: ")
a = " c'est le nombre poils de fesses que tu as !"
print(nombre + a)
nombre_1 = input("rechoisi un nombre michenté : ".capitalize())
b = " c'est ton niveau de beauté en pourcentage !"
print(nombre_1 + b)
mot = input("entrez un mot: ")
mot = str(mot)
nombre_2 = input("entrez le nombre de fois que vous voulez écrire ce mot:")
nombre_2 = int(nombre_2)
print(nombre_2 * mot)
k = f"bonjour {mot}"
print(k)


nombre_croq = random.randint(1, 1000)
liste_27 = [f"pilou mange {nombre_croq} croquettes par jour ! ",
            "carlos", "bernard", "bubulle", "baltazard", "lulu"]
print(liste_27[0:1])

# listes
chat = ["pilou", "vomi", "car", "il mange trop de croquettes"]
chat_2 = "  ".join(chat)
print(chat_2)

liste_258 = ["pilou", "mama", "jacob", "gab", "bernard"]
liste_finie = "\n".join(liste_258)
print(liste_finie)

# liste ibriquées
chat_278 = ["pilou", ["carlos", "bernard", [
    "choupi", "pipinou"]], ["jean pierre"]]
print(chat_278[1][2][1])

# exercice mot de passe
mot_de_passe = input("Entrez un mot de passe (minimum 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court"
mdp_bien = "Votre mot de passe a été enregistré !"
if len(mot_de_passe) == 0:
    print(mdp_trop_court.upper())
elif len(mot_de_passe) < 8:
    print(mdp_trop_court.capitalize())
elif len(mot_de_passe) < 8 and mot_de_passe.isdigit:
    print("Votre mot de passe est trop court mais ne contient que des nombres, rajoutez d'autres caractères")
elif mot_de_passe.isdigit():
    print("Votre mot de passe ne contient que des nombres")
elif mot_de_passe.isupper():
    print("Rajoutez des minuscules !")
else:
    print(mdp_bien)

# essaie boucles
liste = [0, 45, "proute"]
for element in liste:
    print(element)


liste = ["roro", "dodo", "mongo", "bobo"]
for i in liste:
    if i == "mongo":
        print("mongo")


nombreu = input("rentrez le nombre de fois que vous voulez écrire chat : ")
nombreu = int(nombreu)
for right_nombredefois in range(nombreu):
    print("chat")


i = 0
while i < 50:
    print("bonjour")
    i += 1


#sec = 0
# while True:
#    print(sec)
#    sec += 1
#   time.sleep(1)


# essaies compréhensions de listes

liste = [-4, -5, -9, 1, 2, 3, 4, 5]
nombre_po = [i for i in liste if i > 0]
print(nombre_po)
liste_2 = [-2, -5, -8, -1, 89, 56]
nombre_po = nombre_po + [el for el in liste_2 if el > 0]
print(nombre_po)


# exos fin de la vidéo de 7h !!!!

print("les deux nombres que vous aller entrez vont s'additionner ")
yes = True
while yes:
    nombre_1 = input("entrez un nombre : ")
    nombre_2 = input("puis le deuxième : ")
    if nombre_1.isdigit() and nombre_2.isdigit():
        nombre_1 = int(nombre_1)
        nombre_2 = int(nombre_2)
        print(
            f"L'opération de {nombre_1} + {nombre_2} est égale à {nombre_1 + nombre_2}")
        yes = False
    else:
        print("Vous ne pouvez additionner que des nombres")
        continue


# exercice liste de course

liste_encours = True
liste_de_course = []

while liste_encours:
    print("\n-----------------------------------------------------------------")
    action = input("\n\nChoisissez parmi les 5 options suivantes :\n1) Ajouter un élément à la liste \n2) Retirer un élément à la liste \n3) Afficher la liste \n4) Vider la liste \n5) Quitter \n ------> Votre choix : ")
    if action.isdigit() and action == 1 or 2 or 3 or 4 or 5:
        action = int(action)
        if action == 1:
            element_ajt = input(
                "\nEntrez l'élément que vous voulez ajouter : ")
            liste_de_course.append(element_ajt)
            print(f"\n{element_ajt} a été ajouté à la liste")
        elif action == 2:
            element_rtr = input("\nEntrez lélément que vous voulez retirer : ")
            if element_rtr in liste_de_course:
                liste_de_course.remove(element_rtr)
                print(f"\n{element_rtr} a bien été retiré à la liste")
            else:
                print(
                    f"\n{element_rtr} n'est pas dans la liste \nSi vous pensez qu'il est dans la liste revérifier l'orthographe")
        elif action == 3:
            liste_afchr = "\n".join(liste_de_course)
            print(liste_afchr)
        elif action == 4:
            liste_de_course.clear()
            print("Tout les éléments de la liste de course ont été supprimé")
        elif action == 5:
            liste_encours = False
    else:
        print("Vous ne pouvez rentrez que les nombres des choix affichés")
        continue

# Lire et écrire dans des fichiers

# txt

chemin = r"C:\Users\boris\pytonJEU\dossier chocolat\essaielecfich.txt"
f = open(chemin, "a")
f.write("\nMais 5 n'a jamais été atteint !!! ")
d = open(chemin, "r")
contenu = d.read()
print(contenu)
f.close()

# json

chemin = r"C:\Users\boris\pytonJEU\fichierspycréés\idéésprojets\doosier.json"
f = open(chemin, "a")
liste_3 = [1, 1, 2, 2, 3, 8]
json.dump(liste_3, f, indent=4)
f.close()

# essai

hh = Path.home()
hh = (hh / "PythonJEU" / "dossier chocolat" / "ESSAIEPYGAME_1.py").suffix
print(hh)

# graphique (a faire marcher)

plt.title("évolution du michenté en fonction des années")
plt.plot([2000, 2005, 2010, 2015, 2020, 2023], [
         1, 5, 65, 88, 120, 265], "g--", linwedth=2)
plt.xlabel("Année")
plt.ylabel("Nombre en Michenté")
plt.axis([2000, 2023, 0, 300])
plt.show()
