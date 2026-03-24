#1)Faça uma função para calcular a área de um triângulo.
def area_do_triangulo():
    def calcular_area_triangulo(base,altura):
        area = (base*altura) / 2
        return area

    b = float(input("Informe o valor da base: "))
    a = float(input("Informe o valor da altura: "))

    print(f"A area do triangulo é: {calcular_area_triangulo(b,a)}")

#2)Faça um procedimento para mostrar um cardápio simples na tela.
def menu_restaurante():
    def mostrar_cardapio():
        print("cardápio")
        print("1-Hambúrguer")
        print("2-Batata frita")
        print("3-Refrigerante")

    while True:

        mostrar_cardapio()

        escolhido = int(input("Escolha seu pedido: "))

        while escolhido < 1 or escolhido > 3:
            print("Pedido inválida, escolha novamente: ")

        if escolhido == 1:
            print("Está com fome né? escolheu o hambúrguer")

        if escolhido == 2:
            print("Boa escolha, batata para entrada ")

        if escolhido == 3:
            print("Refrigerante para acompanhar")

        resposta = input("gostaria de pedir de novo? ").lower()

        if resposta != "s":
            print("você optou por sair")
            break
        
#3)Faça uma função para verificar se um número é par ou impar e use ele em um if para imprimir se é par ou se é impar.
def par_ou_ímpar():

    def verificação(variavel,lista_par,lista_impar):
        if variavel % 2 == 0:
            lista_par.append(variavel)
        else:
            lista_impar.append(variavel)

    def escreva(mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    quantidade = 10
    pares = []
    impares = []
    while True:
        for i in range(quantidade):
            while True:
                try:
                    numero = int(input(f"Digite o {i+1} número: "))
                    break
                except ValueError:
                    escreva("Entrada Invalida. Tente novamente")

            verificação(numero,pares,impares)

        escreva(f"Os números {pares} são pares.")

        escreva(f"Os números {impares} são ímpar.")

        resposta = input("Gostaria de repetir? S para sim N para não: ").lower()

        if resposta != "s":
            escreva("Você optou por sair")
            break

#Crie uma função calcular_desconto(preco, porcentagem) que retorne o preço com desconto. Crie um procedimento mostrar_preco_final(preco, porcentagem) que use a função acima e imprima o resultado.
def desconto():
    def calcular_desconto(preco,porcentagem):
        desconto = (porcentagem/100) * preco
        preco_final = preco - desconto
        return preco_final


    def mostrar_preco_final(preco, porcentagem):
        preco_com_desconto = calcular_desconto(preco,porcentagem)

        print(f"O preço do produto com {porcentagem}% de desconto é de {preco_com_desconto}")


    def escreva(mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    preco = 0
    porcentagem = 0

    while True:
        while True:
            try:
                preco = int(input("Digite o preço do produto: "))
                porcentagem = int(input("Digite o desconto do produto: "))
                break
            except ValueError:
                escreva("Entrada invalida. Tente novamente")
            
        mostrar_preco_final(preco,porcentagem)

        resposta = input("Gostaria de repetir? S para e N para não: ").lower()

        if resposta != "s":
            escreva("Você optou por sair")
            break

