from random import randint

tabuleiro = {}
for propriedade in range(20):
    custo_venda = randint(250, 500)
    valor_aluguel = randint(40, 400)
    tabuleiro[propriedade] = {
        'custo_venda': custo_venda,
        'valor_aluguel': valor_aluguel,
        'proprietario': ''
    }


def tabuleiro_reset():
    tabuleiro = {}
    for propriedade in range(20):
        custo_venda = randint(250, 500)
        valor_aluguel = randint(40, 400)
        tabuleiro[propriedade] = {
            'custo_venda': custo_venda,
            'valor_aluguel': valor_aluguel,
            'proprietario': ''
        }
    return tabuleiro

