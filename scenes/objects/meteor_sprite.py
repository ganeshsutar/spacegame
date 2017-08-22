"""
Meteor
"""

import pygame
import vector

vec = vector.Vec2d

# meteorTypes = ['big1', 'big2', 'big3', 'big4', 'med1', 'med2', 'small1', 'small2', 'tiny1', 'tiny2']
# meteorColors = ['Brown', 'Grey']
# metors = ['./assets/spaceArt/redux/PNG/Meteros/meteor%s_%s.png' % (color, type) for type in meteorTypes for color in meteorColors]

class Meteor(pygame.sprite.Sprite):
    def __init__(self, type, color, pos, vel):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.color = color # F:/git-projects/spacegame/assets/redux/PNG/Meteors/meteorBrown_big1.png
        self.imageFilename = './assets/redux/PNG/Meteors/meteor%s_%s.png' % (color, type)
        self.image = pygame.image.load(self.imageFilename)
        self.rect = self.image.get_rect()

        self.pos = vec(pos[0],pos[1])
        self.vel = vec(vel[0],vel[1])
        self.rect.center = self.pos

    def update(self):
        screenSize = pygame.display.get_surface().get_size()
        if self.pos.x < -500 or self.pos.x > screenSize[0] + 500:
            self.kill()
        if self.pos.y < -500 or self.pos.y > screenSize[1] + 500:
            self.kill()
        
        self.pos += self.vel
        self.rect.center = self.pos

