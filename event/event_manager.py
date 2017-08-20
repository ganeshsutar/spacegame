"""
Event manager to handle all the events
"""

class EventManager:
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()
    
    def registerListener(self, listener):
        self.listeners[listener] = 1
    
    def unregisterListener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]
    
    def raiseEvent(self, event):
        for listener in self.listeners.keys():
            listener.notify(event)
