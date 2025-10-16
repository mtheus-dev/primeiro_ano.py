'''
PROGRAMA: FUNCIONAMENTO DO ENQUANTO - WHILE
PROGRAMA 7
autor:Matheus Henrique De Lima Soares 1B de informatica
'''

#Crie um algoritmo que solicite do usuário um número. Some todos os números de 0 até o número escolhido e mostre o resultado na tela.
#versão com while e for
def soma_numeros_1():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    #versão com while e for
    while True:
        try:
            numero = int(input("Digite um número: "))
            total = 0

            for i in range(0,numero+1,1):
                print(i)
                total += i
            print(total)
            resposta = input("Gostaria de repetir? S para sim e N para não ").lower()
            if resposta != "s":
                escreva("Você optou por sair")
                break
        except ValueError:
            escreva("Digite novamente: ")
        
#versão só com while
def soma_numeros_2():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    #versão só com while
    while True:
        try:
            numero = int(input("Digite um número: "))
            total = 0
            contador = numero

            while contador >= 0:
                print(contador)
                total += contador
                contador -= 1
            print(total)

            resposta = input("Gostaria de repetir? S para sim e N para não ").lower()

            if resposta != "s":
                escreva("Você optou por sair")
                break
        except ValueError:
            escreva("Digite novamente: ")

def menu():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    escreva("Escolha uma das opções abaixo: ")
    print("1 - Soma números com for")
    print("2 - Soma números com while")
    print("0 - Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        soma_numeros_1()
        menu()
    elif escolha == "2":
        soma_numeros_2()
        menu()
    elif escolha == "0":
        escreva("Você optou por sair.")
    else:
        escreva("Opção inválida. Tente novamente.")
        menu()

#execução do menu
menu()