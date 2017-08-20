"""
Sprite that holds background
"""

import pygame

class BackgroundSprite(pygame.sprite.Sprite):
    def __init__(self, fill = (255,255,255), image=''):
        pygame.sprite.Sprite.__init__(self)
        screenSize = pygame.display.get_surface().get_size()
        self.image = pygame.Surface(screenSize)
        self.rect = self.image.get_rect()
        if image != '':
            self.setImage(image, screenSize)
        else:
            self.setFill(fill)

    def setImage(self, image, screenSize):
        image = pygame.image.load(image)
        imageSize = image.get_size()
        for x in range(screenSize[0]/imageSize[0] + 1):
            for y in range(screenSize[1]/imageSize[1] + 1):
                self.image.blit(image, (x*imageSize[0],y*imageSize[1]))
    
    def setFill(self, fill):
        self.image.fill(fill)
