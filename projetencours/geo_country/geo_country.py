import pygame
from pathlib import Path
import json
import time
import random

# MDP shift heroes : Yg3dyd

# initialisation et tout le reste
pygame.init()
screen = pygame.display.set_mode((1280, 896))
pygame.display.set_caption("GEO COUNTRY")

# recuperer les donnees json
chemin_database = Path(r"geo_country.json")

if not chemin_database.exists():
    DATABASE_init = {"world record": 0}
    with open(chemin_database, "w") as fichier_ouvert:
        json.dump(DATABASE_init, fichier_ouvert, ensure_ascii=False, indent=4)

with open(chemin_database, "r") as fichier_ouvert:
    DATABASE = json.load(fichier_ouvert)

# gerer le tempo
clock = pygame.time.Clock()

# background
background_jour = pygame.image.load(r"fond_jour.png").convert_alpha()
background_nuit = pygame.image.load(r"fond_nuit.png").convert_alpha()
background = background_jour
time_jour_nuit = 0

# panneau des scores
panneau_des_scores_jour = pygame.image.load(
    r"panneaux_score.png").convert_alpha()
panneau_des_scores_nuit = pygame.image.load(
    r"panneaux_score_nuit.png").convert_alpha()
panneau_des_scores = panneau_des_scores_jour
panneau_game_over = pygame.image.load(r"panneau_game_over.png").convert_alpha()
panneau_world_record = pygame.image.load(
    r"panneau_world_record.png").convert_alpha()
score = 0

# ENVIRONNEMENT
# sol
sol = pygame.image.load(r"sol.png").convert_alpha()
x_sol_1 = 0
x_sol_2 = 1255
x_sol_3 = 2511

# ferme
ferme_jour = pygame.image.load(r"ferme_jour.png").convert_alpha()
ferme_nuit = pygame.image.load(r"ferme_nuit.png").convert_alpha()
ferme = ferme_jour
x_ferme = 20

# soleil et lune

soleil = pygame.image.load(r"soleil.png").convert_alpha()
lune = pygame.image.load(r"lune.png").convert_alpha()
soleil_ou_lune = soleil
x_soleil_lune = 900

# nuages
nuage_1_nuit = pygame.image.load(r"nuage_1_nuit.png").convert_alpha()
nuage_1_jour = pygame.image.load(r"nuage_1_jour.png").convert_alpha()
nuage_1 = nuage_1_jour

nuage_2_nuit = pygame.image.load(r"nuage_2_nuit.png").convert_alpha()
nuage_2_jour = pygame.image.load(r"nuage_2_jour.png").convert_alpha()
nuage_2 = nuage_2_jour

nuage_3_nuit = pygame.image.load(r"nuage_3_nuit.png").convert_alpha()
nuage_3_jour = pygame.image.load(r"nuage_3_jour.png").convert_alpha()
nuage_3 = nuage_3_jour

x_nuage = 1280
y_nuage = 300

nuage = False
tempo_nuage = 0

# PERSOS
# perso principal
perso = pygame.image.load(r"jacky.png").convert_alpha()
y_perso = 643
x_perso = 400

descente = False
pixel_jumper = 0
jump = False
double_jump = False
relacher_pour_pas_tricher = False

# MONSTRES ET OBSTACLES
# monstre
# zombies
zombie_niv_1 = pygame.image.load(r"monstre_1.png").convert_alpha()

# fantomes
fantome_niv_1 = pygame.image.load(r"monstre_2.png").convert_alpha()
boule_de_feu_jour = pygame.image.load(r"boule_de_feu_jour.png").convert_alpha()
boule_de_feu_nuit = pygame.image.load(r"boule_de_feu_nuit.png").convert_alpha()
boule_de_feu = boule_de_feu_jour
x_boule_de_feu = 0
y_boule_de_feu = 0

# cochon canon
cochon_canon_nuit = pygame.image.load(r"cochon_canon_nuit.png").convert_alpha()
cochon_canon_jour = pygame.image.load(r"cochon_canon_jour.png").convert_alpha()
cochon_canon = cochon_canon_jour

missile_mortier = pygame.image.load(r"missile_mortier.png").convert_alpha()
x_missile_mortier = 0
y_missile_mortier = 0
descente_missile_mortier = False

# nyan cat
nyan_cat_jour = pygame.image.load(r"nyan_cat_jour.png").convert_alpha()
nyan_cat_nuit = pygame.image.load(r"nyan_cat_nuit.png").convert_alpha()
nyan_cat = nyan_cat_jour
monter_nyan = False

# obstacles
# cactus
cactus = pygame.image.load(r"cactus.png").convert_alpha()

nbr_de_monstre = 5
tempo_spawn_monstre = 0
monstre_spawn = 0
vitesse_de_spawn = 1
liste_type_monstre = []


# LOGOS
logo_touche_pour_jouer = pygame.image.load(
    r"logo_touche_entree_pour_jouer.png").convert_alpha()

play = True
menu = True
game = False
game_over = False

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    pressed = pygame.key.get_pressed()

    # ACTION DANS MENU
    if menu == True:
        # verifier si lancer partie et reinitialiser les données de la partie
        if pressed[pygame.K_RETURN]:
            x_sol_1 = 0
            x_sol_2 = 1255
            x_sol_3 = 2511

            tempo_spawn_monstre = 0
            monstre_spawn = 0
            vitesse_de_spawn = 1
            liste_type_monstre = []

            score = 0

            game = True
            menu = False

        x_ferme = 20
        y_perso = 643

    # ACTION DANS GAME
    elif game == True:
        # deco qui s'en va
        x_ferme -= 1

        # ACTIONS du perso
        # jump ?
        if jump == False and double_jump == False and descente == False and pressed[pygame.K_SPACE]:
            jump = True

        # pendant le jump
        if jump == True:
            if not pressed[pygame.K_SPACE]:
                relacher_pour_pas_tricher = True

            y_perso -= 4
            pixel_jumper += 4

            if pixel_jumper > 150 and pixel_jumper < 250:
                y_perso += 3

                # regarder si double jump ?
                if pressed[pygame.K_SPACE] and relacher_pour_pas_tricher == True:
                    pixel_jumper = 0
                    double_jump = True
                    jump = False

            elif pixel_jumper > 250:
                descente = True
                jump = False

        # pendant double jump
        if double_jump == True:
            y_perso -= 4
            pixel_jumper += 4

            if pixel_jumper > 150 and pixel_jumper < 250:
                y_perso += 3

            elif pixel_jumper > 250:
                descente = True
                double_jump = False
                relacher_pour_pas_tricher = False

        # pendant la descente
        elif descente == True:
            y_perso += 1
            pixel_jumper -= 1

            if pixel_jumper < 200:
                y_perso += 1

            if y_perso >= 643:
                y_perso = 643
                pixel_jumper = 0
                descente = False

        # gerer le mouvement du sol
        x_sol_1 -= 1
        x_sol_2 -= 1
        x_sol_3 -= 1

        if x_sol_1 == -1255:
            x_sol_1 = 2511

        elif x_sol_2 == -1255:
            x_sol_2 = 2511

        elif x_sol_3 == -1255:
            x_sol_3 = 2511

        # GERER APPARITION MONSTRE MOUVEMENT ET COLISION
        tempo_spawn_monstre += vitesse_de_spawn
        if tempo_spawn_monstre >= 800:
            # intensifier le spawnage de monstre
            monstre_spawn += 1
            if monstre_spawn == 25:
                vitesse_de_spawn += 1

            # faire spawner un monstre aléatoirement en l'ajoutant a la liste des monstres
            random_monstre = random.randint(1, nbr_de_monstre)
            liste_type_monstre.append([random_monstre, 1600, 643, False])

            tempo_spawn_monstre = 0

    elif game_over == True:
        if score <= DATABASE["world record"]:
            screen.blit(panneau_game_over, (300, 250))
            x_score = 540
            for o in str(score):
                chiffre = pygame.image.load(rf"nbr_{o}.png").convert_alpha()
                screen.blit(chiffre, (x_score, 537))
                x_score += 16
            pygame.display.flip()
            time.sleep(3)

        else:
            screen.blit(panneau_world_record, (300, 250))
            x_score = 540
            for o in str(score):
                chiffre = pygame.image.load(rf"nbr_{o}.png").convert_alpha()
                screen.blit(chiffre, (x_score, 537))
                x_score += 16
            DATABASE["world record"] = score
            pygame.display.flip()
            time.sleep(6)

        game_over = False
        menu = True

    # GERER LE FOND (nuit ou jour)
    time_jour_nuit += 1

    if time_jour_nuit == 20000:
        if background == background_jour:
            soleil_ou_lune = lune
            ferme = ferme_nuit
            background = background_nuit
            boule_de_feu = boule_de_feu_nuit
            nuage_1 = nuage_1_nuit
            nuage_2 = nuage_2_nuit
            nuage_3 = nuage_3_nuit
            cochon_canon = cochon_canon_nuit
            nyan_cat = nyan_cat_nuit
            panneau_des_scores = panneau_des_scores_nuit
        elif background == background_nuit:
            soleil_ou_lune = soleil
            ferme = ferme_jour
            background = background_jour
            boule_de_feu = boule_de_feu_jour
            nuage_1 = nuage_1_jour
            nuage_2 = nuage_2_jour
            nuage_3 = nuage_3_jour
            cochon_canon = cochon_canon_jour
            nyan_cat = nyan_cat_jour
            panneau_des_scores = panneau_des_scores_jour

        time_jour_nuit = 0

    # GERER LES AFFICHAGES
    # le fond
    screen.blit(background, (0, 0))

    # panneaux des scores
    screen.blit(panneau_des_scores, (15, 15))

    x_score = 55
    for o in str(score):
        if background == background_jour:
            chiffre = pygame.image.load(rf"nbr_{o}.png").convert_alpha()
        else:
            chiffre = pygame.image.load(rf"nbr_{o}_nuit.png").convert_alpha()
        screen.blit(chiffre, (x_score, 60))
        x_score += 16

    x_record = 190
    for c in str(DATABASE["world record"]):
        if background == background_jour:
            chiffre = pygame.image.load(rf"nbr_{c}.png").convert_alpha()
        else:
            chiffre = pygame.image.load(rf"nbr_{c}_nuit.png").convert_alpha()
        screen.blit(chiffre, (x_record, 60))
        x_record += 16

    # soleil et lune
    screen.blit(soleil_ou_lune, (x_soleil_lune, 150))
    x_soleil_lune -= 0.002
    if x_soleil_lune < -98:
        x_soleil_lune = 1380

    # nuages
    if nuage == False:
        tempo_nuage += 1
        if tempo_nuage == 12000:
            nuage = True
    elif nuage == True:
        x_nuage -= 0.1
        screen.blit(nuage_1, (x_nuage, y_nuage))
        screen.blit(nuage_2, (x_nuage + 120, y_nuage + 15))
        screen.blit(nuage_3, (x_nuage + 300, y_nuage))

        if x_nuage < -600:
            tempo_nuage = 0
            nuage = False

    # deco qui s'en va
    if x_ferme > -1000:
        screen.blit(ferme, (x_ferme, 191))

    # affichage quand menu
    if menu == True:
        screen.blit(sol, (12, 691))
        screen.blit(logo_touche_pour_jouer, (630, 760))
        screen.blit(perso, (x_perso, y_perso))

    elif game == True:
        screen.blit(sol, (x_sol_1, 691))
        screen.blit(sol, (x_sol_2, 691))
        screen.blit(sol, (x_sol_3, 691))

        screen.blit(perso, (x_perso, y_perso))

        # boucler sur la liste des monstres pour les afficher et colision
        for i in liste_type_monstre:
            if i[0] == 1:
                i[1] -= 2
                screen.blit(zombie_niv_1, (i[1], 643))

                if zombie_niv_1.get_rect(x=i[1], y=i[2]).colliderect(perso.get_rect(x=x_perso, y=y_perso)):
                    game_over = True
                    game = False

            elif i[0] == 2:
                i[1] -= 2
                screen.blit(fantome_niv_1, (i[1], 643))

                if fantome_niv_1.get_rect(x=i[1], y=i[2]).colliderect(perso.get_rect(x=x_perso, y=y_perso)):
                    game_over = True
                    game = False

                if i[3] == False:
                    x_boule_de_feu = i[1] - 36
                    y_boule_de_feu = 655

                if i[1] < 1200:
                    i[3] = True
                    screen.blit(boule_de_feu, (x_boule_de_feu, y_boule_de_feu))
                    x_boule_de_feu -= 3

                    if boule_de_feu.get_rect(x=x_boule_de_feu, y=y_boule_de_feu).colliderect(perso.get_rect(x=x_perso, y=y_perso)):
                        game_over = True
                        game = False

                    if x_boule_de_feu < 100:
                        i[3] = False

            elif i[0] == 3:
                i[1] -= 1
                screen.blit(cactus, (i[1], 600))

                if cactus.get_rect(x=i[1], y=619).colliderect(perso.get_rect(x=x_perso, y=y_perso)):
                    game_over = True
                    game = False

            elif i[0] == 4:
                i[1] -= 2
                screen.blit(cochon_canon, (i[1], 643))

                if cochon_canon.get_rect(x=i[1], y=643).colliderect(perso.get_rect(x=x_perso, y=y_perso)):
                    game_over = True
                    game = False

                if i[3] == False:
                    x_missile_mortier = i[1] + 12
                    y_missile_mortier = 667
                    descente_missile_mortier = False

                if i[1] < 1100:
                    screen.blit(missile_mortier,
                                (x_missile_mortier, y_missile_mortier))

                    x_missile_mortier -= 2.5
                    if y_missile_mortier >= 275 and descente_missile_mortier == False:
                        y_missile_mortier -= 4

                    if y_missile_mortier < 275 and descente_missile_mortier == False:
                        y_missile_mortier -= 2

                    if y_missile_mortier < 150:
                        descente_missile_mortier = True
                    if descente_missile_mortier == True:
                        y_missile_mortier += 3

                    if missile_mortier.get_rect(x=x_missile_mortier, y=y_missile_mortier).colliderect(perso.get_rect(x=x_perso, y=y_perso)):
                        game_over = True
                        game = False

                    i[3] = True

                    if y_missile_mortier > 664:

                        y_missile_mortier -= 3
                        x_missile_mortier += 1.5

            elif i[0] == 5:
                i[1] -= 0.5

                if i[3] == False:
                    i[2] = 300
                    monter_nyan = True
                    i[3] = True

                if monter_nyan == True:
                    i[2] -= 1
                    if i[2] <= 100:
                        monter_nyan = False
                else:
                    i[2] += 1
                    if i[2] >= 400:
                        monter_nyan = True

                screen.blit(nyan_cat, (i[1], i[2]))

                if nyan_cat.get_rect(x=i[1], y=i[2]).colliderect(perso.get_rect(x=x_perso, y=y_perso)):
                    game_over = True
                    game = False

            if i[1] <= -300:
                score += 1
                liste_type_monstre.remove(i)

    pygame.display.flip()

    clock.tick(170)

with open(chemin_database, "w") as fichier_ouvert:
    json.dump(DATABASE, fichier_ouvert, ensure_ascii=False, indent=4)
