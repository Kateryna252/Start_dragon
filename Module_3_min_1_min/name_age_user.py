while True:
    name = input("Hello, what is your name?\n ")
    if name.find('is') > -1:  # My name is ___
        name = name[(name.find('is') + 2):]
    try:
        age = int(input('How old are you?\n'))
        hundred_years = 100 - age
        print('Dear {}, You will have 100 anniversary in {} years'.format(name, hundred_years))
        break
    except ValueError:
        print("please write years as number")
        continue
