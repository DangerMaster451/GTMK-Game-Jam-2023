import pygame
from pygame.math import Vector2

class Tile():
    def __init__(self, window:pygame.surface.Surface, position:Vector2, scale:Vector2, image:pygame.surface.Surface, layer:str) -> None:
        self.window = window
        self.position = position
        self.image = pygame.transform.scale(pygame.image.load(image), scale)
        self.layer = layer

    def render(self) -> None:
        self.window.blit(self.image, self.position)