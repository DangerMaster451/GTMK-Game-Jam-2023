import pygame
from pygame.math import Vector2

class Tile():
    def __init__(self, window:pygame.surface.Surface, position:Vector2, scale:Vector2, image:pygame.surface.Surface, layer:str) -> None:
        self.window = window
        self.position = position
        self.image = pygame.transform.scale(image, scale)
        self.layer = layer

    def render(self) -> None:
        self.window.blit(self.image, self.position)

class Anvil(Tile):
    def __init__(self, window:pygame.surface.Surface, position:Vector2, scale:Vector2) -> None:
        image = pygame.image.load("Assets/Tiles/Colored/tile_0018.png")
        layer = "Wall"
        Tile.__init__(self, window, position, scale, image, layer)

class Grass(Tile):
    def __init__(self, window:pygame.surface.Surface, position:Vector2, scale:Vector2) -> None:
        image = pygame.image.load("Assets/Custom/grass.png")
        layer = "Floor"
        Tile.__init__(self, window, position, scale, image, layer)

class Center_Tiles(Tile):
    def __init__(self, window:pygame.surface.Surface, position:Vector2, scale:Vector2) -> None:
        image = pygame.image.load("Assets/Custom/tiles_center.png")
        layer = "Floor"
        Tile.__init__(self, window, position, scale, image, layer)

class Cracked_Tiles(Tile):
    def __init__(self, window:pygame.surface.Surface, position:Vector2, scale:Vector2) -> None:
        image = pygame.image.load("Assets/Custom/tiles_cracked.png")
        layer = "Floor"
        Tile.__init__(self, window, position, scale, image, layer)

class Decorative_Tiles(Tile):
    def __init__(self, window:pygame.surface.Surface, position:Vector2, scale:Vector2) -> None:
        image = pygame.image.load("Assets/Custom/tiles_decorative.png")
        layer = "Floor"
        Tile.__init__(self, window, position, scale, image, layer)

class Default_Tiles(Tile):
    def __init__(self, window:pygame.surface.Surface, position:Vector2, scale:Vector2) -> None:
        image = pygame.image.load("Assets/Custom/tiles.png")
        layer = "Floor"
        Tile.__init__(self, window, position, scale, image, layer)