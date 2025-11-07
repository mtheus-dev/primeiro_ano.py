#Inverter string: leia uma string e imprima-a invertida.'''
def Inverter_string():
    palavra = input("Digite uma palavra: ")
    print(palavra[::-1])

#Contar vogais: leia uma palavra e conte quantas vogais ela contém.
def Contar_vogais():
    palavra = input("Digite uma palavras: ")
    contador = [
        {"variavela": "conteúdo"},
    ]

    vogais = ["a", "e", "i", "o", "u"]

    for i in palavra:
        if i in vogais:
            print(i)

#Palíndromo: verifique se uma string é palíndroma (ignorar maiúsculas/minúsculas).
def palindroma():
    palavra = input("Digite uma palavra: ")

    if palavra == (palavra[::-1]):
        print(f"A palavra '{palavra}' é palíndromo.")

    else:
        print(f"A palavra '{palavra}' não é palíndromo.")

#Soma condicional: dado um número N, calcule a soma apenas dos números pares entre 1 e N.
def media_pares():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta == "s":
        try:
            soma = 0
            n = int(input("Digite um número: "))

            for i in range(1,n):
                if i % 2 == 0:
                    soma += i 
            print(soma)

            resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Digite novamente: ")
    escreva("Você optou por sair.")

#Verificador de primo: determine se um número é primo.
def numero_primo():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta == "s":
        try:
            numero = int(input("Digite um número: "))

            if numero <= 1:
                print("Não é primo.")
            else:
                primo = True

                for i in range(2,numero):
                    if numero % i == 0:
                        primo = False
                        break
                
                if primo == True:
                    print(f"{numero} é primo.")
                else:
                    print(f"{numero} não é primo.")
            
            resposta = input("Gostaria de repetir? S para sim e N para não: ")
        except ValueError:
            escreva("Digite novamente: ")
    escreva("Você optou por sair.")

#Lista de primos até N: gere todos os números primos menores ou iguais a N.
def lista_numeros_primos():

    def primo(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
            
    n = int(input("Número: "))
    for i in range(n+1):
        if primo(i):
            print(i)

#Fibonacci (iterativo): gere os primeiros n termos da sequência (ou retorne o n-ésimo termo).
def sequencia_fibonacci():
    n = int(input("Digite um número: "))
    a = 0
    b = 1
    for i in range(0,n):
        print(a, end=" ")
        a, b = b, a + b
   
#Fibonacci (recursivo): compute o n-ésimo termo usando recursão.
def fibonacci_recursivo(n):
    n = int(input("Digite um número: "))
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

#Menor divisor maior que 1: dado n>1, encontre o menor divisor de n além de 1.
def menor_divisor():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta == "s":
        try:
            n = int(input("Digite um número: "))

            for i in range(2,n+1):
                if (i == n):
                    print("O número é primo!")
                    break
                if n % i == 0:
                    print(i)
                    break
        except ValueError:
            escreva("Tente novamente: ")

#Validador de CPF (formato): verifique se a entrada possui exatamente 11 dígitos.
def cpf():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta == "s":
        try:
            cpf = int(input("Digite o seu CPF: "))

            if len(cpf) == 11:
                print("CPF valido! ")

            else:
                print("Seu CPF tem menos de 11 digitos")

            resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair")

#Contador de caracteres únicos: conte quantos caracteres distintos aparecem numa string (sem diferenciar maiúsculas/minúsculas).
def contador_caracteres():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta == "s":
        try:
            alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            contidos = []

            palavra = input("Digite uma palavra: ").lower()

            for i in palavra:
                if palavra and not i in contidos:
                    contidos.append(i);
            
            print(contidos)

            resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair")

#Maior subsequência crescente consecutiva: leia uma sequência de números até o usuário digitar “sair” e retorne o maior comprimento de subsequência estritamente crescente e consecutiva.


#MDC e MMC: calcule o máximo divisor comum de dois números e, a partir dele, o mínimo múltiplo comum.


#Mini-projeto — jogo de adivinhação por intervalos: descubra interativamente um número pensado pelo usuário entre 1 e 100, reduzindo um intervalo até encontrá-lo.'''

"Esse numero é meno do que {}"

contador_caracteres()