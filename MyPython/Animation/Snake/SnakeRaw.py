__author__ = 'epq_008'
# snake1.py

from Tkinter import *

def mousePressed(event):
    redrawAll()

def keyPressed(event):
    redrawAll()

def timerFired():
    redrawAll()
    delay = 250 # milliseconds
    canvas.after(delay, timerFired) # pause, then call timerFired again

def redrawAll():
    canvas.delete(ALL)
    drawSnakeBoard()

def drawSnakeBoard():
    snakeBoard = canvas.data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            drawSnakeCell(snakeBoard, row, col)

def drawSnakeCell(snakeBoard, row, col):
    margin = 5
    cellSize = 30
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize
    bottom = top + cellSize
    canvas.create_rectangle(left, top, right, bottom, fill="white")
    if (snakeBoard[row][col] > 0):
        # draw part of the snake body
        canvas.create_oval(left, top, right, bottom, fill="blue")

def loadSnakeBoard():
    canvas.data.snakeBoard = [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                               [ 0, 0, 0, 0, 4, 5, 6, 0, 0, 0 ],
                               [ 0, 0, 0, 0, 3, 0, 7, 0, 0, 0 ],
                               [ 0, 0, 0, 1, 2, 0, 8, 0, 0, 0 ],
                               [ 0, 0, 0, 0, 0, 0, 9, 0, 0, 0 ],
                               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    ]

def printInstructions():
    print "Snake!"
    print "Use the arrow keys to move the snake."
    print "Eat food to grow."
    print "Stay on the board!"
    print "And don't crash into yourself!"

def init():
    printInstructions()
    loadSnakeBoard()
    redrawAll()
def init(canvas):
    pass
########### copy-paste below here ###########

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    canvas = Canvas(root, width=310, height=310)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    init(canvas)
    # set up events
    root.bind("<Button-1>", lambda event: mousePressed(event,canvas))
    root.bind("<Key>", lambda event: keyPressed(event,canvas))
    # care the use way of lambda
    timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()