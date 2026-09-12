nota_1 = float(input("Qual a nota da avaliação 1? "))
nota_2 = float(input("Qual a nota da avaliação 2? "))
frequencia = int(input("Qual a sua frequência ('%')? "))
if nota_1 + nota_2 / 2 >= 6:
    print("Aprovado por Nota")
else:
    print("Reprovado por Nota")
if frequencia < 75:
    print("Reprovado por Falta")

    