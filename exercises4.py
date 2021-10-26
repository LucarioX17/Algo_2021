import random, math

print("\n" + "5:" + "\n")

moyenneList = [4, 3, 7, 10]

def moyenne(list):
    return min(list)

print("     " + str(moyenneList))
print("     " + "Lowest: " + str(moyenne(moyenneList)))

print("\n" + "6:" + "\n")

containList = [4, 7, 1, 5]
containNumber = 3

def contain(list, n):
    for i in list:
        if (i == n):
            return "     Contains: " + str(n)
        else:
            return "     Doesn't contain: " + str(n)

print("     " + str(containList))
print(contain(containList, containNumber))
print(contain(containList, containNumber+1))

print("\n" + "7:" + "\n")

counterList = [4, 10, 4, 3, 3]
counterNumber = 3

def counter(list, n):
    counter = 0
    for i in list:
        if (i == n):
            counter += 1
    return "     The number " + str(n) + " appears " + str(counter) + " time(s)"

print("     " + str(counterList))
print(counter(counterList, counterNumber))

print("\n" + "8:" + "\n")

ocurrenceList = [2, 10, 5, 2, 5, 2]

def ocurrence():
    counter = 0
    num = ocurrenceList[0]
    for i in ocurrenceList:
        currentN = ocurrenceList.count(i)
        if (currentN > counter):
            counter = currentN
            num = i
    return "The number " + str(num) + " appears the most amount of times"

print("     " + str(ocurrenceList))
print("     " + str(ocurrence()))

print("\n" + "9:" + "\n")

mergeList1 = [1, 2, 3]
mergeList2 = [4, 5, 6]

print("     " + str(mergeList1))
print("     " + str(mergeList2))
print("     " + "Merged lists: " + str(mergeList1 + mergeList2))

print("\n" + "10:" + "\n")

list = [1, 2, 3, 4, 5]
findList = [3, 5]

def finder(list, findList):
    appeared = 0
    for i in findList:
        for j in list:
            if (i == j):
                appeared += 1
    if (appeared == len(findList)):
        return "The numbers " + str(findList) + " appear in the list above"
    else:
        return "One or more numbers from this list, " + str(findList) + " don't appear in the list above"

print("     " + str(list))
print("     " + str(finder(list, findList)))

print("\n" + "11:" + "\n")

swapList = [1, 2, 3, 4, 5]

def swap(list):
    firstN = list[0]
    list[0] = list[len(list)-1]
    list[len(list)-1] = firstN
    return list

print("     " + "Swap numbers from list: ")
print("     " + str(swapList))
print("     " + str(swap(swapList)))

print("\n" + "12:" + "\n")

randomList = []
for _ in range(8):
    randomList.append(random.randint(0, 100))

def split(list):
    list1 = list[:len(list)//2]
    list2 = list[len(list)//2:]
    return list1, list2

def triFusion(list):
    print("     " + str(list))
    while (len(list) > 1):
        list, list2 = split(list)
        print("     " + str(list) + str(list2))

triFusion(randomList)

print("\n")

'''list1 = randomList[:len(randomList)//2]
    list2 = randomList[len(randomList)//2:]
    print("       " + str(list1) + "  " + str(list2))

    list3 = list1[:len(list1)//2]
    list4 = list1[len(list1)//2:]
    list5 = list2[:len(list2)//2]
    list6 = list2[len(list2)//2:]
    print("     " + str(list3) + "  " + str(list4) + "  " + str(list5) + "  " + str(list6))

    list7 = list3
    if (list7[0] > list7[1]):
        firstN = list7[0]
        list7[0] = list7[1]
        list7[1] = firstN

    list8 = list4
    if (list8[0] > list8[1]):
        firstN = list8[0]
        list8[0] = list8[1]
        list8[1] = firstN
    
    list9 = list5
    if (list9[0] > list9[1]):
        firstN = list9[0]
        list9[0] = list9[1]
        list9[1] = firstN
    
    list10 = list6
    if (list10[0] > list10[1]):
        firstN = list10[0]
        list10[0] = list10[1]
        list10[1] = firstN
    print("     " + str(list7) + "  " + str(list8) + "  " + str(list9) + "  " + str(list10))

    list11 = list7 + list8
    list11New = []
    list12 = list9 + list10
    list12New = []

    while list11:
        minimum = list11[0]
        for x in list11: 
            if x < minimum:
                minimum = x
        list11New.append(minimum)
        list11.remove(minimum)
    
    while list12:
        minimum = list12[0]
        for x in list12: 
            if x < minimum:
                minimum = x
        list12New.append(minimum)
        list12.remove(minimum)
    print("       " + str(list11New) + "  " + str(list12New))

    list13 = list11New + list12New
    list13New = []

    while list13:
        minimum = list13[0]
        for x in list13: 
            if x < minimum:
                minimum = x
        list13New.append(minimum)
        list13.remove(minimum)
    print("        " + str(list13New))
'''