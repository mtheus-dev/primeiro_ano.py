'''
PROGRAMA: FUNCIONAMENTO DO ENQUANTO - WHILE
PROGRAMA 6
autor:Matheus Henrique De Lima Soares 1B de informatica
'''

#Crie um algoritmo que mostre ao usuário um menu que ofereça opções para efetuar operações matemáticas (soma, subtração, multiplicação e divisão). O usuário deve escolher qual operação fazer, ao final o programa deve perguntar se o usuário quer efetuar nova operação ou sair do programa.
#versão só com while

'''while True:

    print("1-soma\n2-subtração\n3-multiplicação\n4-divisão")
    operacao = int(input("Digite o número da operçao que deseja fazer: "))

    if operacao == 1:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        resultado = n1 + n2
        print("O resultado da sua soma é",resultado)
    elif operacao == 2:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        resultado = n1 - n2
        print("O resultado da sua subtração é",resultado)
    elif operacao == 3:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        resultado =  n1 * n2
        print("O resultado da sua multiplicação é",resultado)
    elif operacao == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        resultado = n1 / n2
        print("O resultado da sua divisão é",resultado)
    else:
        print("você não escolheu nenhuma das operações")   

    resposta = input("Gostaria de fazer uma nova operação? S para sim e N para não ")
    if resposta == "s" or resposta == "S":
        continue
    else:
        print("Você optou por sair")
        break'''

#versão com while e for

while True:

    operacoes = [ '1-soma', '2-subtração', '3-multiplicação', '4-divisão']
    for menu in operacoes:
        print(menu)
    operacao = int(input("Digite o número da operçao que deseja fazer: "))

    if operacao == 1:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        resultado = n1 + n2
        print("O resultado da sua soma é",resultado)
    elif operacao == 2:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        resultado = n1 - n2
        print("O resultado da sua subtração é",resultado)
    elif operacao == 3:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        resultado =  n1 * n2
        print("O resultado da sua multiplicação é",resultado)
    elif operacao == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        resultado = n1 / n2
        print("O resultado da sua divisão é",resultado)
    else:
        print("você não escolheu nenhuma das operações")   

    resposta = input("Gostaria de fazer uma nova operação? S para sim e N para não ")
    if resposta == "s" or resposta == "S":
        continue
    else:
        print("Você optou por sair")
        break