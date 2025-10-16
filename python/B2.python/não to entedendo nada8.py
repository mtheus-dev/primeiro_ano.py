'''
PROGRAMA: FUNCIONAMENTO DO ENQUANTO - WHILE
PROGRAMA 8
autor:Matheus Henrique De Lima Soares 1B de informatica
'''

#Crie um algoritmo que solicite do usuário um número, em seguida mostre todos os números em escala decrescente iniciando no número escolhido e terminando em 0.
#versão com while e for
def numeros_decrescente():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    #versão com while e for
    resposta = "s"
    while resposta == "s":
        try:
            numero = int(input("Digite um número: "))

            while numero < 0:
                print("Você digitou um número negativo")
                numero = int(input("Redigite o número: "))

            for i in range(numero,-1,-1):
                print(i)

            resposta = input("Gostaria de fazer de roda esse programa de novo? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Digite novamente: ")
    escreva("Você optou por sair")

def numeros_descrecente_while():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    #versão só com while
    resposta = "s"
    while resposta == "s":
        try:
            numero = int(input("Digite um número: "))

            while numero < 0:
                print("Você digitou um número negativo")
                numero = int(input("Redigite o número: "))

            contador = numero
            while contador >= 0:
                print(contador)
                contador -= 1
            resposta = input("Gostaria de fazer de roda esse programa de novo? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Digite novamente: ")
    escreva("Você optou por sair")

def numeros_decrescente_for():
    #versão só com for 
    numero = int(input("Digite um número: "))

    for i in range(numero,-1,-1):
        print(i)

def menu():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    print("Escolha uma das opções abaixo: ")
    print("1 - Números decrescente com while e for")
    print("2 - Números decrescente só com while")
    print("3 - Números decrescente só com for")
    print("0 - Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        numeros_decrescente()
    elif escolha == "2":
        numeros_descrecente_while()
    elif escolha == "3":
        numeros_decrescente_for()
    elif escolha == "0":
        escreva("Você optou por sair.")
    else:
        escreva("Opção inválida. Tente novamente.")

#execução do menu
menu() 
    