ano = input("Digite um ano: ")
if (int(ano) % 4 == 0 and int(ano) % 100 != 0) or (int(ano) % 400 == 0):
    print("O ano é bissexto?: True")
else:
    print("O ano é bissexto: False")