import random

import pygame


def rodar_dado():
    return random.randint(1, 20)

def resultados_combate():
    rolagem_jogador = rodar_dado()
    rolagem_inimigo = rodar_dado()

    return rolagem_jogador, rolagem_inimigo

def checar_encontro():
    rolagem = rodar_dado()

    if rolagem >= 14:
        return True
    else:
        return False

def gerenciar_combate(tela, texto, tecla):
    tela.blit(texto, (800, 1000))

    if tecla is not None and tecla[pygame.K_e]:
        r_jogador, r_inimigo = resultados_combate()

        if r_jogador > r_inimigo + 1:
            return 'Jogador'
        else:
            return 'Inimigo'
    return None