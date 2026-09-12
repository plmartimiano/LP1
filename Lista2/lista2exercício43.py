valor = float(input("Qual valor da sua compra? R$ "))
if valor < 50:
    print("Sem desconto. Você pagará o valor de R$", float(valor))
elif valor >= 50 and valor < 200:
    print("5'%' de desconto. Você pagará o valor de R$", float(valor - (valor * 0.05)))
elif valor >= 200 and valor < 500:
     print("10'%' de desconto. Você pagará o valor de R$", float(valor - (valor * 0.10)))
elif valor >= 500:
    print("15'%' de desconto. Você pagará o valor de R$", float(valor - (valor * 0.15)))