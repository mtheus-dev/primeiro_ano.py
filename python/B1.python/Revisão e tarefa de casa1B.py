'''
PROGRAMA: FUNCIONAMENTO DO ENQUANTO - WHILE
DATA: 16/05/2025
autor:Matheus Henrique De Lima Soares 1B de informatica
'''

#1)Crie um programa que receba 4 notas bimestrais, calcule a média e ao final informe ao usuário a média e se o estudante passou ou não (considere a média para passar de 60 pontos).
def media_do_ano():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta == "s":
        try:
            # a variável soma_notas vai armazenar a soma das notas(por isso eu crei ela antes de todo mais ainda colocando ela dentra while para que tado vez que o codigo for repetido a soma volte a ser zero)
            soma_notas = 0
            for i in range(1,5):# o for vai repetir 4 vezes para pegar as notas dos 4 bimestres
                notas_B = float(input(f"Digite sua nota do {i} bimestre: "))

                while notas_B < 0:# se uma das notas for negativa o codigo vai se repetir ate que o usuário digite uma nota válida
                    print("Você digitou um número negativo")
                    notas_B = float(input(f"Redigite sua nota do {i} bimestre : ")) 

                soma_notas += notas_B#isso e a mesma coisa de soma_notas = soma_notas + notas_B
            media = soma_notas / 4# soma_notas que tem os valores das quatro notas dividido por 4 para fazer a média

            if media >= 60:#se a media for maior ou igual a 60 o aluno passou.a parte do {media:.2f} serve para quando o numero aparecer na tela ele aparecer com duas casas decimais
                escreva(f"A sua média é {media:.2f}, parabéns você passou!")
            else:
                escreva(f"A sua média é {media:.2f}, infelizmente você não passou.")
                
            resposta = input("Gostaria de fazer sua média novamente? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("você optou por sair")

#2)Crie um programa que solicite o ano de nascimento de uma pessoa e o ano atual. Ele deve calcular a idade e informar se a pessoa é menor de idade (menos que 18 anos), adulto (a partir de 18 a 59 anos) ou idoso (com 60 anos ou mais).
def classificacao_de_idade_N():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta == "s":
        try:
            nascimento = int(input("Digite seu ano de nascimento: "))

            while nascimento < 0:
                print(" você digitou um ano de nascimento negativo. por favor corrija.")
                nascimento = int(input("Tente novamente: "))
            idade = 2025 - nascimento

            if idade < 18:
                escreva(f"Sua idade é {idade}, você é menor de idade.")

            elif idade >= 18 and idade <= 59:
                escreva(f"Sua idade é {idade}, você é adulto")

            else:
                escreva(f"Sua idade é {idade}, você é um idoso.")

            resposta = input("gostaria repetir o programa? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair")

#3)Crie um programa que solicite 2 notas bimestrais do usuário e quantidade de faltas. O programa deve calcular a média do aluno e informar se ele está aprovado, sendo que para tal ele deve ter: Média mínima de 60 pontos e menos de 6 faltas para estar aprovado Média entre 48 e 59 pontos e menos de 8 faltas para estar de recuperação Qualquer outra situação ele estará reprovado.
def aprovacao():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta == "s":
        try:
            soma_notas = 0#eu acho que vocês ja entenderam para que serve a variável soma_notas
            soma_faltas = 0# a variável soma_faltas vai fazer a mesma coisa que soma_notas, mas para as faltas
            for i in range(1,3):# o for vai repetir duas vezes para pegar as notas e faltas dos dois bimestres
            
                notas_B = float(input(f"Digite a sua nota do {i} bimestre: "))
                faltas_B = int(input(f"Digite a quantidades de faltas do {i} bimestre: "))

                while notas_B < 0 or faltas_B < 0:# se uma das notas ou faltas for negativa o codigo vai se repetir ate que o usuário digite uma nota válida
                    print("Você digitou suas notas ou faltas de forma negativa. por favor corrija.")
                    notas_B = float(input(f"Redigite sua nota do {i} bimestre : "))
                    faltas_B = int(input(f"Redigite a quantidades de faltas do {i} bimestre: "))

                soma_notas += notas_B#isso e a mesma coisa de soma_notas = soma_notas + notas_B(só uma coisa esses soma_notas+= notas_B e soma_notas += faltas_B estão dentro para que eles possam fazer a soma das notas e faltas de cada bimestre)
                soma_faltas += faltas_B
            media_n = soma_notas / 2# soma_notas que tem os valores das duas notas dividido por 2 para fazer a média
            media_f = soma_faltas / 2# a mesma coisa que media_n, mas para as faltas

            #essa parte eu acho que vocês ja entederam
            if media_n >= 60 and media_f < 6:#se a media for maior ou igual a 60 e a media de faltas for menor que 6 o aluno passou.(e por ai vai)

                escreva(f"Sua média é {media_n:.2f} e teve {media_f}faltas, parabéns você foi aprovado.")
            elif 48 <= media_n < 60 and media_f < 8:
                escreva(f"Sua média é {media_n:.2f} e teve {media_f}faltas, você ficou de recuperação.")
            else:
                escreva(f"Sua média é {media_n:.2f} e teve {media_f}faltas, você está reprovado.")
            
            resposta = input("Gostaria de repetir o programa? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair")

#4)Crie um programa que solicite ao usuário 3 números diferentes e informe qual é o segundo número maior (ou seja, o do meio).
def logica():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    #Jesus Cristo! como eu vou explicar isso?!
    while True:# isso vai continuar até que o while seja interrompido pelo break ou mude para false
        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            n3 = float(input("Digite o terceiro número: "))

            if n1 != n2 and n2 != n3 and n1 != n3:# se n1, n2 e n3 forem diferentes(break e continua o codigo ja que todos os números são diferentes)
                break
            else:# se algum dos números forem iguais ele vai pedir para o usuário digitar novamente
                print("Todos os números devem ser diferentes. Tente novamente.")
        except ValueError:
            print("você digitou algo diferente de um número. Tente novamente: ")

    if n1 > n2 and n1 < n3 or n1 < n2 and n1 > n3:# se n1 for maior que n2 e menor que n3 ou menor que n2 e maior que n3 o n1 e o número do meio(a mesma coisa para os outros.(nem sei se eu mesmo entendi isso '_'))
        meio = n1
    elif n2 > n1 and n2 < n3 or n2 < n1 and n2 > n3:
        meio = n2
    else:
        meio = n3

    escreva(f"O segundo maior número é {meio}")

#5)Crie um programa que solicite ao usuário que informe login e senha. Se o login for “admin” e a senha “1234” mostre a mensagem “Acesso Permitido"; se o login for “admin” e a senha diferente de “1234” deve aparecer a mensagem “Senha incorreta”; Se o login for diferente de “admin” deve aparecer a mensagem “Usuário não cadastrado”.
def login():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    senha = 1234
    login = "admin"

    login_s = input("Entre com seu login: ")
    senha_s = int(input("Entre com sua senha numérica: "))

    if login_s == login and senha_s == senha:# se a senha que eu digitei for igual a senha cadastrada o acesso é permitido a mesma coisa para o login
        escreva("Acesso Permitido.")

    elif login_s == login and senha_s != senha:# se o login for igual a "admin" e a senha diferente de "1234" deve aparecer a mensagem “Senha incorreta”
        escreva("Senha incorreta.")

    else:
        escreva("Usuário não cadastrado.")# se o login for diferente de "admin" deve aparecer a mensagem “Usuário não cadastrado”.

#6)Crie um algoritmo que solicite a idade de uma pessoa e informe se ela é obrigada a votar considerando as faixas de idade: menos de 16 anos não vota; de 16 anos a menos de 18 e acima de 70 anos é facultativo; de 18 anos a 69 anos o voto é obrigatório.
def checa_idade_voto():

    #eu acho que esse codigo ucom outrom que ja fiz, mas não tenho certeza

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

            if idade < 16:
                escreva(f"Sua idade é {idade}, você ainda não pode votar.")

            elif idade >= 16 and idade < 18 or idade >= 70:
                escreva(f"Sua idade é {idade}, você não é obrigado a votar.")

            else:
                escreva(f"Sua idade é {idade}, você é obrigado a votar.")

            resposta = input("Gostaria de repetir o programa? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair")

#7)Crie um programa que solicite do usuário um horário no formato de 24 horas e mostre para ele: “Bom dia” se a hora estiver entre 5 e 11; “Boa tarde” se a hora estiver entre 12 e 18; “Boa noite” se a hora estiver entre 19 e 23; “Boa madrugada” se estiver entre 0 e 5; “Você não digitou uma hora válida” caso ele digite outros valores.
def bom_dia():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta  == "s":
        try:
            hora = int(input("Digite a hora(entre 0 a 24): "))

            while hora < 0 or hora > 24:
                print("Horário inválido. por favor digite um número entre 0 a 24.")
                hora = int(input(" tente novamente: "))

            if hora >= 5 and hora <= 11:
                escreva(f"{hora}h bom dia!")

            elif hora >= 12 and hora <= 18:
                escreva(f"{hora}h boa tarde.")

            elif hora >= 19 and hora <= 23:
                escreva(f"{hora}h boa noite.")

            else:
                escreva(f"{hora}h boa madrugada.")

            resposta = input("Gostara de repetir o programa? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair")


def menu():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    print("Escolha uma das opções abaixo: ")
    print("1 - Média do ano")
    print("2 - Classificação de idade")
    print("3 - Aprovação")
    print("4 - Segundo maior número")
    print("5 - Login")
    print("6 - Checagem de idade para voto")
    print("7 - Saudação conforme horário")
    print("0 - Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        media_do_ano()
        menu()
    elif escolha == "2":
        classificacao_de_idade_N()
        menu()
    elif escolha == "3":
        aprovacao()
        menu()
    elif escolha == "4":
        logica()
        menu()
    elif escolha == "5":
        login()
        menu()
    elif escolha == "6":
        checa_idade_voto()
        menu()
    elif escolha == "7":
        bom_dia()
        menu()
    elif escolha == "0":
        escreva("Você optou por sair.")
    else:
        escreva("Opção inválida. Tente novamente.")
        menu()


menu()