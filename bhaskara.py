a = float(input("Digite o valor de A: ").replace(",","."))
b = float(input("Digite o valor de B: ").replace(",","."))
c = float(input("Digite o valor de C: ").replace(",","."))

delta = ((b**2) - (4*a*c))

if delta == 0:
    x1 = ((-b + (delta**(1/2)))/(2*a))
    print(x1)
elif delta < 0:
    print("A equação não possui raízes reais!!!")
elif delta > 0:
    x1 = ((-b + (delta**(1/2)))/(2*a))
    x2 = ((-b - (delta**(1/2)))/(2*a))
    print(x1)
    print(x2)