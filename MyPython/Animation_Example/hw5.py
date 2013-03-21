#hw5
#Yujia Wang, yujiaw,
#due date: 2/18/2013

"""
Part a
a. Reasoning Over Code
1. f1('afkpu')
    //add every 5th letter in the lower case list, starting from 0
2. f2([6,8,5,7])
    //a is a number string composed of 5, 6, 7, 8
    multiply b 's element by 3, 2, 1, 0, seperately.
    so a = '6857'
3. f3(36, 8)
    //y = 2**(x/10); y*2**(x/10)+x == 100 which implies 4**(x/10) +x ==100
    try y = 8, x should be 3x, 36 would fit
4. f4('abcddad')
    //count for s[0] to s[3] is 2,1,1,3, try 'abcdaddxxxx'
    every 3rd, should be the same with element s[5] to s[3], the length of s should
    be between 7 and 9, s[0] = s[5], s[3] = s[4], s[6] = s[3]
    so s[0]=s[5], s[3]=s[4]=s[6]    "abcddad"would fit
5. f5(23)
    //c counts the factor's number of x, 28 has 1, 2, 4, 7, 14, 28: totally 6 factors
    decrease to the first prime, which is 23, y == x, so y should be 23
6. f6(8766)
    //r==6, implies the str(x) should be 78, 678, or 6678, digits can be in any order
    the biggest on it 8766, so n should be it
7. f7(6,2,-2)
    //length of s is 6, n=6; /t is whitespace, index is 2, so k=2;
    s.find('e') returns -1, s.find('b') returns 1, so x=2
8. f8('%+dabc%0.1f')
    //not much to say..
9. f9('degjn')
    //ord of s[i] should equal the previous one's ord plus index
    first one is 'd', so 'degjn'
10. f10('edc5b', 'ab5cd')
    //s from the second element is reverse of t from the 5th element to the second
    length of s is 5; try length of t equals 5, t[2] is '5'
    so t = 'ab2cd', s = 'edc2b'
11. f11([1,'1',2,'3',4,'7',8,'15'])
    //a should be a list, the even element should be string, the odd element should be
    int, add every 2nd number in a to s, the next number in a is equal to s
    try from a[0] = 1, so [1,'1',2,'3',4,'7',8,'15']
12. f12([0,1,3,5,2,4])
    //b ''
    i = a.1, a[i] = 1, a[i+1] = 3, a[i+2] = 5
    try i =1, a = [0,1,3,5,2,4]
    a from index i, i+1, i+2; b[1], b[3], b[5]; b = [0,1,2,3,4,5]
    a[i,i+1,i+2] = b[1,3,5] = [1,3,5];
b.
    a. TRUE
    b. FALSE
    c. FALSE
    d. TRUE
    e. FALSE
    f. FALSE
    g. TRUE
    h. FALSE 
    i. TRUE
    j. TRUE
c.
    a:  4,6,2,5,1,3,8,7
        4,6,  2,5,  1,3,  7,8
        2,4,5,6,  1,3,7,8   //half-way
        1,2,3,4,5,6,7,8
    b:  def f(s,t):
            return (a == b)
    c:  0.002*log_2(1000000) =  0.04 second
    d:  fa: Oh(n**2)
        fb: Oh(1)
        fc: Oh(n**3)
        fd: Oh(n)
    e:  accelerate expression evaluation
"""

def nearestHarshadNumber(n):
    nlower = n
    nhigher = n
    firstHarshadNumber = 10
    if (n<10): return firstHarshadNumber 
    if (isHarshadNumber(n)): return n;
    else:
        while(not isHarshadNumber(nlower)): #find the nearest lower HarshadNumber
            nlower -= 1 
            if(not isHarshadNumber(nhigher)): #find the nearest highter HarshadNumber
                nhigher += 1
            else: return nhigher
        return nlower
    return -1

def isHarshadNumber(n):         #check if n is a Harshad number
    if (n<=0): return False
    sumD = sumOfDigit(n)
    return (n%sumD == 0)

def sumOfDigit(n):          #compute the sum of digits in a number
    acc = 0
    while(n/10!=0):
        acc += n%10
        n = n/10
    acc += n
    return acc

def alternatingSum(list):
    acc = 0
    for i in xrange(len(list)):
        if i%2 == 0:        #add number
            acc += list[i]
        else:               #subtract number
            acc -= list[i]
    return acc

def mostCommonName(nameList):
    sortedList = sorted(nameList)
    maxCount = 0
    listCommonName = []
    i = 0
    while(i<len(sortedList)):                       #compute the number of times that common name appears
        count = sortedList.count(sortedList[i])
        if(count>maxCount): maxCount = count
        i += count
    i = 0
    while(i<len(sortedList)):
        count = sortedList.count(sortedList[i])     #count the number of ith name
        if(count == maxCount):                      #add to current Common name 
            listCommonName.append(sortedList[i])
        i += count
    if(len(listCommonName) == 1):
        return listCommonName[0]
    if (listCommonName != []):
        return listCommonName
    else:
        return None

def reverse(list):
    length = len(list)
    for i in xrange(length/2):          #swap top and end element
        temp = list[i]
        list[i] = list[length-1-i]
        list[length-1-i] = temp

def vectorSum(list1, list2):
    if(len(list1) != len(list2)): return False
    sumList = []
    for i in xrange(len(list1)):            #append sum to the new list
        sumList.append(list1[i]+list2[i])
    return sumList

def isSorted(list):
    i = 0
    length = len(list)
    if(length<2): return True
    while(list[i]-list[i+1]==0):        #find the first two different number
        if (i < length-2):
            i +=1
            continue
        else:
            return True
    signFirst = sign(list[i]-list[i+1]) #record the trend, increase or decrease
    while(i< length-1):
        signCurr = sign(list[i]-list[i+1]) #check if it follows the trend
        if (signCurr == 0 or signCurr == signFirst):
            i+=1
            continue
        else:
            return False
    return True

def sign(n):       #compute the signal of number
    if (n>0): return 1
    elif(n<0): return -1
    else: return 0

def duplicates(list):
    length = len(list)
    sortedList = sorted(list)
    dupList = []
    i = 0
    while(i<length-1):
        #find the duplicated number that is not in dupList
        if(sortedList[i]==sortedList[i+1] and (sortedList[i] not in dupList)):
            dupList.append(sortedList[i])
        i += 1
    return dupList

def dotProduct(list1, list2):
    length1 = len(list1)
    length2 = len(list2)
    length = min(length1, length2)
    acc = 0
    for i in xrange(length):
        acc += list1[i]*list2[i]
    return acc

import copy
def isRotation(list1, list2):
    if (list1==list2): return True
    if (len(list1)!=len(list2)): return False
    opList = copy.copy(list1)           #the operation should be non-constructively
    for i in xrange(len(list1)-1):
        n = opList.pop(0)               #rotate the list, check if they are same
        opList.append(n)
        if(opList == list2):
            return True
    return False

def subsetSum(list):
    n = len(list)
    i = 1
    subList = []
    while(i<2**n):
        acc = 0
        for j in xrange(n):      #add every number in the list corresponding to bit value of 1
            acc += list[j]*((i>>j)&1)
        if (acc==0):
            for j in xrange(n):  #append the found elements to the return list
                if (((i>>j)&1)==1):
                    subList.append(j)
            return subList
        i += 1
    if(subList != []):
        return subList
    else:
        return None

    
def runTest():
    #nearestHarshadNumber test
    assert(nearestHarshadNumber(0) == 10)
    assert(nearestHarshadNumber(10) == 10)
    assert(nearestHarshadNumber(11) == 10)
    assert(nearestHarshadNumber(14) == 12)
    assert(nearestHarshadNumber(15) == 12)
    assert(nearestHarshadNumber(16) == 18)
    #alternatingSum test
    assert(alternatingSum([5,3,8,4])==6)
    assert(alternatingSum([1,2,3,4,5])==3)
    #mostCommonName test
    assert(mostCommonName(["Jane", "Aaron", "Cindy", "Aaron"])=="Aaron")
    assert(mostCommonName(["Jane", "Aaron", "Jane", "Cindy", "Aaron"])==["Aaron", "Jane"])
    #reverse test
    a = [2,3,4]
    reverse(a)
    assert(a == [4,3,2])
    a = [10,100,1000,10000]
    reverse(a)
    assert(a == [10000,1000,100,10])
    #vectorSum test
    assert(vectorSum([2,4],[10,40])==[12,44])
    assert(vectorSum([1,2,3,4,5],[50,40,30,20,10])==[51,42,33,24,15])
    assert(vectorSum([2,3],[1])==False)
    #isSorted test
    assert(isSorted([])==True)
    assert(isSorted([1])==True)
    assert(isSorted([0,0,0,0,0,0])==True)
    assert(isSorted([1,1,1,1,1,1,2])==True)
    assert(isSorted([1,1,1,1,1,1,-1])==True)
    assert(isSorted([1,1,1,1,1,-1,1])==False)
    assert(isSorted([-1,2,3,4,4,10,1000])==True)
    assert(isSorted([-1,2,3,4,3,10,1000])==False)
    #duplicates test
    assert(duplicates([1,3,5,7,9,5,3,5,3])==[3,5])
    assert(duplicates([2,2,1,1,1,1,1,1,1,1,1,1])==[1,2])
    assert(duplicates([1,2,3,4,5,6,7,8])==[])
    assert(duplicates([])==[])
    #dotProduct test
    assert(dotProduct([1,2,3],[4,5,6])==32)
    assert(dotProduct([1,2,3],[4,5,6,4,56,7,89])==32)
    #isRotation test
    assert(isRotation([2,3,4,5,6], [4,5,6,2,3])==True)
    assert(isRotation([2,3,4,5,6], [2,3,4,5,6])==True)
    assert(isRotation([2,3,4,5,6], [4,5,6,2,3,4])==False)
    assert(isRotation([2,3,4,5,6], [6,2,3,4,5])==True)
    assert(isRotation([2,3,4,5,6], [4,6,5,2,3])==False)
    #subsetSum test
    assert(subsetSum([2,5,-13,-6,4,3])==[0,3,4])
    assert(subsetSum([2,5,100,-6,-2,3]) in [[0,4],[1,3,4,5]])
    assert(subsetSum([1,2,3,4,5]) == None)
    assert(subsetSum([1,0,2,3,4,5]) == [1])
    
    print("Passed all tests!!")

def main():
    runTest()

if __name__ == "__main__":
    main() 
