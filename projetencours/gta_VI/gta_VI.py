import pygame
import random
from pathlib import Path
import json
import time


# initialisation

pygame.init()
screen = pygame.display.set_mode((1280, 896))
pygame.display.set_caption("GTA VI")
image = pygame.image
clock = pygame.time.Clock()

# creer le chemin json si il n'existe pas et l'importer

chemin_DATABASE = Path(r"gta_VI.json")

if not chemin_DATABASE.exists():
    DATABASE_dump = {}

    with open(chemin_DATABASE, "w") as file_open:
        json.dump(DATABASE_dump, file_open, ensure_ascii=False, indent=4)

with open(chemin_DATABASE, "r") as file_open:
    DATABASE = json.load(file_open)

# maps et decors
# maps

map_6 = image.load(r"map_6.png").convert_alpha()
x_map_6 = 1296
y_map_6 = 0

map_1 = map_6
x_map_1 = -1296
y_map_1 = - 896

map_2 = map_6
x_map_2 = 0
y_map_2 = - 896

map_3 = map_6
x_map_3 = 1296
y_map_3 = - 896

map_4 = map_6
x_map_4 = -1296
y_map_4 = 0

map_5 = map_6
x_map_5 = 0
y_map_5 = 0

map_7 = map_6
x_map_7 = - 1296
y_map_7 = 896

map_8 = map_6
x_map_8 = 0
y_map_8 = 896

map_9 = map_6
x_map_9 = 1296
y_map_9 = 896

# colision avec les objet statique (maison, etc...)
x_rect_maison_1_map_6 = 1315
y_rect_maison_1_map_6 = 29
rect_maison_1_map_6 = pygame.Rect(
    x_rect_maison_1_map_6, y_rect_maison_1_map_6, 320, 181)

x_rect_maison_2_map_6 = 1315
y_rect_maison_2_map_6 = 370
rect_maison_2_map_6 = pygame.Rect(
    x_rect_maison_2_map_6, y_rect_maison_2_map_6, 320, 181)


# reglage perso

franklin_up = pygame.image.load(r"franklin_up.png").convert_alpha()
franklin_down = pygame.image.load(r"franklin_down.png").convert_alpha()
franklin_left = pygame.image.load(r"franklin_left.png").convert_alpha()
franklin_right = pygame.image.load(r"franklin_right.png").convert_alpha()
franklin = franklin_up

x_franklin = 640
y_franklin = 448

dict_action_perso = {"conduire": [False, None, None, None, None]}

# objets
# voitures

voiture_verte_up = image.load(r"voiture_verte_up.png").convert_alpha()
voiture_verte_down = image.load(r"voiture_verte_down.png").convert_alpha()
voiture_verte_right = image.load(r"voiture_verte_right.png").convert_alpha()
voiture_verte_left = image.load(r"voiture_verte_left.png").convert_alpha()

voiture_verte_1 = voiture_verte_left
x_voiture_verte_1 = 1415
y_voiture_verte_1 = 218


voiture_rouge_up = image.load(r"voiture_rouge_up.png").convert_alpha()
voiture_rouge_down = image.load(r"voiture_rouge_down.png").convert_alpha()
voiture_rouge_right = image.load(r"voiture_rouge_right.png").convert_alpha()
voiture_rouge_left = image.load(r"voiture_rouge_left.png").convert_alpha()

voiture_rouge_1 = voiture_rouge_left
x_voiture_rouge_1 = 1415
y_voiture_rouge_1 = 560


# variables booléens du jeu
vitesse_voiture = 0.1
stop_walk = False
play = True

# boucle du jeu
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    pressed = pygame.key.get_pressed()

    # mise à jour des positions des objets statique
    rect_maison_1_map_6 = pygame.Rect(
        x_rect_maison_1_map_6, y_rect_maison_1_map_6, 320, 181)
    rect_maison_2_map_6 = pygame.Rect(
        x_rect_maison_2_map_6, y_rect_maison_2_map_6, 320, 181)

    # colision avec les objets statiques
    if rect_maison_1_map_6.colliderect(franklin.get_rect(x=x_franklin, y=y_franklin)):
        stop_walk = True

    # Actions perso
    # desactiver le stop_walk
    if stop_walk == True:
        if franklin == franklin_down and (pressed[pygame.K_UP] or pressed[pygame.K_z]) and (not pressed[pygame.K_RIGHT] and not pressed[pygame.K_d]) and (not pressed[pygame.K_LEFT] and not pressed[pygame.K_q]):
            stop_walk = False
        elif franklin == franklin_up and (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and (not pressed[pygame.K_RIGHT] and not pressed[pygame.K_d]) and (not pressed[pygame.K_LEFT] and not pressed[pygame.K_q]):
            stop_walk = False
        elif franklin == franklin_left and (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and (not pressed[pygame.K_DOWN] and not pressed[pygame.K_s]) and (not pressed[pygame.K_UP] and not pressed[pygame.K_z]):
            stop_walk = False
        elif franklin == franklin_right and (pressed[pygame.K_LEFT] or pressed[pygame.K_q]) and (not pressed[pygame.K_DOWN] and not pressed[pygame.K_s]) and (not pressed[pygame.K_UP] and not pressed[pygame.K_z]):
            stop_walk = False
        elif dict_action_perso["conduire"][0] == True:
            stop_walk = False

    # avancer
    if (pressed[pygame.K_UP] or pressed[pygame.K_z]) and stop_walk == False:
        y_map_1 += 1
        y_map_2 += 1
        y_map_3 += 1
        y_map_4 += 1
        y_map_5 += 1
        y_map_6 += 1
        y_map_7 += 1
        y_map_8 += 1
        y_map_9 += 1
        y_rect_maison_1_map_6 += 1
        y_rect_maison_2_map_6 += 1
        y_voiture_verte_1 += 1
        y_voiture_rouge_1 += 1
        franklin = franklin_up
    elif (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and stop_walk == False:
        y_map_1 -= 1
        y_map_2 -= 1
        y_map_3 -= 1
        y_map_4 -= 1
        y_map_5 -= 1
        y_map_6 -= 1
        y_map_7 -= 1
        y_map_8 -= 1
        y_map_9 -= 1
        y_rect_maison_1_map_6 -= 1
        y_rect_maison_2_map_6 -= 1
        y_voiture_verte_1 -= 1
        y_voiture_rouge_1 -= 1
        franklin = franklin_down
    elif (pressed[pygame.K_LEFT] or pressed[pygame.K_q]) and stop_walk == False:
        x_map_1 += 1
        x_map_2 += 1
        x_map_3 += 1
        x_map_4 += 1
        x_map_5 += 1
        x_map_6 += 1
        x_map_7 += 1
        x_map_8 += 1
        x_map_9 += 1
        x_rect_maison_1_map_6 += 1
        x_rect_maison_2_map_6 += 1
        x_voiture_verte_1 += 1
        x_voiture_rouge_1 += 1
        franklin = franklin_left
    elif (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and stop_walk == False:
        x_map_1 -= 1
        x_map_2 -= 1
        x_map_3 -= 1
        x_map_4 -= 1
        x_map_5 -= 1
        x_map_6 -= 1
        x_map_7 -= 1
        x_map_8 -= 1
        x_map_9 -= 1
        x_rect_maison_1_map_6 -= 1
        x_rect_maison_2_map_6 -= 1
        x_voiture_verte_1 -= 1
        x_voiture_rouge_1 -= 1
        franklin = franklin_right

    # Actions voiture
    # colision avec les voitures
    if voiture_verte_1.get_rect(x=x_voiture_verte_1, y=y_voiture_verte_1).colliderect(franklin.get_rect(x=x_franklin, y=y_franklin)) and not pressed[pygame.K_1] and not pressed[pygame.K_KP_1] and not pressed[pygame.K_KP1]:
        stop_walk = True
    elif voiture_rouge_1.get_rect(x=x_voiture_rouge_1, y=y_voiture_rouge_1).colliderect(franklin.get_rect(x=x_franklin, y=y_franklin)) and not pressed[pygame.K_1] and not pressed[pygame.K_KP_1] and not pressed[pygame.K_KP1]:
        stop_walk = True

    # rentrer dans une voiture
    # voiture verte 1
    if dict_action_perso["conduire"][0] == False:
        if voiture_verte_1.get_rect(x=x_voiture_verte_1, y=y_voiture_verte_1).colliderect(franklin.get_rect(x=x_franklin, y=y_franklin)) and (pressed[pygame.K_1] or pressed[pygame.K_KP_1] or pressed[pygame.K_KP1]) and dict_action_perso["conduire"][0] == False:
            dict_action_perso["conduire"][1] = voiture_verte_1
            dict_action_perso["conduire"][2] = voiture_verte_1.get_rect(
                x=x_voiture_verte_1, y=y_voiture_verte_1)
            dict_action_perso["conduire"][3] = x_voiture_verte_1
            dict_action_perso["conduire"][4] = y_voiture_verte_1
            dict_action_perso["conduire"][0] = True

        elif voiture_rouge_1.get_rect(x=x_voiture_rouge_1, y=y_voiture_rouge_1).colliderect(franklin.get_rect(x=x_franklin, y=y_franklin)) and (pressed[pygame.K_1] or pressed[pygame.K_KP_1] or pressed[pygame.K_KP1]) and dict_action_perso["conduire"][0] == False:
            dict_action_perso["conduire"][1] = voiture_rouge_1
            dict_action_perso["conduire"][2] = voiture_rouge_1.get_rect(
                x=x_voiture_rouge_1, y=y_voiture_rouge_1)
            dict_action_perso["conduire"][3] = x_voiture_rouge_1
            dict_action_perso["conduire"][4] = y_voiture_rouge_1
            dict_action_perso["conduire"][0] = True

    # conduire
    elif dict_action_perso["conduire"][0] == True:
        # voiture verte 1
        if dict_action_perso["conduire"][1] == voiture_verte_1:
            if pressed[pygame.K_UP] or pressed[pygame.K_z]:
                y_map_1 += vitesse_voiture
                y_map_2 += vitesse_voiture
                y_map_3 += vitesse_voiture
                y_map_4 += vitesse_voiture
                y_map_5 += vitesse_voiture
                y_map_6 += vitesse_voiture
                y_map_7 += vitesse_voiture
                y_map_8 += vitesse_voiture
                y_map_9 += vitesse_voiture
                y_rect_maison_1_map_6 += vitesse_voiture
                y_rect_maison_2_map_6 += vitesse_voiture
                y_voiture_rouge_1 += vitesse_voiture
                y_voiture_verte_1 -= 1
                if vitesse_voiture < 7:
                    vitesse_voiture += 0.01
                dict_action_perso["conduire"][1] = voiture_verte_up
                voiture_verte_1 = voiture_verte_up
            elif pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
                y_map_1 -= vitesse_voiture
                y_map_2 -= vitesse_voiture
                y_map_3 -= vitesse_voiture
                y_map_4 -= vitesse_voiture
                y_map_5 -= vitesse_voiture
                y_map_6 -= vitesse_voiture
                y_map_7 -= vitesse_voiture
                y_map_8 -= vitesse_voiture
                y_map_9 -= vitesse_voiture
                y_rect_maison_1_map_6 -= vitesse_voiture
                y_rect_maison_2_map_6 -= vitesse_voiture
                y_voiture_rouge_1 -= vitesse_voiture
                y_voiture_verte_1 += 1
                if vitesse_voiture < 7:
                    vitesse_voiture += 0.01
                dict_action_perso["conduire"][1] = voiture_verte_down
                voiture_verte_1 = voiture_verte_down
            elif pressed[pygame.K_LEFT] or pressed[pygame.K_q]:
                x_map_1 += vitesse_voiture
                x_map_2 += vitesse_voiture
                x_map_3 += vitesse_voiture
                x_map_4 += vitesse_voiture
                x_map_5 += vitesse_voiture
                x_map_6 += vitesse_voiture
                x_map_7 += vitesse_voiture
                x_map_8 += vitesse_voiture
                x_map_9 += vitesse_voiture
                x_rect_maison_1_map_6 += vitesse_voiture
                x_rect_maison_2_map_6 += vitesse_voiture
                x_voiture_rouge_1 += vitesse_voiture
                x_voiture_verte_1 -= 1
                if vitesse_voiture < 7:
                    vitesse_voiture += 0.01
                dict_action_perso["conduire"][1] = voiture_verte_left
                voiture_verte_1 = voiture_verte_left
            elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                x_map_1 -= vitesse_voiture
                x_map_2 -= vitesse_voiture
                x_map_3 -= vitesse_voiture
                x_map_4 -= vitesse_voiture
                x_map_5 -= vitesse_voiture
                x_map_6 -= vitesse_voiture
                x_map_7 -= vitesse_voiture
                x_map_8 -= vitesse_voiture
                x_map_9 -= vitesse_voiture
                x_rect_maison_1_map_6 -= vitesse_voiture
                x_rect_maison_2_map_6 -= vitesse_voiture
                x_voiture_rouge_1 -= vitesse_voiture
                x_voiture_verte_1 += 1
                if vitesse_voiture < 7:
                    vitesse_voiture += 0.01
                dict_action_perso["conduire"][1] = voiture_verte_right
                voiture_verte_1 = voiture_verte_right
            else:
                if vitesse_voiture != 0:
                    vitesse_voiture -= 0.04
                if vitesse_voiture <= 0:
                    vitesse_voiture = 0

            # quitter voiture_verte_1
            if pressed[pygame.K_2] or pressed[pygame.K_KP2] or pressed[pygame.K_KP_2]:
                x_franklin = 640
                y_franklin = 448
                franklin = franklin_left
                x_voiture_verte_1 = 675
                vitesse_voiture = 0
                stop_walk = False
                dict_action_perso["conduire"][0] = False

        # voiture rouge 1
        if dict_action_perso["conduire"][1] == voiture_rouge_1:
            if pressed[pygame.K_UP] or pressed[pygame.K_z]:
                y_map_1 += vitesse_voiture
                y_map_2 += vitesse_voiture
                y_map_3 += vitesse_voiture
                y_map_4 += vitesse_voiture
                y_map_5 += vitesse_voiture
                y_map_6 += vitesse_voiture
                y_map_7 += vitesse_voiture
                y_map_8 += vitesse_voiture
                y_map_9 += vitesse_voiture
                y_rect_maison_1_map_6 += vitesse_voiture
                y_rect_maison_2_map_6 += vitesse_voiture
                y_voiture_verte_1 += vitesse_voiture
                y_voiture_rouge_1 -= 1
                if vitesse_voiture < 7:
                    vitesse_voiture += 0.01
                dict_action_perso["conduire"][1] = voiture_rouge_up
                voiture_rouge_1 = voiture_rouge_up
            elif pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
                y_map_1 -= vitesse_voiture
                y_map_2 -= vitesse_voiture
                y_map_3 -= vitesse_voiture
                y_map_4 -= vitesse_voiture
                y_map_5 -= vitesse_voiture
                y_map_6 -= vitesse_voiture
                y_map_7 -= vitesse_voiture
                y_map_8 -= vitesse_voiture
                y_map_9 -= vitesse_voiture
                y_rect_maison_1_map_6 -= vitesse_voiture
                y_rect_maison_2_map_6 -= vitesse_voiture
                y_voiture_verte_1 -= vitesse_voiture
                y_voiture_rouge_1 += 1
                if vitesse_voiture < 7:
                    vitesse_voiture += 0.01
                dict_action_perso["conduire"][1] = voiture_rouge_down
                voiture_rouge_1 = voiture_rouge_down
            elif pressed[pygame.K_LEFT] or pressed[pygame.K_q]:
                x_map_1 += vitesse_voiture
                x_map_2 += vitesse_voiture
                x_map_3 += vitesse_voiture
                x_map_4 += vitesse_voiture
                x_map_5 += vitesse_voiture
                x_map_6 += vitesse_voiture
                x_map_7 += vitesse_voiture
                x_map_8 += vitesse_voiture
                x_map_9 += vitesse_voiture
                x_rect_maison_1_map_6 += vitesse_voiture
                x_rect_maison_2_map_6 += vitesse_voiture
                x_voiture_verte_1 += vitesse_voiture
                x_voiture_rouge_1 -= 1
                if vitesse_voiture < 7:
                    vitesse_voiture += 0.01
                dict_action_perso["conduire"][1] = voiture_rouge_left
                voiture_rouge_1 = voiture_rouge_left
            elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                x_map_1 -= vitesse_voiture
                x_map_2 -= vitesse_voiture
                x_map_3 -= vitesse_voiture
                x_map_4 -= vitesse_voiture
                x_map_5 -= vitesse_voiture
                x_map_6 -= vitesse_voiture
                x_map_7 -= vitesse_voiture
                x_map_8 -= vitesse_voiture
                x_map_9 -= vitesse_voiture
                x_rect_maison_1_map_6 -= vitesse_voiture
                x_rect_maison_2_map_6 -= vitesse_voiture
                x_voiture_verte_1 -= vitesse_voiture
                x_voiture_rouge_1 += 1
                if vitesse_voiture < 7:
                    vitesse_voiture += 0.01
                dict_action_perso["conduire"][1] = voiture_rouge_right
                voiture_rouge_1 = voiture_rouge_right
            else:
                if vitesse_voiture != 0:
                    vitesse_voiture -= 0.04
                if vitesse_voiture <= 0:
                    vitesse_voiture = 0

            # quitter voiture_rouge_1
            if pressed[pygame.K_2] or pressed[pygame.K_KP2] or pressed[pygame.K_KP_2]:
                x_franklin = 640
                y_franklin = 448
                franklin = franklin_left
                x_voiture_rouge_1 = 675
                vitesse_voiture = 0
                stop_walk = False
                dict_action_perso["conduire"][0] = False

    # Gestion d'affichage
    # bliter les images
    screen.fill("black")

    # maps
    screen.blit(map_1, (x_map_1, y_map_1))
    screen.blit(map_2, (x_map_2, y_map_2))
    screen.blit(map_3, (x_map_3, y_map_3))
    screen.blit(map_4, (x_map_4, y_map_4))
    screen.blit(map_5, (x_map_5, y_map_5))
    screen.blit(map_6, (x_map_6, y_map_6))
    screen.blit(map_7, (x_map_7, y_map_7))
    screen.blit(map_8, (x_map_8, y_map_8))
    screen.blit(map_9, (x_map_9, y_map_9))

    if not dict_action_perso["conduire"][0] == True:
        screen.blit(franklin, (x_franklin, y_franklin))

    screen.blit(voiture_verte_1, (x_voiture_verte_1, y_voiture_verte_1))
    screen.blit(voiture_rouge_1, (x_voiture_rouge_1, y_voiture_rouge_1))

    # affichage temporaire des rect
    pygame.draw.rect(screen, "blue", rect_maison_2_map_6)

    # mettre a jour l'écran
    pygame.display.flip()

    # reglage de la vitesse du jeu
    clock.tick(150)
