#Faça um programa que, dada a idade de um nadador, o classifique em uma das categorias listadas na tabela abaixo.
#Imprima o resultado na tela.
# Categoria                    Idade
# Infantil A                   5 - 7
# Infantil B                   8 - 10
# Juvenil A                    11 - 13
# Juvenil B                    14 - 17
# Sênior                       Maiores de 18

id = int(input("Entre com o valor da idade "))

if (id>=5) and (id<=7):
    print ("Infantil A")
elif (id>=8) and (id<=10):
    print ("Infantil B")
elif (id>=11) and (id<=13):
    print ("Juvenil A")
elif (id>=14) and (id<=17):
    print ("Juvenil B")
else:
    id >= 18
    print ("Sênior")
