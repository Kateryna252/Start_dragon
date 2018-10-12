from turtle import *
from math import *
a = int(input("Enter side a= ",))
b = int(input("Enter side b= ",))
c = int(input("Enter side c= ",))
t = Pen()
#трикутник
#нерівність трикутників
if (a < b+c) and (b < a+c) and (c < b+a):
    # теорема косинусів
    hama = (acos(((a*a) + (b*b) - (c*c))/(2*a*b)))*(180/pi)
    alfa = (acos(((c*c) + (b*b) - (a*a))/(2*c*b)))*(180/pi)
    beta = (acos(((c*c) + (a*a) - (b*b))/(2*c*a)))*(180/pi)
    t.forward(a)
    t.left(180-hama)
    t.forward(b)
    t.left(180-alfa)
    t.forward(c)
    t.left(180-beta)
else:
    print("Incorrect data!")
t.up()
t.backward(200)
t.down()
#квадрат
for i in range(4):
    t.forward(a)
    t.right(90)
done()




