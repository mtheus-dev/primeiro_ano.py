#Importando abstract base class - ab
from abc import ABC, abstractmethod

#criando class
class servidor(ABC):
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

    @abstractmethod
    def calculaRendimentos(self):
        pass

class professor(servidor):
    def __init__(self, nome, salario,turma):
        super().__init__(nome, salario)
        self.turma = turma

    def calculaRendimentos(self):
        return self.salario 
    
class chefe (servidor):
    def __init__(self, nome, salario,bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def calculaRendimentos(self):
        return self.salario + self.bonus
    