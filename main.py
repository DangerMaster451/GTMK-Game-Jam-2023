import pygame
from pygame.math import Vector2
from sys import exit

import Classes.task as task_module
import Classes.npc as npc_module
import Classes.particles as particles_module
from Classes.tiles import *
from Classes.item import Item
from Classes.player import Player
from Classes.grid import Grid
from Classes.side_bars import Left_Bar, Right_Bar
from Classes.end_screen import Game_Over_Screen
from Classes.start_screen import Start_Screen
from Classes.help_screen import Help_Screen

# Basic Setup
pygame.init()
pygame.mixer.init()
DEFAULT_RESOLUTION = (1280, 720)
window = pygame.display.set_mode(DEFAULT_RESOLUTION, pygame.RESIZABLE | pygame.SCALED)

pygame.display.set_caption("\"The Hero's Blacksmith\" - GMTK Game Jam Entry 2023")
pygame.display.set_icon(pygame.image.load("Assets/Images/Logo/Logo_Icon.png"))
clock = pygame.time.Clock()

# Load Sound FX
anvil_fx = pygame.mixer.Sound("Assets/SoundFX/Anvil.wav")
step_fx = [
    pygame.mixer.Sound("Assets/SoundFX/Step 1.wav"),
    #pygame.mixer.Sound("Assets/SoundFX/Step 2.wav")
]
# Load Assets
grass_particle = pygame.image.load("Assets/Images/Tiles/Grass.png")
player_particle = pygame.image.load("Assets/Images/Tiles/Tiles.png")
tool_tip_e = pygame.transform.scale(pygame.image.load("Assets/Images/Icons/tool_tip_e.png"), (50,50))
tool_tip_space = pygame.transform.scale(pygame.image.load("Assets/Images/Icons/tool_tip_space.png"), (100,50))
ticking = pygame.mixer.Sound("Assets/Music/countdown.mp3")

# Create Objects
game_state = "Start"
start_display = Start_Screen(window)
help_display = Help_Screen(window)
game_display = pygame.surface.Surface((720, 720))
game_over_display = Game_Over_Screen(window)

right_bar = Right_Bar(window, (1000, 0), (78, 156, 230))
left_bar = Left_Bar(window, (0, 0), (78, 156, 230))

player = Player(game_display)
grid = Grid(game_display, "grid_data.json", player)

tasks = []
npcs = []
particles = []

min_npcs = 1
max_npcs = 4
npc_spawn_chance = 5

score = 0
display_score = ""

pygame.time.set_timer(pygame.USEREVENT, 1000)
timer = 60
display_timer = ""

interactable_tiles = grid.get_interactable_tiles_in_scene()

pickup = Item(game_display, Vector2(0,0), grass_particle, (35,35))

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT and game_state == "Game": 
            timer -= 1
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_state == "Game":
        # Clear All Windows
        window.fill((94, 129, 162))
        left_bar.sideBar_surface.fill(left_bar.bg_color)
        right_bar.sideBar_surface.fill(right_bar.bg_color)
        game_display.fill((94, 129, 162))

        # Spawn NPCs
        npcs = npc_module.try_spawn_npc(game_display, npcs, min_npcs, max_npcs, npc_spawn_chance)

        # Render Sprites    
        grid.render()
        pickup.update(player.position, player.item_texture)
        player.update()

        # Spawn Player Particles
        if player.is_moving():
            particles = particles_module.spawn_particles(game_display, particles, Vector2(player.position.x+25, player.position.y+45), player_particle, Vector2(100,100), 75)

        # Spawn NPC Particles
        for npc in npcs:
            if npc.state == "move" or npc.state == "leave":
                particles = particles_module.spawn_particles(game_display, particles, Vector2(npc.position.x+25, npc.position.y+45), grass_particle, Vector2(100,100), 75)

        # Render Particles
        for particle in particles: particle.update() 

        # Remove unused Particles
        for particle in particles:
            if particle.life <= 0:
                particles.remove(particle)
                del particle

        # Update NPCs
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

        # Display Text
        right_bar.display_text("Score", (255, 255, 255), 75)
        right_bar.display_text(display_score, (255, 255, 255), 100, small_text=True)

        left_bar.display_text(f"Timer: {display_timer}", (255, 255, 0), 75)

        right_bar.display_text("Player", (255, 255, 255), 275)
        right_bar.display_text("Inventory", (255, 255, 255), 310)
        right_bar.display_text(player.item, (255, 255, 0), 335, small_text=True)

        right_bar.display_text("Anvil", (255, 255, 255), 375)
        right_bar.display_text("Inventory", (255, 255, 255), 410)

        for index, item in enumerate(grid.get_anvil_inventories()[0]):
            right_bar.display_text(item, (255, 255, 0), (435 + index*20), small_text=True)

        # Display Tasks
        left_bar.display_text("Tasks", (255, 255, 255), 125)
        for index, _task in enumerate(tasks):
            left_bar.display_task(
                _task,
                grid,
                (255, 255, 0),
                Vector2(75, 175*(index+1)),
                25,
                _task.check_if_task_completed(grid),
            )

        keys = pygame.key.get_pressed()

        # Check for interactions
        for tile in interactable_tiles:
            if tile.check_interaction(player):
                game_display.blit(tool_tip_e, Vector2(player.position.x, player.position.y - 65))
                if keys[pygame.K_e]:
                    if type(tile) == Anvil_Left:
                        if player.item not in tile.inventory and player.item != None:
                            anvil_fx.play()
                            tile.inventory.append(player.item)
                        player.item = None
                        player.item_texture = None
                    else:
                        player.item = tile.item_name
                        player.item_texture = tile.item_texture        

        # Check for completed Tasks
        for _task in tasks:
            if _task.check_if_task_completed(grid):
                game_display.blit(tool_tip_space, Vector2(player.position.x - 25, player.position.y + 60))
                if keys[pygame.K_SPACE]:
                    tasks.remove(_task)
                    grid.clear_anvil_inventories()
                    score += 1

        # Update Display Score          
        display_score = str(score)

        # Update Display Timer
        display_timer = str(timer)

        # Clear Anvil Inventories
        if keys[pygame.K_q]:
            grid.clear_anvil_inventories()


    # Render Final Surfaces
    keys = pygame.key.get_pressed()
    match game_state:
        case "Start":
            start_display.render()
            window.blit(start_display.surface, (0,0))

            if keys[pygame.K_SPACE]:
                game_state = "Help"
        case "Help":
            help_display.render()
            window.blit(help_display.surface, (0,0))

            if keys[pygame.K_w]:
                game_state = "Game"
                ticking.play()
        case "Game":
            window.blit(game_display, (280, 0))
            right_bar.render()
            left_bar.render()

            if timer < 0:
                game_state = "End"
        case "End":
            game_over_display.render(display_score)
            window.blit(game_over_display.surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)