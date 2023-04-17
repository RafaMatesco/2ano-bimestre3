def binario():
    numero = num
    res = list()
    dois = 2
    while numero >= 1:
        numero = int(numero)
        res.append(numero%2)
        numero = numero/2
        print(res)
        print(numero)
    #for v in res:
     #   print(v, end='')

num = float(input('Digite um número inteiro: '))
binario()

