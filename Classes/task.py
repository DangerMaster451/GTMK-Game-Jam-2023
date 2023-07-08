import pygame

class Task():
    def __init__(self, weapon_type:str, materials:list[pygame.surface.Surface], enchantments:list[pygame.surface.Surface]) -> None:
        self.weapon_type = weapon_type
        self.materials = materials
        self.enchantments = enchantments

