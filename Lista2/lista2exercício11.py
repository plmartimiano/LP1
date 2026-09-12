numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: ")) 
numero_3 = int(input("Digite o terceiro número: "))
if numero_1 == numero_2 and numero_1 == numero_3:
    print("Os três números são iguais.")
if numero_1 == numero_2 and numero_1 != numero_3:
    print("O primeiro e o segundo número são iguais.")
if numero_1 != numero_2 and numero_1 == numero_3:
    print("O primeiro e o terceiro número são iguais.")
if numero_1 != numero_2 and numero_1 != numero_3 and numero_2 == numero_3:
    print("O segundo e o terceiro número são iguais.")
if numero_1 != numero_2 and numero_1 != numero_3 and numero_2 != numero_3: 
    print("Os três números são diferentes.")