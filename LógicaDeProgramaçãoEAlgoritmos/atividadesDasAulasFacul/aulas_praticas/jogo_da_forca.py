import random
import os

def borda(s1):
    tam= len(s1)
    if tam:
        print("+", "-" * tam, "+")
        print("|",s1,"|")
        print("+", "-" * tam, "+")

def mostrarMenu():
    return int(input("- - - - -MENU- - - - -\n" \
    "1- Jogar\n" \
    "2- Score\n" \
    "3- Sair \n"))

def acertou_a_letra():
     pontos=0
     if chute in palavra_sorteada:
        pontos=pontos+1
        score.update({"Pontuação": pontos})
        print(f"Parabens, a letra: {chute.upper()} existe na palavra.\n")
        revelar_letras()
        print(f"As letras que você digitou até agora, foram: {letras_digitadas}\n")


def errou_a_letra():
    if chute not in palavra_sorteada:
         print(f"Puts, a letra: {chute.upper()} não existe na palavra\n")
         revelar_letras()
         print(f"As letras que você digitou até agora, foram: {letras_digitadas}\n")

def acertou_a_palavra_inteira():
    pontos=0
    if len(palavras_digitadas)>0 and chute in palavra_sorteada:
        pontos=pontos+1
        score.update({"Pontuação": pontos})
        print("🎉VOCÊ VENCEU! VOCÊ ADIVINHOU A PALAVRA🎉 \n")
        print(f"A palavra reamente era: {palavra_sorteada}")
        return True
    return False


def revelar_letras():
    for i in range (len(palavra_sorteada)):
        if palavra_sorteada[i]==chute:
            palavra_oculta[i]=chute
    print(f"A palavra está assim até agora:")
    print(" ".join(palavra_oculta))

def verificar_morte():
    tamanho= len(letras_digitadas)
    tamanho_da_palavra_sorteada= len(palavra_sorteada)
    if tamanho >= tamanho_da_palavra_sorteada:
        print(f"☠️ Você morreu, chutou: {len(letras_digitadas)} letras e a palavra tinha {len(palavra_sorteada)} letras !!:(☠️ \n")
        print(f"A palavra era: {palavra_sorteada}")
        return True

    return False

def verificar_vitoria():
    if palavra_oculta.count("-")==1:
        print("🎉VOCÊ VENCEU! VOCÊ ADIVINHOU A PALAVRA🎉 \n")
        print(f"A palavra era: {palavra_sorteada}")
        return True

    return False

def limpar_terminal():
    if os.name=="nt":
        os.system("cls")



palavras_digitadas=[]
letras_digitadas=[]
score={}
palavras =["gato", "casa", "sol", "livro", "bola", "amigo", "janela", "planeta", "escova", "camisa","abacaxi", "helicoptero", "xilofone", "maracuja", "quilombo", "pipoca", "escola", "telefone", "carro", "girassol", "montanha", "praia", "computador", "cachorro", "elefante", "borboleta", "chave", "futebol", "geladeira", "janela", "lapis", "mesa", "navio", "oceano", "palhaco", "python", "garrafa", "xicara", "caneta"]
palavra_oculta=[]

OPCAO_JOGAR=1
OPCAO_SCORE=2
OPCAO_SAIR=3

OPCOES_VALIDAS=[
OPCAO_JOGAR,
OPCAO_SCORE,
OPCAO_SAIR
]

borda("JOGO-DA-FORCA")

while True:
    opcao= mostrarMenu()

    if opcao not in OPCOES_VALIDAS:
        print("Você escolheu uma opção inválida! Escolha uma válida.")

    if opcao==OPCAO_JOGAR:
        palavra_sorteada = random.choice(palavras)
        nome= input("Digite seu nome: \n")
        score.update({"nome": nome})
        limpar_terminal()
        pontos=0

        for letra in palavra_sorteada:
            palavra_oculta.append("-")

        print(" ".join(palavra_oculta))
        chute=input(f"Digite uma letra da palavra acima ou chute qual palavra você acha que é:\n")
        if len(chute)==1:
            letras_digitadas.append(chute)
        else: palavras_digitadas.append(chute)

        while True:
            acertou_a_palavra= acertou_a_palavra_inteira()
            if acertou_a_palavra:
                print("Seu score dessa partida, ficou assim: \n")
                print(score)
                jogar_novamente= input("Você deseja jogar novamente? S/N:")

                if jogar_novamente.upper()=="S":
                    letras_digitadas.clear()
                    score.clear()
                    break
                else: break

            esta_morto= verificar_morte()
            if esta_morto:
                tentar_novamente= input("Você deseja jogar novamente? S/N:")

                if tentar_novamente.upper()=="S":
                    print("Seu score dessa partida, ficou assim: \n")
                    print(score)
                    letras_digitadas.clear()
                    score.clear()
                    limpar_terminal()
                    break
                else: break

            venceu= verificar_vitoria()
            if venceu:
                jogar_novamente= input("Você deseja jogar novamente? S/N:")

                if jogar_novamente.upper()=="S":
                    print("Seu score dessa partida, ficou assim: \n")
                    print(score)
                    letras_digitadas.clear()
                    score.clear()
                    break
                else: break

            acertou_a_letra()

            errou_a_letra()

            tentar_novamente= input("Você deseja continuar adivinhando? S/N: \n"
            "(Caso não, você irá retornar ao menu!)")

            if tentar_novamente.upper()=="S":
                limpar_terminal()
                print(f"Chute de novo uma letra ou uma palavra: \n{" ".join(palavra_oculta)}")
                chute= input()
                if len(chute)==1:
                    letras_digitadas.append(chute)
                elif len(chute)>1:
                    palavras_digitadas.append(chute)

            else:
                print("Seu score dessa partida, ficou assim: \n")
                print(score)
                letras_digitadas.clear()
                score.clear()
                break


    if opcao==OPCAO_SCORE:
        if not score:
            print("O score está vazio")
        else:
            print(score)

        sair= input("Deseja retornar ao menu? (S/N):\n")
        if sair.upper()=="N":
            break
        else: continue

    if opcao==OPCAO_SAIR:
        print("Você escolheu a opção SAIR, o programa será fechado!!")
        break


