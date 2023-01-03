alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']



def encripta(msg, chave):
    palavraNova = list(range(len(msg)))
    for i in range(len(msg)):
        if msg[i] == ' ':
            letraEncripitada = ' '
            palavraNova[i] = letraEncripitada
        else:
            letraEncripitada = alpha.index(msg[i])
            palavraNova[i] = alpha[letraEncripitada + chave]

    palavraEncripitada = "".join(palavraNova)
    print(f'A mensagem criptografa é {palavraEncripitada}')

def desencripta(msg, chave):
    palavraNova = list(range(len(msg)))
    for i in range(len(msg)):
        if msg[i] == ' ':
            letraEncripitada = ' '
            palavraNova[i] = letraEncripitada
        else:
            letraEncripitada = alpha.index(msg[i])
            palavraNova[i] = alpha[letraEncripitada - chave]
    palavraEncripitada = "".join(palavraNova)
    print(f'A mensagem descriptografa é {palavraEncripitada}')


    

    






