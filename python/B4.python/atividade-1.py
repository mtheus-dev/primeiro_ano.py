#1)Faça uma função para calcular a área de um triângulo.
def area_do_triangulo():
    def calcular_area_triangulo(base,altura):
        area = (base*altura) / 2
        return area

    b = float(input("Informe o valor da base: "))
    a = float(input("Informe o valor da altura: "))

    print(f"A area do triangulo é: {calcular_area_triangulo(b,a)}")

#2)Faça um procedimento para mostrar um cardápio simples na tela.
def menu():
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

        resposta = input("gostaria de pedir de novo? ")

        if resposta != "s":
            print("você optou por sair")
            break
        
#Faça uma função para verificar se um número é par ou impar e use ele em um if para imprimir se é par ou se é impar.
def par_ou_ímpar():

    def verificação(variavel):
        if variavel % 2 == 0:
            print(f"O número {variavel} é par.")
        
        else:
            print(f"O número {variavel} é ímpar.")

    def escreva(mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)

    resposta = "s"
    while resposta == "s":
        try:
            numero = int(input("Digite um número: "))
        except ValueError:
            escreva("Entrada Invalida. Tente novamente")

        verificação(numero)

        resposta = input("Gostaria de repetir? S para sim N para não: ")

menu()