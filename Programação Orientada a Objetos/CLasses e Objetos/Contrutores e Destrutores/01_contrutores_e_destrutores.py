class cachorro:
    def __init__(self, nome, idade, cor, acordado = True):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.acordado = acordado
    
    def __del__ (self):
        print("Removendo Instancia da classe")
    
    def falar (self):
        print("Au Au")

def criar_cachorro():
    c = cachorro("Amora",14,"Mesclada",False)
    print(c.nome)

#=cachorro ("Amora",14,"Mesclada",False)
#.falar()
criar_cachorro()