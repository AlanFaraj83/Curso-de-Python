nome = input("Digite seu nome:")
idade = int(input("Digite a sua idade:"))


if idade >= 18:
    print("Você pode beber a vontade")
    if idade >= 21:
        print("E você é cliente Vip.")
        

else:
    print ("Você só pode beber bebidas não alcoolizadas")

