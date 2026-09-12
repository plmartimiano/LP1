valor_compra = input("Digite um valor da compra: ")
if float(valor_compra) > 100:
    print("Você ganhou um desconto de 10%")
    valor_desconto = float(valor_compra) * 0.10
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Valor a pagar: R$ {float(valor_compra) - valor_desconto:.2f}")
else:
    print("Você não ganhou desconto")
    valor_sem_desconto = float(valor_compra)
    print(f"Valor a pagar: R$ {valor_sem_desconto:.2f}")