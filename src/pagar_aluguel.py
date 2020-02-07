from src.tabuleiro import tabuleiro
from src.jogadores import jogadores

def pagar_aluguel(tabuleiro, jogadores, jogador_atual):
    if tabuleiro[jogadores[jogador_atual]['posicao_atual']]['proprietario'] != jogadores[jogador_atual]['nome'] and tabuleiro[jogadores[jogador_atual]['posicao_atual']]['proprietario'] != '':
        print('Amigão, voçê precisa pagar o aluguel para', tabuleiro[jogadores[jogador_atual]['posicao_atual']]['proprietario'])
        print('saldo na conta = ', jogadores[jogador_atual]['caixa'])
        print('valor do aluguel = ', tabuleiro[jogadores[jogador_atual]['posicao_atual']]['valor_aluguel'])
        jogadores[jogador_atual]['caixa'] = jogadores[jogador_atual]['caixa'] - tabuleiro[jogadores[jogador_atual]['posicao_atual']]['valor_aluguel']
        print('SALDO ATUAL = ',jogadores[jogador_atual]['caixa'])

        if tabuleiro[jogadores[jogador_atual]['posicao_atual']]['proprietario'] == 'Impulsivo':
            for id, info in jogadores.items():
                if info['nome'] == 'Impulsivo':
                    info['caixa'] += tabuleiro[jogadores[jogador_atual]['posicao_atual']]['valor_aluguel']

        if tabuleiro[jogadores[jogador_atual]['posicao_atual']]['proprietario'] == 'Exigente':
            for id, info in jogadores.items():
                if info['nome'] == 'Exigente':
                    info['caixa'] += tabuleiro[jogadores[jogador_atual]['posicao_atual']]['valor_aluguel']

        if tabuleiro[jogadores[jogador_atual]['posicao_atual']]['proprietario'] == 'Cauteloso':
            for id, info in jogadores.items():
                if info['nome'] == 'Cauteloso':
                    info['caixa'] += tabuleiro[jogadores[jogador_atual]['posicao_atual']]['valor_aluguel']

        if tabuleiro[jogadores[jogador_atual]['posicao_atual']]['proprietario'] == 'Aleatório':
            for id, info in jogadores.items():
                if info['nome'] == 'Aleatório':
                    info['caixa'] += tabuleiro[jogadores[jogador_atual]['posicao_atual']]['valor_aluguel']


