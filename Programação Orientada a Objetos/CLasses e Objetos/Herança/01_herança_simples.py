class Veiculo:
    def __init__(self,cor,placa,numero_rodas):
            self.numero_rodas = 0
            self.placa= placa
            self.cor = cor
    def ligar_motor(self):
        print("Ligando Motor")
    def __str__(self):
         return self.cor
class Motocicleta (Veiculo):
    pass
class Carro (Veiculo):
    pass

class Caminhao (Veiculo):
    def __init__(self,cor,placa,numero_rodas,carregado):
         super().__init__(cor,placa,numero_rodas)
         self.carregado = carregado
    def esta_carregado(self):
         print(f"{'Sim'if self.carregado else'Não'} está carregado")

moto = Motocicleta("Vermelha","ABC-1234",2)
moto.ligar_motor()

carro = Carro("Preto","DEF-5678",4)
carro.ligar_motor()

caminhao = Caminhao("Branco","GHI-9012",6,True)
caminhao.ligar_motor()
caminhao.esta_carregado()
