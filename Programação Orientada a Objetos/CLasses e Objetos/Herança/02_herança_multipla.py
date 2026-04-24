class Animal:
    def __init__(self, nmro_de_patas):
        self.nmro_de_patas = nmro_de_patas
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(f'{chave}={valor}' for chave, valor in self.__dict__.items())}"
    
class Mamifero(Animal):
    def __init__(self,cor_pelo,**kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
class Ave(Animal):
    def __init__(self,cor_bico,**kw):       
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Cachorro(Mamifero):
    pass
class Gato(Mamifero):
    pass
class Leaão(Mamifero):
    pass   
class ornitorrinco(Mamifero, Ave):
   def __init__(self,cor_bico,cor_pelo,nmro_de_patas):
        super().__init__(cor_bico=cor_bico,cor_pelo=cor_pelo,nmro_de_patas=nmro_de_patas)

Gato1 = Gato(cor_pelo='preto',nmro_de_patas=4)
print(Gato1)

ornitorrinco1 = ornitorrinco(cor_pelo='marrom',cor_bico='amarelo',nmro_de_patas=4)
print(ornitorrinco1)    