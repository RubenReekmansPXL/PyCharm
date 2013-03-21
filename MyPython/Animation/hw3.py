# hw3-bogus.py

"""
WARNING: 

THIS FILE IS JUST SO THAT YOU CAN GET A HEAD-START BEFORE THE ACTUAL
STARTER CODE GETS RELEASED!
"""

######################################################################
# Non-graphics solutions
######################################################################
def nthPalindromicPrime(n):
    if n == 0: return 2              #0th palindromic prime number is 2
    i = 0
    x = 3
    while (i<n):
        if(isPalindromic(x) and isPrime(x)): #check if is both palindromic number and prime number
            i += 1
        x += 2
    return x-2
   

def isPalindromic(n):
    digit = 0
    num = n
    while(num/10!=0):                       #check the number of digits of the number
        digit += 1
        num = num/10 
    for i in xrange(digit/2+1):             #compare the ith and (digit-i)th number
        if (n/(10**i))%10 != (n/(10**(digit-i)))%10:
            return False
    return True

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

##3 nthSmithNumber
##Write the function nthSmithNumber that takes a non-negative int n and returns the nth Smith number,
##where a Smith number is a composite (non-prime) the sum of whose digits are the sum of the digits of
##its prime factors (excluding 1). Note that if a prime number divides the Smith number multiple times,
##its digit sum is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is counted twice,
##thus making 4 a Smith Number. The first few Smith numbers are 4, 22, 27, 58, 85, 94, 121, ... You may read more about Smith numbers
def nthSmithNumber(n):
    if(n==0): return 4         #the first one is 4
    i = -1
    x = 4
    while (i<n):
        if(isSmithNumber(x)):   #find the nth smith number
            i += 1
        x += 1
    return x-1

def isSmithNumber(n):
    if(isPrime(n)): return False
    sumOfFactor = 0
    sumOfNumber = sumOfDigit(n)
    while not(isPrime(n)):
        maxFactor = int(round(n**0.5))
        for factor in xrange(2, maxFactor+1):
            if(n%factor == 0)and(isPrime(factor)):  #add sum of the digit of factor every loop
                sumOfFactor += sumOfDigit(factor)
                n = n/factor
                break
    sumOfFactor += sumOfDigit(n)
    return (sumOfFactor == sumOfNumber)             #compare the sum of prime factor and sum of the digit

    
def sumOfDigit(n):
    acc = 0
    while(n/10!=0):
        acc += n%10
        n = n/10
    acc += n
    return acc

##4 findZeroWithBisection
## the function findZeroWithBisection that takes a function f, a float x0, a float x1, and a float epsilon,
## and returns an approximate value x in [x0,x1] where f(x) is approximately zero.  Your function should stop
## when x0 and x1 are within epsilon, and at that time should return the midpoint of that range.  Note that
## if it is not true that exactly one of f(x0) and f(x1) is negative, your function should return the Python value None,
## signifying that the bisection method cannot be used on the given range.
def findZeroWithBisection(f, lo, hi, epsilon):
    lo = float(lo)
    hi = float(hi)
    if((f(lo)>0 and f(hi)>0) or (f(lo)<0 and (f(hi)<0))):
        return None
    while((abs(f(lo))>epsilon) and (abs(f(hi))>epsilon)):
        mid = (lo + hi)/2.0
        if((f(lo)>=0 and f(mid)>=0) or (f(lo)<=0 and (f(mid)<=0))):  ##lo and mid have same sign, use [mid,high]
            lo = mid
        elif((f(hi)>=0 and f(mid)>=0) or (f(hi)<=0 and (f(mid)<=0))):  ##lo and mid have same sign, use[low, mid]
            hi = mid
        else: return mid
    if(abs(f(lo))<=epsilon): return lo
    else: return hi
   
         

##5 encodeRightLeftRouteCipher
##A right-left route cipher is a fairly simple way to encrypt a message.  It takes two values, some plaintext and
##a number of rows, and it first constructs a grid with that number of rows and the minimum number of columns required,
##writing the message in successive columns.  For example, if the message is WEATTACKATDAWN, with 4 rows, the grid would be:
##   W T A W
##   E A T N
##   A C D
##   T K A
##We will assume the message only contains uppercase letters.  We'll fill in the missing grid entries with lowercase letters
##starting from z and going in reverse (wrapping around if necessary), so we have:
##   W T A W
##   E A T N
##   A C D z
##   T K A y
##Next, we encrypt the text by reading alternating rows first to the right ("WTAW"), then to the left ("NTAE"),
##then back to the right ("ACDz"), and back to the left ("yAKT"), until we finish all rows.  We precede these values
##with the number of rows itself in the string.  So the encrypted value for the message WEATTACKATDAWN with 4 rows is "4WTAWNTAEACDzyAKT". 
##
##With this in mind, write the function encodeRightLeftRouteCipher that takes an all-uppercase message and a positive
##integer number of rows, and returns the encoding as just described.

def encodeRightLeftRouteCipher(message, row):
    n = len(message);
    if (n%row == 0):
        col = n/row
    else:
        col = n/row+1
        nFill = row - n%row
        for i in xrange(nFill):
            message += chr(ord('z') - i%26)
    cipher = str(row)                   #store the row value to the cipher
    for i in xrange(row):
        for j in xrange(col):           #add charactor to the cipher using right left route rules
            if(i%2 == 0):               #read from left
                cipher += message[j*row+i]
            else:
                cipher += message[(col-j-1)*row+i] #read from right
    return cipher
            
            
    


#6 decodeRightLeftRouteCipher
##Write the function decodeRightLeftRouteCipher, which takes an encoding from the previous problem and runs it in reverse,
##returning the plaintext that generated the encoding.  For example, decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT") returns "WEATTACKATDAWN".

def decodeRightLeftRouteCipher(cipher):
    n = 0
    row = 0
    while (ord(cipher[n])<=ord('9')):       #read the row value from cipher
        n += 1
    for digitIndex in xrange(n):
        digit = ord(cipher[digitIndex])-ord('0')
        row += digit*10**(n-1-digitIndex)
    col = (len(cipher) - n)/row
    message = ''                            #initialize the message
    for j in xrange(col):
        for i in xrange(row):
            if(i%2==0):                     #read the odd column
                if (ord(cipher[i*col + j+n])<= ord('Z')): #return the value when meet the lower case make-up letter
                    message += cipher[i*col + j+n]
                else:
                    return message
            else:                           #read the even colume
                if (ord(cipher[(i+1)*col-j-1+n])<= ord('Z')):
                    message += cipher[(i+1)*col-j-1+n]
                else:
                    return message
    return message

######################################################################
# Additional tests
######################################################################

def runMoreStudentTests():
    print "Running additional tests...",
    #### PUT YOUR ADDITIONAL TESTS HERE ####
    s = encodeRightLeftRouteCipher('WEATTACKATDAWN', 4)
    print s
    d = decodeRightLeftRouteCipher(s)
    print d
    s1 = encodeRightLeftRouteCipher('IOTXAVZAZXCEINJWHJUOBMPKDXELLM', 2)
    print s1
    d1 = decodeRightLeftRouteCipher('2ZYZOHEJODFFXMRHTAZJRQOMNCELHYQ')
    d2 = decodeRightLeftRouteCipher('3YILAJKXMKDCIIOQZNKVFQBYDIYUIBC')
    d3 = decodeRightLeftRouteCipher('4JYPPXTYYOPMIOHUDEEJCSBPzyCZYDECM')
    print d1
    print d2
    print d3
    print "Passed!"

def f1(x):
    return x**2-2*x-3

def f2(x):
    return x*5-10

def f3(x):
    return x**3-2*x+1

    

##ignore_rest line
######################################################################
# Graphics solution
######################################################################

from Tkinter import *
import math
import random

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def randomCircleFun(canvas,x0,y0,width,height):
    left = x0
    top = y0
    n = width*height/300
    for i in xrange(n):
        xCenter = random.randint(left, left + width)
        yCenter = random.randint(top, top + height)
        radius = random.randint(35, 50)
        while(radius>=0):
            radius = radius - random.randint(1,7)
            red = random.randint(0, 255)
            green  = random.randint(0,255)
            #while (180>green>70): green  = random.randint(0,255)
            blue = random.randint(0,255)
            #while (180>blue>70): blue = random.randint(0,255)
            canvas.create_oval(xCenter-radius, yCenter-radius, xCenter+radius, yCenter+radius, \
                               fill = rgbString(red, green, blue), width = 0)
    canvas.create_rectangle(left,top,left+width,top+height,width=5)

######################################################################
# Drivers: do not modify this code
######################################################################

def onButton(canvas, drawFn):
    canvas.data.drawFn = drawFn
    redrawAll(canvas)
    
def redrawAll(canvas):
    canvas.delete(ALL)
    canvas.create_rectangle(0,0,canvas.data.width,canvas.data.height,fill="cyan")
    (drawFn,i) = canvas.data.drawFn
    if (drawFn):
        left = canvas.data.canvases[i][0]
        top = canvas.data.canvases[i][1]
        right = left+canvas.data.canvases[i][2]
        bottom = top+canvas.data.canvases[i][3]
        canvas.create_rectangle(left,top,right,bottom,width=4)
        drawFn(canvas, *canvas.data.canvases[i])
        canvas.create_text(canvas.data.width/2,20, text=drawFn.__name__ + str(i), fill="black", font="Arial 24 bold")
    
def graphicsMain():
    root = Tk()
    canvas = Canvas(root, width=750, height=500)
    class Struct: pass
    canvas.data = Struct()
    canvas.data.width = 750
    canvas.data.height = 500
    canvas.data.canvases = [(50,50,650,400),
                            (100,100,200,300),
                            (100,250,200,200),
                            (50,75,437,384)]
    buttonFrame = Frame(root)
    canvas.data.drawFns = [(randomCircleFun,0), (randomCircleFun,1), (randomCircleFun,2), (randomCircleFun,3)]
    canvas.data.drawFn = canvas.data.drawFns[0]
    for i in xrange(len(canvas.data.drawFns)):
        drawFn = canvas.data.drawFns[i]
        b = Button(buttonFrame, text=drawFn[0].__name__ + str(drawFn[1]), command=lambda drawFn=drawFn:onButton(canvas, drawFn))
        b.grid(row=0,column=i)
    canvas.pack()
    buttonFrame.pack()
    redrawAll(canvas)
    root.mainloop()

######################################################################
# Main: you may modify this to run just the parts you want to test
######################################################################

def main():
    runMoreStudentTests()
    graphicsMain()
    
if __name__ == "__main__":
    main()
