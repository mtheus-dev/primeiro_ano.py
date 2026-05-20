import random
class Carta:
    #construtor
    def __init__(self,nome0,resistencia1,ataque2,defesa3,dano_psicologico4,beleza5):
        #atributos
        self.__nome = nome0
        self.__resistencia = resistencia1
        self.__ataque = ataque2
        self.__defesa = defesa3
        self.__dano_psicologico = dano_psicologico4
        self.__beleza = beleza5

    def get_nome(self):
        nome = self.__nome
        return nome
    
    def get_resistencia(self):
        resistencia = self.__resistencia
        return resistencia
    
    def get_ataque(self):
        ataque = self.__ataque
        return ataque
    
    def get_defesa(self):
        defesa = self.__defesa
        return defesa
    
    def get_dano_psicalogico(self):
        dano_psicologico = self.__dano_psicologico
        return dano_psicologico
    
    def get_beleza(self):
        beleza = self.__beleza
        return beleza


        