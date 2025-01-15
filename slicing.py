"""
Slicing - Permite ter acesso a subconjuntos de uma sequência ou coleção
    sintaxe : sequencia[inicio:fim:passo]
    inicio - a posição do primeiro a incluir
    fim    - é posição onde termina o slice NÃO É INCLUI
    passo  - intervalo entre os elementos a inclui no slice
"""

nome = "Joaquim Silva"
nome_5_letras = nome[0:5:1] #copia as letras das posições 0 a 4
print(nome_5_letras)
nome_5_letras = nome[:5:1] #copia as primeiras 5 letras
print(nome_5_letras)
nome_ultimas_letras = nome[7:] #copia as letras da posição 7 até ao fim
print(nome_ultimas_letras)
nome_ultimas_letras = nome[7:110] #copia as letras da posição 7 até ao fim
print(nome_ultimas_letras)
nome_invertido = nome[::-1]  #inverter a string
print(nome_invertido)
nome_2_2_letras = nome[::2]
print(nome_2_2_letras)
print(nome[-1]) #ultima letra da string
ultimo_nome_invertido = nome[-1:-6:-1]
print(ultimo_nome_invertido)
ultimo_nome_invertido = nome[:7:-1]
print(ultimo_nome_invertido)
ultimo_nome_invertido = nome[12:7:-1]
print(ultimo_nome_invertido)

import numpy as np

nomes=np.array(["joaquim","maria","antónio","augusto","césar"])
#mostrar todos os nomes por ordem inversa
print(nomes[::-1])
#mostrar os dois últimos nomes
print(nomes[len(nomes)-2:])
#mostrar o 1º,3º,5º
print(nomes[::2])