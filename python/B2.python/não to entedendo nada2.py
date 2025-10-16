'''
PROGRAMA: FUNCIONAMENTO DO ENQUUANTO - WHILE
PROGRAMA 2
Autor:Matheus Henrique de lima Soares
'''
#Faça um algoritmo que simule um caixa eletronico, o usuário pode sacar enquanto tiver dinheiro

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

