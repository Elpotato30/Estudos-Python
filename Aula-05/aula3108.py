"""
nome = input("Qual é o seu nome: ")
av1 = float(input("Qual é a sua nota na AV1: "))
av2 = float(input("Qual é a sua nota na AV2: "))

ma = (av1 + av2) / 2

if ma >= 7 and ma <=10: 
    print("Aprovado")
elif ma >= 4 and ma < 7:
    print("Em recuperação")
    ar = float(input("Nota da rec: "))
elif ma >= 0 and ma < 4:
    print("Reprovado")
else:
    print("Média inválida!")

print("FIM")
"""

peso = float(input("Qual é o seu peso "))
altura = float(input("Qual é a sua altura "))

imc = peso / altura ** 2 
#imc = peso / pow(altura, 2) 

if imc <18.5:
    print("abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("peso ideal")
elif imc >= 25:
    print("acima do peso")
else: imc >= 30
print("acima do peso")
