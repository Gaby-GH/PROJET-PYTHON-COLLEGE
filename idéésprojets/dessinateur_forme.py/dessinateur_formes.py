import Forme

x_1 = "yo"
y_1 = "yo"
indent_1 = "yo"

running = True

while running:
    sortie = input(
        "Voulez vous quitter ? Entrez 1 si vous le souhaitez sinon entrez autre chose : ")
    sortie = sortie.strip(" ")
    if sortie == "1":
        running = False

    while not str(x_1).isdigit():
        x_1 = input("Largeur : ")
        x_1 = x_1.strip(" ")

        if x_1.isdigit() and x_1 != "0":
            if int(x_1) > 0:
                x_1 = int(x_1)

        else:
            print("Rentrez un nombre au dessus de 0")

    while not str(y_1).isdigit():
        y_1 = input("Hauteur : ")
        y_1 = y_1.strip(" ")

        if y_1.isdigit() and y_1 != "0":
            if int(y_1) > 0:
                y_1 = int(y_1)

        else:
            print("Rentrez un nombre au dessus de 0")

    while not str(indent_1).isdigit():
        indent_1 = input("L'espace entre le bord et le rectangle : ")
        indent_1 = indent_1.strip(" ")

        if indent_1.isdigit():
            if int(indent_1) > -1:
                indent_1 = int(indent_1)

        else:
            print("Rentrez un nombre au dessus de -1")

    carre = Forme.rectangle(int(x_1), int(y_1), int(indent_1))
    print(carre)

    x_1 = "yo"
    y_1 = "yo"
    indent_1 = "yo"
