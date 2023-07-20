print("-------------------------------------\n---BEM VINDO A CANTINA DO SENAI!!!---\n-------------------------------------")
produtos = {100:{"descricao":"Cachorro-Quente",
                 "preco":9.0},
            101:{"descricao":"Cachorro-Quente Duplo",
                 "preco":11.0},
            102:{"descricao":"X-Egg",
                 "preco":12.0},
            103:{"descricao":"X-Salada",
                  "preco":12.0},
            104:{"descricao":"X-Bacon",
                  "preco":14.0},
            105:{"descricao":"X-Tudo",
                  "preco":17.0},
            200:{"descricao":"Refrigerante Lata",
                  "preco":5.0},
            201:{"descricao":"Chá-Gelado",
                  "preco":4.0}
            }

soma = 0
pergunta = int(input("Quer comprar?\n1 - SIM\n2 - NÃO\n:"))
print("--------------CARDÁPIO--------------")
print("| Código |    Descrição    | Valor |")
print("|  100   | Cachorro-quente |  9,00 |")
print("|  101   | Cachorro duplo  | 11,00 |")
print("|  102   |      X-Egg      | 12,00 |")
print("|  103   |    X-Salada     | 12,00 |")
print("|  104   |     X-Bacon     | 14,00 |")
print("|  105   |     X-Tudo      | 17,00 |")
print("|  200   |  Refrigerante   |  5,0  |")
print("|  201   |   Chá-Gelado    |  4,0  |")

codigos = []
while (True):
    
    if pergunta == 1:
        codigo = int(input("\nDigite o código do produto desejado: "))
        codigos.append(codigo)

        validacao = produtos.get(codigo,"Código não encontrado")
        if validacao == "Código não encontrado":
            print(validacao)
            continue

        soma += int(produtos[codigo]["preco"])
        print("--------------------------------------")
        print(f"O valor do produto", produtos[codigo]["descricao"], "é igual a R$",produtos[codigo]["preco"])
        print("--------------------------------------")
        pergunta = int(input("Quer continuar comprando?\n1 - SIM\n2 - NÃO\n:"))
        continue
    elif pergunta == 2:
        print(f"-------------VALOR TOTAL--------------")
        for i in range(len(codigos)):
            print(i+1," - ",produtos[codigos[i]]["descricao"],": R$",produtos[codigos[i]]["preco"],sep="")
        print(f"O valor total dos produtos é igual a: R${soma:.2f}")
        break
    else:
        print("Opção inválida!!!")
        pergunta = int(input("Quer continuar comprando?\n1 - SIM\n2 - NÃO\n:"))
        continue