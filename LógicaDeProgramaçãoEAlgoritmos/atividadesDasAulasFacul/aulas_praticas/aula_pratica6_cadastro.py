#ler nome, ano de nascimento e sexo de diferentes pessoas. Armazene os dados em um dicionário com lista. Ao encerrar o cadastro, apresente:
# -O total de cadastros efetuados,
# -A média da idade das pessoas.
# -Uma lista de mulheres com menos de 30 anos,
# -Uma lista de homens com idade acima da média


def borda(s1):
    tam= len(s1)
    if tam:
        print("+", "-" * tam, "+")
        print("|",s1,"|")
        print("+", "-" * tam, "+")
borda("Realize o cadastro de um usuáro")

cadastros={"nome": [], "data de nascimento": [], "sexo": []}

idades=[]
mulheres=[]
homens=[]
sair_opcaos_validas= []
total_de_cadastros=0
total_de_idades=0
while True:
        nome=input("Digite o nome da pessoa:")
        ano_de_nascimento=int(input("Digite o ano de nascimento da pessoa:"))
        sexo= input("Digite o sexo da pessoa (F/M):")

        total_de_cadastros=total_de_cadastros+1

        cadastros["nome"].append(nome)
        cadastros["data de nascimento"].append(ano_de_nascimento)
        cadastros["sexo"].append(sexo)

        total_de_idades=total_de_idades+1

        idade=2025-ano_de_nascimento
        idades.append(idade)
        soma= sum(idades)

        media=soma//total_de_idades

        if sexo.upper()=="F":
             if idade < 30:
                  mulheres.append(nome)

        elif sexo.upper()=="M":
            if idade > media:
                 homens.append(nome)


        media=soma//total_de_idades


        sair=input("Deseja realizar mais algum cadastro? S/N")

        # if sair.upper()!="S" and sair.upper!="N":
        #       print("Você digitou uma opção invalida, digite uma opção válida")
        #       continue
        if sair.upper()=="S":
            continue
        elif sair.upper()=="N":
            print(f"O total de cadastros efetuados foi:{total_de_cadastros}\n")
            print(f"A média da idade das pessoas cadastradas foi de: {media}\n")
            print(f"A lista de mulheres com menos de 30 anos é: {mulheres}\n")
            print(f"A lista de homens com idade acima da média é: {homens}\n")
            break


