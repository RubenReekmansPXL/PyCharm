# hw4.py
# <Yujia Wang> <yujiaw> <section A> 
"""
B. Practice-quiz
1. Quick Answers
    1. s = '15112', s[4] = '0'
    2. single-quoted is representing a single line string, triple-quoted can represent
    multi-line string
    3. no
    4. str is better, because what eval does is evaluate expression, not just convert to int
    and much faster
    5. s.lower() changes all the letters in the string to lower case, s.islower check if all
    the letters in the string are all lower case
    6. s.isalpha() checks if the string consists of alphabetic only and at least one charater
    7. String 'abc12e  34.57g'
    8. value that not stored in a meaningful name variable, except 1,-1,0,2,10,-2
    9.  [1]understand the problem
        [2]devise a plan
        [3]carry out the plan
        [4]examine and review
    10. [1]use explicit, small, clear steps
        [2]make the steps work for any case
        [3]do not require human memory
2. Code tracing:
    1.  2 blvFP      
        3 v
        None
        //in the first loop  s starts from 'a' ends 'Z', length is 51, length/5 = 10
        counts from s[1]('b') every ten letters results 'blvFP'
        in the second loop s become 'blvFP', length from s[2]to s[-2] is 1,
        counts from s[2]('v') to s[-2]('P'), result string 'v'
        in the third loop, length s[3:-3] is 0, and break
    2.  1, b, a
        3, d, c
        //check if there is an letter in t that is the one alphabetically after one letter 
        in s, if yes, print the letter location in s, character in s and t.
3.  Reasoning Over Code
    1.  f(14, 29, 5)
    //(-ord('a'))%26 is 7, offset for "VAF" to "A" is 21, 0, 5, n could be
    14, (-7)or 19, (-2) or 24, so the argument'z' has to be 5, x could be 14
    and y could be 29
    2.  g('0246897531')
    // every loop adds the first character to t and cut the first one and reverse
    the string, t == '0123456789', the input should be '0246897531'
    
4. Free Response
    see code

C. Quiz 3
1. Quick Answers.
    1. a%bc123e  45.7g
    2. value that not stored in a meaningful name variable, except 1,-1,0,2,10,-2
2. Code Tracing
    1.  1 adbec
        2 dc
        //in the first loop  s 'abcdeabcdeabcde', length is 15,
        counts from s[0]('a') every 3 letters results 'adbec'
        in the second loop s become 'adbec', length is 5,
        counts from s[1]('d') every 3 letters, result string 'dc'
        in the third loop, length s[2] is none, s[-3] is none, and break
    2.  1 2
        1 4
        2 6
        3 6
        bcbccebe
        //count from b
3.  Reasonning Over Code
        1.  f(0.63)
        //return true when argument is pi/5, format it as %0.2f, 3.14/5 is 0.63
        2.  f('LLLLKKKJJI')
        //character bias i to 'H' times i added to the beginning of the string
4. Free Response
    see code

D.  1.  f1(6, 2, 2)
        //the string is ab <tab> c\d length is 6
        string.whitespace consists of space + tab + linefeed + return + formfeed
        + vertical tab, s[2] is tab
        s.find return the index, 'b' index is 1, 'e' is not in the string, index
        is -1, x=2
    2.  f2('%+dabc%0.1f')
    3.  f3('degjn')
        //the first is d, ord of next letter equals ord of previous plus i,
        result 'degjn'
    4.  f4('adc5b', 'ab5cd')
        //the length of s should be 4+1, assume length of t is 5, t[2]='4',
        s[1] to s[4] is the reverse of t[1] to t[5]
    5.  f5('34a')
        //'-' is not in s, "3-4-" should come from the first try, len(s) should be
        2, a error should come after the number, s might be '34a'

E.  1.  a)O(n**2)   b)O(n log n)    c)O(n)  d)O(log n)  e)O(n)  f)O(n**0.5)
    2.  10, 30, 40
    3.  1,4,6,8,2,3,5,7
        //6,8,1,4,2,5,3,7
    4.  2,5,4,1,3
        2,3,4,1,5
        2,3,1,4,5
        2,1,3,4,5
        1,2,3,4,5
    5.  n log n
        //8/3 = 2.67, 21.5/3 = 7.17, between n to n**2
    6.  yes, i got it
    7.  selectionsort N + N-1 + N-2 +... + 1 = N(N+1)/2
        mergesort   N/2+N/2+...N/2 (totally log_2 N times)=N*(log_2 N)/2
    8.  Using approximate compute time
        selectionsort
        N:10,000            0.569 s
        N:20,000            2.138 s     3.75 times          
        N:40,000            8.961 s     15.7 times      N**2
        mergesort
        N:1,000,000         0.567 s     
        N:2,000,000         1.195 s     2.10 times      
        N:4,000,000         2.456 s     4.33 times      NlogN
    9.  A. T = 2N + 5                       O(N)
        B. T = N + logN                     O(N)
        C. T = N**3 + 45N**2 + 100logN      O(N**3)
        D. T = 10N * 3N                     O(N**2) 
        E. T = 10N + 3N                     O(N)
        F. T = number of steps merge sort takes to sort a list of N numbers
                                            O(NlogN)
    10. f0  n*(n-1)         O(n**2)
        f1  n*(n-1)/2       O(n**2)
        f2  n/4*(n/8-1)/2   O(n**2)
        f3  n*100           O(n)
        f4  2*log_2 n       O(log n)
        f5  n*2*(N/2 log_2 N + N/4 log_2(N/2)+...)
            = 2*N**N log_2 N                O(N**2logN)
"""

"""
WARNING: 

THIS FILE IS JUST SO THAT YOU CAN GET A HEAD-START BEFORE THE ACTUAL
STARTER CODE GETS RELEASED!
"""

######################################################################
# Non-graphics solutions
######################################################################
##sameChars
##Write the function sameChars(s1, s2) that takes two strings and returns True
##if the two strings are composed of the same characters (though perhaps in different
##numbers and in different orders) -- that is, if every character that is in the first
##string, is in the second, and vice versa -- and False otherwise. This test is case-sensitive,
##so "ABC" and "abc" do not contain the same characters. The function returns False if
##either parameter is not a string, but returns True if both strings are empty (why?).
##
import math
import string

def sameChars(s1, s2):
    if(not (type(s1)==str and type(s2)==str)):
        return False
    if(s1 == '' and s2 == ''):
        return True
    for i in xrange(len(s1)):       ##check if all characters in s1 can be found in s2
        for j in xrange(len(s2)):
            if (s1[i] == s2[j]):
                break
            if (j==len(s2)-1):
                return False
    for i in xrange(len(s2)):       ##check if all characters in s2 can be found in s1
        for j in xrange(len(s1)):
            if (s2[i] == s1[j]):
                break
            if (j==len(s1)-1):
                return False
    return True


##hasBalancedParentheses
##Write the function hasBalancedParentheses, which takes a string and returns True if
##that code has balanced parentheses and False otherwise (ignoring all non-parentheses in the string).
##We say that parentheses are balanced if each right parenthesis closes (matches) an open (unmatched)
##left parenthesis, and no left parentheses are left unclosed (unmatched) at the end of the text.
##So, for example, "( ( ( ) ( ) ) ( ) )" is balanced, but "( ) )" is not balanced, and "( ) ) (" is
##also not balanced.
##

def hasBalancedParentheses(s):
    count = 0
    for c in s:
        if c =='(':                 
            count += 1
        elif c == ')':
            count -= 1
        if count<0: return False  #unmatched parentheses found
    return(count == 0)
##inverseF
##Consider the function f(x) = 3x - 2x.  Write the function inverseF(y), that takes a positive
##floating-point value y, and finds and returns the value x such that f(x) == y.  As this is approximate,
##your answer needs to be within 0.001 of the actual answer.  For example, f(2) = 32 - 22 = 9 - 4 = 5.
##Thus, since f(2)==5, inverseF(5)==2.  How to do this?  Using bisection, though you may have to slightly adapt it.
##
##Hint:  in the homework, we used bisection to find zeros.  We can adjust this problem easily to
##search for a zero.  How?  Well, say:
##     y = 3x - 2x
##Then we also have:
##     3x - 2x - y = 0
def inverseF(y):
    if (y==0): return 0
    lo = 0                             #define root section [lo, hi]        
    hi = math.log(y)/math.log(3) + 1   
    result = findZeroWithBisectionAdjust(sampleF, y, lo, hi, 0.001)
    return result

def findZeroWithBisectionAdjust(f, y, lo, hi, epsilon):
    lo = float(lo)
    hi = float(hi)
    if((f(lo)-y>0 and f(hi)-y>0) or (f(lo)-y<0 and (f(hi)-y<0))):
        return None
    while((abs(f(lo)-y)>epsilon) and (abs(f(hi)-y)>epsilon)):
        mid = (lo + hi)/2.0
        if((f(lo)-y>=0 and f(mid)-y>=0) or (f(lo)-y<=0 and (f(mid)-y<=0))):  ##lo and mid have same sign, use [mid,high]
            lo = mid
        elif((f(hi)-y>=0 and f(mid)-y>=0) or (f(hi)-y<=0 and (f(mid)-y<=0))):  ##lo and mid have same sign, use[low, mid]
            hi = mid
        else: return mid
    if(abs(f(lo)-y)<=epsilon): return lo
    else: return hi

def almostEqual(x1, x2):
    if(abs(x1-x2)<=0.001): return True
    else: return False
    
def sampleF(x):
    return 3**x-2**x

##quiz 3 function
def islower(s):
    flag = 0;                                   #flag for if 
    for c in s:
        if (c in string.ascii_letters):
            flag = 1
            if (c in string.ascii_uppercase ):   #if find capital letters, return false
                return False
    return True and flag


##hw3 functions
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
    return (sumOfFactor == sumOfNumber)

def findZeroWithBisection(f, lo, hi, epsilon):
    lo = float(lo)
    hi = float(hi)
    if((f(lo)>0 and f(hi)>0) or (f(lo)<0 and (f(hi)<0))):           ##no root found the section [lo,hi]
        return None
    while((abs(f(lo))>epsilon) and (abs(f(hi))>epsilon)):
        mid = (lo + hi)/2.0
        if((f(lo)>=0 and f(mid)>=0) or (f(lo)<=0 and (f(mid)<=0))):  ##lo and mid have same sign, use [mid,high]
            lo = mid
        elif((f(hi)>=0 and f(mid)>=0) or (f(hi)<=0 and (f(mid)<=0))):  ##lo and mid have same sign, use[low, mid]
            hi = mid
        else: return mid
    if(abs(f(lo))<=epsilon): return lo
    else: return hi       #compare the sum of prime factor and sum of the digit

    
def sumOfDigit(n):          #compute the sum of digits in a number
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
    if((f(lo)>0 and f(hi)>0) or (f(lo)<0 and (f(hi)<0))):           ##no root in this section [lo, hi]
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
    if (n%row == 0):                    #compute the rows and cols for cipher
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
##    s = encodeRightLeftRouteCipher('WEATTACKATDAWN', 4)
##    print s
##    d = decodeRightLeftRouteCipher(s)
##    print d
##    s1 = encodeRightLeftRouteCipher('IOTXAVZAZXCEINJWHJUOBMPKDXELLM', 2)
##    print s1
##    d1 = decodeRightLeftRouteCipher('2ZYZOHEJODFFXMRHTAZJRQOMNCELHYQ')
##    d2 = decodeRightLeftRouteCipher('3YILAJKXMKDCIIOQZNKVFQBYDIYUIBC')
##    d3 = decodeRightLeftRouteCipher('4JYPPXTYYOPMIOHUDEEJCSBPzyCZYDECM')
##    print d1
##    print d2
##    print d3
##    assert(d=='WEATTACKATDAWN')
    assert(sameChars('abc', 'cba')==True)
    assert(sameChars('abc', 'cccbba')==True)
    assert(sameChars('abc', 'cdea')==False)
    assert(sameChars('cga', 'agccc')==True)

    assert(hasBalancedParentheses('(()')==False)
    assert(hasBalancedParentheses('()')==True)
    assert(hasBalancedParentheses(')(')==False)
    assert(hasBalancedParentheses('()(a)(b)(c(()))')==True)

    assert(inverseF(0)==0.0)   
    assert(almostEqual(inverseF(1),1.0))
    assert(almostEqual(inverseF(5),2.0))
    assert(almostEqual(inverseF(10),2.505))
    assert(almostEqual(inverseF(19),3.0))
    assert(almostEqual(inverseF(10000),8.414))

    assert(islower('')==''.islower())
    assert(islower('abc')=='abc'.islower())
    assert(islower('..a11bc!!')=='..a11bc!!'.islower())
    assert(islower('Abc')=='Abc'.islower())
    assert(islower('!Abzz')=='!Abzz'.islower())
    assert(islower('123')=='123'.islower())
    
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
##    graphicsMain()
    
if __name__ == "__main__":
    main()
