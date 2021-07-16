from random import randint


class Carta():
    def __init__(self, naipe, val):
        self.naipe = naipe
        self.valor = val

    def retornar(self):
        print("{} de {}".format(self.valor, self.naipe))


class Gerador():
    def __init__(self):
        self.cartas = []
        self.construtor()

    def construtor(self):
        for n in ["Paus", "Copas", "Espadas", "Ouros"]:
            for v in range(1, 14):
                self.cartas.append(Carta(n, v))

    def retornar(self):
        for c in self.cartas:
            c.retornar()

    def embaralhador(self):
        for i in range(len(self.cartas)-1, 0, -1):
            r = randint(0, i)
            self.cartas[i], self.cartas[r] = self.cartas[r], self.cartas[i]

    def draw(self):
        return self.cartas.pop()



gerar = Gerador()
gerar.embaralhador()
gerar.retornar()



