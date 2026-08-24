#Faça um algoritmo para calcular quantas ferraduras são necessárias para equipar todos os cavalos comprados para um haras.

'''
cavalos = int(input("cavalos: "))

ferraduras = cavalos * 4

print("Você precisa de", ferraduras, "ferraduras.")
'''

#Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida ela possui.
#Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma
#pessoa com 19 anos possui 6935 dias de vida; veja um exemplo de saída:
#MARIA, VOCÊ JÁ VIVEU 6935 DIAS.

'''
nome = (input("Qual é seu nome: "))
idade = int(input("Idade: "))

Dias = idade * 365

print("Olá", nome, "você tem", Dias, "de vida.")
'''

#A padaria Hotpão vende uma certa quantidade de pães franceses e uma
#quantidade de broas a cada dia. Cada pãozinho custa R$ 0,12 e a broa custa R$
#1,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães
#e broas (juntos), e quanto deve guardar numa conta de poupança (10% do total
#arrecadado). Você foi contratado para fazer os cálculos para o dono. Com base
#nestes fatos, faça um algoritmo para ler as quantidades de pães e de broas, e
#depois calcular os dados solicitados.

'''
broas = int(input("Quantidade de broas vendidas: "))
paozinhos = int(input("Quantidade de pãozinhos vendidos: "))

valbroas = broas * 1.50
valpaozinhos = paozinhos * 0.12

faturamento = valbroas + valpaozinhos
 
print("Você faturou", faturamento, "reais")

print("Poupança", faturamento * 0.1, "reais")
'''

#O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição.
#Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos)
#e imprima o valor a pagar. Assuma que a balança já desconte o peso do prato.

'''
peso = float(input("Peso do prato em Kg: "))

quilo = float(12.00)

valor = peso * quilo

print("Valor do prato:", valor)
'''

#Entrar com o dia e o mês de uma data e informar quantos dias se passaram
#desde o início do ano.
#Esqueça a questão dos anos bissextos e considere sempre que um mês possui
#30 dias.

'''
dia = int(input("Qual é o dia: "))
mes = int(input("Qual é o mês: "))

mesdia = (mes - 1) * 30

print("Já se passaram", mesdia + dia, "dias desde o inicio do ano.")
'''

#Alguns paises medem temperaturas em graus celsius, e outros em graus fahrenheit, 
#faça um algoritmo para ler uma temperatura Celsius e imprimi-la em fahrenheit 
#(pesquise como fazer este tipo de converção)

'''
celsius = float(input("Quantos graus celsius esta hoje: "))

fahrenheit = celsius * 9/5 + 32 

print("A temperatura atual em fahrenheit é:", fahrenheit, "°F.")
'''

#A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00
#por hora extra. Faça um algoritmo para calcular e imprimir o salário bruto e o
#salário líquido de um determinado funcionário. Considere que o salário líquido é
#igual ao salário bruto descontando-se 10% de impostos.

'''
hn = 10.00
he = 15.00

normal = float(input("Quantas horas de trabalho em hora normal você fez esse mês: "))
extra = float(input("Quantas horas de trabalho em hora extra você fez esse mês: "))

n1 = float(hn * normal)
e1 = float(he * extra)

salariob = n1 + e1 
salariol = salariob * 0.9

print("Seu salario bruto é de", salariob, "reais e o seu salario liquido é de", salariol, "reais.")
'''

#A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: lata de
#350 ml, garrafa de 600 ml e garrafa de 2 litros. Se um comerciante compra uma
#determinada quantidade de cada formato, faça um algoritmo para calcular
#quantos litros de refrigerante ele comprou.

'''
lata = float(input("Quantas latas de 350ml você comprou? "))
garrfa1 = float(input("Quantas garrafas de 600ml você comprou? "))
garrafa2 = float(input("Quantas garrafas de 2L você comprou? "))

l1 = lata * 350 / 1000
g1 = garrfa1 * 600 / 1000
g2 = garrafa2 * 2

print("Você comprou cerca de", l1 + g1 + g2, "litros de refri")
'''

#Três amigos, Carlos, André e Felipe. decidiram rachar igualmente a conta de
#um bar.
#Faça um algoritmo para ler o valor total da conta e imprimir quanto cada um
#deve pagar, mas faça com que Carlos e André não paguem centavos. Ex:
#uma conta de R$101,53 resulta em R$33,00 para Carlos, R$33,00 para
#André e R$35,53 para Felipe.

'''
conta = float(input("Qual é o valor total da conta? ")) 

c = conta // 3
a = conta // 3
f = conta - c - a

print("Carlos e André teram que pagar", c, "reais cada e Felipe ira pagar", f, "reais." )
'''