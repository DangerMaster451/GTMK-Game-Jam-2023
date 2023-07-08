import pygame
from pygame.math import Vector2
from random import randint
from Classes.task import Task

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

    def display_task(self, task:Task, text_color, position_y):
        weapon_text = self.font.render(task.weapon_type, True, text_color, self.bg_color)
        weapon_text_rect = weapon_text.get_rect()
        weapon_text_rect.center = Vector2(self.sideBar_surface.get_size()[0]/2, position_y)
        self.sideBar_surface.blit(weapon_text, weapon_text_rect)

        for index, material_icon in enumerate(task.materials):
            position_x = (self.sideBar_surface.get_size()[0] / (len(task.materials)+1) * (index+1)) - material_icon.get_size()[0]/2
            self.sideBar_surface.blit(material_icon, (position_x, position_y+50))

        for index, enchantment_icon in enumerate(task.enchantments):
            position_x = (self.sideBar_surface.get_size()[0] / (len(task.enchantments)+1) * (index+1)) - enchantment_icon.get_size()[0]/2
            self.sideBar_surface.blit(enchantment_icon, (position_x, position_y+100))       
        

    def render(self):
        self.window.blit(self.sideBar_surface, self.sideBar_rect)

class Left_Bar(Side_Bar):
    def __init__(self, window, position: Vector2, bg_color):
        super().__init__(window, position, bg_color)
    
class Right_Bar(Side_Bar):
    def __init__(self, window, position: Vector2, bg_color):
        super().__init__(window, position, bg_color)
        
