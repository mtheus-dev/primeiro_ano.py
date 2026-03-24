#1)Contador de Pontos: Crie um contador que conte de 0 a 50, somando de 5 em 5, simulando a pontuação de um jogador.
#Saída no pc:
#Pontuação: 0
#Pontuação: 5
#Pontuação: 10
#Pontuação: 15
#Pontuação: 20
#Pontuação: 25
#….. Pontuação: 50
def n1():
    for i in range(0,50+ 5,5):
        print(f"Pontuação: {i}")

#2)Exibição de Inimigos: Use um laço PARA para exibir 7 inimigos na tela, imprimindo a mensagem "Exibindo inimigo [número do inimigo]".
#Saída no pc:
#Exibindo inimigo 1
#Exibindo inimigo 2
#Exibindo inimigo 3
def n2():
    for i in range(1,8):
        print(f"Exibindo inimigo {i}")

#3)Vida do Chefe: Use um laço ENQUANTO para diminuir a vida de uma variável
#chamada chefe, que começa com 200 pontos de vida. A cada repetição, a
#vida diminui em 10. O laço deve parar quando a vida chegar a 0.
#Saída no pc:
#Personagem perdeu 10 pontos, está com 190 pontos
#Personagem perdeu 10 pontos, está com 180 pontos
#Personagem perdeu 10 pontos, está com 170 pontos
def n3():
    vida = 200
    while vida > 0:
        vida = vida - 10
        print(f"Personagem perdeu 10 pontos, está com {vida} pontos")

#4) Menu de Pausa: Use um laço REPITA... ATÉ para criar um menu de pausa que só
#para de se repetir quando o jogador pressiona a tecla "S" para "Sair". O laço
#deve sempre mostrar a mensagem "Jogo pausado. Pressione S para sair.".
#Saída no pc:
#“Jogo pausado. Pressione S para sair.”
#Usuário: A
#“Jogo pausado. Pressione S para sair.”
#Usuário: X
#”Jogo pausado. Pressione S para sair.”
#Usuário: S
#“Jogo finalizado, até a próxima!”
def n4():
    desisao = ""
    while desisao != "s":

        desisao = input("Jogo pausado. Pressione S para sair.").lower()

    print("Jogo finalizado, até a próxima!")

#5)Coletando Itens: Imagine que você tem 15 moedas para coletar. Use um laço
#PARA para simular a coleta, exibindo a mensagem "Moeda [número da moeda]
#coletada." para cada uma.
#Saída no pc:
#Moeda 1 coletada
#Moeda 2 coletada
#Moeda 3 coletada
#Moeda 4 coletada
#Moeda 5 coletada
#Moeda 6 coletada
#…até o 15
def n5():
    for i in range(1,16):
        print(f"Moeda {i} coletada")

#6)Jogo de Dados: Simule um jogo de dados com um laço FAÇA ENQUANTO . O
#jogo deve continuar enquanto a soma das variáveis com números aleatórios
#entre 0 e 100, e 5,50 for menor que 100. A cada rodada, imprima a soma atual.
#(se caso for fazer na IDE online de portugol: procure pela biblioteca por uma
#função que vai sortear os números para você).
#Soma atual: 12
#Soma atual: 25
#Soma atual: 43
#Soma atual: 58
#Soma atual: 76
#Soma atual: 89
#Soma atual: 101
#Soma foi maior que 100, jogo finalizado!
def n6():
    import random

    numero = 0
    dados = 100

    while numero < dados:

        numero = (5.50 + random.randint(0,100))

        print(f"Soma atual: {numero}")
    print("Soma foi maior que 100, jogo finalizado!")

#7)Pontuação com Bônus: Crie um laço que adicione pontos ao jogador. Ele deve
#começar com 0 pontos e, a cada repetição, ganhar 10 pontos. Quando o
#jogador tiver 100 pontos, ele ganha um bônus de 50 pontos, e o laço para.
#Jogador está com 10 pontos
#Jogador está com 20 pontos
#Jogador está com 30 pontos
#Jogador está com 40 pontos
#Jogador está com 50 pontos
#Jogador está com 60 pontos
#Jogador está com 70 pontos
#Jogador está com 80 pontos
#Jogador está com 90 pontos
#Jogador está com 100 pontos
#jogador ganhou bônus de 50 pontos! Pontuação final: 150
def  n7():
    pontos = 0
    while pontos < 100:
        pontos += 10
        print(f"Jogador está com {pontos} pontos")

    print(f"jogador ganhou bônus de 50 pontos! Pontuação final: {pontos + 50}")

#8)Repetição de Ataque: Crie um laço PARA que simule 5 ataques seguidos do
#seu personagem, exibindo a mensagem "Ataque [número do ataque]
#realizado!".
#Ataque 1 realizado!
#Ataque 2 realizado!
#Ataque 3 realizado!
#Ataque 4 realizado!
#Ataque 5 realizado!
def n8():
    for i in range(1,6):
        print(f"Ataque {i} realizado!")

#9)Validação de Nível: Crie um laço REPITA... ATÉ que peça ao jogador para digitar
#um número de nível para jogar. O laço deve continuar a pedir um número até
#Exercícios 3
#que o jogador digite um valor entre 1 e 5.
#Digite um nível de 1 a 5:
#Usuário: 8
#Número inválido, tente novamente.
#Digite um nível de 1 a 5:
#Usuário: 0
#Número inválido, tente novamente.
#Digite um nível de 1 a 5:
#Usuário: 3
#Nível 3 selecionado, bom jogo!
def n9():
    while True:

        desicao = int(input("Digite um número:"))

        if 1 < desicao > 5:
            print("Número inválido, tente novamente.")
        
        else:
            print(f"Nível {desicao} selecionado, bom jogo!")
            break

#10)Barra de Energia: Simule o carregamento de uma barra de energia usando um
#laço ENQUANTO . A barra começa em 0% e vai até 100%, aumentando de 10 em
#10. Imprima o progresso a cada etapa.
#Carregando energia: 0%
#Carregando energia: 10%
#Carregando energia: 20%
#Carregando energia: 30%
#Carregando energia: 40%
#Carregando energia: 50%
#Carregando energia: 60%
#Carregando energia: 70%
#Carregando energia: 80%
#Carregando energia: 90%
#Carregando energia: 100%

energia = 0
while energia < 100:
    energia += 10
    print(f"Carregando energia: {energia}%")

    