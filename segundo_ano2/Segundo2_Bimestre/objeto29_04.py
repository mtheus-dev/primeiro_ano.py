from atividade29_04 import *

def escreva(mgs):
    tamanho = len(mgs) + 4
    print("_" * tamanho)
    print(f"  {mgs}")
    print("_" * tamanho)

deivid = pessoa("Deivid","Henrique de Oliveira", "desconhecido",17,69,1.73)

escreva("===EXEBIR PESSOA===")
deivid.exibir()

deivid = empregado("2025106060036",750,"Deivd","Henrique de Oliveira",17,"desconhecido",69,1.73)

escreva("===EXEBIR empregado===")
deivid.exibir()

deivid = chefe(1,"2025106060036",1000,"Deivd","Henrique de Oliveira",17,"desconhecido",69,1.73)

escreva("===EXEBIR chefe===")
deivid.exibir() 