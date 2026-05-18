import pygame
import sys

from GameManager import verificar_tecla_pressionada
from GameManager import verificar_segundo_andar
from GameManager import verificar_iniciar_jogo
from GameManager import verificar_sair_jogo
from GameManager import verificar_cozinha
from GameManager import verificar_porao
from GameManager import gerenciar_menu
from GameManager import verificar_sala

pygame.init()

#CONFIG GERAL
LARGURA = 1920
ALTURA = 1080
BRANCO = (255,255,255)
CINZA = (128, 128, 128)
PRETO = (0,0,0)

tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption("CP2")

clock = pygame.time.Clock()
fonte_menu = pygame.font.Font('./fonts/NightsideDemoRegular.ttf', 100)
fonte_geral = pygame.font.Font('./fonts/DevilCandle.otf', 50)

texto_menu = fonte_menu.render("FAITH", True, BRANCO)

botoes = [fonte_geral.render("Jogar", True, BRANCO), fonte_geral.render("Sair", True, BRANCO)]

#IMAGENS
porao = pygame.image.load("./images/basement.png").convert()
cozinha = pygame.image.load("./images/kitchen.png").convert()
sala = pygame.image.load("./images/living-room.png").convert()
menu_image = pygame.image.load("./images/house-exterior.png").convert()
hall_entrada = pygame.image.load("./images/entrance-hall.png").convert()
corredor_andar2 = pygame.image.load("./images/upstairs-hallway.png").convert()

no_menu = True
na_sala = False
no_porao = False
na_cozinha = False
no_segundo_andar = False
no_primeiro_andar = False

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if no_menu and evento.type == pygame.MOUSEBUTTONDOWN:
            no_menu = verificar_iniciar_jogo(None, evento)

            if not no_menu:
                no_primeiro_andar = True
            else:
                verificar_sair_jogo(evento)
        elif not no_menu and not na_sala and not na_cozinha and not no_porao and no_primeiro_andar and evento.type == pygame.MOUSEBUTTONDOWN:
            no_segundo_andar = verificar_segundo_andar(evento)
            na_sala = verificar_sala(evento)
            na_cozinha = verificar_cozinha(evento)
            no_porao = verificar_porao(evento)

            if no_segundo_andar or na_sala or na_cozinha or no_porao:
                no_primeiro_andar = False

    tecla_pressionada = pygame.key.get_pressed()

    if no_menu:
        no_menu = verificar_iniciar_jogo(tecla_pressionada)
        na_sala, no_primeiro_andar, no_segundo_andar, na_cozinha, no_porao = False, False, False, False, False
        if not no_menu:
            no_primeiro_andar = True
        gerenciar_menu(botoes, fonte_geral, CINZA, BRANCO, PRETO, tela, menu_image, texto_menu)
    elif no_primeiro_andar:
        no_menu = verificar_tecla_pressionada(tecla_pressionada, True)
        if no_menu:
            no_primeiro_andar = False
        tela.blit(hall_entrada, (236, 0))
    elif na_sala:
        no_menu = verificar_tecla_pressionada(tecla_pressionada, True)
        tela.blit(sala, (236, 0))
    elif na_cozinha:
        no_menu = verificar_tecla_pressionada(tecla_pressionada, True)
        tela.blit(cozinha, (236, 0))
    elif no_porao:
        no_menu = verificar_tecla_pressionada(tecla_pressionada, True)
        tela.blit(porao, (236, 0))
    elif no_segundo_andar:
        no_menu = verificar_tecla_pressionada(tecla_pressionada, True)
        tela.blit(corredor_andar2, (236, 0))

    pygame.display.flip()
    clock.tick(60)
