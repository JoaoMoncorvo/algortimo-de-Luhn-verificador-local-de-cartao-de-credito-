#basico que funciona
while True:
    cartaolista = []
    while True:
        cartao = input('Digite seu numero de cartao: ')
        cartao = cartao.replace(' ', '')
        cartaolista = list(cartao)
        if len(cartaolista) == 16 and cartao.isnumeric():
            break
        else:
            print('escreva um numero de cartao de credito que contenha 16 digitos e so numeros!! ')
            continue


    cartaolistaint = [int(x) for x in cartaolista]

    for c in range(0, 16, 2):
            cartaolistaint[c] = cartaolistaint[c] * 2
            if cartaolistaint[c] > 9:
                cartaolistaint[c] = cartaolistaint[c] - 9


    print(cartao)
    soma = sum(cartaolistaint)

    if soma % 10 == 0:
        print('seu cartao e valido ')
    else:
        print('seu cartao nao e valido ')

    while True:
        opcao = str(input('quer ver mais cartoes? [S/N] ')).strip().upper()[0]
        if opcao == 'S':
            continuar = 'S'
            break
        if opcao == 'N':
            continuar = 'N'
            break
        else:
            print('digite apenas S ou N')
            continue
    if opcao == 'S':
        continue
    elif opcao == 'N':
        break
    








