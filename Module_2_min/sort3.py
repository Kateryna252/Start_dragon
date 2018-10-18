list1 = [87, 87, 5, 54, 21, 12, 45, 64, 87]
for i in range(0,len(list1)):
    for j in range(1,len(list1)-i):
        print(j)
        if list1[j] > list1[j-1]:
            tmp = list1[j]
            list1[j] = list1[j-1]
            list1[j-1] = tmp
print(list1)
