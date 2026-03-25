#Criar máquina de venda de ingresso.

class MaquinaDeIngresso:
    #construtor
    def __init__ (self,valor_p):#valor_p,valor_s,valor_t
        #atributos
        self.preco = float(valor_p)
        self.saldo = 0
        self.total = 0
    
        #método
        #método acessor
    def preco (self):
        return self.preco
    
    #método modificador
    def definirPreco (self,novoPreco):
        self.preco = novoPreco

    def imprimir_ingresso(self):
    novoPreco = float(input("Qual é o novo preço do ingresso?: "))

#costruir objeto

maquina1 = MaquinaDeIngresso ()
maquina2 = MaquinaDeIngresso ()