import pygame

class orderBar():
    def __init__(self, window, color):
        self.color = color
        self.window = window
        orderBar_surface = pygame.surface.Surface((280,720))
        orderBar_surface.fill(color)
        orderBar_rect = orderBar_surface.get_rect()
        self.window.blit(orderBar_surface, orderBar_rect)
class sideBar():
    def __init__(self, window, color):
        self.color = color
        self.window = window
        sideBar_surface = pygame.surface.Surface((280,720))
        sideBar_surface.fill(color)
        sideBar_rect = sideBar_surface.get_rect(topleft=(1000, 0))
        self.window.blit(sideBar_surface, sideBar_rect)
        
