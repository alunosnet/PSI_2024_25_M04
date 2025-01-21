texto = " olá mundo"

tamanho = len(texto)
print(tamanho)
texto = texto.upper()   #devolve a string em maiusculas
print(texto)
texto = texto.lower()   #devolve a string em minusculas
print(texto)
texto = texto.capitalize() #devolve a string com a primeira em M
print(texto)
texto =  texto.strip() #devolve a string sem espaços em branco no inicio e no final
print(texto)
texto = texto.replace(" ","-") #devolve a string substituindo o primeiro parametro pelo segundo (" " por "-")
print(texto)
print(texto.isdigit()) #devolve verdadeiro se todos as letras sem digitos (números)
frase="Olá mundo, o computador é uma torradeira"
palavras = frase.split(" ")  #devolve uma lista com as partes da string separadas por carater indicado " "
print(palavras)
print(len(palavras))
print(palavras[1])
posicao = frase.index("m")  #devolve a posição da string mas se não existir dá erro
print(posicao)
posicao = frase.find("m") #devolve a posição da string se não encontrar devolve -1
if posicao == -1:
    print("Não encontrei")
else:
    print("Encontrei na posição "+str(posicao))

#código ascii de uma letra
codigo = ord('a')
print(codigo)
#devolve a letra correspondente ao código ASCII
letra = chr(97)