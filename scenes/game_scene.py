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

def sign(x):
    if x < 0:
        return -1
    return 1

class GameScene(BaseScene):
    def __init__(self):
        self.screenSize = pygame.display.get_surface().get_size()
        self.visualSprites = pygame.sprite.RenderPlain()
        self.backgroundSprites = pygame.sprite.RenderPlain()
        self.collideSprites = pygame.sprite.RenderPlain()

        # Background Sprite
        self.backgroundSprite = objects.BackgroundSprite(image='./assets/redux/Backgrounds/blue.png')
        self.backgroundSprites.add(self.backgroundSprite)

        # Add Life Bar
        self.life = objects.LifeSprite(3, './assets/spaceArt/png/life.png')
        self.life.rect.topleft = (10,10)
        self.visualSprites.add(self.life)

        # Add Score
        self.score = objects.ScoreSprite(99999)
        self.visualSprites.add(self.score)

        # Player
        self.player = objects.PlayerSprite(0,1,1, self.collideSprites)
        self.collideSprites.add(self.player)

        # Health
        self.health = objects.HealthBarSprite((300,15), 'HEALTH', color=(200, 100, 150, 150))
        self.health.rect.topleft = (10, self.screenSize[1]-50)
        self.visualSprites.add(self.health)

        # Shield
        self.shield = objects.HealthBarSprite((300, 15), 'SHIELD', 100, color=(255, 200, 50, 150), flip=True)
        self.shield.rect.topleft = (self.screenSize[0] - 310, self.screenSize[1]-50)
        self.visualSprites.add(self.shield)

        self.lastMeteorAdded = pygame.time.get_ticks()
    
    def draw(self, timeDelta):
        screen = pygame.display.get_surface()
        self.backgroundSprites.draw(screen)
        self.collideSprites.draw(screen)
        self.visualSprites.draw(screen)
    
    def update(self, timeDelta):
        self.collideSprites.update()
        self.addMeteor()
    
    def addMeteor(self):
        screenSize = pygame.display.get_surface().get_size()
        if pygame.time.get_ticks() - self.lastMeteorAdded < METEOR_RATE:
            return
        
        pos = (random.randint(-200, screenSize[1]+200), random.randint(-200, -100))
        vel = (sign(screenSize[0]-pos[0]) * (random.randint(0, 5)), random.randint(0, 10))
        # pos = (100, 100)
        # vel = (0, 5)
        type = random.sample(meteorTypes, 1)[0]
        color = random.sample(meteorColors, 1)[0]
        meteor = objects.Meteor(type, color, pos, vel)
        self.collideSprites.add(meteor)
        # print(type, color, pos, vel)
        self.lastMeteorAdded = pygame.time.get_ticks()

