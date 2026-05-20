from trabalho_de_cartas import *

jogador = []
cpu = []

formiga = Carta("Formiga de mel",200,10,15,2,9)
barata = Carta("Barata",600,20,70,9,3)
abelha = Carta("Abelha",500,25,40,7,8)
escorpiao = Carta("Escorpião",2000,85,65,9,5)
mariposa = Carta("Mariposa",1500,50,30,6,10)
louva_deus = Carta("Louva-Deus",700,30,35,2,9)
lacraia = Carta("Lacraia",2000,80,15,10,7)
aranha = Carta("Aranha viuva negra",3000,90,50,10,7)

baralho = [
    formiga,
    barata,
    abelha,
    escorpiao,
    mariposa,
    louva_deus,
    lacraia,
    aranha,
]

def distribuir_cartas(baralho):
    mao_de_jogo = []
    random.shuffle(baralho)
    mao_de_jogo = len(baralho)//2
    return mao_de_jogo

def mao_jogador(baralho):
    mao_jogador = []
    mao_jogador = distribuir_cartas(baralho)
    return mao_jogador

def mao_cpu(baralho):
    mao_cpu = []
    mao_cpu = distribuir_cartas(baralho)
    return mao_cpu

def exibir_mao(mao_jogador,mao_cpu):
    for i in range (len(mao_jogador)):
        print(f"===Mão de jogador===\n{mao_jogador[i]}")

    for i in range (len(mao_cpu[i])):
        print(f"===Mão da CPU===\n{mao_cpu[i]}")


jogador = mao_jogador(baralho)
cpu = mao_cpu(baralho)
exibir_mao(jogador,cpu)