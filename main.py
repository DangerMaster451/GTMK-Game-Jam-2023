import pygame
from sys import exit

from player import Player

# Basic Setup
pygame.init()
DEFAULT_RESOLUTION = (1280, 720)
screen = pygame.display.set_mode(DEFAULT_RESOLUTION, pygame.RESIZABLE | pygame.SCALED)
pygame.display.set_caption("Shopkeeper")
clock = pygame.time.Clock()

# Create Objects
player = Player(screen)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((94,129,162))

    # Render Sprites
    player.update()

    pygame.display.flip()
    clock.tick(60)