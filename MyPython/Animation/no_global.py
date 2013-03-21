__author__ = 'epq_008'
# events-example1-no-globals.py
# Demos timer, mouse, and keyboard events

# Search for "DK" in comments for all the changes
# required to eliminate globals.

from Tkinter import *

def mousePressed(canvas, event):
    canvas.data.mouseText = "last mousePressed: " + str((event.x, event.y))
    redrawAll(canvas)

def keyPressed(canvas, event):
    canvas.data.keyText = "last keyPressed: char=" + event.char + ", keysym=" + event.keysym
    redrawAll(canvas)

def timerFired(canvas):
    canvas.data.timerCounter += 1
    canvas.data.timerText = "timerCounter = " + str(canvas.data.timerCounter)
    redrawAll(canvas)
    delay = 250 # milliseconds
    def f():
        timerFired(canvas) # DK: define local fn in closure
    canvas.after(delay, f) # pause, then call timerFired again

def redrawAll(canvas): # DK: redrawAll() --> redrawAll(canvas)
    canvas.delete(ALL)
    # draw the text
    canvas.create_text(150,20,text="events-example1.py")
    canvas.create_text(150,40,text=canvas.data.mouseText)
    canvas.create_text(150,60,text=canvas.data.keyText)
    canvas.create_text(150,80,text=canvas.data.timerText)

def init(canvas):
    canvas.data.mouseText = "No mousePresses yet"
    canvas.data.keyText = "No keyPresses yet"
    canvas.data.timerText = "No timerFired calls yet"
    canvas.data.timerCounter = 0

def run():
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=300, height=200)
    canvas.pack()
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    init(canvas) # DK: init() --> init(canvas)
    # set up events
    # DK: You can use a local function with a closure
    # to store the canvas binding, like this:
    def f(event): mousePressed(canvas, event)
    root.bind("<Button-1>", f)
    # DK: Or you can just use an anonymous lamdba function,
    # like this:
    root.bind("<Key>", lambda event: keyPressed(canvas, event))
    timerFired(canvas) # DK: timerFired() --> timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()