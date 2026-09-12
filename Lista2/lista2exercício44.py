idade = int(input("Qual a sua idade "))
sexo = input("Qual o seu sexo M/F ")
if sexo == "M" or sexo == "m":
    print("Masculino")
elif sexo == "F" or sexo == "f":
    print("Feminino")
else:
    print("Inválido")
if sexo == "M" or sexo == "m" and idade >= 18:
        print("Apto ao Serviço Militar")
 