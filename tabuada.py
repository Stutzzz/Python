numero = 0
for i in range (1, 11):
    print("")
    numero = numero + 1
    for j in range(1, 11):
        res = numero * j
        print(f"{numero} x {j} = ", res)