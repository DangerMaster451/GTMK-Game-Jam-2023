import pygame
from pygame.math import Vector2
from Classes.player import Player

class Item():
    def __init__(self, window:pygame.surface.Surface, position:Vector2, target_object, item_texture:pygame.surface.Surface=None, scale:tuple[int,int]=(None,None)) -> None:
        self.window = window
        self.position = position
        self.target_object = target_object
        if item_texture != None:
            self.item_texture = pygame.transform.scale(item_texture, scale)
        else:
            self.item_texture = None

    def update(self, item_texture:pygame.surface.Surface=None):
        target_position = self.target_object.position
        self.move(target_position)
        if item_texture == None:
            self.render(self.item_texture)
        else:
            self.render(item_texture)

    def move(self, target_position:Vector2):
        xDistance = self.position.x - target_position.x
        yDistance = self.position.y - target_position.y

        self.position = Vector2(self.position.x - xDistance/25, self.position.y - yDistance/25)

    def render(self, item_texture:pygame.surface.Surface):
        if item_texture != None:
            self.window.blit(item_texture, self.position)
