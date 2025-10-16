'''
Curso Técnico em Informática Integrado ao Ensino Médio
Disciplina:Lógica de Programação
Professor(a):Jean Carlos Wai Keung e Sabrina Maria Rodrigues Feliciano da Silva
Atividade avaliativa    Data 24/07/2025
Acadêmico:Matheus Henrique de Lima Soares 
'''
#1)Faça um programa que solicite do usuário um número inteiro.Após isso liste na tela todos os números inteiros deste o número digitado até 0.Ao final pergunte ao usuário se ele quer repetir o programa, se a resposta for sim ele deve inicia novamente.(Devem ser usados, obrigatoriamente  nesta questão:if,while e for).
def conta_ate_zero():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta =="s":
        try:
            numero = int(input("Digite um número: "))

            if numero > 0:
                for i in range(numero,-1,-1):
                    print(i)
            else:
                print("Não a um intervalo entre esse número e 0")
            resposta = input("Gostaria de fazer de roda esse programa de novo? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair")
#2)Faça um programa que solicite do usuário um número e uma palavra.Em sequida, o programa deve mostrar a palavra escolhida n vezes, onde n é o número informado pelo usuário.
def repete_palavra():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta =="s":
        try:
            palavra = str(input("Digite uma palavra: "))
            numero = int(input("Digite quantas vezes deseja que essa palavra se repita: "))

            if numero > 0:
                for i in range(numero):
                    print(palavra)
            else:
                print("Você digitou um número igual a 0 ou menor que 0")
            resposta = input("Gostaria de fazer de roda esse programa de novo? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair")

#3)Faça um programa que solicite 10 números inteiros e positivos para o usuário, em seguida o programa deve informar na tela quantos são pares e quantos são ímpares. Ao final o programa deve perguntar ao usuário se ele quer rodar o programa novamente. Se a resposta for sim ele deve iniciar novamente.
def pares_impares():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta == "s":
        par = 0
        impar = 0
        try:
            for i in range(1,11):
                numero = int(input("Digite 10 números positivos: "))
                while numero < 0:
                    print("Você digitou um número negativo")
                    numero = int(input("Redigite o numero: ")) 
                if numero % 2 == 0:
                    print(f"O número {numero} é par.")
                    par+=1
                else:
                    print(f"O número {numero} é impar")
                    impar+=1

            escreva(f"existem {par} números pares e {impar} números impares.")

            resposta = input("Gostaria de fazer de roda esse programa de novo? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair.")



def menu():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    print("Escolha uma das opções abaixo: ")
    print("1 - Contar até zero")
    print("2 - Repetir palavra")
    print("3 - Números pares e ímpares")
    print("0 - Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        conta_ate_zero()
        menu()
    elif escolha == "2":
        repete_palavra()
        menu()
    elif escolha == "3":
        pares_impares()
        menu()
    elif escolha == "0":
        escreva("Você optou por sair.")
    else:
        escreva("Opção inválida. Tente novamente.")
        menu()


# Inicia o programa
menu()