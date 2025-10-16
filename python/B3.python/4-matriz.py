matriz = []
mlinhas = 3
ncolunas = 2

#declaração de matriz np python percorre a quantidade de linhas
for i in range(0,mlinhas):
    linha = []
    for j in range (0,ncolunas):
        linha.append (0)
    matriz.append(linha)

for i in range (len(matriz)):
    print(matriz[i])



#simples
for i in range (0,mlinhas):
    matriz.append([0]*ncolunas)

for i in range (len(matriz)):
    print(matriz[i])