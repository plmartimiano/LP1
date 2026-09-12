# Peça ao usuário a idade e exiba o resultado da expressão not (idade >= 18).

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if not (idade >= 18):
    print ( nome , ", você não é maior de idade.")