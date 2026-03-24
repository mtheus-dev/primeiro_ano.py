#Leia uma matriz de 5x5 e verifique:
#– Qual o maior elemento da matriz e sua
#respectiva posição (linha e coluna).
#– Qual o menor elemento da matriz e sua
#respectiva posição (linha e coluna).
#– Qual a soma dos números da matriz.
#– Qual a média dos números da matriz.

def analisar_matriz_5x5():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    linhas = 2
    colunas = 2
    matriz = []
    soma = 0
    elementos = 0

    for i in range (linhas):
        matriz.append([0]*colunas)

    for i in range (linhas):
        for j in range (colunas):
            while True:
                try:
                    num = int(input(f"informe um numero para os indices [{i+1}] [{j+1}]: "))
                    break
                except ValueError:
                    escreva("Entrada inválida. Tente novamente.")
            
            soma += num
            elementos += 1

            matriz[i][j] = num

    maior_numero = matriz [0][0]
    menor_numero = matriz [0][0]
    posicao_maior = (0,0)
    posicao_menor = (0,0)

    for i in range (linhas):
        for j in range (colunas):
            if matriz [i][j] > maior_numero:
                maior_numero = matriz[i][j]
                posicao_maior = (i,j)

            if matriz [i][j] < menor_numero:
                menor_numero = matriz[i][j]
                posicao_menor = (i,j)
        
    media = soma / elementos

    escreva("Matriz informada:")
    for linha in matriz:
        print(" "+" ".join(f"{num:3}" for num in linha))

    escreva(f"O maior número da Matriz é {maior_numero} e está na linha {posicao_maior [0] + 1} coluna {posicao_maior [1] + 1}")

    escreva(f"O menor número da matriz é {menor_numero} e está na linha {posicao_menor [0] + 1} coluna {posicao_menor [1] + 1}")

    escreva(f"A soma dos números da matriz é {soma}")

    escreva(f"Média dos elementos é {media}")

#Leia uma matriz de 3x3 e verifique se há
#números repetidos na matriz. Caso tenha,
#imprima “SIM”, se não, imprima “NAO”.
def verificacao_de_numeros():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    linhas = 3
    colunas = 3
    matriz = []
    todos_numeros = []
    numeros_repitidos = 0

    # criando matriz
    for i in range(linhas):
        linha = []

    #verificação de entrada inválida
    for i in range(linhas):
        for j in range (colunas):
            while True:
                try:
                    num = int(input(f"informe um numero para os indices [{i+1}] [{j+1}]: "))
                    linha.append(num)
                    todos_numeros.append(num)
                    break
                except ValueError:
                    escreva("Entrada inválida. Tente novamente.")

        matriz.append(linha)

    escreva("Matriz informada:")
    for linha_m in matriz:
        print(" "+" ".join(f"{num:3}" for num in linha_m))
        
    #verificação para ver se tem números repetidos
    for m in range (len(todos_numeros)):
        for n in range (m+1,len(todos_numeros)):

            if todos_numeros[m] == todos_numeros[n]:
                numeros_repitidos += 1
                
        break
    if numeros_repitidos != 0:
        escreva("SIM")
    else:
        escreva("NÃO")

#Faça um programa que leia duas matrizes 2x2 e imprima a matriz C com a soma das matrizes A e B.
def multiplicacaodematriz():
    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    linhas = 2
    colunas = 2
    matriz_a = []
    matriz_b = []
    matriz_c = []

    def criando_matriz(nome):
        matriz = []
        #criando matriz.
        #verificação de entrada inválida.
        for i in range (linhas):
            mlinha = []
            for j in range (colunas):
                while True:
                    try:
                        numero = int(input(f"informe um numero para os indices [{i+1}] [{j+1}]: "))
                        mlinha.append(numero)
                        break
                    except ValueError:
                        escreva("Entrada inválida. Tente novamente.")

            matriz.append(mlinha)
        escreva("Matriz informada:")
        for linha in matriz:
            print(" "+" ".join(f"{num:3}" for num in linha))
            return matriz

    #criando matriz A
    escreva("==Matriz A==")
    matriz_a = criando_matriz("A")

    #criando matriz B
    escreva("==Matriz B==")
    matriz_b = criando_matriz("B")

    #resultado Matriz C
    for i in range (linhas):
        linha = []
        for j in range (colunas):
            
            linha.append(matriz_a[i][j]*matriz_b[i][j])
        matriz_c.append(linha)

    escreva("==Matriz C ==")
    for linha in matriz_c:
        print(" "+" ".join(f"{num:3}" for num in linha))

#Leia uma matriz 3x3 e retorne o maior elemento de cada linha.

#Faça um programa que leia uma matriz 3x3 e multiplique os elementos da diagonal principal por k. Imprima a matriz antes e depois da multiplicação.
