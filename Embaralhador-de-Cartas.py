from random import randint


class Carta:
    def __init__(self, naipe, valor):
        print(valor)
        if valor == 0:
            self.valor = 1
        else:
            self.valor = valor
        Naipes = ['Paus', 'Copas', 'Espadas', 'Ouros']
        self.naipe = Naipes[naipe]

    def retornar(self, valor):
        cartas = {1: "A", 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: "Q", 12: "J", 13: "K"}
        return cartas[valor]

    def getNaipe(self):
        return self.naipe

    def getValor(self):
        return self.valor

    def compara(self, carta):
        if carta == 0 or carta == self.valor:
            print('Carta:', self.retornar(self.getValor()))
            print('Naipe:', self.getNaipe())
            return "A primeira carta {} é igual a segunda carta {}, o retorno é: {}".format(self.valor, carta, 0)
        elif carta < self.valor:
            print('Carta:', self.retornar(self.getValor()))
            print('Naipe:', self.getNaipe())
            return "A primeira carta {} é maior que a segunda carta {}, o retorno é: {}".format(self.valor, carta, 1)
        elif carta > self.valor:
            print('Carta:', self.retornar(self.getValor()))
            print('Naipe:', self.getNaipe())
            return "A primeira carta {} é menor que a segunda carta {}, o retorno é: {}".format(self.valor, carta, -1)


carta1 = Carta(randint(0, 3), randint(0, 12))
carta2 = Carta(randint(0, 3), randint(0, 12))

print('Comparação:', carta1.compara(carta2.getValor()))
