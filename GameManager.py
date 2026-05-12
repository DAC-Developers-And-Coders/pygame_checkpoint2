import pygame

def verificar_sair_menu(tecla_pressionada = None, evento = None):
    if evento is not None:
        x = evento.pos[0]
        y = evento.pos[1]

        if 605 < x < 695 and 321 < y < 360:
            return False

    if tecla_pressionada is not None and tecla_pressionada[pygame.K_RETURN]:
        return False

    return True