#Escreva um programa que retorna verdadeiro se existir ao menos um elemento que seja comum as duas listas.

lista_1 = ["aba", "x12", "ama", "abcx", "aa", "a1", "c4"]
lista_2 = ["abcx", "321aa", "64", "dsa", "ffgdg", "a2", "c4"]


for item in lista_1:
    for itens in lista_2:
        if item == itens:
            print(item, True)