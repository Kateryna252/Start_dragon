list1 = [int(i) for i in input("Enter list of number\n").split()]
print(list1)
for i in range(1, len(list1)):
    k = list1[i]
    j = i
    while j > 0 and list1[j-1] < k:
        list1[j] = list1[j-1]
        j = j - 1
        list1[j] = k
    print(list1)
