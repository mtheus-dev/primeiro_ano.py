#1)Faça um módulo com as operações de matemáticas:
#● Soma
#● Subtração
#● Divisão
#● Multiplicação
#● Módulo (resto da divisão)
from biblioteca import calculadora as calc

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

    if opcao == 1:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        escreva(f"O valor da sua adição entre o número {numero1} e o número {numero2} é: {calc.soma(numero1,numero2)}")

    elif opcao == 2:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        escreva(f"O valor da sua subtracao entre o número {numero1} e o número {numero2} é: {calc.subtracao(numero1,numero2)}")

    elif opcao == 3:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        escreva(f"O valor da sua divisão entre o número {numero1} e o número {numero2} é: {calc.divisao(numero1,numero2)}")

    elif opcao == 4:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        escreva(f"O valor da sua multiplicação entre o número {numero1} e o número {numero2} é: {calc.multilicacao(numero1,numero2)}")

    elif opcao == 5:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        escreva(f"O valor do seu modulo  entre o número {numero1} e o número {numero2} é: {calc.subtracao(numero1,numero2)}")

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

