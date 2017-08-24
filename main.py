#! /usr/bin/python

import os
import util
import pygame
from scenes import sceneManager, TitleScene, GameScene

def main():
    config = util.loadConfiguration('./config.ini')
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (2,25)
    #os.environ['SDL_VIDEO_CENTERED'] = '0'
    pygame.init()
    screen = pygame.display.set_mode(config.getScreenSize())
    pygame.display.set_caption('Space JAM')
    pygame.font.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    scene = GameScene()
    sceneManager.push(scene)

    keepGoing = True
    while keepGoing:
        timeDelta = clock.tick(config.fpsLimit)
        # print('timeDelta: %d, FPS: %d' % (timeDelta, clock.get_fps()))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            else:
                sceneManager.handleEvent(event)
        sceneManager.update(timeDelta)
        sceneManager.draw(timeDelta)
        pygame.display.flip()

if __name__ == "__main__":
    main()
