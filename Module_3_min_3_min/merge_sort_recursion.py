import random


def Merge(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        leftpart = alist[:mid]
        rightpart = alist[mid:]

        Merge(leftpart)
        Merge(rightpart)

        i = 0
        j = 0
        k = 0
        while (i < len(leftpart)) and (j < len(rightpart)) :
            if leftpart[i] > rightpart[j]:
                alist[k] = leftpart[i]
                i += 1
            else:
                alist[k] = rightpart[j]
                j += 1
            k += 1

        while i < len(leftpart):
            alist[k] = leftpart[i]
            i += 1
            k += 1

        while j < len(rightpart):
            alist[k] = rightpart[j]
            j += 1
            k += 1


n = int(input('Enter number of lenght of list\n'))
alist = [random.randint(0, n) for i in range(0,n)]
print(alist)

Merge(alist)
print(alist)
