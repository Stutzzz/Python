QuantidadeNotas = int(input("Digite o número de notas: "))
notas = []
peso = []
somaNotasPeso = 0
somaPeso = 0
for i in range(QuantidadeNotas):
    notas.append(float(input(f"Digite o valor da nota {i+1}: ")))
    peso.append(int(input(f"Digite o peso da nota {i+1}: ")))
    somaNotasPeso += (notas[i] * peso[i])
    somaPeso += peso[i]

for i in range(QuantidadeNotas):
    print(f"nota {i+1}: {notas[i]} peso: {peso[i]}")

media = somaNotasPeso/somaPeso
print(f"Sua média é igual a {media:.1f}")
