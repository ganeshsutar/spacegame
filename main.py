#! /usr/bin/python

import pygame
import event
import scenes

def main():
    evtManager = event.EventManager()
    spinner = event.CPUSpinnerController(evtManager, (640, 480), 60)
    pygameView = event.PyGameView(scenes.BaseScene())

    evtManager.registerListener(spinner)
    evtManager.registerListener(pygameView)

    titleScene = scenes.TitleScene()
    pygameView.pushScene(titleScene)

    spinner.run()

if __name__ == "__main__":
    main()
