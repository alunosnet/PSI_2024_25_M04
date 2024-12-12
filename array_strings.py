import numpy as np

#definir um array para strings
"""
i - inteiros
f - reais
b - boleanos
S - strings
U - unicode string
M - datetime
"""
nomes = np.empty(10,dtype="U20") 

for i in range(len(nomes)):
    nomes[i] = input("Introduza o nome: ")
print(nomes)