nombre  = input("Como te llamas: ")
print("hola " + nombre)

edad = input("cuantos años tienes: ")
print("tienes " + edad + " años")

edad = int(edad)
if edad >= 18:
    print("eres mayor de edad")
else:
    print("Eres menor de edad")

""" 
Solamente se pueden concatenar string con string
si tienes un numero tienes que convertirlo a string

operadores numericos solo funcionan con numeros

Si preguntas al usuario su edad input()
reconoce el numero como string
edad = input("cual es tu edad: ")
si quieres hacer operaciones con con la variable edad
tienes que convertira a input
"""