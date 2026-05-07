from abc import ABC, abstractmethod

class ControleRemoto:
    @abstractmethod
    def ligar (self):
        pass
    @abstractmethod
    def desligar(self):
        pass
class ControleRemotoTv(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
    def desligar(self):            
        print("Desligando a TV")

controle = ControleRemotoTv()
controle.ligar()
controle.desligar()
