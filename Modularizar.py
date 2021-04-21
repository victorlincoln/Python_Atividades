# Programa que realiza diversos cálculos, para isso criamos várias funções
#Separar em arquivos diferentes
# Para que um scrip consiga enxergar o outro, utilizamos o comando (import)
# Dois ou mais arquivos que estão na mesma página, se enxeguem, um podendo acessar o conteúdo do outro
from calculadora import *

# Este código está fora da função

op = -1
while op!=5:
    print("1 - Somar dois valores ")
    print("2 - Subtrair dois valores ")
    print("3 - Dividir dois valores ")
    print("4 - Multiplicar dois valores ")
    print("5 - Sair ")
    op = int(input("Digite sua opção! "))
    if (op == 1):
        print(somar(float(input("Digite o primeiro valor")) , float(input("Digite o segundo valor"))))
    elif (op == 2):
        print(subtrair(float(input("Digite o primeiro valor")) , float(input("Digite o segundo valor"))))
    elif (op == 3):
        print(dividir(float(input("Digite o primeiro valor")), float(input("Digite o segundo valor"))))
    elif (op == 4):
        print(multiplicar(float(input("Digite o primeiro valor")), float(input("Digite o segundo valor"))))