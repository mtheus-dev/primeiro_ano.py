
def escreva(mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)
class pessoa:
    #construtor
    def __init__(self,nome,sobrenome,genero,idade,peso,altura):
        #atributos
        self.altura = altura
        self.idade = idade
        self.peso = peso
        self.nome = nome
        self.sobrenome = sobrenome
        self.genero = genero

    def exibir(self):
        escreva(f"Bom dia {self.nome} {self.sobrenome} muito prazer em conhecer você.\nVocê tem {self.idade} anos, {self.altura} de altura e {self.peso} kilos\nSeu genero é {self.genero}")

class empregado(pessoa):
    #construtor
    def __init__(self,matricula,salario,nome,sobrenome,idade,genero,peso,altura):
        #atributos
        self.matricula = matricula
        self.salario = salario
        super().__init__(nome,sobrenome,genero,idade,peso,altura)

    def exibir(self):
        super().exibir()
        print(f"A sua matricula de emprego e {self.matricula} e seu salario é de {self.salario} reais")

class chefe(empregado):
    #construtor
    def __init__(self,bonus,matricula, salario, nome, sobrenome, idade, genero, peso, altura):
        #atributos
        self.bonus = bonus
        super().__init__(matricula, salario, nome, sobrenome, idade, genero, peso, altura)
        
    def calcula_bonus(self):
        return self.salario + self.bonus
    
    def exibir(self):
        super().exibir()
        print(f"Seu bonus é de {self.bonus} reais\no total recebido foi de {self.calcula_bonus()}")