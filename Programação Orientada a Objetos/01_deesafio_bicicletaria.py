class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

caloi = Bicicleta("vermelha", "caloi", 2020, 1500)

def buzinar(self):
    print("Buzinando: Plim Plim")

def parar (self): 
    print ("Parando a bicicleta")
    print ("Bicicleta parada")

def correr (self) : 
    print ("VRUMMMMMM")

b1 = Bicicleta("vermelha", "caloi", 2020, 1500)
#.buzinar()
#1.parar()
#1.correr()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta ("azul","monark", 2019, 1200)
#2.buzinar()
#2.parar()
b1.modelo
b2.modelo

b1.cor
b2.cor

b1.ano
b2.ano


def __str__(self):
    return f"{self.__class__.__name__}:[f'{chave}={valor}' for chave, valor in self.__dict__.items()]"
  