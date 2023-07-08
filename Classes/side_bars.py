import pygame
from pygame.math import Vector2
from random import randint
from Classes.task import Task
from Classes.grid import Grid

class Side_Bar():
    def __init__(self, window, position:Vector2, bg_color):
        self.bg_color = bg_color
        self.window = window
        self.sideBar_surface = pygame.surface.Surface((280,720))
        self.sideBar_surface.fill(self.bg_color)
        self.sideBar_rect = self.sideBar_surface.get_rect(topleft=(position))
        self.normal_font = pygame.font.Font("Assets/Fonts/PixelFont.ttf", 24)
        self.small_font = pygame.font.Font("Assets/Fonts/PixelFont.ttf", 12)

    def display_text(self, text:str, text_color:tuple[int,int,int], position_y:int, small_text=False) -> None:
        if small_text:
            render_text = self.small_font.render(text, True, text_color, self.bg_color)
        else:
            render_text = self.normal_font.render(text, True, text_color, self.bg_color)
        render_text_rect = render_text.get_rect()
        render_text_rect.center = Vector2(self.sideBar_surface.get_size()[0]/2, position_y)
        self.sideBar_surface.blit(render_text, render_text_rect)   

    def display_task(self, task:Task, grid:Grid, text_color, position:Vector2, spacing:int, task_complete:bool) -> None:
        center_x = self.sideBar_surface.get_size()[0]/2
        # Render Weapon Type
        weapon_text = self.normal_font.render(task.weapon_type, True, text_color, self.bg_color)
        weapon_text_rect = weapon_text.get_rect()
        weapon_text_rect.center = Vector2(center_x, position.y)
        self.sideBar_surface.blit(weapon_text, weapon_text_rect)

        # Render Materials Heading
        material_text = self.small_font.render("~ Materials ~", True, text_color, self.bg_color)
        material_text_rect = material_text.get_rect()
        material_text_rect.center = Vector2(center_x, position.y+spacing*1.5)
        self.sideBar_surface.blit(material_text, material_text_rect)

        # Render Material Icons
        for index, material_icon in enumerate(task.material_icons):
            position_x = (self.sideBar_surface.get_size()[0] / (len(task.material_icons)+1) * (index+1)) - material_icon.get_size()[0]/2
            if task.material_names[index] in grid.get_anvil_inventories()[0]:
                completed_material_icon = task.completed_material_icons[index]
                self.sideBar_surface.blit(completed_material_icon, (position_x, position.y+spacing*2))
            else:
                self.sideBar_surface.blit(material_icon, (position_x, position.y+spacing*2))

        if task_complete:
            complete_text = self.small_font.render("Press SPACE to Complete", True, text_color, self.bg_color)
            complete_text_rect = complete_text.get_rect()
            complete_text_rect.center = Vector2(center_x, position.y+spacing*4)
            self.sideBar_surface.blit(complete_text, complete_text_rect)
        
    def render(self):
        self.window.blit(self.sideBar_surface, self.sideBar_rect)

class Left_Bar(Side_Bar):
    def __init__(self, window, position: Vector2, bg_color):
        super().__init__(window, position, bg_color)
    
class Right_Bar(Side_Bar):
    def __init__(self, window, position: Vector2, bg_color):
        super().__init__(window, position, bg_color)
        
