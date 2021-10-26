print("\n" + "1:" + "\n")

multipleOf = 1
counter = 5
multiplesList = []

def multiples(m, count):
    for i in range(0, count*m, m):
        if (i % m == 0 and i < count and i > 0):
            multiplesList.append(i)
    print("     " + str(multiplesList))
    multiplesList.clear()
    m += 1
    count += 5
    if (m < 4): 
        multiples(m, count)

multiples(multipleOf, counter)

print("\n" + "2:" + "\n")

def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n-1)

print("     " + str(factorial(5)))

print("\n" + "3:" + "\n")

import random

def randomList():
    randomList = []
    for i in range(5):
        randomList.append(random.randint(-100, 100))
    print("     " + str(randomList))

    maxNumber = randomList[0]
    for i in randomList:
        if (i > maxNumber):
            maxNumber = i
    print("     " + str(maxNumber))

randomList()

print("\n" + "4:" + "\n")

ocurrenceList = [2, 10, 5, 2, 5, 2]

def ocurrence():
    counter = 0
    num = ocurrenceList[0]
    for i in ocurrenceList:
        currentN = ocurrenceList.count(i)
        if (currentN > counter):
            counter = currentN
            num = i
    return num

print("     " + str(ocurrenceList))
print("     " + str(ocurrence()))

#Git Test