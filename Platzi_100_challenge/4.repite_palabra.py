
def repitiendo(text, n):
    if n == 0:
        return

    print(n, text)
    repitiendo(text, n-1)

text = "recursividad"
n = 10

repitiendo(text, n)