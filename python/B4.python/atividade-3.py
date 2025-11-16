#1)Faça um módulo com as operações de matemáticas:
#● Soma
#● Subtração
#● Divisão
#● Multiplicação
#● Módulo (resto da divisão)
def calculadora():
    from biblioteca import calculadora as calc

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    def menu_calculadora():
        escreva("\nEscolha uma operação matematica:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Divisão")
        print("4 - Multiplicação")
        print("5 - Módulo da divisão")
        print("0 - Sair")
        
        while True:
            try:

                opcao = int(input("Digite a opção desejada: "))
                
                if opcao >= 0 and opcao <= 5:
                    return opcao
                
                else:
                    escreva("Esse número não está no menu. Tente novamente")

            except ValueError:
                escreva("Entrada invalida.Tente novamente")

    def executar_operacoes(nome,funcao):
        while True:
            try:
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: "))
                break
            except ValueError:
                escreva("Entrada invalida. Tente novamente")
        resultado = funcao(numero1,numero2)

        escreva(f"O valor da sua {nome} entre o número {numero1:.2f} e o número {numero2:.2f} é: {resultado:.2f}")

    operacoes = {
        1:("adição",calc.soma),
        2:("subtração",calc.subtracao),
        3:("divisão",calc.divisao),
        4:("multiplicação",calc.multiplicacao),
        5:("módulo da divisão",calc.modulo)
    }

    while True:
        opcao = menu_calculadora()

        if opcao == 0:
            escreva("Você optou por sair")
            break

        nome, funcao = operacoes[opcao]
        executar_operacoes(nome,funcao)
    
#2)Faça um módulo com as operações para:
#● Encontrar o maior número
#● Encontrar o menor número
#● Saber se um número é par ou impar
from biblioteca import operacoes as oper
def operacao():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho) 
        print(f"  {mgs}")
        print("_" * tamanho)

    def menu_operacoes():
        escreva("\nEscolha uma operação")
        print("1 - Encontrar o maior número")
        print("2 - Encontra o menor número")
        print("3 - Saber se um número é par ou impar")
        print("0 - sair")

        while True:
            try:

                opcao = int(input("Digite a opção desejada: "))

                if opcao >= 0 and opcao <=  3:
                    return opcao
                
                else:
                    escreva("Esse número não está no menu. Tente novamente")

            except ValueError:
                escreva("Entrada invalida. Tente novamente")

    def executando_operacoes(nome,funcao,vetor = None):
        if vetor is None:
            vetor = []

        for i in range(quantidade):
            numeros = int(input(f"Digite o {i+1} número: ")
            )

            vetor.append(numeros)

        if nome != "par_e_impar" and funcao != oper.par_ou_impar:

            escreva(f"O {nome} número da lista {vetor} é: {funcao(vetor)}") 

        else:
            pares, impares = oper.par_ou_impar(vetor)
            escreva(f"Os números pares e impares da lista{vetor} é de sendo pares {pares} e impares {impares}")

    operacoes = {
        1:("maior",oper.maior_n,),
        2:("menor",oper.menor_n),
        3:("par_e_impar",oper.par_ou_impar)
    }

    quantidade = 10

    while True:
        opcao = menu_operacoes()

        if opcao == 0:
            escreva("Você optou por sair")
            break

        nome, funcao = operacoes[opcao]
        executando_operacoes(nome,funcao)

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
