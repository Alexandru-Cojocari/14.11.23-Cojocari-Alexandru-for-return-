x = float(input('x='))
n = int(input('n='))
suma = 1
for i in range(1, n + 1):
    suma += 1 / (i * x)

print('Suma=',suma)
