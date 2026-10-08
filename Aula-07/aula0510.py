'''
somaMult = 0
inicial = int(input("Qual é o valor inicial: "))
final = int(input("Informe o valor final: "))
if inicial < final:
    for i in range(inicial, final + 1):
        if i % 3 == 0:
            somaMult = somaMult + i
elif inicial > final:
    for i in range(100, 50 - 1, -1):
        if i % 3 == 0:
            somaMult = somaMult + i

print(somaMult)
'''

'''
n1 = int(input("Qual é a tabuada desejada: "))
resultado = None

for i in range(1, 11):
    resultado = n1 * i
    #print(n1, "x", i, "=", resultado)
    print(f"{n1}0 x {i} = {resultado}")
'''

'''
NomeCompleto = input("Informe seu nome: ")
contChar = 0

for c in NomeCompleto:
    if c != " ":
        contChar = contChar + 1
print(contChar)
'''

nome = input("Qual é o seu nome: ")
primeironome = ""
for c in nome:
    if c != " ":
        print(c)

        primeironome = primeironome + c
    elif c == " ":
        break

print(primeironome)