"""
Meteor
"""

import pygame
from .vector import Vec2d

vec = Vec2d

# meteorTypes = ['big1', 'big2', 'big3', 'big4', 'med1', 'med2', 'small1', 'small2', 'tiny1', 'tiny2']
# meteorColors = ['Brown', 'Grey']
# metors = ['./assets/spaceArt/redux/PNG/Meteros/meteor%s_%s.png' % (color, type) for type in meteorTypes for color in meteorColors]

class Meteor(pygame.sprite.Sprite):
    def __init__(self, type, color, pos, vel, rot):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.color = color # F:/git-projects/spacegame/assets/redux/PNG/Meteors/meteorBrown_big1.png
        self.imageFilename = './assets/redux/PNG/Meteors/meteor%s_%s.png' % (color, type)
        self.originalImage = pygame.image.load(self.imageFilename)
        self.image = self.originalImage
        self.rect = self.image.get_rect()

        self.pos = vec(pos[0],pos[1])
        self.vel = vec(vel[0],vel[1])
        self.rot = rot
        self.rotation = self.rot
        self.rect.center = self.pos

    def rotate(self):
        """Rotate the sprite about its center"""
        self.rotation = (self.rotation + self.rot) % 360
        rot_image = pygame.transform.rotate(self.originalImage, self.rotation)
        rot_rect = rot_image.get_rect(center=self.rect.center)
        # pygame.draw.circle(rot_image, (255,255,255, 150), rot_image.get_rect().center, rot_image.get_rect().width/2, 2 )
        self.image, self.rect = rot_image, rot_rect

    def update(self):
        screenSize = pygame.display.get_surface().get_size()
        if self.pos.x < -500 or self.pos.x > screenSize[0] + 500:
            self.kill()
        if self.pos.y < -500 or self.pos.y > screenSize[1] + 500:
            self.kill()

        self.rotate()
        self.pos += self.vel
        self.rect.center = self.pos
