import random
n = int(input("please write lenght of list\n"))
list1 = []
for i in range(n):
    list1.append(random.randint(0,n))
# print(set(list1))
list1_without_dublicates = []
for i in list1:
  if i not in list1_without_dublicates:
    list1_without_dublicates.append(i)
print(list1_without_dublicates)


