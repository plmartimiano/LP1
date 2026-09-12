temperatura =  float(input("Qual a Temperatura? "))
umidade = int(input("Qual a umidade do ar? "))
if temperatura >30:
    if umidade <30:
        print("Alerta de Incêndio")
    else:
        print("Calor, mas sem risco de incêndio")
else:
        print("Calor, mas sem risco de incêndio")