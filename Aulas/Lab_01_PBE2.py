# Modifique o programa anterior, de maneira que o usuário também consiga entrar com a taxa de câmbio do dia.
# Mude o cálculo para utilizar o valor guardado na variável ao invés do valor fixo de R$ 5,50.

dolar = float (input("Digite o valor em dólar "))
cambio = float (input("Digite o valor do dólar atual "))
real = cambio*dolar
print ("O valor em real é: ",real)