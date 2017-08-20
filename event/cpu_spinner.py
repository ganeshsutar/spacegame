"""
CPU Spinner Controller
"""

from event import TickEvent, QuitEvent
import pygame

class CPUSpinnerController:
    def __init__(self, evtManager, screenSize, fpsLimit):
        self.keepGoing = True
        self.clock = pygame.time.Clock()
        self.fpsLimit = fpsLimit
        self.screenSize = screenSize
        self.evtManager = evtManager
        pygame.init()
        pygame.display.set_mode(self.screenSize)
        pygame.display.set_caption('Spaceflight')
        pygame.font.init()

    def run(self):
        while self.keepGoing:
            timeDeltaInMillis = self.clock.tick(self.fpsLimit)
            event = TickEvent(timeDeltaInMillis)
            self.evtManager.raiseEvent(event)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.evtManager.raiseEvent(QuitEvent())
    
    def notify(self, event):
        if isinstance(event, QuitEvent):
            self.keepGoing = False
