import pygame
from pygame.math import Vector2
from sys import exit

import Classes.task as task
from Classes.tiles import *
from Classes.player import Player
from Classes.grid import Grid
from Classes.side_bars import Left_Bar, Right_Bar

# Basic Setup
pygame.init()
DEFAULT_RESOLUTION = (1280, 720)
window = pygame.display.set_mode(DEFAULT_RESOLUTION, pygame.RESIZABLE | pygame.SCALED)
game_display = pygame.surface.Surface((720,720))
pygame.display.set_caption("Shopkeeper")
clock = pygame.time.Clock()

# Create Objects
player = Player(game_display)
grid = Grid(game_display, "grid_data.json", player)

right_bar = Right_Bar(window, (1000,0), (94,129,162))
left_bar = Left_Bar(window, (0,0), (94,129,162))

test_task = task.new_task("items.json", (25,25))

interactable_tiles = grid.get_interactable_tiles_in_scene()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Clear All Windows
    window.fill((94,129,162))
    left_bar.sideBar_surface.fill(left_bar.bg_color)
    right_bar.sideBar_surface.fill(right_bar.bg_color)
    game_display.fill((94,129,162))
    
    # Render Sprites    
    grid.render()
    player.update()

    left_bar.display_text("Task 1", (255,255,255), 75)
    left_bar.display_task(test_task, (255,255,0), Vector2(75, 175), 25)

    right_bar.display_text(player.item, (255,255,255), 75)
    right_bar.display_text(str(grid.get_anvil_inventories()), (255,255,255), 175)

    # Check for interactions
    for tile in interactable_tiles:
        if tile.check_interaction(player):
            if type(tile) == Anvil:
                if player.item not in tile.inventory:
                    tile.inventory.append(player.item)
                player.item = None
            else:
                player.item = tile.item_name    

    # Render Game
    window.blit(game_display, (280,0))

    # Render Side Bars
    right_bar.render()
    left_bar.render()

    pygame.display.flip()
    clock.tick(60)