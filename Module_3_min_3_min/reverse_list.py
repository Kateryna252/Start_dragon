alist = [12, 5, 4, 9, 63, 4, 12, 3, 4, 6]


def rev(a):
    if len(a) == 0:
        return a
    return [a[-1]] + rev(a[:-1])


print(rev(alist))

