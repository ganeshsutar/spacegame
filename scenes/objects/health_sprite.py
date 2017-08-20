"""
Health Bar
"""

import pygame

class HealthBarSprite(pygame.sprite.Sprite):
    def __init__(self, size, health = 100, color=(200, 200, 200), flip = False):
        pygame.sprite.Sprite.__init__(self)
        self.imageSize = size
        self.color = color
        self.imageFlip = flip
        self.image = pygame.Surface(size, pygame.SRCALPHA, 32).convert_alpha()
        self.rect = self.image.get_rect()
        self.health = health
        self.updateImage()
    
    def updateImage(self):
        self.image = pygame.Surface(self.imageSize, pygame.SRCALPHA, 32).convert_alpha()
        width = int(self.imageSize[0]/100)
        rectWidth = int(self.imageSize[0]/100 * 0.75)

        for i in range(self.health):
            rect = pygame.Rect(i*width, 0, rectWidth, self.imageSize[1])
            pygame.draw.rect(self.image, self.color, rect)
        # pygame.draw.rect(self.image, (0,0,0), self.rect, 1)

        if self.imageFlip:
            self.image = pygame.transform.flip(self.image, True, False)



