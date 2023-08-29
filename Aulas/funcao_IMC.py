#Faça uma função para calcular o IMC de uma pessoa
#IMC = peso/(altura^2)

altura = float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))

def IMC(altura, peso):
    IMC = peso/(altura*altura)
    print (IMC)

IMC (altura, peso)