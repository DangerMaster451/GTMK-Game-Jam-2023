import pygame
from sys import exit

from player import Player
from dialog_box import Dialog_Box
from grid import Grid
from side_bar import orderBar, sideBar

# Basic Setup
pygame.init()
DEFAULT_RESOLUTION = (1280, 720)
window = pygame.display.set_mode(DEFAULT_RESOLUTION, pygame.RESIZABLE | pygame.SCALED)
game_display = pygame.surface.Surface((720,720))
pygame.display.set_caption("Shopkeeper")
clock = pygame.time.Clock()

# Create Objects
grid = Grid(game_display, "grid_data.json")
player = Player(game_display)
dialog_box = Dialog_Box(game_display, "Hello World", (255,255,0), (0,0,0))

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill((94,129,162))

    # Render Sprites
    window.blit(game_display, (280,0))
    game_display.fill((94,129,162))
    grid.render()
    player.update()
    orderBar(window, (255,255,255))
    sideBar(window, (255,255,255))
    # dialog_box.render()

    pygame.display.flip()
    clock.tick(60)