#Criar máquina de venda de ingresso.

class MaquinaDeIngresso:
    #construtor
    def __init__ (self,valor_p):#valor_p,valor_s,valor_t
        #atributos  '
        self.preco = float(valor_p)
        self.saldo = 100
        self.total = 0
    
        #método
        #método acessor
    def preco (self):
        return self.preco
    
    #método modificador
    def definirPreco (self,novoPreco):
        self.preco = novoPreco

    def desconto (self,valor):
        self.preco -= valor

    def inserir_dinheiro(self,valor):
        if valor >= 0:
            self.saldo += valor
            print(f"O saldo atual é: {self.saldo}")
        
        else:
            print("O valor inserido é invalido.")
    
    def imprimir_ingresso(self):
        if self.saldo >= self.preco:
            print("=" * 20)
            print("=     Ingresso     =")
            print(f"= Preço: R$ {self.preco}=")
            print("=" *20)
            self.total += self.saldo
            self.saldo -=self.preco
            print(self.saldo)
        else:
            print("Saldo insuficiente")
         
    
