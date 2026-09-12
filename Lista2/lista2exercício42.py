nota = float(input("Qual a sua nota? "))
faltas = int(input("Qantas faltas você teve? "))
if faltas > 15:
    print("Reprovado por faltas")
elif float(nota) >= 9:
    print("Conceito A")
elif float(nota) >= 7:
    print("Conceito B")
elif float(nota) >= 5:
    print("Conceito C")
elif float(nota)< 5:
    print("Conceito D")