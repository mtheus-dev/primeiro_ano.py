#1) Crie uma função chamada somar_vetor(vetor) que receba uma lista de números e retorne a soma de todos os elementos.
def soma_da_lista_professor():
    def somar_vetor(vetor):
        soma = 0
        for i in range(len(vetor)):
            soma += vetor[i]
        return soma

    lista = []
    quantidade = 5

    for i in range(quantidade):
        numero = int(input(f"Digite o {i+1} número: "))

        lista.append(numero)

    print(f"A soma dos números {lista} é: {somar_vetor(lista)}")

def soma_da_lista_matheus():
    import random
    lista = []
    quantidade = 10

    for i in range(quantidade):  
        lista.append(random.randint(0,100))
    
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    soma = sum(lista)

    escreva(f"A soma dos números {lista} é: {soma}")

#2) Crie um procedimento contar_pares_impares(vetor) que mostre quantos números pares e ímpares existem na lista.
def conta_lista_pares_impares():
    import random
    lista = []
    contador_impares = 0
    contador_pares = 0
    quantidade = 10

    for i in range(quantidade):
        lista.append(random.randint(0,100))

    def conta_pares_impares(vetor,conta_impares,conta_pares):
        for i in range(quantidade):
            if vetor[i] % 2 != 0:
                conta_impares += 1

            else:
                conta_pares += 1

        print(f"Na lista {lista} tem {conta_pares} números pares e {conta_impares} números impares")

    conta_pares_impares(lista,contador_impares,contador_pares)

#3) Crie uma função buscar_elemento(vetor, valor) que retorne True se o valor estiver presente no vetor e False caso contrário.
import random
lista = []
quantidade = 10

for i in range(quantidade):
    lista.append(random.randint(0,100))

def buscar_elemento(vetor, valor):
    for i in vetor:
        if vetor[i] == valor:
            return True
        else:
            return False
        
valor = random.randint(0,100)

buscar_elemento(lista,)
    

    


#4) Faça uma função interseccao(v1, v2) que receba dois vetores e retorne uma lista com os elementos que aparecem em ambos.



#5) Crie um módulo chamado conversoes.py com funções para converter:
#• Metros em centímetros;
#• Celsius em Fahrenheit (Fórmula: F = (C x 1,8) + 32 ),
#• Reais para dólares (1 real = 0,19 dólares).
#No arquivo principal, importe o módulo e permita que o usuário escolha qual conversão deseja realiz