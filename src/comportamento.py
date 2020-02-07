from random import randint

from src.tabuleiro import tabuleiro
from src.jogadores import jogadores


def impulsivo(tabuleiro, jogadores, jogador_atual):
    if tabuleiro[jogadores[jogador_atual]['posicao_atual']]['proprietario'] != jogadores[jogador_atual]['nome'] \
        and jogadores[jogador_atual]['caixa'] > tabuleiro[jogadores[jogador_atual]['posicao_atual']]['custo_venda']:
        print('Jogador = ', jogadores[jogador_atual]['nome'])
        print('saldo na conta = ', jogadores[jogador_atual]['caixa'])
        print('valor do imovel = ',
              tabuleiro[jogadores[jogador_atual]['posicao_atual']]['custo_venda'])
        print('A propriedade é do =',
              tabuleiro[jogadores[jogador_atual]['posicao_atual']]['proprietario'])
        print('---' * 50)
        print('Propriedade pode ser comprada')
        print('---' * 50)

        jogadores[jogador_atual]['caixa'] = (
            jogadores[jogador_atual]['caixa'] - tabuleiro[jogadores[jogador_atual]['posicao_atual']]['custo_venda'])
        jogadores[jogador_atual]['propriedades'].append(
            jogadores[jogador_atual]['posicao_atual'])
        tabuleiro[jogadores[jogador_atual]['posicao_atual']
                  ]['proprietario'] = jogadores[jogador_atual]['nome']
        print('Propriedade comprada!!!')

        print('---' * 50)
        print('NOVO SALDO = ', jogadores[jogador_atual]['caixa'])
        print('Total de propriedades = ', len(
            jogadores[jogador_atual]['propriedades']))
        print('Detalhes = ', jogadores[jogador_atual])
        print('---' * 50)


def exigente(tabuleiro, jogadores, jogador_atual):
    if tabuleiro[jogadores[jogador_atual]['posicao_atual']]['proprietario'] != jogadores[jogador_atual]['nome'] \
        and jogadores[jogador_atual]['caixa'] > tabuleiro[jogadores[jogador_atual]['posicao_atual']]['custo_venda'] \
            and tabuleiro[jogadores[jogador_atual]['posicao_atual']]['valor_aluguel'] > 50:
        print('Jogador = ', jogadores[jogador_atual]['nome'])
        print('saldo na conta = ', jogadores[jogador_atual]['caixa'])
        print('valor do imovel = ',
              tabuleiro[jogadores[jogador_atual]['posicao_atual']]['custo_venda'])
        print('A propriedade é do =',
              tabuleiro[jogadores[jogador_atual]['posicao_atual']]['proprietario'])
        print('---' * 50)
        print('Propriedade pode ser comprada')
        print('---' * 50)

        jogadores[jogador_atual]['caixa'] = (
            jogadores[jogador_atual]['caixa'] - tabuleiro[jogadores[jogador_atual]['posicao_atual']]['custo_venda'])
        jogadores[jogador_atual]['propriedades'].append(
            jogadores[jogador_atual]['posicao_atual'])
        tabuleiro[jogadores[jogador_atual]['posicao_atual']
                  ]['proprietario'] = jogadores[jogador_atual]['nome']
        print('Propriedade comprada!!!')

        print('---' * 50)
        print('NOVO SALDO = ', jogadores[jogador_atual]['caixa'])
        print('Total de propriedades = ', len(
            jogadores[jogador_atual]['propriedades']))
        print('Detalhes = ', jogadores[jogador_atual])
        print('---' * 50)


def cauteloso(tabuleiro, jogadores, jogador_atual):
    if tabuleiro[jogadores[jogador_atual]['posicao_atual']]['proprietario'] != jogadores[jogador_atual]['nome'] \
        and jogadores[jogador_atual]['caixa'] > tabuleiro[jogadores[jogador_atual]['posicao_atual']]['custo_venda'] \
            and jogadores[jogador_atual]['caixa'] - tabuleiro[jogadores[jogador_atual]['posicao_atual']]['custo_venda'] >= 80:
        print('Jogador = ', jogadores[jogador_atual]['nome'])
        print('saldo na conta = ', jogadores[jogador_atual]['caixa'])
        print('valor do imovel = ',
              tabuleiro[jogadores[jogador_atual]['posicao_atual']]['custo_venda'])
        print('A propriedade é do =',
              tabuleiro[jogadores[jogador_atual]['posicao_atual']]['proprietario'])
        print('---' * 50)
        print('Propriedade pode ser comprada')
        print('---' * 50)

        jogadores[jogador_atual]['caixa'] = (
            jogadores[jogador_atual]['caixa'] - tabuleiro[jogadores[jogador_atual]['posicao_atual']]['custo_venda'])
        jogadores[jogador_atual]['propriedades'].append(
            jogadores[jogador_atual]['posicao_atual'])
        tabuleiro[jogadores[jogador_atual]['posicao_atual']
                  ]['proprietario'] = jogadores[jogador_atual]['nome']
        print('Propriedade comprada!!!')

        print('---' * 50)
        print('NOVO SALDO = ', jogadores[jogador_atual]['caixa'])
        print('Total de propriedades = ', len(
            jogadores[jogador_atual]['propriedades']))
        print('Detalhes = ', jogadores[jogador_atual])
        print('---' * 50)

def aleatorio(tabuleiro, jogadores, jogador_atual):
    if tabuleiro[jogadores[jogador_atual]['posicao_atual']]['proprietario'] != jogadores[jogador_atual]['nome'] \
        and jogadores[jogador_atual]['caixa'] > tabuleiro[jogadores[jogador_atual]['posicao_atual']]['custo_venda'] \
            and randint(0, 1) == 1:
        print('Jogador = ', jogadores[jogador_atual]['nome'])
        print('saldo na conta = ', jogadores[jogador_atual]['caixa'])
        print('valor do imovel = ',
              tabuleiro[jogadores[jogador_atual]['posicao_atual']]['custo_venda'])
        print('A propriedade é do =',
              tabuleiro[jogadores[jogador_atual]['posicao_atual']]['proprietario'])
        print('---' * 50)
        print('Propriedade pode ser comprada')
        print('---' * 50)

        jogadores[jogador_atual]['caixa'] = (
            jogadores[jogador_atual]['caixa'] - tabuleiro[jogadores[jogador_atual]['posicao_atual']]['custo_venda'])
        jogadores[jogador_atual]['propriedades'].append(
            jogadores[jogador_atual]['posicao_atual'])
        tabuleiro[jogadores[jogador_atual]['posicao_atual']
                  ]['proprietario'] = jogadores[jogador_atual]['nome']
        print('Propriedade comprada!!!')

        print('---' * 50)
        print('NOVO SALDO = ', jogadores[jogador_atual]['caixa'])
        print('Total de propriedades = ', len(
            jogadores[jogador_atual]['propriedades']))
        print('Detalhes = ', jogadores[jogador_atual])
        print('---' * 50)