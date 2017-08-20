"""
PyGame View Renderer
"""

from event import TickEvent
import pygame

class PyGameView:
    def __init__(self, baseScene):
        self.scenes = [baseScene]
    
    def pushScene(self, scene):
        self.scenes.append(scene)
    
    def popScene(self):
        return self.scenes.pop()
    
    def peek(self):
        return self.scenes[len(self.scenes)-1]
    
    def notify(self, event):
        if isinstance(event, TickEvent):
            # Draw Scene
            surface = pygame.display.get_surface()
            surface.fill((255,255,255))
            scene = self.peek()
            scene.update(event)
            scene.draw(event)
            pygame.display.flip()
