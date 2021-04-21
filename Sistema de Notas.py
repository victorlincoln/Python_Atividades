# Sistema de notas
notas = []
opcao = -1

while opcao != 3:
    print("1 - Informar as notas \n 2 - Exibir notas \n  3 - Calcular a média")
    opcao = int(input("Escolha sua opção: "))
    if opcao ==1:
        notas.append(float(input("Digite a nota :")))
    elif opcao ==2:
        #Para x assumir cada valor da lista de notas
        for x in notas:
            print(x)
    elif opcao ==3:
        #Para calcular a soma das notas da lista, método (sum) de soma e (len) tamanho da lista
        print(sum(notas) / len(notas))
