def somar_numeros_impares(n):
    numero = 1
    soma = 0
    contador = 0
    
    while contador < n:
        soma += numero
        numero += 2
        contador += 1
    
    return soma

n = int(input("Digite o valor de n: "))
resultado = somar_numeros_impares(n)
print(f"A soma dos primeiros {n} numeros impares e: {resultado}")