from random import randint

from src.tabuleiro import tabuleiro
from src.jogadores import jogadores

resumoA = {0: {'nome': ''}, 1: {'nome': ''},
           2: {'nome': ''}, 3: {'nome': ''}}

total_jogadas = 0
jogador_atual = randint(0, 3)
tempoSec = []
timeout = []
tempodeA = []
vencedoresA = []
rodadasA = []
rodadas = -1

def estado_reset():
    resumoA = {0: {'nome': ''}, 1: {'nome': ''},
               2: {'nome': ''}, 3: {'nome': ''}}

    total_jogadas = 0
    jogador_atual = randint(0, 3)

    return resumoA
