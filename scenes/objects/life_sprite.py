"""
Life Sprite which draw the life
"""

import pygame

class LifeSprite(pygame.sprite.Sprite):
    def __init__(self, startCount, imageFilename):
        pygame.sprite.Sprite.__init__(self)
        self.startCount = startCount
        self.imageFilename = imageFilename
        self.updateImage()
    
    def reduceCount(self):
        if self.startCount == 0:
            return
        self.startCount -= 1
        topleft = self.rect.topleft
        self.updateImage()
        self.rect.topleft = topleft

    def updateImage(self):
        self.lifeImage = pygame.image.load(self.imageFilename).convert_alpha()
        lifeImageSize = [x for x in self.lifeImage.get_size()]
        lifeImageSize[0] = lifeImageSize[0] + 10
        imageSize = (self.startCount * lifeImageSize[0], lifeImageSize[1])
        self.image = pygame.Surface(imageSize, pygame.SRCALPHA, 32).convert_alpha()
        self.rect = self.image.get_rect()
        for i in range(self.startCount):
            self.image.blit(self.lifeImage, (i * lifeImageSize[0], 0))
