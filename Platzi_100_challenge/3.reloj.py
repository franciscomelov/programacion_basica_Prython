def reloj(h,m):
    seg = h * 60 * 60
    seg += m*60
    print(f'Hay {seg} segundos')

h = 32
m = 20
reloj(h, m)