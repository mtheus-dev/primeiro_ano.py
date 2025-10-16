#1) Ler um vetor com 15 elementos inteiros. Construir um programa que mostre quantos números do vetor são números primos.
def números_primos():
    def escreva(mgs):
        tamanho = len(mgs) + 4
        print("_"*tamanho)
        print(f"  {mgs}")
        print("_"*tamanho)

    resposta = "s"
    while resposta == "s":
        try:
            vetor_primo = []
            vetor_n_primo = []
            quantidades = 5
            contador = 0

            for i in range(quantidades):
                numero = int(input(f"Digite o {i+1}º número: "))

                if numero <= 1:
                    vetor_n_primo.append (numero);

                else:
                    primo = True
                    
                for i in range (2,int(numero**0.5)+1):
                    if numero % i == 0:
                        primo = False
                        vetor_n_primo.append (numero);

                    else:
                        vetor_primo.append (numero);
                        contador += 1

            escreva(f"Tem {contador} números primos e sendo eles {vetor_primo}")

            resposta = input("Gostaria de repetir? S para sim e N para não: ")
            escreva("Você optou por sair.")
        except ValueError:
            escreva("Digite novamente: ")

#2) Ler um vetor com 20 números inteiros. Criar um segundo vetor contendo apenas os números pares do primeiro, e um terceiro vetor contendo apenas os números ímpares.
def numero_pares_impares():
    def escreva(mgs):
        tamanho = len(mgs) + 4
        print("_"*tamanho)
        print(f"  {mgs}")
        print("_"*tamanho)

    resposta = "s"
    while resposta == "s":
        vetor_a = []
        vetor_pares = []
        vetor_impares = []
        contador_pares = 0
        contador_impares = 0
        quantidade = 5

        for i in range (quantidade):
                numero = input(f"Digite o {i+1}º número: ")
                while not numero.isdecimal():
                    print("Tente novamente")
                    numero = input(f"Digite o {i+1}º número: ")
                
                numero = int(numero)
        
                vetor_a.append (numero)

                if numero % 2 == 0:
                    vetor_pares.append (numero)
                    contador_pares += 1

                else:
                    vetor_impares.append (numero)
                    contador_impares += 1

        escreva(f"Dos números {vetor_a} tem {contador_pares} números pares e {contador_impares} números impares sendo eles {vetor_pares} pares e {contador_impares} impares")

        resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()

        if resposta != "s":
            escreva("Você optou por sair")

#3) Ler um vetor com 12 números reais representando as temperaturas médias de cada mês do ano. Mostrar a maior temperatura, a menor temperatura e em que mês elas ocorreram.
vetor_temperatura = []

#4) Ler um vetor com 10 números inteiros e verificar se existem elementos repetidos. Caso existam, mostrar quais são os números repetidos.

#5) Ler um vetor com 15 números inteiros. Mostrar o segundo maior e o segundo menor valor armazenado no vetor.

#6) Ler um vetor com 10 nomes. Depois, solicitar ao usuário um nome e verificar se ele está presente no vetor. Se estiver, mostrar a posição; caso contrário, informar que não foi encontrado.

#7) Ler dois vetores com 5 números inteiros cada. Construir um vetor C que contenha apenas os elementos que aparecem nos dois vetores (interseção).

#8) Ler um vetor com 8 números inteiros. Construir um vetor com os mesmos números, mas sem repetir valores (remover duplicatas).

#executando as funções
numero_pares_impares()