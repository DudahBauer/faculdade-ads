#idade = int(input("Qual a sua idade?"))
#dano = input("Qual o valor do seu dano?")
#escudo= input("Qual o valor do seu escudo?")


#if idade > 60:
    #print("Vc tem direito aos beneficios")

#if dano > 10 and escudo == 0:
    #print("Você está morto")

# ano= int(input("Digite um  ano:"))
# if ano % 4 == 0:
#     print(f"O ano {ano} é um ano bissexto!!")
# else:
#     print(f"O {ano} não é um ano bissexto!")


# escreva um algoritmo que pede 2 números ao usuário e da a possibilidade dele escolher qual operação deseja realizar

n1= int(input("Digite o primeiro número:"))
n2= int(input("Digite o segundo número"))

operacao= int(input("Escolha a operação que você deseja realizar:\n" \
"1- Soma \n" \
"2- Subtração\n" \
"3- Multiplicação\n" \
"4- Divisão\n"))

if operacao == 1:
    print(f"A soma de {n1} + {n2} é de: {n1 + n2:.2f}")
elif operacao == 2:
    print(f"A subtração de {n1} - {n2} é de: {n1 - n2:.2f}")
elif operacao == 3:
    print(f"A multiplicação de {n1} X {n2} é de {n1 * n2:.2f}")
else:
    print(f"A divisão de {n1} por {n2} é de: {n1//n2:.2f}")
