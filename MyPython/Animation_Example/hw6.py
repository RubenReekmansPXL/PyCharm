#hw6   15-112
#Yujia Wang (yujiaw) Section A

"""
Part 2.
1.  f1(8,2)
    //((x>>y)<<y == x) implies the last 'y' digit of binary representation of x
    is 0; try y = 2, and x+y should be 10, so x =8; moreover 8 = 0b1000,
    so that fits
2.  f2(31,13)
    //((100>x>y>0) and (y == x%10*10 + x/10) implies y is in the reverse digit of x
    x+y == 44, possible solutions so far are 40,4; 31,13; and 31,13 fit the condition
    x%y == 5
3.  f3(67,1)
    //when y=1 is the easiest case, the equation x/2+x**y == 100 becomes
    x/2+x == 100, implies x = 67. That works
4.  f4(32,8)
    //x|y == x+y implies binary representation of x and y has no same digit in the
    same digit position. 40 = 0b101000, 100>x>y>0: so x = 0b100000=32, y = 0b1000=8
5.  f5(6,4)
    //round(float(x/y)) != round(float(x)/y) says x%y != 0, and x%y >=y/2
    so 6,4 would fit
6.  f6(18)
    //if (z % 7 == 0):  y += 1, implies y add 1 every time z is multiple of 7,
    below 20 there are 0, 7, 14 fit the condition. y would be added by 3 at last
    so x = 21-3 = 18
           
    
"""
def solvesCryptarithm(puzzle, solution):
    elements = readPuzzle(puzzle)
    a = evalStringValue(elements[0],solution)
    b = evalStringValue(elements[1],solution)
    c = evalStringValue(elements[2],solution)
    return (a+b==c)

##the readPuzzle reads the puzzle and returns a list of 3 strings
##readPuzzle("A+B=C") returns ['A','B','C'] 
def readPuzzle(puzzle):
    elements = []
    start = 0
    for i in xrange(len(puzzle)):
        if (ord(puzzle[i]) == ord('+')):
            elements.append(puzzle[0:i])
            start = i+1
        elif (ord(puzzle[i])==ord('=')):
            elements.append(puzzle[start:i])
            elements.append(puzzle[i+1:])
    return elements

##the function returns the string s's value based on the solution
def evalStringValue(s, solution):
    value = 0
    l = len(s)
    for i in xrange(l):
        try:
            digit = solution.index(s[i])
        except:
            print('invalid puzzle or solution!')
            return -1           
        value += digit*(10**(l-1-i))
    return value

##the function bestScrabbleScore(dictionary, letterScores, hand) that takes 3
##lists -- dictionary (a list of lowercase words), letterScores (a list of 26
##integers), and hand (a list of lowercase characters) -- and returns a tuple of
##the highest-scoring word in the dictionary that can be formed by some arrange
##of some subset of letters in the hand, followed by its score.     
def bestScrabbleScore(dictionary, letterScores, hand):
    bestScore = 0
    bestWordTuple = []
    #find the highest word score in dictionary and add to the result
    for i in xrange(len(dictionary)):           
        scoreWord = evalWord(dictionary[i], letterScores, hand)
        if (scoreWord > bestScore):
            bestScore = scoreWord
            bestWordTuple = []
            bestWordTuple.append(dictionary[i])
        elif (scoreWord == bestScore):
            bestWordTuple.append(dictionary[i])
    if (bestScore == 0): return None
    if (len(bestWordTuple)==1): result = [bestWordTuple[0],bestScore]
    else: result = (bestWordTuple, bestScore)
    return result

import copy
##return a word s points based on letterScores and hand.
def evalWord(s, letterScores, hand):
    handCopy = copy.copy(hand)
    value = 0
    l = len(s)
    for i in xrange(l):
        if(s[i] in handCopy):
            letterIndex = ord(s[i])-ord('a')
            value +=  letterScores[letterIndex]
            handCopy.remove(s[i])
        else:
            return 0
    return value

##ignore_rest
##Rule for memory game:
## An RxC rectangular grid is filled with random numbers such that each integer
## from 1 to RC/2 occurs exactly twice. Numbers are hidden. On each turn,
## the player uncovers two numbers. If they match, they are unhidden (so the
## player can see them). Play ends when all the numbers are unhidden. The score
## depends both on the number of incorrect guesses and the total time required.
## guess command requires two typing, like A1 then D3; also includes instruction
## command, help; and a cheat command: cheat, the total score decreases when
## cheating too much, exceed a particular number of times.
##
import random
#create board that store numbers
def create2dMemoryBoard(rows, cols):
    boardRaw = []
    board = []
    n = rows*cols
    if(n%2 == 1): boardRaw.insert(0,'*')
    for i in xrange(n/2):  #insert a number to random index
        boardRaw.insert(random.randint(0,len(boardRaw)), i)
        boardRaw.insert(random.randint(0,len(boardRaw)), i)
    for j in xrange(rows):
        board.append(boardRaw[(j*cols):((j+1)*cols)])
    return board

def create2dStateBoard(rows, cols, memoryBoard):
    #the board that stores the information if the number has been unhidden
    #1 represents unhidden, 0 represents hidden
    state=[]
    for row in xrange(rows):
        state += [[0]*cols]
        if '*' in memoryBoard[row]:
            n = memoryBoard[row].index('*')
            state[row][n] = 1
    return state

#print the current game diagram
def printGame(memoryBoard, stateBoard):
    print "\n**********************"
    (rows, cols) = (len(memoryBoard), len(memoryBoard[0]))
    printColLabels(memoryBoard)
    for row in xrange(rows):
        print "%2d" % (row+1),
        for col in xrange(cols):    
            if(stateBoard[row][col]==0):  #hidden number displays '-'
                print '-',
            elif(stateBoard[row][col]==1):
                print memoryBoard[row][col],
        print "%2d" % (row+1)
    printColLabels(memoryBoard)

#check if the guess is legal
def isLegalGuess(stateBoard, row, col):
    (rows, cols) = (len(stateBoard), len(stateBoard[0]))
    #out of bound
    if ((row < 0) or (row >= rows) or (col < 0) or (col >= cols)): return False
    #has already been unhidden
    if (stateBoard[row][col]==1): return False
    return True

import time
#the function will show the whole memory board for about 3 second
def cheatGame(memoryBoard):
    cheatState=[]
    (rows, cols) = (len(memoryBoard), len(memoryBoard[0]))
    for row in xrange(rows):
        cheatState += [[1]*cols]
    printGame(memoryBoard, cheatState)
    time.sleep(3)
    print "\n"*2000

def helpGame():
    print """
    This is an instruction for the game.
    
    In the beginning you will be shown a array of numbers for 3 seconds, try to
    remember their locations as much as possible. Then all the number turns
    into invisible. YOU DON'T NEED TO WORRY ABOUT THE STAR. Your job is to match
    the same numbers by entering your guess location. Every time you enter one
    guess, such as "A3", the number in that block will become unhidden;
,   then enter another guess, such as "D6", if the number in two blocks are
    not the same these numbers will go back to invisible again. Also, you can
    type "cheat" to see the whole diagram again for 3 seconds. But CAREFULLY!
    This action will decrease your points significantly! Or you can type "help"
    to see this instruction again. This doesn't kill your points. When you
    finishing finding out all the pairs, the game will evaluate your performance
    and give a score. The faster you matches all and the less you cheat, the
    higher points you will get.

    LET'S DO THIS!
    Command list:
    something like "1D" or "4A": Make a guess
                          cheat: Make a cheat to see the whole diagram again
                                 for 3 seconds
                           help: To see this instruction again
    """
    while True:
        prompt = "Press Enter to continue: "
        command = raw_input(prompt).upper()
        if command == '':
            break

        
def getGuess(memoryBoard, stateBoard, cheat):
    while True:
        prompt = "Enter your guess position for number: "
        guess = raw_input(prompt).upper()
        #guess is something like "A3"
        if (guess == 'CHEAT'):
            cheat[0] += 1
            cheatGame(memoryBoard)
            printGame(memoryBoard, stateBoard)
        elif (guess == 'HELP'):
            helpGame()
            printGame(memoryBoard, stateBoard)
        #make 2 digit legal
        elif(guess == '' or (not guess[0].isalpha()) or \
            (not ((len(guess)==2 and guess[1].isdigit()) or \
            (len(guess)==3 and guess[1].isdigit() and guess[2].isdigit())))):
            print "Wrong format!  Enter something like A3 or D5."
        else:
            col = ord(guess[0]) - ord('A')
            if (len(guess)==2):
                row = int(guess[1])-1
            #read potential 2 digits
            elif (len(guess)==3):
                row = int(guess[2])+ 10*int(gues[1])-1
            if (not isLegalGuess(stateBoard, row, col)):
                print "That is not a legal guess!  Try again."
            else:
                return (memoryBoard[row][col], row, col)

#if stateBoard[row1][col1] is 1, change to 0; if is 0, changing to 1        
def changeStateBoard(stateBoard, row, col):
    if(stateBoard[row][col]==0): stateBoard[row][col]=1
    elif(stateBoard[row][col]==1): stateBoard[row][col]=0

def isAllNumberUnhidden(stateBoard):
    (rows, cols) = (len(stateBoard), len(stateBoard[0]))
    for row in xrange(rows):
        for col in xrange(cols):
            if (stateBoard[row][col] ==0): return False
    return True

def playMemoryGame(rows, cols):
    memoryBoard = create2dMemoryBoard(rows, cols)
    stateBoard = create2dStateBoard(rows, cols, memoryBoard)
    cheat = [0]
    score = 0
    print "Welcome to play memory game! "
    helpGame()
    cheatGame(memoryBoard)
    printGame(memoryBoard, stateBoard)
    print "Time Start!"
    start = end = time.time()#record time
    while True:
        #read guest's command
        (guess1, row1, col1) = getGuess(memoryBoard, stateBoard, cheat)
        #update states
        changeStateBoard(stateBoard, row1, col1)
        printGame(memoryBoard, stateBoard)
        (guess2, row2, col2) = getGuess(memoryBoard, stateBoard, cheat)
        changeStateBoard(stateBoard, row2, col2)
        printGame(memoryBoard, stateBoard)
        if (guess1 == guess2):
            score += 4              #each successful guess worth 4 points
            print "Correct. Good job! Go on"
        else:
            print "Wrong! Try again, don't be upset."
            changeStateBoard(stateBoard, row1, col1)
            changeStateBoard(stateBoard, row2, col2)
        printGame(memoryBoard, stateBoard)
        if (isAllNumberUnhidden(stateBoard)):
            end = time.time()
            consumedTime = end-stare
            score = score - consumedTime/5 - cheat[0]*5
            #each cheat takes off 5 points
            print "Consumed time: %d second" % consumedTime
            print "Cheat times: %d" % cheat[0]
            print "Congratulations! You nailed all of them. \
                    \n Your score is %d" % score
            break
    print "Goodbye!"

def make2dList(rows, cols):
    a=[]
    for row in xrange(rows): a += [[0]*cols]
    return a

def hasMove(board, player):
    (rows, cols) = (len(board), len(board[0]))
    for row in xrange(rows):
        for col in xrange(cols):
            if (hasMoveFromCell(board, player, row, col)):
                return True
    return False

def hasMoveFromCell(board, player, startRow, startCol):
    (rows, cols) = (len(board), len(board[0]))
    if (board[startRow][startCol] != 0):
        return False
    for dir in xrange(8):
        if (hasMoveFromCellInDirection(board, player, startRow, startCol, dir)):
            return True
    return False

def hasMoveFromCellInDirection(board, player, startRow, startCol, dir):
    (rows, cols) = (len(board), len(board[0]))
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (drow,dcol) = dirs[dir]
    i = 1
    while True:
        row = (startRow + i*drow)%rows       #adjust to sandwich across the edge
        col = (startCol + i*dcol)%cols
        #print row, col
        if ((row < 0) or (row >= rows) or (col < 0) or (col >= cols)):
            return False
        elif (board[row][col] == 0):
            # no blanks allowed in a sandwich!
            return False
        elif (board[row][col] == player):
            # we found the other side of the 'sandwich'
            break
        else:
            # we found more 'meat' in the sandwich
            i += 1
    return (i > 1)

def makeMove(board, player, startRow, startCol):
    # assumes the player has a legal move from this cell
    (rows, cols) = (len(board), len(board[0]))
    for dir in xrange(8):
        if (hasMoveFromCellInDirection(board, player, startRow, startCol, dir)):
            makeMoveInDirection(board, player, startRow, startCol, dir)
    board[startRow][startCol] = player

def makeMoveInDirection(board, player, startRow, startCol, dir): #adjust
    (rows, cols) = (len(board), len(board[0]))
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (drow,dcol) = dirs[dir]
    i = 1
    while True:
        row = (startRow + i*drow)%rows
        col = (startCol + i*dcol)%cols
        if (board[row][col] == player):
            # we found the other side of the 'sandwich'
            break
        else:
            # we found more 'meat' in the sandwich, so flip it!
            board[row][col] = player
            i += 1

def getPlayerLabel(player):
    labels = ["-", "X", "O"]
    return labels[player]

def printColLabels(board):
    (rows, cols) = (len(board), len(board[0]))
    print "  ", # skip row label
    for col in xrange(cols): print chr(ord("A")+col),
    print

def printBoard(board, player): #add player parameter
    (rows, cols) = (len(board), len(board[0]))
    printColLabels(board)
    player1Score=0
    player2Score=0
    legalMoveList = getLegalMove(board, player)
    for row in xrange(rows):
        print "%2d" % (row+1),
        for col in xrange(cols):
            if [row,col] in legalMoveList:#print '.' for elements in legal move
                print '.',
            else: print getPlayerLabel(board[row][col]),
            if(board[row][col]==1):
                player1Score +=1
            elif(board[row][col]==2):
                player2Score +=1
        print "%2d" % (row+1)
    printColLabels(board)
    print('Score of Player X: %2d' % player1Score)
    print('Score of Player O: %2d' % player2Score)

def isLegalMove(board, player, row, col):
    (rows, cols) = (len(board), len(board[0]))
    if ((row < 0) or (row >= rows) or (col < 0) or (col >= cols)): return False
    return hasMoveFromCell(board, player, row, col)

def getMove(board, player):
    print "\n**************************"
    printBoard(board, player)
    while True:
        prompt = "Enter move for player " + getPlayerLabel(player) + ": "
        move = raw_input(prompt).upper()
        # move is something like "A3"
        if (move =="" or (not move[0].isalpha()) or \
            (not ((len(move)==2 and move[1].isdigit()) or \
            (len(move)==3 and move[1].isdigit() and move[2].isdigit())))):
            #make 2 digit legal
            print "Wrong format!  Enter something like A3 or D5."
        else:
            col = ord(move[0]) - ord('A')
            if (len(move)==2):
                row = int(move[1])-1
            elif (len(move)==3):
                row = int(move[2])+ 10*int(move[1])-1 #read potential 2 digits
            if (not isLegalMove(board, player, row, col)):
                print "That is not a legal move!  Try again."
            else:
                return (row, col)

import random

def getMoveAgainstRandomComputer(board, player):
    print "\n**************************"
    printBoard(board, player)
    legalMoveList = getLegalMove(board, player)
    while True:
        prompt = "Enter move for player " + getPlayerLabel(player) + ": "
        if(player == 1):
            move = raw_input(prompt).upper()
        elif(player == 2):              #get random move for computer
            moveRaw = legalMoveList[random.randint(0,len(legalMoveList)-1)]
            move = chr(ord('A')+moveRaw[1]) + str(moveRaw[0]+1)
            print('Computer takes move: %s'% move)
        # move is something like "A3"
        if (move =="" or (not move[0].isalpha()) or \
            (not ((len(move)==2 and move[1].isdigit()) or \
            (len(move)==3 and move[1].isdigit() and move[2].isdigit())))):
            #make 2 digit legal
            print "Wrong format!  Enter something like A3 or D5."
        else:
            legalMoveList = getLegalMove(board, player)
            col = ord(move[0]) - ord('A')
            if (len(move)==2):
                row = int(move[1])-1
            elif (len(move)==3):
                row = int(move[2])+ 10*int(move[1])-1
                #read potential 2 digits
            if (not isLegalMove(board, player, row, col)):
                print "That is not a legal move!  Try again."
            else:
                return (row, col)

def getLegalMove(board, player):  #get legal move for curret player
    (rows, cols) = (len(board), len(board[0]))
    legalMoveList = []
    for i in xrange(rows):
        for j in xrange(cols):
            if(isLegalMove(board, player, i,j)):
                legalMoveList.append([i,j])
    return legalMoveList

def playOthello(rows, cols):
    # create initial board
    board = make2dList(rows, cols)
    board[rows/2][cols/2] = board[rows/2-1][cols/2-1] = 1
    board[rows/2-1][cols/2] = board[rows/2][cols/2-1] = 2
    (currentPlayer, otherPlayer) = (1, 2)                       ####
    # and play until the game is over
    while True:
        if (hasMove(board, currentPlayer) == False):
            if (hasMove(board, otherPlayer)):
                print "No legal move!  PASS!"
                (currentPlayer, otherPlayer) = (otherPlayer, currentPlayer)
            else:
                print "No more legal moves for either player!  Game over!"
                printBoard(board, currentPlayer)
                break
        (row, col) = getMove(board, currentPlayer)
        makeMove(board, currentPlayer, row, col)
        (currentPlayer, otherPlayer) = (otherPlayer, currentPlayer)
    print "Goodbye!"

def playOthelloAgainstRandomComputer(rows, cols):
     # create initial board
    board = make2dList(rows, cols)
    board[rows/2][cols/2] = board[rows/2-1][cols/2-1] = 1
    board[rows/2-1][cols/2] = board[rows/2][cols/2-1] = 2
    (currentPlayer, otherPlayer) = (1, 2)                       ####
    # and play until the game is over
    while True:
        if (hasMove(board, currentPlayer) == False):
            if (hasMove(board, otherPlayer)):
                print "No legal move!  PASS!"
                (currentPlayer, otherPlayer) = (otherPlayer, currentPlayer)
            else:
                print "No more legal moves for either player!  Game over!"
                printBoard(board, currentPlayer)
                break
        (row, col) = getMoveAgainstRandomComputer(board, currentPlayer)
        makeMove(board, currentPlayer, row, col)
        (currentPlayer, otherPlayer) = (otherPlayer, currentPlayer)
    print "Goodbye!"

def runTest():
    assert (bestScrabbleScore(['a', 'b', 'c'], [1, 1, 1, 1, 1, 1, 1, 1, 1, \
                                                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
                                                1, 1, 1, 1, 1, 1, 1], ['z'])\
                                                ==None)
    print bestScrabbleScore(['xyz', 'zxy', 'zzy', 'yy', 'yx', 'wow'], [1, 2, 3, \
            4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1], \
            ['x', 'y', 'z'])
    assert( bestScrabbleScore(['xyz', 'zxy', 'zzy', 'yy', 'yx', 'wow'], [1, 2, 3, \
            4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1], \
            ['x', 'y', 'z'])== (['xyz', 'zxy'], 10))
    
    assert(readPuzzle('A+B=C')==['A','B','C'])
    assert(readPuzzle("SEND+MORE=MONEY")==['SEND','MORE','MONEY'])
    
    assert(evalStringValue('ABC','CBA-------')==210)
    assert(evalStringValue('ABC','CBD-------')==-1)

    assert(solvesCryptarithm('SEND+MORE=MONEY', 'OMY--ENDRS'))

    letterScores =  [ 1,  3,  3,  2,  1,  4,  2,  4,  1,  8,  5,  1,  3, \
                      1,  1,  3, 10,  1,  1,  1,  1,  4,  4,  8,  4,  10]
    hand =          ['a','b','c','d','e','f','g','h','i','j','k','l','m', \
                     'n','o','p','q','r','s','t','u','v','w','x','y','z']
    assert(evalWord('computer', letterScores, hand)==14)

    print('Passed all tests!')
    
def main():
    runTest()

if __name__ == "__main__":
    main() 
