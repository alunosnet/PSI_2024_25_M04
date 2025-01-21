"""Programa para ler dois nomes completos e indicar se são familiares. Dois nomes são de familiares se o último nome for igual.
Versão hacker: Dois nomes são de familiares se um dos dois últimos nomes forem iguais por qualquer ordem (ultimo=penultimo, ultimo=ultimo, penultimo=penultimmo).
"""
def Familiares(A,B) -> bool:
    """Função que devolve true se os nomes são de familiares"""
    nomesA = A.split(" ") #lista com os nomes
    nomesB = B.split(" ")   #lista com os nomes
    #Verificar se os últimos nomes são iguais
    if nomesA[len(nomesA)-1] == nomesB[len(nomesB)-1]:
        return True
    #verificar se um dos dois últimos nomes são iguais
    for i in nomesA[1:]:
        for k in nomesB[1:]:
            if i == k:
                return True
    return False

nomeA = input("Introduza um nome completo: ")
nomeB = input("Introduza um nome completo: ")
print(Familiares(nomeA,nomeB))