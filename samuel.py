n_atletas=int(input("Quantos atletas:"))

soma = 0
altura_maior = 0
for i in range(n_atletas):
    altura = float(input("Altura:"))
    soma = soma + altura
    if i == 0:
        altura_maior = altura
    else:
        if altura > altura_maior:
            altura_maior = altura

media = soma/ n_atletas
print("Média",media)
print("Maior",altura_maior)