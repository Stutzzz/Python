print("----------Escolha um número!----------")
print("pense em número de 1 a 10")

question = input("Seu número é impar?\n1 - SIM\n2 - NÃO\n- ")
if question == "1":
    question = input("Seu número é primo?\n1 - SIM\n2 - NÃO\n- ")
    if question == "1":
        question = input("Seu número é maior que 6?\n1 - SIM\n2 - NÃO\n- ")
        if question == "1":
            print("----------SEU NÚMERO É 7!!!----------")
        elif question == "2":
            question = input("Seu número é 5?\n1 - SIM\n2 - NÃO\n- ")
            if question == "1":
                print("----------SEU NÚMERO É 5!!!----------")
            elif question == "2":
                print("----------SEU NÚMERO É 3!!!----------")
    elif question == "2":
        question = input("Seu número é divisível por 3?\n1 - SIM\n2 - NÃO\n- ")
        if question == "1":
            print("----------SEU NÚMERO É 9!!!----------")
        elif question == "2":
            print("----------SEU NÚMERO É 1!!!----------")
elif question == "2":
    question = input("Seu número é maior que 5?\n1 - SIM\n2 - NÃO\n- ")
    if question == "1":
        question = input("Seu número dividido por 2 é igual a 4?\n1 - SIM\n2 - NÃO\n- ")
        if question == "1":
            print("----------SEU NÚMERO É 8!!!----------")
        elif question == "2":
            question = input("Seu número é o maior possivel nesse jogo?\n1 - SIM\n2 - NÃO\n- ")
            if question == "1":
                print("----------SEU NÚMERO É 10!!!----------")
            elif question == "2":
                print("----------SEU NÚMERO É 6!!!----------")
    elif question == "2":
        question = input('Seu número é igual ao número da alternativa "NÃO"?\n1 - SIM\n2 - NÃO\n- ')
        if question == "1":
            print("----------SEU NÚMERO É 2!!!----------")
        elif question == "2":
            print("----------SEU NÚMERO É 4!!!----------")

