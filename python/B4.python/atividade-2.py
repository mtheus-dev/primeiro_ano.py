#Escreva um programa que solicite do usuário login e senha, ele só terá 3 tentativas para acertar.

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

#Faça um algoritmo que simule um caixa eletronico, o usuário pode sacar enquanto tiver dinheiro
def caixaeletronico():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    def escolher_operacao(operacao):
        print("1-sacar")
        print("2-depositar")
        print("3-ver saldo")
        print("4-sair")

        operacao = int(input("escolha a operação: "))

    def sacar ():


    valor_caixa = 1000
    valor_atual = valor_caixa

    escreva("Bem vindo ao caixa para saques")
    escolher_operacao()

    while valor_atual <= valor_caixa:

        if valor_atual <= 0:
            print("\nSaldo insuficiente. programa encerrado\n")
            break
