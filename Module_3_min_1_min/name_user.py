answer = input("Hello, what is your name?\n ")
if answer.find('is')>-1:        #My name is ___
    name = answer[(answer.find('is')+2):]
    print('Hello {}'.format(name))
elif answer.find('am')>-1:      #I am _____
    name = answer[(answer.find('am') + 2):]
    print('Hello {}'.format(name))
else:
    print('Hello',answer)

