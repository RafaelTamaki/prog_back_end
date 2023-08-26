#Escreva um programa que remova valores duplicados de uma lista e exiba o antes e o depois. Você pode utilizar um laço
#para isso.

lista_antiga = ["a", "c", "d", "e", "a", "b", "c", "c", "e", "a", "b"]

print("Lista antiga:", lista_antiga)

lista = []

for i in lista_antiga:
    if i not in lista:
        lista.append(i)

lista_antiga[:] = lista

print("Atualizada:", lista_antiga)