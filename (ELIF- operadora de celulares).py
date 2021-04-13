# Cálculo de bônus operadora de celulares

pontuacao = int(input(" Informe sua pontuação: "))
if pontuacao > 1000:
    print("Você ganhou 3gb de bônus")
elif pontuacao > 500:
    print("Você ganhou 1,5gb de bônus")
elif pontuacao > 200:
    print("Você ganhou 500mb de bônus")
else:
    print("Você não ganhou nada!!!")