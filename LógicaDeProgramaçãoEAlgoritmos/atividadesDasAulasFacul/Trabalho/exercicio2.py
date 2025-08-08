#mostra o menu
print("Olá, boas vindas ao restaurante da Maria Eduarda Vicente Bauer!!\n"

"Temos em nosso menu as seguintes opções de pratos:\n"

"1- Bife acebolado (BA) pequeno: 16 reais ou Filé de frango (FF) pequeno: 15 reais\n"

"2- Bife acebolado (BA) médio: 18 reais ou Filé de frango (FF) médio: 17 reais\n"

"3- Bife acebolado (BA) grande: 22 reais ou Filé de frango (FF) grande: 21 reais")


totalDosPedidos=0

while True:#loop principal

    while True:

        sabor = input("Insira o sabor desejado (BA ou FF):")

        if sabor not in ["BA","FF"]:
            print("Pedido inválido!!Insira um pedido válido")
            continue
        break



    while True:
        tamanho= input("Insira do tamanho desejado (P, M OU G):")

        if tamanho not in ["P", "M", "G"]:
            print("Tamanho inválido!! Insira um tamanho válido")
            continue
        break



#define o valor com base no sabor e no tamanho
    if sabor == "BA":

        if tamanho == "P":

            valor = 16

        elif tamanho == "M":

            valor = 18

        elif tamanho == "G":

            valor = 22



    elif sabor == "FF":

        if tamanho == "P":

            valor = 15

        elif tamanho == "M":

            valor = 17

        elif tamanho == "G":

            valor = 21

    #incrementa o acumulador
    totalDosPedidos=totalDosPedidos + valor

    print(f"Você pediu um {sabor} do tamanho {tamanho}! Seu pedido fica no valor de: {valor} reais.")
    print(f"O valor total do seu pedido é de: {totalDosPedidos}")

    resposta= input("Gostaria de pedir mais alguma coisa? (S ou N):")
    if resposta == "N":
            print("Agradeco seu pedido. volte sempre!")
            break













