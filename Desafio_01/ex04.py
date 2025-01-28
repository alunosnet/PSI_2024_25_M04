
def Contar(nomes,nome):
    contar_repetidos=0
    for v in nomes:
        if v == nome:
            contar_repetidos = contar_repetidos + 1
    return contar_repetidos

def ContarV2(nomes,nome):
    contar_repetidos=0
    for p in range(len(nomes)):
        if nomes[p] == nome:
            contar_repetidos = contar_repetidos + 1
    return contar_repetidos