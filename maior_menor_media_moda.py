"""
Programa para ler temperatura média mensal de uma cidade ao longo de um ano. O programa deve mostrar a média, a menor, a maior, a moda e os meses em que a temperatura foi superior à média.
Utilize valores inteiros.
"""
import numpy as np

NR_MESES = 12
#declaração do array
temperaturas = np.zeros(NR_MESES)
#leitura das temperaturasa para o array
for mes in range(NR_MESES):
    temperaturas[mes] = int(input(f"Introduza a temperatura média do mês {mes+1}: "))
#maior e a menor temperatura
maior = temperaturas[0]
menor = temperaturas[0]
for mes in range(1,NR_MESES):
    if temperaturas[mes] > maior:
        maior = temperaturas[mes]
    if temperaturas[mes] < menor:
        menor = temperaturas[mes]
print(f"A temperatura mais elevada foi de {maior} e a menor temperatura foi de {menor}.")
#média
soma = 0
for t in temperaturas:
    soma = soma + t
media = soma / NR_MESES
print(f"A temperatura média anual foi de {media}")
#mostrar meses com temperatura superior à média
for mes in range(NR_MESES):
    if temperaturas[mes] > media:
        print(f"A temperatura do mês {mes+1} foi de {temperaturas[mes]} sendo superior à média.")
#moda
moda = 0
nr_vezes_moda = 0
for mes in range(NR_MESES):
    conta = 0
    for m_atual in range(NR_MESES):
        if temperaturas[mes] == temperaturas[m_atual]:
            conta = conta + 1
    if conta > nr_vezes_moda:   #se o conta é superior ao nr_vezes_moda este passa a ser a moda
        nr_vezes_moda = conta #nr de vezes que a temperatura da posicao mes aparece
        moda = mes             #a posicao da temperatura contada
print(f"A moda é a temperatura {temperaturas[moda]} que ocorreu {nr_vezes_moda} vezes")