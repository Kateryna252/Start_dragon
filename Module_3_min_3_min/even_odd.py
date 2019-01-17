alist = [i for i in range(1, int(input("Enter number of list\n"))) if (i % 2 == 0 and i % 3 == 0) or (i % 2 != 0 and i % 5 ==0)]
print(alist)