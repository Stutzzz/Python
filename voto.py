idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não vota!!!")
elif idade >= 18 and idade <= 70:
    print("Voto obrigatóio!!!")
else:
    print("Voto opcional!!!")