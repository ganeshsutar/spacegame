"""
Sprite that holds background
"""

import pygame

class BackgroundSprite(pygame.sprite.Sprite):
    def __init__(self, fill):
        pygame.sprite.Sprite.__init__(self)
        screenSize = pygame.display.get_surface().get_size()
        self.image = pygame.Surface(screenSize)
        self.image.fill(fill)
        self.rect = self.image.get_rect()

