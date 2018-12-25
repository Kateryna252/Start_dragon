list1 = [int(i) for i in input("please write number").split() ]
for i in range(1, len(list1)):
	list_i = list1[i]
	j = i
	while j>0 and list1[j-1]>list_i:
		list1[j] = list1[j-1]
		j = j-1
		list1[j] = list_i
print(list1)