#Escreva um programa Python para contar o número de elementos de tamanho 2 ou mais de uma lista qualquer, onde o
#primeiro e o último caractere do elemento são os mesmos.

lista_1 = ["cda", "gog", "qwe", "xax", "xay", "ak", "ax", "kak"]
count = 0

for i in lista_1:
    if len(lista_1) >= 2 and i[0] == i[-1]:
        count += 1

print ("O número de elementos da lista que tem o primeiro e último caratere igual são: ", count)