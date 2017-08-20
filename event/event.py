"""
This is the superclass of all the events
"""

class Event:
    def __init__(self):
        self.name = 'Generic Event'

class TickEvent:
    def __init__(self, timeDeltaInMillis = 0.1):
        self.name = 'TickEvent'
        self.timeDeltaInMillis = timeDeltaInMillis

class QuitEvent:
    def __init__(self):
        self.name = 'QuitEvent'
