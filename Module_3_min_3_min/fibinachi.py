n = int(input("Enter number of length of list \n"))


def fib(n):
    if n == 0: return 0
    elif n == 1 or n == 2: return 1
    else: return fib(n-1) + fib(n-2)


list1 = [fib(i) for i in range(n)]
print(list1)
