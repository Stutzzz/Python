catetoA = float(input("Digite o valor do cateto A: ").replace(",","."))
catetoB = float(input("Digite o valor do vateto B: ").replace(",","."))

hipotenusa = (catetoA**2) + (catetoB**2)
hipo = (hipotenusa ** (1/2))

perimetro = hipo + catetoB + catetoA
area = (catetoA * catetoB) /2

print(f"O valor do perímetro é igual a: {perimetro}")
print(f"O valor da área é igual a : {area}")