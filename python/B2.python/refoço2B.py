'''
PROGRAMA: FUNCIONAMENTO DO ENQUANTO - WHILE
DATA: 21/06/2025
autor:Matheus Henrique De Lima Soares 1B de informatica
'''
#1)Crie um algoritmo que solicite um número do usuário e faça a tabuada de 1 a 10 deste número, em seguida pergunte se o usuário quer fazer a tabuada de outro número.
def tabuada():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    #versão só com while
    resposta = "s"
    while resposta == "s":
        try:
            num_escolhido = int(input("Digite um número que deseje a tabuada: "))
            i = 1
            while i< 11:
                resultado = num_escolhido * i
                print(num_escolhido, "x", i,"=", resultado)
                i = i + 1
            resposta = input("Deseja fazer a tabuada de outro número? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair")

def tabuada_while_for():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = 's'
    while resposta == "s":
        try:
            numero_escolhido = int(input("Digite um número que deseje a tabuada: "))

            for i in range (1,11,1):
                resultado = i*numero_escolhido
                print(numero_escolhido,"X",i,"=",resultado)
            resposta = input("Deseja fazer a tabuada de outro número? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair")

#2)crie um algoritmo que solicite 2 números do usuário e mostre na tela todos os números no intervalo entre essses números.
def numeros_intervalo():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho) 


    #versão só com while 
    resposta = "s"
    while resposta == "s":
        try:
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número :"))
            if n1 < n2: 
                i = n1 + 1
                while i < n2:
                    print(i)
                    i = i + 1
            elif n1 > n2:
                i = n2 + 1
                while i < n1:
                    print(i)
                    i = i + 1
            else:
                print("Não a um intervalo entre esses números: ")
            resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair.")

def numeros_intervalo_while_for():

    def escreva (mgs):  
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)    


    #versão só com for e while
    resposta = "s"
    while resposta == "s":
        try:
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))

            if n1 < n2:
                for i in range(n1+1,n2,1):
                    print(i)
            elif n1 > n2:
                for i in range(n1-1,n2,-1):
                    print(i)
            else:
                print("Os números são iguais")
            
            resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair.")

#3)crie um algoritmo que solicite 2 números do usuário e some todos os números no intervalo entre esses número.
def soma_numeros_intervalo():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    #versão só com while
    resposta = "s"
    while resposta == "s":
        try:
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            total = 0

            if n1 < n2:
                i = n1 
                while i <= n2:
                    print(i)
                    total = total + i
                    i = i + 1
                print(total)
            elif n1 > n2:
                i = n2
                while i <= n1:
                    print(i)
                    total = total + i
                    i = i + 1
                print(total)
            else:
                print("Não a nenhum intervalo entre esses números: ")
            
            resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair.")

def soma_numeros_intervalo_while_for():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    #versão só com for e while
    resposta = "s"
    while resposta == "s":
        try:
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            total = 0
            if n1 < n2:
                for i in range(n1,n2+1,1):
                    print(i)
                    total = total + i
                print(total)
            elif n1 > n2:
                for i in range(n1,n2-1,-1):
                    print(i)
                    total = total + i
                print(total)
            else:
                print("Não a nenhum intervalo entre esses números: ")

            resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair.")

#4)Crie um algoritmo que solicite do usuário 2 números, sendo base e expoente, calcule a potência sem utilize um loop.
def potencia():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    #versão só com for e while
    resposta = "s"
    while resposta == "s":
        try:
            base = int(input("Digite o número base: "))
            expoente = int(input("Digite o expoente: "))

            resultado = 1
            for i in range(expoente):
                resultado*=base

            print(f"O resultado da sua conta é {resultado}")
        
            resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
        except ValueError:
            escreva ("Tente novamente: ")
    escreva ("Você optou por sair.")


def menu():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    print("Escolha uma das opções abaixo: ")
    print("1 - Tabuada")
    print("2 - Números no intervalo")
    print("3 - Soma dos números no intervalo")
    print("4 - Potência")
    print("5 - Sair")

    escolha = input("Digite a opção desejada: ")

    if escolha == "1":
        tabuada_while_for()
        menu()
    elif escolha == "2":
        numeros_intervalo_while_for()
        menu()
    elif escolha == "3":
        soma_numeros_intervalo_while_for()
        menu()
    elif escolha == "4":
        potencia()
        menu()
    elif escolha == "5":
        escreva("Você optou por sair.")
    else:
        escreva("Opção inválida. Tente novamente.")
        menu()
#Executando
menu()