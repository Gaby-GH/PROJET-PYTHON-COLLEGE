import pygame
from pathlib import Path
import json
import random
import os
import time


# SI C PAS FAIT REGARDER LA TROISEME VIDEO SUR PYGAME ET LES COLISIONS §§§§§§§§§§§§§§§§§§§§§§§§§§§§§

pygame.init()
screen = pygame.display.set_mode((1280, 896))
pygame.display.set_caption("pocket clop")
icone_pocket_clop = pygame.image.load(r"icon_grand.png").convert_alpha()
pygame.display.set_icon(icone_pocket_clop)

# creation du fichier json database si non existant
chemin_database = Path(r"pocket_clop.json")

if not chemin_database.exists():
    DATABASE_init = {"cloporte_P full": False,
                     "cloporte_P type charge": None,
                     "num_obj": 0,
                     "num_lot_obj": 0,
                     "cost": {"reserve feuille": {"niv 1": [15, 20],
                                                  "niv 2": [20, 30],
                                                  "niv 3": [1, 1],
                                                  "niv 4": [1, 1],
                                                  "niv 5": [1, 1],
                                                  "niv 6": [1, 1],
                                                  "niv 7": [1, 1],
                                                  "niv 8": [1, 1],
                                                  "niv 9": [1, 1],
                                                  "niv 10": [1, 1]},
                              "reserve champignon": {"niv 1": [25, 10],
                                                     "niv 2": [1, 1],
                                                     "niv 3": [1, 1],
                                                     "niv 4": [1, 1],
                                                     "niv 5": [1, 1],
                                                     "niv 6": [1, 1],
                                                     "niv 7": [1, 1],
                                                     "niv 8": [1, 1],
                                                     "niv 9": [1, 1],
                                                     "niv 10": [1, 1]}},

                     "niveaux": {"stockage feuille map_1": 1,
                                 "stockage champignon map_1": 1},
                     "stockage max": {"reserve feuille": {"niv 1": 25,
                                                          "niv 2": 35,
                                                          "niv 3": 50,
                                                          "niv 4": 80,
                                                          "niv 5": 120,
                                                          "niv 6": 200,
                                                          "niv 7": 300,
                                                          "niv 8": 500,
                                                          "niv 9": 1000,
                                                          "niv 10": 1500},
                                      "reserve champignon": {"niv 1": 25,
                                                             "niv 2": 999,
                                                             "niv 3": 999,
                                                             "niv 4": 999,
                                                             "niv 5": 999,
                                                             "niv 6": 999,
                                                             "niv 7": 999,
                                                             "niv 8": 999,
                                                             "niv 9": 999,
                                                             "niv 10": 0}},
                     "stockage general": {"feuille": 80000,
                                          "champignon": 8000,
                                          "bois": 0},
                     "stockage map_1":   {"feuille": 8000,
                                          "champignon": 8000,
                                          "bois": 0},
                     "stockage map_2":   {"feuille": 0,
                                          "champignon": 0,
                                          "bois": 0},
                     "stockage map_3":   {"feuille": 0,
                                          "champignon": 0,
                                          "bois": 0},
                     "stockage map_4":   {"feuille": 0,
                                          "champignon": 0,
                                          "bois": 0},
                     "obj_cree": {}}

    with open(chemin_database, "w") as database_open:
        json.dump(DATABASE_init, database_open, indent=4, ensure_ascii=False)


# load des images : persos, background...

# sauvegarde
with open(chemin_database, "r") as database_open:
    DATABASE = json.load(database_open)

# map
map_1 = pygame.image.load(r"map_1.png").convert_alpha()
map_2 = pygame.image.load(r"map_2.png").convert_alpha()
map_parametre = pygame.image.load(r"fond_parametre.png").convert_alpha()
map_amelioration = pygame.image.load(r"fond_map_amelioration.png")
map_P = map_1

map_precedente = map_1

# img perso
# cloporte principal
cloporte_P = pygame.image.load(r"essai_cloporte.png").convert_alpha()
cloporte_P_up = pygame.image.load(r"essai_cloporte.png").convert_alpha()
cloporte_P_down = pygame.image.load(r"cloporte_descend.png").convert_alpha()
cloporte_P_right = pygame.image.load(r"cloporte_right.png").convert_alpha()
cloporte_P_left = pygame.image.load(r"cloporte_left.png").convert_alpha()
x_cloporte_P = 1100
y_cloporte_P = 150


# position obj pour colision

# SOURIS
mouse_x, mouse_y = pygame.mouse.get_pos()
rect_souris = pygame.Rect(mouse_x, mouse_y, 15, 20)

# map_1
# rect de la zone de sortie de la map_1
rect_exit_camp_P = pygame.Rect(496, 0, 288, 50)

# Contact avec les murs
# Colision grace aux sorties de zone à respecter du cloporte
rect_zone_deplacement_1 = pygame.Rect(516, 0, 248, 780)
rect_zone_deplacement_2 = pygame.Rect(100, 100, 216, 216)
rect_zone_deplacement_3 = pygame.Rect(964, 100, 216, 136)
rect_zone_deplacement_4 = pygame.Rect(788, 180, 152, 56)
rect_zone_deplacement_5 = pygame.Rect(340, 180, 152, 56)
rect_zone_deplacement_6 = pygame.Rect(340, 596, 152, 56)
rect_zone_deplacement_7 = pygame.Rect(100, 500, 216, 248)

# Zone pour lacher morceau de buisson
rect_zone_stockage_feuille = pygame.Rect(100, 100, 216, 216)
# Zone pour lacher morceau de champignon
rect_zone_stockage_champi = pygame.Rect(100, 500, 216, 248)


# map_2
# camp principal
rect_camp_P = pygame.Rect(232, 525, 80, 80)
# camp 1 (camp de culture)
rect_camp_clop_1 = pygame.Rect(185, 285, 128, 144)
# camp 2 (camp d'entrainement)
rect_camp_clop_2 = pygame.Rect(583, 510, 118, 88)
# camp des fourmis
rect_camp_fourmi = pygame.Rect(760, 704, 64, 128)
# Fleuve
rect_fleuve_1 = pygame.Rect(512, 0, 200, 120)
rect_fleuve_2 = pygame.Rect(599, 116, 200, 176)
rect_fleuve_3 = pygame.Rect(760, 285, 200, 415)
rect_fleuve_4 = pygame.Rect(764, 600, 550, 100)
# entrée dans map_3 bloqué
rect_entree_map_3 = pygame.Rect(0, 60, 130, 85)


# zone de forêt (où peuvent etre générer les arbres buissons etc...)
rect_foret_1 = pygame.Rect(325, 150, 200, 350)
rect_foret_2 = pygame.Rect(150, 25, 300, 225)
rect_foret_3 = pygame.Rect(30, 175, 150, 620)
rect_foret_4 = pygame.Rect(125, 620, 600, 175)
# obj de le map (arbre, buisson etc...)
arbre = pygame.image.load(r"arbre.png").convert_alpha()
buisson = pygame.image.load(r"buisson.png").convert_alpha()
bout_de_buisson = pygame.image.load(r"bout_de_buisson.png").convert_alpha()
bout_de_champignon = pygame.image.load(
    r"bout_de_champignon.png").convert_alpha()
logo_buisson_level_up = pygame.image.load(r"logo_buisson_level_up.png")
logo_champignon_level_up = pygame.image.load(r"logo_champignon_level_up.png")
pos_feuille_x = 0
pos_feuille_y = 0
tronc = pygame.image.load(r"tronc.png").convert_alpha()
bout_de_tronc = pygame.image.load(r"bout_de_tronc.png").convert_alpha()
bout_de_nourriture = bout_de_buisson

str_champignon = "champignon"
str_buisson = "buisson"
tempo_obj = 0
obj = buisson
rect_obj = pygame.Rect(0, 0, 0, 0)
x = 0
y = 0
pv_obj = 0
bout_de_nourriture_lacher = 0
type_bout_de_nourriture = 0
bout_de_nourriture_lacher = 0
pos_x_bout_de_nourriture = 0
pos_y_bout_de_nourriture = 0
rect_bout_de_nourriture = 0
map_du_bout_de_nourriture = 0


# AUTRE SORTE D'IMAGE
# barre de point de vie (obj)
full_life_barre = pygame.image.load(r"full_life.png").convert_alpha()
trois_quart_life_barre = pygame.image.load(
    r"trois_quart_life.png").convert_alpha()
demi_life_barre = pygame.image.load(r"demi_life.png").convert_alpha()
un_quart_life_barre = pygame.image.load(r"un_quart_life.png").convert_alpha()
no_life_barre = pygame.image.load(r"no_life.png").convert_alpha()

# MESSAGES ET AVERTISSEMENTS
message_1 = pygame.image.load(r"message_1.png").convert_alpha()
message_2 = pygame.image.load(r"message_2.png").convert_alpha()
rect_message_2 = pygame.Rect(230, 400, 30, 30)
message_3 = pygame.image.load(r"message_3.png").convert_alpha()
rect_message_3 = pygame.Rect(625, 583, 30, 30)
message_4 = pygame.image.load(r"message_4.png").convert_alpha()
rect_message_4 = pygame.Rect(758, 744, 30, 30)
message_5 = pygame.image.load(r"message_5.png").convert_alpha()
rect_message_5 = pygame.Rect(552, 100, 30, 30)
message_6 = pygame.image.load(r"message_6.png").convert_alpha()
rect_message_6 = pygame.Rect(105, 87, 30, 30)

# LOGOS
logo_buisson = pygame.image.load(r"logo_buisson.png").convert_alpha()
logo_champignon = pygame.image.load(r"logo_champignon.png").convert_alpha()
logo_parametres = pygame.image.load(r"logo_parametre.png").convert_alpha()
logo_exit_parametre = pygame.image.load(
    r"logo_exit_parametre.png").convert_alpha()
logo_ameliorations = pygame.image.load(
    r"logo_amelioration.png").convert_alpha()


# RECT map_parametre
rect_logo_amelioration = logo_ameliorations.get_rect(x=175, y=150)

# IMAGE ET AUTRES DANS MAP AMELIORATION
logo_titre_base_principale = pygame.image.load(
    r"logo_titre_base_principale.png")
logo_titre_base_ouvriere = pygame.image.load(r"logo_titre_base_ouvrieres.png")
logo_titre_base_militaire = pygame.image.load(r"logo_titre_base_militaire.png")
logo_titre_base_construction = pygame.image.load(
    r"logo_titre_base_construction.png")

logo_titre_reserve_feuille = pygame.image.load(
    r"logo_titre_reserve_feuille.png")
logo_titre_reserve_champignon = pygame.image.load(
    r"logo_titre_reserve_champignon.png")

logo_level_up_1 = pygame.image.load(r"logo_level_up.png")

# RECT map_amelioration
rect_exit_map_amelioration = pygame.Rect(970, 730, 253, 70)
rect_logo_level_up_1 = logo_level_up_1.get_rect(x=20, y=350)

# barre de progression niv
barre_progression_niv = pygame.image.load(r"barre_progression_niv_1.png")

souris_pressed = False


# barre de recource (A FINIR, EN COURS DE PROGRAMMATION)
fond_barre_de_recource = pygame.image.load(
    r"fond_barre_de_recource.png").convert_alpha()

# reglage de la vitesse de jeu
clock = pygame.time.Clock()

play = True

yoyoyoyoyooo = 0

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        # savoir si souris est cliquée
        if event.type == pygame.MOUSEBUTTONDOWN:
            souris_pressed = True
        else:
            souris_pressed = False

    # Mouvement du cloporte principale
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
        x_cloporte_P += 3
        cloporte_P = cloporte_P_right

    if pressed[pygame.K_LEFT] or pressed[pygame.K_q]:
        x_cloporte_P -= 3
        cloporte_P = cloporte_P_left

    if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
        y_cloporte_P += 3
        cloporte_P = cloporte_P_down

    if pressed[pygame.K_UP] or pressed[pygame.K_z]:
        y_cloporte_P -= 3
        cloporte_P = cloporte_P_up

    # CONTACT OBJ ET CHANGEMENT DE MAP, COLISIONS ET BORDURES DE LA MAP
    # bordure map 1, 2 etc...
    if y_cloporte_P > 805:
        y_cloporte_P -= 3

    if y_cloporte_P < 10:
        y_cloporte_P += 3

    if x_cloporte_P > 1272:
        x_cloporte_P -= 3

    if x_cloporte_P < 10:
        x_cloporte_P += 3

    # COLISION DANS MAP 1
    if map_P == map_1:

        # Colison avec les murs
        # Colision avec les murs (si cloporte sort de la zone)
        if not rect_zone_deplacement_1.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)) and not rect_zone_deplacement_2.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)) and not rect_zone_deplacement_3.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)) and not rect_zone_deplacement_4.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)) and not rect_zone_deplacement_5.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)) and not rect_zone_deplacement_6.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)) and not rect_zone_deplacement_7.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
            if cloporte_P == cloporte_P_down:
                y_cloporte_P -= 3
            if cloporte_P == cloporte_P_up:
                y_cloporte_P += 3
            if cloporte_P == cloporte_P_left:
                x_cloporte_P += 3
            if cloporte_P == cloporte_P_right:
                x_cloporte_P -= 3

            # Réparation bug (sortie de map)
            if x_cloporte_P < 0 or x_cloporte_P > 1280 or y_cloporte_P < 0 or y_cloporte_P > 848:
                x_cloporte_P = 1100
                y_cloporte_P = 150

    # Sortie base principal (camp_P), de map_1 à map_2
        if rect_exit_camp_P.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
            map_P = map_2
            x_cloporte_P = 250
            y_cloporte_P = 450

    # COLISIONS DANS MAP_2
    if map_P == map_2:

        # colision avec la base des ouvriers cloportes (camp_2)
        if rect_camp_clop_1.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
            if x_cloporte_P < 185:
                x_cloporte_P -= 3
            if x_cloporte_P > 300:
                x_cloporte_P += 3
            if y_cloporte_P < 285:
                y_cloporte_P -= 3
            if y_cloporte_P > 420:
                y_cloporte_P += 3

        # colision avec la base d'entrainement cloportes (camp_3)
        if rect_camp_clop_2.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
            if x_cloporte_P < 583:
                x_cloporte_P -= 3
            if x_cloporte_P > 695:
                x_cloporte_P += 3
            if y_cloporte_P < 505:
                y_cloporte_P -= 3
            if y_cloporte_P > 590:
                y_cloporte_P += 3

        # colision avec l'entrée dans le monde des fourmis
        if rect_camp_fourmi.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
            x_cloporte_P -= 3

        # colision avec le fleuve
        # fleuve_1
        if rect_fleuve_1.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
            if cloporte_P == cloporte_P_down or cloporte_P == cloporte_P_right:
                x_cloporte_P -= 3
            elif cloporte_P == cloporte_P_up or cloporte_P_left:
                y_cloporte_P += 3

        # fleuve_2
        if rect_fleuve_2.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
            if cloporte_P == cloporte_P_down or cloporte_P == cloporte_P_right:
                x_cloporte_P -= 3
            elif cloporte_P == cloporte_P_up or cloporte_P_left:
                y_cloporte_P += 3

        # fleuve_3
        if rect_fleuve_3.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
            x_cloporte_P -= 3

        # fleuve_4
        if rect_fleuve_4.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
            y_cloporte_P += 3

        # colision avec l'entrée de la map 3
        if rect_entree_map_3.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
            if cloporte_P == cloporte_P_down:
                y_cloporte_P -= 3
            elif cloporte_P == cloporte_P_up:
                y_cloporte_P += 3
            if cloporte_P == cloporte_P_left:
                x_cloporte_P += 3

        # changement de map, map_2 à map_1
        # base principal
         # entrée
        if rect_camp_P.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
            map_P = map_1
            x_cloporte_P = 640
            y_cloporte_P = 60

    # MAP PARAMETRE
    # verifier si l'utilisateur veut afficher les parametre
    if pressed[pygame.K_RETURN]:
        if map_P == map_1:
            map_precedente = map_1
        elif map_P == map_2:
            map_precedente = map_2

        map_P = map_parametre

    # gestion des choix et actions dans map parametre
    if map_P == map_parametre:
        # sortir des parametres
        if pressed[pygame.K_BACKSPACE]:
            map_P = map_precedente

        # <------------------ POUVOIR CLIQUER SUR AMELIORATION ;)
       # elif rect_logo_amelioration.colliderect(pressed[pygame.MOUSEBUTTONDOWN])

    # GENERATION D'OBJ
    tempo_obj += 1
    if tempo_obj == 2000 and len(DATABASE["obj_cree"]) != 30:
        tempo_obj = 0

        obj_alt = random.randint(1, 3)

        if obj_alt == 1:
            obj = buisson
            pv_obj = 10
        elif obj_alt == 2:
            obj = tronc
            pv_obj = 10
        elif obj_alt == 3:
            obj = arbre
            pv_obj = 20

        while True:
            y_obj = random.randint(25, 780)
            x_obj = random.randint(30, 725)
            rect_obj = obj.get_rect(x=x_obj, y=y_obj)

            if rect_foret_1.colliderect(rect_obj) or rect_foret_2.colliderect(rect_obj) or rect_foret_3.colliderect(rect_obj) or rect_foret_4.colliderect(rect_obj):
                DATABASE["num_lot_obj"] += 1
                num_obj = DATABASE["num_lot_obj"]
                DATABASE["obj_cree"][f"obj_{num_obj}"] = {}
                DATABASE["obj_cree"][f"obj_{num_obj}"]["type"] = obj_alt
                DATABASE["obj_cree"][f"obj_{num_obj}"]["x_obj"] = x_obj
                DATABASE["obj_cree"][f"obj_{num_obj}"]["y_obj"] = y_obj
                DATABASE["obj_cree"][f"obj_{num_obj}"]["rect_obj"] = obj_alt
                DATABASE["obj_cree"][f"obj_{num_obj}"]["PV_obj"] = pv_obj
                break

    # AFFICHAGE DE TOUTE LES SURFFACES
    screen.fill("black")
    screen.blit(map_P, (0, 0))
    #pygame.draw.rect(screen, "blue", rect_message_6)
    screen.blit(cloporte_P, (x_cloporte_P, y_cloporte_P))

    # AFFICHAGE BARRE DE RECOURCE (gauche vers droite)
    screen.blit(fond_barre_de_recource, (0, 848))
    # nbr feuille
    screen.blit(logo_buisson, (15, 860))
    nbr_feuille_reserve = str(DATABASE["stockage general"]["feuille"])
    x_chiffre_feuille_nbr = 50
    for i in nbr_feuille_reserve:
        numero = pygame.image.load(rf"numero_{i}.png").convert_alpha()
        screen.blit(numero, (x_chiffre_feuille_nbr, 860))
        x_chiffre_feuille_nbr += 16

    # nbr champignon
    screen.blit(logo_champignon, (250, 860))
    nbr_champignon_reserve = str(DATABASE["stockage general"]["champignon"])
    x_chiffre_champi_nbr = 285
    for i in nbr_champignon_reserve:
        numero = pygame.image.load(rf"numero_{i}.png").convert_alpha()
        screen.blit(numero, (x_chiffre_champi_nbr, 860))
        x_chiffre_champi_nbr += 16

    # logo parametres
    if map_P != map_parametre:
        screen.blit(logo_parametres, (1075, 862))
    else:
        screen.blit(logo_exit_parametre, (1075, 860))

    # AFFICHAGE NOURRITURE
    # affichage nourriture dans bouche cloporte_P
    if DATABASE["cloporte_P full"] == True:
        if DATABASE["cloporte_P type charge"] == "buisson":
            bout_de_nourriture = bout_de_buisson
        elif DATABASE["cloporte_P type charge"] == "tronc":
            bout_de_nourriture = bout_de_tronc

        if cloporte_P == cloporte_P_down:
            screen.blit(bout_de_nourriture,
                        (x_cloporte_P + 3, y_cloporte_P + 32))
        elif cloporte_P == cloporte_P_up:
            screen.blit(bout_de_nourriture,
                        (x_cloporte_P + 3, y_cloporte_P - 8))
        elif cloporte_P == cloporte_P_right:
            screen.blit(bout_de_nourriture,
                        (x_cloporte_P + 32, y_cloporte_P + 3))
        elif cloporte_P == cloporte_P_left:
            screen.blit(bout_de_nourriture,
                        (x_cloporte_P - 8, y_cloporte_P + 3))

    # lachage du bout de nourriture
    if (not rect_zone_stockage_feuille.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)) and not rect_zone_stockage_champi.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)) or map_P == map_2) and DATABASE["cloporte_P full"] == True and pressed[pygame.K_KP2]:
        pos_x_bout_de_nourriture = x_cloporte_P
        pos_y_bout_de_nourriture = y_cloporte_P
        map_du_bout_de_nourriture = map_P
        type_bout_de_nourriture = DATABASE["cloporte_P type charge"]
        bout_de_nourriture_lacher = True
        DATABASE["cloporte_P full"] = False

    # afficher et gerer bout de nourriture lacher
    if bout_de_nourriture_lacher == True and map_du_bout_de_nourriture == map_P:
        if type_bout_de_nourriture == "buisson":
            rect_bout_de_nourriture = bout_de_buisson.get_rect(
                x=pos_x_bout_de_nourriture, y=pos_y_bout_de_nourriture)
            bout_a_afficher = bout_de_buisson
        else:
            rect_bout_de_nourriture = bout_de_tronc.get_rect(
                x=pos_x_bout_de_nourriture, y=pos_y_bout_de_nourriture)
            bout_a_afficher = bout_de_tronc

        screen.blit(bout_a_afficher,
                    (pos_x_bout_de_nourriture, pos_y_bout_de_nourriture))

        if rect_bout_de_nourriture.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)) and pressed[pygame.K_KP3]:
            DATABASE["cloporte_P full"] = True
            bout_de_nourriture_lacher = False
        elif not rect_bout_de_nourriture.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)) and DATABASE["cloporte_P full"] == True:
            bout_de_nourriture_lacher = False

    if map_P == map_1:
        screen.blit(logo_buisson, (35, 200))
        screen.blit(logo_champignon, (35, 600))

        # afficher reserve feuille
        space = 0
        space_y = 0
        for i in range(DATABASE["stockage map_1"]["feuille"]):
            if i <= 109:
                pos_feuille_x = 100 + space
                space += 20
                if space == 200:
                    space = 0

                pos_feuille_y = 100 + space_y

                screen.blit(bout_de_buisson, (pos_feuille_x, pos_feuille_y))

                if space == 0:
                    space_y += 20

        # afficher reserve champignon
        space = 0
        space_y = 400
        for i in range(DATABASE["stockage map_1"]["champignon"]):
            if i <= 109:
                pos_champignon_x = 100 + space
                space += 20
                if space == 200:
                    space = 0

                pos_champignon_y = 100 + space_y

                screen.blit(bout_de_champignon,
                            (pos_champignon_x, pos_champignon_y))

                if space == 0:
                    space_y += 20

        # Nourriture déposée affichage
        # deposage feuille
        niveau_stockage_feuille_1 = DATABASE["niveaux"]["stockage feuille map_1"]
        if rect_zone_stockage_feuille.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)) and DATABASE["cloporte_P full"] == True and pressed[pygame.K_KP2] and DATABASE["cloporte_P type charge"] == "buisson" and DATABASE["stockage map_1"]["feuille"] != DATABASE["stockage max"]["reserve feuille"][f"niv {niveau_stockage_feuille_1}"]:
            DATABASE["cloporte_P full"] = False
            DATABASE["stockage general"]["feuille"] += 1
            DATABASE["stockage map_1"]["feuille"] += 1

            screen.blit(bout_de_buisson, (x_cloporte_P - 16, y_cloporte_P + 8))
            pygame.display.flip()
            time.sleep(0.5)
            screen.blit(no_life_barre, (x_cloporte_P - 35, y_cloporte_P - 10))
            pygame.display.flip()
            time.sleep(0.5)
            screen.blit(un_quart_life_barre,
                        (x_cloporte_P - 35, y_cloporte_P - 10))
            pygame.display.flip()
            time.sleep(0.5)
            screen.blit(demi_life_barre,
                        (x_cloporte_P - 35, y_cloporte_P - 10))
            pygame.display.flip()
            time.sleep(0.5)
            screen.blit(trois_quart_life_barre,
                        (x_cloporte_P - 35, y_cloporte_P - 10))
            pygame.display.flip()
            time.sleep(0.5)
            screen.blit(full_life_barre,
                        (x_cloporte_P - 35, y_cloporte_P - 10))
            pygame.display.flip()
            time.sleep(0.5)

        # deposage champi
        niveau_stockage_champi_1 = DATABASE["niveaux"]["stockage champignon map_1"]
        if rect_zone_stockage_champi.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)) and DATABASE["cloporte_P full"] == True and pressed[pygame.K_KP2] and DATABASE["stockage map_1"]["champignon"] != DATABASE["stockage max"]["reserve champignon"][f"niv {niveau_stockage_champi_1}"]:
            DATABASE["cloporte_P full"] = False
            DATABASE["stockage general"]["champignon"] += 1
            DATABASE["stockage map_1"]["champignon"] += 1

            bout_de_nourriture = DATABASE["cloporte_P type charge"]
            if bout_de_nourriture == "buisson":
                bout_de_nourriture = bout_de_buisson
            elif bout_de_nourriture == "tronc":
                bout_de_nourriture = bout_de_tronc

            screen.blit(bout_de_nourriture,
                        (x_cloporte_P - 16, y_cloporte_P + 8))
            pygame.display.flip()
            time.sleep(0.5)
            screen.blit(no_life_barre, (x_cloporte_P - 35, y_cloporte_P - 10))
            pygame.display.flip()
            time.sleep(0.5)
            screen.blit(un_quart_life_barre,
                        (x_cloporte_P - 35, y_cloporte_P - 10))
            pygame.display.flip()
            time.sleep(0.5)
            screen.blit(demi_life_barre,
                        (x_cloporte_P - 35, y_cloporte_P - 10))
            pygame.display.flip()
            time.sleep(0.5)
            screen.blit(trois_quart_life_barre,
                        (x_cloporte_P - 35, y_cloporte_P - 10))
            pygame.display.flip()
            time.sleep(0.5)
            screen.blit(full_life_barre,
                        (x_cloporte_P - 35, y_cloporte_P - 10))
            pygame.display.flip()
            time.sleep(0.5)

    if map_P == map_2 and len(DATABASE["obj_cree"]) != 0:
        # AFFICHAGE OBJ
        for i in DATABASE["obj_cree"]:
            obj = DATABASE["obj_cree"][i]["type"]
            if obj == 1:
                obj = buisson
            elif obj == 2:
                obj = tronc
            elif obj == 3:
                obj = arbre

            screen.blit(obj, (DATABASE["obj_cree"]
                        [i]["x_obj"], DATABASE["obj_cree"][i]["y_obj"]))

        # COLISION AVEC OBJ ET DISPARITION
        for i in DATABASE["obj_cree"]:
            type_obj = DATABASE["obj_cree"][i]["rect_obj"]
            x_obj = DATABASE["obj_cree"][i]["x_obj"]
            y_obj = DATABASE["obj_cree"][i]["y_obj"]

            if type_obj == 1:
                rect_obj = buisson.get_rect(
                    x=DATABASE["obj_cree"][i]["x_obj"], y=DATABASE["obj_cree"][i]["y_obj"])
            elif type_obj == 2:
                rect_obj = tronc.get_rect(
                    x=DATABASE["obj_cree"][i]["x_obj"], y=DATABASE["obj_cree"][i]["y_obj"])
            elif type_obj == 3:
                rect_obj = arbre.get_rect(
                    x=DATABASE["obj_cree"][i]["x_obj"], y=DATABASE["obj_cree"][i]["y_obj"])

            # disparition et collecte
            if rect_obj.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)) and pressed[pygame.K_KP_1] and DATABASE["cloporte_P full"] == False:
                DATABASE["cloporte_P full"] = True
                DATABASE["obj_cree"][i]["PV_obj"] -= 1
                type_obj = DATABASE["obj_cree"][i]["rect_obj"]
                pv_obj = DATABASE["obj_cree"][i]["PV_obj"]

                if type_obj == 1:
                    DATABASE["cloporte_P type charge"] = "buisson"
                elif type_obj == 2:
                    DATABASE["cloporte_P type charge"] = "tronc"
                elif type_obj == 3:
                    if pv_obj >= 10:
                        DATABASE["cloporte_P type charge"] = "buisson"
                    else:
                        DATABASE["cloporte_P type charge"] = "tronc"

                if DATABASE["obj_cree"][i]["PV_obj"] == 0:
                    del DATABASE["obj_cree"][i]
                    break
                else:
                    screen.blit(full_life_barre, (x_obj, y_obj - 25))
                    pygame.display.flip()
                    time.sleep(0.5)
                    screen.blit(trois_quart_life_barre, (x_obj, y_obj - 25))
                    pygame.display.flip()
                    time.sleep(0.5)
                    screen.blit(demi_life_barre, (x_obj, y_obj - 25))
                    pygame.display.flip()
                    time.sleep(0.5)
                    screen.blit(un_quart_life_barre, (x_obj, y_obj - 25))
                    pygame.display.flip()
                    time.sleep(0.5)
                    screen.blit(no_life_barre, (x_obj, y_obj - 25))
                    pygame.display.flip()
                    time.sleep(0.5)

            elif rect_obj.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)) and pressed[pygame.K_KP_1] and DATABASE["cloporte_P full"] == True:
                screen.blit(message_1, (x_cloporte_P, y_cloporte_P - 75))
                pygame.display.flip()
                time.sleep(1)

            # colision
            elif rect_obj.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
                if cloporte_P == cloporte_P_down:
                    y_cloporte_P -= 3
                if cloporte_P == cloporte_P_up:
                    y_cloporte_P += 3
                if cloporte_P == cloporte_P_left:
                    x_cloporte_P += 3
                if cloporte_P == cloporte_P_right:
                    x_cloporte_P -= 3

        # MESSAGE DANS MAP 2
        if rect_message_2.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
            screen.blit(message_2, (150, 200))
        elif rect_message_3.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
            screen.blit(message_3, (500, 450))
        elif rect_message_4.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
            screen.blit(message_4, (700, 620))
        elif rect_message_5.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
            screen.blit(message_5, (650, 75))
        elif rect_message_6.colliderect(cloporte_P.get_rect(x=x_cloporte_P, y=y_cloporte_P)):
            screen.blit(message_6, (200, 80))

    # afficher parametre par dessus cloporte
    if map_P == map_parametre:
        screen.blit(map_P, (0, 0))
        screen.blit(logo_ameliorations, (175, 150))

        # Verification si souris clique sur un logo (amelioration, etc...)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rect_souris = pygame.Rect(mouse_x, mouse_y, 15, 20)

        if souris_pressed:
            if rect_logo_amelioration.colliderect(rect_souris):
                map_P = map_amelioration

    # map_amelioration
    elif map_P == map_amelioration:
        screen.blit(map_P, (0, 0))

        # TITRES BASES
        screen.blit(logo_titre_base_principale, (40, 175))
        screen.blit(logo_titre_base_ouvriere, (340, 175))
        screen.blit(logo_titre_base_militaire, (640, 175))
        screen.blit(logo_titre_base_construction, (940, 175))

        # Sous titres de base
        # titre base principale
        screen.blit(logo_titre_reserve_feuille, (100, 240))
        screen.blit(logo_titre_reserve_champignon, (85, 570))

        # Barre de progression et logo niv
        # base principale
        niv_progression_barre = DATABASE["niveaux"]["stockage feuille map_1"]
        barre_progression_niv = pygame.image.load(
            rf"barre_progression_niv_{niv_progression_barre}.png")
        logo_niv = pygame.image.load(rf"logo_niv_{niv_progression_barre}.png")

        # blit des logos de reserve feuille map_1
        screen.blit(barre_progression_niv, (40, 270))
        screen.blit(logo_niv, (225, 298))
        screen.blit(logo_level_up_1, (20, 350))
        screen.blit(logo_buisson_level_up, (50, 402))
        screen.blit(logo_champignon_level_up, (145, 402))

        nbr_cost_feuille = DATABASE["cost"]["reserve feuille"][
            f"niv {niv_progression_barre}"][0]
        nbr_cost_champignon = DATABASE["cost"]["reserve feuille"][
            f"niv {niv_progression_barre}"][1]

        x_chiffre_level_up = 75
        for i in str(nbr_cost_feuille):
            chiffre_level_up = pygame.image.load(rf"nbr_cost_{i}.png")
            screen.blit(chiffre_level_up, (x_chiffre_level_up, 401))
            x_chiffre_level_up += 15

        x_chiffre_level_up = 170
        for i in str(nbr_cost_champignon):
            chiffre_level_up = pygame.image.load(rf"nbr_cost_{i}.png")
            screen.blit(chiffre_level_up, (x_chiffre_level_up, 401))
            x_chiffre_level_up += 15

        # Verification si souris clique sur un logo (amelioration, etc...)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rect_souris = pygame.Rect(mouse_x, mouse_y, 15, 20)

        if souris_pressed:
            # donnees necessaire pour actions
            level_reserve_feuille_map_1 = DATABASE["niveaux"]["stockage feuille map_1"]

            # retour map_parametre
            if rect_exit_map_amelioration.colliderect(rect_souris):
                map_P = map_parametre

            # validation de l'amelioration de la reserve de feuille map 1 (logo_level_up_1)
            elif rect_logo_level_up_1.colliderect(rect_souris) and DATABASE["stockage general"]["feuille"] >= DATABASE["cost"]["reserve feuille"][f"niv {level_reserve_feuille_map_1}"][0] and DATABASE["stockage general"]["champignon"] >= DATABASE["cost"]["reserve feuille"][f"niv {level_reserve_feuille_map_1}"][1] and level_reserve_feuille_map_1 != 10:
                # enlever le coup de l'amelioration de la reserve sur le stockage general et les stockages de bases
                cost_en_feuille = DATABASE["cost"]["reserve feuille"][
                    f"niv {level_reserve_feuille_map_1}"][0]
                cost_en_champi = DATABASE["cost"]["reserve feuille"][
                    f"niv {level_reserve_feuille_map_1}"][1]
                DATABASE["stockage general"]["feuille"] -= cost_en_feuille
                DATABASE["stockage general"]["champignon"] -= cost_en_champi

                # stockage de base feuille
                if DATABASE["stockage map_1"]["feuille"] >= cost_en_feuille:
                    DATABASE["stockage map_1"]["feuille"] -= cost_en_feuille
                elif DATABASE["stockage map_1"]["feuille"] < cost_en_feuille and DATABASE["stockage map_2"]["feuille"] >= (cost_en_feuille - DATABASE["stockage map_1"]["feuille"]):
                    cost_en_feuille -= DATABASE["stockage map_1"]["feuille"]
                    DATABASE["stockage map_1"]["feuille"] = 0
                    DATABASE["stockage map_2"]["feuille"] -= cost_en_feuille
                elif DATABASE["stockage map_1"]["feuille"] < cost_en_feuille and DATABASE["stockage map_2"]["feuille"] < (cost_en_feuille - DATABASE["stockage map_1"]["feuille"]) and DATABASE["stockage map_3"]["feuille"] >= (cost_en_feuille - (DATABASE["stockage map_1"]["feuille"] + DATABASE["stockage map_2"]["feuille"])):
                    cost_en_feuille -= DATABASE["stockage map_1"]["feuille"]
                    cost_en_feuille -= DATABASE["stockage map_2"]["feuille"]
                    DATABASE["stockage map_1"]["feuille"] = 0
                    DATABASE["stockage map_2"]["feuille"] = 0
                    DATABASE["stockage map_3"]["feuille"] -= cost_en_feuille
                else:
                    cost_en_feuille -= DATABASE["stockage map_1"]["feuille"]
                    cost_en_feuille -= DATABASE["stockage map_2"]["feuille"]
                    cost_en_feuille -= DATABASE["stockage map_3"]["feuille"]
                    DATABASE["stockage map_1"]["feuille"] = 0
                    DATABASE["stockage map_2"]["feuille"] = 0
                    DATABASE["stockage map_3"]["feuille"] = 0
                    DATABASE["stockage map_4"]["feuille"] -= cost_en_feuille

                # stockage de base champi
                if DATABASE["stockage map_1"]["champignon"] >= cost_en_champi:
                    DATABASE["stockage map_1"]["champignon"] -= cost_en_champi
                elif DATABASE["stockage map_1"]["champignon"] < cost_en_champi and DATABASE["stockage map_2"]["champignon"] >= (cost_en_champi - DATABASE["stockage map_1"]["champignon"]):
                    cost_en_champi -= DATABASE["stockage map_1"]["champignon"]
                    DATABASE["stockage map_1"]["champignon"] = 0
                    DATABASE["stockage map_2"]["champignon"] -= cost_en_champi
                elif DATABASE["stockage map_1"]["champignon"] < cost_en_champi and DATABASE["stockage map_2"]["champignon"] < (cost_en_champi - DATABASE["stockage map_1"]["champignon"]) and DATABASE["stockage map_3"]["champignon"] >= (cost_en_champi - (DATABASE["stockage map_1"]["champignon"] + DATABASE["stockage map_2"]["champignon"])):
                    cost_en_champi -= DATABASE["stockage map_1"]["champignon"]
                    cost_en_champi -= DATABASE["stockage map_2"]["champignon"]
                    DATABASE["stockage map_1"]["champignon"] = 0
                    DATABASE["stockage map_2"]["champignon"] = 0
                    DATABASE["stockage map_3"]["champignon"] -= cost_en_champi
                else:
                    cost_en_champi -= DATABASE["stockage map_1"]["champignon"]
                    cost_en_champi -= DATABASE["stockage map_2"]["champignon"]
                    cost_en_champi -= DATABASE["stockage map_3"]["champignon"]
                    DATABASE["stockage map_1"]["champignon"] = 0
                    DATABASE["stockage map_2"]["champignon"] = 0
                    DATABASE["stockage map_3"]["champignon"] = 0
                    DATABASE["stockage map_4"]["champignon"] -= cost_en_champi

                # Mise a niveau du stockage de feuille
                DATABASE["niveaux"]["stockage feuille map_1"] += 1

                # Temps de l'amelioration
                time.sleep(0.5)

    pygame.display.flip()

    # reglage de la vitesse d'affichage
    clock.tick(70)

# Décharger le cloporte
DATABASE["cloporte_P full"] = False

# SAUVEGARDE DE LA PARTIE
with open(chemin_database, "w") as database_open:
    json.dump(DATABASE, database_open, indent=4, ensure_ascii=False)
