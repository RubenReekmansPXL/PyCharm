# hw1.py
#

######################################################################
# Place your solutions here (and your test functions below)
######################################################################

def ceiling(n):
    # We'll require that n be positive since this only works in that case.
    assert(n >= 0)
    # This uses "boolean arithmetic", which is not recommended, but
    # we are using it here as a workaround for not having conditionals yet
    return int(n) + (n % 1 > 0)

def kthDigit(x, k):
    return abs(x/(10**k))%10

def numberOfPoolBalls(rows):
    return (rows**2+rows)/2

def numberOfPoolBallRows(balls):
    return ceiling((-1+(1+8*balls)**.5)/2)

def isEvenPositiveInt(x):
    return type(x)==int and x>0 and x%2 == 0

def isPerfectCube(x):
    return abs(x)**(1.0/3)%1 == 0

def isTriangular(x):
    return x>=0 and((-1+(1+8*x)**.5)/2)%1 == 0

def fabricYards(inches):
    return ceiling(inches/36.0)
 
def fabricExcess(inches):
    return (36 - inches%36)*(inches%36 != 0)

def nearestBusStop(street):
    return 8*(int(round(street/8.0))-(street%8==4))

def areCollinear(x1, y1, x2, y2, x3, y3):
    return (x1 == x2 and x2 == x3) or  (((not(x1 == x2)) and (not(x1==x3))) and ((y2-y1)/float(x2-x1) == (not(x1==x3))*(y3-y1)/float(x3-x1)))

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

def testKthDigit():
    print "Testing kthDigit()...",
    assert(kthDigit(789, 0) == 9)
    assert(kthDigit(789, 1) == 8)
    assert(kthDigit(789, 2) == 7)
    assert(kthDigit(789, 3) == 0)
    assert(kthDigit(-789, 0) == 9)
    print "Passed!"

def testNumberOfPoolBalls():
    print "Testing numberOfPoolBalls()...",
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 1+2)
    assert(numberOfPoolBalls(3) == 1+2+3)
    assert(numberOfPoolBalls(10) == 55)
    print "Passed!"

def testNumberOfPoolBallRows():
    print "Testing numberOfPoolBallRows()...",
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(54) == 10)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print "Passed!"
 
def testIsEvenPositiveInt():
    print "Testing isEvenPositiveInt()...",
    assert(isEvenPositiveInt(2) == True)
    assert(isEvenPositiveInt(2040608) == True)
    assert(isEvenPositiveInt(21) == False)
    assert(isEvenPositiveInt(20406081) == False)
    assert(isEvenPositiveInt(0) == False)
    assert(isEvenPositiveInt(-2) == False)
    assert(isEvenPositiveInt(-2040608) == False)
    assert(isEvenPositiveInt("Go Steelers!") == False)
    assert(isEvenPositiveInt(1.23456) == False)
    assert(isEvenPositiveInt(True) == False)
    print "Passed!"
 
def testIsPerfectCube():
    print "Testing isPerfectCube()...",
    assert(isPerfectCube(0) == True)
    assert(isPerfectCube(1) == True)
    assert(isPerfectCube(-1) == True)
    assert(isPerfectCube(8) == True)
    assert(isPerfectCube(-8) == True)
    assert(isPerfectCube(27) == True)
    assert(isPerfectCube(-27) == True)
    assert(isPerfectCube(16) == False)
    assert(isPerfectCube(-16) == False)
    print "Passed!"
 
def testIsTriangular():
    print "Testing isTriangular()...",
    assert(isTriangular(0) == True)
    assert(isTriangular(1) == True)
    assert(isTriangular(2) == False)
    assert(isTriangular(3) == True)
    assert(isTriangular(4) == False)
    assert(isTriangular(5) == False)
    assert(isTriangular(6) == True)
    assert(isTriangular(54) == False)
    assert(isTriangular(55) == True)
    assert(isTriangular(56) == False)
    assert(isTriangular(-1) == False)
    print "Passed!"
 
def testFabricYards():
    print "Testing fabricYards... ",
    assert(fabricYards(0) == 0)
    assert(fabricYards(1) == 1)
    assert(fabricYards(35) == 1)
    assert(fabricYards(36) == 1)
    assert(fabricYards(37) == 2)
    assert(fabricYards(72) == 2)
    assert(fabricYards(73) == 3)
    assert(fabricYards(108) == 3)
    assert(fabricYards(109) == 4)
    print "Passed all tests!"
 
def testFabricExcess():
    print "Testing fabricExcess... ",
    assert(fabricExcess(0) == 0)
    assert(fabricExcess(1) == 35)
    assert(fabricExcess(35) == 1)
    assert(fabricExcess(36) == 0)
    assert(fabricExcess(37) == 35)
    assert(fabricExcess(72) == 0)
    assert(fabricExcess(73) == 35)
    assert(fabricExcess(108) == 0)
    assert(fabricExcess(109) == 35)
    print "Passed all tests!"

def testNearestBusStop():
    print "Testing nearestBusStop()...",
    assert(nearestBusStop(0) == 0)
    assert(nearestBusStop(4) == 0)
    assert(nearestBusStop(5) == 8)
    assert(nearestBusStop(12) == 8)
    assert(nearestBusStop(13) == 16)
    assert(nearestBusStop(20) == 16)
    assert(nearestBusStop(21) == 24)
    print "Passed all tests!"
 
def testAreCollinear():
    print "Testing areCollinear()...",
    assert(areCollinear(0, 0, 1, 1, 2, 2) == True)
    assert(areCollinear(0, 0, 1, 1, 2, 3) == False)
    assert(areCollinear(1, 1, 0, 0, 2, 2) == True)
    assert(areCollinear(1, 1, 0, -1, 2, 2) == False)
    assert(areCollinear(2, 0, 2, 1, 2, 2) == True)
    assert(areCollinear(2, 0, 2, 1, 3, 2) == False)
    assert(areCollinear(3, 0, 2, 1, 3, 2) == False)
    assert(areCollinear(1, 1, 1, 2, 1, 4) == True)
    print "Passed all tests!"

def testAll():
    testKthDigit()
    testNumberOfPoolBalls()
    testNumberOfPoolBallRows()
    testIsEvenPositiveInt()
    testIsPerfectCube()
    testIsTriangular()
    testFabricYards()
    testFabricExcess()
    testNearestBusStop()
    testAreCollinear()

if __name__ == "__main__":
    testAll()
