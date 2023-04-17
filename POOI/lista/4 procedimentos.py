def areaTotal(*casa):
    comodos = casa[0]
    comprimentos = casa[1]
    larguras = casa[2]
    areaComodo = list()
    areaTotalCasa = 0
    for y in range(0,qntComodos):
        areaComodo.append(comprimentos[y] * larguras[y])
        print(f'Nome do comodo: {comodos[y]}, comprimento: {comprimentos[y]}, largura: {larguras[y]}, área do cômodo: {areaComodo[y]}')
        areaTotalCasa += areaComodo[y]
    print(f'A casa tem {areaTotalCasa}m²')



qntComodos = int(input('Digite quantos cômodos serão inseridos:'))
x = 0
comodos = list()
comprimentos = list()
larguras = list()

while x < qntComodos:
        comodos.append(input('Nome do cômodo: '))
        comprimentos.append(int(input('Comprimento: ')))
        larguras.append(int(input('Largura: ')))
        x += 1

areaTotal(comodos, comprimentos, larguras)
