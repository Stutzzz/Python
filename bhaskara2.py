def main():
    a = float(input("Digite o valor de A: ").replace(",","."))
    b = float(input("Digite o valor de B: ").replace(",","."))
    c = float(input("Digite o valor de C: ").replace(",","."))
    delta = calDelta(a, b, c)
    bhaskara = calBhaskara(delta, a, b, c)


def calDelta(a, b, c):
    delta = (b**2)-(4*a*c)
    return delta

def calBhaskara(delta, a, b, c):
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

main()