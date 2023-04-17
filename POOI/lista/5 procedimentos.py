def MaiorMenorNum(numeros):
    maior = 0
    menor = numeros[-1]
    for x in range(0, len(numeros)):
        if numeros[x] > maior:
            maior = numeros[x]
            indiceMaior = x
        if numeros[x] < menor:
            menor = numeros[x]
            indiceMenor = x
    print(f'\nO maior valor é: {maior} e está na posição: {indiceMaior} \nO menor valor é: {menor} e está na posição: {indiceMenor}')


listaNumeros = list()
while True:
    x = int(input('Digite um numero: '))
    if x in listaNumeros:
        print('Digitou numero já digitado anteriormente')
        continue
    else:
        listaNumeros.append(x)
    if input('Se deseja continuar digite: s') == 's':
        continue
    else:
        break

MaiorMenorNum(listaNumeros)