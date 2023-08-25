#Escreva um programa que receba dois números inteiros do usuario. A seguir, imprima todos os números inteiros entre
#a e b, incluindo eles mesmos

a = int(input("Entre com o menor número"))
b = int(input("Entre com o maior número"))

for i in range(a, b+1):
    print (i)
