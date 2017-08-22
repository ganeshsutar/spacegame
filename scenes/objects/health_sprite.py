"""
Health Bar
"""

import pygame

fontFile = './assets/redux/Bonus/kenvector_future.ttf'

class HealthBarSprite(pygame.sprite.Sprite):
    def __init__(self, size, name, health = 100, color=(200, 200, 200, 150), flip = False):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.imageSize = (size[0], size[1]+30)
        self.color = color
        self.imageFlip = flip
        self.image = pygame.Surface(size, pygame.SRCALPHA, 32).convert_alpha()
        self.rect = self.image.get_rect()
        self.health = health
        self.font = pygame.font.Font(fontFile, 10)
        self.updateImage()

    def setHealth(self, health):
        self.health = health
        self.updateImage()

    def updateImage(self):
        self.image = pygame.Surface(self.imageSize, pygame.SRCALPHA, 32).convert_alpha()
        width = int(self.imageSize[0]/100)
        rectWidth = int(self.imageSize[0]/100 * 0.75)

        for i in range(self.health):
            rect = pygame.Rect(i*width, 25, rectWidth, self.imageSize[1]-30)
            pygame.draw.rect(self.image, self.color, rect)
        # pygame.draw.rect(self.image, (0,0,0), self.rect, 1)

        textSurface = self.font.render('%s: %d' % (self.name, self.health), True, self.color)
        if self.imageFlip:
            textSurface = pygame.transform.flip(textSurface, True, False)

        self.image.blit(textSurface, (0,10))

        if self.imageFlip:
            self.image = pygame.transform.flip(self.image, True, False)
