import pygame
from pygame.math import Vector2
from sys import exit

import Classes.task as task_module
import Classes.npc as npc_module
from Classes.tiles import *
from Classes.player import Player
from Classes.npc import NPC
from Classes.grid import Grid
from Classes.side_bars import Left_Bar, Right_Bar

# ! Add delta time for player speed

# Basic Setup
pygame.init()
DEFAULT_RESOLUTION = (1280, 720)
window = pygame.display.set_mode(DEFAULT_RESOLUTION, pygame.RESIZABLE | pygame.SCALED)
game_display = pygame.surface.Surface((720, 720))
pygame.display.set_caption("Shopkeeper - GMTK Game Jam Entry 2023")
clock = pygame.time.Clock()

# Create Objects
player = Player(game_display)
grid = Grid(game_display, "grid_data.json", player)

right_bar = Right_Bar(window, (1000, 0), (94, 129, 162))
left_bar = Left_Bar(window, (0, 0), (94, 129, 162))

tasks = []
npcs = []

min_npcs = 1
max_npcs = 12
npc_spawn_chance = 3

interactable_tiles = grid.get_interactable_tiles_in_scene()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Clear All Windows
    window.fill((94, 129, 162))
    left_bar.sideBar_surface.fill(left_bar.bg_color)
    right_bar.sideBar_surface.fill(right_bar.bg_color)
    game_display.fill((94, 129, 162))

    # Spawn NPCs
    npcs = npc_module.try_spawn_npc(game_display, npcs, min_npcs, max_npcs, npc_spawn_chance)

    # Render Sprites
    grid.render()
    player.update()

    for npc in npcs:
        npc.update()

        match npc.state:
            case "start_order":
                tasks.append(task_module.new_task(npc, "items.json", (25,25)))

            case "wait":
                match = False
                for _task in tasks:
                    if _task.npc == npc:
                        match = True
                if match == False:
                    npc.state = "leave"

            case "delete":
                npcs.remove(npc)
                del npc

    left_bar.display_text("Tasks", (255, 255, 255), 75)
    for index, _task in enumerate(tasks):
        left_bar.display_task(
            _task,
            grid,
            (255, 255, 0),
            Vector2(75, 175 + 150 * index),
            25,
            _task.check_if_task_completed(grid),
        )

    right_bar.display_text("Player", (255, 255, 255), 75)
    right_bar.display_text("Inventory", (255, 255, 255), 110)
    right_bar.display_text(player.item, (255, 255, 0), 135, small_text=True)

    right_bar.display_text("Anvil", (255, 255, 255), 175)
    right_bar.display_text("Inventory", (255, 255, 255), 210)

    for index, item in enumerate(grid.get_anvil_inventories()[0]):
        right_bar.display_text(item, (255, 255, 0), (235 + index * 20), small_text=True)

    # Check for interactions
    for tile in interactable_tiles:
        if tile.check_interaction(player):
            if type(tile) == Anvil_Left:
                if player.item not in tile.inventory and player.item != None:
                    tile.inventory.append(player.item)
                player.item = None
            else:
                player.item = tile.item_name

    keys = pygame.key.get_pressed()
    for _task in tasks:
        if _task.check_if_task_completed(grid):
            if keys[pygame.K_SPACE]:
                tasks.remove(_task)
                grid.clear_anvil_inventories()
    if keys[pygame.K_q]:
        grid.clear_anvil_inventories()

    # Render Game
    window.blit(game_display, (280, 0))

    # Render Side Bars
    right_bar.render()
    left_bar.render()

    pygame.display.flip()
    clock.tick(60)