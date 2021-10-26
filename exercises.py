print("\n" + "First exercise:" + "\n")

multipleOf = 7
counter = 100
table1 = []
table2 = []
table3 = []

def multiples(m, count, list1, list2, list3):
    listCounter = 0
    listIndex = 0
    for i in range(0, count*m, m):
        if (i % m == 0 and i < count):
            listCounter += 1

            if (listIndex == 0):
                list1.append(i)
            if (listIndex == 1):
                list2.append(i)
            if (listIndex == 2):
                list3.append(i)
            
            if (listCounter == count / 20):
                listIndex += 1
                listCounter = 0

            print(i)

multiples(multipleOf, counter, table1, table2, table3)

print("\n" + "Second exercise:" + "\n")

print(" " + str(table1))
print(table2)
print(table3)

#Git Test