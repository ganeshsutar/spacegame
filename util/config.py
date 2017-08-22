"""
Hold the configuration
"""

from ConfigParser import ConfigParser
from ast import literal_eval

def loadConfiguration(filename):
    configParser = ConfigParser()
    configParser.read(filename)
    config = Configuration()
    config.width = literal_eval(configParser.get('display', 'width'))
    config.height = literal_eval(configParser.get('display', 'height'))
    return config

class Configuration:
    def __init__(self):
        self.width = 640
        self.height = 480
        self.fpsLimit = 60
    
    def getScreenSize(self):
        return (self.width, self.height)
    
