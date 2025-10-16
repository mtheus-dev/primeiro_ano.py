'''
PROGRAMA: FUNCIONAMENTO DO ENQUUANTO - WHILE
DATA: 12/06/2025
autor:Matheus Henrique De Lima Soares 1B de informatica
'''
# Escreva um programa que solicite do usuário login e senha, ele só terá 3 tentativas para acertar.
contador = 1 
login = "admin"
senha = 12345

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
    senha_user = int(input("Entre com a sua numérica: "))

    if  login_user == login and senha_user == senha:
        print("_____________")
        print("Acesso autorizado.")
        print("________________")
        
    else:
        print("______________________________")
        print("ACESSO NEGADO. Entre em contado com o administrador do sistema.")
        print("_______________________________")