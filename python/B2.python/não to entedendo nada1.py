'''
PROGRAMA: FUNCIONAMENTO DO ENQUUANTO - WHILE
DATA: 12/06/2025
autor:Matheus Henrique De Lima Soares 1B de informatica
'''
# Escreva um programa que solicite do usuário login e senha, ele só terá 3 tentativas para acertar.

# isso e a mesma coisa que o outro que expliquei só que com contador( o contador serve para contar as tentativas eu tenho para corrigir)
contador = 0
login = "admin"
senha = 1234

print("________________________________")
print("ACESSO AO SISTEMA")
print("Entre com login e senha")
print("____________________________")

login_user = input("Entre com seu login: ")
senha_user = int(input("Entre com a sua senha numérica: "))

while contador <=3 and (login_user != login or senha_user != senha):# se o contador for menor ou igual a 3 e o login ou senha estiverem errados esse codigo vai repetir
    print("Foi sua tentativa ", contador,"tente novamente")
    contador = contador + 1# isso serve para contar as tentativas que o usuário fez(e se chagar a 3 tentativas o codigo para)
    login_user = input("Entre com seu login: ")
    senha_user = int(input("Entre com a sua numérica: "))

    if  login_user == login and senha_user == senha:# se o login e a senha estiverem corretos o acesso é autorizado
        print("_____________")
        print("Acesso autorizado.")
        print("________________")
        
    else:
        print("______________________________")
        print("ACESSO NEGADO. Entre em contado com o administrador do sistema.")
        print("_______________________________")