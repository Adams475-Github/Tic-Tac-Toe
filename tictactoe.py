import zellegraphics as zg
import time
import math

PPS = 150
inset = 15
column = int(input("How many rows and columns do you want?"))
row = column
windowSizeX = column * PPS
windowSizeY = column * PPS
board = [['~']*column for i in range(column)]
hasWinner = False

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
    zg.Line( zg.Point((row * PPS) + inset, column * PPS + inset), zg.Point((row + 1) * PPS - inset, (column + 1) * PPS - inset)).draw(win)
    zg.Line( zg.Point((row + 1) * PPS - inset, column * PPS + inset), zg.Point(row * PPS + inset, (column + 1) * PPS - inset)).draw(win)

def drawO(row, column):
    center = zg.Point((row * PPS) + (PPS / 2), (column * PPS) + (PPS / 2))
    zg.Circle(center, PPS / 2 - inset).draw(win)

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
    if not hasWinner:
        drawNextPiece(point)
        #printBoard()
        checkForWin()
    else:
        win.close()

def checkForWin():
    # Check for horizontal 'x' win
    times = 0
    for x in range(column):
        for y in range(column):
            if board[x][y] == 'x':
                times += 1
            else:
                times = 0
            
            if times >= column:
                winFound('x')
                return
        times = 0
    
    # Check for vertical 'x' win
    times = 0
    for y in range(column):
        for x in range(column):
            if board[x][y] == 'x':
                times += 1
            else:
                times = 0
            
            if times >= column:
                winFound('x')
                return
        times = 0
    
    # Check for right diagonal 'x' win
    times = 0 
    for x in range(column):
        if board[x][x] == 'x':
            times += 1
        else:
            times = 0
        
        if times >= column:
            winFound('x')
            return
    times = 0
    
    # Check for left diagonal 'x' win
    times = 0
    for x in range((column - 1), -1, -1):
        y = column - 1 - x
        if board[x][y] == 'x':
            times += 1
        else:
            times = 0
        
        if times >= column:
            winFound('x')
            return
    times = 0
    
    # Check for horizontal 'o' win
    times = 0
    for x in range(column):
        for y in range(column):
            if board[x][y] == 'o':
                times += 1
            else:
                times = 0
            
            if times >= column:
                winFound('o')
                return
        times = 0
    
    # Check for vertical 'o' win
    times = 0
    for y in range(column):
        for x in range(column):
            if board[x][y] == 'o':
                times += 1
            else:
                times = 0
            
            if times >= column:
                winFound('o')
                return
        times = 0
    
    # Check for right diagonal 'o' win
    times = 0 
    for x in range(column):
        if board[x][x] == 'o':
            times += 1
        else:
            times = 0
        
        if times >= column:
            winFound('o')
            return
    times = 0
    
    # Check for left diagonal 'o' win
    times = 0
    for x in range((column - 1), -1, -1):
        y = column - 1 - x
        if board[x][y] == 'o':
            times += 1
        else:
            times = 0
        
        if times >= column:
            winFound('o')
            return
    times = 0

def winFound(winner):
    winner = winner.upper()
    print(winner, "WON!")
    winText = zg.Text(zg.Point(windowSizeX / 2, windowSizeY / 2), winner + " WON!")
    winText.setSize(30)
    winText.setStyle("bold")
    winText.setTextColor("red")
    winText.draw(win)
    
    global hasWinner
    hasWinner = True
    
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

    while not hasWinner:
        point = win.getMouse()
        onClick(point)

    win.getMouse()

initialize()