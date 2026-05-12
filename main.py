import pygame
import sys

from GameManager import verificar_sair_menu

pygame.init()

#CONFIG GERAL
LARGURA = 1280
ALTURA = 720
BRANCO = (255,255,255)
PRETO = (0,0,0)

tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption("CP2")

clock = pygame.time.Clock()
fonte_menu = pygame.font.Font('./fonts/NightsideDemoRegular.ttf', 100)
fonte_geral = pygame.font.Font('./fonts/DevilCandle.otf', 30)

texto_menu = fonte_menu.render("FAITH", True, BRANCO)
botao_jogar = fonte_geral.render("Jogar", True, BRANCO)

#IMAGENS
menu_image = pygame.image.load("./images/house-menu.jpeg").convert()

no_menu = True

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if no_menu and evento.type == pygame.MOUSEBUTTONDOWN:
            no_menu = verificar_sair_menu(None, evento)

    tecla_pressionada = pygame.key.get_pressed()

    if no_menu:
        no_menu = verificar_sair_menu(tecla_pressionada)
        tela.blit(menu_image, (24,0))
        tela.blit(texto_menu, (550, 160))
        tela.blit(botao_jogar, (605, 330))
    else:
        tela.fill(PRETO)

    pygame.display.flip()
    clock.tick(60)
