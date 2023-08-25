# Crie um progranma onde o usuário deve digitar as três medidas referente aos lados de um triângulo qualquer.
# O programa deve informar o tipo de triângulo de acordo com a seguinte regra:
# * Três lados iguais: Equilátero
# * Dois lados iguais: Isósceles
# * Três lados iguais: Escaleno

lad_1 = int (input("Digite o valor do primeiro lado "))
lad_2 = int (input("Digite o valor do segundo lado "))
lad_3 = int (input("Digite o valor do terceiro lado "))

if (lad_1!=lad_2!=lad_3) and (lad_2!=lad_3) and (lad_1!=lad_3):
    print ("Triângulo Escaleno")
    
elif  (lad_1==lad_2) and (lad_2==lad_3):
    print ("Triângulo Equilátero")
else:
    (lad_1!=lad_2) or (lad_1==lad_2) or (lad_1==lad_3) and (lad_2!=lad_3)
    print ("Triângulo Isósceles")
    