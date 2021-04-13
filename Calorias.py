# 1 – O projeto HealthTrack está tomando forma e podemos pensar em algoritmos que possam ser reaproveitados
# quando estivermos implementando o front e o back do nosso sistema. Uma das funções mais procuradas por
# usuários de aplicativos de saúde é o de controle de calorias ingeridas em um dia. Por essa razão,
# você deve elaborar um algoritmo implementado em Python em que o usuário informe quantos alimentos
# consumiu naquele dia e depois possa informar o número de calorias de cada um dos alimentos. Como não estudamos
# listas nesse capítulo você não deve se preocupar em armazenar todas as calorias digitadas,
# mas deve exibir o total de calorias no final.


alimentos = int(input("Digite quantos alimentos consumiu hoje: "))
i = 1
resultado = int(0)
print(alimentos)

while i <= alimentos:
    calorias = int(input("Digite a quantidade de calorias do alimento:  "))
    i = i + 1
    resultado = calorias + resultado
    print(calorias)

print(f"O total de calorias consumidos no dia é: {resultado}")