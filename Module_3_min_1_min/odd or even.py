while True:
    try:
        number = int(input('write please a number\n'))
        if number %2==0:
            print("This number is even\n")
            break
        print("This number is odd\n")
        break
    except ValueError:
        print("please write number as integer number")
        continue
