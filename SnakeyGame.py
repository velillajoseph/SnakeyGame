from graphics import *
from random import *

#Creating the window
win = GraphWin('SNAKEY SNAKE', 800, 985)
win.setBackground('black')

#Defining snake and snake size
size = 1
snake = [0] * size;

#Define apple 
apple = Rectangle(Point(0, 0), Point(0, 0))

def setSize(_size):
    size = _size

def getSize():
    return size

def setSnake(_snake):
    snake = _snake

def getSnake():
    return snake

def setApple(_apple):
    apple = _apple

def getApple():
    return apple


#Creates the text that will be dislplayed
def Title():
    title = Text(Point(400, 150), "S N A K E Y  S N A K E")
    title.setFace('courier')
    title.setSize(36)
    title.setStyle("bold italic")
    title.setTextColor("deeppink")
    title.draw(win)

#Display Score
def Score():
    theScore = 0
    score = Text(Point(400, 200), "S C O R E :  " + str(theScore))
    score.setFace('courier')
    score.setSize(16)
    score.setStyle("bold italic")
    score.setTextColor('orchid')
    score.draw(win)

#Display How to play
def HTP():
    howToPlay = Text(Point(400, 270), "W - UP\nA - LEFT\nS - DOWN\nD - RIGHT\nESC - END GAME")
    howToPlay.setFace('courier')
    howToPlay.setSize(12)
    howToPlay.setStyle("bold italic")
    howToPlay.setTextColor('mediumorchid')
    howToPlay.draw(win)

#Draw Walls
def Walls():
    walls = Rectangle(Point(50, 350), Point(750, 950))
    walls.setFill('silver')
    walls.setOutline('dimgrey')
    walls.draw(win)

#Draws Where the game is taking place
def GameBoard():
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
    

def spawnSnake():
    snake = getSnake()
    for i in range(size):
        snake[i] = Rectangle(Point(100, 400), Point(120, 420))
        snake[i].setFill('grey')
        snake[i].setOutline('black')
        snake[i].draw(win)
    setSnake(snake)

def growSnake():
    size = getSize() + 1
    snake = getSnake()
    snake.append(snake[0].clone())
    setSize(size)
    setSnake(snake)

def spawnApple():
    x = randint(0, 32) * 20
    y = randint(0, 27) * 20
    try:
        getApple().undraw;
    except:
        print('\nThere is no apple to delete')
    
    anApple = Rectangle(Point(60 + x, 380 + y), Point(80 + x, 400 + y))
    setApple(anApple)
    anApple.setFill('red')
    anApple.setOutline('black')
    anApple.draw(win)


def moveSnake(direction):
    snake = getSnake()
    tiles = getSize() - 1 
    snake[tiles].undraw()
    while tiles > 0:
        snake[tiles] = snake[tiles - 1]
        tiles -= 1
    snake[0] = snake[0].clone()
    if direction == 1:
        snake[0].move(0, 20)
    elif direction == 2:
        snake[0].move(20, 0)
    elif direction == 3:
        snake[0].move(-20, 0)
    elif direction == 4:
        snake[0].move(0, -20)
    snake[0].draw(win)
    setSnake(snake)

def Collisions():
    collided = False
    snake = getSnake()
    max_x1 =  snake[0].getP1().getX()
    max_x2 = snake[0].getP2().getX()
    max_y1 = snake[0].getP1().getY()
    max_y2 = snake[0].getP2().getY()
    center_x = snake[0].getCenter().getX()
    center_y = snake[0].getCenter().getY()

    if(max_x1 < 100 or max_x2 > 700 or max_y1 < 400 or max_y2 > 900):
        collided = True
        return collided

    elif((center_x == getApple().getCenter().getX()) and (center_y == getApple().getCenter().getY())):
        growSnake()
        spawnApple()
        print("Apple collision")
    for j in range(0, size):
        if (center_x == snake[j].getCenter().getX() and center_y == snake[j].getCenter().getY()):
            return collided

def gameOver():
    GameOver = Text(Point(300,50),"Game Over. Press any key to exit...")
    GameOver.setOutline("white")
    GameOver.setSize(16)
    GameOver.draw(win)



def main():
    
    #  Validates game state false - playing / true - gameover
    state = False

    #Defining snake direction: 1 = dowm, 2 = right, 3 = up, 4 = left. 
    #By default is set to 1.
    direction = 1

    #Call functions to display window
    Title()
    Score()
    HTP()
    Walls()
    GameBoard()
    Cuadricula(680, 20)
    spawnSnake()
    spawnApple()

    while(not state):
        key = win.checkKey()
        time.sleep(0.12)
        if(Collisions() == True):
            state = True
            gameOver()
        if(key == 'w'):
            direction = 4
            moveSnake(direction)
        elif(key == 'a'):
            direction = 3
            moveSnake(direction)
        elif(key =='s'):
            direction = 1
            moveSnake(direction)
        elif(key == 'd'):
            direction = 2
            moveSnake(direction)
        else:
            moveSnake(direction)
            Collisions() 
        
    
    win.getKey()
    win.close()

main()

