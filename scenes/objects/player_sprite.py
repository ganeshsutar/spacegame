"""
Main Player
"""
import pygame
import vector
from laser import Laser

PLAYER_ACC = 0.6
PLAYER_FRICTION = 0.12
PLAYER_FIRE_RATE = 100
FPS = 60.0

vec = vector.Vec2d

class PlayerAssets:
    def __init__(self, i, color):
        self.playerAssets = './assets/redux/PNG/playerShip%d_%s.png' % (i, color)
        self.damagesAssets = [ './assets/redux/PNG/Damage/playerShip%d_damage%d.png' % (i, j) for j in range(1,3)]
        self.laserSound = './assets/redux/Bonus/sfx_laser1.ogg'
        self.loaded = False
    
    def load(self):
        self.player = pygame.image.load(self.playerAssets).convert_alpha()
        self.damages = [pygame.image.load(x).convert_alpha() for x in self.damagesAssets]
        self.fireSound = pygame.mixer.Sound(self.laserSound)

playerAssets = [PlayerAssets(i, color) for i in range(1,4) for color in ['blue', 'green', 'orange', 'red']]
shieldAssets = ['./assets/redux/PNG/Effects/shield%d.png' % i for i in range(1,4)]
shields = []

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, player, damage, shield, collideSprite):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.damage = damage
        self.shield = shield
        self.lastFire = pygame.time.get_ticks()
        self.collideSprite = collideSprite
        self.playerRectSize = (150,150)
        self.image = pygame.Surface(self.playerRectSize, pygame.SRCALPHA, 32).convert_alpha()
        self.rect = self.image.get_rect()

        for playerAsset in playerAssets:
            playerAsset.load()
        
        for shieldImage in shieldAssets:
            shields.append(pygame.image.load(shieldImage).convert_alpha())

        self.playerAssets = playerAssets[self.player]

        self.pos = vec(0, 0)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
    
        self.updateImage()
        self.setCenter()
    
    def fire(self):
        currentTime = pygame.time.get_ticks()
        if (currentTime - self.lastFire) < PLAYER_FIRE_RATE:
            return
        laserLeft = Laser((self.pos.x-20, self.pos.y-20), (0, -10))
        laserRight = Laser((self.pos.x+20, self.pos.y-20), (0, -10))
        self.collideSprite.add(laserLeft)
        self.collideSprite.add(laserRight)
        self.playerAssets.fireSound.play()
        self.lastFire = pygame.time.get_ticks()

    def update(self):
        self.acc = vec(0,0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keys[pygame.K_UP]:
            self.acc.y = -PLAYER_ACC
        if keys[pygame.K_DOWN]:
            self.acc.y = PLAYER_ACC
        if keys[pygame.K_b]:
            # print('Total Sprites: %d' % (len(self.collideSprite)))
            self.fire()
            
        self.acc += self.vel * (-PLAYER_FRICTION)
        self.vel += self.acc
        self.pos += (self.vel + 0.5 * self.acc)
        # print(self.acc, self.vel, self.pos)

        screenSize = pygame.display.get_surface().get_size()
        if self.pos.x < 0: self.pos.x = 0
        if self.pos.x > screenSize[0]: self.pos.x = screenSize[0]
        if self.pos.y < 0: self.pos.y = 0
        if self.pos.y > screenSize[1]: self.pos.y = screenSize[1]
        
        self.rect.center = self.pos

    
    def updateImage(self):
        self.image.fill((0,0,0,0))
        self.blitAtCenter(self.playerAssets.player, 20)

        if self.damage != -1:
            self.blitAtCenter(self.playerAssets.damages[self.damage], 20)
        
        if self.shield != -1:
            self.blitAtCenter(shields[self.shield])
        
    def updatePlayer(self, player):
        if 0 < player < len(playerAssets):
            self.player = player
            self.updateImage()
    
    def updateDamage(self, damage):
        if 0 < damage < 4:
            self.damage = damage
            self.updateImage()
    
    def updateShield(self, shield):
        if 0 < shield < 3:
            self.shield = shield
            self.updateImage()

    def blitAtCenter(self, drawImage, yOffset = 0):
        baseSize = self.image.get_size()
        drawSize = drawImage.get_size()
        topLeftPos = (baseSize[0]/2-drawSize[0]/2, baseSize[1]/2-drawSize[1]/2 + yOffset)
        self.image.blit(drawImage, topLeftPos)
    
    def setCenter(self):
        screenSize = pygame.display.get_surface().get_size()
        imageSize = self.image.get_size()
        self.pos = vec(screenSize[0]/2, screenSize[1]-imageSize[1]/2)
        self.rect.center = self.pos
