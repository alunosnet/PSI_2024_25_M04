"""
Um programa para registar os nomes dos clientes que entraram numa loja num determinado dia e o valor das compras de cada.
O programa deve mostrar o nome do cliente que fez a compra mais cara.
"""
import numpy as np

MAX_CLIENTES = 10
#perguntar quantos clientes entraram
MAX_CLIENTES = int(input("Quantos clientes entraram na loja?"))

nomes   = np.empty(MAX_CLIENTES,dtype="U50")
compras = np.empty(MAX_CLIENTES,dtype="f")

#array passado por referência
def LerDados(nomes_clientes,compras_clientes):
    for i in range(MAX_CLIENTES):
        #ler nome
        nomes_clientes[i] = input("Nome: ")
        #ler valor compras
        compras_clientes[i] = input("Valor das compras: ")

#função para mostrar o nome do melhor cliente
def MelhorCliente(nomes_clientes,compras_clientes):
    #maior_compra=compras_clientes[0]
    posicao = 0
    #percorrer o array
    for i in range(MAX_CLIENTES):
        if compras_clientes[posicao] < compras_clientes[i]:
            #guardar o maior valor e a posição
            #maior_compra = compras_clientes[i]
            posicao = i
    print(f"O melhor cliente foi {nomes_clientes[posicao]} que gastou {compras_clientes[posicao]}")

LerDados(nomes,compras)
MelhorCliente(nomes,compras)