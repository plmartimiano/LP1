ano = (input("Insira um ano "))
if int(ano) % 4 == 0:
    if int(ano) % 100 == 0:
        if int(ano) % 400 == 0:
            print("Ano bissexto")
        else:
            print("Não Bissexto")
    else:
        print("Bissexto")
else:
    print("Não Bissexto")