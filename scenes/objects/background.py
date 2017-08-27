"""
Sprite that holds background
"""

import pygame
from vector import Vec2d
vec = Vec2d

class BackgroundSprite(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.screenSize = pygame.display.get_surface().get_size()
        self.backgroundImage = pygame.image.load(image)
        self.imageSize = self.backgroundImage.get_size()
        self.image = pygame.Surface(self.screenSize)
        self.rect = self.image.get_rect()
        self.pos = vec(0, -2*self.imageSize[1])
        self.vel = vec(0,2)
        self.updateImage()

    def updateImage(self):
        self.image.fill((0,0,0))
        for x in range(self.screenSize[0]/self.imageSize[0] + 1):
            for y in range(-2, self.screenSize[1]/self.imageSize[1] + 3):
                self.image.blit(self.backgroundImage,
                    (self.pos.x + x*self.imageSize[0],self.pos.y + y*self.imageSize[1]))

    def update(self):
        self.pos += self.vel
        if self.pos.y > -self.imageSize[1]:
            self.pos = vec(0, -2 * self.imageSize[1])
        self.updateImage()
