import random

def rodar_dado():
    return random.randint(1, 20)


def combate(jogador, inimigo):
    rolagem_jogador = rodar_dado()
    rolagem_inimigo = rodar_dado()

    if rolagem_jogador > rolagem_inimigo:
        inimigo['hp'] -= 1
    elif rolagem_jogador < rolagem_inimigo:
        jogador['hp'] -= 1
    return rolagem_jogador, rolagem_inimigo

def checar_encontro():
    rolagem = rodar_dado()

    if rolagem >= 14:
        return True
    else:
        return False