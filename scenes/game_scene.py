"""
Main Game scene
"""

import pygame
import objects
import random
from base_scene import BaseScene
from pygame.locals import *

meteorTypes = ['big1', 'big2', 'big3', 'big4', 'med1', 'med2', 'small1', 'small2', 'tiny1', 'tiny2']
meteorColors = ['Brown', 'Grey']

METEOR_RATE = 500
SIZES = {
    'big' : (80,80),
    'med' : (50,50),
    'small' : (30,30),
    'tiny' : (15,15)
}

def sign(x):
    if x < 0:
        return -1
    return 1

def findCollidePoint(sprite1, sprite2):
    x1, y1 = sprite1.rect.center
    r1 = sprite1.rect.width/2
    x2, y2 = sprite2.rect.center
    r2 = sprite2.rect.width/2
    d = r1+r2
    return ((r2*x1+r1*x2)/d, (r2*y1 + r1*y2)/d)

class GameScene(BaseScene):
    def __init__(self):
        self.screenSize = pygame.display.get_surface().get_size()
        self.backgroundSprites = pygame.sprite.RenderPlain()
        self.meteorSprites = pygame.sprite.RenderPlain()
        self.playerSprites = pygame.sprite.RenderPlain()
        self.bulletSprites = pygame.sprite.RenderPlain()
        self.explosionSprites = pygame.sprite.RenderPlain()
        self.visualSprites = pygame.sprite.RenderPlain()

        # Background Sprite
        self.backgroundSprite = objects.BackgroundSprite(image='./assets/redux/Backgrounds/blue.png')
        self.backgroundSprites.add(self.backgroundSprite)

        # Add Life Bar
        self.life = objects.LifeSprite(3, './assets/redux/PNG/UI/playerLife1_blue.png')
        self.life.rect.topleft = (10,10)
        self.visualSprites.add(self.life)

        # Add Score
        self.score = objects.ScoreSprite(0)
        self.visualSprites.add(self.score)

        # Player
        self.player = objects.PlayerSprite(0,-1,1, self.bulletSprites)
        self.playerSprites.add(self.player)

        # Health
        self.health = objects.HealthBarSprite((300,15), 'HEALTH', color=(200, 100, 150, 150))
        self.health.rect.topleft = (10, self.screenSize[1]-50)
        self.visualSprites.add(self.health)

        # Shield
        self.shield = objects.HealthBarSprite((300, 15), 'SHIELD', 100, color=(255, 200, 50, 150), flip=True)
        self.shield.rect.topleft = (self.screenSize[0] - 310, self.screenSize[1]-50)
        self.visualSprites.add(self.shield)

        self.lastMeteorAdded = pygame.time.get_ticks()
        objects.loadExplosionImages()

    def draw(self, timeDelta):
        screen = pygame.display.get_surface()
        self.backgroundSprites.draw(screen)
        self.meteorSprites.draw(screen)
        self.playerSprites.draw(screen)
        self.bulletSprites.draw(screen)
        self.explosionSprites.draw(screen)
        self.visualSprites.draw(screen)

    def update(self, timeDelta):
        self.meteorSprites.update()
        self.bulletSprites.update()
        self.explosionSprites.update()
        self.playerSprites.update()
        self.addMeteor()
        collidedSprites = pygame.sprite.spritecollide(self.player, self.meteorSprites, True, pygame.sprite.collide_circle)
        if len(collidedSprites) > 0:
            self.player.blinkShield()
            for sprite in collidedSprites:
                pos = findCollidePoint(self.player, sprite)
                pointSprite = objects.ExplosionSprite(pos)
                self.explosionSprites.add(pointSprite)
        collidedSprites = pygame.sprite.groupcollide(self.meteorSprites, self.bulletSprites, True, True, pygame.sprite.collide_circle)
        for key, value in collidedSprites.iteritems():
            pos = findCollidePoint(key, value[0])
            pointSprite = objects.ExplosionSprite(key.pos, size=SIZES[key.type[:-1]], vel=key.vel)
            self.explosionSprites.add(pointSprite)
            add_score = 10 * len(value)
            self.score.addScore(add_score)

    def addMeteor(self):
        screenSize = pygame.display.get_surface().get_size()
        if pygame.time.get_ticks() - self.lastMeteorAdded < METEOR_RATE:
            return

        pos = (random.randint(-200, screenSize[1]+200), random.randint(-200, -100))
        vel = (sign(screenSize[0]/2-pos[0]) * (random.randint(0, 5)), random.randint(0, 10))
        # pos = (100, 100)
        # vel = (0, 5)
        type = random.sample(meteorTypes, 1)[0]
        color = random.sample(meteorColors, 1)[0]
        rot = random.randint(1,10)
        meteor = objects.Meteor(type, color, pos, vel, rot)
        self.meteorSprites.add(meteor)
        # print(type, color, pos, vel)
        self.lastMeteorAdded = pygame.time.get_ticks()
