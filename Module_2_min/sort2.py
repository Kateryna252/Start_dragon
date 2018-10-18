list1 = [int(i) for i in input('Enter the number through a space\n ').split()]
for i in range(0,len(list1)):
    for i in range(1,len(list1)):
        if list1[i] <= list1[i-1]:
            list1[i-1],list1[i] = list1[i],list1[i-1]
print(list1)
