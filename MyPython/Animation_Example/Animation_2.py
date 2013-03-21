__author__ = 'epq_008'
# events-example2.py
# Demos timer, mouse, and keyboard events

from Tkinter import *

def mousePressed(event):
    newCircleCenter = (event.x, event.y)
    canvas.data.circleCenters.append(newCircleCenter)
    redrawAll()

def keyPressed(event):
    if (event.char == "d"):
        if (len(canvas.data.circleCenters) > 0):
            canvas.data.circleCenters.pop(0)
        else:
            print "No more circles to delete!"
    if (event.keysym == "Left"):
        sqRight = canvas.data.squareLeft + 100
        if (sqRight > 0):
            canvas.data.squareLeft -= 20
        else:
            canvas.data.squareLeft = 300
    if (event.keysym == "Right"):
        sqRight = canvas.data.squareLeft - 100
        if (sqRight <200):
            canvas.data.squareLeft += 20
        else:
            canvas.data.squareLeft = -100
    redrawAll()

def timerFired():
    if (canvas.data.squareFill == "green"):
        canvas.data.squareFill = "yellow"
    else:
        canvas.data.squareFill = "green"
    redrawAll()
    delay = 750 # milliseconds
    canvas.after(delay, timerFired) # pause, then call timerFired again

def redrawAll():
    canvas.delete(ALL)
    # draw the square
    canvas.create_rectangle(canvas.data.squareLeft, 50,
                            canvas.data.squareLeft+100, 150,
                            fill=canvas.data.squareFill)
    # draw the circles
    for circleCenter in canvas.data.circleCenters:
        (cx, cy) = circleCenter
        r = 20
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="cyan")
        # draw the text
    canvas.create_text(150,20,text="events-example2.py")
    canvas.create_text(150,40,text="Mouse clicks create circles")
    canvas.create_text(150,60,text="Pressing 'd' deletes circles")
    canvas.create_text(150,80,text="Left arrow moves square left")
    canvas.create_text(150,100,text="Timer changes color of square")

def init():
    canvas.data.squareLeft = 50
    canvas.data.squareFill = "yellow"
    canvas.data.circleCenters = [ ]

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