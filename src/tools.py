def search(lista, term):
    for k, v in lista.items():
        if term in v:
            return k

    return None



jogadores = {0: {'caixa': 63135, 'jogadas': 1001, 'nome': 'Aleatório', 'posicao_atual': 18, 'propriedades': [...], 'start': True}, 3: {'caixa': 133695, 'jogadas': 1001, 'nome': 'Exigente', 'posicao_atual': 5, 'propriedades': [...], 'start': ''}}

jogadores = OrderedDict(sorted(jogadores.items(), key = lambda x: getitem(x[1], 'caixa'), reverse = True))

for i in jogadores.items():
	print(i)

next(iter(jogadores.values()))


from collections import OrderedDict 
from operator import getitem
res = OrderedDict(sorted(jogadores.items(), key = lambda x: getitem(x[1], 'caixa'), reverse = True))
next(iter(desempate.values()))['nome']

                elif len(jogadores) == 1:
                    vencedoresA.append(jogadores[jogador_atual]['nome'])
                    print('---' * 50)
                    print('O JOGADOR', jogadores[jogador_atual]['nome'], 'é o VENCEDOR', vencedoresA)
                    finalizando(tempo_decorrido, resumoA, rodadas, rodadasA, simulacoes, jogadores, tempodeA, tempoSec)


print('The count of i is:', count)
print('The count of i is:', calc*100,'%')

x = 0.25
y = -0.25

vencedoresA = ['a', 'e', 'Impulsivo', 'o', 'Impulsivo', 'Impulsivo', 'Impulsivo', 'Impulsivo', 'Paulo Henrique', 'Paulo Henrique']
count = vencedoresA.count('Impulsivo')
count = vencedoresA.count('Exigente')
count = vencedoresA.count('Cauteloso')
count = vencedoresA.count('Aleatório')

calc = count / len(vencedoresA)

print("Impulsivo - Porcentagem de "+"{:.2%} de vitória(s)".format(vencedoresA.count('Impulsivo')/ len(vencedoresA)))
print("Impulsivo - Porcentagem de "+"{:.2%} de vitória(s)".format(vencedoresA.count('Exigente')/ len(vencedoresA)))
print("Impulsivo - Porcentagem de "+"{:.2%} de vitória(s)".format(vencedoresA.count('Cauteloso')/ len(vencedoresA)))
print("Impulsivo - Porcentagem de "+"{:.2%} de vitória(s)".format(vencedoresA.count('Aleatório')/ len(vencedoresA)))


temp = {0: {'nome': 'Impulsivo'}, 1: {'nome': 'Exigente'},
            2: {'nome': 'Cauteloso'}, 3: {'nome': 'Aleatório'}}

temp[0]['pertotal'] = (vencedoresA.count('Impulsivo')/ len(vencedoresA))
temp[1]['pertotal'] = (vencedoresA.count('Exigente')/ len(vencedoresA))
temp[2]['pertotal'] = (vencedoresA.count('Cauteloso')/ len(vencedoresA))
temp[3]['pertotal'] = (vencedoresA.count('Aleatório')/ len(vencedoresA))

ordem = OrderedDict(sorted(temp.items(), key = lambda x: getitem(x[1], 'pertotal'), reverse = True))
next(iter(temp.values()))['nome']


temp

temp.items()

vencedoresA.append(next(iter(temp.values()))['nome'])
print('O JOGADOR', next(iter(temp.values()))['nome'], 'é o VENCEDOR', vencedoresA)
