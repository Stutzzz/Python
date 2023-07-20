salario = float(input("Digite o seu salário").replace(",","."))
print(f"O salário bruto é igual a: {salario}")
ir = 0
if salario <= 1903.98:
    salario = salario
    print(f"O valor da dedução do IR é igual a: {ir}")
    print(f"O valor do salário líquido é igual a: {salario}")
elif salario <= 2826.65:
    ir = float(salario * 0.075)
    print(ir)
    salario = (salario - ((ir) - 142.80))
    print(f"O valor da dedução do IR é igual a: {ir}")
    print(f"O valor do salário líquido é igual a: {salario}")
    
elif salario <= 3751.05:
    ir = float(salario*0.15)
    salario = (salario - ((ir) - 354.80))
    print(f"O valor da dedução do IR é igual a: {ir}")
    print(f"O valor do salário líquido é igual a: {salario}")
    
elif salario <= 4664.68:
    ir = salario*0.225
    salario = (salario - ((ir) - 636.13))
    print(f"O valor da dedução do IR é igual a: {ir}")
    rint(f"O valor do salário líquido é igual a: {salario}")
    
elif salario > 4664.68:
    ir = salario*0.275
    salario = (salario - ((ir) - 869.36))
    print(f"O valor da dedução do IR é igual a: {ir}")
    print(f"O valor do salário líquido é igual a: {salario}")
    

