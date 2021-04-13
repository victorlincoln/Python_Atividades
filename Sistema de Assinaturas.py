# Exercício 2, cap.2 Fiap
#Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente,
# o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês.
#O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem
#sobre o faturamento que o canal do cliente obteve ao longo do ano.


print("Pacotes de assinaturas: " " Basic,  Silver,  Gold, Platinum")
var = input("Digite qual tipo de sua assinatura: ")
assinatura = var.upper()
print(assinatura)
faturamento = float(input("Quanto foi seu faturamento anual? "))

if assinatura == "BASIC":
    bonus = faturamento * 0.3
    print(f"O valor do bônus a ser pago é de R${bonus}")

elif assinatura == "SILVER":
    bonus = faturamento * 0.2
    print(f"O valor do bônus a ser pago é de R${bonus}")

elif assinatura == "GOLD":
    bonus = faturamento * 0.1
    print(f"O valor do bônus a ser pago é de R${bonus}")

elif assinatura == "PLATINUM":
    bonus = faturamento * 0.05
    print(f"O valor do bônus a ser pago é de R${bonus}")

else:
    print("Erro")


