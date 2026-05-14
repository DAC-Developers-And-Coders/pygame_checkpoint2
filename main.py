import pygame
import sys

from GameManager import verificar_tecla_pressionada
from GameManager import verificar_iniciar_jogo
from GameManager import verificar_sair_jogo
from GameManager import gerenciar_menu

pygame.init()

#CONFIG GERAL
LARGURA = 1920
ALTURA = 1080
BRANCO = (255,255,255)
CINZA = (128, 128, 128)
PRETO = (0,0,0)

tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption("CP2")

clock = pygame.time.Clock()
fonte_menu = pygame.font.Font('./fonts/NightsideDemoRegular.ttf', 100)
fonte_geral = pygame.font.Font('./fonts/DevilCandle.otf', 50)

texto_menu = fonte_menu.render("FAITH", True, BRANCO)

botoes = [fonte_geral.render("Jogar", True, BRANCO), fonte_geral.render("Sair", True, BRANCO)]

#IMAGENS
menu_image = pygame.image.load("./images/house-exterior.png").convert()
hall_entrada = pygame.image.load("./images/entrance-hall.png").convert()

no_menu = True

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if no_menu and evento.type == pygame.MOUSEBUTTONDOWN:
            no_menu = verificar_iniciar_jogo(None, evento)

            if no_menu:
                verificar_sair_jogo(evento)

    tecla_pressionada = pygame.key.get_pressed()

    if no_menu:
        no_menu = verificar_iniciar_jogo(tecla_pressionada)
        gerenciar_menu(botoes, fonte_geral, CINZA, BRANCO, PRETO, tela, menu_image, texto_menu)
    else:
        no_menu = verificar_tecla_pressionada(tecla_pressionada, True)
        tela.blit(hall_entrada, (236, 0))

    pygame.display.flip()
    clock.tick(60)
