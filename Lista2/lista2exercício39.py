peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura **2)
print("Seu IMC é: ", imc)
if imc < 18.5:
     print("Abaixo do Peso")
elif imc < 25:
     print("Peso Normal")
elif imc < 30:
     print("Sobrepeso")
elif imc >= 30:
    print("Obseidade")  