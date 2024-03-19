a = [1,2,3,4,5,6]
b= [3,4,6,7]
c = [1,2,2,2,3]
d = [2]

def printList(list1):
    for index in range(len(list1)):
        print(list1[index], "is in list 1")
'''
def arrayDiff(list1, list2):
    list3 = []
    index1 = range(len(list1))
    index2 = range(len(list2))
    for i in index1:
        if list1[i] not in list2:
            list3.append(list1[i])
    for i in index2:
        if list2[i] not in list1:
            list3.append(list2[i])
    return list3
'''
def arrayDiff(list1, list2):
    list3 = []
    index1 = range(len(list1))
    for i in index1:
        if list1[i] not in list2:
            list3.append(list1[i])
    return list3
e = arrayDiff(c, d)

print(e)



