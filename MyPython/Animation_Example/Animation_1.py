__author__ = 'epq_008'
# events-example1.py
# Demos timer, mouse, and keyboard events

from Tkinter import *

def mousePressed(event):
    canvas.data.mouseText = "last mousePressed: " + str((event.x, event.y))
    redrawAll()

def keyPressed(event):
    canvas.data.keyText = "last keyPressed: char=" + event.char + ", keysym=" + event.keysym
    redrawAll()

def timerFired():
    canvas.data.timerCounter += 1
    canvas.data.timerText = "timerCounter = " + str(canvas.data.timerCounter)
    redrawAll()
    delay = 250 # milliseconds
    canvas.after(delay, timerFired) # pause, then call timerFired again

def redrawAll():
    canvas.delete(ALL)
    # draw the text
    canvas.create_text(150,20,text="events-example1.py")
    canvas.create_text(150,40,text=canvas.data.mouseText)
    canvas.create_text(150,60,text=canvas.data.keyText)
    canvas.create_text(150,80,text=canvas.data.timerText)

def init():
    canvas.data.mouseText = "No mousePresses yet"
    canvas.data.keyText = "No keyPresses yet"
    canvas.data.timerText = "No timerFired calls yet"
    canvas.data.timerCounter = 0

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