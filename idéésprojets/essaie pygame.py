import pygame
import time


pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("dino")

image_1 = pygame.image.load(
    "vector-illustration-cartoon-dinosaur-pixel-260nw-1029931234.webp").convert()


x = 5
y = 50

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x -= 1

    if pressed[pygame.K_RIGHT]:
        x += 1

    if pressed[pygame.K_UP]:
        y -= 1

    if pressed[pygame.K_DOWN]:
        y += 1

    screen.fill((0, 0, 0))

    screen.blit(image_1, (x, y))
    pygame.display.flip()

    clock.tick(250)

pygame.quit()
