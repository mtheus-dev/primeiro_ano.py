#1) Crie uma função chamada somar_vetor(vetor) que receba uma lista de números e retorne a soma de todos os elementos.
def soma_da_lista_professor():
    import random
    def somar_vetor(vetor):
        soma = 0
        for i in range(len(vetor)):
            soma += vetor[i]
        return soma

    lista = []
    quantidade = 5

    for i in range(quantidade):
        
        lista.append(random.randint(0,100))

    print(f"A soma dos números {lista} é: {somar_vetor(lista)}")

def soma_da_lista_matheus():
    import random
    lista = []
    quantidade = 10

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    for i in range(quantidade):  
        lista.append(random.randint(0,100))
    
    soma = sum(lista)

    escreva(f"A soma dos números {lista} é: {soma}")

#2) Crie um procedimento contar_pares_impares(vetor) que mostre quantos números pares e ímpares existem na lista.
def conta_lista_pares_impares():
    import random
    lista = []
    contador_impares = 0
    contador_pares = 0
    quantidade = 10

    def conta_pares_impares(vetor,conta_impares,conta_pares):
        for i in range(quantidade):
            if vetor[i] % 2 != 0:
                conta_impares += 1

            else:
                conta_pares += 1

        print(f"Na lista {lista} tem {conta_pares} números pares e {conta_impares} números impares")

    for i in range(quantidade):
        lista.append(random.randint(0,100))

    conta_pares_impares(lista,contador_impares,contador_pares)

#3) Crie uma função buscar_elemento(vetor, valor) que retorne True se o valor estiver presente no vetor e False caso contrário.
def buscando_elemento():
    import random
    lista = []
    quantidade = 10

    def buscar_elemento(vetor, valor):
        for i in vetor:
            if i == valor:
                return True
        return False
    
    for i in range(quantidade):
        lista.append(random.randint(0,100))

            
    valor = random.randint(0,100)

    verificador = buscar_elemento(lista,valor)

    if verificador == True:
        print(f"O valor {valor} esta presente na lista {lista}")

    else:
        print(f"O valor {valor} não esta presente na lista {lista}")    

#4) Faça uma função interseccao(v1, v2) que receba dois vetores e retorne uma lista com os elementos que aparecem em ambos.
def lista_semelhantes():
    import random
    lista_1 = []
    lista_2 = []
    quantidade = 10 

    def interseccao(v1, v2):
        semelhantes = []
        for num1 in v1:
            dentro = False
            for num2 in v2:
                if num1 == num2:
                    dentro = True
                    break
            if dentro == True:
                semelhantes.append(num1)
        return semelhantes


    for i in range(quantidade):
        lista_1.append(random.randint(0,100))
        lista_2.append(random.randint(0,100))

    print(f"A lista 1 contém: {lista_1}\nA lista 2 contém: {lista_2}\nOs números que aparecem em ambas são: {interseccao(lista_1, lista_2)}")

#5) Crie um módulo chamado conversoes.py com funções para converter:
#• Metros em centímetros;
#• Celsius em Fahrenheit (Fórmula: F = (C x 1,8) + 32 ),
#• Reais para dólares (1 real = 0,19 dólares).
#No arquivo principal, importe o módulo e permita que o usuário escolha qual conversão deseja realizar
def conversoes():
    from biblioteca import conversoes
    def menu():
        print("\nEscolha uma conversão:")
        print("1 - Metros para centímetros")
        print("2 - Celsius para Fahrenheit")
        print("3 - Reais para Dólares")
        print("0 - Sair")

        opcao = int(input("Digite a opção desejada: "))

        return opcao

    opcao = menu()

    while True:
        if opcao == 1:
            metros = float(input("Digite em metros: "))
            print(f"O valor de {metros} metros em centímetros é {conversoes.converter_m_c(metros)}")

        elif opcao == 2:
            celsius = float(input("Digite a temperatura em celsius: "))
            print(f"A temperatura de {celsius:.2f}º celsius em fahrenheit é {conversoes.celsius_em_fahrenheit(celsius):.2f}º")

        elif opcao == 3:
            reais = float(input("Digite o valor em reais: "))
            print(f"O valor em {reais} reais em dólares é {conversoes.reais_em_dolares(reais):.2f}")

        elif opcao == 0:
            print("Você optou por sair")
            break

        else:
            print("Entrada invalida. Tente novamente")

def menu():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    operacoes ={
        1:soma_da_lista_matheus,
        2:conta_lista_pares_impares,
        3:buscando_elemento,
        4:lista_semelhantes,
    }

    while True:
        print("Escolha uma das opções abaixo: ")
        print("1 - soma da lista")
        print("2 - conta lista pares e impares")
        print("3 - buscando elemento")
        print("4 - lista semelhantes")
        print("0 - Sair")

        while True:
            try:

                escolha = input("Digite a opção desejada: ")

                if 0 <= escolha <= 4:
                    break

                else:
                    escreva("Essa opcão esta no menu. Tente novamente")

            except ValueError:
                escreva("Entrada invalida. Tente novamente")

        if escolha == 0:
            escreva("Você optou por sair")
            break

        operacoes[escolha]

menu()