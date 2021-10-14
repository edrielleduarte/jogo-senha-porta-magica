import sys


def saudacoes():
    print('Olá jogador, seja bem-vindo ao jogo Senha da Porta Magica\n'
          'O guerreiro terá 7 chances para acertar ou você irá perder ocasionando sua morte!\n'
          'O Oráculo diz uma DICA se o número escolhido pelo guerreiro é:\n'
          'MAIOR que o Segredo da porta ou MENOR que o Segredo da porta.\n '
          'Preparado? 1 = SIM e 2 = NÃO')
    escolha = int(input('Digite sua escolha: '))

    if escolha == 1:
        print('Que bom que você aceitou jogar, simbora?')

    elif escolha == 2:
        print('Que pena que não aceitou, quem sabe na próxima! By, by!')
        sys.exit()
    else:
        print('É necessário fazer uma escolha')
        return


def novo_jogo():
    jogar_novamente = input("Jogar novamente? Infomre um sim, é só digitar: ")

    if jogar_novamente.strip().lower() in ["s", "si", "sim"]:
        return saudacoes()

    print("Até a próxima!")
    sys.exit()


def checagem_palpite_user(palpite, segredo_senha):
    if palpite > segredo_senha:
        print(f'Jogador, você digitou um palpite {palpite} alto do segredo da senha!')
    elif palpite < segredo_senha:
        print(f'Jogador, o numero digitado {palpite} esta muito baixo')
    else:
        print(f'Parabéns, o seu palpite {palpite} é a senha correta você acertou!')
        return True
    return False


def palpite_em_int(palpite):
    try:
        palpite = int(palpite)
        return palpite
    except ValueError:
        return None
