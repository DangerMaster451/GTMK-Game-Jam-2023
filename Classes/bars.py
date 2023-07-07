import pygame

class Order_Bar():
    def __init__(self, window, color):
        self.color = color
        self.window = window
        self.orderBar_surface = pygame.surface.Surface((280,720))
        self.orderBar_surface.fill(color)
        self.orderBar_rect = self.orderBar_surface.get_rect()
        
    def render(self):
        self.window.blit(self.orderBar_surface, self.orderBar_rect)
        
class Side_Bar():
    def __init__(self, window, color):
        self.color = color
        self.window = window
        self.sideBar_surface = pygame.surface.Surface((280,720))
        self.sideBar_surface.fill(color)
        self.sideBar_rect = self.sideBar_surface.get_rect(topleft=(1000, 0))
        
    def render(self):
        self.window.blit(self.sideBar_surface, self.sideBar_rect)
        
