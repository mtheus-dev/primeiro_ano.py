#Criar máquina de venda de ingresso.

class MaquinaDeIngresso:
    #construtor
    def __init__ (self,valor_p,valor_s,valor_t):#valor_p,valor_s,valor_t
        #atributos
        self.preco = valor_p
        self.saldo = valor_s
        self.total = valor_t

        
#costruir objeto
maquina1 = MaquinaDeIngresso (10,11,5)
maquina2 = MaquinaDeIngresso (99,18,7)

print(maquina1.preco,maquina1.saldo,maquina1.total)
print(maquina2.preco,maquina2.saldo,maquina2.total)
