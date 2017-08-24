"""
Score Sprite
"""

import pygame

class ScoreSprite(pygame.sprite.Sprite):
    def __init__(self, score, prefix = 'Score: '):
        pygame.sprite.Sprite.__init__(self)
        self.score = score
        self.prefix = prefix + ' %d'
        self.font = pygame.font.Font('./assets/redux/Bonus/kenvector_future_thin.ttf', 16)
        self.color = (180,180,180)
        self.updateImage()

    def updateImage(self):
        screenSize = pygame.display.get_surface().get_size()
        self.image = self.font.render(self.prefix % (self.score), False, self.color)
        imageSize = self.image.get_size()
        self.rect = self.image.get_rect()
        self.rect.topleft = (screenSize[0] - self.rect.width - 10, 10)

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

    def addScore(self, score):
        self.score += score
        self.updateImage()
