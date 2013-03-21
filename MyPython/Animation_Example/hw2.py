# hw2.py
# Yujia Wang + yujiaw + section A

"""
   ** Place your manually-graded (Reasoning Over Code) solutions here! **
"""

######################################################################
# Place your non-graphics solutions here!
######################################################################

def sumOfSquaresOfDigits(n):
    sum = 0
    while (n/10!=0):
        sum += (n%10)**2
        n = n/10
    sum += n**2;
    return sum

def isHappyNumber(n):
    if(n<1):
        return False
    count = 0;
    while(sumOfSquaresOfDigits(n)!=1):   
        if (sumOfSquaresOfDigits(n)==4):
            return False
        n = sumOfSquaresOfDigits(n)
    return True

def nthHappyNumber(n):
    count = 0
    x = 1
    while (count < n+1):
        if(isHappyNumber(x) == True):
            count += 1
            x += 1
        else:
            x += 1          
    return x-1

def isPrime(n): # from course notes
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = int(round(n**0.5))
    for factor in xrange(2,maxFactor+1):
        if (n % factor == 0):
            return False
    return True

def isHappyPrime(n):
    return (isHappyNumber(n) and isPrime(n))

def nthHappyPrime(n):
    count = 0
    x = 1
    while (count < n+1):
        if(isHappyPrime(x) == True):
            count += 1
            x += 1
        else:
            x += 1          
    return x-1


##############################################
## Prime Counting
##############################################

def pi(n):
    count = 0;
    for x in xrange(1,n+1):
        if(isPrime(x)==True):
            count += 1
    return count

def almostEqual(d1, d2):
    epsilon = 0.000001
    return (abs(d2 - d1) < epsilon)

def h(n):
    if n > 0:
        sum = 0;
        for x in xrange(1,n+1):
            sum += 1/float(x)
        return sum
    else:
        return 0

def estimatedPi(n):
    if (n>2):
        return round(n/(h(n)-1.5))
    else:
        return 0

def estimatedPiError(n):
    if (n>2):
        return abs(estimatedPi(n)-pi(n))
    else:
        return 0 

######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################

######################################################################
# Place your (optional) additional tests here
######################################################################

def runMoreStudentTests():
    print "Running additional tests...",
    #### PUT YOUR ADDITIONAL TESTS HERE ####
    print "Passed!"

######################################################################
# Place your graphics solutions here!
######################################################################

from Tkinter import *
import math

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def drawCircle(canvas, x0, y0, x1, y1):
    width = x1 - x0
    if (width > 200):
        fill = "blue"
    else:
        fill = rgbString(147, 197, 114) # pistachio!
    canvas.create_oval(x0, y0, x1, y1, fill=fill, width=4)

def drawArrow(canvas, x0, y0, x1, y1):
    width = abs(x1 - x0)
    height = abs(y1 - y0)
    arrow_width1 = 0.1*width
    arrow_width2 = 0.1*width
    arrow_length1 = 0.6*height
    arrow_length2 = height - arrow_length1
    if (width > 200):
        fill = "red"
        px1 = x0 + width/2 - arrow_width1/2;
        py1 = y1;
        px2 = px1;
        py2 = py1- arrow_length1
        px3 = px2 - arrow_width2
        py3 = py2
        px4 = x0 + width/2
        py4 = y0
    else:
        fill = "blue"
        px1 = x0 + width/2 - arrow_width1/2;
        py1 = y0;
        px2 = px1;
        py2 = py1+arrow_length1
        px3 = px2 - arrow_width2
        py3 = py2
        px4 = x0 + width/2
        py4 = y1
    canvas.create_polygon(px1, py1, px2, py2, px3, py3, px4, py4, px3+arrow_width1+arrow_width2*2, \
                              py3, px2+ arrow_width1, py2, px1 + arrow_width1, py1,fill = fill)
 

def drawGradient(canvas, x0, y0, x1, y1):
    width = x1 - x0
    if (width > 200):
        blue = rgbString(0, 0, 255) # blue
        black = rgbString(0, 0, 0) # black
        gap =  width/128.0
        for xp in xrange(0, 128):
            fill = rgbString(0, 0, 255*xp/128)
            canvas.create_rectangle(x0+xp*gap, y0, x0+gap*(xp+1), y1, fill = fill, width = 0)
    else:
        gap = width/10.0
        for xp in xrange(0, 10):
            fill = rgbString(255*xp/10, 255*xp/10, 255*xp/10)
            canvas.create_rectangle(x0+xp*gap, y0, x0+gap*(xp+1), y1, fill = fill, width = 0)
    pass

def drawGrid(canvas, x0, y0, x1, y1):
    width = x1 - x0
    length = y1 - y0
    if (width > 200):
        shade_blue = rgbString(100, 255, 255)
        shade_red = rgbString(255, 100, 100)
        line_space = width/8.0
        column_space = length/4.0
        for i in xrange(0, 8):
            for j in xrange(0,4):
                if (i+j)%2 == 0:
                    canvas.create_rectangle(x0+i*line_space, y0+j*column_space, \
                                            x0+line_space*(i+1), y0+column_space*(j+1), fill = shade_red, width = 2)
                else:
                    canvas.create_rectangle(x0+i*line_space, y0+j*column_space, \
                                            x0+line_space*(i+1), y0+column_space*(j+1), fill = shade_blue, width = 2)
                canvas.create_text(x0 + line_space/2 + i*line_space, y0+ column_space/2+j*column_space,text=i+j*8+1, fill="red")
    else:
        line_space = width/4.0
        column_space = length/8.0
        for i in xrange(0, 4):
            for j in xrange(0,8):
                if (i+j)%2 == 1:
                    canvas.create_rectangle(x0+i*line_space, y0+j*column_space, \
                                            x0+line_space*(i+1), y0+column_space*(j+1), fill = "white", width = 2)
                else:
                    canvas.create_rectangle(x0+i*line_space, y0+j*column_space, \
                                            x0+line_space*(i+1), y0+column_space*(j+1), fill = "black", width = 2)
                canvas.create_text(x0 + line_space/2 + i*line_space, y0+ column_space/2+j*column_space,text=8*(i+1)-j, fill="red")
 
    pass

def drawSpiral(canvas, x0, y0, x1, y1):
    width = x1 - x0
    if (width > 200):
        for i in xrange(0, 28):
            for j in xrange(0, 32):
                theta0 = -2*math.pi*i/28
                offset = -2*math.pi*j/32
                r = width*j/32/2
                rp = width/90;
                fill = rgbString(255-128*j/32,255*(32-j)/32,255*j/32)
                xp = x0+width/2+r*math.cos(theta0+offset)
                yp = y0+width/2-r*math.sin(theta0+offset)
                canvas.create_oval(xp-rp, yp-rp, xp+rp, yp+rp, fill=fill, width=0)            
    else:
        for i in xrange(0, 28):
            for j in xrange(0, 32):
                theta0 = -2*math.pi*i/28
                offset = -2*math.pi*j/32
                r = width*j/32/2
                rp = width/90
                fill = rgbString(128*j/32,255*(32-j)/32,255*j/32)
                xp = x0+width/2+r*math.cos(theta0+offset)
                yp = y0+width/2-r*math.sin(theta0+offset)
                canvas.create_oval(xp-rp, yp-rp, xp+rp, yp+rp, fill=fill, width=0)            

    pass

######################################################################
# Drivers: do not modify this code
######################################################################

def onButton(canvas, drawFn):
    canvas.data.drawFn = drawFn
    redrawAll(canvas)
    
def redrawAll(canvas):
    canvas.delete(ALL)
    canvas.create_rectangle(0,0,canvas.data.width,canvas.data.height,fill="cyan")
    drawFn = canvas.data.drawFn
    if (drawFn):
        canvas.create_rectangle(50, 50, 450, 450, width=4)
        drawFn(canvas, 50, 50, 450, 450)
        canvas.create_rectangle(500, 150, 700, 350, width=4)
        drawFn(canvas, 500, 150, 700, 350)
        canvas.create_text(canvas.data.width/2,20, text=drawFn.__name__, fill="black", font="Arial 24 bold")

def graphicsMain():
    root = Tk()
    canvas = Canvas(root, width=750, height=500)
    class Struct: pass
    canvas.data = Struct()
    canvas.data.width = 750
    canvas.data.height = 500
    buttonFrame = Frame(root)
    canvas.data.drawFns = [drawCircle, drawArrow, drawGradient, drawGrid, drawSpiral]
    canvas.data.drawFn = canvas.data.drawFns[0]
    for i in xrange(len(canvas.data.drawFns)):
        drawFn = canvas.data.drawFns[i]
        b = Button(buttonFrame, text=drawFn.__name__, command=lambda drawFn=drawFn:onButton(canvas, drawFn))
        b.grid(row=0,column=i)
    canvas.pack()
    buttonFrame.pack()
    redrawAll(canvas)
    root.mainloop()

######################################################################
# Main: you may modify this to run just the parts you want to test
######################################################################

def main():
    # include following line to autograde when you run this file
    execfile("hw2-public-grader.py", globals())
    runMoreStudentTests()
    graphicsMain()

if __name__ == "__main__":
    main()
