"""
Title Scene for the game
"""

from base_scene import BaseScene
from objects import *
import pygame

class TitleScene(BaseScene):
    def __init__(self):
        BaseScene.__init__(self)
        self.font = pygame.font.SysFont('moonhouse', 30)
        self.menuFont = pygame.font.SysFont('Courier New', 20)
        self.gameTitle = TextSprite('SPACE JAM', self.font, (10, 10, 10))
        self.newGame = TextSprite('New Game', self.menuFont, (10, 10, 10))
        self.background = BackgroundSprite((150,150,150))
        self.gameTitle.rect.topleft = (20,20)
        self.newGame.rect.topleft = (70,70)
        self.allsprites = pygame.sprite.OrderedUpdates((self.background, self.gameTitle, self.newGame))
    
    def draw(self, tickEvent):
        screen = pygame.display.get_surface()
        self.allsprites.draw(screen)
    
    def update(self, tickEvent):
        pass
