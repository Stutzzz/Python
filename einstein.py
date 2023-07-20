massa = int(input("Digite um valor de massa: "))
c = 300000000
c2 = pow(c,2)
cal = massa * c2 
str(cal)
text = (f"O valor em Joules é igual a: {cal:,}").replace(",",".")
print(text)

