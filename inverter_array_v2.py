"""Programa para inverter os elementos de um array com 5 nomes"""
import numpy as np

NR_ELEMENTOS = 5

nomes = np.empty(NR_ELEMENTOS,dtype="U20")

for i in range(NR_ELEMENTOS):
    nomes[i] = input(f"Introduza o nome: ")

#preencher o array invertendo as posições
k = NR_ELEMENTOS - 1
for i in range(NR_ELEMENTOS // 2):
    temp     = nomes[i]
    nomes[i] = nomes[k]
    nomes[k] = temp
    k = k - 1

#mostrar os dois array
print(nomes)