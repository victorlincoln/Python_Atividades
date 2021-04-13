# Exercício 1, cap.2, Fiap
# Cálculo IMC

peso = float(input("Digite seu peso em Kg: "))
altura= float(input("Digite sua altura em metros: "))
imc = peso / (altura * altura)
print("O seu imc é {:.2f}".format(imc))

if imc < 16.0:
    print("O usuário está na categoria: Baixo peso Grau III")
elif 16 < imc < 16.99:
    print("O usuário está na categoria: Baixo peso Grau II")
elif 17 < imc < 18.49:
    print("O usuário está na categoria: Baixo peso Grau I")
elif 18.50 < imc < 24.99:
    print("O usuário está na categoria: Peso ideal")
elif 25.00 < imc < 29.99:
    print("O usuário está na categoria: Sobrepeso")
elif 30.00 < imc < 34.99:
    print("O usuário está na categoria: Obesidade Grau I")
elif 35.00 < imc < 39.99:
    print("O usuário está na categoria: Obesidade Grau II")
else:
    print("O usuário está na categoria: Obesidade Grau III")

