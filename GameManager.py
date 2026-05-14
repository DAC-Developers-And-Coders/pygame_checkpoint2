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

def verificar_cores_botoes(mouse_pos):
    if 882 < mouse_pos[0] < 1028 and 543 < mouse_pos[1] < 586:
        return 0, True
    elif 902 < mouse_pos[0] < 1007 and 603 < mouse_pos[1] < 647:
        return 1, True
    else:
        return None

def gerenciar_menu(botoes, fonte_geral, CINZA, BRANCO, PRETO, tela, menu_image, texto_menu):
    trocar_cor_botoes = verificar_cores_botoes(pygame.mouse.get_pos())
    if trocar_cor_botoes is not None:
        if trocar_cor_botoes[0] == 0 and trocar_cor_botoes[1]:
            botoes[0] = fonte_geral.render("Jogar", True, CINZA)
        elif trocar_cor_botoes[0] == 1 and trocar_cor_botoes[1]:
            botoes[1] = fonte_geral.render("Sair", True, CINZA)
    else:
        botoes[0] = fonte_geral.render("Jogar", True, BRANCO)
        botoes[1] = fonte_geral.render("Sair", True, BRANCO)

    tela.fill(PRETO)
    tela.blit(menu_image, (236, 0))
    tela.blit(texto_menu, (860, 400))
    tela.blit(botoes[0], (880, 540))
    tela.blit(botoes[1], (900, 600))