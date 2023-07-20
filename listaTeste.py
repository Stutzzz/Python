# Uma lista/Array funciona da mesma forma que uma variavel, a diferença é que pode aribuir uma lista de valores
saladaDeFrutas = ["Banana"]
# Método append para adcionar um intem no final da lista
saladaDeFrutas.append ("Maçã")
# Método insert serve para adcionar em uma posicao especifica da lista, precisa dar a posicao
saladaDeFrutas.insert(0,"Laranja")
# Método remove exclui um intem
saladaDeFrutas.remove("Maçã")
# Método pop remove o ultima item. Porém ele serve para remover e inserir em outro lugar
fruta = saladaDeFrutas.pop()
# Método clear, limpa toda a lista
saladaDeFrutas.clear()
# Método copy, copia a lista
copia = saladaDeFrutas.copy()
# Se voce ussar o (=) x = saladaDeFrutas, voce pode mudar o x e a saladaDe Frutas tambem vai mudar
x = saladaDeFrutas

x.append(10)

print(saladaDeFrutas)

print(saladaDeFrutas)
print(fruta)
print(copia)



senhas = [10,20,30,40]
senhas.insert(0,senhas.pop())
print(senhas)

# Método reverse, muda a ordem da senha
senhas.reverse()
# Método sort serve para ordenar em ordem crescente
senhas.sort()
# Decrescente
senhas.sort(reverse = True)
# Método min ele pega o menor termo da lista/ max funciona da mesma forma
min(senhas)
max(senhas)
# Método cont() serve para contar quantos items iguais existem na lista
con = senhas.count(10)
# Método index() serve para mostrar em qual posicao esta deerminado item
pos = senhas.index(10)



print(senhas)

nome = "Leandro"
print(nome[0])