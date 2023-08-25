cor = ["azul", "vermelho", "verde"]
carros = ["gol", "argo", "fusca"]

for x in cor:
    for y in carros:
        print("O carro " + y + " é " + x)

################################################################
#matriz

matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        print(matriz[linha][coluna])