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
        wood_icon = pygame.transform.scale(pygame.image.load("Assets/Images/Icons/Wood_Icon.png"), (25,25))
        steel_icon = pygame.transform.scale(pygame.image.load("Assets/Images/Icons/Steel_Icon.png"), (25,25))
        string_icon = pygame.transform.scale(pygame.image.load("Assets/Images/Icons/String_Icon.png"), (25,25))
        titanium_icon = pygame.transform.scale(pygame.image.load("Assets/Images/Icons/Titanium_Icon.png"), (25,25))

        wood_deposit = pygame.transform.scale(pygame.image.load("Assets/Images/Tiles/Wood_Tile.png"), (25,25))
        steel_deposit = pygame.transform.scale(pygame.image.load("Assets/Images/Tiles/Steel_Tile.png"), (25,25))
        string_deposit = pygame.transform.scale(pygame.image.load("Assets/Images/Tiles/String_Tile.png"), (25,25))
        titanium_deposit = pygame.transform.scale(pygame.image.load("Assets/Images/Tiles/Titanium_Tile.png"), (25,25))


        self.surface.fill(self.bg_color)

        render_text = self.normal_font.render("How to Play", True, (255,255,255), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 50
        )
        self.surface.blit(render_text, render_text_rect)

        render_text = self.small_font.render("You are a Blacksmith NPC", True, (255,255,0), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.topleft = Vector2(75, 75)
        self.surface.blit(render_text, render_text_rect)

        render_text = self.small_font.render("Your job is to create weapons for adventurous heros", True, (255,255,0), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.topleft = Vector2(75, 100)
        self.surface.blit(render_text, render_text_rect)

        render_text = self.small_font.render("To create weapons, you must gather resources: ", True, (255,255,0), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.topleft = Vector2(75, 150)
        self.surface.blit(render_text, render_text_rect)

        self.surface.blit(wood_icon, Vector2(630,143))
        self.surface.blit(steel_icon, Vector2(670,143))
        self.surface.blit(string_icon, Vector2(710,143))
        self.surface.blit(titanium_icon, Vector2(750,143))

        render_text = self.small_font.render("Resources are found in Resource Deposits: ", True, (255,255,0), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.topleft = Vector2(75, 200)
        self.surface.blit(render_text, render_text_rect)

        self.surface.blit(wood_deposit, Vector2(630,193))
        self.surface.blit(steel_deposit, Vector2(670,193))
        self.surface.blit(string_deposit, Vector2(710,193))
        self.surface.blit(titanium_deposit, Vector2(750,193))

        render_text = self.small_font.render("Once you have a resource, bring it to the anvil in the middle of the room", True, (255,255,0), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.topleft = Vector2(75, 250)
        self.surface.blit(render_text, render_text_rect)

        render_text = self.small_font.render("The anvil will store your items until you are ready to use them", True, (255,255,0), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.topleft = Vector2(75, 275)
        self.surface.blit(render_text, render_text_rect)

        render_text = self.small_font.render("Heroes will create tasks for you", True, (255,255,0), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.topleft = Vector2(75, 325)
        self.surface.blit(render_text, render_text_rect)

        render_text = self.small_font.render("Once you have all the materials collected in the anvil, press SPACE to smith their weapon", True, (255,255,0), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.topleft = Vector2(75, 350)
        self.surface.blit(render_text, render_text_rect)

        render_text = self.small_font.render("Smith as many weapons as possible in 60 seconds to beat your high score", True, (255,255,0), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.topleft = Vector2(75, 400)
        self.surface.blit(render_text, render_text_rect)

        render_text = self.small_font.render("Use WASD to move, E to interact, SPACE to smith", True, (255,255,0), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.topleft = Vector2(75, 400)
        self.surface.blit(render_text, render_text_rect)

        render_text = self.normal_font.render("Good Luck!", True, (255,255,255), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 500
        )
        self.surface.blit(render_text, render_text_rect)

        render_text = self.small_font.render("Press \"W\" to Start", True, (255,255,0), self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(
            self.surface.get_size()[0] / 2, 550
        )
        self.surface.blit(render_text, render_text_rect)