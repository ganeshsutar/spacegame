"""
Score Sprite
"""

import pygame

class ScoreSprite(pygame.sprite.Sprite):
    def __init__(self, score, font, color, prefix = 'Score: '):
        pygame.sprite.Sprite.__init__(self)
        self.score = score
        self.prefix = prefix + ' %d'
        self.font = font
        self.color = color
        self.updateImage()

    def updateImage(self):
        self.image = self.font.render(self.prefix % (self.score), False, self.color)
        self.rect = self.image.get_rect()
    
    def setPrefix(self, prefix):
        self.prefix = prefix + ' %d'
        self.updateImage()
    
    def setFont(self, font):
        self.font = font
        self.updateImage()
    
    def setColor(self, color):
        self.color = color
        self.updateImage()

    def setScore(self, score):
        self.score = score
        self.updateImage()

