"""
Programa para gerir uma agenda de contactos. Cada contacto deve ter um nome, email e telefone.
A agenda dever permitir:
1. Adicionar
2. Listar
3. Procurar
4. Apagar
5. Terminar
Utilize arrays para implementar as estruturas de dados.
"""
import numpy as np
#Estruturas de Dados
MAX_ITEMS = 3

def Adicionar(nomes,emails,telefones,nr_contactos):
    """
    Função para ler o nome, email e telefone de um contacto e adicionar aos respetivos arrays
    Função deve atualizar o nr_contactos registados ????
    """
    print("#"*30)
    print("## Adicionar contacto ##")
    print("#"*30)
    #testar se o array está cheio
    if nr_contactos == MAX_ITEMS:
        print("A agenda de contactos está cheia!")
        return nr_contactos
    nomes[nr_contactos]     = input("Nome: ")
    emails[nr_contactos]    = input("Email: ")
    telefones[nr_contactos] = input("Telefone: ")
    nr_contactos += 1
    return nr_contactos

def Listar(nomes,emails,telefones,nr_contactos):
    print("#"*60)
    print("## Listar contactos ",end="")
    print(" "*38,end="")
    print("##")
    print("#"*60)
    for i in range(nr_contactos):
        print(f"# {nomes[i]} \t {emails[i]} \t {telefones[i]} \t #")

def Procurar(nomes,emails,telefones,nr_contactos):
    print("#"*60)
    print("## Procurar contacto ",end="")
    print(" "*39,end="")
    print("##")
    print("#"*60)
    nome_procurar = input("Qual o nome do contacto: ")
    for i in range(nr_contactos):
        if nome_procurar in nomes[i]:
            print(f"# {nomes[i]} \t {emails[i]} \t {telefones[i]} \t #")

def Apagar(nomes,emails,telefones,nr_contactos):
    print("#"*60)
    print("## Apagar contacto ",end="")
    print(" "*39,end="")
    print("##")
    print("#"*60)
    nome_procurar = input("Qual o nome do contacto: ")
    for i in range(nr_contactos):
        if nome_procurar in nomes[i]:
            print(f"# {nomes[i]} \t {emails[i]} \t {telefones[i]} \t #")
            op = input("Tem a certeza que pretende apagar este contacto? (s/n)")
            if op in 'sS':
                for k in range(i,nr_contactos):
                    if k == MAX_ITEMS-1:    #evita erro de ultrapassar limtie do array
                        break
                    nomes[k] = nomes[k+1]
                    emails[k] = emails[k+1]
                    telefones[k] = telefones[k+1]
                nr_contactos -= 1
    return nr_contactos 

def Editar(nomes,emails,telefones,nr_contactos):
    """Função pesquisa um contacto pelo nome e permite alterar os dados"""
    #pedir o nome ao utilizador
    nome = input("Qual o nome do contacto a editar: ")
    #percorrer o array dos nomes 
    for i in range(nr_contactos):
        #encontra o nome permite alterar os dados
        if nome in nomes[i]:
            print(f"Dados do contacto: {nomes[i]} - {emails[i]} - {telefones[i]}")
            op = input("Pretende editar estes dados? (S/N)")
            if op.lower()!="s":
                continue
            #editar os dados
            novo_nome = input("Introduza o novo nome ou deixa em branco para não alterar:")
            novo_email = input("Introduza o novo email ou deixe em branco para não alterar:")
            novo_telefone = input("Introduza o novo telefone ou deixe em branco para não alterar:")
            if novo_nome.strip()!="":
                nomes[i]=novo_nome.strip()
            if novo_email.strip()!="":
                emails[i]=novo_email.strip()
            if novo_telefone.strip()!="":
                telefones[i]=novo_telefone.strip()

def Menu():
    nr_contactos = 0
    nomes = np.empty(MAX_ITEMS,dtype="U50")
    emails = np.empty(MAX_ITEMS,dtype="U50")
    telefones = np.empty(MAX_ITEMS,dtype="U9")
    op = 0
    while op != 6:
        print("1.Adicionar\n2.Listar\n3.Procurar\n4.Apagar\n5.Editar\n6.Terminar")
        op = int(input("Opção:"))
        if op == 1:
            nr_contactos = Adicionar(nomes,emails,telefones,nr_contactos)
        elif op == 2:
            Listar(nomes,emails,telefones,nr_contactos)
        elif op == 3:
            Procurar(nomes,emails,telefones,nr_contactos)
        elif op == 4:
            nr_contactos = Apagar(nomes,emails,telefones,nr_contactos)
        elif op == 5:
            Editar(nomes,emails,telefones,nr_contactos)
        elif op == 6:
            break
        else:
            print("Opção não existe!")

if __name__=="__main__":
    Menu()