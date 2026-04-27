class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade 
    
pessoa1 = Pessoa("Vinicius", 27)
print(pessoa1.nome)  # Acessando o nome usando a propriedade
print(pessoa1.idade)  # Acessando a idade usando a propriedade