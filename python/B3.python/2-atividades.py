#Ler varios valores e armazenar em um vetor (lista) quando o usuario digitar 0 (zero), o programa deve parar de ler os números. em seguida, mostre todos os valores do vetor.
def vetor1 ():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    while True:
        try:
            numeros = []

            while True:
                n = int(input("Informe um número: "))
                if n == 0:
                    break
                numeros.append(n);

            print(numeros)
        except ValueError:
            escreva("Tente novamente: ")

#Construa um algoritmo para ler no máximo 30 números reais informados pelo usuário e exiba a média desses números. Considere que o valor -99 encerra a entrada dos dados.
def vetor2():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    while True:

        try:
            v = []

            while True:
                n = float(input("Informe um número ou Digite -99 para sair: "))
                
                v.append(n);

                if n <= -99 or len(v) == 30:
                    print("Você optou por sair")
                    break

                
            media = sum(v)/ len(v)

            print(v)
            print(f"A média dos números é {media:.2f}")
            break
        except ValueError:
            escreva("Tente novamente: ")

#Em uma prova do Enem, em um dia, um aluno responde a uma avaliação de 90 perguntas de múltipla escolha com cada questão tendo respostas de A até E. Faça um algoritmo para ler as respostas de um aluno e o gabarito da prova, depois informe quantas questões ele acertou.
def gabarito():
    import random

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    alternativas = ['A', 'B', 'C', 'D', 'E']
    nota = 0
    quantidade = 5
    

    resposta = "s"
    while resposta == "s":
        try:
            acertos = 0
            gabarito = []
            resp = []

            #Lê as respostas do aluno
            for i in range(quantidade):
                resposta_aluno =input(f"Digite a sua resposta da {i+1}: ").upper()
                resp.append(resposta_aluno);
                
            
            #Gera o gabarito aleatoriamente
            for i in range(quantidade):
               gabarito.append(random.choice(alternativas))

            print("--------------------------------------------------------------")
            #Compara as respostas do aluno com o gabarito
            for i in range(len(gabarito)):
                if gabarito[i] == resp[i]:
                    acertos += 1
                    print(f"{i+1} questão: Gabarito = {gabarito[i]} | sua resposta = {resp[i]} ✔️")
                
                else:
                    print(f"{i+1} questão: Gabarito = {gabarito[i]} | sua resposta = {resp[i]} ❌")
            print("--------------------------------------------------------------")

            nota = (acertos*100) / quantidade

            print("===Gabarito===")
            print(gabarito)
            print("===Respostas do aluno===")
            print(resp)

            print(f"Você acertou {acertos} questões é tirou {nota:.2f} na prova.")
            
            resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
            if resposta != "s":
                escreva("Você optou por sair.")
        except ValueError:
            escreva("Tente novamente: ")

#Ler um vetor A que conterá 15 números inteiros. Construir um vetor B do mesmo tipo, sendo que cada elemento de B deverá ser a metade (parte inteira) de cada elemento de A. 
def ler_vetor():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s" 
    while resposta == "s":
        try:
            vetor_a = []
            vetor_b = []
            quantidade = 5
            for i in range(quantidade):
                numero = int(input(f"Digite o {i+1}º inteiro "))

                vetor_a.append(numero);
                vetor_b.append(numero // 2)

            print("===VETOR_A===")
            print(vetor_a)
            print("===VETOR_B===")
            print(vetor_b)
            resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
            if resposta != "s":
                escreva("Você optou por sair.")
        except ValueError:
            escreva("Tente novamente: ")

#Ler um vetor A com 20 elementos negativos. Construir um vetor B de mesmo tipo e dimensão, sendo que cada elemento do vetor B deverá ser o valor positivo do elemento correspondente do vetor A. Desta forma, se em A[1] estiver armazenado o elemento –3, deverá estar em B[1] o valor 3, e assim por diante. 
def vetor_negativo():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    resposta = "s"
    while resposta == "s":
        try:

            vetor_a = []
            vetor_b = []
            quantidade = 1

            for i in range(quantidade):
                numero = int(input(f"Digite o {i+1}º número negativo: "))

                while numero >= 0:
                    print("você digitou um número positivo. tente novamente")
                    numero = int(input(f"Digite o {i+1}º número negativo: "))

                vetor_a.append(numero);
                vetor_b.append (vetor_a[i] *-1)

            print(vetor_a)
            print(vetor_b)

            resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
            if resposta != "s":
                escreva("você optou por sair")
        except ValueError:
            escreva("tente novamente")

#Faça um programa que efetue a leitura de dez elementos de um vetor A. Construir vetor B de mesmo tipo, observando a seguinte lei de formação: se o valor do índice for par, o valor deverá ser multiplicado por 5, sendo ímpar, deverá ser somando com 5. Ao final mostrar o conteúdo do vetor B. 
def vetor_par_ímpar():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta == "s":
        try:
            vetor_a = []
            vetor_b = []
            quatidade = 5

            for i in range(quatidade):
                numero = int(input(f"Digite o {i+1}º número: "))

                vetor_a.append(numero);

                if numero % 2 == 0:
                    numero *= 5
                    vetor_b.append(numero);
                
                elif numero % 2 != 0:
                    numero += 5
                    vetor_b.append(numero);

            print("===VETOR_A===")
            print(vetor_a)
            print("===VETOR_B===")
            print(vetor_b)

            response = input("Gostaria de repetir? S para sim e N para não: ").lower()
            if response != "s":
                escreva("Você optou por sair.")
                break
        except ValueError:
            escreva("Tente novamente.")

#Elabore um algoritmo que, dado dois vetores inteiros de 20 posições, efetue as respectivas operações matemáticas indicadas por outro vetor de 20 posições de caracteres também fornecido pelo usuário contendo as quatro operações básicas aritméticas e armazena o resultado em um terceiro vetor
def operacoes_matematicas():
    vertor_a = []
    vertor_b = []
    operacoes = []
    resultado = []
    quantidade = 5

    resposta = "s"
    while resposta == "s":

        for i in range(quantidade):
            numero1 = int(input(f"Digite {i+1}º número: "))
            vertor_a.append(numero1)

        for i in range(quantidade):
            numero2 = int(input(f"Digite {i+1}º número: "))
            vertor_b.append(numero2)

        for i in range(quantidade):
            op = input("informe um operador (+, -, *, /, **): ")
            operacoes.append(op)
            
        for i in range(quantidade):
            if operacoes[i] == "+":
                valor = vertor_a[i] + vertor_b[i]
            
            elif operacoes[i] == "-":
                valor = vertor_a[i] - vertor_b[i]
            
            elif operacoes[i] == "*":
                valor = vertor_a[i] * vertor_b[i]

            elif operacoes[i] == "/" and vertor_b[i] != 0:
                valor = vertor_a[i] / vertor_b[i]
            
            resultado.append(valor)

            print(f"{vertor_a[i]} {operacoes[i]} {vertor_b[i]} = {valor}")

        resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
        if resposta != "s":        
            print("Você optou por sair.")

#Altere o exercício anterior para realizar a operação da seguinte: a operação do primeiro valor do vetor pelo último valor do segundo vetor, o segundo valor do primeiro vetor pelo penúltimo do segundo vetor. O resultado deve ser armazenado em um terceiro vetor na primeira posição, segunda, e assim por diante


#Desenvolva um algoritmo para ler um vetor de 10 posições e coloque eles em ordem crescente. 


#Menu de opções
def menu():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    print("Escolha uma das opções abaixo: ")
    print("1 - Ler vários valores e armazenar em um vetor")
    print("2 - Calcular a média de até 30 números")
    print("3 - Verificar acertos em uma prova do Enem")
    print("0 - Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        vetor1()
        menu()
    elif escolha == "2":
        vetor2()
        menu()
    elif escolha == "3":
        gabarito()
        menu()
    elif escolha == "0":
        escreva("Você optou por sair.")
    else:
        escreva("Opção inválida. Tente novamente.")
        menu()

vetor_par_ímpar()