"""
Preencher o array com o dobro do valor do indice da posição de cada elemento
"""
import numpy as np

NR_ELEMENTOS = 10

numeros = np.empty(NR_ELEMENTOS)

for i in range(NR_ELEMENTOS):
    numeros[i] = i * 2

print(numeros)