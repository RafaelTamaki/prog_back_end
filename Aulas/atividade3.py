#Crie um programa que receba duas matrizes quadradas de dimensão n*n qualquer, com n>=3.
#O progama deve verificar se existem elementos iguais em ambas matrizes, considerando sempre a mesma posição.

matriz_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_2 = [[1, 2, 3], [5 ,6, 7], [7, 9, 10]]

for linha in range(len(matriz_1)):
    for coluna in range(len(matriz_1)):
        if matriz_1[linha][coluna] == matriz_2[linha][coluna]:
            print (matriz_1[linha][coluna], matriz_2[linha][coluna])
 