import pygame
import math
from pygame.math import Vector2

from Classes.player import Player


class Tile:
    def __init__(
        self,
        window: pygame.surface.Surface,
        position: Vector2,
        scale: Vector2,
        image: pygame.surface.Surface,
    ) -> None:
        self.window = window
        self.position = position
        self.image = pygame.transform.scale(image, scale)

    def render(self) -> None:
        self.window.blit(self.image, self.position)


class Anvil_Left(Tile):
    def __init__(
        self, window: pygame.surface.Surface, position: Vector2, scale: Vector2
    ) -> None:
        image = pygame.image.load("Assets/Images/Tiles/Anvil_Left.png")
        Tile.__init__(self, window, position, scale, image)
        self.scale = scale
        self.inventory = []

    def check_interaction(self, player) -> bool:
        # calculate distance a**2 + b**2 = c**2
        distance_to_player = math.sqrt(
            abs(self.position.x - player.position.x) ** 2
            + abs(self.position.y - player.position.y) ** 2
        )
        if distance_to_player < 50:
            return True
        else:
            return False

    def update(self) -> None:
        self.render()

class Anvil_Right(Tile):
    def __init__(
        self, window: pygame.surface.Surface, position: Vector2, scale: Vector2
    ) -> None:
        image = pygame.image.load("Assets/Images/Tiles/Anvil_Right.png")
        Tile.__init__(self, window, position, scale, image)
        self.scale = scale
        self.inventory = []

    def update(self) -> None:
        self.render()


class Wood_Deposit(Tile):
    def __init__(
        self, window: pygame.surface.Surface, position: Vector2, scale: Vector2
    ) -> None:
        image = pygame.image.load("Assets/Images/Tiles/Wood_Tile.png")
        Tile.__init__(self, window, position, scale, image)
        self.item_name = "Wood"
        self.scale = scale

    def check_interaction(self, player) -> bool:
        # calculate distance a**2 + b**2 = c**2
        distance_to_player = math.sqrt(
            abs(self.position.x - player.position.x) ** 2
            + abs(self.position.y - player.position.y) ** 2
        )
        if distance_to_player < 50:
            return True
        else:
            return False

    def update(self) -> None:
        self.render()


class Steel_Deposit(Tile):
    def __init__(
        self, window: pygame.surface.Surface, position: Vector2, scale: Vector2
    ) -> None:
        image = pygame.image.load("Assets/Images/Tiles/Steel_Tile.png")
        Tile.__init__(self, window, position, scale, image)
        self.item_name = "Steel"
        self.scale = scale

    def check_interaction(self, player) -> bool:
        # calculate distance a**2 + b**2 = c**2
        distance_to_player = math.sqrt(
            abs(self.position.x - player.position.x) ** 2
            + abs(self.position.y - player.position.y) ** 2
        )
        if distance_to_player < 50:
            return True
        else:
            return False

    def update(self) -> None:
        self.render()


class String_Deposit(Tile):
    def __init__(
        self, window: pygame.surface.Surface, position: Vector2, scale: Vector2
    ) -> None:
        image = pygame.image.load("Assets/Images/Tiles/String_Tile.png")
        Tile.__init__(self, window, position, scale, image)
        self.item_name = "String"
        self.scale = scale

    def check_interaction(self, player) -> bool:
        # calculate distance a**2 + b**2 = c**2
        distance_to_player = math.sqrt(
            abs(self.position.x - player.position.x) ** 2
            + abs(self.position.y - player.position.y) ** 2
        )
        if distance_to_player < 50:
            return True
        else:
            return False

    def update(self) -> None:
        self.render()


class Titanium_Deposit(Tile):
    def __init__(
        self, window: pygame.surface.Surface, position: Vector2, scale: Vector2
    ) -> None:
        image = pygame.image.load("Assets/Images/Tiles/Titanium_Tile.png")
        Tile.__init__(self, window, position, scale, image)
        self.item_name = "Titanium"
        self.scale = scale

    def check_interaction(self, player) -> bool:
        # calculate distance a**2 + b**2 = c**2
        distance_to_player = math.sqrt(
            abs(self.position.x - player.position.x) ** 2
            + abs(self.position.y - player.position.y) ** 2
        )
        if distance_to_player < 50:
            return True
        else:
            return False

    def update(self) -> None:
        self.render()


class Grass(Tile):
    def __init__(
        self, window: pygame.surface.Surface, position: Vector2, scale: Vector2
    ) -> None:
        image = pygame.image.load("Assets/Images/Tiles/Grass.png")
        Tile.__init__(self, window, position, scale, image)
        self.size = image.get_size()

    def update(self) -> None:
        self.render()


class Center_Tiles(Tile):
    def __init__(
        self, window: pygame.surface.Surface, position: Vector2, scale: Vector2
    ) -> None:
        image = pygame.image.load("Assets/Images/Tiles/Tiles_Center.png")
        Tile.__init__(self, window, position, scale, image)
        self.size = image.get_size()

    def update(self) -> None:
        self.render()


class Cracked_Tiles(Tile):
    def __init__(
        self, window: pygame.surface.Surface, position: Vector2, scale: Vector2
    ) -> None:
        image = pygame.image.load("Assets/Images/Tiles/Tiles_Cracked.png")
        Tile.__init__(self, window, position, scale, image)
        self.size = image.get_size()

    def update(self) -> None:
        self.render()


class Decorative_Tiles(Tile):
    def __init__(
        self, window: pygame.surface.Surface, position: Vector2, scale: Vector2
    ) -> None:
        image = pygame.image.load("Assets/Images/Tiles/Tiles_Decorative.png")
        Tile.__init__(self, window, position, scale, image)
        self.size = image.get_size()

    def update(self) -> None:
        self.render()


class Default_Tiles(Tile):
    def __init__(
        self, window: pygame.surface.Surface, position: Vector2, scale: Vector2
    ) -> None:
        image = pygame.image.load("Assets/Images/Tiles/Tiles.png")
        Tile.__init__(self, window, position, scale, image)
        self.size = image.get_size()

    def update(self) -> None:
        self.render()
