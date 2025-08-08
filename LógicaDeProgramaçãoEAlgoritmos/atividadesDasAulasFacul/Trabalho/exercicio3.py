print("Bem vindo ao sistema de cobrança! Desenvolvido por Maria Eduarda Vicente Bauer.")

# Função para esolcher o modelo de camisa
def escolha_modelo():
    while True:
        #Dicionario com chave sendo o modelo e o valor sendo o valor
        modelos = {
            "MLC":1.8,
            "MLS":2.1,
            "MCE":2.9,
            "MLE":3.2,
        }

        modelo = input("Escolha o modelo [MCS | MLS | MCE | MLE].").upper()
        if modelo in modelos:
            return modelos[modelo]
        else:
            print("Opção inválida! Tente novamente!")

#Função para obter o numero de camisas
def obter_numero_de_camisas():
    while True:
        try:
            quantidade_de_camisas = int(input("Digite o numero de camisas: "))

            if quantidade_de_camisas > 20_000:
                print("Quantidade de camisas não permitida! O máximo é de 20.000 camisetas.")
                continue

            if quantidade_de_camisas < 0:
                print("Quantidade de camisas não pode ser negativa.")
                continue

            return quantidade_de_camisas
        except ValueError:
            print("Opção inválida! Tente novamente!")

#Função para aplicar desconto
def aplicar_desconto(quantidade_de_camisas):
    desconto = 0

    if quantidade_de_camisas < 20:
        desconto = 0
    elif 20 <= quantidade_de_camisas < 200:
        desconto = 0.05
    elif 200 <= quantidade_de_camisas < 2_000:
        desconto = 0.07
    elif 2_000 <= quantidade_de_camisas <= 20_000:
        desconto = 0.12

    return desconto

#Função para realizar o calculo do frete
def calcular_frete():
    while True:
        opcao = input("Escolha o frete:\
                      \n1 - Transportadora (R$100)\
                      \n2 - Sedex (R$200)\
                      \n3 - Retirar na fábrica (R$0)" \
                      "\n")

        if opcao == "1":
            return 100
        elif opcao == "2":
            return 200
        elif opcao == "3":
            return 0

        print(f"A opção {opcao} de frete é inválida! Escolha entre [1, 2, 3]")

#Função que mostra o pedido formatado para o usuario final
def mostrar_pedido(valor_modelo,quantidade_camisas,desconto,valor_do_frete,total):
    print(f"\nResumo do pedido:")
    print(f"Valor da unidade do modelo escolhido: R${valor_modelo:.2f}")
    print(f"Quantidade de camisetas: {quantidade_camisas}")
    print(f"Desconto aplicado: {desconto*100:.2f}%")
    print(f"Valor do frete: R${valor_do_frete:.2f}")
    print(f"Total a pagar: R${total:.2f}")

def main():
    try:
        valor_do_modelo = escolha_modelo()
        quantidade_de_camisas = obter_numero_de_camisas()
        desconto = aplicar_desconto(quantidade_de_camisas=quantidade_de_camisas)
        valor_do_frete = calcular_frete()

        subtotal = valor_do_modelo * quantidade_de_camisas
        valor_do_desconto = subtotal * desconto
        total = subtotal - valor_do_desconto + valor_do_frete

        mostrar_pedido(
            desconto=desconto,
            quantidade_camisas=quantidade_de_camisas,
            total=total,
            valor_do_frete=valor_do_frete,
            valor_modelo=valor_do_modelo,
        )

    except Exception as e:
        print("Ocorreu um erro inesperado:\n\n", e)

if __name__ == "__main__":
    main()
