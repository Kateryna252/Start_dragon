list_of_divisors = []
n = int(input("Enter number:\n"))
for i in range(1,n):
    if i%3 == 0 or i%5 == 0:
        list_of_divisors.append(i)
        for i in range(1, len(list_of_divisors)):
            tmp = list_of_divisors[i]
            i_index = i
            while i_index>0 and list_of_divisors[i_index-1]>tmp:
                list_of_divisors[i_index] = list_of_divisors[i_index-1]
                i_index = i_index-1
            list_of_divisors[i_index] = tmp
print(list_of_divisors)
