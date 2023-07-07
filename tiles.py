import pygame
import math
from pygame.math import Vector2

from player import Player

class Tile():
    def __init__(self, window:pygame.surface.Surface, position:Vector2, scale:Vector2, image:pygame.surface.Surface, layer:str) -> None:
        self.window = window
        self.position = position
        self.image = pygame.transform.scale(image, scale)
        self.layer = layer

    def render(self) -> None:
        self.window.blit(self.image, self.position)

class Anvil(Tile):
    def __init__(self, window:pygame.surface.Surface, position:Vector2, scale:Vector2, player:Player) -> None:
        image = pygame.image.load("Assets/Tiles/Colored/tile_0018.png")
        layer = "Wall"
        Tile.__init__(self, window, position, scale, image, layer)
        self.scale = scale
        self.player = player
        
    def check_interaction(self) -> bool:
        # calculate distance a**2 + b**2 = c**2
        keys = pygame.key.get_pressed()
        distance_to_player = math.sqrt(abs(self.position.x - self.player.position.x)**2 + abs(self.position.y - self.player.position.y)**2)
        if distance_to_player < 50 and keys[pygame.K_e]:
            return True
        else:
            return False

    def update(self):
        self.render()
        if self.check_interaction():
            print("interaction")

class Grass(Tile):
    def __init__(self, window:pygame.surface.Surface, position:Vector2, scale:Vector2) -> None:
        image = pygame.image.load("Assets/Custom/grass.png")
        layer = "Floor"
        Tile.__init__(self, window, position, scale, image, layer)
        self.size = image.get_size()

    def update(self):
        self.render()
        

class Center_Tiles(Tile):
    def __init__(self, window:pygame.surface.Surface, position:Vector2, scale:Vector2) -> None:
        image = pygame.image.load("Assets/Custom/tiles_center.png")
        layer = "Floor"
        Tile.__init__(self, window, position, scale, image, layer)
        self.size = image.get_size()

    def update(self):
        self.render()

class Cracked_Tiles(Tile):
    def __init__(self, window:pygame.surface.Surface, position:Vector2, scale:Vector2) -> None:
        image = pygame.image.load("Assets/Custom/tiles_cracked.png")
        layer = "Floor"
        Tile.__init__(self, window, position, scale, image, layer)
        self.size = image.get_size()

    def update(self):
        self.render()

class Decorative_Tiles(Tile):
    def __init__(self, window:pygame.surface.Surface, position:Vector2, scale:Vector2) -> None:
        image = pygame.image.load("Assets/Custom/tiles_decorative.png")
        layer = "Floor"
        Tile.__init__(self, window, position, scale, image, layer)
        self.size = image.get_size()

    def update(self):
        self.render()

class Default_Tiles(Tile):
    def __init__(self, window:pygame.surface.Surface, position:Vector2, scale:Vector2) -> None:
        image = pygame.image.load("Assets/Custom/tiles.png")
        layer = "Floor"
        Tile.__init__(self, window, position, scale, image, layer)
        self.size = image.get_size()

    def update(self):
        self.render()