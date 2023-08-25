def calcular_fatorial(numero):
    if numero == 0:
        return 1
    
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    
    return fatorial

def main():
    numero = int(input("Digite um número entre 0 e 8: "))
    
    if numero < 0 or numero > 8:
        print("Número fora da faixa permitida.")
    else:
        fatorial = calcular_fatorial(numero)
        print(f"O fatorial de {numero} é: {fatorial}")

if __name__ == "__main__":
    main()