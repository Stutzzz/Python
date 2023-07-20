valor = float(input("Digite o valor unitário do produto: "))
valor2 = str(valor).replace(",",".")

quantidade = int(input("Digite a quantidade desse produto: "))

produto = valor * quantidade
print(f"O valor total sem desconto é: {produto}")

if quantidade <= 9 and quantidade > 0:
    # 0
    print(f"O valor total com desconto é: {produto}")
elif quantidade <= 99:
    # 5
    pro = (produto * 5) / 100
    desc = produto - pro
    
    print(f"O valor total com desconto é: {desc}")
elif quantidade <= 999:
    # 10
    pro = (produto * 10) /100
    
    desc = produto - pro
    print(f"O valor total com desconto é: {desc}")
elif quantidade >= 1000:
    pro = (produto * 15) / 100
    desc = produto - pro
    
    print(f"O valor total com desconto é: {desc}")