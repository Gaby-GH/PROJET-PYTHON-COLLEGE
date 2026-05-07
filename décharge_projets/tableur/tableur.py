import pygame
from pathlib import Path

pygame.init()

screen = pygame.display.set_mode((1920, 1020))

tableau_img = pygame.image.load(r"C:\Users\boris\pytonJEU\tableur\tableau.png")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(tableau_img, (0, 0))

    pygame.display.flip()

pygame.quit()
