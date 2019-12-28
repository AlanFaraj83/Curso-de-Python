"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média do aluno
"""
"""
Meu programa
"""
aluno = input("Digite o nome do aluno:")
nota1 = int(input("Digite a primeira nota:"))
nota2 = int(input("Digite a segunda nota:"))
nota3 = int(input("Digite a terceira nota:"))
nota4 = int(input("Digite a quarta nota:"))

media = (nota1 + nota2 + nota3 + nota4)/4
print("A média do aluno",aluno,"é:",media)


"""
Programa do Professor
"""
soma = int(input("Digite a primeira nota: "))
soma = soma + int(input("Digite a segunda nota: "))
soma = soma + int(input("Digite a terceira nota: "))
soma = soma + int(input("Digite a quarta nota: "))
soma = soma/4 #queremos um numero real
print("A média do aluno foi", soma)
