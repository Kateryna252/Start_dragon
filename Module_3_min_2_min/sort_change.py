import random
n = int(input("please write number of lenght of list\n"))
list1 = [random.randint(0,n) for i in range(0,n)]
for i in range(0,len(list1)):
    for i in range(1,len(list1)):
        if list1[i] <= list1[i-1]:
            list1[i-1],list1[i] = list1[i],list1[i-1]
list2 = [ i for i in list1 if i % 2 == 0 ]
list3 = [ i for i in list1 if i % 2 != 0 ]
print(list3+list2)