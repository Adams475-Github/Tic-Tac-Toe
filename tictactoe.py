import zellegraphics as zg
import time
import math

runGame = True
PPS = 150
column = int(input("How many rows and columns do you want?"))
row = column
windowSizeX = column * PPS
windowSizeY = column * PPS
board = [['~']*column for i in range(column)]

def drawBoard(row, column, windowSizeX, windowSizeY, PPS):
    global win
    win = zg.GraphWin("Name Jeff", windowSizeX, windowSizeY)

    for i in range(1, row):
        
        line = zg.Line(zg.Point(PPS*i, 0), zg.Point(PPS*i, windowSizeY))
        line.draw(win)
    
    for i in range (1, column):
        
        line = zg.Line( zg.Point(0, PPS*i), zg.Point(windowSizeX, PPS*i) )
        line.draw(win)

def drawX(row, column):
    zg.Line( zg.Point(row * PPS, column * PPS), zg.Point((row + 1) * PPS, (column + 1) * PPS) ).draw(win)
    zg.Line( zg.Point((row + 1) * PPS, column * PPS), zg.Point(row * PPS, (column + 1) * PPS) ).draw(win)

def drawO(row, column):
    center = zg.Point( (row * PPS) + (PPS / 2), (column * PPS) + (PPS / 2))
    zg.Circle(center, PPS / 2).draw(win)

def fillBoard():
    last = 'o'
    for x in range(column):
        for o in range(row):
            if last == 'o':
                drawX(x, o)
                last = 'x'
            else:
                drawO(x, o)
                last = 'o'
last = 'o'
def onClick(point):
    drawNextPiece(point)
    #printBoard()
    checkForWin()

def checkForWin():
    times = 0
    lastColumn = 0
    for x in range(column):
        for y in range(column):
            if board[x][y] == 'x':
                times += 1
                print(board[x][y], end=' ')
            else:
                print(board[x][y], end=' ')
                times = 0
            
            if times >= column:
                winFound('x')
                return
            
        times = 0
        print('')

def winFound(winner):
    print(winner, "WON!")
    
def printBoard():
    for i in range(column):
        for j in range(column):
            print(board[i][j], end='') # Prevents a new line from being created
        print('')
    print('')

def drawNextPiece(point):
    x = point.getX()
    y = point.getY()

    row = (x // PPS)
    column = (y // PPS)
    
    if board[column][row] != '~':
        print('Spot already taken!')
        return

    global last
    if last == 'o': # Draw X
        drawX(row, column)
        del board[column][row] # Remove placeholder
        board[column].insert(row, 'x') # Add 'x'
        last = 'x'
    else: # Draw O
        drawO(row, column)
        del board[column][row] # Remove placeholder
        board[column].insert(row, 'o') # Add 'y'
        last = 'o'
 
def initialize():

    drawBoard(column, row, windowSizeX, windowSizeY, PPS)

    while runGame:
        point = win.getMouse()
        onClick(point)

    win.getMouse()

initialize()