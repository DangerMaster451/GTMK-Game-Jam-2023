import pygame
from pygame.math import Vector2
from random import randint

class Side_Bar():
    def __init__(self, window, position:Vector2, bg_color):
        self.bg_color = bg_color
        self.window = window
        self.sideBar_surface = pygame.surface.Surface((280,720))
        self.sideBar_surface.fill(self.bg_color)
        self.sideBar_rect = self.sideBar_surface.get_rect(topleft=(position))
        self.font = pygame.font.Font("Assets/Fonts/PixelFont.ttf", 24)

    def display_text(self, text:str, text_color:tuple[int,int,int], position_y:int) -> None:
        render_text = self.font.render(text, True, text_color, self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(self.sideBar_surface.get_size()[0]/2, position_y)
        self.sideBar_surface.blit(render_text, render_text_rect)

    def render(self):
        self.window.blit(self.sideBar_surface, self.sideBar_rect)

class Left_Bar(Side_Bar):
    def __init__(self, window, position: Vector2, bg_color):
        super().__init__(window, position, bg_color)
    

class Right_Bar(Side_Bar):
    def __init__(self, window, position: Vector2, bg_color):
        super().__init__(window, position, bg_color)
        
