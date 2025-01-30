"""Um programa que utiliza as palavras de um array para alterar a frase introduzida pelo utiliador, substituindo-as pelas palavras alternativas de outro arra"""
import numpy as np

proibidas    = np.array(["mau","pobre","infeliz","péssimo","triste"])
alternativas = np.array(["bom","rico","feliz","ótimo","feliz"])

frase = input("Introduza a frase:")

#verificar se algumas das palavras proibidas está presenta na frase
#e substituir pela palavra alternativa correspondente
for i in range(len(proibidas)):
    if proibidas[i] in frase:
        frase = frase.replace(proibidas[i],alternativas[i])

print(frase)