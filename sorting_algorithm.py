#BUBBLE SORT DEMO
#list1=[67,45,2,13,1,998]
#list2=[89,23,33,45,10,12,45,45,45]

def bubbleSort(myList):
    for x in range (0, len(myList) -1):
        for y in range (0, len(myList) -1 - x):
            if myList[y] > myList[y+1]:
                myList[y], myList[y+1] = myList[y+1], myList[y]
    return myList

myList = [67,45,2,13,1,998]
print(bubbleSort(myList))

myList2 = [89,23,33,45,10,12,45,45,45]
print(bubbleSort(myList2))
