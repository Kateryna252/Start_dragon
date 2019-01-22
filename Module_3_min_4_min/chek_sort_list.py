list1 = [1,2,3,5,6,7,10,11]


def check_list(alist):
    if all(alist[i] <= alist[i+1] for i in range(len(alist)-1)):
        return print("It`s sorted list")
    elif all(alist[i] >= alist[i + 1] for i in range(len(alist) - 1)):
        return print("It`s sorted list")
    return print("It`s unsorted list")


check_list(list1)
