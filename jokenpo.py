import random

p = int(input("1 - j1 vs j2\n2 - j1 vs pc\nEm qual modo você quer jogar?"))
cal =0


if p == 1:
    player1 = int(input("PLAYER 1 - \n1 - Pedra\n2 - Papel\n3 - Tesoura\nDigite sua jogada:"))
    player2 = int(input("PLAYER 2 - \n1 - Pedra\n2 - Papel\n3 - Tesoura\nDigite sua jogada: "))
    cal = player1 - player2

elif p == 2:
    player1 = int(input("PLAYER 1 - \n1 - Pedra\n2 - Papel\n3 - Tesoura\nDigite sua jogada:"))
    pc = random.randrange(1,4)
    cal = player1 - pc

    if pc == 1:
        print("A jogado do PC foi: Pedra")
    elif pc == 2:
        print("A jogada do PC foi: Papel")
    else:
        print("A jogada do PC foi: Tesoura")
else:
    print("DIGITE UM NÚMERO VÁLIDO")

#1 - 1 = 0 em -
#1 - 2 = -1 de
#1 - 3 = -2 vi

#2 - 1 = 1 vi
#2 - 2 = 0 em -
#2 - 3 = -1 de

#3 - 1 = 2 de
#3 - 2 = 1 vi
#3 - 3 = 0 em -

#0 = em
# -1, 2 = de
# -2, 1 = vi

if cal == 0:
    print("EMPATE!!!")
elif cal == -1 or cal == 2:
    print("DERROTA do Player 1!!!")
elif cal == -2 or cal == 1:
    print("VITÓRIA do player 1")
else:
    print("DIGITE UM VALOR VÁLIDO")

