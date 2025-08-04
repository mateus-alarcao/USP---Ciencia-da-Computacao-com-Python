contv = 0
contc = 0

def inicio():
    print('Bem-vindo ao jogo do NIM! Escolha: ')
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato ')
    res = input()

    if res == '1':
        print('Você escolheu uma partida isolada! ')
        return partida()
    else:
        print('Você escolheu um campeonato!')
        return campeonato()


def usuario_escolhe_jogada(n, m):
    global contv
    max_tirar = min(m, n)

    jogada = int(input('Quantas peças você vai tirar? '))
    while jogada < 1 or jogada > max_tirar:
        print('Oops! Jogada inválida! Tente de novo.')
        jogada = int(input('Quantas peças você vai tirar? '))

    if jogada == 1:
        print('Você tirou uma peça.')
    else:
        print(f'Você tirou {jogada} peças.')

    return jogada


def computador_escolhe_jogada(n, m):
    global contc
    jogada = min(m, n)

    while jogada > 0:
        if (n - jogada) % (m + 1) == 0:
            break
        jogada -= 1

    if jogada == 0:
        jogada = min(m, n)

    if jogada == 1:
        print('O computador tirou uma peça.')
    else:
        print(f'O computador tirou {jogada} peças.')

    return jogada


def partida(is_campeonato=False):
    global contv, contc
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    if n % (m + 1) == 0:
        print('Você começa!')
        while n > 0:
            jogada_usuario = usuario_escolhe_jogada(n, m)
            n -= jogada_usuario
            if n == 0:
                print('Fim do jogo! Você ganhou!')
                contv += 1
                break
            jogada_pc = computador_escolhe_jogada(n, m)
            n -= jogada_pc
            if n == 0:
                print('Fim do jogo! O computador ganhou!')
                contc += 1
                break
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            elif n > 1:
                print(f'Agora restam {n} peças no tabuleiro.')

    else:
        print('Computador começa!')
        while n > 0:
            jogada_pc = computador_escolhe_jogada(n, m)
            n -= jogada_pc
            if n == 0:
                print('Fim do jogo! O computador ganhou!')
                contc += 1
                break
            jogada_usuario = usuario_escolhe_jogada(n, m)
            n -= jogada_usuario
            if n == 0:
                print('Fim do jogo! Você ganhou!')
                contv += 1
                break
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            elif n > 1:
                print(f'Agora restam {n} peças no tabuleiro.')

    if not is_campeonato:
        if contv > contc:
            print('Você venceu a partida!')
        else:
            print('O computador venceu a partida!')


def campeonato():
    global contv, contc
    contv = 0
    contc = 0
    for x in range(3):
        print(f'\n**** Rodada {x + 1} ****')
        partida(is_campeonato=True)
    print('**** Final do campeonato! ****')
    print(f'Placar: Você {contv} X {contc} Computador')


inicio()
