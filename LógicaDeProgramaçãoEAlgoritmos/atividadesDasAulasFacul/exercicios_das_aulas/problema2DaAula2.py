#pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais o carro foi alugado. Com isso, calcular o valor que vai dar, levando em conta que o carro custa 60 por dia e 0,15 por km

dias =int(input("Por quantos dias você alugou o carro?:"))
km_rodado= int(input("Quantos km o carro rodou?:"))

valor_por_dia= dias*60
valor_por_km= km_rodado*0.15

valor_total_do_aluguel= valor_por_dia+valor_por_km

print(f"Você alugou o carro por {dias} dias e ele rodou {km_rodado} km. Portanto, o valor que vc deve pagar é de: {valor_total_do_aluguel}")
