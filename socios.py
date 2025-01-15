import numpy as np

socios_A = np.array(["joaquim","maria","joão","luís","carla"])
socios_B = np.array(["maria","antónio","carla"])

#listar os sócios que pertence aos dois clubes
contar = 0
for nome_A in socios_A:
    for nome_B in socios_B:
        if nome_A == nome_B:
            print(f"O sócio com o nome {nome_A} pertence aos dois clubes")
#versão 2
for nome_A in socios_A:
    if nome_A in socios_B:
            print(f"O sócio com o nome {nome_A} pertence aos dois clubes")
