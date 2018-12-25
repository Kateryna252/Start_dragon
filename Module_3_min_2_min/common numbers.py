import random
list3 = []
n = int(input("write lenght of list1\n"))
m = int(input("write lenght of list2\n"))
list1 = [random.randint(0, m) for i in range(0, n)]
list2 = [random.randint(0, n) for j in range(0, m)]
for i in list1:
    for j in list2:
        if i == j:
            list3.append(i)
print(set(list3))


