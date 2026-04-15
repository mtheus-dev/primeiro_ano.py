#from (nome do arquivo) import (nome da class)
from atividade15_04 import Aquecedor

def escreva (mgs):
    tamanho = len(mgs) + 4
    print("_" * tamanho)
    print(f"  {mgs}")
    print("_" * tamanho)

def esfriar_d(nome):
    nome.esfriar()
    escreva(f"A temperatura do aquecedor é: {nome.getTemperatura()}°C")

def aquecer_a(nome):
    nome.aquecer()
    escreva(f"A temperatura do aquecedor é: {nome.getTemperatura()}°C")

#objeto = NomeDaClass
aquecedor_comum = Aquecedor (9,35)
aquecedor_premium = Aquecedor (5,40)

esfriar_d(aquecedor_comum)