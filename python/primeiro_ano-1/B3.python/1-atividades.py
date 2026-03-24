#1) Elabore um programa que efetue a leitura devalores positivos inteiros até que um valor negativo seja informado. Ao final devem ser apresentados o maior e o menor valores informados pelo usuário. 

def numero_maior_e_menor ():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    maior = -99999
    menor = 99999

    resposta = "s"
    while resposta == "s":
        try:
            while True:
                n = int(input("informe um número: "))
                if n < 0:
                    break

                #verifica e atualiza o maior valor
                if n > maior:
                    maior = n
                #verifica e atualiza o menor valor
                if n < menor:
                    menor = n

            print(f"Maior valor lido: {maior}")
            print(f"Menor valor lido: {menor}")
            
        except ValueError:
            escreva ("Tente novamente: ")

        resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
    escreva("Você optou por sair.")
#2) Elabore um programa para efetuar o cálculo do fatorial do número 5, 5!”. Desta forma, temos que 5! = 5 x 4 x 3 x 2 x 1, ou seja, 5! = 120.

def fatorial():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    total = 1

    resposta = "s"
    while resposta == "s":
        try:
            numero = int(input("Digite um número: "))

            while numero <= 0:
                numero = int(input("O número tem que ser positivo: "))

            for i in range (1,numero+1,1):
                total *= i

            print(f"O fatorial de {numero} é {total}")

            resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair.")


#3) Faça um programa para apresentar todos os números divisíveis por 4 que sejam menores que 200. Para verificar se o número é divisível por 4, é necessário verificar se o resto da divisão por 4 é nulo. Se o número é divisível; sendo, mostre-o; não sendo, passe para o próximo passo. 

def numeros_divisiveis_por_4():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    resposta = "s"
    while resposta == "s":

        for i in range (1,201):
            if i % 4 == 0:
                print(i)
        
        resposta = input("Gostaria de fazer de roda esse programa de novo? S para sim e N para não: ").lower()
    escreva("Você optou por sair")


#4) Elaborar um programa que apresente como resultado o valor do fatorial dos valores ímpares situados na faixa numérica de 1 a 10. 

def fatotial_impares():
    total = 1

    for i in range (1,10+1,1):
        total *= i
        if i % 2 != 0:
            print(total)


#5) Elaborar um programa que calcule a seguinte fórmula:

def formula():
    n = 1
    total = 0
    for i in range (1,101,1):
        total += n / i 
    print (f"Resultado: %.3f " % total)


#Menu de opções
