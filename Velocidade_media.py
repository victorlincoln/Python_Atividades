#Esse programa recebe a distância e o tempo e calcula a velocidade média
#Primeiro vamos pedir a distância e o tempo
print ("Esse é o calculador de velocidade média")
distancia = input("Digite a distância percorrida: ")
tempo = input("Digite o tempo percorrido: ")
#Realizando o cálculo:
velocidade_media = float (distancia) / float (tempo)
print("Aguarde um momento.... ")
#Exibindo a mensagem na tela:
print("A velocidade média calculada foi de {:.2f} km/h".format(velocidade_media))
