"""
Laser 
"""

import pygame
import pygame.math

vec = pygame.math.Vector2

laserImage = './assets/redux/PNG/Lasers/laserBlue01.png'

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, vel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(laserImage).convert_alpha()
        self.rect = self.image.get_rect()
        
        self.pos = vec(pos[0], pos[1])
        self.vel = vec(vel[0], vel[1])
        self.rect.center = self.pos
    
    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        if self.pos.y < -100:
            self.kill()


