class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade  
    @classmethod
    def criar_apartir_data_nascimento(cls,ano,mes,dia,nome):
        from datetime import date
        hoje = date.today()
        idade = hoje.year - ano - ((hoje.month, hoje.day) < (mes, dia))
        return Pessoa(nome, idade)
    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18

p1 = Pessoa.criar_apartir_data_nascimento(1990, 5, 15, 'João')
print(p1.nome)
print(p1.idade) 
print(Pessoa.e_maior_de_idade(p1.idade))
p2 = Pessoa.criar_apartir_data_nascimento(2005, 10, 20, 'Maria')
print(p2.nome)
print(p2.idade)
print(Pessoa.e_maior_de_idade(p2.idade))

