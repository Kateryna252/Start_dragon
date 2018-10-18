list1 = [int(i) for i in input('Enter the number through a space\n ').split()]
list_even = []
list_odd = []
for i in range(0, len(list1)):
    for j in range(1, len(list1)-i):
        if list1[j] >= list1[j-1]:
            list1[j-1], list1[j] = list1[j], list1[j-1]
for j in range(0,len(list1)):
    if list1[j]%2 == 0:
        list_even.append(list1[j])
    else:
        list_odd.append(list1[j])
print(list_even + list_odd)