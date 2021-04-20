from graphics import *
from random import *

#Creating the window
win = GraphWin('SNAKEY SNAKE', 800, 985)
win.setBackground('black')

#Creating the text that will be dislplayed
title = Text(Point(400, 150), "S N A K E Y  S N A K E")
title.setFace('courier')
title.setSize(36)
title.setStyle("bold italic")
title.setTextColor("deeppink")
title.draw(win)

#Score
theScore = 0
score = Text(Point(400, 200), "S C O R E :  " + str(theScore))
score.setFace('courier')
score.setSize(16)
score.setStyle("bold italic")
score.setTextColor('orchid')
score.draw(win)

#Walls
walls = Rectangle(Point(50, 350), Point(750, 950))
walls.setFill('silver')
walls.setOutline('dimgrey')
walls.draw(win)

#Where the game is taking place
gameBoard = Rectangle(Point(60, 360), Point(740, 940))
gameBoard.setFill('yellowgreen')
gameBoard.setOutline('black')
gameBoard.draw(win)

#Creating square grid in Game Board
def Cuadricula(GRID, SIZE):
    lines = int(GRID/SIZE)
    x1 = 80
    y1 = 380
    for i in range(0, lines):
        hLine = Line(Point(60, y1), Point(740, y1))
        yLine = Line(Point(x1, 360), Point(x1, 940))
        hLine.draw(win)
        yLine.draw(win)
        x1 = x1 + SIZE
        y1 = y1 + SIZE

def spawnSnake(snake, size):
    for i in range(size):
        snake[i] = Rectangle(Point(100, 400), Point(120, 420))
        snake[i].setFill('red')
        snake[i].setOutline('black')
        snake[i].draw(win)

def growSnake(snake, size):
    size += 1
    snake.append(snake[0].clone())


def moveSnake(snake, size, direction, win):
    tiles = size -1 
    snake[tiles].undraw()
    while tiles > 0:
        snake[tiles] = snake[tiles - 1]
        tiles -= 1
    snake[0] = snake[1].clone()
    if direction == 1:
        snake[0].move(0, 20)
    elif direction == 2:
        snake[0].move(20, 0)
    elif direction == 3:
        snake[0].move(-20, 0)
    elif direction == 4:
        snake[0].move(0, -20)
    snake[0].draw(win)



def main():
    #Defining snake and snake size
    sSize = 1
    snake = [0] * sSize

    #Defining snake direction: 1 = dowm, 2 = right, 3 = up, 4 = left. 
    #By default is set to 1.
    direction = 1
    Cuadricula(680, 20)
    spawnSnake(snake, sSize)



    win.getKey()
    win.close()

main()

