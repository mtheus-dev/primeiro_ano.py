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

login()