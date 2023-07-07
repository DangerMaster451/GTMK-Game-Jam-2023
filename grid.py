import pygame
from pygame.math import Vector2
import json

from tile import Tile

class Grid():
    def __init__(self, window:pygame.surface.Surface, file_path:str) -> None:
        self.tiles = []
        # Load Data
        with open(file_path, "r") as file:
            json_data = json.load(file)
            map = json_data["map"]
            grid_data = json_data["grid_data"]

            # Get Tile Size
            tile_size = Vector2(window.get_size()[0]/len(grid_data[0]), window.get_size()[1]/len(grid_data))

            # Loop through every value in 2D space
            for row_index in range(len(grid_data)):
                for column_index in range(len(grid_data[row_index])):
                    # find object 
                    value = grid_data[row_index][column_index]
                    for tile_type in map:
                        if tile_type["data_index"] == value:
                            # Create new tile object
                            position = Vector2(tile_size.x * column_index, tile_size.y * row_index)
                            image = tile_type["file_path"]
                            layer = tile_type["layer"]
                            tile = Tile(window, position, tile_size, image, layer)
                            self.tiles.append(tile)

    def render(self):
        # Render all tiles
        for tile in self.tiles:
            tile.render()