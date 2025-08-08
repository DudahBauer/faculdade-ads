#escreva uma função que calcule o fatorial de um número recebido como parãmetro e retorne o seu resultado
#Por meio de outra função faça a validação de dados permitindo que somente valores positivos sejam aceitos

# def fatorial (num):
#     fat = 1
#     if num == 0:
#         return fat
# #essa parte só executa se o num > 0
#     for i in range (1, num + 1 , 1):
#         fat*= i
#     return fat

# def validar(pergunnta, min, max):
#     x= int(input(pergunta))

#     while x< min or x > max:
#        x= int(input(pergunta))
#     return x

# x = validar("Insira um número para calcular o fatorial dele:", 0, 99999)
# print(f"{x}! = {fatorial(x)}")
def mostrarMenu():
    return int(input("- - - - -MENU- - - - -\n" \
    "1- Cadastrar novo item \n" \
     #ela tem q armazenar e mostrar os dados da opção de cadastro, como faço isso, eu n seiii
    "2- Listar tudo cadastrado\n " \
    "3- Sair"))

def cadastrarJogo():
    return input("Digite o jogo que você deseja cadastrar: ")

def mostrarJogos():
    return print(f"Os jogos\consoles cadastrados até agora são: {jogos}")

def sairDoPrograma():
    return  print("Voce escolheu a opcao sair, o programa sera fechado")


OPCAO_CADASTRO=1
OPCAO_LISTAR=2
OPCAO_SAIR=3

OPCOES_VALIAS=[
    OPCAO_CADASTRO,
    OPCAO_LISTAR,
    OPCAO_SAIR
]


jogos= [

]

while True:
    opcao= mostrarMenu()

    if opcao  == OPCAO_CADASTRO:
        nomeDoJogo= cadastrarJogo
        jogos.append(nomeDoJogo)

    elif opcao == OPCAO_LISTAR :
        mostrarJogos()

    elif opcao not in OPCOES_VALIAS:
        print("Digite uma opção válida")

    elif opcao == OPCAO_SAIR:
        sair= sairDoPrograma()

    sair= input("Voce deseja sair? (S/N)")

    if sair.upper()== "S":
        print("Voce escolheu a opcao sair, o programa sera fechado")
        break








#a pessoa escolhe uma opcao, se ela escolher a opcao 1, adiciona coisa na lista, se ela escolher a opcao 2, mas a lista estiver vazia, dizer q a lista esta vazia e repete o menu. Se ja tiver coisa adicionada, mostrar o que e ai, perguntar se quer sair, se sim finalizar. se nao fzr loop. se selecionar sair, dizer q ela escolheu sair e que o programa vai ser finalizado.



OPCAO_CADASTRO=1
OPCAO_LISTAR=2
OPCAO_SAIR=3

OPCOES_VALIAS=[
    OPCAO_CADASTRO,
    OPCAO_LISTAR,
    OPCAO_SAIR
]


jogos= [

]

while True:
    opcao= int(input("- - - - -MENU- - - - -\n" \
    "1- Cadastrar novo item \n" \
     #ela tem q armazenar e mostrar os dados da opção de cadastro, como faço isso, eu n seiii
    "2- Listar tudo cadastrado\n " \
    "3- Sair"))

    if opcao  == OPCAO_CADASTRO:
        nomeDoJogo= input("Digite o jogo que você deseja cadastrar: ")
        jogos.append(nomeDoJogo)

    elif opcao == OPCAO_LISTAR :
        print(f"Os jogos\consoles cadastrados até agora são: {jogos}")

    elif opcao not in OPCOES_VALIAS:
        print("Digite uma opção válida")

    elif opcao == OPCAO_SAIR:
        print("Voce escolheu a opcao sair, o programa sera fechado")

    sair= input("Voce deseja sair? (S/N)")

    if sair.upper()== "S":
        print("Voce escolheu a opcao sair, o programa sera fechado")
        break








#a pessoa escolhe uma opcao, se ela escolher a opcao 1, adiciona coisa na lista, se ela escolher a opcao 2, mas a lista estiver vazia, dizer q a lista esta vazia e repete o menu. Se ja tiver coisa adicionada, mostrar o que e ai, perguntar se quer sair, se sim finalizar. se nao fzr loop. se selecionar sair, dizer q ela escolheu sair e que o programa vai ser finalizado.
