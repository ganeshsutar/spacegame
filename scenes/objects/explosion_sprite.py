"""
Explosion Sprite for the game
"""

import pygame
from .vector import Vec2d

vec = Vec2d
basePath = './assets/smokeParticleAssets/PNG/%s/%s%02d.png'
explosionBlackFiles = [basePath % ('BlackSmoke', 'blackSmoke', i) for i in range(12)]
explosionGoldFiles = [basePath % ('Explosion', 'explosion', i) for i in range(9)]
explosionFlashFiles = [basePath % ('Flash', 'flash', i) for i in range(9)]

explosionGold = None
explosionBlack = None
explosionFlash = None

RATE = 50

def loadExplosionImages():
    global explosionGold, explosionBlack, explosionFlash
    if explosionGold == None:
        explosionGold = list(map(lambda x: pygame.image.load(x).convert_alpha(), explosionGoldFiles))
    if explosionBlack == None:
        explosionBlack = list(map(lambda x: pygame.image.load(x).convert_alpha(), explosionBlackFiles))
    if explosionFlash == None:
        explosionFlash = list(map(lambda x: pygame.image.load(x).convert_alpha(), explosionFlashFiles))


class ExplosionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, size = (50,50), vel=(0,0)):
        pygame.sprite.Sprite.__init__(self)

        self.idx = 0
        self.pos = vec(pos)
        self.vel = vec(vel)
        self.size = size
        self.lastUpdated = pygame.time.get_ticks()
        self.updateImage()

    def updateImage(self):
        self.image = pygame.Surface(self.size, pygame.SRCALPHA, 32).convert_alpha()
        if self.idx < len(explosionBlack):
            self.image.blit(pygame.transform.scale(explosionBlack[self.idx], self.size), (0,0))
        if self.idx < len(explosionGold):
            self.image.blit(pygame.transform.scale(explosionGold[self.idx], self.size), (0,0))
        if self.idx < len(explosionFlash):
            self.image.blit(pygame.transform.scale(explosionFlash[self.idx], (self.size[0]/2, self.size[1]/2)), (self.size[0]/4,self.size[1]/4))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.lastUpdated = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.lastUpdated < RATE:
            return
        self.idx += 1
        self.updateImage()
        if self.idx >= 25:
            self.kill()
        self.pos += self.vel
        self.rect.center = self.pos
