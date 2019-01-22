import random
n = int(input("enter length of list\n"))
alist = [random.randint(0,n) for i in range(n)]
print(alist)


def quick_sort_with_recursion(list1):
    left_part = []
    right_part = []
    mid_part = []
    if len(list1) > 1:
        elem_list = random.choice(list1)
        for i in list1:
            if i < elem_list:
                left_part.append(i)
            if i == elem_list:
                mid_part.append(i)
            if i > elem_list:
                right_part.append(i)
        return quick_sort_with_recursion(left_part) + mid_part + quick_sort_with_recursion(right_part)
    else:
        return list1
print(quick_sort_with_recursion(alist))
