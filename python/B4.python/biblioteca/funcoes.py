def letra_maiusculas(palavra):

    maiusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    resultado = ""

    for letra in palavra:
        trocou = False
        for i in range (len(minusculas)):
            
            if letra == minusculas[i]:

                resultado += (maiusculas[i])
                trocou = True
                break

        if not trocou:
            resultado += letra
                
    print(resultado)

def letra_minuscula(palavra):

    maiusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    resultado = ""

    for letra in palavra:
        trocou = False
        for i in range (len(maiusculas)):#posição da minha letra
            
            if letra == maiusculas[i]:

                resultado += minusculas[i]
                trocou = True
                break

        if not trocou:
            resultado += letra

    print(resultado)

def conta_letras(palavra):

    contador = 0

    for i in palavra:
        
        contador += 1

    print(f"Na palavra {palavra} tem {contador} letras")


def primeira_letra_m(palavra):

    maiusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    resultado = ""

    for letra in palavra:
        trocou = False
        for i in range (len(minusculas)):
            
            if letra[0] == minusculas[i]:

                resultado += (maiusculas[i])
                trocou = True
                break

        if not trocou:
            resultado += letra                
    print(resultado)

primeira_letra_m("banana")