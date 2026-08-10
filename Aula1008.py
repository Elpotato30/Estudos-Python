'''
#saida de dados
print ("hello world\n 'bem vindo'")
Exercicio 1
Meu primeiro programa
'''

'''
#variaveis 
nome = "pedro"

#int - integer - nº inteiro
idade = 20 

#float - nº reais
altura = 1.77 

print(nome)
print(idade)
print(altura)

print(nome, "tem", idade, "anos e mede", altura, ".")
'''

'''
#tipagem dinamica
exemplo = "Um" #string
print(exemplo)
print(type(exemplo))

exemplo = 1 #int
print(exemplo)
print(type(exemplo))

exemplo = 1.1 #float
print(exemplo)
print(type(exemplo))
'''

nome = input("Informe seu nome completo: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura: "))

print(type(nome))
print(type(idade))
print(type(altura))

print(nome, "tem", idade, "anos e mede", altura, ".")