#imprima valores na tela um intervalo especificado pelo usuário e que sejam números pares
print("Crie uma sequência de números pares")
comeco= int(input("Digite um o valor que deseja iniciar sua sequência"))
final= int(input("Digite o valor de deseja terminar sua sequência"))

x= comeco

while x<= final:
    if x % 2 == 0:
        print(f"{x}")
    x= x + 1
