def main(): 
    reais = reais_to_float(input("Quanto deu a conta? "))
    percent = percent_to_float(input("Qual a porcentagem da gorgeta? "))
    tip = reais * percent
    print(f"Deixe R${tip:.2f}")

def reais_to_float(d): 
    d.replace("R$", "")
    try:
        d = float(d)
    except:
        print("Valor informado não é númerico")
    return d

def percent_to_float(p):
    p.replace("%", "")
    try:
        p = float(p)
    except:
        print("Valor informado não é númerico")
    p = p/100
    return p

main()