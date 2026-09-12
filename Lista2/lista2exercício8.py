nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
if idade >= 18 and salario > 1000:
    print(nome, "você é maior de idade e seu salário é maior que R$ 1000, ")