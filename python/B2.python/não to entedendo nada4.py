'''
PROGRAMA: FUNCIONAMENTO DO ENQUANTO - WHILE
PROGRAMA 4
autor:Matheus Henrique De Lima Soares 1B de informatica
'''

#Crie um algoritmo que solicite do usuário um número de 0 a 20 e mostre todos os números pares até chegar ao número escolhido começando em 0.

def numeros_pares():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    #versão só com o while
    resposta = "s"
    while resposta == "s":
        try:
            numero_escolhido = int(input("Digite um número de 0 a 20: "))

            while numero_escolhido < 0 or numero_escolhido > 20:
                print("Você digitou um número menor que 0 ou maior que 20: ")
                numero_escolhido = int(input("Digite um número de 0 a 20: "))   

            while numero_escolhido >= 0 and numero_escolhido <=20:
                if numero_escolhido % 2 == 0:
                    print(numero_escolhido)
                    numero_escolhido -= 2
                else:
                    numero_escolhido -= 1
                    print(numero_escolhido)
                    numero_escolhido -= 2
            resposta = input("Gostaria de roda esse programa de novo? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair: ")

def numeros_pares_for():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    #versão só com o for
    resposta = "s"
    while resposta == "s":
        try:
            numero_escolhido = int(input("Digite um número de 0 a 20: "))

            if numero_escolhido < 0 or numero_escolhido > 20:
                print("Você digitou um número menor que 0 ou maior que 20: ")
                numero_escolhido = int(input("Digite um número de 0 a 20: "))
            else:
                if numero_escolhido % 2 != 0:
                    numero_escolhido -= 1
                for i in range(numero_escolhido,-1,-2):
                    print(i)
            resposta = input("Gostaria de roda esse programa de novo? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair: ")    

def numeros_pares_while_for():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    #versão só com o while e for
        resposta = "s"
        while resposta == "s":
            try:
                numero_escolhido = int(input("Digite um número de 0 a 20: "))
                
                while numero_escolhido < 0 or numero_escolhido > 20:
                    print("Você digitou um número menor que 0 ou maior que 20: ")
                    numero_escolhido = int(input("Digite um número de 0 a 20: "))
                
                if numero_escolhido % 2 != 0:
                    numero_escolhido -= 1
                for i in range(numero_escolhido,-1,-2):
                    print(i)
                resposta = input("Gostaria de roda esse programa de novo? S para sim e N para não: ").lower()
            except ValueError:
                escreva("Tente novamente: ")
        escreva("Você optou por sair: ")


def menu():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    print("Escolha uma das opções abaixo: ")
    print("1 - Números pares só com while")
    print("2 - Números pares só com for")
    print("3 - Números pares com while e for")
    print("0 - Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        numeros_pares()
        menu()
    elif escolha == "2":
        numeros_pares_for()
        menu()
    elif escolha == "3":
        numeros_pares_while_for()
        menu()
    elif escolha == "0":
        escreva("Você optou por sair.")
    else:
        escreva("Opção inválida. Tente novamente.")
        menu()

#execução do programa
menu()
