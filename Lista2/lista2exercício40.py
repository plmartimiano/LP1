minutos = float (input ("Quantos minutos você utilizou no mês?"))
if minutos < 100:
    print (" Voce pagará o valor de R$", minutos * 0.25)
elif minutos >= 100 and minutos < 300:
    print (" Voce pagará o valor de R$", minutos * 0.20)
elif minutos >= 300 and minutos <500:
    print ("Voce pagará o valor de R$", minutos * 0.15)
elif minutos >= 50:
    print ("Voce pagará o valor de R$", minutos * 0.10)