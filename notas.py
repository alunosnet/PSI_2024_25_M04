"""
Programa para ler as notas de 10 alunos, calcular e mostrar a média das notas e por fim mostrar as notas que são superiores à média
"""
import numpy as np

#constante com o valor do nº de alunos
NR_ALUNOS = 10

#definir o array para as notas
notas = np.zeros(NR_ALUNOS)

#ler as notas
for n in range(NR_ALUNOS):
    notas[n] = int(input(f"Introduza a nota do aluno nº {n+1}: "))

#calcular a média
soma = 0
for n in range(NR_ALUNOS):
    soma = soma + notas[n]

media = soma / NR_ALUNOS
print(f"A média das notas dos alunos foi de {media}")

#listar as notas que são superiores à média
for n in range(NR_ALUNOS):
    if notas[n] > media:
        print(f"A nota de {notas[n]} do aluno nº {n+1} é superior à média")