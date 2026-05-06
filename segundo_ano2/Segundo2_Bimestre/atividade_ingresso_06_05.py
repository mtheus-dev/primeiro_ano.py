class ingresso:
    #construtor
    def __init__(self,valor):
        #atributos
        self.valor_ingresso = valor

    def exebir(self):
        print(f"o valor do ingresso é: {self.valor_ingresso}")


class ingresso_vip (ingresso):
    #construtor
    def __init__(self, valor,valor_adicinal):
        #atributos
        self.valor_adicinal_vip = valor_adicinal
        super().__init__(valor)

    def calculo_vip(self):
        return self.valor_ingresso + self.valor_adicinal_vip

    def exebir(self):
        super().exebir()
        print(f"O valor do ingresso VIP é: {self.calculo_vip()}")