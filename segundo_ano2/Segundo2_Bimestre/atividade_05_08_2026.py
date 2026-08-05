class Endereco:
    #construtor
    def __init__(self,rua,cidade,estado):
    #atributos
        self.__logradoura = rua
        self.__cidade = cidade
        self.__estado = estado
    #métrodos

    def exebirEndereco(self):
        print("O endereço é: ")
        print("Rua:",self.__logradoura,"," ,self.__cidade,"-",self.__estado)

    def getconsultaLogradouro(self):
        return self.__logradoura

class Produto:
    def __init__(self,codigo,nome):
        self.codigo = codigo
        self.nome = nome

    def consultaNome(self):
        return self.nome

    def exebirProduto(self):
        print("nome do produto:" , self.nome)

class Pessoa:
    def __init__(self,nome:str,endereco:Endereco,numero:str):
        self.__nome = nome
        self.__numero = numero
        self.__endereco = endereco

    def consultaNome(self):
        return self.__nome

    def consultaEndereco(self):
        self.__endereco.exebirEndereco()

    def exebirPessoa(self):
        print("nome: ",self,self.consultaNome)
        self.consultaEndereco()
        print("número:",self.numero)

class Compra:
    def __init__(self):
        self.__pessoa = None
        self.__produto = None

    def Comorar(self,cliente,produto):
        self.pessoa = cliente
        self.produto = produto

    def exebirCompres(self):
        print(self.__pessoa.consultaNome(),"Comprou", self.__produto)