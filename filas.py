"""
O Sr. Joaquim tem restaurante muito popular é precisa de ajuda a gerir a fila de espera dos clientes.
Pretende-se criar um programa para registar os nomes dos clientes em espera e de cada vez retirar o primeiro a chegar à fila (FIFO)
Menu: 1.Entrada 2.Saída 3.Consultar Fila 4.Terminar
"""
import numpy as np

NR_MAX = 4
def Entrada(fila):
    """Adicionar um nome ao final da fila de espera"""
    #procurar o ultimo lugar da fila
    encontrou=False
    for posicao in range(NR_MAX):
        if fila[posicao]=="":
            encontrou = True
            break
    #avisar se fila cheia
    if encontrou == False:
        print("Fila cheia. Volte mais tarde.")
        return
    #ler o nome
    nome = input("Indique o nome para a fila de espera: ")
    #inserir no final
    fila[posicao]=nome
    print(f"A sua posição na fila de espera é {posicao+1}º")

def Saida(fila):
    """Retirar o primeiro nome da fila de espera"""
    #verificar se a fila está vazia
    if fila[0]=="":
        print("Não tem ninguém a fila de espera.")
        return
    #retirar o primeiro nome da fila
    print(f"O cliente com o nome {fila[0]} pode entrar.")
    #avançar os restantes nomes da fila uma posição
    for i in range(NR_MAX-1):
        fila[i] = fila[i+1]
    fila[NR_MAX-1] = "" #limpar a última posição do array

def Consultar(fila):
    """Listar os nomes na fila de espera"""
    #Verificar se a fila está vazia
    if fila[0]=="":
        print("Não tem ninguém a fila de espera.")
        return
    #listar os nomes das pessoas em espera
    Fila_Cheia = True
    for posicao in range(NR_MAX):
        if fila[posicao]=="":
            Fila_Cheia = False
            break
        print(f"{posicao+1}º - {fila[posicao]}")
    #verificar se a fila está cheia
    if Fila_Cheia == True:
        print("Fila de espera está cheia.")

def main():
    fila = np.empty(NR_MAX,dtype="U20")
    #limpar array
    for i in range(NR_MAX):
        fila[i]=""
    op = 0
    while op !=4:
        op=input("1.Entrada\n2.Saída\n3.Consultar Fila\n4.Terminar")
        if op == "1":
            Entrada(fila)
        elif op=="2":
            Saida(fila)
        elif op=="3":
            Consultar(fila)
        elif op=="4":
            break
        else:
            print("Opção inválida")

if __name__=='__main__':
    main()