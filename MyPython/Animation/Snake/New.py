__author__ = 'epq_008'


import random
from Tkinter import *

def mousePressed(canvas, event):
    #place wall when detecting mouse press in pause mode
    if (canvas.data.isPaused == True):
        point = (event.x, event.y)
        placeWall(canvas, point)
    redrawAll(canvas)

def keyPressed(canvas, event):
    canvas.data.ignoreNextTimerEvent = True # for better timing
    # first process keys that work even if the game is over
    if (event.char == "q"):
        gameOver(canvas)
    elif (event.char == "r"):
        init(canvas)
    elif (event.char == "d"):
        canvas.data.inDebugMode = not canvas.data.inDebugMode
    elif (event.char == "p"):
        canvas.data.isPaused = not canvas.data.isPaused
        # now process keys that only work if the game is not over
    if (canvas.data.isGameOver == False and canvas.data.isPaused == False):
        if (event.keysym == "Up"):
            moveSnake(canvas, -1, 0)
        elif (event.keysym == "Down"):
            moveSnake(canvas, +1, 0)
        elif (event.keysym == "Left"):
            moveSnake(canvas, 0, -1)
        elif (event.keysym == "Right"):
            moveSnake(canvas, 0, +1)
    redrawAll(canvas)

def moveSnake(canvas, drow, dcol):
    # move the snake one step forward in the given direction.
    canvas.data.snakeDrow = drow # store direction for next timer event
    canvas.data.snakeDcol = dcol
    snakeBoard = canvas.data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    headRow = canvas.data.headRow
    headCol = canvas.data.headCol
    newHeadRow = headRow + drow
    newHeadCol = headCol + dcol
    # the wall is lasting for one more move every snake move
    for row in xrange(rows):
        for col in xrange(cols):
            if(snakeBoard[row][col]<=-10):
                snakeBoard[row][col] -= 1
    if ((newHeadRow < 0) or (newHeadRow >= rows) or
            (newHeadCol < 0) or (newHeadCol >= cols)):
        # snake ran off the board
        gameOver(canvas)
    elif (snakeBoard[newHeadRow][newHeadCol] > 0):
        # snake ran into itself!
        gameOver(canvas)
    elif (snakeBoard[newHeadRow][newHeadCol] == -1):
        # eating food!  Yum!
        snakeBoard[newHeadRow][newHeadCol] = 1 + snakeBoard[headRow][headCol]
        canvas.data.headRow = newHeadRow
        canvas.data.headCol = newHeadCol
        canvas.data.score += 1
        # the poison is placed with every 3 foods in level 2
        if (canvas.data.score % 3 == 0):
            canvas.data.level = 2
            placePoison(canvas)
        placeFood(canvas)
    elif (snakeBoard[newHeadRow][newHeadCol] == -2):
        # eating poison...
        gameOver(canvas)
    elif (snakeBoard[newHeadRow][newHeadCol] <= -10):
        # breaking wall!
        canvas.data.wallHitFlag = True
        snakeBoard[newHeadRow][newHeadCol] = 1 + snakeBoard[headRow][headCol]
        canvas.data.headRow = newHeadRow
        canvas.data.headCol = newHeadCol
        canvas.data.score -= 1
        removeTail(canvas)
        # if score is negative, then snake dies
        if (canvas.data.score < 0):
            gameOver(canvas)
    else:
        # normal move forward (not eating food)
        snakeBoard[newHeadRow][newHeadCol] = 1 + snakeBoard[headRow][headCol]
        canvas.data.headRow = newHeadRow
        canvas.data.headCol = newHeadCol
        removeTail(canvas)

def removeTail(canvas):
    # find every snake cell and subtract 1 from it.  When we're done,
    # the old tail (which was 1) will become 0, so will not be part of the snake.
    # So the snake shrinks by 1 value, the tail.
    snakeBoard = canvas.data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            if (snakeBoard[row][col] > 0):
                snakeBoard[row][col] -= 1
        # do subtract twice when hit a wall
    if canvas.data.wallHitFlag == True:
        for row in range(rows):
            for col in range(cols):
                if (snakeBoard[row][col] > 0):
                    snakeBoard[row][col] -= 1
        canvas.data.wallHitFlag = False

def gameOver(canvas):
    canvas.data.isGameOver = True
    score = canvas.data.score
    # add wall existing bonus points
    score += countWall(canvas)
    canvas.data.score = score
    # update highScore list
    highScore = canvas.data.highScore
    if len(highScore)<3:
        highScore += [score]
    elif score > highScore[2]:
        highScore[2]= score
    highScore.sort()
    highScore.reverse()
    canvas.data.highScore=highScore

def countWall(canvas):
    #count wall bonus points if wall exists longer than 20 movements
    snakeBoard = canvas.data.snakeBoard
    score = 0
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in xrange(rows):
        for col in xrange(cols):
            if(snakeBoard[row][col]<=-10-20):
                score +=1
    return score

def timerFired(canvas):
    ignoreThisTimerEvent = canvas.data.ignoreNextTimerEvent
    canvas.data.ignoreNextTimerEvent = False
    if (canvas.data.isPaused == False):
        if ((canvas.data.isGameOver == False) and
                (ignoreThisTimerEvent == False)):
            # only process timerFired if game is not over
            drow = canvas.data.snakeDrow
            dcol = canvas.data.snakeDcol
            moveSnake(canvas, drow, dcol)
            redrawAll(canvas)
    # if paused, simply redraw the canvas
    elif (canvas.data.isPaused == True):
        redrawAll(canvas)
        # whether or not game is over, call next timerFired
    # (or we'll never call timerFired again!)
    # change dalay time according to game level
    if(canvas.data.level==1):
        delay = 150 # milliseconds
    elif(canvas.data.level==2):
        delay = 90
    def f():
        timerFired(canvas)
    canvas.after(delay, lambda : timerFired(canvas))
    # pause, then call timerFired again

def redrawAll(canvas):
    canvas.delete(ALL)
    drawSnakeBoard(canvas)
    drawScore(canvas)
    highScore = canvas.data.highScore
    cx = canvas.data.canvasWidth/2
    cy = canvas.data.canvasHeight/2 + canvas.data.offset
    if (canvas.data.isGameOver == True):
        canvas.create_text(cx, cy, text="Game Over!", \
                           font=("Helvetica", 32, "bold"))
        cx = canvas.data.canvasWidth*5/6
        cy = canvas.data.offset/2
        #draw high score list when game over
        if(len(highScore)==0):
            canvas.create_text(cx, cy, text= \
                "High Score", font = ("Helvetica",10, "bold"))
        elif(len(highScore)==1):
            canvas.create_text(cx, cy, text= \
                "High Score:\n  1. %d" \
                %highScore[0], font=("Helvetica",10, "bold"))
        elif(len(highScore)==2):
            canvas.create_text(cx, cy, text= \
                "High Score:\n  1. %d\n  2. %d" \
                %(highScore[0], highScore[1]), \
                               font = ("Helvetica",10, "bold"))
        elif(len(highScore)==3):
            canvas.create_text(cx, cy, text= \
                "High Score:\n  1. %d\n  2. %d\n  3. %d\n" \
                %(highScore[0], highScore[1], highScore[2]), \
                               font = ("Helvetica",10, "bold"))
    if (canvas.data.isPaused == True):
        canvas.create_text(cx, cy, text="PAUSE", font=("Helvetica", 32, "bold"))

def drawScore(canvas):
    cx = canvas.data.canvasWidth/2
    cy = canvas.data.offset/2
    highScore = canvas.data.highScore
    canvas.create_text(cx, cy, text="Score: %d"%canvas.data.score, \
                       font=("Helvetica", 24))

def drawSnakeBoard(canvas):
    snakeBoard = canvas.data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            drawSnakeCell(canvas, snakeBoard, row, col)

def drawSnakeCell(canvas, snakeBoard, row, col):
    margin = canvas.data.margin
    offset = canvas.data.offset
    cellSize = canvas.data.cellSize
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize + offset
    bottom = top + cellSize
    canvas.create_rectangle(left, top, right, bottom, fill="white")
    if (snakeBoard[row][col] > 0):
        # draw part of the snake body
        if (canvas.data.isPaused):
            canvas.create_oval(left, top, right, bottom, fill="light slate blue")
        else: canvas.create_oval(left, top, right, bottom, fill="blue")
    elif (snakeBoard[row][col] == -1):
        # draw food
        if (canvas.data.isPaused):
            canvas.create_oval(left, top, right, bottom, fill="lawn green")
        else: canvas.create_oval(left, top, right, bottom, fill="green")
    elif (snakeBoard[row][col] == -2):
        # draw poison
        if (canvas.data.isPaused):
            canvas.create_oval(left, top, right, bottom, fill="pink")
        else: canvas.create_oval(left, top, right, bottom, fill="red")
    elif (snakeBoard[row][col] <= -10):
        # draw wall
        if (canvas.data.isPaused):
            canvas.create_oval(left, top, right, bottom, fill="sandy brown")
        else: canvas.create_oval(left, top, right, bottom, fill="brown")
        # for debugging, draw the number in the cell
    if (canvas.data.inDebugMode == True):
        canvas.create_text(left+cellSize/2,top+cellSize/2,
                           text=str(snakeBoard[row][col]),font=("Helvatica", 14, "bold"))

def loadSnakeBoard(canvas):
    rows = canvas.data.rows
    cols = canvas.data.cols
    snakeBoard = [ ]
    for row in range(rows): snakeBoard += [[0] * cols]
    snakeBoard[rows/2][cols/2] = 1
    canvas.data.snakeBoard = snakeBoard
    findSnakeHead(canvas)
    placeFood(canvas)

def placeFood(canvas):
    # place food (-1) in a random location on the snakeBoard, but
    # keep picking random locations until we find one that is not
    # part of the snake!
    snakeBoard = canvas.data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    while True:
        row = random.randint(0,rows-1)
        col = random.randint(0,cols-1)
        if (snakeBoard[row][col] == 0):
            break
    snakeBoard[row][col] = -1

def placePoison(canvas):
    # place poison (-2)
    snakeBoard = canvas.data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    headRow = canvas.data.headRow
    headCol = canvas.data.headCol
    while True:
        row = random.randint(0,rows-1)
        col = random.randint(0,cols-1)
        if (snakeBoard[row][col] == 0 and
                    (abs(row-headRow)+ abs(col-headCol))>2):
            break
    snakeBoard[row][col] = -2

def findSnakeHead(canvas):
    # find where snakeBoard[row][col] is largest, and
    # store this location in headRow, headCol
    snakeBoard = canvas.data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    headRow = 0
    headCol = 0
    for row in range(rows):
        for col in range(cols):
            if (snakeBoard[row][col] > snakeBoard[headRow][headCol]):
                headRow = row
                headCol = col
    canvas.data.headRow = headRow
    canvas.data.headCol = headCol

def placeWall(canvas, point):
    # place initiated wall (-10)
    snakeBoard = canvas.data.snakeBoard
    (row, col) =  findIndexOfCell(canvas, point)
    if (snakeBoard[row][col]==0):
        snakeBoard[row][col] = -10

def findIndexOfCell(canvas, point):
    # find cell index corresponding to mouse click
    margin = canvas.data.margin
    offset = canvas.data.offset
    cellSize = canvas.data.cellSize
    col = (point[0] - margin)/cellSize
    row = (point[1] - offset - margin)/cellSize
    return (row, col)

def printInstructions():
    print "Snake!"
    print "Use the arrow keys to move the snake."
    print "Eat food to grow."
    print "Stay on the board!"
    print "And don't crash into yourself!"
    print "Press 'd' for debug mode."
    print "Press 'r' to restart."
    print "Press 'p' to pause."

def init(canvas):
    printInstructions()
    loadSnakeBoard(canvas)
    canvas.data.inDebugMode = False
    canvas.data.isGameOver = False
    canvas.data.isPaused = False
    canvas.data.score = 0
    canvas.data.level = 1
    canvas.data.wallHitFlag = False
    canvas.data.snakeDrow = 0
    canvas.data.snakeDcol = -1 # start moving left
    canvas.data.ignoreNextTimerEvent = False
    redrawAll(canvas)

########### copy-paste below here ###########

def run(rows, cols):
    # create the root and the canvas
    root = Tk()
    margin = 5
    offset = 100
    cellSize = 30
    canvasWidth = 2*margin + cols*cellSize
    canvasHeight = 2*margin + rows*cellSize
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight+offset)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    canvas.data.margin = margin
    canvas.data.offset = offset
    canvas.data.cellSize = cellSize
    canvas.data.canvasWidth = canvasWidth
    canvas.data.canvasHeight = canvasHeight
    canvas.data.rows = rows
    canvas.data.cols = cols
    canvas.data.highScore = []
    init(canvas)
    # set up events
    root.bind("<Button-1>", lambda event: mousePressed(canvas, event))
    root.bind("<Key>", lambda event: keyPressed(canvas, event))
    timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run(8,16)
