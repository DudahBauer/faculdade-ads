
def mostrarTotal(valorComJuros,valorTotalParcelado):
    print(f"O valor das parcelas é de: {valorComJuros :.2f}")
    print(f"O valor total parcelado é de: {valorTotalParcelado :.2f}")

#função que calcula o juros, o valor com juros e o valor total das parcelas e retorna uma tupla com valor com juros e valor parcelado
def calcularJuros(valorDaParcela, porcentagem, quantidadeDeParcelas):
    juros= valorDaParcela*porcentagem
    valorComJuros= juros + valorDaParcela
    valorTotalParcelado= valorComJuros * quantidadeDeParcelas

    return(valorComJuros, valorTotalParcelado)

print("Olá, bem vindo(a) Maria Eduarda Vicente Bauer")
valorDoPedido = float(input("Qual o valor do seu pedido?"))
quantidadeDeParcelas = int(input("Em quantas parcelas você deseja parcelar esse valor?"))

valorDaParcela = valorDoPedido/quantidadeDeParcelas

if quantidadeDeParcelas < 4:
    print("Você não terá juros no seu pedido!!")

elif quantidadeDeParcelas >=4 and quantidadeDeParcelas < 6:

    valorComJuros ,valorTotalParcelado = calcularJuros(valorDaParcela, 0.04, quantidadeDeParcelas)
    mostrarTotal(valorComJuros,valorTotalParcelado)

elif quantidadeDeParcelas >= 6 and quantidadeDeParcelas <9:

    valorComJuros, valorTotalParcelado = calcularJuros(valorDaParcela, 0.08, quantidadeDeParcelas)
    mostrarTotal(valorComJuros,valorTotalParcelado)

elif quantidadeDeParcelas >= 9 and quantidadeDeParcelas <13:

    valorComJuros ,valorTotalParcelado = calcularJuros(valorDaParcela, 0.16, quantidadeDeParcelas)
    mostrarTotal(valorComJuros,valorTotalParcelado)

else:
    valorComJuros ,valorTotalParcelado = calcularJuros(valorDaParcela, 0.32, quantidadeDeParcelas)
    mostrarTotal(valorComJuros,valorTotalParcelado)



