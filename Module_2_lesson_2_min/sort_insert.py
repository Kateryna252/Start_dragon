import random
list1 = []
n = int(input("Enter number of length of list:\n"))
for i in range(0, n):
    list1.append(random.randint(0,n))
print("Unsorted list:",list1)
for i in range(1, len(list1)):
    tmp = list1[i]
    i_tmp = i
    while i_tmp > 0 and list1[i_tmp-1] > tmp:
        list1[i_tmp] = list1[i_tmp- 1]
        i_tmp = i_tmp - 1
        list1[i_tmp] = tmp
print("Sorted list:  ",list1)


