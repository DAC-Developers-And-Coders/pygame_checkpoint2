import pygame
import sys

pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('The Visit')

import GameManager as gm
import game_state as gs
import combat as cm

from map import lugar_atual, overlay_ativo, lugares
from constants import *
from assets import *

clock = pygame.time.Clock()

try:
    pygame.mixer.music.load('./sfx/menu_music.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)
except pygame.error as e:
    print(f'Erro ao carregar musica {e}')

def mudar_musica_menu(iniciou = False):
    pygame.mixer.music.stop()

    if iniciou or lugar_atual != MENU:
        pygame.mixer.music.load(som_ambiente)
    else:
        pygame.mixer.music.load('./sfx/menu_music.mp3')

    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

        if overlay_ativo is not None:
            overlay = lugares[lugar_atual][overlay_ativo]

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if overlay['fechar'].collidepoint(evento.pos):
                    overlay_ativo = None
            continue

        if evento.type == pygame.MOUSEBUTTONDOWN and gs.pode_clicar:
            if lugar_atual == MENU:
                if not gm.verificar_iniciar_jogo(None, evento):
                    gs.pode_clicar = False
                    som_porta_menu.play()
                    mudar_musica_menu(True)
                    gs.timer = [pygame.time.get_ticks(), INICIO]
                else:
                    gm.verificar_sair_jogo(evento)

            elif lugar_atual == INICIO:
                if gm.verificar_segundo_andar(evento):
                    som_escada.play()
                    gs.pode_clicar = False
                    gs.timer = [pygame.time.get_ticks(), SEGUNDO_ANDAR]
                elif gm.verificar_sala(evento):
                    lugar_atual = SALA
                    som_porta_geral.play()
                    gs.garota_spawn = cm.checar_encontro()
                elif gm.verificar_cozinha(evento):
                    som_passos.play()
                    gs.pode_clicar = False
                    gs.timer = [pygame.time.get_ticks(), COZINHA]
                elif gm.verificar_porao(evento):
                    som_passos.play()
                    gs.pode_clicar = False
                    gs.timer = [pygame.time.get_ticks(), PORAO]

            elif lugar_atual == SEGUNDO_ANDAR:
                if gm.verificar_sotao(evento):
                    som_passos.play()
                    gs.pode_clicar = False
                    gs.timer = [pygame.time.get_ticks(), SOTAO]
                elif gm.verificar_quarto_pais(evento):
                    lugar_atual = QUARTO_PAIS
                    som_porta_geral.play()
                    gs.garota_spawn = cm.checar_encontro()
                elif gm.verificar_quarto_filha(evento):
                    lugar_atual = QUARTO_FILHA
                    som_porta_geral.play()
                    gs.garota_spawn = cm.checar_encontro()
                elif gm.verificar_retornar(evento, SEGUNDO_ANDAR):
                    som_escada.play()
                    gs.pode_clicar = False
                    gs.timer = [pygame.time.get_ticks(), INICIO]

            elif lugar_atual == SALA:
                if gm.verificar_parede_sala(evento):
                    overlay_ativo = 'overlay_foto_familia'
                elif gm.verificar_retornar(evento, SALA):
                    lugar_atual = INICIO

            elif lugar_atual == COZINHA:
                if gm.verificar_retornar(evento, COZINHA):
                    lugar_atual = INICIO
                    som_porta_geral.play()

            elif lugar_atual == PORAO:
                if gm.verificar_armario_porao(evento):
                    overlay_ativo = 'overlay_documento_padre'
                elif gm.verificar_retornar(evento, PORAO):
                    lugar_atual = INICIO

            elif lugar_atual == SOTAO:
                if gm.verificar_cruz_esquerda(evento):
                    overlay_ativo = 'overlay_mary'
                elif gm.verificar_cruz_meio(evento):
                    overlay_ativo = 'overlay_rosalia'
                elif gm.verificar_cruz_direita(evento):
                    overlay_ativo = 'overlay_william'
                elif gm.verificar_retornar(evento, SOTAO):
                    lugar_atual = SEGUNDO_ANDAR

            elif lugar_atual == QUARTO_PAIS:
                if gm.verificar_mesa_quarto_pais(evento):
                    overlay_ativo = 'overlay_foto_garota'
                elif gm.verificar_retornar(evento, QUARTO_PAIS):
                    lugar_atual = SEGUNDO_ANDAR

            elif lugar_atual == QUARTO_FILHA:
                if gm.verificar_mesa_quarto_filha(evento):
                    overlay_ativo = 'overlay_diario'
                elif gm.verificar_quarto_filha_foto(evento):
                    overlay_ativo = 'overlay_foto'
                elif gm.verificar_retornar(evento, QUARTO_FILHA):
                    lugar_atual = SEGUNDO_ANDAR

    if gs.timer is not None:
        tempo = pygame.time.get_ticks() - gs.timer[0]
        destino = gs.timer[1]

        if destino == FIM:
            if tempo >= 8000:
                gs.timer = None

                gs.no_fim = False
                lugar_atual = MENU

                gs.jogador['hp'] = gs.jogador['full_hp']
                gs.inimigo['hp'] = gs.inimigo['full_hp']

                gs.garota_spawn = False

                mudar_musica_menu()
                gs.pode_clicar = True
        elif tempo >= 2000:
            gs.timer = None
            lugar_atual = destino
            gs.pode_clicar = True

            if destino in [COZINHA, PORAO, SOTAO]:
                gs.garota_spawn = cm.checar_encontro()
        pygame.event.clear(pygame.MOUSEBUTTONDOWN)

    tecla_pressionada = pygame.key.get_pressed()

    if lugar_atual == MENU:
        gs.garota_spawn = False
        overlay_ativo = None
        gm.gerenciar_menu(tela, imagens['menu_imagem'])

        if not gm.verificar_iniciar_jogo(tecla_pressionada):
            lugar_atual = INICIO
            mudar_musica_menu()

    else:
        lugar = lugares[lugar_atual]

        imagem = lugar['imagem_garota'] if gs.garota_spawn and lugar['imagem_garota'] else lugar['imagem']

        gm.gerenciar_tela(tela, imagem, lugar_atual)

        if overlay_ativo is not None:
            overlay = lugar[overlay_ativo]

            gm.gerenciar_tela(tela, overlay['imagem'])
            tela.blit(texto_x, (overlay['fechar'].x + 12, overlay['fechar'].y + 2))

    if lugar_atual != MENU and not gs.garota_spawn and not gs.no_fim:
        if gm.verificar_tecla_pressionada(tecla_pressionada, True):
            lugar_atual = MENU
            mudar_musica_menu()

    if gs.garota_spawn:
        gs.pode_clicar = False
        ganhador = cm.gerenciar_combate(tela, texto_combate, tecla_pressionada)

        if ganhador is not None:
            if ganhador == 'Jogador':
                gs.inimigo['hp'] -= 1
                som_acerto.play()
                gs.timer_batalha = [pygame.time.get_ticks(), 'Sucesso']
            else:
                gs.jogador['hp'] -= 1
                som_risada.play()
                gs.timer_batalha = [pygame.time.get_ticks(), 'Falha']

            gs.pode_clicar = True
            gs.garota_spawn = False

    if gs.timer_batalha is not None:
        if gs.timer_batalha[1] == 'Sucesso' and pygame.time.get_ticks() - gs.timer_batalha[0] <= 5000:
            tela.blit(fonte_pequena.render(f'Sucesso! Mary:', True, BRANCO), (236, 900))
            tela.blit(fonte_numeros.render(f'{gs.inimigo["hp"]} / {gs.inimigo["full_hp"]}', True, BRANCO), (236, 930))
        elif gs.timer_batalha[1] == 'Falha' and pygame.time.get_ticks() - gs.timer_batalha[0] <= 5000:
            tela.blit(fonte_pequena.render(f'Falha. Você:', True, BRANCO), (236, 900))
            tela.blit(fonte_numeros.render(f'{gs.jogador["hp"]} / {gs.jogador["full_hp"]}', True, BRANCO), (236, 930))

    if gs.no_fim:
        tela.fill(PRETO)
        altura = 100

        if gs.jogador['hp'] <= 0:
            for texto in textos_ruins:
                tela.blit(texto, (236, altura))
                altura += 100
        elif gs.inimigo['hp'] <= 0:
            for texto in textos_bons:
                tela.blit(texto, (236, altura))
                altura += 100

    if gs.jogador['hp'] <= 0 and not gs.no_fim:
        gs.timer = [pygame.time.get_ticks(), FIM]
        gs.pode_clicar = False
        gs.no_fim = True
    elif gs.inimigo['hp'] <= 0 and not gs.no_fim:
        gs.timer = [pygame.time.get_ticks(), FIM]
        gs.pode_clicar = False
        gs.no_fim = True

    pygame.display.flip()
    clock.tick(60)