#2 – Olhando para o mercado de educação infantil, você e sua equipe decidem criar um aplicativo
# onde as crianças aprendam a controlar os seus gastos.

#Como forma de validar um protótipo, foi solicitado que você crie um script simples, em que o usuário 
#deve informar QUANTAS TRANSAÇÕES financeiras realizou ao longo de um dia e, na sequência, deve informar o 
#VALOR DE CADA UMA das transações que realizou.

#Seu programa deverá exibir, ao final, o valor total gasto pelo usuário e também a média do valor de cada transação.

gastos = int(input("Quantas transações foram efetuadas no dia? "))

# Todos os valores digitados
valor = []

for x in range(gastos):
    valor.append(float(input("Qual valor de cada uma das transações? ")))

# Calcula a soma dos valores
soma = 0
for x in valor:
    soma = soma + x



# Calcula a media dos valores
media = soma / gastos
print( f"O valor gasto foi de: R${soma} e a média do valor de cada transição foi :  R${media}")

