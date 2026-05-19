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

def verificar_segundo_andar(evento):
    if evento is not None:
        x, y = evento.pos
        if 238 < x < 668 and 0 < y < 1015:
            return True
    return False

def verificar_sala(evento):
    if evento is not None:
        x, y = evento.pos
        if 675 < x < 992 and 234 < y < 847:
            return True
    return False

def verificar_cozinha(evento):
    if evento is not None:
        x, y = evento.pos
        if 1365 < x < 1441 and 226 < y < 856:
            return True
    return False

def verificar_porao(evento):
    if evento is not None:
        x, y = evento.pos
        if 1178 < x < 1300 and 313 < y < 777:
            return True
    return False

def verificar_quarto_pais(evento):
    if evento is not None:
        x, y = evento.pos
        if 570 < x < 687 and 282 < y < 936:
            return True
    return False

def verificar_sotao(evento):
    if evento is not None:
        x, y = evento.pos
        if 821 < x < 1099 and 373 < y < 660:
            return True
    return False

def verificar_quarto_filha(evento):
    if evento is not None:
        x, y = evento.pos
        if 1249 < x < 1352 and 282 < y < 936:
            return True
    return False

def verificar_mesa_quarto_filha(evento):
    if evento is not None:
        x, y = evento.pos
        if 1420 < x < 1500 and 560 < y < 631:
            return True
    return False

def verificar_tecla_pressionada(tecla_pressionada, verificando_retorno_menu = False):
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

def verificar_retornar_a1(evento, quarto):
    if evento is not None:
        x, y = evento.pos
        if quarto == 'L' or quarto == 'S' or quarto == 'A':
            if 236 < x < 1684 and 986 < y < 1080:
                return True
        elif quarto == 'K':
            if 947 < x < 1159 and 186 < y < 563:
                return True
        elif quarto == 'B':
            if 1069 < x < 1294 and 295 < y < 535:
                return True
        elif quarto == 'P':
            if 560 < x < 761 and 200 < y < 775:
                return True
        elif quarto == 'D':
            if 1007 < x < 1294 and 129 < y < 773:
                return True
    return False

def gerenciar_menu(botoes, fonte_geral, cinza, branco, preto, tela, menu_image, texto_menu):
    trocar_cor_botoes = verificar_cores_botoes(pygame.mouse.get_pos())
    if trocar_cor_botoes is not None:
        if trocar_cor_botoes[0] == 0 and trocar_cor_botoes[1]:
            botoes[0] = fonte_geral.render("Jogar", True, cinza)
        elif trocar_cor_botoes[0] == 1 and trocar_cor_botoes[1]:
            botoes[1] = fonte_geral.render("Sair", True, cinza)
    else:
        botoes[0] = fonte_geral.render("Jogar", True, branco)
        botoes[1] = fonte_geral.render("Sair", True, branco)

    tela.fill(preto)
    tela.blit(menu_image, (236, 0))
    tela.blit(texto_menu, (860, 400))
    tela.blit(botoes[0], (880, 540))
    tela.blit(botoes[1], (900, 600))

def gerenciar_tela(tela, imagem):
    tela.blit(imagem, (236, 0))