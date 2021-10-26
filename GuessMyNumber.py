import random, os, time, math
os.system("cls")

randNum = random.randint(0, 100)

print("\n" + "GUESS THE NUMBER BETWEEN 0-100:" + "\n")

guess = int(input())

startTimer = time.time()
counter = 1

while guess != randNum:
    if (guess > randNum):
        print("\n Lower \n")
    elif (guess < randNum):
        print("\n Higher \n")

    guess = int(input())
    counter += 1

print("\n You Won!")
print(" Timer: " + str(math.floor(time.time() - startTimer)) + " seconds")
print(" Steps: " + str(counter))