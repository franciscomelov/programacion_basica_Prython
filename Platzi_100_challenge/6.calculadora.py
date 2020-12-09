def calculadora(n1, op, n2):
    resultado = 0
    if op == "+": resultado = n1 + n2
    elif op == "-": resultado = n1 - n2
    elif op == "*": resultado = n1 * n2
    elif op == "/": resultado = n1 / n2
    elif op == "%": resultado = n1 % n2

    print(f'{n1} {op} {n2} = {resultado}')


n1 = 3
op = "%"
n2 = 11
calculadora(n1, op, n2)