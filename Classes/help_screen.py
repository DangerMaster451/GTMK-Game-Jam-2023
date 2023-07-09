import pygame
from pygame.math import Vector2

class Help_Screen():
    def __init__(self, window):
        self.bg_color = (94, 129, 162)
        self.window = window
        self.surface = pygame.surface.Surface((1280, 720))
        self.surface.fill(self.bg_color)
        self.normal_font = pygame.font.Font("Assets/Fonts/PixelFont.ttf", 24)
        self.small_font = pygame.font.Font("Assets/Fonts/PixelFont.ttf", 12)


    def render(self):
        self.surface.fill(self.bg_color)

        render_text = self.normal_font.render("How to Play", True, (255,255,255), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 50
        )
        self.window.blit(render_text, render_text_rect)