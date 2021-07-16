from random import randint

class Carta:
    def init(self, naipe, valor):
        if valor==0:
            self.valor = 1
        else:
            self.valor = valor
        lista_naipes = ['Paus', 'Copas', 'Espadas', 'Ouros']
        self.naipe = lista_naipes[naipe]

    def get_valor(self):
        return self.valor

    def get_naipe(self):
        return self.naipe

    def retorna_valor_carta(self, valor):
        cartas = {1:'A', 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:'Q', 12:'J', 13:'K'}
        return cartas[valor]

    def compara(self, carta):
        if carta==0 or carta==self.valor:
            print('Carta SELF:', self.retorna_valor_carta(self.get_valor()))
            print('Naipe:',self.get_naipe())
            return "Iguais - C1:", carta," - C:2", self.valor
        elif carta<self.valor:
            print('Carta SELF:', self.retorna_valor_carta(self.get_valor()))
            print('Naipe:',self.get_naipe())
            return "Maior que a primeira carta", 1
        elif carta>self.valor:
            print('Carta SELF:', self.retorna_valor_carta(self.get_valor()))
            print('Naipe:',self.get_naipe())
            return "Menor que a primeira carta",-1




carta1 = Carta(randint(0,3),randint(0,12)) # range(1,13) dá erro de Index Out Range, portanto foi usado o range(0,12)
carta2 = Carta(randint(0,3),randint(0,12)) 

print('Resultado comparação carta:',carta1.compara(carta2.get_valor()))