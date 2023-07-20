peso = 0
notas = []
quantNotas = int(input("Quantas notas deseja informar? "))
pesoNota = []
mediaNotas = 0
for i in range (quantNotas):
    notas.append(float(input(f"Digite a nota {i + 1}: ")))
    pesoNota.append(float(input(f"Digite o peso da nota {i + 1}: ")))
    peso += pesoNota[i] 
    mediaNotasMult = notas[i] * pesoNota[i]
    mediaNotas = mediaNotas + mediaNotasMult
    media = mediaNotas / peso

print("----------MÉDIA----------")
print(f"{media:.2f}")
