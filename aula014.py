"""
while alguma coisa:
    execute isso
Acabou o ciclo     
"""
"""
n = 10
cont = 0
while cont < n:
    print(cont)
    cont = cont +1
"""      
"""
Faça um programa que peça dois numeros,base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função potência da linguagem.
"""
#O numero do expoente indica o número de vezes que a base é multiplicada
#por ela mesma.
#A potência é o numero 1 multiplicado pela base o número do expoente vezes.


base = int(input("Digite o valor da base:"))
expoente = int(input("Digite o valor do expoente:"))

cont = 0
produto = 1
while cont < expoente:
    produto = produto * base
    cont = cont + 1

print(base,"elevado a",expoente,"=",produto) 

