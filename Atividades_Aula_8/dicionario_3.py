meu_dicionario = {
    "valor1" : 12,
    "valor2" : 8,
    "valor3" : 6,
    "valor4" : 20,
    "valor5" : 2,
    "valro6" : 24,
}

soma_divi4 = 0

for valor in meu_dicionario.values():
    if valor %4 == 0:
        soma_divi4 += valor

print ("A soma dos valores divisiveis por 4 é: " , soma_divi4)

