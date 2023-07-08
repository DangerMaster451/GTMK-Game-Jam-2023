import pygame
from sys import exit

from Classes.player import Player
from Classes.grid import Grid
from Classes.side_bars import Left_Bar, Right_Bar
from Classes.task import Task

# Basic Setup
pygame.init()
DEFAULT_RESOLUTION = (1280, 720)
window = pygame.display.set_mode(DEFAULT_RESOLUTION, pygame.RESIZABLE | pygame.SCALED)
game_display = pygame.surface.Surface((720,720))
pygame.display.set_caption("Shopkeeper")
clock = pygame.time.Clock()

# Load Images
wood_icon = pygame.transform.scale(pygame.image.load("Assets/Tiles/Colored/tile_0008.png"), (25,25))
iron_icon = pygame.transform.scale(pygame.image.load("Assets/Tiles/Colored/tile_0010.png"), (25,25))
snake_icon = pygame.transform.scale(pygame.image.load("Assets/Tiles/Colored/tile_0020.png"), (25,25))
mouse_icon = pygame.transform.scale(pygame.image.load("Assets/Tiles/Colored/tile_0022.png"), (25,25))
crab_icon = pygame.transform.scale(pygame.image.load("Assets/Tiles/Colored/tile_0023.png"), (25,25))

# Create Objects
player = Player(game_display)
grid = Grid(game_display, "grid_data.json", player)

right_bar = Right_Bar(window, (1000,0), (94,129,162))
left_bar = Left_Bar(window, (0,0), (94,129,162))

test_task = Task("Sword", [wood_icon, iron_icon], [snake_icon, mouse_icon, crab_icon])

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

    left_bar.display_text("Hi", (255,255,255), 75)
    right_bar.display_text("Hello", (255,255,255), 175)

    left_bar.display_task(test_task, (255,255,0), 175)
    
    right_bar.render()
    left_bar.render()

    pygame.display.flip()
    clock.tick(60)