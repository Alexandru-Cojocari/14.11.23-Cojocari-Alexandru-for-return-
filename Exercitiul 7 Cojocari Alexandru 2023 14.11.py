for n in range(100, 600):
    cifra_sute = n // 100
    cifra_zeci = (n // 10) % 10
    cifra_unitati = n % 10

    if cifra_sute < cifra_zeci < cifra_unitati and cifra_sute + cifra_zeci + cifra_unitati == 18:
        print(n,end=' ')
