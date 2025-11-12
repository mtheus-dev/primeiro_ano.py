def maior_n(vetor):
    maior = vetor[0]

    for i in range(len(vetor)):

        if maior < vetor[i]:
            maior = vetor[i] 

    return maior

def menor_n(vetor):
    menor = vetor[0]

    for i in range(len(vetor)):

        if menor > vetor[i]:
            menor = vetor[i]

    return menor

def par_ou_impar(vetor):
    pares = []
    impares = []
    for i in range(len(vetor)):

        if vetor[i] % 2 == 0:
            pares.append(vetor[i])

        else:
            impares.append(vetor[i])

    return pares, impares
g