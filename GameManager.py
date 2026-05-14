import pygame
import sys

def verificar_iniciar_jogo(tecla_pressionada = None, evento = None):
    if evento is not None:
        x, y = evento.pos
        if 882 < x < 1028 and 543 < y < 586:
            return False

    if tecla_pressionada is not None and tecla_pressionada[pygame.K_RETURN]:
        return False

    return True

def verificar_sair_jogo(evento):
    if evento is not None:
        x, y = evento.pos
        if 902 < x < 1007 and 603 < y < 647:
            pygame.quit()
            sys.exit()

def verificar_tecla_pressionada(tecla_pressionada, verificando_retorno_menu):
    if tecla_pressionada[pygame.K_ESCAPE] and verificando_retorno_menu:
        return True

    return None