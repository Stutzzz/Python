res = ""
contador = 0
nomeD = []
disciplinas = int(input("Quantas disciplinas deseja informar: "))
for i in range (disciplinas):
    nomeD.append(input(f"Qual o nome da disciplina {i}: "))
    
for i in range (disciplinas):
     print(f"----------{nomeD[i]}-----------")
     nuemroNotasDis = int(input("Digite o número de notas: "))
     soma = 0
     
     for j in range (nuemroNotasDis):
        print(f"------------{nomeD[i]}---------------")
        n = float(input("Digite a nota: "))
        soma = soma + n
        soma = soma / nuemroNotasDis
     print(f"A média de {nomeD[i]} é: {soma:.2f}")
     res += str(f"\nA média de {nomeD[i]} é: {soma:.2f}")
print(f"\nAs médias são: {res}")