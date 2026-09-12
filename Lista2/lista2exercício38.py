mes = int(input("Digite um número de 1 a 12): "))
if mes == int("1"):
    print("Janeiro")
elif mes == int("2"):
    print("Fevereiro")
elif mes == int("3"):
    print("Março")
elif mes == int("4"):
    print("Abril")
elif mes == int("5"):
    print("Maio")
elif mes == int("6"):
    print("Junho")
elif mes == int("7"):
    print("Julho")
elif mes == int("8"):
    print("Agosto")
elif mes == int("9"):
    print("Setembro")
elif mes == int("10"):
    print("Outubro")
elif mes == int("11"):
    print("Novembro")
elif mes == int("12"):
    print("Dezembro")
else:
    print("Mês inválido")

if mes == int("12") or mes == int("1") or mes == int("2"):
    print("Verão")
elif mes == int("3") or mes == int("4") or mes == int("5"):
    print("Outono")
elif mes == int("6") or mes == int("7") or mes == int("8"):
    print("Inverno")
elif mes == int("9") or mes == int("10") or mes == int("11"):
    print("Primavera")