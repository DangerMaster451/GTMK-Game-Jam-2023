import pygame
from pygame.math import Vector2

class Side_Bar():
    def __init__(self, window, position:Vector2, color):
        self.color = color
        self.window = window
        self.sideBar_surface = pygame.surface.Surface((280,720))
        self.sideBar_surface.fill(color)
        self.sideBar_rect = self.sideBar_surface.get_rect(topleft=(position))
        
    def render(self):
        self.window.blit(self.sideBar_surface, self.sideBar_rect)
        
