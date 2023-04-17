def binario(numero):
    res = list()
    while numero >= 1:
        numero = int(numero)
        res.append(numero%2)
        numero = numero/2
    print(res)

num = float(input('Digite um número inteiro: '))

binario(num)
binario(59)

