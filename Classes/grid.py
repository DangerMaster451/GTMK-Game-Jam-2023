import pygame
from pygame.math import Vector2
import json

from Classes.tiles import *

class Grid:
    def __init__(self, window: pygame.surface.Surface, file_path: str, player) -> None:
        self.tiles = []
        # Load Data
        with open(file_path, "r") as file:
            json_data = json.load(file)
            map = json_data["map"]
            grid_data = json_data["grid_data"]

            # Get Tile Size
            tile_size = Vector2(
                window.get_size()[0] / len(grid_data[0]),
                window.get_size()[1] / len(grid_data),
            )

            # Loop through every value in 2D space
            for row_index in range(len(grid_data)):
                for column_index in range(len(grid_data[row_index])):
                    # find object
                    value = grid_data[row_index][column_index]
                    for tile_json_object in map:
                        if tile_json_object["data_index"] == value:
                            # Create new tile object
                            position = Vector2(
                                tile_size.x * column_index, tile_size.y * row_index
                            )
                            object = tile_json_object["object"]

                            match object:
                                case "Default_Tiles":
                                    tile = Default_Tiles(window, position, tile_size)
                                case "Cracked_Tiles":
                                    tile = Cracked_Tiles(window, position, tile_size)
                                case "Decorative_Tiles":
                                    tile = Decorative_Tiles(window, position, tile_size)
                                case "Center_Tiles":
                                    tile = Center_Tiles(window, position, tile_size)
                                case "Grass":
                                    tile = Grass(window, position, tile_size)
                                case "Anvil_Left":
                                    tile = Anvil_Left(window, position, tile_size)
                                case "Anvil_Right":
                                    tile = Anvil_Right(window, position, tile_size)
                                case "Wood_Deposit":
                                    tile = Wood_Deposit(window, position, tile_size)
                                case "Steel_Deposit":
                                    tile = Steel_Deposit(window, position, tile_size)
                                case "String_Deposit":
                                    tile = String_Deposit(window, position, tile_size)
                                case "Titanium_Deposit":
                                    tile = Titanium_Deposit(window, position, tile_size)
                                case _:
                                    raise Exception("No class to represent json value")
                            self.tiles.append(tile)

    def render(self) -> None:
        # Render all tiles
        for tile in self.tiles:
            tile.update()

    def get_interactable_tiles_in_scene(self) -> list[Tile]:
        INTERACTABLE_TILE_TYPES = [
            Anvil_Left,
            Wood_Deposit,
            Steel_Deposit,
            String_Deposit,
            Titanium_Deposit
        ]

        return [tile for tile in self.tiles if type(tile) in INTERACTABLE_TILE_TYPES]

    def get_anvil_inventories(self) -> list[list]:
        return [tile.inventory for tile in self.tiles if type(tile) == Anvil_Left]

    def clear_anvil_inventories(self) -> None:
        for tile in self.tiles:
            if type(tile) == Anvil_Left:
                tile.inventory = []
