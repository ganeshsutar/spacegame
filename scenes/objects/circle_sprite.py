"""
Circle
"""

import pygame

class CircleSprite(pygame.sprite.Sprite):
    def __init__(self, pos, rad):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30, 30], pygame.SRCALPHA, 32).convert_alpha()
        pygame.draw.circle(self.image, (200, 200, 200, 190), (15,15), rad)
        self.rect = self.image.get_rect()
        self.rect.center = pos
