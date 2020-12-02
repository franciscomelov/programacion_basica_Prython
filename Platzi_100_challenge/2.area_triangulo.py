"""
Isoceles = 2 iguales  1 diferente
Equilatero = Todos iguales
Escaleno = Tofos diferentes
"""
from math import sqrt

def triangulo(a, b, c):
    if a == b and b==c and a == c:
        print("Equilatero")
        area = ( sqrt(3) / 4) * (a **2)
        print(f'El area es= {area}')
    elif a != b and b!=c and a!=c:
        print("Escaleno")
        s = (a+b+c) /2
        area = sqrt( s*(s-a)*(s-b)*(s-c) )
        print(f'El es area = {area}')
    else:
        print("Isoceles-")
        if [a,b,c].count(a) == 1:
            b=a
            a=c
        if [a,b,c].count(b) == 1:
            a = c
        else:
            b = c
        area = b * sqrt( a**2 -(b**2 / 4) ) /2
        print(f'El es area = {round(area, 2)}')
a = 5
b = 5
c = 5
triangulo(a, b, c)