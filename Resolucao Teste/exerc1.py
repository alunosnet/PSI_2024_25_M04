import numpy as np

nomes = input("Nomes: ")
tempos = input("Tempos: ")

pilotos = np.array(nomes.split(", "))
voltas = np.array(tempos.split(", "))

i = 0
while i!=5:
    if int(voltas[i])<=0:
        voltas[i]=input("Tempo da volta: ")
    else:
        i = i +1

pm = 0
pp = 0
for i in range(5):
    if int(voltas[i]) < int(voltas[pm]):
        pm = i
    if int(voltas[i]) > int(voltas[pp]):
        pp = i

diferenca = int(voltas[pp]) - int(voltas[pm])
print("Primeiro: ",pilotos[pm])
print("Último: ",pilotos[pp])
print("Diferença: ",diferenca)

for i in range(5):
    print(pilotos[i],voltas[i])