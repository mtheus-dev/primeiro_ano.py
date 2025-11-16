'''
PROGRAMA: FUNCIONAMENTO DO ENQUUANTO - WHILE
DATA: 12/06/2025
autor:Matheus Henrique De Lima Soares 1B de informatica
'''
#1)Escreva um programa que solicite do usuário login e senha, ele só terá 3 tentativas para acertar.
def verificar_login():
    contador = 0
    login = "admin"
    senha = 1234

    print("________________________________")
    print("ACESSO AO SISTEMA")
    print("Entre com login e senha")
    print("____________________________")

    login_user = input("Entre com seu login: ")
    senha_user = int(input("Entre com a sua senha numérica: "))

    while contador <=3 and (login_user != login or senha_user != senha):
        print("Foi sua tentativa ", contador,"tente novamente")
        contador = contador + 1
        login_user = input("Entre com seu login: ")
        senha_user = int(input("Entre com a sua senha numérica: "))

        if  login_user == login and senha_user == senha:
            print("_____________")
            print("Acesso autorizado.")
            print("________________")
            
        else:
            print("______________________________")
            print("ACESSO NEGADO. Entre em contado com o administrador do sistema.")
            print("_______________________________")

#2)Faça um algoritmo que simule um caixa eletronico, o usuário pode sacar enquanto tiver dinheiro
def caixa_eletronico():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    valor_caixa = 1000


    escreva("Bem vindo ao caixa para saques")

    resposta = input(("Você quer sacar? Digite s para sim e n para não: ")).lower()

    if resposta == 's':
        valor_atual = valor_caixa

        while valor_atual <= valor_caixa and (resposta == "s"):
            
            if valor_atual <= 0:
                    print("\nSaldo insuficiente. programa encerrado\n")
                    break

            print(f"O valor atual em caixa é de {valor_atual} reais")
            valor_sacar = float(input("Qual valor você deseja sacar? "))


            if valor_sacar < 0:
                print("Valor Invalido")
            
            elif valor_sacar > valor_atual:
                print("O valor solicitado é maior do que temos em caixa.")
            else:
                valor_atual = valor_atual - valor_sacar
                print("O valor sacado foi de",valor_sacar)
                
            if valor_atual <= 0:
                print("\nSaldo insuficiente. programa encerrado\n")
                break
            
            resposta = input("Gostaria de fazer novo saque? s para sim e n para não: ")
            if resposta == "n":
        
                escreva("Você optou por sair. obrigado e volte sempre")

#3.	Crie um algoritmo que solicite do usuário um valor em reais e em seguida pergunte para qual moeda deve ser convertido: dólar ou euro.
def converter_moeda():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    conotacao_do_dolar = 5.529
    conotacao_do_euro = 6.353

    resposta = "s"
    while resposta == "s":
        try:
            valor_em_reais = float(input("Insira o valor em reais: "))

            while valor_em_reais < 0:
                print("O valor em reais está negativo. por favor corrija")
                valor_em_reais = float(input("Tente novamente: "))

            moeda = input("Para que moeda você gostaria de converter? Digite D para dólar e E para euro: ").lower()

            while moeda != 'd' and moeda != 'e':
                moeda = input("Você não escolheu Dólar e nem Euro. Por favor tente novamente:").lower()

            if moeda == 'd':
                valor_em_Dólar = valor_em_reais / conotacao_do_dolar
                print(f"Sua conversão de reais para dólar deu {valor_em_Dólar:.2f}")

            elif moeda == 'e':
                valor_em_euro = valor_em_reais / conotacao_do_euro
                print(f"Sua conversão de reais para euro deu {valor_em_euro:.2f}")

            resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair")

#4)Crie um algoritmo que solicite do usuário um número de 0 a 20 e mostre todos os números pares até chegar ao número escolhido começando em 0.
def numeros_pares():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

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

#5)Crie um algoritmo que solicite ao usuário números diversos até que ele escolha sair, depois disso ele deve obter a média dos números digitados.
def calcular_media():   
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
        print("Nenhum número foi digitado.")

#6)Crie um algoritmo que mostre ao usuário um menu que ofereça opções para efetuar operações matemáticas (soma, subtração, multiplicação e divisão). O usuário deve escolher qual operação fazer, ao final o programa deve perguntar se o usuário quer efetuar nova operação ou sair do programa.
#versão só com while

while True:

    operacoes = [ '1-soma', '2-subtração', '3-multiplicação', '4-divisão']
    for menu in operacoes:
        print(menu)
    operacao = int(input("Digite o número da operação que deseja fazer: "))

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

#7)Crie um algoritmo que solicite do usuário um número. Some todos os números de 0 até o número escolhido e mostre o resultado na tela.
def soma_numeros_1():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

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

#8)Crie um algoritmo que solicite do usuário um número, em seguida mostre todos os números em escala decrescente iniciando no número escolhido e terminando em 0.

def numeros_decrescente():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

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
