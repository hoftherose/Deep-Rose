from p5 import *
import random as rdm
import math

def setup():
    global window, grid, snake
    size(630, 480)
    background(51)
    grid = Grid(window)
    snake = Snake()

def draw():
    global grid,snake
    KeyPressed()
    background(255,255,255)
    grid.draw()
    snake.update()

def KeyPressed():
    global snake, window
    if key == 65361 and not snake.direction == "EAST": snake.direction = "WEST"
    elif key == 65363 and not snake.direction == "WEST": snake.direction = "EAST"
    elif key == 65362 and not snake.direction == "SOUTH": snake.direction = "NORTH"
    elif key == 65364 and not snake.direction == "NORTH": snake.direction = "SOUTH"
    elif key == "ESCAPE": 
        fill(0,0,255)
        fontsize(50)
        text("paused",window.width//2,window.height//2)
        fontsize(20)
        text("press any key to continue",window.width//2,(window.height//2)-55)
    else:
        print("hi")

class Grid:
    def __init__(self,window):
        self.width = window.width
        self.height = window.height
        self.squares = []
        r,c=0,0
        for x in range(0,self.width,30):
            r = 0
            c += 1
            for y in range(0,self.height,30):
                fill(255)
                self.squares.append(square(x,y,r,c))
                r += 1
        self.respawn()

    def draw(self):
        for i in self.squares:
            i.draw()

    def respawn(self): 
        rdm.choice(self.squares).apple = True

class square:
    def __init__(self,x,y,r,c):
        self.x,self.y,self.r,self.c = x,y,r,c
        self.snake = False
        self.apple = False

    def draw(self):
        if self.snake: fill(0,255,0)
        elif self.apple: fill(255,0,0)
        else: fill(51)
        rect((self.x,self.y),29,29)

class Snake:
    def __init__(self):
        self.headx = int(rdm.randrange(0,21))
        self.heady = int(rdm.randrange(0,16))
        self.direction = rdm.choice(["NORTH","EAST","SOUTH","WEST"])
        self.coords = []
        self.length = 5

    def update(self):
        global grid

        #movement
        if self.direction == "NORTH":
            self.heady += 1
        if self.direction == "SOUTH":
            self.heady -= 1            
        if self.direction == "EAST":
            self.headx += 1
        if self.direction == "WEST":
            self.headx -= 1    

        #wrapping
        if self.headx > 21:
            self.headx = 1
        if self.headx < 1:
            self.headx = 21
        if self.heady > 15:
            self.heady = 0
        if self.heady < 0:
            self.heady = 15

        if [self.headx,self.heady] in self.coords:
            exit()

        self.coords.insert(0,[self.headx,self.heady])
        end = None
        if len(self.coords) > self.length:
            end = self.coords.pop()

        #setting and unsetting snaketiles
        for i in grid.squares:
            if i.r == self.heady and i.c == self.headx: i.snake = True
            if end != None:
                if i.r == end[1] and i.c == end[0]:
                    i.snake = False
            if i.apple and i.r == self.heady and i.c == self.headx:
                i.apple = False
                grid.respawn()
                self.length += 1

run()
