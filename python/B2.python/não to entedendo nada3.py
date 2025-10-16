'''
PROGRAMA: FUNCIONAMENTO DO ENQUUANTO - WHILE
PROGRAMA 3
autor:Matheus Henrique De Lima Soares 1B de informatica
'''
#3.	Crie um algoritmo que solicite do usuário um valor em reais e em seguida pergunte para qual moeda deve ser convertido: dólar ou euro.

'''conotação_do_Dólar = 5.529 
conotação_do_Euro = 6.353
continua = True
 
while continua :
    resposta = input("Deseja transformar valores em real para euro ou dólar? S para sim e N para não: ")
    if resposta == 'n' or resposta == 'N':
        print("Adeus")
        break
    valor_em_reais =float(input("Insira o valor em reais: "))
    if valor_em_reais >= 0:

        moeda = input("Para que moeda você gostaria de converter? Digite D para dólar e E para euro ")

        if moeda == 'D' or moeda == 'd':
        
            valor_em_Dólar = valor_em_reais/conotação_do_Dólar
            print(f"Sua conversão de reais para dólar deu {valor_em_Dólar:.2f}")

        elif moeda == 'E' or moeda == 'e':

            valor_em_Euro = valor_em_reais/conotação_do_Euro
            print(f"Sua conversão de reais para euro deu {valor_em_Euro:.2f}")

        else: 
            print("Você não escolheu Dólar e nem Euro.")
    else:
        print("você colocou o valor em reais está negativo. por favor corrija ")
        break'''

#versão mais organizada

def escreva (mgs):
    tamanho = len(mgs) + 4
    print("_" * tamanho)
    print(f"  {mgs}")
    print("_" * tamanho)


conotacao_do_dolar = 5.529
conotacao_do_euro = 6.353

resposta = "s"
while resposta == "s":
    try:
        valor_em_reais = float(input("Insira o valor em reais: "))

        while valor_em_reais < 0:
            print("O valor em reais está negativo. por favor corrija")
            valor_em_reais = float(input("Tente novamente: "))

        moeda = input("Para que moeda você gostaria de converter? Digite D para dólar e E para euro: ").lower()

        while moeda != 'd' and moeda != 'e':
            moeda = input("Você não escolheu Dólar e nem Euro. Por favor tente novamente:").lower()

        if moeda == 'd':
            valor_em_Dólar = valor_em_reais / conotacao_do_dolar
            print(f"Sua conversão de reais para dólar deu {valor_em_Dólar:.2f}")

        elif moeda == 'e':
            valor_em_euro = valor_em_reais / conotacao_do_euro
            print(f"Sua conversão de reais para euro deu {valor_em_euro:.2f}")

        resposta = input("Gostaria de repetir? S para sim e N para não: ").lower()
    except ValueError:
        escreva("Tente novamente: ")
escreva("Você optou por sair")