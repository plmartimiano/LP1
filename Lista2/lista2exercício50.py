valor = float(input("Qual o valor da compra R$ "))
pagamento = input("Qual a forma de pagamento? Dinheiro ou Cartão? ")
if pagamento == "Dinheiro":
     print("Desconto de 10%. O Total é R$ ", valor - valor * 0.10)
if pagamento == "Cartão":
     parcelas = int(input("qual número de parcelas? "))
     if parcelas > 3:
          print("Havera juros de 2% ao mês")
     if parcelas <= 3:
          print ("Parcelas sem Juros")
