import pygame
import math
from pygame.math import Vector2


class NPC(pygame.sprite.Sprite):
    def __init__(self, window:pygame.surface.Surface):
        self.window = window
        self.position = Vector2(650, 0)
        self.image = pygame.transform.scale(pygame.image.load("Assets/Images/Sprites/NPC_1.png"), (50,50))
        self.state = "move"
        self.speed = 1
        self.wobble_value = 0

    def update(self):
        if self.state == "move":
            self.move()
        self.render()

    def move(self):
        self.position.y += self.speed
        self.wobble_value += 1


    def render(self):
        render_image = pygame.transform.rotate(
            self.image, math.sin(self.wobble_value / 5) * 10
        )
        self.window.blit(render_image, self.position)