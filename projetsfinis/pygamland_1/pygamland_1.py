import pygame
import time
from pathlib import Path
import json
import random

# initialiser les composants et création de la fenêtre
pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Conception idée colision")

# donnees menu
menu = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\MENU.png").convert()
logo_menu = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\LOGO_MENU_0p2.png").convert()
logo_jeu_1 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\LOGO_jeu_1.png").convert()
logo_jeu_2 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\LOGO_jeu_2.png").convert()

# donnees JEU N°1
menu_game_over_gre = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\menu_fond_game_over.png").convert()
logo_game_over_point_exclamation = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\LOGO_game_over_avec_un_!.png").convert()
logo_game_over = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\LOGO_game_over.png").convert()
logo_rejouer = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\LOGO_rejouer.png").convert()
logo_retour_menu = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\LOGO_retour_menu.png").convert()

grenouille_ima = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\grenouille.png").convert()
x_gre = 0
y_gre = 0

spawner_grenouille = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\spawner_grenouille.png").convert()
grenouille_ima_2 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\grenouille_2.png").convert()
grenouille_2 = False
x_gre_2 = 350
y_gre_2 = 350
grenouille_ima_3 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\grenouille_3.png").convert()
grenouille_3 = False
x_gre_3 = 350
y_gre_3 = 350
acceleration = True


mini_bonhomme = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\ptit_bonhomme.png").convert()
x_mnb = 0
y_mnb = 0

map = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map.png").convert()

dec_3 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\3_dec.png").convert()
dec_2 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\2_dec.png").convert()
dec_1 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\1_dec.png").convert()

score = 0
cadre_du_score = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\cadre_du_score.png").convert()
logo_score = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\LOGO_score.png").convert()
score_final = 0
affichage_score = "0"
numero = "0"
record_battu_1 = False
logo_nouveau_record_ima = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\LOGO_nouveau_record.png")

retrecicement = 0

time_spawn_gre = 0

clock = pygame.time.Clock()

x_gauche_zone = 0
x_droite_zone = 775
y_haut_zone = 0
y_bas_zone = 775

# DONNEES JEU N°2

map_jeu_2 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\MAP_jeu_2.png").convert()
ciel_jeu_2 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\ciel_jeu_2.png").convert()
x_ciel = 0
x_ciel_2 = x_ciel + 800
tempo_ciel = 0

sol = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\sol_map_jeu_2.png").convert()
x_sol = 0
x_sol_2 = x_sol + 800

# les tuyaux

# taille des tuyaux et adaptation en y
tuyau_verts_T1 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\TUYAU_vert_jeu_2.png").convert()
y_tuyau_T1 = 480
tuyau_verts_T2 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\TUYAU_T2_vert_jeu_2.png").convert()
y_tuyau_T2 = 460
tuyau_verts_T3 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\TUYAU_T3_vert_jeu_2.png").convert()
y_tuyau_T3 = 425

tuyau_verts_inverse_T1 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\TUYAU_à_l'envers_jeu_2.png").convert()
tuyau_verts_inverse_T2 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\TUYAU_T2_à_l'envers_jeu_2.png").convert()
tuyau_verts_inverse_T3 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\TUYAU_T3_à_l'envers_jeu_2.png").convert()

# tuyau et leur position
tuyau_pas_encore_creer = False
tempo_resserement_tuyau = 0
ecartement_tuyau = 300

tuyau_1 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\RIEN.png")
tuyau_2 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\RIEN.png")
tuyau_3 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\RIEN.png")

x_tuyau_1 = 700
x_tuyau_2 = x_tuyau_1 + (ecartement_tuyau * 2)
x_tuyau_3 = x_tuyau_1 + (ecartement_tuyau * 4)

y_tuyau_1 = 0
y_tuyau_2 = 0
y_tuyau_3 = 0

tuyau_inverse_1 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\RIEN.png")
tuyau_inverse_2 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\RIEN.png")
tuyau_inverse_3 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\RIEN.png")

x_tuyau_inverse_1 = x_tuyau_1 + ecartement_tuyau
x_tuyau_inverse_2 = x_tuyau_inverse_1 + (ecartement_tuyau * 2)
x_tuyau_inverse_3 = x_tuyau_inverse_1 + (ecartement_tuyau * 4)
#

perso_bird = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\PERSO_bird_jeu_2.png").convert()
perso_bird_tombe = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\PERSO_bird_tombe_jeu_2.png").convert()
y_bird = 300
dec_tombe = 0

dec_1_jeu_2 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\1_dec_jeu_2.png").convert()
dec_2_jeu_2 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\2_dec_jeu_2.png").convert()
dec_3_jeu_2 = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\3_dec_jeu_2.png").convert()

animation_bird_tombe = False

vitesse_fois_2 = False


score_jeu_2 = 0
record_battu_2 = False
record_jeu_2 = 0

# DONNEES GENERAL
running = True

menu_1 = True
play_1 = False
play_2 = False
tempo = False
game_over_play_1 = False
game_over_play_2 = False

record_play_1_ima = pygame.image.load(
    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\record_play_1.png")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if menu_1 == True:
        # affichage du menu
        screen.blit(menu, (0, 0))
        screen.blit(logo_menu, (200, 75))
        screen.blit(logo_jeu_1, (75, 275))
        screen.blit(logo_jeu_2, (425, 275))

        # reinitialisation JEU N°1
        # verification de si la partie du jeu_1 est lancée
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_1] or pressed[pygame.K_KP1] or pressed[pygame.K_KP_1]:
            play_1 = True
            menu_1 = False

        # réinitialisation des paramètres de la partie 1
        x_gre = 200
        y_gre = 150

        grenouille_2 = False
        x_gre_2 = 350
        y_gre_2 = 350

        grenouille_3 = False
        x_gre_3 = 350
        y_gre_3 = 350

        acceleration = True

        x_mnb = 600
        y_mnb = 150

        x_gauche_zone = 0
        x_droite_zone = 775
        y_haut_zone = 0
        y_bas_zone = 775

        tempo = True

        score = 0
        score_final = 0
        affichage_score = "0"
        numero = "0"
        record_battu_1 = False

        time_spawn_gre = 0

        map = pygame.image.load(
            r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map.png").convert()

        # reinitialisation JEU N°2
        # verification de si la partie du jeu_2 est lancée
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_2] or pressed[pygame.K_KP2] or pressed[pygame.K_KP_2]:
            play_2 = True
            menu_1 = False

        # réinitialisation des paramètres de la partie
        tempo = True

        perso_bird = pygame.image.load(
            r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\PERSO_bird_jeu_2.png").convert()
        y_bird = 300
        dec_tombe = 0

        x_ciel = 0
        x_ciel_2 = x_ciel + 800

        x_sol = 0
        x_sol_2 = x_sol + 800

        tuyau_pas_encore_creer = True
        tempo_resserement_tuyau = 0
        ecartement_tuyau = 300

        x_tuyau = 700
        x_tuyau_2 = x_tuyau + (ecartement_tuyau * 2)
        x_tuyau_3 = x_tuyau + (ecartement_tuyau * 4)
        y_tuyau = 0
        y_tuyau_2 = 0
        y_tuyau_3 = 0

        x_tuyau_inverse_1 = x_tuyau_1 + ecartement_tuyau
        x_tuyau_inverse_1 = x_tuyau_inverse_1 + (ecartement_tuyau * 2)
        x_tuyau_inverse_1 = x_tuyau_inverse_1 + (ecartement_tuyau * 4)

        animation_bird_tombe = False

        vitesse_fois_2 = False

        score_jeu_2 = 0

        game_over_play_2 = False
        record_battu_2 = False

    # JEU N°1
    if play_1 == True:

        # déplacement bonhomme
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            x_mnb -= 1

        if pressed[pygame.K_RIGHT]:
            x_mnb += 1

        if pressed[pygame.K_UP]:
            y_mnb -= 1

        if pressed[pygame.K_DOWN]:
            y_mnb += 1

        # déplacement grenouilles
        if x_gre < x_mnb:
            x_gre += 0.5
        elif x_gre > x_mnb:
            x_gre -= 0.5
        if y_gre < y_mnb:
            y_gre += 0.5
        elif y_gre > y_mnb:
            y_gre -= 0.5

        if grenouille_2 == True:
            if x_gre_2 < x_mnb:
                if acceleration == False:
                    x_gre_2 += 0.5
                    acceleration = True
                else:
                    x_gre_2 += 1
                    acceleration = False

            elif x_gre_2 > x_mnb:
                x_gre_2 -= 0.5
            if y_gre_2 < y_mnb:
                y_gre_2 += 0.5
            elif y_gre_2 > y_mnb:
                y_gre_2 -= 0.5

        if grenouille_3 == True:
            if x_gre_3 < x_mnb:
                x_gre_3 += 0.5
            elif x_gre_3 > x_mnb:
                x_gre_3 -= 0.5
            if y_gre_3 < y_mnb:
                y_gre_3 += 0.5
            elif y_gre_3 > y_mnb:
                if acceleration == False:
                    y_gre_3 -= 0.5
                    acceleration = True
                else:
                    y_gre_3 -= 1
                    acceleration = False

        # déplacement et conception de la zone

        if x_mnb == x_gauche_zone:
            play_1 = False

        if x_mnb == x_droite_zone:
            play_1 = False

        if y_mnb == y_haut_zone:
            play_1 = False

        if y_mnb == y_bas_zone:
            play_1 = False

        if x_gauche_zone < 250 and x_droite_zone > 525 and y_haut_zone < 250 and y_bas_zone > 525:
            retrecicement += 2.5
            if retrecicement == 100:
                retrecicement -= 100
                x_gauche_zone += 1
                x_droite_zone -= 1
                y_haut_zone += 1
                y_bas_zone -= 1

            if x_gauche_zone == 16 and y_haut_zone == 16:
                map = pygame.image.load(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map_2.png").convert()

            if x_gauche_zone == 32 and y_haut_zone == 32:
                map = pygame.image.load(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map_3.png").convert()

            if x_gauche_zone == 48 and y_haut_zone == 48:
                map = pygame.image.load(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map_4.png").convert()

            if x_gauche_zone == 64 and y_haut_zone == 64:
                map = pygame.image.load(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map_5.png").convert()

            if x_gauche_zone == 80 and y_haut_zone == 80:
                map = pygame.image.load(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map_6.png").convert()

            if x_gauche_zone == 96 and y_haut_zone == 96:
                map = pygame.image.load(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map_7.png").convert()

            if x_gauche_zone == 112 and y_haut_zone == 112:
                map = pygame.image.load(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map_8.png").convert()

            if x_gauche_zone == 128 and y_haut_zone == 128:
                map = pygame.image.load(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map_9.png").convert()

            if x_gauche_zone == 144 and y_haut_zone == 144:
                map = pygame.image.load(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map_10.png").convert()

            if x_gauche_zone == 160 and y_haut_zone == 160:
                map = pygame.image.load(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map_11.png").convert()

            if x_gauche_zone == 176 and y_haut_zone == 176:
                map = pygame.image.load(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map_12.png").convert()

            if x_gauche_zone == 192 and y_haut_zone == 192:
                map = pygame.image.load(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map_13.png").convert()

            if x_gauche_zone == 208 and y_haut_zone == 208:
                map = pygame.image.load(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map_14.png").convert()

            if x_gauche_zone == 224 and y_haut_zone == 224:
                map = pygame.image.load(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map_15.png").convert()

            if x_gauche_zone == 240 and y_haut_zone == 240:
                map = pygame.image.load(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map_16.png").convert()

            if x_gauche_zone == 249 and y_haut_zone == 249:
                map = pygame.image.load(
                    r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map_17.png").convert()

        if x_mnb < x_gauche_zone:
            play_1 = False

        if x_mnb > x_droite_zone:
            play_1 = False

        if y_mnb < y_haut_zone:
            play_1 = False

        if y_mnb > y_bas_zone:
            play_1 = False

        # spawner à grenouille

        ver_x_mnb = x_mnb
        ver_y_mnb = y_mnb
        pos_mnb = (ver_x_mnb, ver_y_mnb)

        pos_x_spawner = 360
        pos_y_spawner = 360
        pos_spawner = (pos_x_spawner, pos_y_spawner)

        for verification in range(100):
            if pos_mnb == pos_spawner:
                y_mnb -= 15

            pos_x_spawner += 1
            pos_spawner = (pos_x_spawner, pos_y_spawner)

        for verification in range(100):
            if pos_mnb == pos_spawner:
                x_mnb += 15

            pos_y_spawner += 1
            pos_spawner = (pos_x_spawner, pos_y_spawner)

        for verification in range(100):

            if pos_mnb == pos_spawner:
                y_mnb += 15

            pos_x_spawner -= 1
            pos_spawner = (pos_x_spawner, pos_y_spawner)

        for verification in range(100):

            if pos_mnb == pos_spawner:
                x_mnb -= 15

            pos_y_spawner -= 1
            pos_spawner = (pos_x_spawner, pos_y_spawner)

        time_spawn_gre += 1
        if time_spawn_gre == 2000:
            grenouille_2 = True
            x_gre_2 = 400
            y_gre_2 = 400

        elif time_spawn_gre == 4000:
            grenouille_3 = True
            x_gre_3 = 400
            y_gre_3 = 400

        # mise a jour de la surfface
        screen.fill((0, 0, 0))

        screen.blit(map, (0, 0))
        screen.blit(mini_bonhomme, (x_mnb, y_mnb))
        screen.blit(spawner_grenouille, (380, 380))
        screen.blit(grenouille_ima, (x_gre, y_gre))
        if grenouille_2 == True:
            screen.blit(grenouille_ima_2, (x_gre_2, y_gre_2))

        if grenouille_3 == True:
            screen.blit(grenouille_ima_3, (x_gre_3, y_gre_3))

        # mise à jour du score

        score += 1
        if score == 200:
            score_final += 1
            affichage_score = str(score_final)
            score -= 200

        screen.blit(cadre_du_score, (0, 0))
        screen.blit(logo_score, (10, 10))

        x_numero = 300
        for aff in affichage_score:
            numero = pygame.image.load(
                rf"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\{aff}.png").convert()
            screen.blit(numero, (x_numero, 25))
            x_numero += 25

        # verification du contact entre le bonhomme et le logo score
        ver_x_mnb = x_mnb
        ver_y_mnb = y_mnb
        pos_mnb = (ver_x_mnb, ver_y_mnb)
        x_score = 0
        y_score = 75
        for verification in range(425):
            if pos_mnb == (x_score, y_score):
                y_mnb += 20

            x_score += 1

        for verification in range(75):
            if pos_mnb == (x_score, y_score):
                x_mnb += 20

            y_score -= 1

        # verification de la collision entre la grenouille et le bonhomme
        # grenouille 1
        ver_x_gre = x_gre
        ver_y_gre = y_gre
        pos_gre = (ver_x_gre, ver_y_gre)
        ver_x_mnb = x_mnb
        ver_y_mnb = y_mnb
        pos_mnb = (ver_x_mnb, ver_y_mnb)

        if pos_gre == pos_mnb:
            play_1 = False

        ver_x_gre += 5
        ver_y_gre += 5
        pos_gre = (ver_x_gre, ver_y_gre)
        for verification_droite in range(35):
            if pos_gre == pos_mnb:
                play_1 = False

            ver_y_gre -= 1
            pos_gre = (ver_x_gre, ver_y_gre)

        for verication_haut in range(35):
            if pos_gre == pos_mnb:
                play_1 = False

            ver_x_gre -= 1
            pos_gre = (ver_x_gre, ver_y_gre)

        for verification_gauche in range(35):
            if pos_gre == pos_mnb:
                play_1 = False

            ver_y_gre += 1
            pos_gre = (ver_x_gre, ver_y_gre)

        for verification_bas in range(35):
            if pos_gre == pos_mnb:
                play_1 = False

            ver_x_gre += 1
            pos_gre = (ver_x_gre, ver_y_gre)

        # grenouille 2
        ver_x_gre_2 = x_gre_2
        ver_y_gre_2 = y_gre_2
        pos_gre_2 = (ver_x_gre_2, ver_y_gre_2)
        ver_x_mnb = x_mnb
        ver_y_mnb = y_mnb
        pos_mnb = (ver_x_mnb, ver_y_mnb)

        if pos_gre_2 == pos_mnb:
            play_1 = False

        ver_x_gre_2 += 5
        ver_y_gre_2 += 5
        pos_gre_2 = (ver_x_gre_2, ver_y_gre_2)
        for verification_droite in range(35):
            if pos_gre_2 == pos_mnb:
                play_1 = False

            ver_y_gre_2 -= 1
            pos_gre_2 = (ver_x_gre_2, ver_y_gre_2)

        for verication_haut in range(35):
            if pos_gre_2 == pos_mnb:
                play_1 = False

            ver_x_gre_2 -= 1
            pos_gre_2 = (ver_x_gre_2, ver_y_gre_2)

        for verification_gauche in range(35):
            if pos_gre_2 == pos_mnb:
                play_1 = False

            ver_y_gre_2 += 1
            pos_gre_2 = (ver_x_gre_2, ver_y_gre_2)

        for verification_bas in range(35):
            if pos_gre_2 == pos_mnb:
                play_1 = False

            ver_x_gre_2 += 1
            pos_gre_2 = (ver_x_gre_2, ver_y_gre_2)

        # grenouille 3
        ver_x_gre_3 = x_gre_3
        ver_y_gre_3 = y_gre_3
        pos_gre_3 = (ver_x_gre_3, ver_y_gre_3)
        ver_x_mnb = x_mnb
        ver_y_mnb = y_mnb
        pos_mnb = (ver_x_mnb, ver_y_mnb)

        if pos_gre_3 == pos_mnb:
            play_1 = False

        ver_x_gre_3 += 5
        ver_y_gre_3 += 5
        pos_gre_3 = (ver_x_gre_3, ver_y_gre_3)
        for verification_droite in range(35):
            if pos_gre_3 == pos_mnb:
                play_1 = False

            ver_y_gre_3 -= 1
            pos_gre_3 = (ver_x_gre_3, ver_y_gre_3)

        for verication_haut in range(35):
            if pos_gre_3 == pos_mnb:
                play_1 = False

            ver_x_gre_3 -= 1
            pos_gre_3 = (ver_x_gre_3, ver_y_gre_3)

        for verification_gauche in range(35):
            if pos_gre_3 == pos_mnb:
                play_1 = False

            ver_y_gre_3 += 1
            pos_gre_3 = (ver_x_gre_3, ver_y_gre_3)

        for verification_bas in range(35):
            if pos_gre_3 == pos_mnb:
                play_1 = False

            ver_x_gre_3 += 1
            pos_gre_3 = (ver_x_gre_3, ver_y_gre_3)

        # affichage de la surfface jeu
        pygame.display.flip()

        # temporisation de début de partie
        if tempo == True:
            screen.blit(dec_3, (300, 300))
            pygame.display.flip()
            time.sleep(1)
            screen.blit(dec_2, (300, 300))
            pygame.display.flip()
            time.sleep(1)
            screen.blit(dec_1, (200, 225))
            pygame.display.flip()
            time.sleep(1)
            tempo = False

        # activation game over
        if play_1 == False:
            game_over_play_1 = True
            # récupérer le record
            chemin_donnees_pygamland = Path(
                r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\pygamland_1.json")
            with open(chemin_donnees_pygamland, "r") as fichier_ouvert:
                donnees_pygamland = json.load(fichier_ouvert)
                record_play_1 = donnees_pygamland["JEU 1"]["record"]
                aff_record_play_1 = str(record_play_1)

            # mettre à jour le record si il a été battu
            if score_final > record_play_1:
                donnees_pygamland["JEU 1"]["record"] = score_final
                with open(chemin_donnees_pygamland, "w") as fichier_ouvert:
                    json.dump(donnees_pygamland, fichier_ouvert,
                              indent=4, ensure_ascii=False)

                record_battu_1 = True

            screen.fill((0, 0, 0))
            screen.blit(menu_game_over_gre, (0, 0))
            if record_battu_1 == True:
                screen.blit(logo_nouveau_record_ima, (5, 100))
                pygame.display.flip()
                time.sleep(5)
            else:
                screen.blit(logo_game_over_point_exclamation, (190, 250))
                pygame.display.flip()
                time.sleep(2)

    # game over du jeu 1 (grenouille)
    if game_over_play_1 == True:
        # récupérer le record
        record_play_1_ima = pygame.image.load(
            r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\record_play_1.png")
        chemin_donnees_pygamland = Path(
            r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\pygamland_1.json")
        with open(chemin_donnees_pygamland, "r") as fichier_ouvert:
            donnees_pygamland = json.load(fichier_ouvert)
            record_play_1 = donnees_pygamland["JEU 1"]["record"]
            aff_record_play_1 = str(record_play_1)

        # mettre à jour le record si il a été battu
        if score_final > record_play_1:
            donnees_pygamland["JEU 1"]["record"] = score_final
            with open(chemin_donnees_pygamland, "w") as fichier_ouvert:
                json.dump(donnees_pygamland, fichier_ouvert,
                          indent=4, ensure_ascii=False)

            record_battu_1 = True

        # affichage
        screen.blit(menu_game_over_gre, (0, 0))
        screen.blit(logo_game_over, (200, 50))
        screen.blit(logo_retour_menu, (210, 455))
        screen.blit(logo_rejouer, (210, 615))

        screen.blit(cadre_du_score, (180, 240))
        screen.blit(logo_score, (190, 250))
        screen.blit(record_play_1_ima, (180, 335))

        # affichage score
        x_numero = 490
        for aff in affichage_score:
            numero = pygame.image.load(
                rf"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\{aff}.png").convert()
            screen.blit(numero, (x_numero, 265))
            x_numero += 25

        # affichage record
        x_numero_record = 490
        for aff in aff_record_play_1:
            numero = pygame.image.load(
                rf"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\{aff}.png").convert()
            screen.blit(numero, (x_numero, 360))
            x_numero += 25

        # vérification des options choisi ou pas
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_0] or pressed[pygame.K_KP0] or pressed[pygame.K_KP_0]:
            menu_1 = True
            play_1 = False
            game_over_play_1 = False

        if pressed[pygame.K_1] or pressed[pygame.K_KP1] or pressed[pygame.K_KP_1]:
            # réinitialisation des paramètres de la partie 1
            x_gre = 200
            y_gre = 150

            grenouille_2 = False
            x_gre_2 = 350
            y_gre_2 = 350

            grenouille_3 = False
            x_gre_3 = 350
            y_gre_3 = 350

            acceleration = True

            x_mnb = 600
            y_mnb = 150

            x_gauche_zone = 0
            x_droite_zone = 775
            y_haut_zone = 0
            y_bas_zone = 775

            tempo = True

            score = 0
            score_final = 0
            affichage_score = "0"
            numero = "0"
            record_battu_1 = False

            time_spawn_gre = 0

            map = pygame.image.load(
                r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\map.png").convert()

            play_1 = True
            game_over_play_1 = False

        pygame.display.flip()

    # JEU N° 2 (flappy bird)
    if play_2 == True:

        # déplacement bonhomme
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            y_bird -= 4
            perso_bird = pygame.image.load(
                r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\PERSO_bird_jeu_2.png").convert()
        else:
            y_bird += 2

            dec_tombe += 1
            if dec_tombe == 100:
                perso_bird = perso_bird_tombe
                dec_tombe = 0

        # déplacement sol et ciel
        # ciel
        tempo_ciel += 1
        if tempo_ciel == 5:
            x_ciel -= 1
            x_ciel_2 -= 1

            tempo_ciel = 0

            # boucler les allés des nuages
            if x_ciel_2 == 0:
                x_ciel = 0
                x_ciel_2 = 800

        # sol
        x_sol -= 1
        x_sol_2 -= 1

        if x_sol_2 == 0:
            x_sol = 0
            x_sol_2 = 800

        # Déplacement, creation aléatoire des tuyaux verts et hardification du niveau en retirant de l'esapce

        # hardification
        tempo_resserement_tuyau += 1
        if tempo_resserement_tuyau == 1000:
            if ecartement_tuyau > 250:
                ecartement_tuyau -= 5
                tempo_resserement_tuyau = 0
        if tempo_resserement_tuyau == 2000:
            vitesse_fois_2 = True

        # creation

        if tuyau_pas_encore_creer == True or x_tuyau_3 == 140:
            taille_tuyau_1 = random.randint(1, 3)
            taille_tuyau_2 = random.randint(1, 3)

            if taille_tuyau_1 == 1:
                tuyau_1 = tuyau_verts_T1
                y_tuyau_1 = y_tuyau_T1
            elif taille_tuyau_1 == 2:
                tuyau_1 = tuyau_verts_T2
                y_tuyau_1 = y_tuyau_T2
            elif taille_tuyau_1 == 3:
                tuyau_1 = tuyau_verts_T3
                y_tuyau_1 = y_tuyau_T3

            if taille_tuyau_2 == 1:
                tuyau_2 = tuyau_verts_T1
                y_tuyau_2 = y_tuyau_T1
            elif taille_tuyau_2 == 2:
                tuyau_2 = tuyau_verts_T2
                y_tuyau_2 = y_tuyau_T2
            elif taille_tuyau_2 == 3:
                tuyau_2 = tuyau_verts_T3
                y_tuyau_2 = y_tuyau_T3

            x_tuyau_1 = 800
            x_tuyau_2 = x_tuyau_1 + (ecartement_tuyau * 2)

            taille_tuyau_inverse_1 = random.randint(1, 3)
            taille_tuyau_inverse_2 = random.randint(1, 3)

            if taille_tuyau_inverse_1 == 1:
                tuyau_inverse_1 = tuyau_verts_inverse_T1
            elif taille_tuyau_inverse_1 == 2:
                tuyau_inverse_1 = tuyau_verts_inverse_T2
            elif taille_tuyau_inverse_1 == 3:
                tuyau_inverse_1 = tuyau_verts_inverse_T3

            if taille_tuyau_inverse_2 == 1:
                tuyau_inverse_2 = tuyau_verts_inverse_T1
            elif taille_tuyau_inverse_2 == 2:
                tuyau_inverse_2 = tuyau_verts_inverse_T2
            elif taille_tuyau_inverse_2 == 3:
                tuyau_inverse_2 = tuyau_verts_inverse_T3

            x_tuyau_inverse_1 = x_tuyau_1 + ecartement_tuyau
            x_tuyau_inverse_2 = x_tuyau_inverse_1 + (ecartement_tuyau * 2)

        if tuyau_pas_encore_creer == True or x_tuyau_3 == -200:
            taille_tuyau_3 = random.randint(1, 3)

            if taille_tuyau_3 == 1:
                tuyau_3 = tuyau_verts_T1
                y_tuyau_3 = y_tuyau_T1
            elif taille_tuyau_3 == 2:
                tuyau_3 = tuyau_verts_T2
                y_tuyau_3 = y_tuyau_T2
            elif taille_tuyau_3 == 3:
                tuyau_3 = tuyau_verts_T3
                y_tuyau_3 = y_tuyau_T3

            x_tuyau_3 = x_tuyau_1 + (ecartement_tuyau * 4)

        if tuyau_pas_encore_creer == True or x_tuyau_inverse_3 == -200:
            taille_tuyau_inverse_3 = random.randint(1, 3)

            if taille_tuyau_inverse_3 == 1:
                tuyau_inverse_3 = tuyau_verts_inverse_T1
            elif taille_tuyau_inverse_3 == 2:
                tuyau_inverse_3 = tuyau_verts_inverse_T2
            elif taille_tuyau_inverse_3 == 3:
                tuyau_inverse_3 = tuyau_verts_inverse_T3

            x_tuyau_inverse_3 = x_tuyau_inverse_1 + (ecartement_tuyau * 4)

            tuyau_pas_encore_creer = False

        # deplacement
        x_tuyau_1 -= 1
        x_tuyau_2 -= 1
        x_tuyau_3 -= 1
        x_tuyau_inverse_1 -= 1
        x_tuyau_inverse_2 -= 1
        x_tuyau_inverse_3 -= 1

        if vitesse_fois_2 == True:
            x_tuyau_1 -= 1
            x_tuyau_2 -= 1
            x_tuyau_3 -= 1
            x_tuyau_inverse_1 -= 1
            x_tuyau_inverse_2 -= 1
            x_tuyau_inverse_3 -= 1
            x_sol -= 1
            x_sol_2 -= 1
            x_ciel -= 1
            x_ciel_2 -= 1

        # verification que l'oiseau n'est pas touché le sol ou le ciel
        # ciel
        if y_bird < 10:
            y_bird += 100

        # sol
        if y_bird > 650:
            play_2 = False
            y_bird = 587

        # mise a jour de la surfface
        if tempo == True:
            perso_bird = pygame.image.load(
                r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\PERSO_bird_jeu_2.png").convert()
        screen.blit(map_jeu_2, (0, 0))
        screen.blit(perso_bird, (50, y_bird))
        screen.blit(tuyau_1, (x_tuyau_1, y_tuyau_1))
        screen.blit(tuyau_2, (x_tuyau_2, y_tuyau_2))
        screen.blit(tuyau_3, (x_tuyau_3, y_tuyau_3))
        screen.blit(ciel_jeu_2, (x_ciel, -100))
        screen.blit(ciel_jeu_2, (x_ciel_2, -100))
        screen.blit(tuyau_inverse_1, (x_tuyau_inverse_1, 0))
        screen.blit(tuyau_inverse_2, (x_tuyau_inverse_2, 0))
        screen.blit(tuyau_inverse_3, (x_tuyau_inverse_3, 0))
        screen.blit(sol, (x_sol, 725))
        screen.blit(sol, (x_sol_2, 725))
        screen.blit(cadre_du_score, (360, 648))
        screen.blit(logo_score, (370, 658))

        # gestion du score

        if x_tuyau_1 == 20 or x_tuyau_2 == 20 or x_tuyau_3 == 20 or x_tuyau_inverse_1 == 20 or x_tuyau_inverse_2 == 20 or x_tuyau_inverse_3 == 20:
            score_jeu_2 += 1

        score_2_str = str(score_jeu_2)
        x_numero_score_2 = 655

        for aff in score_2_str:
            numero = pygame.image.load(
                rf"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\{aff}.png").convert()
            screen.blit(numero, (x_numero_score_2, 673))
            x_numero_score_2 += 25

        # affichage du jeu 2
        pygame.display.flip()

        # collision tuyau verts
        ver_x_tuyau_1 = x_tuyau_1 - 100
        ver_x_tuyau_2 = x_tuyau_2 - 100
        ver_x_tuyau_3 = x_tuyau_3 - 100
        ver_y_tuyau_1 = y_tuyau_1 - 120
        ver_y_tuyau_2 = y_tuyau_2 - 120
        ver_y_tuyau_3 = y_tuyau_3 - 120
        ver_x_tuyau_inverse_1 = x_tuyau_inverse_1 - 120
        ver_x_tuyau_inverse_2 = x_tuyau_inverse_2 - 120
        ver_x_tuyau_inverse_3 = x_tuyau_inverse_3 - 120
        ver_y_tuyau_inverse_1 = 0
        ver_y_tuyau_inverse_2 = 0
        ver_y_tuyau_inverse_3 = 0

        pos_tuyau_1 = (ver_x_tuyau_1, ver_y_tuyau_1)
        pos_tuyau_2 = (ver_x_tuyau_2, ver_y_tuyau_2)
        pos_tuyau_3 = (ver_x_tuyau_3, ver_y_tuyau_3)
        pos_tuyau_inverse_1 = (ver_x_tuyau_inverse_1, ver_y_tuyau_inverse_1)
        pos_tuyau_inverse_2 = (ver_x_tuyau_inverse_2, ver_y_tuyau_inverse_2)
        pos_tuyau_inverse_3 = (ver_x_tuyau_inverse_3, ver_y_tuyau_inverse_3)

        ver_x_bird = 50
        ver_y_bird = y_bird
        pos_bird = (ver_x_bird, ver_y_bird)

        # verif tuyau 1
        if tuyau_1 == tuyau_verts_T1:
            for verification_2 in range(390):
                if pos_bird == pos_tuyau_1:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_2 <= 280:
                    ver_y_tuyau_1 += 1
                    pos_tuyau_1 = (ver_x_tuyau_1, ver_y_tuyau_1)
                    if verification_2 == 280:
                        ver_y_tuyau_1 -= 280

                if verification_2 > 280:
                    ver_x_tuyau_1 += 1
                    pos_tuyau_1 = (ver_x_tuyau_1, ver_y_tuyau_1)

        elif tuyau_1 == tuyau_verts_T2:
            for verification_2 in range(410):
                if pos_bird == pos_tuyau_1:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_2 <= 300:
                    ver_y_tuyau_1 += 1
                    pos_tuyau_1 = (ver_x_tuyau_1, ver_y_tuyau_1)
                    if verification_2 == 300:
                        ver_y_tuyau_1 -= 300

                if verification_2 > 300:
                    ver_x_tuyau_1 += 1
                    pos_tuyau_1 = (ver_x_tuyau_1, ver_y_tuyau_1)

        elif tuyau_1 == tuyau_verts_T3:
            for verification_2 in range(420):
                if pos_bird == pos_tuyau_1:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_2 <= 310:
                    ver_y_tuyau_1 += 1
                    pos_tuyau_1 = (ver_x_tuyau_1, ver_y_tuyau_1)
                    if verification_2 == 310:
                        ver_y_tuyau_1 -= 310

                if verification_2 > 310:
                    ver_x_tuyau_1 += 1
                    pos_tuyau_1 = (ver_x_tuyau_1, ver_y_tuyau_1)

        # verif tuyau 2
        if tuyau_2 == tuyau_verts_T1:
            for verification_3 in range(390):
                if pos_bird == pos_tuyau_2:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_3 <= 280:
                    ver_y_tuyau_2 += 1
                    pos_tuyau_2 = (ver_x_tuyau_2, ver_y_tuyau_2)
                    if verification_3 == 280:
                        ver_y_tuyau_2 -= 280

                if verification_3 > 280:
                    ver_x_tuyau_2 += 1
                    pos_tuyau_2 = (ver_x_tuyau_2, ver_y_tuyau_2)

        elif tuyau_2 == tuyau_verts_T2:
            for verification_3 in range(410):
                if pos_bird == pos_tuyau_2:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_3 <= 300:
                    ver_y_tuyau_2 += 1
                    pos_tuyau_2 = (ver_x_tuyau_2, ver_y_tuyau_2)
                    if verification_3 == 300:
                        ver_y_tuyau_2 -= 300

                if verification_3 > 300:
                    ver_x_tuyau_2 += 1
                    pos_tuyau_2 = (ver_x_tuyau_2, ver_y_tuyau_2)

        elif tuyau_2 == tuyau_verts_T3:
            for verification_3 in range(430):
                if pos_bird == pos_tuyau_2:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_3 <= 320:
                    ver_y_tuyau_2 += 1
                    pos_tuyau_2 = (ver_x_tuyau_2, ver_y_tuyau_2)
                    if verification_3 == 320:
                        ver_y_tuyau_2 -= 320

                if verification_3 > 320:
                    ver_x_tuyau_2 += 1
                    pos_tuyau_2 = (ver_x_tuyau_2, ver_y_tuyau_2)

        # verif tuyau 3
        if tuyau_3 == tuyau_verts_T1:
            for verification_4 in range(390):
                if pos_bird == pos_tuyau_3:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_4 <= 280:
                    ver_y_tuyau_3 += 1
                    pos_tuyau_3 = (ver_x_tuyau_3, ver_y_tuyau_3)
                    if verification_4 == 280:
                        ver_y_tuyau_3 -= 280

                if verification_4 > 280:
                    ver_x_tuyau_3 += 1
                    pos_tuyau_3 = (ver_x_tuyau_3, ver_y_tuyau_3)

        elif tuyau_3 == tuyau_verts_T2:
            for verification_4 in range(410):
                if pos_bird == pos_tuyau_3:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_4 <= 300:
                    ver_y_tuyau_3 += 1
                    pos_tuyau_3 = (ver_x_tuyau_3, ver_y_tuyau_3)
                    if verification_4 == 300:
                        ver_y_tuyau_3 -= 300

                if verification_4 > 300:
                    ver_x_tuyau_3 += 1
                    pos_tuyau_3 = (ver_x_tuyau_3, ver_y_tuyau_3)

        elif tuyau_3 == tuyau_verts_T3:
            for verification_4 in range(420):
                if pos_bird == pos_tuyau_3:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_4 <= 310:
                    ver_y_tuyau_3 += 1
                    pos_tuyau_3 = (ver_x_tuyau_3, ver_y_tuyau_3)
                    if verification_4 == 320:
                        ver_y_tuyau_3 -= 320

                if verification_4 > 310:
                    ver_x_tuyau_3 += 1
                    pos_tuyau_3 = (ver_x_tuyau_3, ver_y_tuyau_3)

        # verif tuyau inverse 1
        if tuyau_inverse_1 == tuyau_verts_inverse_T1:
            for verification_5 in range(390):
                if pos_bird == pos_tuyau_inverse_1:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_5 <= 280:
                    ver_y_tuyau_inverse_1 += 1
                    pos_tuyau_inverse_1 = (
                        ver_x_tuyau_inverse_1, ver_y_tuyau_inverse_1)

                if verification_5 > 280:
                    ver_x_tuyau_inverse_1 += 1
                    pos_tuyau_inverse_1 = (
                        ver_x_tuyau_inverse_1, ver_y_tuyau_inverse_1)

        elif tuyau_inverse_1 == tuyau_verts_inverse_T2:
            for verification_5 in range(410):
                if pos_bird == pos_tuyau_inverse_1:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_5 <= 300:
                    ver_y_tuyau_inverse_1 += 1
                    pos_tuyau_inverse_1 = (
                        ver_x_tuyau_inverse_1, ver_y_tuyau_inverse_1)

                if verification_5 > 300:
                    ver_x_tuyau_inverse_1 += 1
                    pos_tuyau_inverse_1 = (
                        ver_x_tuyau_inverse_1, ver_y_tuyau_inverse_1)

        elif tuyau_inverse_1 == tuyau_verts_inverse_T3:
            for verification_5 in range(420):
                if pos_bird == pos_tuyau_inverse_1:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_5 <= 310:
                    ver_y_tuyau_inverse_1 += 1
                    pos_tuyau_inverse_1 = (
                        ver_x_tuyau_inverse_1, ver_y_tuyau_inverse_1)

                if verification_5 > 310:
                    ver_x_tuyau_inverse_1 += 1
                    pos_tuyau_inverse_1 = (
                        ver_x_tuyau_inverse_1, ver_y_tuyau_inverse_1)

        # verif tuyau inverse 2
        if tuyau_inverse_2 == tuyau_verts_inverse_T1:
            for verification_6 in range(390):
                if pos_bird == pos_tuyau_inverse_2:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_6 <= 280:
                    ver_y_tuyau_inverse_2 += 1
                    pos_tuyau_inverse_2 = (
                        ver_x_tuyau_inverse_2, ver_y_tuyau_inverse_2)

                if verification_6 > 280:
                    ver_x_tuyau_inverse_2 += 1
                    pos_tuyau_inverse_2 = (
                        ver_x_tuyau_inverse_2, ver_y_tuyau_inverse_2)

        elif tuyau_inverse_2 == tuyau_verts_inverse_T2:
            for verification_6 in range(410):
                if pos_bird == pos_tuyau_inverse_2:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_6 <= 300:
                    ver_y_tuyau_inverse_2 += 1
                    pos_tuyau_inverse_2 = (
                        ver_x_tuyau_inverse_2, ver_y_tuyau_inverse_2)

                if verification_6 > 300:
                    ver_x_tuyau_inverse_2 += 1
                    pos_tuyau_inverse_2 = (
                        ver_x_tuyau_inverse_2, ver_y_tuyau_inverse_2)

        elif tuyau_inverse_2 == tuyau_verts_inverse_T3:
            for verification_6 in range(420):
                if pos_bird == pos_tuyau_inverse_2:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_6 <= 310:
                    ver_y_tuyau_inverse_2 += 1
                    pos_tuyau_inverse_2 = (
                        ver_x_tuyau_inverse_2, ver_y_tuyau_inverse_2)

                if verification_6 > 310:
                    ver_x_tuyau_inverse_2 += 1
                    pos_tuyau_inverse_2 = (
                        ver_x_tuyau_inverse_2, ver_y_tuyau_inverse_2)

        # verif tuyau inverse 3
        if tuyau_inverse_3 == tuyau_verts_inverse_T1:
            for verification_7 in range(390):
                if pos_bird == pos_tuyau_inverse_3:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_7 <= 280:
                    ver_y_tuyau_inverse_3 += 1
                    pos_tuyau_inverse_3 = (
                        ver_x_tuyau_inverse_3, ver_y_tuyau_inverse_3)

                if verification_7 > 280:
                    ver_x_tuyau_inverse_3 += 1
                    pos_tuyau_inverse_3 = (
                        ver_x_tuyau_inverse_3, ver_y_tuyau_inverse_3)

        elif tuyau_inverse_3 == tuyau_verts_inverse_T2:
            for verification_7 in range(410):
                if pos_bird == pos_tuyau_inverse_3:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_7 <= 300:
                    ver_y_tuyau_inverse_3 += 1
                    pos_tuyau_inverse_3 = (
                        ver_x_tuyau_inverse_3, ver_y_tuyau_inverse_3)

                if verification_7 > 300:
                    ver_x_tuyau_inverse_3 += 1
                    pos_tuyau_inverse_3 = (
                        ver_x_tuyau_inverse_3, ver_y_tuyau_inverse_3)

        elif tuyau_inverse_3 == tuyau_verts_inverse_T3:
            for verification_7 in range(420):
                if pos_bird == pos_tuyau_inverse_3:
                    play_2 = False
                    animation_bird_tombe = True

                if verification_7 <= 310:
                    ver_y_tuyau_inverse_3 += 1
                    pos_tuyau_inverse_3 = (
                        ver_x_tuyau_inverse_3, ver_y_tuyau_inverse_3)

                if verification_7 > 310:
                    ver_x_tuyau_inverse_3 += 1
                    pos_tuyau_inverse_3 = (
                        ver_x_tuyau_inverse_3, ver_y_tuyau_inverse_3)

        # temporisation de début de partie
        if tempo == True:
            screen.blit(dec_3_jeu_2, (300, 300))
            pygame.display.flip()
            time.sleep(1)
            screen.blit(dec_2_jeu_2, (300, 300))
            pygame.display.flip()
            time.sleep(1)
            screen.blit(dec_1_jeu_2, (260, 285))
            pygame.display.flip()
            time.sleep(1)
            tempo = False

        # animation bird qui tombe
        if animation_bird_tombe == True:

            perso_bird = perso_bird_tombe
            hauteur_tombe_bird = 725 - y_bird - 50
            for i in range(hauteur_tombe_bird):
                y_bird += 1
                screen.blit(map_jeu_2, (0, 0))
                screen.blit(perso_bird, (50, y_bird))
                screen.blit(tuyau_1, (x_tuyau_1, y_tuyau_1))
                screen.blit(tuyau_2, (x_tuyau_2, y_tuyau_2))
                screen.blit(tuyau_3, (x_tuyau_3, y_tuyau_3))
                screen.blit(ciel_jeu_2, (x_ciel, -100))
                screen.blit(ciel_jeu_2, (x_ciel_2, -100))
                screen.blit(tuyau_inverse_1, (x_tuyau_inverse_1, 0))
                screen.blit(tuyau_inverse_2, (x_tuyau_inverse_2, 0))
                screen.blit(tuyau_inverse_3, (x_tuyau_inverse_3, 0))
                screen.blit(sol, (x_sol, 725))
                screen.blit(sol, (x_sol_2, 725))
                screen.blit(cadre_du_score, (360, 648))
                screen.blit(logo_score, (370, 658))

                pygame.display.flip()

            time.sleep(1)

        # verification si game over est activé
        if play_2 == False:
            game_over_play_2 = True
            # récupéré le record et verification pour voir si le record a été battu
            chemin_donnees_pygamland = Path(
                r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\pygamland_1.json")
            with open(chemin_donnees_pygamland, "r") as fichier_open:
                fichier_load = json.load(fichier_open)
                record_jeu_2 = fichier_load["JEU_2"]["record"]
                if score_jeu_2 > record_jeu_2:
                    print(score_jeu_2, record_jeu_2)
                    record_battu_2 = True
                    fichier_load["JEU_2"]["record"] = score_jeu_2
                    with open(chemin_donnees_pygamland, "w") as fichier_open:
                        json.dump(fichier_load, fichier_open,
                                  indent=4, ensure_ascii=False)

            # affichage game over
            screen.fill((0, 0, 0))
            screen.blit(menu_game_over_gre, (0, 0))
            if record_battu_2 == True:
                screen.blit(logo_nouveau_record_ima, (5, 100))
                pygame.display.flip()
                time.sleep(5)
            else:
                screen.blit(logo_game_over_point_exclamation, (190, 250))
                pygame.display.flip()
                time.sleep(2)

    # game over jeu 2 (flappy bird)
    if game_over_play_2 == True:
        # affichage
        screen.blit(menu_game_over_gre, (0, 0))
        screen.blit(logo_game_over, (200, 50))
        screen.blit(logo_retour_menu, (210, 455))
        screen.blit(logo_rejouer, (210, 615))

        screen.blit(cadre_du_score, (180, 240))
        screen.blit(logo_score, (190, 250))
        screen.blit(record_play_1_ima, (180, 335))

        # affichage score
        affichage_score = str(score_jeu_2)
        x_numero = 490
        for aff in affichage_score:
            numero = pygame.image.load(
                rf"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\{aff}.png").convert()
            screen.blit(numero, (x_numero, 265))
            x_numero += 25

        # affichage record
        aff_record_play_2 = str(record_jeu_2)
        x_numero_record = 490
        for aff in aff_record_play_2:
            numero = pygame.image.load(
                rf"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\{aff}.png").convert()
            screen.blit(numero, (x_numero, 360))
            x_numero += 25

        # vérification des options choisi ou pas
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_0] or pressed[pygame.K_KP0] or pressed[pygame.K_KP_0]:
            menu_1 = True
            play_2 = False
            game_over_play_2 = False

        if pressed[pygame.K_1] or pressed[pygame.K_KP1] or pressed[pygame.K_KP_1]:
            # réinitialisation des paramètres de la partie 2
            tempo = True

            perso_bird = pygame.image.load(
                r"C:\Users\boris\pytonJEU\fichierspycréés\projetsfinis\pygamland_1\PERSO_bird_jeu_2.png").convert()
            y_bird = 300
            dec_tombe = 0

            x_ciel = 0
            x_ciel_2 = x_ciel + 800

            x_sol = 0
            x_sol_2 = x_sol + 800

            tuyau_pas_encore_creer = True
            tempo_resserement_tuyau = 0
            ecartement_tuyau = 300

            x_tuyau = 700
            x_tuyau_2 = x_tuyau + (ecartement_tuyau * 2)
            x_tuyau_3 = x_tuyau + (ecartement_tuyau * 4)
            y_tuyau = 0
            y_tuyau_2 = 0
            y_tuyau_3 = 0

            x_tuyau_inverse_1 = x_tuyau_1 + ecartement_tuyau
            x_tuyau_inverse_1 = x_tuyau_inverse_1 + (ecartement_tuyau * 2)
            x_tuyau_inverse_1 = x_tuyau_inverse_1 + (ecartement_tuyau * 4)

            animation_bird_tombe = False

            vitesse_fois_2 = False

            score_jeu_2 = 0

            game_over_play_2 = False
            record_battu_2 = False

            # rejouer
            play_2 = True
            game_over_play_2 = False

        # affichage de la surfface menu
    pygame.display.flip()

    # Regle la vitesse de la boucle
    clock.tick(175)

pygame.quit()
