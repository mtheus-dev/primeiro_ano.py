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
        print(f"bom dia {self.nome} {self.sobrenome} muito prazer em conhecer você.")
        print(f"Você tem {self.idade} anos, {self.altura} de altura e {self.peso} kilos")
        print(f"Seu genero é {self.genero}")

class empregado(pessoa):
    #construtor
    def __init__(self,matricula,salario,nome,sobrenome,idade,genero,peso,altura):
        #atributos
        self.matricula = matricula
        self.salario = salario
        super().__init__(nome,sobrenome,idade,peso,altura,genero)

    def exibir(self):
        super().exibir()
        print(f"A sua matricula de emprego e {self.matricula} e seu e de {self.salario} reais")