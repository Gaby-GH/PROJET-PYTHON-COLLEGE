import pygame
from pathlib import Path
import time

file_path = Path(__file__)
dossier_parent = file_path.parent

pygame.init()
screen = pygame.display.set_mode((1000, 800))

ch_a = dossier_parent / "a.png"
a = pygame.image.load(ch_a)

ch_à = dossier_parent / "à.png"
à = pygame.image.load(ch_à)

ch_b = dossier_parent / "b.png"
b = pygame.image.load(ch_b)

ch_c = dossier_parent / "c.png"
c = pygame.image.load(ch_c)

ch_ç = dossier_parent / "ç.png"
ç = pygame.image.load(ch_ç)

ch_d = dossier_parent / "d.png"
d = pygame.image.load(ch_d)

ch_e = dossier_parent / "e.png"
e = pygame.image.load(ch_e)

ch_é = dossier_parent / "é.png"
é = pygame.image.load(ch_é)

ch_è = dossier_parent / "è.png"
è = pygame.image.load(ch_è)

ch_ë = dossier_parent / "ë.png"
ë = pygame.image.load(ch_ë)

ch_f = dossier_parent / "f.png"
f = pygame.image.load(ch_f)

ch_g = dossier_parent / "g.png"
g = pygame.image.load(ch_g)

ch_h = dossier_parent / "h.png"
h = pygame.image.load(ch_h)

ch_i = dossier_parent / "i.png"
i = pygame.image.load(ch_i)

ch_j = dossier_parent / "j.png"
j = pygame.image.load(ch_j)

ch_k = dossier_parent / "k.png"
k = pygame.image.load(ch_k)

ch_l = dossier_parent / "l.png"
l = pygame.image.load(ch_l)

ch_m = dossier_parent / "m.png"
m = pygame.image.load(ch_m)

ch_n = dossier_parent / "n.png"
n = pygame.image.load(ch_n)

ch_o = dossier_parent / "o.png"
o = pygame.image.load(ch_o)

ch_p = dossier_parent / "p.png"
p = pygame.image.load(ch_p)

ch_q = dossier_parent / "q.png"
q = pygame.image.load(ch_q)

ch_r = dossier_parent / "r.png"
r = pygame.image.load(ch_r)

ch_s = dossier_parent / "s.png"
s = pygame.image.load(ch_s)

ch_t = dossier_parent / "t.png"
t = pygame.image.load(ch_t)

ch_u = dossier_parent / "u.png"
u = pygame.image.load(ch_u)

ch_v = dossier_parent / "v.png"
v = pygame.image.load(ch_v)

ch_w = dossier_parent / "w.png"
w = pygame.image.load(ch_w)

ch_x = dossier_parent / "x.png"
x = pygame.image.load(ch_x)

ch_y = dossier_parent / "y.png"
y = pygame.image.load(ch_y)

ch_z = dossier_parent / "z.png"
z = pygame.image.load(ch_z)

ch_tiret = dossier_parent / "tiret.png"
tiret = pygame.image.load(ch_tiret)

fond = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\idéésprojets\pygamland_2\New Piskel-1.png (21).png")

# BULLE DE TAILLE DIFFERENTE
ch_bulle_1 = dossier_parent / "bulle_1.png"
bulle_1 = pygame.image.load(ch_bulle_1)
x_bulle_1 = 600
y_bulle_1 = 400

ch_bulle_2 = dossier_parent / "bulle_2.png"
bulle_2 = pygame.image.load(ch_bulle_2)
x_bulle_2 = 600
y_bulle_2 = 350

# LISTE AVEC LES CARCTERE QUI NE S'AFFICHA PAS NORMALEMENT
liste_caractere_bizarre = [" ", "m", "i", "n", "j", "\n", "w", "f", "l", "o"]

# GERER LES RETOUR A LA LIGNE
# VARIABLE POUR COMPTER LA LARGEUR DE LA BULLE
largeur_limite_bulle = x_bulle_1 + 175

# VARIABLE POUR AFFICHER QU UNE SEULE FOIS LE MESSAGE
write_phrase = True

# VARIABLE DE L ACTIVATION DE LA FENETRE
running = True


phrase = """abdoul"""

# DECHARGE


# DECHARGE

# BOUCLE DE LA FENETRE
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # AFFICHAGE FOND
    screen.blit(fond, (0, 0))

    # DEFINIR LA TAILLE DE LA BULLE EN FONCTION DU NOMBRE DE CARACTERE DANS LA PHRASE
    if len(phrase) < 55:
        screen.blit(bulle_1, (x_bulle_1, y_bulle_1))

        x_caractere = x_bulle_1 + 25
        y_caractere = y_bulle_1 + 10
    else:
        screen.blit(bulle_2, (x_bulle_2, y_bulle_2))

        x_caractere = x_bulle_2 + 25
        y_caractere = y_bulle_2 + 10

    # GERER l'AFFICHAGE GRAPHIQUE DE LA CHAINE DE CARACTERE EN BOUCLANT DESSUS

    for caractere in phrase.lower():

        if x_caractere > largeur_limite_bulle:
            screen.blit(tiret, (x_caractere, y_caractere))
            x_caractere = x_bulle_1 + 25
            y_caractere += 30

        if caractere not in liste_caractere_bizarre:
            lettre = pygame.image.load(dossier_parent / f"{caractere}.png")
            screen.blit(lettre, (x_caractere, y_caractere))

        # BIEN AFFICHER LES CARACTERE BIZARRE
        else:
            if caractere == " ":
                lettre = pygame.image.load(dossier_parent / f"space.png")
                screen.blit(lettre, (x_caractere, y_caractere))

            elif caractere == "m":
                lettre = pygame.image.load(
                    dossier_parent / f"{caractere}.png")
                screen.blit(lettre, (x_caractere, y_caractere))
                x_caractere += 3

            elif caractere == "n":
                lettre = pygame.image.load(
                    dossier_parent / f"{caractere}.png")
                screen.blit(lettre, (x_caractere, y_caractere + 1))

            elif caractere == "i":
                lettre = pygame.image.load(
                    dossier_parent / f"{caractere}.png")
                screen.blit(lettre, (x_caractere, y_caractere))
                x_caractere -= 6

            elif caractere == "j":
                lettre = pygame.image.load(
                    dossier_parent / f"{caractere}.png")
                screen.blit(lettre, (x_caractere - 1, y_caractere))
                x_caractere -= 2

            elif caractere == "\n":

                x_caractere -= 50
                y_caractere += 22

            elif caractere == "w":
                lettre = pygame.image.load(
                    dossier_parent / f"{caractere}.png")
                screen.blit(lettre, (x_caractere, y_caractere))
                x_caractere += 3

            elif caractere == "f":
                lettre = pygame.image.load(
                    dossier_parent / f"{caractere}.png")
                screen.blit(lettre, (x_caractere, y_caractere))
                x_caractere -= 5

            elif caractere == "l":
                lettre = pygame.image.load(
                    dossier_parent / f"{caractere}.png")
                screen.blit(lettre, (x_caractere, y_caractere))
                x_caractere -= 6

            elif caractere == "o":
                lettre = pygame.image.load(
                    dossier_parent / f"{caractere}.png")
                screen.blit(lettre, (x_caractere, y_caractere))
                x_caractere -= 2

        # FAIRE L'EFFET D'AFFICHAGE QU UNE SEULE FOIS
        if write_phrase == True:
            time.sleep(0.15)
            pygame.display.flip()

        x_caractere += 14

    # DESACTIVER L'EFFET D'AFFICHAGE UNE FOIS LA PHRASE TERMINEE
    write_phrase = False

    pygame.display.flip()
