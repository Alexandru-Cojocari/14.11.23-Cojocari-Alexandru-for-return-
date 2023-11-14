n = int(input('n='))
suma = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        suma += i  


print('Suma numerelor divizibile la 2 până la', n,' este:' ,suma)
