from collections import deque


class Fila:
    def __init__(self):
        self.__itens = deque()

    def insere(self, e):
        self.__itens.append(e)

    def remove(self):
        return self.__itens.popleft()

    def __len__(self):
        return len(self.__itens)

    def proximo(self):
        prox = self.__itens.popleft()
        self.__itens.appendleft(prox)
        return prox


def exibe(F):
    while len(F) > 0:
        print(F.remove())


F1 = Fila()

tamanho_fila = int(input("Quantos elementos você quer que sua fila tenha?"))
for x in range(tamanho_fila):
    F1.insere(x)

exibe(F1)
