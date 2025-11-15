'''
PROGRAMA: FUNCIONAMENTO DO ENQUANTO - WHILE
DATA: 09/05/2025
autor:Matheus Henrique De Lima Soares 1B de informatica
'''
'''Como eu fui aprendendo novos comandos e funções em Python, decidi atulizar este arquivo com exemplos práticos(por isso tem alguns comandos que vocês podem não conhecer)'''

#1).Crie um algoritmo que receba do usuário 2 números e informe qual dos dois é maior ou se são iguais
def números_diferentes():
    
#essa parte do código é para escrever mensagens formatadas, eu usei só para deixa bonitinho não precisa entender
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    # a parte do "resposta = "s" é para controlar o loop do programa, tipo uma condição se ele continuar igual a "s" que é uma abreviação para sim o programa ficara se repetindo

    resposta = "s"
    while resposta =="s":
        # o "try/except" você não vão usar agora isso e apenas para não aparecer uma mensagem de erro feia caso o usuário digite algo errado
        try:
            numero1 = int(input("Digite o primeiro número: "))
            numero2 = int(input("Digite o segundo número: "))

            if numero1 > numero2:
                print("O primeiro número é maior que o segundo")

            elif numero1 < numero2:
                print("O segundo número é maior que o primeiro")

            else:
                print("Os dois números são iguais")

            #caso o usuário digite algo diferente de "s" o codigo vai para de ser repetir

            resposta = input("Gostaria de repetir o programa? S para sim e N para não: ").lower()# o comando lower() transforma a resposta em letra minúscula para facilitar a comparação que acabei não fazendo

        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair")# essa mensagem aparece quando o usuário digita algo diferente de "s"

#2)Crie um algoritmo que pergunte a idade da pessoa e diga se ela já tem idade para votar, sendo a idade mínima para vota de 16 anos.
def verificar_voto():
    
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta == "s":
        try:
            idade = int(input("Digite sua idade: "))

            #se idade for menor que zero o codigo continura repetindo ate o usuário digitar uma idade válida ja que não existe idade negativa

            while idade < 0:
                print("Você digitou sua idade negativa, corrija por favor.")
                idade = int(input("Digite sua idade: "))#precisei colocar a mensagem dentro do loop para garantir que o usuário corrija a idade ja que o valor que ele digitou inicialmente é inválido

            if idade >= 16:# se idade for maior ou igual a 16 aparece essa mensagem
                escreva(f"Sua idade é {idade} você pode votar")# lembrando que o comando "escreva" é apenas para deixar a mensagem mais bonita ele e a mesma coisa que o print

            else:# se idade for menor que 16 aparece essa mensagem
                escreva(f"Sua idade é {idade} você ainda não pode votar")

            resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()

        except ValueError:
            escreva("tente novamente: ")
    escreva("Você optou por sair")

#3)Crie um algoritmo que solicite as notas de lógica do 1º e 2º bimestres e informe se o aluno passou por média ou está de recuperação, sendo a nota mínima para passar de 60 pontos.
def media_de_notas():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)    


    resposta = "s"
    while resposta == "s":
        try:
            # a variável soma vai armazenar a soma das notas(por isso eu crei ela antes de todo mais ainda colocando ela dentra while para que tado vez que o codigo for repetido a soma volte a ser zero)
            soma = 0
            # o for vai repetir duas vezes para pegar as notas dos dois bimestres
            for i in range(1,3):
                nota_B = float(input(f"Digite a sua nota do {i} bimestre: "))

                while nota_B < 0:# se uma das notas for negativa o codigo vai se repetir ate que o usuário digite uma nota válida
                    print("Umas das suas notas está negativa, por favor corrija")
                    nota_B = float(input(f"Digite a sua nota do {i} bimestre: "))

                soma+= nota_B#isso e a mesma coisa de soma = soma + nota_B(como a varialvel soma tem o valor zero quando ela soma com nota_B ela ganha o valor de nota_B)
            media = soma / 2#soma que tem os valores das duas notas dividido por 2 para fazer a média
                
            if media >= 60:#se a media for maior ou igual a 60 o aluno passou.a parte do {media:.2f} serve para quando o numero aparecer na tela ele aparecer com duas casas decimais
                escreva(f"Sua média é {media:.2f}. parabéns você passou!")
            else:#se a media for menor que 60 o aluno está de recuperação
                escreva(f"Sua média é {media:.2f}. infelizmente você não passou.")
            resposta = input("gostaria de fazer novamente sua média? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair")

#4)Crie um programa que solicite uma idade e classifique essa pessoa como: a) 0 – 12 criança b) 13 – 17 adolescente c) 18 – 59 adulto d) 60 ou mais será idoso
def classificacao_de_idade():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta == "s":
        try:
            idade = int(input("Digite sua idade: "))

            while idade < 0:
                print("Você digitou uma idade negativa, por favor corrija.")
                idade = int(input("Digite sua idade: "))
            
            if idade >= 0 and idade <= 12:# se a idade estiver entre 0 e 12 anos, a pessoa é classificada como criança
                escreva(f"Você tem {idade} anos, você ainda é uma criança.")

            elif idade >= 13 and idade <= 17:# se a idade estiver entre 13 e 17 anos, a pessoa é classificada como adolescente
                escreva(f"Você tem {idade} anos, você é um adolescente.")

            elif idade >= 18 and idade <= 59:# se a idade estiver entre 18 e 59 anos, a pessoa é classificada como adulto
                escreva(f"Você tem {idade} anos, você é um adulto.")

            else:# se a idade for maior ou igual a 60 anos, a pessoa é classificada como idoso
                escreva(f"Você tem {idade} anos, você é um idoso.")

            resposta = input("Gostaria de repetir o programa? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair.")

#5)Faça um programa que solicite do usuário o peso e a altura de uma pessoa e calcule o IMC (Índice de Massa Corpórea) e informe se a pessoa está abaixo do peso, com magreza, normal, sobrepeso ou obeso. Considere o cálculo de IMC: imc = peso / (altura)2 Classificação de IMC: Igual o menor que 18,5: magreza Maior que 18,5 e menor ou igual a 24,9: normal Maior ou igual a 25 e menor ou igual a 29,9: sobrepeso Maior ou igual a 30: obesidade.
def imc():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)    


    resposta = "s"
    while resposta == "s":
        try:
            peso = float(input("Digite seu peso: "))
            altura = float(input("Didite sua altura: "))
            imc = peso / (altura)**2

            while peso < 0 or altura < 0:# se o peso ou a altura forem negativos o código vai se repetir até que o usuário digite valores válidos
                print("Você digitou um valor negativo para peso ou altura, isso não é válido. Corrija, por favor ")
                peso = float(input("Digite seu peso: "))
                altura = float(input("Didite sua altura: "))
            
            if imc <= 18.5:# se o IMC for menor ou igual a 18,5 a pessoa está abaixo do peso
                escreva(f"Seu IMC é {imc:.2f} você está abaixo do peso.")
            
            elif imc > 18.5 and imc <= 24.9:# se o IMC for maior que 18,5 e menor ou igual a 24,9 a pessoa está com peso normal
                escreva(f"Seu IMC é {imc:.2f} você está dentro do peso padrão.")

            elif imc >= 25 and imc <= 29.9:
                escreva(f"Seu IMC é {imc:.2f} você está acima do peso.")

            else:
                escreva(f"Seu IMC é {imc:.2f} você está obeso.")

            resposta = input("Gostaria de refazer o seu IMC? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair")

#6)Crie um programa que solicite do usuário um horário de número inteiro entre 0 e 24 e informe se é de manhã (5 - 11), de tarde (12 – 17), de noite (18 – 22) ou de madrugada (23- 4).
def classificacao_de_horario():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta  == "s":
        try:
            hora = int(input("Digite a hora(entre 0 a 24): "))

            while hora < 0 or hora > 24:# se o horário digitado for menor que 0 ou maior que 24 o código vai se repetir até que o usuário digite um valor válido
                print("Horário inválido. por favor digite um número entre 0 a 24.")
                hora = int(input(" tente novamente: "))

            if hora >= 5 and hora <= 11:# se a hora estiver entre 5 e 11, é de manhã
                escreva(f"{hora}h é de manhã.")

            elif hora >= 12 and hora <= 17:
                escreva(f"{hora}h é da tarde.")

            elif hora >= 18 and hora <= 22:# se a hora estiver entre 18 e 22, é de noite
                escreva(f"{hora}h é de noite.")

            else:
                escreva(f"{hora}h é de madrugada.")

            resposta = input("Gostara de repetir o programa? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair")

#esse menu eu criei para me organizar melhor ja que coloquei todos os programas em um único arquivo e dentro de defs eu posso com esse menu chamar cada um deles (não precisam saber disso)

def menu():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    escreva("Menu de opções")
    print("1 - Números diferentes")
    print("2 - Verificar voto")
    print("3 - Média de notas")
    print("4 - Classificação de idade")
    print("5 - IMC")
    print("6 - Classificação de horário")
    print("0 - Sair")

    escolha = input("Escolha uma das opções acima: ")

    if escolha == "1":
        números_diferentes()
        menu()
    elif escolha == "2":
        verificar_voto()
        menu()
    elif escolha == "3":
        media_de_notas()
        menu()
    elif escolha == "4":
        classificacao_de_idade()
        menu()
    elif escolha == "5":
        imc()
        menu()
    elif escolha == "6":
        classificacao_de_horario()
        menu()
    elif escolha == "0":
        escreva("Você optou por sair.")
    else:
        escreva("Opção inválida. Tente novamente.") 

        
#executando o programa
menu()