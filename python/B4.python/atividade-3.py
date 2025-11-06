#1)Faça um módulo com as operações de matemáticas:
#● Soma
#● Subtração
#● Divisão
#● Multiplicação
#● Módulo (resto da divisão)
import calculadora as calc

def escreva (mgs):
    tamanho = len(mgs) + 4
    print("_" * tamanho)
    print(f"  {mgs}")
    print("_" * tamanho)

def menu():
    print("\nEscolha uma operação matematica:")
    print("1 - adição")
    print("2 - subtração")
    print("3 - Divisão")
    print("4 - multiplicação")
    print("5 - Módulo da divisão")
    print("0 - sair")
    
    while True:
        try:

            opcao = int(input("Digite a opção desejada: "))
            break

        except ValueError:
            escreva("Entrada invalida.Tente novamente")

    return opcao

opcao = menu()

while True:

#2)Faça um módulo com as operações para:
#● Encontrar o maior número
#● Encontrar o menor número
#● Saber se um número é par ou impar



#3)Faça um módulo com as seguintes funções:
#● Tornar a string toda em letras maiúsculas.
#● Tornar a string toda em letras minúsculas.
#● Contar quantas letras tem na string.
#● Tornar a primeira letra da string em letra maiúscula e a restante em minúscula.



#4)Faça um módulo para:
#● Converter horas para segundos
#● Converter minutos para segundos
#● Através de um horário em hh:mm:ss, descobrir
#quantos segundos tem este horário usando as funções anteriores.

