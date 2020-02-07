import random

#ordem_jogadores = [0,1,2,3]
#random.shuffle(ordem_jogadores)

# jogadores = {ordem_jogadores[0]: {'nome': 'Impulsivo'}, ordem_jogadores[1]: {'nome': 'Exigente'},
#             ordem_jogadores[2]: {'nome': 'Cauteloso'}, ordem_jogadores[3]: {'nome': 'Aleatório'}}

jogadores = {0: {'nome': 'Impulsivo'}, 1: {'nome': 'Exigente'},
            2: {'nome': 'Cauteloso'}, 3: {'nome': 'Aleatório'}}

nomes = ['Impulsivo', 'Exigente', 'Cauteloso', 'Aleatório']
random.shuffle(nomes)

for jogador in jogadores:
    jogadores[jogador].update(
        caixa=300, posicao_atual=-1, propriedades=[], jogadas=0, start='', nome=nomes[jogador])

jogadores[0]['start'] = True

def jogadores_reset():
    jogadores = {0: {'nome': 'Impulsivo'}, 1: {'nome': 'Exigente'},
            2: {'nome': 'Cauteloso'}, 3: {'nome': 'Aleatório'}}

    nomes = ['Impulsivo', 'Exigente', 'Cauteloso', 'Aleatório']
    random.shuffle(nomes)

    for jogador in jogadores:
        jogadores[jogador].update(
            caixa=300, posicao_atual=-1, propriedades=[], jogadas=0, start='', nome=nomes[jogador])

    jogadores[0]['start'] = True

    return jogadores
    


