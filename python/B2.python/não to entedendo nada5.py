'''
PROGRAMA: FUNCIONAMENTO DO ENQUANTO - WHILE
PROGRAMA 5
autor:Matheus Henrique De Lima Soares 1B de informatica
'''

#Crie um algoritmo que solicite ao usuário números diversos até que ele escolha sair, depois disso ele deve obter a média dos números digitados.
#versão só com while

soma = 0
contador = 0
continuar = True
while continuar:
    numeros_escolhidos = input("Digite os números que queira tira a média ou 'sair' para encerrar o programa: ")

    if numeros_escolhidos == "sair":
        continuar = False
    else:
        numero = float(numeros_escolhidos)
        soma += numero
        contador += 1
        print("Número",numero,"adicionado.total de números:",contador)

if contador > 0:
    media = soma / contador

    print("Quantidade de números digitados: ",contador)
    print("Soma total:", soma)
    print("Média dos números:",media)
else:
    print("Nenum número foi digitado.")
