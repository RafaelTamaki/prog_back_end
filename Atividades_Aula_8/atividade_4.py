#Escreva um programa em Python para dividir uma determinada lista em duas partes, onde o comprimento da primeira
#parte da lista é fornecido.
#• [1, 1, 2, 3, 4, 4, 5, 1]
#• Comprimento da primeira parte da lista: 3
#• Dividiu a referida lista em duas partes: ([1, 1, 2], [3, 4, 4, 5, 1])

comprimento = int(input("Digite o tamanho da primeira Lista: "))

lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

p1 = lista[:comprimento]
p2 = lista[comprimento:]

print("Primeira parte: ",p1)
print("Segunda parte: ",p2)