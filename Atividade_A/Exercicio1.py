n = 0
soma = 0
while n <= 50:
    if (n %3 == 0) or (n %5 == 0):
        soma = soma+n
        print (soma)
    n = n + 1