import random
import time
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
    #BASE CASES
    if j == i:
        piece = li
    elif j == i+1:
        piece = max(li, lj)
    #Recurring Case
    else:
        #check to make sure its not in table
        dp20 = DPTable[i+2][j]
        dp11 = DPTable[i+1][j-1]
        dp02 = DPTable[i][j-2]
        #if not calculated
        if dp20 == 0:
            dp20 = DPTimber(i+2, j)
        if dp11 == 0:
            dp11 = DPTimber(i+1, j-1)
        if dp02 == 0:
            dp02 = DPTimber(i, j-2)
        piece = max(li + min(dp20, dp11), lj + min(dp11, dp02))
    DPTable[i][j] = piece
    return piece
   
def generateLengths(n):
    lengths = []
    for i in range(n):
        x = random.randint(1, 1000)
        lengths.append(x)
    return lengths

lengths = generateLengths(20)
#lengths = [33, 28, 35, 25, 29, 34, 28, 32]
#lengths = [5, 6, 9, 7]
#print(lengths)
n = len(lengths)
DPTable = [[0 for i in range(n)] for j in range(n)]
count = 0

start_time = time.time_ns()
#total = RecTimber(0, n-1)
total = DPTimber(0, n-1)
runtime = round((time.time_ns() - start_time) * (10**-9), 6)
for row in DPTable:
    print(row)
print("Count: " + str(count))
print("Total Length: " + str(total))
print("Time in seconds: " + str(runtime))