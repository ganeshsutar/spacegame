"""
Manages all the scenes
"""

class SceneManager:
    def __init__(self):
        self.scenes = []
    
    def push(self, scene):
        self.scenes.append(scene)
    
    def pop(self):
        return self.scenes.pop()
    
    def peek(self):
        return self.scenes[len(self.scenes)-1]
    
    def draw(self, timeDelta):
        self.peek().draw(timeDelta)
    
    def update(self, timeDelta):
        self.peek().update(timeDelta)
    
    def handleEvent(self, event):
        self.peek().handleEvent(event)
