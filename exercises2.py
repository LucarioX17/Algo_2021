print("\n" + "First exercise:" + "\n")

multipleOf = 1
counter = 5
multiplesList = []

def multiples(m, count):
    for i in range(0, count*m, m):
        if (i % m == 0 and i < count and i > 0):
            multiplesList.append(i)
    print(multiplesList)
    multiplesList.clear()
    m += 1
    count += 5
    if (m < 4): 
        multiples(m, count)

multiples(multipleOf, counter)

print("\n" + "Second exercise:" + "\n")

import random

def randomList():
    randomList = []
    for i in range(5):
        randomList.append(random.randint(-100, 100))
    print(randomList)

    maxNumber = randomList[0]
    for i in randomList:
        if (i > maxNumber):
            maxNumber = i
    print(maxNumber)

randomList()

print("\n" + "Third exercise:" + "\n")

def fibo(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(8))

#Git Test