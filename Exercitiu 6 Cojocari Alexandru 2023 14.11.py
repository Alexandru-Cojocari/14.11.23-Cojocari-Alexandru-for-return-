n = int(input('n='))
suma = 0
for i in range(1, n + 1):
    if (i % 3 == 0) and (i % 5 == 0):
        suma += i  


print('Suma numerelor divizibile la 3 si 5 până la', n,' este:' ,suma)