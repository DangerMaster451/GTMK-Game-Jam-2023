import pygame
from pygame.math import Vector2

class Game_Over_Screen():
    def __init__(self, window):
        self.bg_color = (94-25, 129-25, 162-25)
        self.window = window
        self.surface = pygame.surface.Surface((720, 720))
        self.surface.fill(self.bg_color)
        #self.sideBar_rect = self.surface.get_rect(topleft=(280,0))
        self.normal_font = pygame.font.Font("Assets/Fonts/PixelFont.ttf", 24)
        self.small_font = pygame.font.Font("Assets/Fonts/PixelFont.ttf", 12)

    def render(self, score:str):
        self.surface.fill(self.bg_color)

        render_text = self.normal_font.render("GAME OVER", True, (255,255,255), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 50
        )
        self.surface.blit(render_text, render_text_rect)

        render_text = self.normal_font.render("Score", True, (255,255,255), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 100
        )
        self.surface.blit(render_text, render_text_rect)

        render_text = self.small_font.render(score, True, (255,255,255), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 125
        )
        self.surface.blit(render_text, render_text_rect)

        render_text = self.normal_font.render("High Score", True, (255,255,255), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 200
        )
        self.surface.blit(render_text, render_text_rect)

        render_text = self.small_font.render("1000", True, (255,255,255), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 225
        )
        self.surface.blit(render_text, render_text_rect)
        
