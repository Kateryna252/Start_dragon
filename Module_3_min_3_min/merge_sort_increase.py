import random
n = int(input("Enter number of lenght of list = \n"))
list1 = [random.randint(0, n) for j in range(0, n)]
print(list1)


def Merge(alist):
    def Sortgroup(alist, left, mid, right):
        if left >= right: return None
        if mid < left and mid > right : return None
        temp = left
        for j in range(mid+1, right+1):
            for i in range(temp,j):
                if alist[j]<alist[i]:
                    temp_elem = alist[j]
                    for k in range(j, i, -1):
                        alist[k] = alist[k-1]
                    alist[i] = temp_elem
                    temp = i
                    break
    if len(alist) < 2: return alist
    k = 1
    while k < len(alist):
        l = 0
        while l < len(alist):
            z = l + k + k-1
            r = z if z < len(alist) else len(alist) - 1
            Sortgroup(alist, l, l + k - 1, r)
            l += 2*k
        k *= 2
Merge(list1)
print(list1)