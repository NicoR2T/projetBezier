#!/usr/bin/env python3


from tkinter import *
from test import *

class Game:
    def __init__(self, gameWidth, gameHeight):
        self.root = Tk()
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight
        self.gameWindow()

        self.ship = Ship(self.canvas, x=self.gameWidth / 2,y=self.gameHeight / 2, width=50, height=50, turnspeed=10, acceleration=5)
        self.root.bind('<Left>', self.ship.rotate)
        self.root.bind('<Right>', self.ship.rotate)
        self.root.bind('<Up>', self.ship.accel)
        self.root.bind('<Down>', self.ship.accel)

        self.root.mainloop()

    def gameWindow(self):
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=YES)

        self.canvas = Canvas(self.frame,width=self.gameWidth, height=self.gameHeight, bg="black", takefocus=1)
        self.canvas.pack(fill=BOTH, expand=YES)     

asteroids = Game(600,600)