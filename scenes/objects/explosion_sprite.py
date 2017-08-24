"""
Explosion Sprite for the game
"""

import pygame

basePath = './assets/smokeParticleAssets/PNG/%s/%s%02d.png'
explosionBlackFiles = [basePath % ('Black Smoke', 'blackSmoke', i) for i in range(25)]
explosionGoldFiles = [basePath % ('Explosion', 'explosion', i) for i in range(9)]

explosionGold = None
explosionBlack = None

RATE = 50
SIZE = (70,70)

def loadExplosionImage(filename):
    image = pygame.image.load(filename).convert_alpha()
    return pygame.transform.scale(image, SIZE)

def loadExplosionImages():
    global explosionGold, explosionBlack
    if explosionGold == None:
        explosionGold = map(loadExplosionImage, explosionGoldFiles)
    if explosionBlack == None:
        explosionBlack = map(loadExplosionImage, explosionBlackFiles)

class ExplosionSprite(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.idx = 0
        self.pos = pos
        self.lastUpdated = pygame.time.get_ticks()
        self.updateImage()

    def updateImage(self):
        self.image = pygame.Surface(SIZE, pygame.SRCALPHA, 32).convert_alpha()
        if self.idx < len(explosionBlack):
            self.image.blit(explosionBlack[self.idx], (0,0))
        if self.idx < len(explosionGold):
            self.image.blit(explosionGold[self.idx], (0,0))
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
