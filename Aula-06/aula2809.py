"""
#from time import *
from time import sleep

cR = 5

#para cada var i na sequencia que inicia em 1 e vai até 5
for i in range(1,  6):
    print(cR)
    cR = cR - 1 #cr -=1
    sleep(1)

print("feliz ano novo")
"""

"""
for i in range(1, 6, 2):
    print(i)
"""

"""
for i in range(10, 0, -1):
    print(i)
"""

"""
somaPar = 0
somaImpar = 0
somaMult3 = 0 
for i in range(1, 11):
    if i % 2 == 0: #Par
        somaPar = somaPar + i
    else: #elif i % 2 == 1: #Impar
        somaImpar = somaImpar + i

    if i % 3 == 0: #multiplos de 3
        somaMult3 = somaMult3 + i

print(somaPar)
print(somaImpar)
print(somaMult3)
"""

num = int(input("Informe um número de 1 a 10: "))
somamult = 0

for i in range(1,11):
    if i % num == 0:
        somamult = somamult + 1
    
print(somamult)
