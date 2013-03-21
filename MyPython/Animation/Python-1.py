# events-example0.py
# Barebones timer, mouse, and keyboard events

from Tkinter import *

def mousePressed(event):
    canvas.data.squareX = event.x
    canvas.data.squareY = event.y
    redrawAll()

def keyPressed(event):
    if canvas.data.squareColor == "blue":
        canvas.data.squareColor = "green"
    elif canvas.data.squareColor == "green":
        canvas.data.squareColor = "blue"
    redrawAll()

def timerFired():
    canvas.data.squareX += canvas.data.squareDX
    canvas.data.squareY += canvas.data.squareDY
    print canvas.data.squareX, canvas.data.squareY
    if canvas.data.squareX - canvas.data.squareR <= 0 or canvas.data.squareX + canvas.data.squareR >= canvas.data.canvasWidth:
        canvas.data.squareDX *= -1
    if canvas.data.squareY - canvas.data.squareR <= 0 or canvas.data.squareY + canvas.data.squareR >= canvas.data.canvasHeight:
        canvas.data.squareDY *= -1
    
    redrawAll()
    delay = 50 # milliseconds
    canvas.after(delay, timerFired) # pause, then call timerFired again

def redrawAll():
    canvas.delete(ALL)
    c = canvas.data
    canvas.create_rectangle(c.squareX - c.squareR, #upper-left x
                            c.squareY - c.squareR, # upper-left y
                            c.squareX + c.squareR, # lower-right x
                            c.squareY + c.squareR, # lower-right y
                            fill = c.squareColor)

def init():
    canvas.data.squareX = 50
    canvas.data.squareY = 50
    canvas.data.squareDX = 5
    canvas.data.squareDY = 5
    canvas.data.squareR = 10
    canvas.data.canvasWidth = 300
    canvas.data.canvasHeight = 200
    canvas.data.squareColor = "blue"

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    canvas = Canvas(root, width=300, height=200)
    canvas.pack()
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    init()
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired()
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)


run()