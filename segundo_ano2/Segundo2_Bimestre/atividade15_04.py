class Aquecedor:
    #construtor
    def __init__(self,minimo,maximo):
        #atributos
        self.temperatura = 15.0
        self.max = maximo
        self.min = minimo
        self.incremento = 5.0

    #Método aquecer
    def aquecer(self):
        self.temperatura += self.incremento
        if self.temperatura > self.max:
            self.temperatura = self.max
            print("A temperatura já alcançou o maximo possivel.")

    #Método esfriar
    def esfriar(self):
          self.temperatura -= self.incremento
          if self.temperatura < self.min:
            self.temperatura = self.min
            print("A temperatura já alcançou o minimo possivel.")

    def setincremento(self,valor_i):
        if valor_i > 0:
            self.incremento = valor_i

    def getTemperatura(self):
        return self.temperatura 
    
    def exibir(self):
        print(f"A temperatura do aquecedor é: {self.temperatura}")