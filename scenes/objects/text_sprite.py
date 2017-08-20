"""
Text Sprite
"""

import pygame

class TextSprite(pygame.sprite.Sprite):
    def __init__(self, text, font, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(text, True, color)
        self.rect = self.image.get_rect()
