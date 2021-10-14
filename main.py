from jogo_porta_magica import saudacoes, novo_jogo, checagem_palpite_user, palpite_em_int


def main():
    global resposta_palpite
    import numpy as np

    saudacoes()

    contador = 0
    rodadas = 7  # Quantidade de rodadas
    segredo_senha = np.random.randint(1, 101, 1)
    print(segredo_senha)

    while contador < rodadas:
        print('Escolha: [1] para jogar ou [0] para sair:')
        resposta = int(input('Digita sua escolha:'))

        if resposta == 1:
            palpite = input('Informe seu palpite entre 1 e 100: ')
            palpite = palpite_em_int(palpite)

            if palpite is None:
                print('iiih amigão, você deve digitar um numero, vamos de novo!')
                continue
            if 1 <= palpite <= 100:
                resposta_palpite = checagem_palpite_user(palpite, segredo_senha)

            if resposta_palpite:
                novo_jogo()
                segredo_senha = np.random.randint(1, 101, 1)

        else:
            print('Pena que não finalizou o jogo!')
            break

        contador += 1
    else:
        print('INFELIZMENTE VOCÊ NÃO CONSEGUIU ACERTAR, FIM DO GAME!')


if __name__ == '__main__':
    main()
