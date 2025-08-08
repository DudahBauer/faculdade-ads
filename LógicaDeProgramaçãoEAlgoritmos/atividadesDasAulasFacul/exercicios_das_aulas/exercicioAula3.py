#Leia dois valores inteiros e compare se o primeiro é maior que o segundo, caso seja, print na tela flando que o peimeiro é maior que o segundo.


# print("- - - - - Digite dois números positivos e inteiros e descubra qual é o maior - - - - -")
# n1= int(input("Digite o primeiro número:"))
# n2= int(input("Digite o segundo número: "))

# if n1 > n2:
#     print(f"O número primeiro número ({n1}) é maior")

# else:
#     print(f"O primeiro número que você digitou ({n1}), não é maior que o segundo número ({n2})")


#usuário escolhe se quer comprar 1-maças, 2-bananas ou 3-laranjas, deve-se pedir ao usuário a quantidade de frutas que ele deseja, maçã= 2.30, laranja= 3.60 e banana 1.85.

# fruta= int(input(" - - - - -MENU DA FRUTEIRA DA DUDINHA- - - - -\n" \
#              "Selecione uma opção:\n"
# "1- Maçã \n" \
# "2- Banana \n" \
# "3- Laranja \n"))

# if fruta == 1:
#     quantidade =int(input((f"Qual a quantidade de maçãs você deseja comprar?")))
#     valor= quantidade * 2.30
#     print(f"Você comprou {quantidade} maçãs. O valor da sua compra ficou de:{valor}")

# elif fruta == 2:
#     quantidade2 = int(input(f"Qual a quantidade de bananas você deseja comprar?"))
#     valor2= quantidade2*3.60
#     print(f"Você comprou {quantidade2} bananas.O valor da sua compra ficou de:{valor2}")

# elif fruta== 3:
#     quantidade3= int(input(f"Qual a quantidade de laranjas você deseja comprar?"))
#     valor3= quantidade3*1.85
#     print(f"Você comprou {quantidade3} laranjas. O valor da sua compra ficou de:{valor3}")
# else:
#     print("Você digitou um valor errado, por favor, insira uma opção errada, favor insira uma opção válida!!")


#Peça ao usuário um nome. Se o nome NÃO for Maria Eduarda, peça a idade dele, se for menor de 18 anos, informe que é menor de idade e se tiver mais que 100 anos, informe q essa pessoa possivelmente não existe.

nome= input("Digite seu nome:")

if nome != "Maria Eduarda":
    idade = int(input("Digite sua idade:"))
if idade < 18:
    print("Você é menor de idade!!")
elif idade > 100:
    print("Essa pessoa tem mais de 100 anos e  possivelmente não existe!!")







