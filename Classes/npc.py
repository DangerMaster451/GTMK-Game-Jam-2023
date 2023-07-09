import pygame
import math
import random
from pygame.math import Vector2

class NPC(pygame.sprite.Sprite):
    def __init__(self, window:pygame.surface.Surface, index):
        self.window = window
        self.position = Vector2(650, 0)
        self.image = self.get_image()
        self.order_image = pygame.transform.scale(pygame.image.load("Assets/Images/Icons/speechBubble.png"), (50,50))
        self.state = "move"
        self.speed = 10
        self.wobble_value = 0
        self.start_order_frame = 0
        self.current_frame = 0
        self.index = index

    def get_image(self) -> pygame.surface.Surface:
        images = [
            pygame.transform.scale(pygame.image.load("Assets/Images/Sprites/NPC_1.png"), (50,50)),
            pygame.transform.scale(pygame.image.load("Assets/Images/Sprites/NPC_2.png"), (50,50)),
            pygame.transform.scale(pygame.image.load("Assets/Images/Sprites/NPC_3.png"), (50,50))
                  ]
        return images[random.randint(0,len(images)-1)]

    def update(self):
        match self.state:
            case "move":
                self.move()
            case "start_order":
                self.start_order()
            case "order":
                self.order()
            case "wait":
                self.wait()
            case "leave":
                self.leave()
        self.render()
        self.current_frame += 1

    def move(self):
        self.position.y += self.speed
        self.wobble_value += 1
        if self.position.y > 535 - self.index*135:
            self.state = "start_order"
            self.start_order_frame = self.current_frame

    def start_order(self):
        # play sound effect
        self.wobble_value = 0
        self.state = "order"

    def order(self):          
        if self.current_frame - self.start_order_frame > 60:
            self.state = "wait"

    def wait(self):
        pass
        # TODO idle animation

    def leave(self):
        self.position.y += self.speed
        self.wobble_value += 1
        if self.position.y > 720:
            self.state = "delete"

    def render(self):
        if self.state == "order":
            self.window.blit(self.order_image, ((self.position)-(40,40)))
            self.window.blit(self.image, (self.position))
        else:
            render_image = pygame.transform.rotate(
                self.image, math.sin(self.wobble_value / 5) * 10
            )
            self.window.blit(render_image, self.position)


def try_spawn_npc(window, npcs:list[NPC], min:int, max:int, chance_per_frame:int) -> list[NPC]:
    used_indexes = []
    smallest_index = len(npcs)
    for npc in npcs:
        used_indexes.append(npc.index)
    
    for index in range(len(used_indexes)):
        if not index in used_indexes:
            smallest_index = index
            break

    if len(npcs) < min:
        npcs.insert(smallest_index, NPC(window, smallest_index)) # New NPC
    
    if len(npcs) < max:
        if random.randint(0, 100-chance_per_frame) == 0:
            npcs.insert(smallest_index, NPC(window, smallest_index)) # New NPC
    
    return npcs # Return updated list