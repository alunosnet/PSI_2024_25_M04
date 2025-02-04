"""Um programa para simular o moedeiro de uma máquina de vending
    O programa deve ler o preço a pagar e o valor entregue e depois devolver o troco, caso exista, moeda a moeda de acordo com o stock disponível 
"""
import numpy as np

moedas=np.array([0.01,0.02,0.05,0.1,0.2,0.5,1,2])
stock=np.array([2,2,2,2,2,2,2,2])

#preço do produto
valor_pagar = float(input("Qual o valor a pagar:"))
#TODO: substituir por um ciclo para ler as moedas individuais entregues
#quantia entregue pelo cliente
valor_entregue=float(input("Qual o valor entregue:"))
#calcular o troco
troco = valor_entregue - valor_pagar
if troco==0:
    print("Volte sempre.")
else:
    moedas_a_devolver=""
    #procurar as moedas que prefazem a quantia do troco
    #TODO: testar o ChatGPT para ver se consegue
    while troco > 0:
        encontra=False
        for m in range(len(moedas)-1,-1,-1):
            #se existe a moeda e se valor a devolver é maior do que a moeda
            if moedas[m]<=troco and stock[m]>0:
                moedas_a_devolver = moedas_a_devolver + str(moedas[m]) + ","
                troco = troco - round(moedas[m],2)
                troco = round(troco,2)
                stock[m] = stock[m] - 1
                encontra=True
                break
        if encontra == False:
            print("Não existem moedas suficientes para fazer o troco")
            break
    print(f"Moedas a devolver: {moedas_a_devolver}")
    #print(moedas,stock)