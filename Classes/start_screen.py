import pygame
from pygame.math import Vector2

class Start_Screen():
    def __init__(self, window):
        self.bg_color = (0,0,0)
        self.window = window
        self.surface = pygame.surface.Surface((1280, 720))
        self.surface.fill(self.bg_color)
        self.normal_font = pygame.font.Font("Assets/Fonts/PixelFont.ttf", 24)
        self.small_font = pygame.font.Font("Assets/Fonts/PixelFont.ttf", 12)
        self.full_logo = pygame.image.load("Assets/Images/Logo/Logo_Menu.png")

    def render(self):
        self.surface.fill(self.bg_color)

        
        self.surface.blit(self.full_logo, (0,0))

        render_text = self.small_font.render("Press Space to Start", True, (255,255,255), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 630
        )
        self.surface.blit(render_text, render_text_rect)