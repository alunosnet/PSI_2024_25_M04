"""Criar uma agenda que regista os nomes por ordem alfabética.
Guardar o nome e data de nascimento das pessoas ordenadas por ordem crescente do nome.
Menu: 1.Adicionar contacto 2.Listar contactos 3.Pesquisar 4.Terminar
"""
import numpy as np

NR_MAX = 10

def Adicionar(contactos,nome):
    """Recebe um arrau e o nome do contacto a inserir por ordem alfabética"""
    #verificar se está vazio o array
    if contactos[0]=="":
        contactos[0] = nome
        return
    #verificar se está cheio
    if contactos[NR_MAX-1]!="":
        print("Agenda de contactos está cheia.")
        return
    #procurar a posição do novo contacto
    for posicao in range(NR_MAX):
        if nome < contactos[posicao] or contactos[posicao]=="":
            break
    print(posicao)
    #avançar uma posição os restantes contactos
    for i in range(NR_MAX-1,posicao,-1):
        contactos[i] = contactos[i-1]
    #inserir o contacto
    contactos[posicao] = nome

def Listar(contactos):
    """Lista os nomes e datas de nascimento de todos os contactos"""
    for nome in contactos:
        if nome!="":
            partes = nome.split('-')
            print(f"nome: {partes[0]} Data Nascimento: {partes[1]}")

def Pesquisar(contactos,nome):
    """Recebe o array e o nome a pesquisar"""
    primeiro = 0
    ultimo = 0
    for t in contactos:
        if t=="":
            break
        ultimo = ultimo + 1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        valor_meio = contactos[meio]
        if nome in valor_meio:
            print(f"Contacto encontrado: {valor_meio}")
            return
        elif valor_meio < nome:
            primeiro = meio + 1
        else:
            ultimo = meio - 1
    print("O nome indicado não existe")

def main():
    contactos = np.zeros(NR_MAX,dtype="U30")
    print(contactos)
    op = 0
    while op !=4:
        op=input("1.Adicionar\n2.Listar\n3.Pesquisar\n4.Terminar")
        if op == "1":
            nome = input("Nome do contacto a adicionar:")
            data = input("Data de nascimento:")
            Adicionar(contactos,nome + "-" + data)
        elif op=="2":
            Listar(contactos)
        elif op=="3":
            nome = input("Nome a pesquisar:")
            Pesquisar(contactos,nome)
        elif op=="4":
            break
        else:
            print("Opção inválida")

if __name__=="__main__":
    main()