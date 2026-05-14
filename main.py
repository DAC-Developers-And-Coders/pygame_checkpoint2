import pygame
import sys

from GameManager import verificar_tecla_pressionada
from GameManager import verificar_iniciar_jogo
from GameManager import verificar_sair_jogo

pygame.init()

#CONFIG GERAL
LARGURA = 1920
ALTURA = 1080
BRANCO = (255,255,255)
PRETO = (0,0,0)

tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption("CP2")

clock = pygame.time.Clock()
fonte_menu = pygame.font.Font('./fonts/NightsideDemoRegular.ttf', 100)
fonte_geral = pygame.font.Font('./fonts/DevilCandle.otf', 50)

texto_menu = fonte_menu.render("FAITH", True, BRANCO)
botao_jogar = fonte_geral.render("Jogar", True, BRANCO)
botao_sair = fonte_geral.render("Sair", True, BRANCO)

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
        tela.fill(PRETO)
        tela.blit(menu_image, (236,0))
        tela.blit(texto_menu, (860, 400))
        tela.blit(botao_jogar, (880, 540))
        tela.blit(botao_sair, (900, 600))
    else:
        no_menu = verificar_tecla_pressionada(tecla_pressionada, True)
        tela.blit(hall_entrada, (236, 0))

    pygame.display.flip()
    clock.tick(60)
