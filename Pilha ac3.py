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

    def __len__(self):
        return self.__tamanho


pilha = Pilha()

while True:
    try:
        z = int(input('Digite um número do RA por vez: '))
        pilha.insere(z)
    except ValueError:
        break

pilha.insere(9)

for i in range(len(pilha)):
    print(pilha.remove(), end=',')
