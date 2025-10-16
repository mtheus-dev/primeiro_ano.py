#1)peça um número e diga se ele é primo.
def numero_primo():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta == "s":
        try:
            numero = int(input("Digite um número: "))

            if numero <= 1:
                print("Não é primo.")
            else:
                primo = True

                for i in range(2,numero):
                    if numero % i == 0:
                        primo = False
                        break
                
                if primo == True:
                    print(f"{numero} é primo.")
                else:
                    print(f"{numero} não é primo.")
            
            resposta = input("Gostaria de repetir? S para sim e N para não: ")
            escreva("Você optou por sair.")
        except ValueError:
            escreva("Digite novamente: ")

#2)Peça uma senha e valide ela (Se a senha tiver pelo menos 8 caracteres, letra maiúscula, letra minuscula e número é válida, se não, não valide)
def senha_valida():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    
    tem_maiúscula = False
    tem_minuscula = False
    tem_numero = False

    resposta = "s"
    while resposta == "s":
        try:

            senha = input("Digite uma senha que tenha pelo menos 8 caracteres, letra maiúscula, letra minuscula e número: ")


            if len(senha) >= 8:
                for i in senha:
                    if i.isupper():
                        tem_maiúscula = True
                    elif i.islower():
                        tem_minuscula = True
                    elif i.isnumeric():
                        tem_numero = True

                if tem_maiúscula and tem_minuscula and tem_numero:
                    print("Senha válida!")
                
                else:
                    print("Senha inválida: precisa conter letra maiúscula, minúscula e número.")

            else:
                print("Senha inválida: deve ter pelo menos 8 caracteres.") 

            resposta = input("Gostaria de repetir? S para sim e N para não: ")
            escreva("Você optou por sair.")
        except ValueError:
            escreva("tente novamente")

#3)Peça quantos termos da sequência de Fibonacci devem ser gerados e mostre todos (Pesquisa o que é se tu não sabe) Ex: Entrada = 6 Saída = 0 1 1 2 3 5
def sequência_fibonacci():

    def escreva(mgs):
        tamanho = len(mgs) + 4
        print("_"*tamanho)
        print(f"  {mgs}")
        print("_"*tamanho)


    resposta = "s"
    while resposta == "s":
        try:
            numero = int(input("Digite um número: "))

            a = 0
            b = 1

            for i in range(numero):
                print(a, end=" ")  
                a, b = b, a + b

            resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()

        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair.")
        
#4 - Peça uma palavra e diga se é um palíndromo ou não 
def palindroma():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta == "s":
        try:
            palavra = input("Digite uma palavra: ")

            if palavra == (palavra[::-1]):
                print(f"A palavra '{palavra}' é palíndromo.")

            else:
                print(f"A palavra '{palavra}' não é palíndromo.")

            resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair.")

# 5 - Calculadora completa, soma, subtração, multiplicação, divisão, raiz quadrada e exponenciação, com a quantidade de números que o usuário quiser (sem número definido) 
def calculadora():
    import math
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    def soma ():
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        resultado = n1 + n2
        print(f"O resultado da sua soma é {resultado}")


    def subtracao ():
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        resultado = n1 - n2
        print(f"O resultado da sua subtração é {resultado}")


    def multiplicacao ():
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        resultado =  n1 * n2
        print(f"O resultado da sua multiplicação é {resultado}")


    def divisão ():
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        resultado = n1 / n2
        print(f"O resultado da sua divisão é {resultado}")


    def raiz_quadrada():
        numero = int(input("Digite o número que deseja a raiz quadrada: "))
        while numero < 0:
            print("Não existe raiz quadrada de números negativos")
            numero = int(input(" tente novamente: "))
        resultado = math.sqrt(numero)
        print(f"A raiz quadrada do número {numero} é {resultado}")


    def exponenciacao():
        n1 = int(input("Digite o número base: "))
        n2 = int(input("Digite o expoente: "))
        resultado = math.pow(n1,n2)
        print(f"o resultado é {resultado:.2f}")


    while True:
        try:
            operacoes = [ '1-soma', '2-subtração', '3-multiplicação', '4-divisão','5-raiz quadrada','6-exponenciação']
            for menu in operacoes:
                print(menu)
            operacao = int(input("Digite o número da operaçao que deseja fazer: "))

            if operacao == 1:
                soma()

            elif operacao == 2:
                subtracao()

            elif operacao == 3:
                multiplicacao()

            elif operacao == 4:
                divisão()

            elif operacao == 5:
                raiz_quadrada()

            elif operacao == 6:
                exponenciacao()

            else:
                escreva("você não escolheu nenhuma das operações")   

            resposta = input("Gostaria de fazer uma nova operação? S para sim e N para não ").lower()
            if resposta == "s":
                continue
            else:
                escreva("Você optou por sair")
                break
        except ValueError:
            escreva("Você não digitou nenhum número. Tente novamente : ")
           

calculadora()
# Desafio (difícil): 6 - Jogo da velha com o visual mostrando
def jogo_da_velha():
    tabuleiro = [" "," "," "," "," "," "," "," "," "]



    def mostra_posicoes():
        print()
        print(" 0 | 1 | 2 ")
        print("---+---+---")
        print(" 3 | 4 | 5 ")
        print("---+---+---")
        print(" 6 | 7 | 8 ")
        print()


    def mostra_tabuleiro():
        print()
        print(" " + tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2])
        print("---+---+---")
        print(" " + tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5])
        print("---+---+---")
        print(" "+ tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8])
        print()


    def verificar_vitoria():
        combinacoes = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        for a, b, c in combinacoes:
            if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] and tabuleiro[a] != " ":
                return tabuleiro[a]
        if " " not in tabuleiro:
            return "Empate"
        return None
    jogador_atual = "X"

    mostra_posicoes()

    while True:
        mostra_tabuleiro()

        posicao = int(input(f"Jogador {jogador_atual}, escolha uma posição de 0 a 8: "))

        if tabuleiro[posicao] == " ":
            tabuleiro[posicao] = jogador_atual

        else:
            print("Essa posição ja está ocupada. tente novamente")
            continue


        if jogador_atual == "X":                                                                    
            jogador_atual = "O"

        else:
            jogador_atual = "X"

        vitoria = verificar_vitoria()
        if vitoria == "X":
            mostra_tabuleiro()
            print("O 'X' venceu!")
            break
        elif vitoria == "O":
            mostra_tabuleiro()
            print("O 'O' venceu!")
            break
        elif vitoria == "Empate":
            mostra_tabuleiro()
            print("Empatou")
            break

def menu():
    print("Escolha uma das opções abaixo: ")
    print("1 - Verificar se um número é primo")
    print("2 - Validar uma senha")
    print("3 - Gerar sequência de Fibonacci")
    print("4 - Verificar se uma palavra é palíndroma")
    print("5 - Calculadora completa")
    print("6 - Jogo da velha")
    print("0 - Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        numero_primo()
        menu()
    elif escolha == "2":
        senha_valida()
        menu()
    elif escolha == "3":
        sequência_fibonacci()
        menu()
    elif escolha == "4":
        palindroma()
        menu()
    elif escolha == "5":
        calculadora()
        menu()
    elif escolha == "6":
        jogo_da_velha()
        menu()
    elif escolha == "0":
        print("Você optou por sair.")
    else:
        print("Opção inválida. Tente novamente.")
        menu()
#executando programa:
menu()