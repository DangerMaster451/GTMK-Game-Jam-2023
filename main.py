import pygame
from sys import exit

# Basic Setup
pygame.init()
DEFAULT_RESOLUTION = (1280, 720)
screen = pygame.display.set_mode(DEFAULT_RESOLUTION, pygame.RESIZABLE | pygame.SCALED)
pygame.display.set_caption("Shopkeeper")
clock = pygame.time.Clock()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((94,129,162))
    pygame.display.flip()
    clock.tick(60)