"""
Main Game scene
"""

import pygame
import objects
from base_scene import BaseScene
from pygame.locals import *

class GameScene(BaseScene):
    def __init__(self):
        self.screenSize = pygame.display.get_surface().get_size()
        self.visualSprites = pygame.sprite.RenderPlain()
        self.backgroundSprites = pygame.sprite.RenderPlain()
        self.collideSprites = pygame.sprite.RenderPlain()

        # Background Sprite
        self.backgroundSprite = objects.BackgroundSprite(image='./assets/spaceArt/Background/starBackground.png')
        self.backgroundSprites.add(self.backgroundSprite)

        # Add Life Bar
        self.life = objects.LifeSprite(3, './assets/spaceArt/life.png')
        self.life.rect.topleft = (10,10)
        self.visualSprites.add(self.life)

        # Add Score
        scoreFont = pygame.font.SysFont('Consolas', 12)
        self.score = objects.ScoreSprite(0, scoreFont, (180, 180, 180))
        self.score.rect.topleft = (self.screenSize[0]-100, 10)
        self.visualSprites.add(self.score)

        # Player
        self.player = objects.PlayerSprite()
        self.collideSprites.add(self.player)

        # Health
        self.health = objects.HealthBarSprite((300,15))
        self.health.rect.topleft = (10, self.screenSize[1]-25)
        self.visualSprites.add(self.health)

        # Shield
        self.shield = objects.HealthBarSprite((300, 15), 90, color=(255, 190, 190), flip=True)
        self.shield.rect.topleft = (self.screenSize[0] - 310, self.screenSize[1]-25)
        self.visualSprites.add(self.shield)
    
    def draw(self, timeDelta):
        screen = pygame.display.get_surface()
        self.backgroundSprites.draw(screen)
        self.collideSprites.draw(screen)
        self.visualSprites.draw(screen)
    
    def update(self, timeDelta):
        pass
    
    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            self.handleKeyboard(event)
    
    def handleKeyboard(self, event):
        if event.key == K_LEFT:
            self.player.setState('LEFT')
        elif event.key == K_RIGHT:
            self.player.setState('RIGHT')
        elif event.key == K_UP:
            self.player.setState('IDLE')
        elif event.key == K_DOWN:
            self.player.setState('DAMAGED')
        elif event.key == K_q:
            self.life.reduceCount()

