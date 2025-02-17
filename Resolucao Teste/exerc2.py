contar = 0
email = input("Email: ")
pp    = input("PP: ")

#testar tamanho
if len(pp) >= 8:
    contar = contar + 1

#testar pp no email
if pp not in email:
    contar = contar + 1

#testar minusculas
for l in pp:
    if l>='a' and l<='z':
        contar = contar + 1
        break

#testar maiusculas
for l in pp:
    if l>='A' and l<='Z':
        contar = contar + 1
        break

#testar nº
for l in pp:
    if l>='0' and l<='9':
        contar = contar +1
        break

if contar == 5:
    print("Senha segura")
else:
    print("Senha não segura")