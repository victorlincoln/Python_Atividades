# 3 – Os alunos da sua turma fizeram uma votação para escolher
# qual dia da semana é o melhor para a realização das lives.
# Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana
# (segunda-feira,
# terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.

print("Qual melhor dia da semana para realização das Lives ?")
segunda = int(input(" Digite a quantidade de votos recebidos para segunda-feira: "))
terca = int(input("Digite a quantidade de votos recebidos para terça-feira: "))
quarta = int(input("Digite a quantidade de votos recebidos para quarta-feira: "))
quinta = int(input("Digite a quantidade de votos recebidos para quinta-feira: "))
sexta = int(input("Digite a quantidade de votos recebidos para sexta-feira: "))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    resultado: str = ("segunda-feira")

elif terca > quarta and terca > quinta and terca > sexta and terca > segunda:
    resultado: str = ("terça-feira")

elif quarta > quinta and quarta > sexta and quarta > segunda and quarta > terca:
    resultado: str = ("quarta-feira")

elif quinta > quarta and quinta > sexta and quinta > segunda and quinta > terca:
    resultado: str = ("quinta-feira")

elif sexta > quinta and sexta > quarta and sexta > segunda and sexta > terca:
    resultado: str = ("sexta-feira")



else:
    print("Não foi possível chegar a um consenso, refaça a votação !!!")

print(f"O dia mais votado foi: {resultado}")
