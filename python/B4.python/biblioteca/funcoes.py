
"""
def letra_minuscula():

def conta_letras():

def maiusculas_1():

banana
"""

def letra_maiusculas(palavra):

    maiusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    resultado = ""

    for letra in palavra:
        trocou = False
        for i in range (len(minusculas)):#posição da minha letra
            
            if letra == minusculas[i]:

                resultado += (maiusculas[i])
                trocou = True
                break

            if not trocou:
                resultado += letra
                
    print(resultado)

letra_maiusculas("palavra")