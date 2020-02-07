from collections import OrderedDict 
from operator import getitem

from datetime import datetime 
from src.estado import rodadas
from src.jogadores import jogadores
import statistics

def finalizando(tempo_decorrido, resumoA, rodadas, rodadasA, simulacoes, jogadores, tempoMilis, tempoSec, vencedoresA):
    rodadasA.append(rodadas)
    # tempodeA.append('{}'.format(tempo_decorrido))
    tempoMilis.append(tempo_decorrido.microseconds)
    tempoSec.append(tempo_decorrido.total_seconds())
    # x = int(statistics.mean(tempodeA))

    print('Total de rodadas = ', rodadas)
    #print('Tempo decorrido (hh:mm:ss.ms) {}'.format(tempo_decorrido), tempoSec ,tempoMilis)
    print('Tempo decorrido (hh:mm:ss.ms) {}'.format(tempo_decorrido))

    print('###' * 50)
    print('Ganhador(es)')
    for i in jogadores.items():
        print(i)
    print('Perdedor(es)')
    for i in resumoA.items():
        print(i)

    print('###' * 50)
    print('Total de simulações',simulacoes)
    print('###' * 50)
    print('Quantas partidas terminam por time out (1000 jogadas) =', int(rodadasA.count(1000)))
    print('Quantos turnos em média demora uma partida?')
    print('Média de {0} turnos por partida em {1:0.7f} segundos'.format(statistics.median(rodadasA), statistics.median(tempoSec)))
    print('###' * 50)
    print('Qual a porcentagem de vitórias por comportamento dos jogadores')
    print("Impulsivo - Porcentagem de "+"{:.2%} de vitória(s)".format(vencedoresA.count('Impulsivo')/ len(vencedoresA)))
    print("Exigente  - Porcentagem de "+"{:.2%} de vitória(s)".format(vencedoresA.count('Exigente')/ len(vencedoresA)))
    print("Cauteloso - Porcentagem de "+"{:.2%} de vitória(s)".format(vencedoresA.count('Cauteloso')/ len(vencedoresA)))
    print("Aleatório - Porcentagem de "+"{:.2%} de vitória(s)".format(vencedoresA.count('Aleatório')/ len(vencedoresA)))
    print('###' * 50)
    print('Qual o comportamento que mais vence?')
    temp = {0: {'nome': 'Impulsivo'}, 1: {'nome': 'Exigente'},
            2: {'nome': 'Cauteloso'}, 3: {'nome': 'Aleatório'}}
    temp[0]['pertotal'] = (vencedoresA.count('Impulsivo')/ len(vencedoresA))
    temp[1]['pertotal'] = (vencedoresA.count('Exigente')/ len(vencedoresA))
    temp[2]['pertotal'] = (vencedoresA.count('Cauteloso')/ len(vencedoresA))
    temp[3]['pertotal'] = (vencedoresA.count('Aleatório')/ len(vencedoresA))
    ordem = OrderedDict(sorted(temp.items(), key = lambda x: getitem(x[1], 'pertotal'), reverse = True))
    print(next(iter(ordem.values()))['nome'])
    
    #print('Total de rodadas = ', rodadas, rodadasA)
    #print('(hh:mm:ss.ms) {}'.format(tempo_decorrido))
    print('###' * 50)
    #print('total de {} segundos'.format(tempo_decorrido.total_seconds()))
    #print('Média {0:.0f} rodadas a média de tempo média de (hh:mm:ss.ms) hh:mm:ss.{0:.0f}'.format(statistics.median(rodadasA) , statistics.median(tempoMilis)))




'''
import statistics

data = ['']

x = int(statistics.mean(tempodeA))
print(x)
'''