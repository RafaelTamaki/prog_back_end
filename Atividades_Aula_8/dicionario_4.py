chaves = ["nome", "idade", "cidade"]
valores = ["Rafael", 31, "Itajubá"]


if len(chaves) == len(valores):
    meu_dicionario = {}

    for i in range(len(chaves)):
        chave = chaves[i]
        valor = valores[i]
        meu_dicionario[chave] = valor

    print("Dicionário resultante:", meu_dicionario)
