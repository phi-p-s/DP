import random
import time
import sys

class myPiece:
    def __init__(self):
        self.size = 0
        self.parent = [None, None]
        self.myChoice = None
        self.neighborChoice = None

    def setSize(self, x):
        self.size = x

    def setParent(self, par):
        self.parent = par
    
    def setMyChoice(self, par):
        self.myChoice = par
    
    def setNeighborChoice(self, nei):
        self.neighborChoice = nei
    
    def getSize(self):
        return self.size
    
    def getParent(self):
        return self.parent
    
    def getMyChoice(self):
        return self.myChoice
    
    def getNeighborChoice(self):
        return self.neighborChoice
    
    def getIndex(self):
        return self.index
    
def RecTimber(i, j):
    li = lengths[i]
    lj = lengths[j]
    global count 
    count += 1
    #BASE CASES
    if j == i:
        piece = li
    elif j == i+1:
        piece = max(li, lj)
    #Recurring Case
    else:
        piece = max(li + min(RecTimber(i+2, j), RecTimber(i+1, j-1)), lj + min(RecTimber(i+1, j-1), RecTimber(i, j-2)))
    return piece

def DPTimber(i, j):
    li = lengths[i]
    lj = lengths[j]
    global count 
    count += 1
    currentPiece = myPiece()
    #BASE CASES
    if j == i:
        currentPiece.setSize(li)
        currentPiece.setMyChoice(i)
    elif j == i+1:
        currentPiece.setSize(max(li, lj))
        if li >= lj:
            currentPiece.setMyChoice(i)
            currentPiece.setNeighborChoice(j)
        else:
            currentPiece.setMyChoice(j)
            currentPiece.setNeighborChoice(i)
    #Recurring Case
    else:
        #check to make sure its not in table
        dp20 = DPTable[i+2][j]
        dp20s = dp20.getSize()
        dp11 = DPTable[i+1][j-1]
        dp11s = dp11.getSize()
        dp02 = DPTable[i][j-2]
        dp02s = dp02.getSize()
        #if not calculated
        if dp20s == 0:
            dp20s = DPTimber(i+2, j)
        if dp11s == 0:
            dp11s = DPTimber(i+1, j-1)
        if dp02s == 0:
            dp02s = DPTimber(i, j-2)
        #Get the choices
        if li + min(dp20s, dp11s) >= lj + min(dp11s, dp02s):
            if dp20s <= dp11s:
                currentPiece.setParent([i+2, j])
                currentPiece.setNeighborChoice(i+1)
            else:
                currentPiece.setParent([i+1, j-1])
                currentPiece.setNeighborChoice(j)
            #left optimal is bigger than right optimal, so take left  
            currentPiece.setMyChoice(i)
        else:
            if dp11s <= dp02s:
                currentPiece.setParent([i+1, j-1])
                currentPiece.setNeighborChoice(i)
            else:
                currentPiece.setParent([i, j-2])
                currentPiece.setNeighborChoice(j-1)
            #right optimal is bigger than left optimal, so take right
            currentPiece.setMyChoice(j)
        currentPiece.setSize(max(li + min(dp20s, dp11s), lj + min(dp11s, dp02s)))
    DPTable[i][j] = currentPiece
    return currentPiece.size
    
def traceback(currentPiece):
    order.append(currentPiece.getMyChoice()+1)
    if currentPiece.getNeighborChoice() != None:
        order.append(currentPiece.getNeighborChoice()+1)
    nextIndex = currentPiece.getParent()
    if nextIndex != [None, None]:
        nextPiece = DPTable[nextIndex[0]][nextIndex[1]]
        traceback(nextPiece)

def generateLengths(n):
    lengths = []
    for i in range(n):
        x = random.randint(1, 1000)
        lengths.append(x)
    return lengths

def read_input(fname):
    f_input = open(fname, "r").read()
    n = int(f_input[0])
    input_t = f_input[2:]
    input_t = input_t.split(' ')
    for i in range(n):
        input_t[i] = int(input_t[i])
    return input_t

ns = [25]
for n in ns:
    runtimes = []
    for i in range(3):
        lengths = generateLengths(n)
        #lengths = [33, 28, 35, 25, 29, 34, 28]
        #lengths = [1, 1, 1, 1, 1]
        #print(lengths)
        #n = int(input())
        #lengths = list(map(int, input().split()))
        #n = len(lengths)
        DPTable = [[myPiece() for i in range(n)] for j in range(n)]
        count = 0
        start_time = time.time_ns()
        total = RecTimber(0, n-1)
        #total = DPTimber(0, n-1)
        runtime = round((time.time_ns() - start_time) * (10**-9), 6)
        '''for row in DPTable:
            for element in row:
                print(element.getSize(), end = " ")
            print("")'''

        #order = []
        #traceback(DPTable[0][n-1])
        #print(total)
        #for choice in order:
        #    print(choice, end = ' ')
        #print("Order: " + str(order))
        print("N: " + str(n))
        print("Count: " + str(count))
        #print("Total Length: " + str(total))
        print("Time in seconds: " + str(runtime))
        runtimes.append(runtime)
    avg = runtimes[0] + runtimes[1] + runtimes[2]
    avg = round(avg/3, 6)
    print("Avg: " + str(avg))
