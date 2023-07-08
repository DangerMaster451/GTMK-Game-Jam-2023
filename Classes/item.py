import pygame
from pygame.math import Vector2
from Classes.player import Player

class Item():
    def __init__(self, window:pygame.surface.Surface, position:Vector2, image:pygame.surface.Surface, scale:tuple[int,int]) -> None:
        self.window = window
        self.position = position
        self.image = pygame.transform.scale(image, scale)

    def update(self, target_position:Vector2, item_texture:pygame.surface.Surface):
        self.move(target_position)
        self.render(item_texture)

    def move(self, target_position:Vector2):
        xDistance = self.position.x - target_position.x
        yDistance = self.position.y - target_position.y

        self.position = Vector2(self.position.x - xDistance/25, self.position.y - yDistance/25)

    def render(self, item_texture:pygame.surface.Surface):
        if item_texture != None:
            self.window.blit(item_texture, self.position)
