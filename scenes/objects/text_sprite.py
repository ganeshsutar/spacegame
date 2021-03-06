"""
Text Sprite
"""

import pygame

class TextSprite(pygame.sprite.Sprite):
    def __init__(self, text, font, color):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.font = font
        self.color = color
        self.updateImage()

    def updateImage(self):
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
    
    def setText(self, text):
        self.text = text
        self.updateImage()
    
    def setFont(self, font):
        self.font = font
        self.updateImage()
    
    def setColor(self, color):
        self.color = color
        self.updateImage()

