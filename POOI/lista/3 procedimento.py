def primo(numero):
    cont = 0
    i = 0
    while i <= numero or cont < 2:
        i = i + 1
        x = numero % i
        if x == 0:
            cont = cont + 1

    if cont <= 2:
        print("primo")
    else:
        print("não primo")


num = int(input('Digite um número inteiro: '))


if num < 2:
        print("não primo")
else:
    primo(num)


