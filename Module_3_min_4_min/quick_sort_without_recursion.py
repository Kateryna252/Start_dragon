import random
n = int(input("Enter number of length of list\n"))

def Sort_list(alist):
    list1 = [i for i in range(4 + len(alist) // 2)]
    k = 0
    list1[0] = 0
    list1[1] = len(alist) - 1
    while (k >= 0):
        i = QuickSort(alist, list1[k], list1[k + 1])
        if(i != list1[k + 1]):right_part_left =i + 1
        else:right_part_left =list1[k + 1]
        right_part_right = list1[k + 1]
        left_part_left = list1[k]
        if(i != list1[k]):left_part_right =i - 1
        else:left_part_right =list1[k]
        k -= 2
        if (right_part_left != right_part_right):k += 2; list1[k] = right_part_left; list1[k + 1] = right_part_right
        if (left_part_left != left_part_right):k += 2; list1[k] = left_part_left; list1[k + 1] = left_part_right
    return

def QuickSort(alist, left, right):
    i = left
    j = right - 1
    while (True):
        while (alist[i] < alist[right]): i+=1
        while (alist[j] > alist[right] and j > left): j-=1
        if (i >= j): break
        alist[i],alist[j] = alist[j],alist[i]
    alist[right],alist[i]  = alist[i],alist[right]
    return i


list1 = [random.randint(0,n) for i in range(n)]
Sort_list(list1)
print(list1)