import pygame
import sys

import assets as ast
import constants as const

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

def verificar_quarto_filha_foto(evento):
    if evento is not None:
        x, y = evento.pos
        if 450 < x < 510 and 360 < y < 410:
            return True
    return False

def verificar_mesa_quarto_filha(evento):
    if evento is not None:
        x, y = evento.pos
        if 1420 < x < 1500 and 560 < y < 631:
            return True
    return False

def verificar_mesa_quarto_pais(evento):
    if evento is not None:
        x, y = evento.pos
        if 1070 < x < 1196 and 525 < y < 586:
            return True
    return False

def verificar_parede_sala(evento):
    if evento is not None:
        x, y = evento.pos
        if 1050 < x < 1140 and 370 < y < 500:
            return True
    return False

def verificar_cruz_esquerda(evento):
    if evento is not None:
        x, y = evento.pos
        if 610 < x < 660 and 350 < y < 410:
            return True
    return False

def verificar_cruz_meio(evento):
    if evento is not None:
        x, y = evento.pos
        if 900 < x < 940 and 430 < y < 462:
            return True
    return False

def verificar_cruz_direita(evento):
    if evento is not None:
        x, y = evento.pos
        if 1290 < x < 1360 and 290 < y < 350:
            return True
    return False

def verificar_armario_porao(evento):
    if evento is not None:
        x, y = evento.pos
        if 590 < x < 640 and 440 < y < 520:
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

def verificar_retornar(evento, quarto):
    if evento is not None:
        x, y = evento.pos
        if quarto == 'Sala' or quarto == 'SegundoAndar' or quarto == 'Sotao':
            if 236 < x < 1684 and 986 < y < 1080:
                return True
        elif quarto == 'Cozinha':
            if 947 < x < 1159 and 186 < y < 563:
                return True
        elif quarto == 'Porao':
            if 1069 < x < 1294 and 295 < y < 535:
                return True
        elif quarto == 'QuartoPais':
            if 560 < x < 761 and 200 < y < 775:
                return True
        elif quarto == 'QuartoFilha':
            if 1007 < x < 1294 and 129 < y < 773:
                return True
    return False

def gerenciar_menu(tela, menu_image):
    trocar_cor_botoes = verificar_cores_botoes(pygame.mouse.get_pos())
    if trocar_cor_botoes is not None:
        if trocar_cor_botoes[0] == 0 and trocar_cor_botoes[1]:
            ast.botoes[0] = ast.fonte_geral.render('Jogar', True, const.CINZA)
        elif trocar_cor_botoes[0] == 1 and trocar_cor_botoes[1]:
            ast.botoes[1] = ast.fonte_geral.render('Sair', True, const.CINZA)
    else:
        ast.botoes[0] = ast.fonte_geral.render('Jogar', True, const.BRANCO)
        ast.botoes[1] = ast.fonte_geral.render('Sair', True, const.BRANCO)

    tela.fill(const.PRETO)
    tela.blit(menu_image, (236, 0))
    tela.blit(ast.texto_menu, (782, 400))
    tela.blit(ast.botoes[0], (880, 540))
    tela.blit(ast.botoes[1], (900, 600))

def gerenciar_tela(tela, imagem, lugar = None):
    if lugar != 'Sala':
        tela.blit(imagem, (236, 0))
    else:
        tela.fill((0, 0, 0))
        tela.blit(imagem, (259, 0))