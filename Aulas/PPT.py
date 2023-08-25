#Faça a implementação do jogo pedra-papel-tesoura. O jogo imprime "Vitória", "Empate" ou "Derrota" dependendo da escolha 
#do jogador comparada com a opção soreada aleatoriamente para o computador.
#Utilize os números 1, 2 e 3 como pedra, papel e tesoura, respectavamente.

jogador_1 = (input("Entre com um valor entre 1 e 3 "))
jogador_2 = (input("Entre com um valor entre 1 e 3 "))

if jogador_1 == jogador_2:
    print ("Empate")
elif jogador_1 == 1 and jogador_2 == 3:
    print ("Jogador 1 ganhou")
elif jogador_1 == 2 and jogador_2 == 1:
    print ("Jogador 1 ganhou")
elif jogador_1 == 3 and jogador_2 == 2:
    print ("Jogador 1 ganhou")
else: print ("Jogador 2 ganhou")
