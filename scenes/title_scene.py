"""
Title Scene for the game
"""

from .base_scene import BaseScene
from .objects import *
import pygame
from pygame.locals import *

class TitleScene(BaseScene):
    def __init__(self):
        BaseScene.__init__(self)
        self.fontColor = (180, 180, 180)
        self.background = BackgroundSprite(image='./assets/redux/Backgrounds/black.png')
        self.font = pygame.font.Font('./assets/redux/Bonus/kenvector_future_thin.ttf', 40)
        self.menuFont = pygame.font.Font('./assets/redux/Bonus/kenvector_future.ttf', 20)
        self.gameTitle = TextSprite('SPACE JAM', self.font, self.fontColor)

        self.newGame = TextSprite('New Game', self.menuFont, self.fontColor)
        self.options = TextSprite('Options', self.menuFont, self.fontColor)
        self.exit = TextSprite('Exit', self.menuFont, self.fontColor)
        self.arrow = TextSprite('-', self.menuFont, self.fontColor)

        self.gameTitle.rect.topleft = (20,20)
        self.newGame.rect.topleft = (20,70)
        self.options.rect.topleft = (20,95)
        self.exit.rect.topleft = (20,120)
        self.arrow.rect.topleft = (5,70)
        self.menuSelectIdx = 0

        self.allsprites = pygame.sprite.OrderedUpdates((self.background, self.gameTitle, self.newGame, self.options, self.exit, self.arrow))

    def draw(self, tickEvent):
        screen = pygame.display.get_surface()
        self.allsprites.draw(screen)

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            self.handleKeyEvent(event.key)

    def handleKeyEvent(self, key):
        if key == K_UP and self.menuSelectIdx > 0:
            self.menuSelectIdx -= 1
        elif key == K_DOWN and self.menuSelectIdx < 2:
            self.menuSelectIdx += 1
        elif key == K_RETURN or key == K_KP_ENTER:
            print('Into the rabbit hole')
        self.arrow.rect.topleft = (5, 70 + self.menuSelectIdx * 25)
