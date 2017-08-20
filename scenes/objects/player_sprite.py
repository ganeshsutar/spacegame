"""
Main Player
"""
import pygame

idleImage = './assets/spaceArt/player.png'
leftImage = './assets/spaceArt/playerLeft.png'
rightImage = './assets/spaceArt/playerRight.png'
damagedImage = './assets/spaceArt/playerDamaged.png'
shieldImage = './assets/spaceArt/shield.png'


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, hasShield = True):
        pygame.sprite.Sprite.__init__(self)
        self.playerRectSize = (150,150)
        self.state = 'IDLE'
        self.hasShield = hasShield

        self.idle = pygame.image.load(idleImage).convert_alpha()
        self.left = pygame.image.load(leftImage).convert_alpha()
        self.right = pygame.image.load(rightImage).convert_alpha()
        self.damaged = pygame.image.load(damagedImage).convert_alpha()
        self.shield = pygame.image.load(shieldImage).convert_alpha()
        self.rect = pygame.Rect(0,0,0,0)

        self.updateImage()
        self.setCenter()
    
    def setState(self, newState):
        self.state = newState
        self.updateImage()
    
    def updateImage(self):
        topleft = self.rect.topleft
        self.image = pygame.Surface(self.playerRectSize, pygame.SRCALPHA, 32).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        if self.state == 'IDLE':
            self.blitAtCenter(self.idle, 20)
        elif self.state == 'LEFT':
            self.blitAtCenter(self.left, 20)
        elif self.state == 'RIGHT':
            self.blitAtCenter(self.right, 20)
        elif self.state == 'DAMAGED':
            self.blitAtCenter(self.damaged, 20)
        
        if self.hasShield:
            self.blitAtCenter(self.shield)

    def blitAtCenter(self, drawImage, yOffset = 0):
        baseSize = self.image.get_size()
        drawSize = drawImage.get_size()
        topLeftPos = (baseSize[0]/2-drawSize[0]/2, baseSize[1]/2-drawSize[1]/2 + yOffset)
        self.image.blit(drawImage, topLeftPos)
    
    def setCenter(self):
        screenSize = pygame.display.get_surface().get_size()
        imageSize = self.image.get_size()
        self.rect.topleft = (screenSize[0]/2-imageSize[0]/2, screenSize[1]-imageSize[1])
