palavra = "python"
letrasUsuario = []
chances = 7
ganhou = False
letrasNao = []
num =0


while True:
    for letra in palavra:
        if letra.lower() in letrasUsuario:
            print(letra, end = " ")
        else:
            print("_", end=" ")

    print("\nChances =",chances)
    print(f"suas tentativas: {letrasNao}")
    tentativa = input("Digite a letra da tentativa: ")

    if tentativa not in palavra:
        letrasNao.append(tentativa)

    letrasUsuario.append(tentativa.lower())

    if tentativa.lower() not in palavra:
        chances -=1

    if chances == 0:
        print(f"Você perdeu!!! a palavra é {palavra}")
        break
    for letra in letrasUsuario:
        if letra in palavra:
            num +=1

if num == 7:
    print(f"Você ganhou!!! a palavra era {palavra}")


    