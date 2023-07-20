numero = int(input("Digite um número para saber se é primo ou não: "))

if numero < 0:
    print("O número não é primo!!!")
elif numero == 2 or numero == 3 or numero == 5 or numero == 7:
    print("O número é primo!!!")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print("O número não é primo!!!")
            break
print("O número é primo!!!")