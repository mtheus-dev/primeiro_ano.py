#1)Escreva um programa que solicite do usuário login e senha, ele só terá 3 tentativas para acertar.

def login():

    contador = 1 
    login = "admin"
    senha = 1234

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)
    
    def verificacao(login_user,senha_user):
        if login_user == login and senha_user == senha:
            return True
        
        else:
            return False

    escreva("ACESSO AO SISTEMA\n" \
    "Entre com login e senha") 

    login_user = input("Entre com seu login: ")
    senha_user = int(input("Entre com a sua senha numérica: "))

    while contador <=3 and verificacao(login_user,senha_user) == False:

        print("Foi sua tentativa ", contador,"tente novamente")
        contador = contador + 1
        login_user = input("Entre com seu login: ")
        senha_user = int(input("Entre com a sua numérica: "))

        if  verificacao(login_user,senha_user) == True :
            
            escreva("Acesso autorizado.")
            
        else:
            escreva("ACESSO NEGADO. Entre em contado com o administrador do sistema.")

#2)Faça um algoritmo que simule um caixa eletronico, o usuário pode sacar enquanto tiver dinheiro

saldo = 1000
def escreva (mgs):
    tamanho = len(mgs) + 4
    print("_" * tamanho)
    print(f"  {mgs}")
    print("_" * tamanho)

def escolher_operacao():
    print("1-sacar")
    print("2-depositar")
    print("3-ver saldo")
    print("4-sair")

    while True:
        try:
            opcao = int(input("O que gostaria de fazer no banco hoje?: "))

            if 1 <= opcao <= 4:
                return opcao
            
            else:
                escreva("Esse número não está no menu. Tente novamente.")

        except ValueError:
            escreva("Entrada inválida. Digite um número de 1 a 4.")

def sacar (quantia):
    global saldo
    if quantia <= saldo and quantia > 0:
        saldo -= quantia
        return True
    return False

def depositar(quantia):
    global saldo
    if quantia >= 0:
        saldo += quantia
        return True
    return False

def main():
    while True:
        opcao_escolhida = escolher_operacao()
        if opcao_escolhida == 1:
            quantia = int(input("Informe a quantia a ser sacada: "))
            opcao_sucesso = sacar (quantia)
            if opcao_sucesso:
                print(f"Saque realizado com sucesso\nO saldo restante é: R$ {saldo:.2f}")
            else:
                print("Saque não realizado")

        if opcao_escolhida == 2:
            quantia = int(input("Informe a quantia que você gostaria de depositar: "))
            opcao_sucesso = depositar(quantia)
            if opcao_sucesso:
                print(f"deposito realizado com sucesso\nO saldo restante é: R$ {saldo:.2f}")
            else:
                print("O deposito não foi realizado.")

        if opcao_escolhida == 3:
            print(f"O saldo restante é: R$ {saldo:.2f}")

        if opcao_escolhida == 4:
            escreva("Você optou por sair")
            break
main()

#3)Crie uma função para somar uma lista de números.
def soma_de_lista():
    import random
    lista = []

    def soma_lista(lista):
        tamanho = len(lista)
        soma = 0
        for i in range(0,tamanho):
            soma += lista[i]

        return soma

    def main():
        global lista

        for i in range(0,10):
            lista.append(random.randint(0,100))

        valor_total = soma_lista(lista)
        print(f"Valor total da lista: {valor_total}")
        print(lista)

    main()

#4)Crie uma função para encontrar o maior valor de uma lista.
def maior_numero():
    import random
    lista = []

    def maior_numero(lista):
        tamanho = len(lista)
        maior = lista[0]
        for i in range(0,tamanho):
            if lista[i] > maior:
                maior = lista[i]
        return maior

    def preencher_lista(lista):
        for i in range(0,10):
            lista.append(random.randint(0,100))
        
        return lista

    preencher_lista(lista)
    print(lista)
    print(f"O maior número da lista é : {maior_numero(lista)}")

#5)Escreva uma função para verificar se uma palavra é palíndromo (palíndromo é uma palavra que tem o mesmo significado quando é lido da direita para esquerda, ex: arara ou mirim).
def palavra_palindromo_versao_dificil():
    def verificacao(palavra):
        for i in range(len(palavra)):

            if palavra[i] == palavra[-1]:
                print(f"A palavra {palavra} é palíndroma")
                break
            
            else:
                print(f"A palavra {palavra} não é palíndroma")
                break
    
    while True:
        palavra = input("informe uma palavra: ")

        verificacao(palavra)

        resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()

        if resposta != "s":
            print("você optou por sair")
            break

def palavra_palindromo_versao_facil():
    def verificacao(palavra):
        if palavra == palavra[::-1]:
            print(palavra[::-1])
            print(f"A palavra {palavra} é palíndroma")
        
        else:
            print(palavra[::-1])
            print(f"A palavra {palavra} não é palíndroma")

    palavra = input("informe uma palavra: ")

    verificacao(palavra)
