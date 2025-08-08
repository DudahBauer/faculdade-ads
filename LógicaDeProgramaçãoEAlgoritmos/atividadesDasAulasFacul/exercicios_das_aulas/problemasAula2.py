#Desenvolva um algoritmo que solicite ao usuário o preço de um produto de um percentual de desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto

produto= int(input("Digite o valor de um produto:"))
desconto= int(input("Digite o percentual de desconto que vc deseja aplicar sobre ele: "))

percentual= desconto/100
valor_a_ser_descontado= produto*percentual
desconto_final= produto - valor_a_ser_descontado

print(f"O valor do desconto é de {valor_a_ser_descontado} e o preço do produto com o desconto fica de: {desconto_final}")
