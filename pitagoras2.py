def main():
    catetoA = float(input("Digite o valor do cateto A: "))
    catetoB = float(input("Digite o valor do cateto B: "))
    hipotenusa = calHipotenusa(catetoA, catetoB)
    perimetro = calPerimetro(catetoA, catetoB, hipotenusa)
    print(f"O perimetro é igual á: {perimetro}")
    
    area = calArea(catetoA, catetoB)
    print(f"A área do seu triangulo é igual a: {area}")

def calHipotenusa(catetoA, catetoB):
    hipotenusa = (catetoA**2)+(catetoB**2)
    hipotenusa = hipotenusa**(1/2)
    return hipotenusa
    
def calPerimetro(catetoA, catetoB, hipotenusa):
    perimetro = catetoA + catetoB + hipotenusa
    return perimetro

def calArea(catetoA, catetoB): 
    area = (catetoA * catetoB)/2
    return area

main()