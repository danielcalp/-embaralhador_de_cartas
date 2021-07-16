class Pilha():
    def __init__(self):
        self.__itens = []
        self.__tamanho = 0

    def insere(self, e):
        self.__itens.append(e)
        self.__tamanho += 1

    def remove(self):
        self.__tamanho -= 1
        return self.__itens.pop()

    def topo(self):
        return self.__itens[-1]

    def len(self):
        return self.__tamanho


def maiorvalorpar(pilha):
    listaPar = []
    for i in range(0, 7, 1):
        if pilha[i] % 2 == 0:
            listaPar.append(pilha[i])
        listaPar.sort()
    return listaPar[-1]


def novoRA(pilha):
    lista1 = []
    for i in range(0, 2, 1):
        pilha[i] *= -1
        lista1.append(pilha[i])
    lista1.append(0)
    for i in range(2, 7, 1):
        pilha[i] *= -1
        lista1.append(pilha[i])
    lista1.append(9)

    return lista1


pilha1 = Pilha()
lista = []

for i in range(0, 7, 1):
    lista.append(int(input('Digite um número do RA por vez: ')))
print("O maior numero par é:", maiorvalorpar(lista))
print("O seu novo RA é:", novoRA(lista))


