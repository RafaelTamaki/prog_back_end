#Faça um programa que receba um número real. Caso ele seja positivo, calcule e mostre o número digitado ao quadrado e a raiz 
#quadrada do mesmo número. Caso ele seja nulo ou negativo, exiba essa informação na tela para o usuário.

n = float(input("Digite um número "))

if n <=0:
    print ("Número nulo ou negativo")
else:
    quad = n*n
    print ("O número ao quadrado é: ",quad)
    raiz = n**(1/2)
    print ("A raiz quadrada do número é: ",raiz)