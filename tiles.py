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
        self.scale = scale
        

    def get_hover(self) -> bool:
        mouse_position = Vector2(pygame.mouse.get_pos()[0] - 280, pygame.mouse.get_pos()[1])
        # print(f"Mouse Pos: {mouse_position}, Tile Pos: {self.position}, Tile Size: {self.size}")

        if ((mouse_position.x > self.position.x and mouse_position.x < self.scale.x + self.position.x) and 
            (mouse_position.y > self.position.y and mouse_position.y < self.scale.y + self.position.y)):
            return True
        else:
            return False
        
    def get_pressed(self) -> bool:
        if self.get_hover() and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

    def update(self):
        self.render()
        if self.get_pressed():
            print("Pressed")

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