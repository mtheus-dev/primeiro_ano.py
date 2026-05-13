import random
class Carta:
    #construtor
    def __init__(self,nome0,resistencia1,ataque2,defesa3,dano_psicologico4,beleza5):
        #atributos
        self.nome = nome0
        self.resistencia = resistencia1
        self.ataque = ataque2
        self.defesa = defesa3
        self.dano_psicologico = dano_psicologico4
        self.beleza = beleza5

    def distribuir_cartas(self,baralho):
        random.shuffle(baralho)
        mao_jogador = len(baralho)//2
        return mao_jogador

    def exibir(self):