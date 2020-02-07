from src.jogadores import jogadores
from src.estado import jogador_atual, resumoA
from src.tabuleiro import tabuleiro



def excluir_jogador(jogadores, jogador_atual, tabuleiro, resumoA):
    if jogadores[jogador_atual]['caixa'] < 0:
        print('O jogador', jogadores[jogador_atual]['nome'], 'perdeu e sera removido!!!')

        for id, info in tabuleiro.items():
            if info['proprietario'] == jogadores[jogador_atual]['nome']:
                info['proprietario'] = ''

        resumoA[jogador_atual].update(jogadores.pop(jogador_atual))
    
        # if jogador_atual == 3:
        #     resumoA[jogador_atual].update(jogadores.pop(jogador_atual))
        #     #jogador_atual = 0
        #     print(resumoA)

        # elif jogador_atual == 0 or 1 or 2:
        #     resumoA[jogador_atual].update(jogadores.pop(jogador_atual))
        #     #jogador_atual += 1
        #     #jogadores[jogador_atual]['jogadas'] += 1
        #     print(resumoA)
    