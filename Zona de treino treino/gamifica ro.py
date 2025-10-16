# Faça uma comparação de alguns dos elementos (estruturas de repetição, condição, variáveis, lógica) de pseudocódigo para a sintaxe do C# (ou outra linguagem de programação de sua preferência) e envie no AVA. (alguns comandos, não precisa ser todos)

# Escreva um pseudocódigo que peça um nome, uma idade, verifique se a pessoa é maior de idade.
def classificacao_de_idade_N():

    def escreva (mgs):
        tamanho = len(mgs) + 4
        print("_" * tamanho)
        print(f"  {mgs}")
        print("_" * tamanho)


    resposta = "s"
    while resposta == "s":
        try:
            nome = input("Digite seu nome: ")
            idade = int(input("Digite sua idade: "))

            while idade < 0:
                print(" você digitou um ano de nascimento negativo. por favor corrija.")
                idade = int(input("Tente novamente: "))
        
            if idade < 18:
                escreva(f"{nome}, você tem {idade}anos \n você é menor de idade")

            else:
                escreva(f"{nome}, você tem {idade} anos \n você e maior de idade")

            resposta = input("gostaria repetir o programa? S para sim e N para não: ").lower()
        except ValueError:
            escreva("Tente novamente: ")
    escreva("Você optou por sair")

def resposta():
    #O que é um Pseudocódigo? E quais os benefícios no aprendizado em programação?

    '''O pseudocódigo é uma forma de expressar algoritmos de maneira simples e clara, usando uma linguagem próxima ao português (ou qualquer idioma natural). Ele serve como uma ponte intuitiva entre a ideia de um programa e o código real.

    Clareza e Simplicidade: Permite focar na lógica sem se prender à sintaxe de uma linguagem específica.

    Rascunho Essencial: Atua como um "rascunho" detalhado, ajudando a estruturar o pensamento antes da codificação.

    Independência de Linguagem: Uma vez dominado, pode ser facilmente traduzido para qualquer linguagem de programação (Python, Java, C#, etc.).'''

    #Quais são os tipos de dados Fundamentais?
    '''Inteiro

    Representa números inteiros, sem casas decimais, como 5, -10 ou 0.

    Real

    Para números com casas decimais, como 3.14 ou -0.5.

    Lógico

    Armazena valores booleanos, que podem ser apenas verdadeiro ou falso.

    Caractere (cadeia)

    Usado para texto ou um único caractere, por exemplo, "Olá mundo" ou 'a'.

    '''

    # Qual a diferença entre > e >= ?
    '''O operador > (maior que) verifica se o valor à esquerda é estritamente maior que o valor à direita. Por exemplo, 5 > 3 é verdadeiro, mas 5 > 5 é falso.'''

#1. Variáveis em jogos
#Crie exemplos de variáveis que poderiam existir em um jogo

def dados():
    dano = 0.0
    nome_do_jogador = ""
    selecao_de_nome = 'M'
    mago = False
    vida = 0


    print (type(vida))
    print (type(nome_do_jogador))
    print (type(selecao_de_nome))
    print (type(mago))
    print (type(dano))

#2. Verificação de poderes do mago
#Crie um algoritmo em Portugol que use uma variável booleana chamada mago.

def mago():
    def escreva (mgs):
            tamanho = len(mgs) + 4
            print("_" * tamanho)
            print(f"  {mgs}")
            print("_" * tamanho)

    mago = False

    if mago:
        escreva("Este mago ainda possui poderes")

    else:
        escreva("Não possui poderes disponíveis")

#3. Exemplo de condicional em jogos
#Escreva um exemplo simples de decisão (condicional) que poderia ser usada em um jogo.

def vida():
    def escreva (mgs):
            tamanho = len(mgs) + 4
            print("_" * tamanho)
            print(f"  {mgs}")
            print("_" * tamanho)

    vida = 100
    dano_inimigo = 100
    defesa = 10
    dano_recebido = 0

    while vida > 0:

        decisao = input("gostaria de defender esse ataque? S para sim e N para não: " ).lower()

        if decisao == "s":
            dano_recebido = dano_inimigo - defesa

        elif decisao == "n":
            dano_recebido = dano_inimigo

        vida -= dano_recebido

        if vida > 0:
            escreva(f"Você ainda tem {vida} pontos de vida para lutar")

        else:
            escreva("Game over")
            break

#4. Jogo de adivinhação
#O computador deve gerar um número aleatório entre 1 e 10.
#O jogador deve digitar um número.
#Se o jogador acertar o número, mostrar na tela: "Você acertou!".
#Se o jogador errar, repetir a pergunta até ele acertar.
def jogo_de_adivinhacao():
    import random
    def escreva (mgs):
            tamanho = len(mgs) + 4
            print("_" * tamanho)
            print(f"  {mgs}")
            print("_" * tamanho)

    n_premiado = 10
    numeros = random.randint(1, 10)
    numero_digitado = None

    while numero_digitado != numeros:
        while True:
            try:
                numero_digitado = int(input("Digite um número: "))
                break
            except ValueError:
                escreva("Entrada inválida. Tente novamente.")

        if numero_digitado != numeros:
            escreva(f"Infelizmente o Número {numero_digitado} não é o número certo. Tente novamente")

        else:
            escreva("Parabéns você ganhou!")

#executando a função
jogo_de_adivinhacao()