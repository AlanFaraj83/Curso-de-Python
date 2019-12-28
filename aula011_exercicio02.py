"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero:"))
n3 = int(input("Digite o terceiro numero:"))

if n1 >= n2 >= n3:
    print("O",n1,"é o maior e o",n3,"é o menor")
elif n3 >= n2 >=n1:
    print("O",n3,"é o maior e o",n1,"é o menor")
elif n2 >= n1:
    print("O",n2,"é o maior")
else:
          print(n2,"é o menor")
                      
                      
                      
        
        
                
            
