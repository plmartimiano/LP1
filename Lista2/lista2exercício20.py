lado_a = input("Digite o valor do lado A: ")
lado_b = input("Digite o valor do lado B: ")
lado_c = input("Digite o valor do lado C: ")
if  int(lado_a) + int(lado_b) > int(lado_c) and int(lado_a) + int(lado_c) > int(lado_b) and int(lado_b) + int(lado_c) > int(lado_a):
    print("É um triângulo")
else:
    print("Não é um triângulo")