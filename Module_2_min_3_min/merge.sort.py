import random
list1 = []
n = int(input("Enter number of length of list:\n"))
for i in range(0,n):
    list1.append(random.randint(0,n))
def MergerSort(a):
    def MergerGroup(a, left, m, right):
        if left >= right:
            return None
        if m < left or right < m:
            return None
        t = left
        for j in range(m + 1, right + 1):
            for i in range(t, j):
                if a[j] > a[i]:
                    r = a[j]

                    for k in range(j, i, -1):
                        a[k] = a[k - 1]
                    a[i] = r
                    t = i
                    break

    if len(a) < 2: return None
    k = 1
    while k < len(a):
        g = 0
        while g < len(a):
            z = g + k + k - 1
            r = z if z < len(a) else len(a) - 1
            MergerGroup(a, g, g + k - 1, r)
            g += 2 * k
        k *= 2
MergerSort(list1)
print(list1)