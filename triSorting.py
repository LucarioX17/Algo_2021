print("\n" + "Selection Sorting:" + "\n")

selectionList = [2, 5, 1, 3, 4]

def selection(list):
    res = []
    rang = len(selectionList)

    for i in range(rang):
        lowestNumber = list[0]
        for i in list:
            if i < lowestNumber:
                lowestNumber = i
        res.append(lowestNumber)
        list.remove(lowestNumber)

    return res

print(selectionList)
print(selection(selectionList))

print("\n" + "Quick Sorting:" + "\n")

quickList = [7, 10, 6, 8, 9]

def quick(list):
    less = []
    equal = []
    greater = []

    if len(list) > 1:
        pivot = list[0]
        for x in list:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick(less)+equal+quick(greater)
    else:
        return list

print(quickList)
print(quick(quickList))