class Estudante:
    escola = "DIO" # Atributo de classe

    def __init__(self, nome, matricula):
        self.nome = nome # Atributo de instancia
        self.matricula = matricula # Atributo de instancia  
    def __str__(self):
        return f"Nome: {self.nome} - Matricula: {self.matricula} - Escola: {self.escola}"
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

estudante1: Estudante = Estudante("João", 123)
estudante2 = Estudante("Maria", 456)    
mostrar_valores(estudante1, estudante2)

estudante1.matricula = 769
mostrar_valores(estudante1, estudante2)

