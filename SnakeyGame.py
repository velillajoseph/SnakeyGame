from graphics import *
from random import *


class Snake:
    #Creating the window
    win = GraphWin('SNAKEY SNAKE', 800, 985)
    win.setBackground('black')

    #Defining snake and snake size
    size = 2
    snake = [0] * size
    #Define apple 
    apple = Rectangle(Point(0, 0), Point(0, 0))

    GameOver = Text(Point(300,50),"Game Over. Press any key to exit...")

    theScore = 0

    def setSize(_size):
        Snake.size = _size

    def getSize():
        return Snake.size

    def setSnake(_snake):
        Snake.snake = _snake

    def getSnake():
        return Snake.snake

    def setApple(_apple):
        Snake.apple = _apple

    def getApple():
        return Snake.apple

    #Creates the text that will be dislplayed
    def Title(self):
        title = Text(Point(400, 150), "S N A K E Y  S N A K E")
        title.setFace('courier')
        title.setSize(36)
        title.setStyle("bold italic")
        title.setTextColor("deeppink")
        title.draw(self.win)

    #Display Score
    def Score(self):
        
        score = Text(Point(400, 200), "S C O R E :  " + str(self.theScore))
        score.setFace('courier')
        score.setSize(16)
        score.setStyle("bold italic")
        score.setTextColor('orchid')
        score.draw(self.win)

    #Display How to play
    def HTP(self):
        howToPlay = Text(Point(400, 270), "W - UP\nA - LEFT\nS - DOWN\nD - RIGHT\nESC - END GAME")
        howToPlay.setFace('courier')
        howToPlay.setSize(12)
        howToPlay.setStyle("bold italic")
        howToPlay.setTextColor('mediumorchid')
        howToPlay.draw(self.win)

    #Draw Walls
    def Walls(self):
        walls = Rectangle(Point(50, 350), Point(750, 950))
        walls.setFill('silver')
        walls.setOutline('dimgrey')
        walls.draw(self.win)

    #Draws Where the game is taking place
    def GameBoard(self):
        gameBoard = Rectangle(Point(60, 360), Point(740, 940))
        gameBoard.setFill('yellowgreen')
        gameBoard.setOutline('black')
        gameBoard.draw(self.win)

    #Creating square grid in Game Board
    def Cuadricula(GRID, SIZE, self):
        lines = int(GRID/SIZE)
        x1 = 80
        y1 = 380
        for i in range(0, lines):
            hLine = Line(Point(60, y1), Point(740, y1))
            yLine = Line(Point(x1, 360), Point(x1, 940))
            hLine.draw(self.win)
            yLine.draw(self.win)
            x1 = x1 + SIZE
            y1 = y1 + SIZE


    def spawnSnake(self):
        snake = self.getSnake()
        for i in range(self.getSize()):
            snake[i] = Rectangle(Point(100, 400), Point(120, 420))
            snake[i].setFill('grey')
            snake[i].setOutline('black')
            snake[i].draw(self.win)
            self.setSnake(snake)


    def moveSnake(direction, self):
        snake = self.getSnake()
        tiles = self.getSize() - 1 
        snake[tiles].undraw()
        while tiles > 0:
            snake[tiles] = snake[tiles - 1]
            tiles -= 1
            snake[0] = snake[0].clone()
            if direction == 1:
                snake[0].move(0, 20)
                snake[0].draw(self.win)
                self.setSnake(snake)
            elif direction == 2:
                snake[0].move(20, 0)
                snake[0].draw(self.win)
                self.setSnake(snake)
            elif direction == 3:
                snake[0].move(-20, 0)
                snake[0].draw(self.win)
                self.setSnake(snake)
            elif direction == 4:
                snake[0].move(0, -20)
                snake[0].draw(self.win)
                self.setSnake(snake)

    def growSnake(self):
        size = self.getSize() + 1
        snake = self.getSnake()
        snake.append(snake[0].clone())
        self.setSize(size)
        self.setSnake(snake)

    def Collisions(self):
        collided = False
        snake = self.getSnake()
        max_x1 =  snake[0].getP1().getX()
        max_x2 = snake[0].getP2().getX()
        max_y1 = snake[0].getP1().getY()
        max_y2 = snake[0].getP2().getY()
        center_x = snake[0].getCenter().getX()
        center_y = snake[0].getCenter().getY()

        if(max_x1 < 100 or max_x2 > 700 or max_y1 < 400 or max_y2 > 900):
            collided = True
            return collided

        elif((center_x == self.getApple().getCenter().getX()) and (center_y == self.getApple().getCenter().getY())):
            self.growSnake(Snake)
            self.spawnApple(Snake)
            print("Apple collision")
            return collided
        for j in range(1, Snake.getSize()):
            if (center_x == snake[j].getCenter().getX() and center_y == snake[j].getCenter().getY()):
                return collided

    def gameOver(self):
        
        self.GameOver.setOutline("white")
        self.GameOver.setSize(16)
        self.GameOver.draw(self.win)

    def spawnApple(self):
        x = randint(0, 32) * 20
        y = randint(0, 27) * 20
        apple = self.getApple()
        try:
            apple.undraw()
        except:
            print('\nThere is no apple to delete')

        anApple = Rectangle(Point(60 + x, 380 + y), Point(80 + x, 400 + y))
        self.setApple(anApple)
        anApple.setFill('red')
        anApple.setOutline('black')
        anApple.draw(self.win)

    
def main():
    

    #  Validates game state false - playing / true - gameover
    state = False

    #Defining snake direction: 1 = dowm, 2 = right, 3 = up, 4 = left. 
    #By default is set to 1.
    direction = 1
    
    #object from class
    s = Snake
    #Call functions to display window
    s.Title(s)
    s.Score(s)
    s.HTP(s)
    s.Walls(s)
    s.GameBoard(s)
    s.Cuadricula(680, 20, s)
    s.spawnSnake(s)
    s.spawnApple(s)

    while(not state):
        key = s.win.checkKey()
        time.sleep(0.12)
        if(s.Collisions(s) == True):
            s.gameOver(s)
            state = True
            #s.gameOver(s)
        if(key == 'w'):
            direction = 4
            s.moveSnake(direction, s)
        elif(key == 'a'):
            direction = 3
            s.moveSnake(direction, s)
        elif(key =='s'):
            direction = 1
            s.moveSnake(direction, s)
        elif(key == 'd'):
            direction = 2
            s.moveSnake(direction, s)
        elif(key == 'esc'):
            s.gameOver(s)
        else:
            s.moveSnake(direction, s)
            s.Collisions(s) 
            print(state)
        
    
    s.win.getKey()
    s.win.close()

main()

