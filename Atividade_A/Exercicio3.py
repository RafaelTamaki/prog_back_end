n = int(input("Entre com um valor "))
n1 = 0
n2 = 1

for i in range(0, n):
    f = n1 +n2
    n1 = n2
    n2 = f
    print (f)