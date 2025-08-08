from random import choice

def borda(s1):
    tam= len(s1)
    if tam:
        print("+", "-" * tam, "+")
        print("|",s1,"|")
        print("+", "-" * tam, "+")
borda("Pedra, papel ou tesoura da Dudinha")

PEDRA=1
PAPEL=2
TESOURA=3

OPCOES_VALIDAS= [PEDRA, PAPEL, TESOURA]

historico=[]

O_JOGO_DEVE_CONTINUAR= True

vitoria_do_jogador=0
vitoria_da_maquina= 0

while O_JOGO_DEVE_CONTINUAR:
    jogada_do_jogador= int(input("Selecione entre: Pedra, Papel ou Tesoura\n" \
    "(1)- Pedra\n" \
    "(2)- Papel\n" \
    "(3)- Tesoura\n"))

    jogada_da_maquina= choice([1,2,3])

    if jogada_do_jogador== jogada_da_maquina:
        print("Vocês esclheram a mesma opção, portanto, deu empate")
        continue

    if jogada_do_jogador not in OPCOES_VALIDAS:
        print("Opção inválida, digite uma opção válida!\n")
        continue
#Pedra
    elif jogada_do_jogador==PEDRA:
        if jogada_da_maquina==PAPEL:
            print("Vitória da máquina")
            historico.append((PEDRA,PAPEL))
            vitoria_da_maquina= vitoria_da_maquina+1

        elif jogada_da_maquina==TESOURA:
            print("Vitória do jogador")
            historico.append((PEDRA, TESOURA))
            vitoria_do_jogador=vitoria_do_jogador+1

#Papel
    elif jogada_do_jogador==PAPEL:
        if jogada_da_maquina==PEDRA:
            print("Vitória do jogador")
            historico.append((PAPEL, PEDRA))
            vitoria_do_jogador=vitoria_do_jogador+1

        elif jogada_da_maquina==TESOURA:
            print("Vitória da máquina")
            historico.append((PAPEL, TESOURA))
            vitoria_da_maquina= vitoria_da_maquina+1


#Tesoura
    elif jogada_do_jogador==TESOURA:
        if jogada_da_maquina==PEDRA:
            print("Vitória da máquina")
            historico.append((TESOURA, PEDRA))
            vitoria_da_maquina= vitoria_da_maquina+1

        elif jogada_da_maquina==PAPEL:
            print("Vitória dO jogador")
            historico.append((TESOURA, PAPEL))
            vitoria_do_jogador=vitoria_do_jogador+1

    print(f"O placar dessa partida foi de: \n Jogador:{vitoria_do_jogador}\n PC:{vitoria_da_maquina}")

    sair= input("Você deseja sair? S/N:")
    if sair.upper()=="N":
        continue
    elif sair.upper()=="S":
        print(f"Vc escolheu sair. O placar final do jogo foi de: \n Jogador: {vitoria_do_jogador}.\n PC: {vitoria_da_maquina}")
        if vitoria_do_jogador>vitoria_da_maquina:
            print("Você venceu a rodada!! Parabéns :)")
        elif vitoria_do_jogador<vitoria_da_maquina:
            print("Você perdeu a rodada!")
        break

