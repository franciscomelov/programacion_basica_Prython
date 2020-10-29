# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
# cambiar a f"{}" - f-string

#Opcion 1 - Con funcion
def run(a,b):
    print("""{}
{}
{}""".format(a+b,a-b,a*b))

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    run(a,b)

#opcion 2   *******
a = 4
b = 2
print(a + b)
print(a - b)
print(a * b)

#Opcion 2 - .format()
a = 4
b = 2

print("""{}
{}
{}""".format(a+b,a-b,a*b))

""" 
Instrucciones:
Vas a recibir dos valores (a, b)
y vas a retornar el resultado de 3 operaciones en tres lineas diferentes
suma
resta
multiplicacion

Ejemplo:
a = 4
b = 2

Resultado:
6
2
8
 
 """