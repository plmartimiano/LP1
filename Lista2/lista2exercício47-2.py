num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 > num2:
    if num1 > num3:
        print("O maior número é:", num1)
    else:
        print("O maior número é:", num3)
else:
    if num2 > num3:
        print("O maior número é:", num2)
    else:
        print("O maior número é:", num3)