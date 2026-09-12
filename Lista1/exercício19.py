nome = input ("qual é o seu nome? ")
horas_trabalhadas = input ("quantas horas você trabalha por mês? ")
valor_hora = input ("qual é o valor da sua hora de trabalho? ")
print ("Olá", nome, "você trabalha", int(horas_trabalhadas), "horas por mês, e ganha R$", float(valor_hora), "por hora, o que dá um total de R$", float(horas_trabalhadas) * float(valor_hora), "por mês.")