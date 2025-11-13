
"""
def letra_minuscula():

def conta_letras():

def maiusculas_1():

banana
"""

def letra_maiusculas(palavra):

    maiusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for letra in palavra:

        for mi in minusculas:
            for ma in maiusculas:
                if letra in minusculas[mi]:
                    letra = maiusculas [ma]

    print(letra)

palavra = input("digite uma palavra: ")

letra_maiusculas(palavra)