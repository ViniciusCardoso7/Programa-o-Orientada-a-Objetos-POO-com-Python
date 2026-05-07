# Defina a classe base Passaro
class Passaro:
    def voar(self):
        return "O pássaro está voando."

# Agora defina a subclasse pardal que herda de Passaro
class Pardal(Passaro):  # Corrigido: "Passaro" para "Passaro" (mas usei "Pardal" com maiúscula por convenção)
    def voar(self):  # Sobrescrevendo o método para polimorfismo
        return "O pardal está voando rapidamente."

# Exemplo de uso
passaro = Passaro()
pardal = Pardal()
print(passaro.voar())  # Saída: O pássaro está voando.
print(pardal.voar())   # Saída: O pardal está voando rapidamente.