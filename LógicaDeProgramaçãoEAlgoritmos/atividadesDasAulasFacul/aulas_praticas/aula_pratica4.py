# # realize a sequência de print com for e while
# a) inteiros 3 até 12, com 12 incluso
# b) Inteiros de 0 até 9, excluindo 9, com passo 2
# print("- - - -Exercicio A com for:- - - -\n")
# for i in range(3,13, 1):
#     print(i)

# print("- - - -Exercicio A com while:- - - -\n")
# i=3
# while i <= 12:
#     print(i)
#     x+=1

# print("- - - -Exercicio B com for:- - - -\n")
# for i in range(0,9,2):
#     print(i)

# print("- - - -Exercicio B com while:- - - -\n")

# i=0
# while (i <=8):
#     print(i)
#     i += 2

# mostre na tela opções de produtos para comprar. Coxinha = 5, Pastel= 7, Café= 4, Suco= 6
# PRECO_COXINHA=10
# PRECO_PASTEL=7
# PRECO_CAFE=4
# PRECO_SUCO=6

# OPCAO_COXINHA=1
# OPCAO_PASTEL=2
# OPCAO_CAFE=3
# OPCAO_SUCO=4


# OPCAOES_VALIDAS= [
#     OPCAO_COXINHA,
#     OPCAO_PASTEL,
#     OPCAO_CAFE,
#     OPCAO_SUCO
# ]

# while True:
#     print("- - - - -BEM VINDO(A) A LANCHONETE DA DUDINHA- - - - -\n")
#     opcao= int(input("- - - -Escolha uma opção do MENU:- - - - \n" \
#     f"{OPCAO_COXINHA}- Coxinha: {PRECO_COXINHA} reais\n" \
#     f"{OPCAO_PASTEL}- Pastel: {PRECO_PASTEL} reais\n" \
#     f"{OPCAO_CAFE}- Café: {PRECO_CAFE} reais\n" \
#     f"{OPCAO_SUCO}- Suco: {PRECO_SUCO} reais\n" \
#     f"5- Sair"))
#     if opcao not in OPCAOES_VALIDAS:
#         print("A opção que você escolheu é inválida, digite uma opção válida")
#         continue
#     break

# #n entendi o pq não posso apenas colocar tipo: valor= quantidade*5
# while True:
#     valor=0
#     quantidade= int(input("Digite a quantidade que deseja do item escolhido:"))
#     if opcao== OPCAO_COXINHA:
#         valor+=quantidade*PRECO_COXINHA
#         break
#     elif opcao==OPCAO_PASTEL:
#         valor+=quantidade*PRECO_PASTEL
#         break
#     elif opcao==OPCAO_CAFE:
#         valor+=quantidade*PRECO_CAFE
#         break
#     elif opcao==OPCAO_SUCO:
#         valor+=quantidade*PRECO_SUCO
#         break
#     else:
#         print("A opção que você escolheu é inválida, digite uma opção válida")


# # valor dependa da do item, do preco e da quantidade
# # o valor de um pedido é igual a opcao que a pessoa escolheu X a quantidade X o preco
# print(f"O valor do seu pedido ficou de {valor} reais")

# #1valor_total= opcao*quantidade*preco

#Crie um algoritmo que leia um valor e imprima em quantidade de cédulas necessárias para pagar esse mesmo valor, Com cédulas de 100, 50, 20, 10, 5 e 1

# usuariozin me da um valor, eu pego o valor e divido por 100, se tiver resto 0, dou a quantidade de cédulas que deu a divisão em notas de 100. se tiver resto, pego o resto e divido por 10

# valor=int(input("Escreva um valor inteiro que você deseja sacar:"))
# valorInicial=valor

# # if valor>100:
# #     if valor/100 == 0:
# #         quantidadeDeCedulas= valor/100
# #         print(f"Você vai recebr o {valor} em {quantidadeDeCedulas} cédulas de 100.")


# # #se o valor for maior que 100, mas tiver resto, pegar o resto e dividir por 10, se não tiver resto, dar as notas.
# #     elif valor>100:
# #         if valor/10==0:
# #             quantidadeDeCedulas= valor/10
# #             print(f"Você vai recebr o {valor} em {quantidadeDeCedulas} cédulas de 100.")
# #         elif valor//100 == resto:
# #             if resto//10:
# #                 rest0= valor%10
# #                 quantidadeDeCedulas= valor/10
# #                 print(f"Você vai recebr o {valor} em {quantidadeDeCedulas} cédulas de 100.")

# #     quantidadeDeCedulas=
# contadorDe100=0
# while valor>=100:
#     valor= valor-100
#     contadorDe100= contadorDe100+1

# contadorDe50=0
# while valor>=50:
#     valor= valor-50
#     contadorDe50= contadorDe50+1

# contadorDe20=0
# while valor>=20:
#     valor=valor-20
#     contadorDe20= contadorDe20+1

# contadorDe10=0
# while valor>10:
#     valor=valor-10
#     contadorDe10= contadorDe10+1

# contadorDe5=0
# while valor>=5:
#     valor=valor-5
#     contadorDe5= contadorDe5+1

# contadorDe1=0
# while valor>=1:
#     valor=valor-1
#     contadorDe1= contadorDe1+1



# print(f"O valor que você deseja sacar é: {valorInicial}, você irá receber esse valor em {contadorDe100} notas de 100 \n")
# print(f"O valor que você deseja sacar é: {valorInicial}, você ira receber esse valor em {contadorDe50} notas de 50 \n")
# print(f"O valor que você deseja sacar é: {valorInicial}, você ira receber esse valor em {contadorDe20} notas de 20\n")
# print(f"O valor que você deseja sacar é: {valorInicial}, você ira receber esse valor em {contadorDe10} notas de 10\n")
# print(f"O valor que você deseja sacar é: {valorInicial}, você ira receber esse valor em {contadorDe5} notas de 5 \n")
# print(f"O valor que você deseja sacar é: {valorInicial}, você ira receber esse valor em {contadorDe1} notas de 1 \n")


#cinema cobra diferentes valores, se a pessoa tiver menos de 3 anos, é de grátis, se tiver entre 3 e 12 é 15 e se tiver mais de 12 é 30

# quantidade de pessoas q vão no cinema, a idade de cada uma, a soma dos valores e o valor final

print("- - - - - BEM-VINDO(A) AO CINEMA DA DUDINHA  - - - - -\n")
quantidadeDeIngressos= int(input("Digite a quantide de ingressos que você deseja comprar"))

idades= []

for i in range(quantidadeDeIngressos):
   idade= int(input(f"Digite a idade da pessoa:"))
   idades.append(idade)

somaDasIdades=0
valorDoIngresso=0
for idade in idades:
    if idade < 3:
        print("O seu ingreço é de graça!!")
        valorDoIngresso= valorDoIngresso+0
        somaDasIdades=somaDasIdades+idade

    elif idade >= 3 and idade <= 12:
        valorDoIngresso= valorDoIngresso+15
        somaDasIdades=somaDasIdades+idade

    elif idade > 12:
        valorDoIngresso= valorDoIngresso+30
        somaDasIdades=somaDasIdades+idade

#media é a soma de coisas divida pela quantidade. quantiade de ingressos*idade/idades
media= somaDasIdades/quantidadeDeIngressos


print(f"A quantidade de pessoas que compraram os ingressos é de: {quantidadeDeIngressos}")
print(f"A média de idade das pessoas é de {media}")
print(f"O valor que você deve pagar pelos ingressos é de {valorDoIngresso}")











