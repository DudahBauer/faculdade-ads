if opcao==OPCAO_JOGAR:
    nome=input("Digite seu nome:")
    score.update({"nome": nome})

    pontos=0

    for letra in palavra_sorteada:
        palavra_oculta.append("_")
        print:("Adivinhe que palavra é essa:")


    while True:
        letra_digitada=input("Digite uma letra para tentar adivinhar:  ")
        letras_digitadas.append(letra_digitada)

        encontrou_a_letra = False

        indice = None

        pontos=0

        for i,letra in enumerate(palavra_sorteada):
            if letra == letra_digitada:
                palavra_oculta[i] = letra_digitada
                pontos=pontos+1
                score.update({"pontos": pontos})
                print(f"Parabéns, a letra: {letra_digitada} existe na palavra!!\n")
                encontrou_a_letra = True
                indice = i

                sair= input("Deseja tentar adivinhar mais uma letra? (S/N):\n")
                if sair.upper()=="S":
                    print(f"Tente novamente adivinhar a palavra: \n")
                    print("Palavra até agora:", " ".join(palavra_oculta))

                    print(f"Até agora as letras que você digitou foram: {letras_digitadas}")

                    letra_digitada=input("Digite uma letra para tentar adivinhar:  ")
                    letras_digitadas.append(letra_digitada)

                else:
                    print(f"Você escolheu sair, portanto, o jogo será fechado!")
                    break


        if not encontrou_a_letra:
            print(f"Vish, a letra: {letra_digitada} não existe na palavra: \n ")

            sair= input("Deseja tentar adivinhar mais uma letra? (S/N):\n")

            if sair.upper()=="S":
                print(f"Tente novamente adivinhar a palavra: \n")
                palavra_oculta[i] = letra_digitada
                print(f"Até agora as letras que você digitou foram: {letras_digitadas}")
                letra_digitada=input("Digite uma letra para tentar adivinhar:  ")
                letras_digitadas.append(letra_digitada)
            else:
                print(f"Você escolheu sair, portanto, o jogo será fechado!")
                break


        if indice != None:
            palavra_oculta[indice] = letra_digitada
