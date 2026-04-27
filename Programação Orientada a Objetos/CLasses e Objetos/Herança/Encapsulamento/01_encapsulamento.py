class Conta:
    def __init__(self,nmro_agencia, saldo=0):
        self._saldo = saldo
        self.nmro_agencia = nmro_agencia
        pass
    def depositar(self, valor):
        self._saldo += valor
    def sacar(self, valor): 
        self._saldo-= valor
    def mostrar_saldo(self):
        return self._saldo 

conta1 = Conta("0001",1000)
conta1.depositar(500)
conta1.sacar(200)   
print(conta1.nmro_agencia)
print(conta1.mostrar_saldo())  
