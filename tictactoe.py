import zellegraphics as zg
import time
import math

runGame = True
PPS = 150
column = int(input("How many rows and columns do you want?"))
row = column
windowSizeX = column * PPS
windowSizeY = column * PPS

board = [[]*column]*column

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
    last = 'y'
    for x in range(column):
        for y in range(row):
            if last == 'y':
                drawX(x, y)
                last = 'x'
            else:
                drawO(x, y)
                last = 'y'
last = 'y'
def onClick(point):
    drawNextPiece(point)
    checkForWin()

def checkForWin():
    for i in range(column):
        for j in range(column):
            print(board[i][j], end='')
        print('')

def drawNextPiece(point):
    x = point.getX()
    y = point.getY()

    row = -1
    total = 0
    while total < x:
        total += PPS
        row += 1
    column = -1
    total = 0
    while total < y:
        total += PPS
        column += 1

    global last
    if last == 'y': # Draw X
        drawX(row, column)
        board[column].insert(row, 'x')
        last = 'x'
    else: # Draw O
        drawO(row, column)
        board[column].insert(row, 'y')
        last = 'y'
 
def initialize():

    drawBoard(column, row, windowSizeX, windowSizeY, PPS)

    while runGame:
        onClick(win.getMouse())

    win.getMouse()

initialize()