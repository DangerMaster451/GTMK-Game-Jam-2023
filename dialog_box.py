import pygame

class Dialog_Box():
    def __init__(self, window:pygame.surface.Surface, text:str, text_color:tuple[int,int,int], text_bg_color:tuple[int,int,int]):
        self.window = window

        self.text = text
        self.font = pygame.font.Font("Assets/Fonts/PixelFont.ttf", 48)
        self.display_text = self.font.render(text, True, text_color, text_bg_color)
        self.display_text_rect = self.display_text.get_rect()
        self.display_text_rect.topleft = (50,50)

        size = (self.window.get_size()[0]-100, 250)
        self.render_position = (50, self.window.get_size()[1]/2+size[1]/2)
        self.dialog_surface = pygame.surface.Surface(size)

    def render(self) -> None:
        self.dialog_surface.fill("black")
        self.dialog_surface.blit(self.display_text, self.display_text_rect)

        
        self.window.blit(self.dialog_surface, self.render_position)
        