import pygame
from pygame.math import Vector2

class Game_Over_Screen():
    def __init__(self, window):
        self.bg_color = (94, 129, 162)
        self.window = window
        self.surface = pygame.surface.Surface((1280, 720))
        self.surface.fill(self.bg_color)
        self.normal_font = pygame.font.Font("Assets/Fonts/PixelFont.ttf", 24)
        self.small_font = pygame.font.Font("Assets/Fonts/PixelFont.ttf", 12)

        with open("high_score.txt", "r") as high_score_file:
            self.high_score = high_score_file.read()

    def update_high_score(self, score:int):
        if score > self.high_score:
            with open("high_score.txt", "w") as high_score_file:
                high_score_file.write(str(score))
                self.high_score = score


    def render(self, score:int):
        self.update_high_score(score)
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

        render_text = self.small_font.render(str(score), True, (255,255,255), self.bg_color)
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

        render_text = self.small_font.render(self.high_score, True, (255,255,255), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 225
        )
        self.surface.blit(render_text, render_text_rect)

        render_text = self.normal_font.render("Credits", True, (255,255,255), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 300
        )
        self.surface.blit(render_text, render_text_rect)

        render_text = self.small_font.render("Programers: Andrew Pelton and Tristan Krizan", True, (255,255,255), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 325
        )
        self.surface.blit(render_text, render_text_rect)

        render_text = self.small_font.render("Play Testers: Noah", True, (255,255,255), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 350
        )
        self.surface.blit(render_text, render_text_rect)

        render_text = self.small_font.render("Art: Kenny and Tristan Krizan", True, (255,255,255), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 375
        )
        self.surface.blit(render_text, render_text_rect)

        render_text = self.small_font.render("Music and Sound Design: Andrew Pelton", True, (255,255,255), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 400
        )
        self.surface.blit(render_text, render_text_rect)

        render_text = self.normal_font.render("Press SPACE to play Again", True, (255,255,255), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 500
        )
        self.surface.blit(render_text, render_text_rect)
        
