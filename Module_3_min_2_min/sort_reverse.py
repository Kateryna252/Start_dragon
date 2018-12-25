import random
n = int(input("please write number of lenght of list\n"))
list1 = [random.randint(0,n) for i in range(0,n)]
for i in range(1, len(list1)):
	list_i = list1[i]
	j = i
	while j>0 and list1[j-1]<list_i:
		list1[j] = list1[j-1]
		j = j-1
		list1[j] = list_i
print(list1)